#!/usr/bin/env pybricks-micropython
import sys
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
    #this will later be follow the line to the corner
    i = 0
    while i < 2:
        robot.drive(150, 0)
        if line_sensor.color() == border_color: 
            robot.stop()
            ev3.speaker.beep(frequency=500, duration=1000)
            robot.turn(-90)
            i+=1

def run_coverage():

    find_corner()

    direction = -1
    while True: 
        while line_sensor.color() != border_color:
            robot.drive(150, 0)
        
        robot.stop()
        robot.turn(90 * direction)
        robot.straight(80)
        robot.turn(90 * direction)
        
        direction *= -1
        
        # Find a way to end the program
        # if total_distance > 5000: break
        
try:
    run_coverage()
except KeyboardInterrupt:
    robot.stop()