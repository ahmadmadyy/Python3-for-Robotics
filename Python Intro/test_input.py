from robot_control_class import RobotControl

rc = RobotControl()

num = int(input("Enter a number between 0 and 719 "))

a = rc.get_laser(num)

print("laser: ", a)