#!/usr/bin/python3
import socket


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
        print(client_addr)
        while True:
            # 5.接收数据
            recv_data = new_client_socket.recv(1024)
            print("%s" % recv_data.decode("utf-8"))
            if recv_data is None:
                break
            # 6.自动回复
            new_client_socket.send("自动回复...".encode("utf-8"))

        # 7.关闭socket
        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
