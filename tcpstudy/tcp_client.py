#!/usr/bin/python3
import socket


def main():
    # 1.创建tcp的socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.链接服务器
    server_ip = input("请输入要链接的服务器的ip:")
    server_port = int(input("请输入要链接的服务器的port:"))
    tcp_client_socket.connect((server_ip, server_port))

    # 3.发送数据/接收数据
    send_data = input("请输入要发送的数据:")
    tcp_client_socket.send(send_data.encode("utf-8"))

    # 4.关闭socket
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
