import socket

HOST = '127.0.0.1'
now_PORT = 9999

print("시작 ")

bridge_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

bridge_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

bridge_socket.bind((HOST, now_PORT))

bridge_socket.listen(3)

client_socket, addr = bridge_socket.accept()

print('Connected by', addr)

result = ""

equation_f = client_socket.recv(1024)
equation = equation_f.decode() 

num1_f = client_socket.recv(1024)
num2_f = client_socket.recv(1024)
to_PORT = 0
data = 0

client_socket.close()
print("닫음")
if equation == "+" or equation == "-":
    to_PORT = 9992
    bridge_socket.connect((HOST, to_PORT))
    #값 송신 
    bridge_socket.sendall(equation_f)
    bridge_socket.sendall(num1_f)
    bridge_socket.sendall(num2_f) 
    
    
else:
    to_PORT = 9991
    bridge_socket.connect((HOST, to_PORT))
    #값 송신 
    bridge_socket.sendall(equation_f)
    bridge_socket.sendall(num1_f)
    bridge_socket.sendall(num2_f) 
    
data = bridge_socket.recv(1024)
bridge_socket.sendall(data) 
bridge_socket.close()
client_socket.close()