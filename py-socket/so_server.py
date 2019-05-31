import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    sock = socket.socket()
    sock.bind((host, port))

    sock.listen(1)
    c, addr = sock.accept()
    
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024).decode("utf-8")
        if not data:
            break
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        c.send(data.encode("utf-8"))
    c.close()

if __name__ == "__main__":
    Main()