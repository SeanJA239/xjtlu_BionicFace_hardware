# test_hard.py
import time
from adafruit_servokit import ServoKit

print("1.Start initializing...")

kit = ServoKit(channels=16, address=0x40)

print("2. Initialization complete. Testing servo 0 movement...")

servo0 = kit.servo[0]

print("   -> to 0 degrees")
servo0.angle = 0
time.sleep(1)

print("   -> to 180 degrees")
servo0.angle = 180
time.sleep(1)

print("   -> to 90 degrees")
servo0.angle = 90

print("3. test complete")