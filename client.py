import socket
import threading 
header = 100
port = 3389
ip = "192.168.1.6"
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,port))

name = input("enter your name: ")
send_length = str(len(name.encode("utf-8"))).encode("utf-8")
send_length += b' ' * (header - len(send_length))
client.send(send_length)
client.send(name.encode("utf-8"))
       

def receive():
    while True:
        try:
         mp = int(client.recv(header).decode("utf-8"))
         message = client.recv(mp).decode("utf-8")
         print(f"{message} ")
        except:
         break 

def send_msg():
    while True:
        n=input()
        if n == "/0":
            
            send_length = str(len(n.encode("utf-8"))).encode("utf-8")
            send_length += b' ' * (header - len(send_length))
            client.send(send_length)
            client.send("/0".encode("utf-8"))
            break 
        n=f"{name} >> {n}"              
        send_length = str(len(n.encode("utf-8"))).encode("utf-8")
        send_length += b' ' * (header - len(send_length))
        client.send(send_length)
        client.send(f"{n}".encode("utf-8"))



thread = threading.Thread(target=receive)
thread.start()
thread = threading.Thread(target=send_msg)
thread.start()
