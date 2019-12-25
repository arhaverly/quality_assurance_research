import socket

user_pass_dict = {"user": "pass", "arh2913": "secure_password124$$"}


def manage_pass(clientsocket):
    for i in range(3):
        data = clientsocket.recv(1024)
        print(data)
        split_data = data.decode().split(' ')
        good = False
        if split_data[0] in user_pass_dict:
            if split_data[1] == user_pass_dict[split_data[0]]:
                clientsocket.sendall(b'1')
                print("valid credentials")
                good = True
                return

        if not good:
            print("invalid credentials")
            clientsocket.sendall(b'0')


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 20020
    print (host)
    print (port)
    s.bind((host, port))

    s.listen(5)
    while True:
        print("waiting...")
        (clientsocket, address) = s.accept()
        print("connection found!")
        manage_pass(clientsocket)

        clientsocket.close()




if __name__ == "__main__":
    main()