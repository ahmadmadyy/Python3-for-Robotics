from robot_control_class import RobotControl

rc = RobotControl()

list = rc.get_laser_full()

dict = {"Position 0": list[0],
        "Position 100": list[100],
        "Position 200": list[200],
        "Position 300": list[300], 
        "Position 400": list[400], 
        "Position 500": list[500],
        "Position 600": list[600], 
        "Position 719": list[719]}

print(dict)