#This is a mock driver module for testing purposes when there is no actual hardware connected.
# Raspberry Pi is expected to print messages to the console instead of controlling real GPIO pins.

class MockServo:
    def __init__(self, board_address, pin):
        self.board = board_address
        self.pin = pin
        self._angle = 0
    @property
    def angle(self):
        return self._angle
    
    @angle.setter   
    def angle(self, value):
        self._angle = value
        #print(f"[MOCK] Setting angle of servo on board {hex(self.board)}, pin {self.pin} to {value} degrees.")

class MockServoKit:
    def __init__(self, channels=16, address=0x40):
        print(f"[MOCK] Initializing MockServoKit at address {hex(address)} with {channels} channels.")
        self.servo = [MockServo(address, i) for i in range(channels)]

from mock_driver import MockServoKit
kit = MockServoKit(0x40)
kit.servo[0].angle = 90

#The spinning method of servos needs to be specified as some sort of curve in formal implementation.