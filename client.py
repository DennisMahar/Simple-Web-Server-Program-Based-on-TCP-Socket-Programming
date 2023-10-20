from socket import *
import sys

def main(server_IP, server_port, filename):
    client_socket = socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.connect((server_IP, server_port))
    except:
        print("The server is not available") #jika server tidak tersedia
        client_socket.close()
        sys.exit()
    print(f"[CONNECTED] Client connected to server at {server_IP}:{server_port}")

    request_header = f'GET /{filename} HTTP/1.1\r\nHost: {server_IP}:{server_port}\r\n\r\n'
    client_socket.send(request_header.encode())

    response = client_socket.recv(1024).decode()
    print(f'Response: {response}')

    if "404" in response: #Jika file tidak ditemukan
        print("[ERROR] File not found on the server.\r\n\r\n")
    else:
        f = open(filename[0:])
        outputdata = f.read()
        f.close()
        print("Isi File : \n\n", outputdata, "\n\n")

    client_socket.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"format: {sys.argv[0]} <server_IP> <server_port> <filename>") #Jika format masukan salah
    else:
        server_IP, server_port, filename = sys.argv[1:]
        main(server_IP, int(server_port), filename)

