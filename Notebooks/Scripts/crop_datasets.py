def crop_dataset(grav_data, topo_data, min_lat, max_lat, min_lon, max_lon):
    """
    Crop the gravity and topography datasets to the specified extent.

    Args:
    - grav_data (pd.DataFrame): DataFrame containing gravity data with columns 'latitude', 'longitude', and 'Free Air Anomalies'.
    - topo_data (pd.DataFrame): DataFrame containing topography data with columns 'latitude', 'longitude', and 'elevation'.
    - min_lat (float): Minimum latitude of the desired extent.
    - max_lat (float): Maximum latitude of the desired extent.
    - min_lon (float): Minimum longitude of the desired extent.
    - max_lon (float): Maximum longitude of the desired extent.

    Returns:
    - cropped_grav_data (pd.DataFrame): Cropped gravity dataset.
    - cropped_topo_data (pd.DataFrame): Cropped topography dataset.
    """
    # Crop gravity data
    cropped_grav_data = grav_data[(grav_data['latitude'] >= min_lat) & (grav_data['latitude'] <= max_lat) &
                                  (grav_data['longitude'] >= min_lon) & (grav_data['longitude'] <= max_lon)]
    
    # Crop topography data
    cropped_topo_data = topo_data[(topo_data['latitude'] >= min_lat) & (topo_data['latitude'] <= max_lat) &
                                  (topo_data['longitude'] >= min_lon) & (topo_data['longitude'] <= max_lon)]
    
    return cropped_grav_data, cropped_topo_data