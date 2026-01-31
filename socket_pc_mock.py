import socket
import time
import json
import random

HOST = '192.168.137.93'
PORT = 52183 # don't know yet

def main():
    print(f" Sending fake angles to {HOST}:{PORT} ")
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # try:
    while True:
        fake_angles = [random.randint(0,180) for _ in range (33)]

        message = json.dumps(fake_angles).encode('utf-8')
        client.sendto(message, (HOST, PORT))

        print(f" Sent: {fake_angles[:3]} ")
        time.sleep(0.1)

    #     except KeyboardInterrupt:
    #   #user command processing
    #         print("\n ctrl+c detected. Exiting...")
        
    # finally:
    #   #cleaning up
    #     client.close()
    #     print(" Socket closed. Goodbye")

if __name__ == "__main__":
    main()