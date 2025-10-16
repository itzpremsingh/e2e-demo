from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("Usage: python main.py <server/client>")
    elif argv[1] == "client":
        from client import client

        client()
    elif argv[1] == "server":
        from server import server

        server()
