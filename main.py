#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait


ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
line_sensor = ColorSensor(Port.S3)
robot = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=90)
border_color = Color.RED

def find_corner():
    
    i = 0
    while i < 2:
        robot.drive(150, 0)
        if line_sensor.color() == border_color: 
            robot.stop()
            robot.turn(-90)
            i += 1

def run_coverage():
    find_corner()
    direction = -1 
    task_finished = False

    while not task_finished: 
       
        while line_sensor.color() != border_color:
            robot.drive(150, 0)
        
        robot.stop()
        
     
        robot.turn(90 * direction)
        
        distance_covered = 0
        hit_border = False
        
        while distance_covered < 80:
            robot.drive(100, 0)
            if line_sensor.color() == border_color:
                hit_border = True 
                break
            wait(10)
            distance_covered += 1
            
        robot.stop()
        
        
        if hit_border:
            
            robot.turn(90 * direction) 
            robot.drive(150, 0)        
            wait(2000)                 
            robot.stop()
            task_finished = True     
        else:
            
            robot.turn(90 * direction)
            direction *= -1

    
    ev3.speaker.beep(frequency=1000, duration=2000)
    robot.stop()

try:
    run_coverage()
except KeyboardInterrupt:
    robot.stop()
