import socket 
import json
import time

USE_MOCK_HARDWARE = False

HOST_IP = '0.0.0.0'
PORT = 52183

if USE_MOCK_HARDWARE:
    print("Mock Running")
    from mock_driver import MockServoKit as ServoKit
else:
    print("Real Running")
    from adafruit_servokit import ServoKit

try:
    from config import MOTOR_MAP
except ImportError:
    print("Map not found, using default mapping.")# I dkn what default mapping is
    MOTOR_MAP = {}

def init_kits():
    print("Initializing kits",flush=True)
    drivers = {}
    try:
        print("Try connecting kit 1",flush=True)
        drivers[0] = ServoKit(channels = 16, address = 0x40)
       #drivers[1] = ServoKit(channels = 16, address = 0x41)
       #drivers[2] = ServoKit(channels = 16, address = 0x42)
        print("Initialization complete")
    except Exception as e:
        print(f"Error initializing kits: {e}")
        return None
    return drivers

def safety_clamp(angle):
    return max(0, min(180,angle))

def apply_movements(drivers, data_list):
    for motor_id, target_angle in enumerate(data_list):
        if motor_id in MOTOR_MAP:
            board_idx, channel = MOTOR_MAP[motor_id]
        else:
            board_idx = motor_id // 16
            channel = motor_id % 16

        safe_angle = safety_clamp(target_angle)

        if board_idx in drivers:
            try:
                print(f"Setting board {board_idx} - Port {channel} -> {safe_angle} degrees")
                drivers[board_idx].servo[channel].angle = safe_angle
            except Exception as e:
                print(f"Error for board {board_idx} Ch {channel}:{e}")

def main():
    kits = init_kits()
    if not kits:
        print("init_kits() returned empty...")
        return
    print ("Init process worked!")
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST_IP, PORT))

    print(f"UDP server up and listening on {HOST_IP}:{PORT}")

    try:
        while True:
            data, addr = server.recvfrom(4096)
            print(f"Received message from {addr}")
            try:
                angles = json.loads(data.decode('utf-8'))
                if len(angles) > 0:
                    apply_movements(kits, angles)

            except json.JSONDecodeError:
                print("Received invalid JSON data")

    except KeyboardInterrupt:
        print("\n User interrupted the program.")

    finally:
        server.close()
        print("Socket closed")
if __name__ == "__main__":
    main()
