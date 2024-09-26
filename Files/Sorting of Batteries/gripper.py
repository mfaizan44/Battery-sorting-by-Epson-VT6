import RPi.GPIO as GPIO

GRIPPER_PIN = 17

def setup_gripper():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GRIPPER_PIN, GPIO.OUT)

def activate_gripper():
    GPIO.output(GRIPPER_PIN, GPIO.HIGH)
    print("Gripper activated")

def deactivate_gripper():
    GPIO.output(GRIPPER_PIN, GPIO.LOW)
    print("Gripper deactivated")

def cleanup_gripper():
    GPIO.cleanup()
