import socket
import sys

# create a file
fo = open("newFile", "w")
fo.write("THIS IS A FILE\nBLAH BLAH BLAH \nTHIS FILE WILL BE SENT\n test test test\n Daniella Sherman")
fo.close()

# read file into buffer

with open('newFile', 'rb') as fo:
    file_buffer = fo.read()

HOST, PORT = "localhost", 9999
data = sys.argv[1]

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(file_buffer))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("File sent.")

fo.close()