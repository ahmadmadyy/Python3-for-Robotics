from robot_control_class import RobotControl

rc = RobotControl()

laser1 = rc.get_laser(360)
print("laser1: ",laser1)

laser2 = rc.get_laser(400)
print("laser2: ",laser2)

laser2 = rc.get_laser(410)
print("laser2: ",laser2)