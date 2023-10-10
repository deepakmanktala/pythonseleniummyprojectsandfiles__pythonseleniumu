import socket
import sys

try:
    #Create an AF_INET, Stream Socket (TCP)
    sock_object= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err_msg:
    print("Unable to instantiate socket. Error Code"+ str(err_msg[0])+",Error Message: "+str(err_msg[1]))
    sys.exit();

print("Socket Initialized")
