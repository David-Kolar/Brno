import geopy

def find_min_max_xy(cordinates):
    x_max = y_max = 0
    x_min = y_min = float("inf")
    for key, node in cordinates.items():
        x_min = min(x_min, node["x"])
        x_max = max(x_max, node["x"])
        y_min = min(y_min, node["y"])
        y_max = max(y_max, node["y"])

    return (x_min, x_max), (y_min, y_max)