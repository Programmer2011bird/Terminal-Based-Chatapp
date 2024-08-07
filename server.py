import threading
import socket


HOST: str = "127.0.0.1"
PORT: int = 8000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SERVER_SOCKET:
        SERVER_SOCKET.bind((HOST, PORT))

        print(f"[SERVER STARTED] Listening on {HOST} : {PORT}")

        SERVER_SOCKET.listen()
        
        while True:
            connection, address = SERVER_SOCKET.accept()
            
            print(f"[NEW CONNECTION] connected by {address}")
            
            data = connection.recv(2048)

            print(f"[{address}] {data.decode()}")

            connection.send("ping".encode())


main()
