import socket

HEADER_SIZE = 10
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect((socket.gethostname(),1212))

def recive_Message():
    recieved_replay = ''
    while True:
        recieved_replay_chunk = soc.recv(16).decode('utf-8')
        recieved_replay += recieved_replay_chunk
        if len(recieved_replay_chunk)<=0 or (len(recieved_replay[HEADER_SIZE:]) == int(recieved_replay[:HEADER_SIZE])):
            break
    return recieved_replay[HEADER_SIZE:]

while True:
    recieved_replay = recive_Message()
    print(recieved_replay)
    request = input("\nEnter Data: ")
    request = f"{len(request):<{HEADER_SIZE}}" + request
    soc.send(bytes(request,'utf-8'))
    if request.lower() == "exit":
        if recive_Message() == "Confirm Connection Termination":
            soc.close()
        break