import socket

HOST = '127.0.0.1'
PORT = 9991

print("시작 ")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()
print("듣는 중 ")

bridge_socket, addr = server_socket.accept()

print('Connected by', addr)

result = ""
while True:
    if not equation:
        break
    equation_f = bridge_socket.recv(1024)
    num1_f = bridge_socket.recv(1024)
    num2_f = bridge_socket.recv(1024)
    
    equation = equation_f.decode() 
    num1 = int(num1_f.decode())
    num2 = int(num2_f.decode())

    print('Received from', addr,"  수식 : ", equation,"  두 숫자 : ",num1,num2)
    if equation == "/":
        result =str( num1 / num2)
    else :
        result =str( num1 * num2)
    result = bytes(result, 'utf-8')
    
    bridge_socket.sendall(result)

bridge_socket.close()
server_socket.close()