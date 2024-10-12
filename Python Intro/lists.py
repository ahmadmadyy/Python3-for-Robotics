from robot_control_class import RobotControl

rc = RobotControl()

list = rc.get_laser_full()

print("Position 0: ", list[0])
print("Position 360: ", list[360])
print("Position 719: ", list[719])
