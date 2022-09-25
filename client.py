import socket

print("hi")
HOST = '127.0.0.1'  
message = input('방정식을 입력하여 주세요 ex(1+1,2-1) : ')
message = list(message)
equation = message[1]
num1 = message[0]
num2 = message[2]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 9999
client_socket.connect((HOST, PORT))

#값 송신 
client_socket.sendall(equation.encode())
client_socket.sendall(num1.encode())
client_socket.sendall(num2.encode()) 



# 메시지를 수신
data = client_socket.recv(1024)
print('원하신 방정식의 결과값 :', repr(data.decode()))

# 소켓을 닫습니다.
client_socket.close()