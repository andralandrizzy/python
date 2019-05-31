# self note: run server program first before run the client.

import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    sock  = socket.socket()
    sock.connect((host, port))

    message = input("Type message here -> : ")
    while message != "q":
        sock.send(message.encode("utf-8"))
        data = sock.recv(1024).decode("utf-8")
        print("Received from server: " + data)
        message = input("Type message here ->")
    sock.close()

if __name__ == "__main__":
    Main()