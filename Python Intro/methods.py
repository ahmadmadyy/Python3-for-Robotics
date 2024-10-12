from robot_control_class import RobotControl
import time

rc = RobotControl(robot_name="summit")

def time_straight(x):
    rc.move_straight()
    time.sleep(x)
    rc.stop_robot()

def summit(x,y,z):
    a = rc.get_laser_summit(x)
    b = rc.get_laser_summit(y)
    c = rc.get_laser_summit(z)
    return[a,b,c]

time_straight(5)
a,b,c = summit(0,500,1000)

print("a: ",a)
print("b: ",b)
print("c: ",c)