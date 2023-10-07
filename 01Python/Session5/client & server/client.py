import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="127.0.0.1"
client.connect((ip,5000))

while True:
    msg=str(input("PLease eneter msg to send: "))
    msg_encoded=msg.encode('UTF-8')
    client.send(msg_encoded)

    rodata=client.recv(1024)
    print(f"{ip} is sending a msg to you {rodata.decode('UTF-8')}")
    client.close()