import socket
import json
import time
import math

TARGET_IP = '192.168.137.93'
TARGET_PORT = 52183
TOTAL_MOTORS = 32
FREQUENCY = 10
print(f"Activating PC Sender...")
print(f"Target IP: {TARGET_IP}, Target Port: {TARGET_PORT}")
print("Mode: Sine Wave Test")

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    frame_count = 0
    start_time = time.time()

    while True:
        t = time.time()
        sin_value = (math.sin(t*2)+1)/2 * 180

        angles = [int(sin_value)for _ in range(TOTAL_MOTORS)]

        #If we want to let particular motor move faster,
        #angles[0] = int((math.sin(t*4)+1)/2 * 180)  # Motor 0 moves at double frequency
        
        #message packing and sending
        message = json.dumps(angles).encode('utf-8')
        client.sendto(message, (TARGET_IP, TARGET_PORT))

        #log
        if frame_count %30 == 0:
            print(f"Frame {frame_count}: Sent angles {angles[:3]}...(Length: {len(angles)})")

        frame_count += 1

        time.sleep(1/FREQUENCY)

except KeyboardInterrupt:
    print("\n User interrupted.")
finally:
    client.close()
    print("Socket closed...")