#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
line_sensor = ColorSensor(Port.S3)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=107)
border_color = Color.RED
obstacle_sensor = UltrasonicSensor(Port.S2)
DISTANCE_THRESHOLD = 100

log_file = open("coverage_log.txt", "w")

def log_position():
    """Logs current cumulative distance and angle to the file."""
    log_file.write("{},{}\n".format(robot.distance(), robot.angle()))

def logged_turn(angle):
    """Turns the robot at a steady medium speed while continuously logging."""
    target_angle = robot.angle() + angle
    direction = 1 if angle > 0 else -1
    # Turning at a steady 80 deg/s
    while (direction == 1 and robot.angle() < target_angle) or (direction == -1 and robot.angle() > target_angle):
        robot.drive(0, direction * 80) 
        log_position()
        wait(20)
    robot.stop()

def logged_straight(distance, speed=100):
    """Drives straight for a specific distance while continuously logging."""
    target_dist = robot.distance() + distance
    direction = 1 if distance > 0 else -1
    while (direction == 1 and robot.distance() < target_dist) or (direction == -1 and robot.distance() > target_dist):
        robot.drive(direction * speed, 0)
        log_position()
        wait(20)
    robot.stop()

def find_corner():
    i = 0
    while i < 2:
        robot.drive(150, 0)
        if line_sensor.color() == border_color: 
            robot.stop()
            # Standard turn is fine here as we don't log setup phase
            robot.turn(-100) 
            i += 1

def avoid_obstacle():
    robot.stop()
    logged_turn(100)
    logged_straight(100)
    logged_turn(-100)
    while True:
        start_dist = robot.distance()
        hit_border_during_evasion = False
        
        while (robot.distance() - start_dist) < 100:
            robot.drive(100, 0)
            log_position()
            if line_sensor.color() == border_color:
                hit_border_during_evasion = True
                break
            wait(20)
        robot.stop()
        
        if hit_border_during_evasion:
            return
            
        logged_turn(-100)
        if obstacle_sensor.distance() > DISTANCE_THRESHOLD:
            break
        logged_turn(100)
        
    logged_straight(100)
    logged_turn(100)

def run_coverage():
    # Find corner first without logging
    find_corner()
    
    # Setup origin point (0,0)
    robot.reset()
    ev3.speaker.beep()

    direction = -1 
    task_finished = False

    while not task_finished: 
        # Drive forward until hitting a border or detecting an obstacle
        while line_sensor.color() != border_color:
            if obstacle_sensor.distance() < DISTANCE_THRESHOLD:
                robot.stop()
                avoid_obstacle()
            else:
                robot.drive(150, 0)        
                log_position()
                wait(20)
        robot.stop()
        
        # Turn to perform side-shift step (changed angle to 100)
        logged_turn(100 * direction)
        
        # Shift step over to next grid lane
        start_dist = robot.distance()
        hit_border = False
        
        while (robot.distance() - start_dist) < 80:
            robot.drive(100, 0)
            log_position()
            if line_sensor.color() == border_color:
                hit_border = True 
                break
            wait(20)
            
        robot.stop()        
        
        if hit_border:
            # Turn toward home stretch (changed angle to 100)
            logged_turn(100 * direction) 
            
            # Integrated your custom last loop while keeping it plottable
            while line_sensor.color() != border_color:
                robot.drive(150, 0)
                log_position()
                wait(20)
                
            robot.stop()
            task_finished = True     
        else:    
            # Turn back into the workspace (changed angle to 100)
            logged_turn(100 * direction)
            direction *= -1
            
    ev3.speaker.beep()
    robot.stop()

try:
    run_coverage()
finally:
    log_file.close()
    robot.stop()
