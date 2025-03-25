import math

def define_wind_direction(wind_direction_x,wind_direction_y):
    
    wind_direction = ""
    
    if wind_direction_y == 1:
        wind_direction += "S"
    elif wind_direction_y == -1:
        wind_direction += "N"
    
    if wind_direction_x == 1:
        wind_direction += "E"
    elif wind_direction_x == -1:
        wind_direction += "W"
    
    return wind_direction if wind_direction else "X"

def get_score(shoot,radii,points,target_x,target_y):
    mx, my = shoot
    dist = math.sqrt((mx - target_x) ** 2 + (my - target_y) ** 2)
    for i in range(len(radii)):
        if dist <= radii[i]:
            return points[i]
    return 0