from json import dumps, loads
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

from config import HOST, PORT


def forward(src: socket, dst: socket):
    try:
        while True:
            data = src.recv(4096)
            if not data:
                break
            print(f"Forwarding: {data.decode()}")
            dst.send(data)
    finally:
        src.close()
        dst.close()


def handle_pair(client1: socket, client2: socket):
    print("Pair connected")

    # Exchange keys first
    key1 = loads(client1.recv(4096).decode())
    key2 = loads(client2.recv(4096).decode())

    client1.send(dumps(key2).encode())
    client2.send(dumps(key1).encode())

    # Start forwarding messages
    Thread(target=forward, args=(client1, client2), daemon=True).start()
    Thread(target=forward, args=(client2, client1), daemon=True).start()


def server():
    waiting = None
    srv = socket(AF_INET, SOCK_STREAM)
    srv.bind((HOST, PORT))
    srv.listen()
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client, addr = srv.accept()
        print(f"Connected: {addr}")

        if waiting is None:
            waiting = client
        else:
            Thread(target=handle_pair, args=(waiting, client), daemon=True).start()
            waiting = None


if __name__ == "__main__":
    server()
