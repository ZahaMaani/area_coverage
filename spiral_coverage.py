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
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=107)
    #16 , 12, 10
border_color = Color.RED

def find_corner():
    i = 0
    while i < 2:
        robot.drive(150, 0)
        if line_sensor.color() == border_color: 
            robot.stop()
            robot.turn(-93)
            i += 1
    ev3.speaker.beep()

def measure_room():
    robot.reset()
    robot.drive(100, 0)
    while line_sensor.color() != border_color:
        wait(10)
    robot.stop()
    width = robot.distance()
    
    # Reposition for Height
    robot.straight(-10) # Back up slightly
    robot.turn(-93)
    
    # Measure Height
    robot.reset()
    robot.drive(100, 0)
    while line_sensor.color() != border_color:
        wait(10)
    robot.stop()
    height = robot.distance()
    
    return height, width

def run_inward_spiral():
    find_corner()
    height, width = measure_room()
    robot.turn(-93)

    area = height * width
    width -=20
    counter = 0
    while area > 0:
        if counter % 2 == 0:
            robot.straight(width)
            width -= 160
        else:
            height -= 160
            robot.straight(height)
        robot.turn(-93)
        area = height * width
        counter += 1  

    ev3.speaker.beep()
    robot.stop()

try:
    run_inward_spiral()
except KeyboardInterrupt:
    robot.stop()
