
import RPi.GPIO as GPIO

import time

servo = 18
back = 22
forth = 23

trim = 85

def init():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(servo, GPIO.OUT)
    GPIO.setup(back, GPIO.OUT)
    GPIO.setup(forth, GPIO.OUT)

    global pwm
    pwm = GPIO.PWM(servo, 100)
    pwm.start(5)

def motorTest():
    GPIO.output(back, GPIO.HIGH)
    print("1")
    time.sleep(2)

    pwm.ChangeDutyCycle(100)
    GPIO.output(back, GPIO.HIGH)
    GPIO.output(forth, GPIO.HIGH)
    print("2")
    time.sleep(2)

    pwm.ChangeDutyCycle(0)
    GPIO.output(back, GPIO.HIGH)
    GPIO.output(forth, GPIO.LOW)
    print("3")
    time.sleep(2)

    pwm.ChangeDutyCycle(75)
    GPIO.output(back, GPIO.HIGH)
    GPIO.output(forth, GPIO.HIGH)
    print("4")
    time.sleep(2)

    pwm.ChangeDutyCycle(25)
    GPIO.output(back, GPIO.LOW)
    GPIO.output(forth, GPIO.HIGH)
    print("5")
    time.sleep(2)

    pwm.ChangeDutyCycle(50)
    GPIO.output(back, GPIO.LOW)
    GPIO.output(forth, GPIO.LOW)
    print("6")
    time.sleep(2)


    GPIO.output(back, GPIO.HIGH)
    GPIO.output(forth, GPIO.HIGH)

def servoTest():
    i = 0
    step = 0.1
    while i <= 1:
        print("i:"+str(i))
        pwm.ChangeDutyCycle(float((90*i)+90) / 10.0)
        time.sleep(1)
        i+=step

    i = 1
    while i >= 0:
        print("i:"+str(i))
        pwm.ChangeDutyCycle(float((90*i)+60) / 10.0 + 2.5)
        time.sleep(1)
        i-=step

#direction:(0=left, 1=right, 0.5=straight) speed:(-1=backwards, 1=forwards, 0=stationary)
def drive(dir, spd):
    pwm.ChangeDutyCycle(float((90 * dir) + trim) / 10.0)
    GPIO.output(back, GPIO.LOW if spd < 0 else GPIO.HIGH)
    GPIO.output(forth, GPIO.LOW if spd > 0 else GPIO.HIGH)

def stop():
    drive(0.5, 0)

def driveTest():
    stop()
    print("drive test: steering")
    time.sleep(2)

    drive(0, 0)
    print("left")
    time.sleep(1)
    drive(0.25, 0)
    time.sleep(1)

    drive(0.5, 0)
    print("straight")
    time.sleep(2)

    drive(1, 0)
    print("right")
    time.sleep(1)
    drive(0.75, 0)
    time.sleep(1)

    stop()
    print("drive test: motor")
    time.sleep(2)

    drive(0.5, 1)
    print("forwards")
    time.sleep(1)
    drive(0.5, 0.5)
    time.sleep(1)

    drive(0.5, 0)
    print("stationary")
    time.sleep(2)

    drive(0.5, -1)
    print("backwards")
    time.sleep(1)
    drive(0.5, -0.5)
    time.sleep(1)

    stop()
    print("test complete")


def kill():
    global pwm
    pwm.stop()  #?
    del pwm
    GPIO.cleanup()

if __name__ == '__main__':
    init()
    driveTest()
    kill()
