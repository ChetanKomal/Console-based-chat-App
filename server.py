import socket
import threading
header = 100
port = 3389
ip = "192.168.1.6"
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
clients=[]
names=[]
server.listen()
def broadcast(message):
    for client in clients:
        send_length = str(len(message)).encode("utf-8")
        send_length += b' ' * (header - len(send_length))
        client.send(send_length)
        client.send(message)
    
def handle_client(conn,addr):
    while True:
        mmm = int(conn.recv(header).decode("utf-8"))
        msg = str(conn.recv(mmm).decode("utf-8"))
        if msg == "/0":
            try:
             index = clients.index(conn)
             clients.remove(conn)
             name = names[index]
             broadcast(f"{name} disconnected".encode("utf-8"))
             print(f"{name} {addr} disconnected")
             names.remove(name)
             break
            except:
             break           
        broadcast(msg.encode("utf-8"))  
    conn.close()
     


    
def start():
    
    print(f"server is started and listening on {ip}:{port}") 
    while True:
        conn,addr = server.accept()
        print(f"connected with {addr}")
        aa=int(conn.recv(header).decode("utf-8"))
        nn = conn.recv(aa).decode("utf-8")
        names.append(nn)
        clients.append(conn)
        print(f"{nn} joined the chat")
        msg2 = f"\n{nn} joined the chat".encode("utf-8")
        broadcast(msg2)
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"Total Connected clients: {threading.activeCount() - 1}\n")
start()