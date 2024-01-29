import threading
import socket

username = input("Enter your username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.104', 4444))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message =="username?":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except Exception as e:
            print(f"Error: {e}")
            client.close()
            break

def send():
    while True:
        try:
            message = f'{username}:{input("")}'
            client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            client.close()
            break

# Start the receive thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Infinite loop for sending messages
while True:
    send_thread = threading.Thread(target=send)
    send_thread.start()
    send_thread.join()  # Wait for the send thread to finish before prompting again
