import threading 
import socket
host = '192.168.0.104'
port = 4444
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients=[]
usernames=[]
def broadcast(message, sender_client):
    for c in clients:
        if c != sender_client:
            c.send(message)

def hanndel_client(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message,client)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            username=usernames[index]
            broadcast(f'{username} has left the chat room'.encode('utf-8'),client)
            usernames.remove(username)
            break
def recieve():
    while True:
        print('server is listening in port 4444')
        client,address=server.accept()
        print(f"connection is established with {str(address)} ")
        client.send('username?'.encode('utf-8'))
        username=client.recv(1024)
        usernames.append(username)
        clients.append(client)
        print(f'the user of this client is {username}'.encode('utf-8'))
        broadcast(f'{username} has connected to chat room'.encode('utf-8'),client)
        client.send("you are now connected".encode('utf-8'))
        thread=threading.Thread(target=hanndel_client,args=(client,))
        thread.start()
if __name__=="__main__":
    recieve()
            
        
    

