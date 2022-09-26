import socket
from time import sleep

SERVER = "127.0.0.1"
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
client.connect((SERVER, 8002))


print("Example : 4 + 5")
inp = input("예시와 같은 방적식을 입력하여 주십시오 : ")

client.send(inp.encode())

#보내고나서 1초를 기다린 뒤 다시 연결
client.close()
sleep(5)
client = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)
client.connect((SERVER, 8002))

#정답을 받아온다. 
answer = client.recv(1024)
print("정답 :  "+answer.decode())
 
client.close()