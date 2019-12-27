import socket
import pickle
HEADER_SIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1111))
data = b''
while True:
    data_chunk = s.recv(16)
    data += data_chunk
    if len(data[HEADER_SIZE:]) == int(data[:HEADER_SIZE]):
        break
original_data = pickle.loads(data[HEADER_SIZE:])
print(original_data)
