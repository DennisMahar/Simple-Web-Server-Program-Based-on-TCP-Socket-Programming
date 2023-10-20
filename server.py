from socket import *
import sys


def handle_request(connectionSocket, client_address):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:], "rb")
        outputdata = f.read()
        f.close()

        header = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\r\n\r\n"
        connectionSocket.send(header.encode())
        print(f'Connection from {client_address}')
        print("Response: HTTP/1.1 200 OK")
        connectionSocket.send(outputdata)
        connectionSocket.close()

    except IOError:
        header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
        connectionSocket.send(header.encode())
        print(f'Connection from {client_address}')
        print("Response: HTTP/1.1 404 Not Found")
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
        connectionSocket.close()
    print("\n===============================================\n")

def start_server():
    server_socket = socket(AF_INET, SOCK_STREAM)

    server_IP = "localhost"
    server_port = 80
    server_socket.bind((server_IP, server_port))
    server_socket.listen(1)

    print(f"[LISTENING] Server is listening on {server_IP}:{server_port}")
    print("===============================================\n")
    
    while True:
        connection_socket, client_address = server_socket.accept()  
        handle_request(connection_socket, client_address)
    connectionSocket.close()
    sys.exit()

if __name__ == '__main__':
    start_server()