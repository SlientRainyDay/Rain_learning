import socket

payload = 'fd200000a6ffbe4c00000000000000000000000000000000000000000000000000000000204116000101ce28'

# 创建TCP或UDP套接字对象
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # for TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # for UDP

# 连接到目标IP地址和端口号
sock.connect(('192.168.56.139', 5501))



# 将16进制报文转换为二进制数据并发送
bin_msg = bytes.fromhex(payload)
sock.sendall(bin_msg)

