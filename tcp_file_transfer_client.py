import socket
import sys

HOST, PORT = "10.10.11.2", 9999
fileName = sys.argv[1]

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # create a file
    fo = open(fileName, "w")
    fo.write("THIS IS A FILE\nBLAH BLAH BLAH \nTHIS FILE WILL BE SENT\n test test test")
    fo.close()

    # read file into buffer
    with open(fileName, 'rb') as fo:
        file_buffer = fo.read()


    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(file_buffer))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

    fo.close();

    

print("File '" + fileName +"' sent.")