# 导入socket库
import socket
# 创建一个socket;
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 创建连接
s.connect(('www.sina.com.cn',80))
# 注意一下，80端口为默认的Web服务端口,SMTP端口为25,
# FTP端口为21,1024以下的端口都为标准服务的端口,1024以上的端口可用任意使用
# 发送请求
s.send(b'GET /HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
# 数据接收
buffer=[]
while True:
	b=s.recv(1024)
	if b:
		buffer.append(b)
	else:
		break
data=b''.join(buffer)
# 关闭连接
s.close()
header, html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
# 把接收到的数据写入文件
with open('index.html','wb') as f:
	f.write(html)
