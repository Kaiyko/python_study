#!/usr/bin/python3
import socket


def send_file_2_client(new_client_socket, client_addr):

    # 接收客户端发过来要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端%s需要下载的文件是: %s " % ((str(client_addr)), file_name))

    # 读取文件信息
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as result:
        print("没有要打开的文件(%s)" % result)

    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1.创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("服务器启动....")

    # 2.绑定端口
    tcp_server_socket.bind(("", 8088))

    # 3.设置为被连接socket 16-数量
    tcp_server_socket.listen(16)

    while True:
        # 4.等待
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 5.发送数据
        send_file_2_client(new_client_socket, client_addr)

        # 关闭socket
        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
