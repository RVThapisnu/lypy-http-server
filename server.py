from properties import *
from sockets import *
from conn_handler import *
from datetime import datetime

server = create_server(host,port)

show_banner()
print(f'Server Started in {host}:{port} !!')

nlog = open_log(log)

try:
    while True:
        try:
            client,client_ip = connect_client(server)
            request = client_recv(client)
            response = handle_req(request,client_ip,nlog)
            client_send(client,response)
            close_conn(client)
        except Exception as e:
            print('Error :',e)
            continue
except KeyboardInterrupt as k:
    print('\rTERMINATE SIGNAL RECEIVED !!')
except Exception as e:
    print('Error :',e)
finally:
    close_conn(server)
    close_log(nlog)
    print('\rServer Has Been Closed !!')
