import socket
 
LOCALHOST = "127.0.0.1"
PORT = 8004
pm_server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

pm_server.bind((LOCALHOST, PORT))
pm_server.listen(1)
print("서버 시작")
print("브릿지를 기다립니다..")

bridge, clientAddress = pm_server.accept()
print("브릿지와의 연결이 되었습니다. 연결자 :", clientAddress)
msg = ''

data = bridge.recv(1024)
msg = data.decode()


print("방정식을 수신")

result = 0
operation_list = msg.split()
oprnd1 = operation_list[0]
operation = operation_list[1]
oprnd2 = operation_list[2]

num1 = int(oprnd1)
num2 = int(oprnd2)


if operation == "/":
    result = num1 / num2
else:
    result = num1 * num2

print("정답을 클라이언트에게 전송")

output = str(result)
bridge.send(output.encode())
bridge.close()