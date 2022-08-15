import socket
import _thread
import sys

server = ""
port = 5555

#create a socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
