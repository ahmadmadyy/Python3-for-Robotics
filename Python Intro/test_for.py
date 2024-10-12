from robot_control_class import RobotControl

rc = RobotControl()

l = rc.get_laser_full()

max = 0

for i in l:
    if i>max:
        max = i

print("Max value is: ",max)