import socket
import json
from mock_driver import MockServoKit 

kit1 = MockServoKit(address=0x40)
kit2 = MockServoKit(address=0x41)
kit3 = MockServoKit(address=0x42)
kits = [kit1, kit2, kit3]

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 00000))# Replace 00000 with desired port number

print("UDP server up and listening")

while True:
    data, addr = server.recvfrom(4096)
    angles = json.loads(data.decode('utf-8'))

    for i, angle in enumerate(angles):
        board_id = i//16
        channel_id = i%16

        if board_id < 3:
            kits[board_id].servo[channel_id].angle = angle