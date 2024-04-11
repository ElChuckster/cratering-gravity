import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
def plot_gravity_anomalies(cropped_grav_data, min_lat, max_lat, min_lon, max_lon):
    """
    Plot gravity anomalies over the cropped region of the lunar surface.

    Args:
    - cropped_grav_data (pd.DataFrame): Cropped gravity dataset with columns 'latitude', 'longitude', and 'Free Air Anomalies'.
    - min_lat (float): Minimum latitude of the cropped region.
    - max_lat (float): Maximum latitude of the cropped region.
    - min_lon (float): Minimum longitude of the cropped region.
    - max_lon (float): Maximum longitude of the cropped region.
    """
    # Create latitude and longitude meshgrids
    num_lat_points = 1000
    num_lon_points = 1000
    lat_grid = np.linspace(min_lat, max_lat, num_lat_points)
    lon_grid = np.linspace(min_lon, max_lon, num_lon_points)
    lon_mesh, lat_mesh = np.meshgrid(lon_grid, lat_grid)

    # Interpolate gravity anomalies onto the meshgrid
    grav_mesh = griddata((cropped_grav_data['longitude'], cropped_grav_data['latitude']),
                         cropped_grav_data['Free Air Anomalies'], (lon_mesh, lat_mesh), method='linear')

    # Plot gravity anomalies
    plt.figure(figsize=(10, 6))
    plt.contourf(lon_mesh, lat_mesh, grav_mesh, cmap='viridis')  # You can choose any colormap you like
    plt.colorbar(label='Gravity Anomalies (mgal)')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Free Air Gravity Anomalies over Lunar Surface')
    plt.show()


def plot_topography(cropped_topo_data, min_lat, max_lat, min_lon, max_lon):
    """
    Plot topography over the cropped region of the lunar surface.

    Args:
    - cropped_topo_data (pd.DataFrame): Cropped topography dataset with columns 'latitude', 'longitude', and 'elevation'.
    - min_lat (float): Minimum latitude of the cropped region.
    - max_lat (float): Maximum latitude of the cropped region.
    - min_lon (float): Minimum longitude of the cropped region.
    - max_lon (float): Maximum longitude of the cropped region.
    """
    # Create latitude and longitude meshgrids
    num_lat_points = 100
    num_lon_points = 100
    lat_grid = np.linspace(min_lat, max_lat, num_lat_points)
    lon_grid = np.linspace(min_lon, max_lon, num_lon_points)
    lon_mesh, lat_mesh = np.meshgrid(lon_grid, lat_grid)

    # Interpolate topography onto the meshgrid
    topo_mesh = griddata((cropped_topo_data['longitude'], cropped_topo_data['latitude']),
                         cropped_topo_data['elevation'], (lon_mesh, lat_mesh), method='linear')

    # Plot topography
    plt.figure(figsize=(10, 6))
    plt.contourf(lon_mesh, lat_mesh, topo_mesh, cmap='terrain')  # You can choose any colormap you like
    plt.colorbar(label='Elevation (m)')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Topography of the Lunar Surface')
    plt.show()