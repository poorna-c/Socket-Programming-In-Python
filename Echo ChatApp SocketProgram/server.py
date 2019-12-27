import socket

HEADER_SIZE = 10
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1212))
s.listen(2)

while True:
    client_socket,client_addr = s.accept()
    print(f"Connection established with the {client_addr}")
    Welcome_text = "Welcome to the Server!!!"
    Welcome_text = f"{len(Welcome_text):<{HEADER_SIZE}}" + Welcome_text
    client_socket.send(bytes(Welcome_text,'utf-8'))
    while True:
        client_request = ''
        while True:
            client_request_chunk = client_socket.recv(16).decode('utf-8')
            client_request += client_request_chunk
            if len(client_request_chunk) <= 0 or (len(client_request[HEADER_SIZE:]) == int(client_request[:HEADER_SIZE])):
                break
        client_request = client_request[HEADER_SIZE:]
        print("Client Requested:",client_request)
        if client_request.lower() == "exit":
            client_socket.send(bytes(f"{len('Confirm Connection Termination'):<{HEADER_SIZE}}Confirm Connection Termination",'utf-8'))
            client_socket.close()
            break
        else:
            replay = "You Said: "+client_request
            replay = f"{len(replay):<{HEADER_SIZE}}" + replay
            client_socket.send(bytes(replay,'utf-8'))

    client_socket.close()
s.close()