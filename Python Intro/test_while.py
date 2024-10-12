from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(360)

while a>1:
    rc.move_straight()
    a = rc.get_laser(360)
rc.stop_robot()

print ("Wall is at %f meters! Stop the robot!" % a)