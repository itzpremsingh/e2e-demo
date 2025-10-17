from json import dumps, loads
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

from common import decrypt, encrypt
from config import HOST, PORT, Char
from keys import generate_keys

friend_public_key: int | None = None
friend_modulus: int | None = None


def receive_messages(sock: socket, private_key: int, modulus: int):
    global friend_public_key
    global friend_modulus
    while True:
        try:
            data = sock.recv(4096)
            if not data:
                break
            data = loads(data.decode())
            if Char.message in data:
                cipher = data[Char.message]
                msg = decrypt(cipher, modulus, private_key)
                print(f"Friend: {msg}")
            elif Char.key in data:
                friend_modulus = data[Char.key][0]
                friend_public_key = data[Char.key][1]

        except Exception as e:
            print("Connection closed.", e)
            break


def send_messages(sock: socket) -> None:
    while True:
        msg = input("> ")
        if not msg:
            sock.close()
            break
        if friend_public_key is None or friend_modulus is None:
            continue
        cipher = encrypt(msg, friend_modulus, friend_public_key)
        sock.send(dumps({Char.message: cipher}).encode())


def client():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))

    modulus, public_key, private_key = generate_keys()
    sock.send(dumps({Char.key: (modulus, public_key)}).encode())

    Thread(
        target=receive_messages, args=(sock, private_key, modulus), daemon=True
    ).start()
    send_messages(sock)


if __name__ == "__main__":
    client()
