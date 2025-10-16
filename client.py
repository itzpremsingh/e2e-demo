from json import dumps, loads
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

from config import HOST, PORT, Char
from keys import generate_keys


def handle_response(client: socket):
    public_key: None | tuple[int, int] = None
    data = client.recv(1024)
    if not data:
        return
    print(data.decode("utf-8"))
    data = loads(data.decode("utf-8"))
    # if Char.message in data:
    #     print(data[Char.message])

    if Char.key in data:
        public_key = data

    elif Char.friend in data:
        if data[Char.friend] == 1:
            print("Friend found")
            print(public_key)

        else:
            print("Waiting for friend")
            data = client.recv(1024)
            if not data:
                return

            data = loads(data.decode("utf-8"))
            print("Friend found")
            print(data)
            print(public_key)

        while True:
            data = client.recv(1024)
            if not data:
                return

            data = loads(data.decode("utf-8"))
            if Char.message in data:
                print(data[Char.message])


def handle_request(client: socket):
    while True:
        message = input("> ")
        if not message:
            client.close()
            print("Connection closed")
            break
        data = {Char.message: message}
        data = dumps(data)
        client.send(data.encode("utf-8"))


def client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((HOST, PORT))

    n, e, d = generate_keys()
    data = {Char.key: (n, e)}
    data = dumps(data)
    client.send(data.encode("utf-8"))

    Thread(target=handle_request, args=(client,)).start()
    Thread(target=handle_response, args=(client,)).start()


if __name__ == "__main__":
    client()
