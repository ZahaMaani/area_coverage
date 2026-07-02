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

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

def turn_right(last_run = False):
    while line_sensor.reflection() > 10:
        robot.drive(150,0)
    robot.turn(90)
    robot.straight(100)
    if line_sensor.reflection() < 10:
        last_run = True
    robot.turn(90)
    robot.stop() 
    return last_run 


def turn_left(last_run = False):
    while line_sensor.reflection() > 10:
        robot.drive(150,0)
    robot.turn(-90)
    robot.straight(100)
    if line_sensor.reflection() < 10:
        last_run = True
    robot.turn(-90)
    robot.stop() 
    return last_run 


def cover_area():
    counter = 1
    last = False
    while last == False: 
        if counter % 2 == 1:
            last = turn_left(last)
            counter += 1
        else:
            last = turn_right(last)
            counter += 1


    robot.drive(150,0)
    if line_sensor.reflection() < 10:  
        robot.stop()
        sys.exit()

def run_coverage():
    flag = 0

    while True:
        # تحرك للأمام بسرعة ثابتة
        robot.drive(150, 0)
        if line_sensor.reflection() < 10 and flag == 0:  # اكتشاف الخط الأسود
            flag = 1
            robot.stop()
            robot.turn(-90)  # انعطاف عند اكتشاف الخط الأسود
            continue  # العودة إلى الحلقة لمتابعة الحركة بعد الانعطاف

        if line_sensor.reflection() < 10:
                robot.stop()
                robot.turn(-90) 
                ev3.speaker.beep(frequency=500, duration=1000)
                cover_area()
        
try:
    #this will later change to follow the line to the corner
    run_coverage()
except KeyboardInterrupt:
    robot.stop()


'''

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# الإعدادات
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
line_sensor = ColorSensor(Port.S3)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

def run_coverage_loop():
    direction = 1  # 1 لليمين، -1 لليسار
    
    while True:
        # 1. تحرك للأمام حتى تجد خطاً (حافة المنطقة)
        while line_sensor.reflection() > 10:
            robot.drive(150, 0)
        
        # 2. عند العثور على الخط، توقف وارجع قليلاً
        robot.stop()
        robot.straight(-20)
        
        # 3. قم بالانعطاف لتغيير المسار
        # استخدام direction لتغيير زاوية الانعطاف في كل مرة
        robot.turn(90 * direction)
        robot.straight(50)  # مسافة الانتقال للمسار التالي
        robot.turn(90 * direction)
        
        # 4. اعكس الاتجاه للمرة القادمة
        direction *= -1
        
        # شرط الخروج: يمكنك إضافة حساس آخر أو عداد لإنهاء المهمة
        # if total_distance > 5000: break

try:
    run_coverage_loop()
except KeyboardInterrupt:
    robot.stop()

'''