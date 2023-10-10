import socket

##sock_object = socket.socket(socket_family, socket_type, protocol=0)
#Instantiate an AF_INET, STREAM socket (TCP)

sock_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Initialized')
