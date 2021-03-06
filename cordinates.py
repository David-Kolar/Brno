import geopy
import geopy.distance

x = {"max" : 49.3599973, "min" : 49.060001}
y = {"max" : 16.8399997, "min" : 16.3600013}

def find_min_max_xy(cordinates):
    x_max = y_max = 0
    x_min = y_min = float("inf")
    for key, node in cordinates.items():
        x_min = min(x_min, node["x"])
        x_max = max(x_max, node["x"])
        y_min = min(y_min, node["y"])
        y_max = max(y_max, node["y"])

    return x_max, x_min, y_max, y_min

def count_distance(x1, y1, x2, y2):
    pt1 = geopy.Point(x1, y1)
    pt2 = geopy.Point(x2, y2)
    dist = geopy.distance.distance(pt1, pt2).m
    return dist

def is_it_in_interval(a, a1, a2):
    return (a1 <= a <= a2)
