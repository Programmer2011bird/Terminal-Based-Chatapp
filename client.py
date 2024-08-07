import threading
import socket


HOST: str = "127.0.0.1"
PORT: int = 8000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SERVER_SOCKET:
        SERVER_SOCKET.connect((HOST, PORT))

        SERVER_SOCKET.send("pong".encode())

        DATA = SERVER_SOCKET.recv(2048).decode()

        print(DATA)


main()
