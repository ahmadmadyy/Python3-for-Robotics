from robot_control_class import RobotControl
import time

class MoveRobot():
    def __init__(self, motion, clockwise, speed, time):
        self.robotcontrol = RobotControl()
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 6.0 
        self.rotate_r = 80 #90
        self.rotate_l = -80 #-90
        self.safety_value_f = 0.75
        self.safety_value_s = 2
        #self.time_turn = 7.0 # 90
        # This is an estimate time in which the robot will rotate 90 degrees

    def move_straight(self):
        self.robotcontrol.move_straight_time(self.motion, self.speed, self.time)
        #self.move_straight()

    def move_straight_2(self):
        laser = mv1.get_laser_value(360)
        while laser>1:
            self.robotcontrol.move_straight()
            laser = mv1.get_laser_value(360)

        self.stop_robot()

    def rotate(self,dir):
        if dir==1:
            self.robotcontrol.rotate(self.rotate_r)
        else:
            self.robotcontrol.rotate(self.rotate_l)
 
    def get_laser_value(self,x):
        return self.robotcontrol.get_laser(x)

    def get_laser_full_(self):
        list = self.robotcontrol.get_laser_full()
        a,b = list[0], list[719]
        return [a,b]

    def turn(self,dir):
        if dir == 1:
            self.robotcontrol.turn(self.clockwise, self.speed, self.time_turn)
        else:
            self.robotcontrol.turn('counter-clockwise', self.speed, self.time_turn)

    def stop_robot(self):
        self.stop_robot()

'''
mv1 = MoveRobot('forward', 'clockwise', 0.3, 4)
mv1.draw_square()
mv2 = MoveRobot('forward', 'clockwise', 0.3, 8)
mv2.draw_square()
'''


if __name__ == '__main__':
    mv1 = MoveRobot('forward', 'clockwise', 0.3, 2)
    laser = mv1.get_laser_value(360)
    mv1.move_straight()
    while True:
        a,b = mv1.get_laser_full_()
        print('a: ', a)
        print('b: ', b)
        print('laser: ',laser)
        if laser>mv1.safety_value_f:
            if a<mv1.safety_value_s and b<mv1.safety_value_s:
                mv1.move_straight()
                #print('straight')
        elif laser<=mv1.safety_value_f:
            if a>mv1.safety_value_s:
                #mv1.stop_robot()
                #mv1.turn(1)
                mv1.rotate(2)
                print('rotate left')
            elif b>mv1.safety_value_s:
                #mv1.stop_robot()
                #mv1.turn(2)
                mv1.rotate(1)
                print('rotate right')
        laser = mv1.get_laser_value(360)

        
        