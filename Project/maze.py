from robot_control_class import RobotControl
import time

class MoveRobot():
    def __init__(self, speed, time):
        self.robotcontrol = RobotControl()
        self.clockwise = "clockwise"
        self.speed = speed
        self.time = time
        self.turn_speed = 0.8
        self.turn_time = 1
        self.safety_value_f = 1

    def move(self):
        laser = self.get_laser_value(360)
        while laser>self.safety_value_f:
            self.robotcontrol.move_straight()
            laser = mv1.get_laser_value(360)
        self.stop_robot()

    def rotate(self):
        laser = self.get_laser_value(360)
        laser_r = self.robotcontrol.get_laser(180)
        laser_l = self.robotcontrol.get_laser(540)
        if laser_r > laser_l:
            while laser < self.safety_value_f:
                self.robotcontrol.turn(self.clockwise, self.turn_speed, self.turn_time)
                laser = mv1.get_laser_value(360)
        else:
            while laser < self.safety_value_f:
                self.robotcontrol.turn("aclockwise", self.turn_speed, self.turn_time)
                laser = mv1.get_laser_value(360)
        self.stop_robot()
 
    def get_laser_value(self,x):
        return self.robotcontrol.get_laser(x)

    def stop_robot(self):
        self.robotcontrol.stop_robot()



if __name__ == '__main__':
    mv1 = MoveRobot(5, 1)
    while True:
        mv1.move()
        mv1.rotate()
