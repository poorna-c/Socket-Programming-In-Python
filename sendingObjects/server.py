import socket
import pickle
HEADER_SIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1111))
s.listen(2)
client_socket,client_address = s.accept()
d = {'One':1,'Two':2,'Three':3}
data = pickle.dumps(d)
data = bytes(f"{len(data):<{HEADER_SIZE}}",'utf-8')+data
client_socket.send(data)
client_socket.close()
s.close()