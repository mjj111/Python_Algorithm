# Import socket module
import socket
from time import sleep
 
LOCALHOST = "127.0.0.1"
PORT = 8002
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind((LOCALHOST, PORT))
server.listen()
print("서버 시작")
print("클라이언트를 기다립니다..")
client, clientAddress = server.accept()
print("클라이언트와의 연결이 되었습니다. 연결자 :", clientAddress)
msg = ''
answer = ''


data = client.recv(1024)    
msg = data.decode()


print("방정식을 수신")
operation_list = msg.split()
operation = operation_list[1]

#데이터를 받고 나서는 잠시끊는다. 
server.close()

server = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)

# 연결 해야한다. 
if operation == "+" or operation == "-" :
    print("더하기 뺴기 서버에 접속")
    server.connect((LOCALHOST, 8003))

else :
    print("나누기 곱하기 서버에 접속")
    server.connect((LOCALHOST, 8004))

#데이터를 받고 받았을 경우 연결을 끊는다. 
print("데이터 수신중")
server.sendall(data)
answer = server.recv(1024)

print("정답을 클라이언트에게 전송 : ",answer.decode())
server.close()
    
    
    
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind((LOCALHOST, PORT))
server.listen()
print("클라이언트를 기다립니다..")
client, clientAddress = server.accept()
print("클라이언트와의 연결이 되었습니다. 연결자 :", clientAddress)
   
client.send(answer)
server.close()