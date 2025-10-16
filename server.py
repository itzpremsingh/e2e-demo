from json import dumps
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

from config import HOST, PORT, Char


def handle_chat(client1: socket, client2: socket) -> None:
    client1.send(dumps({Char.friend: 1}).encode("utf-8"))
    while True:
        data = client1.recv(1024)
        if not data:
            break
        print(data.decode("utf-8"))
        client2.send(data)


def server():
    waiting: None | socket = None

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    while True:
        client, address = server.accept()
        print(f"Connected to {address}")

        if waiting:
            Thread(target=handle_chat, args=(client, waiting)).start()
            Thread(target=handle_chat, args=(waiting, client)).start()
            waiting = None
        else:
            waiting = client
            client.send(dumps({Char.friend: 0}).encode("utf-8"))


if __name__ == "__main__":
    server()
