import socket

def create_server(host,port):
    addr = (host,port)
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    server.listen(1)
    return server

def connect_client(server):
    client,client_addr = server.accept()
    return client,client_addr

def client_recv(client,size = 1024):
    data = client.recv(size)
    data = data.decode()
    return data

def client_send(client,data):
    #data = data.encode()
    client.send(data)

def close_conn(conn):
    conn.shutdown(socket.SHUT_RDWR)

def show_banner():
    print("\n"
          " ██╗  ██╗   ██╗██████╗ ██╗   ██╗    ██╗  ██╗████████╗████████╗██████╗ \n"
          " ██║  ╚██╗ ██╔╝██╔══██╗╚██╗ ██╔╝    ██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗ \n"
          " ██║   ╚████╔╝ ██████╔╝ ╚████╔╝     ███████║   ██║      ██║   ██████╔╝ \n"
          " ██║    ╚██╔╝  ██╔═══╝   ╚██╔╝      ██╔══██║   ██║      ██║   ██╔═══╝  \n"
          " ███████╗██║   ██║        ██║       ██║  ██║   ██║      ██║   ██║     \n"
          " ╚══════╝╚═╝   ╚═╝        ╚═╝       ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝     \n"
          "                                                                       \n"
          " ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗                     \n"
          " ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗                    \n"
          " ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝                    \n"
          " ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗                    \n"
          " ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║                    \n"
          " ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝                    \n"
          )
