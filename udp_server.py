import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999')
while True:
	# 接收数据
	data,addr = s.recvfrom(1024)
	# recvfrom可以获取到客户端的端口和地址
	print('Received from %s:%s' %addr)
	s.sendto(b'Hello,%s!' %data,addr)

