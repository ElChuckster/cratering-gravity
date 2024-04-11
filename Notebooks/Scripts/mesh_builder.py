#import statements
import numpy as np
from scipy.interpolate import LinearNDInterpolator
import matplotlib as mpl
import matplotlib.pyplot as plt
import os

from discretize import TensorMesh
from discretize.utils import mkvc, active_from_xyz

from SimPEG.utils import plot2Ddata, model_builder
from SimPEG import maps
from SimPEG.potential_fields import gravity

def get_mesh_from_topo(x_topo, y_topo, z_topo, n_rec):
    x_topo, y_topo, z_topo = mkvc(x_topo), mkvc(y_topo), mkvc(z_topo)
    topo_xyz = np.c_[x_topo, y_topo,z_topo]
    


    # extent_x = 2*x_topo.max() 
    # extent_y = 2*y_topo.max()
    # extent_z = z_topo.max()
    # dx = 5
    # dy = 5
    # dz = 5
    # nx = int(np.ceil(extent_x / dx))
    # ny = int(np.ceil(extent_y / dy))
    # nz = int(np.ceil(extent_z / dz))

    # hx = np.ones(nx) * dx
    # hy = np.ones(ny) * dy
    # hz = np.ones(nz) * dz
    # origin = np.array([-extent_x / 2, -extent_y / 2, 0])
    # mesh = TensorMesh([hx, hy, hz], origin=origin)
    

    dh = 5.0 * 1000
    dh_z = 1.25 * 25
    hx = [(dh, 5, -1.3), (dh, 40), (dh, 5, 1.3)]
    hy = [(dh, 5, -1.3), (dh, 40), (dh, 5, 1.3)]
    hz = [(dh_z, 15, -1.3)]
    
    middle_x = len(x_topo) // 2  # Get the index of the middle element
    middle_valx = x_topo[middle_x]

    middle_y = len(y_topo) // 2  # Get the index of the middle element
    middle_valy = y_topo[middle_y]


    mesh = TensorMesh([hx, hy, hz])

    # Determine the desired location for the origin
    mesh.origin = np.array([x_topo.min(), y_topo.min(), z_topo.min()])  # Adjust these coordinates as needed

    # Set the origin of the mesh
   # mesh.origin = origin_location



    print("Origin: {}".format(mesh.origin))


    x_rx = np.linspace(x_topo.min(), x_topo.max(), n_rec)
    y_rx = np.linspace(y_topo.min(), y_topo.max(), n_rec)
    x_rx, y_rx = np.meshgrid(x_rx, y_rx)
    x_rx, y_rx = mkvc(x_rx.T), mkvc(y_rx.T)
    fun_interp = LinearNDInterpolator(np.c_[x_topo, y_topo], z_topo)
    z_rx = fun_interp(np.c_[x_rx, y_rx]) + 5.0
    z_rx = np.ones_like(x_rx)*100
    receiver_locations = np.c_[x_rx, y_rx, z_rx]

    components = ["gz"]

    receiver_list = gravity.receivers.Point(receiver_locations, components=components)

    receiver_list = [receiver_list]

    source_field = gravity.sources.SourceField(receiver_list=receiver_list)

    survey = gravity.survey.Survey(source_field)
    
    return survey, topo_xyz, mesh, receiver_list

def get_dpred_from_sim(background_density_air, background_density_ground, topo_xyz, mesh, survey):
    # Create density model arrays with appropriate values for ground and air cells
    model_ground = background_density_ground * np.ones(mesh.nC)
    model_air = background_density_air * np.ones(mesh.nC)

    # Define which cells are considered active (both ground and air cells)
    active_cells_all = np.ones(mesh.nC, dtype=bool)

    # Find indices of ground cells below the surface
    active_cells_ground = active_from_xyz(mesh, topo_xyz)

    # Set the density values for ground cells
    model_ground[active_cells_ground == True] = background_density_ground

    # Set the density values for air cells
    model_ground[active_cells_ground == False] = background_density_air

    # Combine density models for ground and air cells
    #model_combined = np.where(active_cells_ground, model_ground, model_air)

    # Create a mapping for the combined density model
    model_map_combined = maps.IdentityMap(nP=mesh.nC)

    # Run simulation for ground and air cells combined
    simulation_all = gravity.simulation.Simulation3DIntegral(
        survey=survey,
        mesh=mesh,
        rhoMap=model_map_combined,
        ind_active=active_cells_all,
        store_sensitivities="forward_only",
    )

    # Calculate predicted data for ground and air cells combined
    dpred_all = simulation_all.dpred(model_ground)
    return dpred_all, active_cells_all, model_ground
