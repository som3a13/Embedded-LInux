import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="127.0.0.1"

s.bind((ip,5000))
s.listen(5)

while True:
    client,address=s.accept()
    rodata=client.recv(1024)
    print(f"{address} is sending a msg to you: {rodata.decode('UTF-8')}")

    msg=str(input("Please enter message to send: "))
    msg_encoded=msg.encode('UTF-8')
    client.send(msg_encoded)
    client.close()