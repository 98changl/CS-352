import threading
import time
import random

import socket
import sys

def client(rsHostname, rsListenPort, tsListenPort):
    # connect to rs server
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    #port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    rs_server_binding = (localhost_addr, rsListenPort)
    rs.connect(rs_server_binding)
    
    # send data to the server

    # Receive data from the server
    data_from_server = rs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
    
    data = data_from_server.split()
    hostname = data[0]
    address = data[1]
    flag = data[2]
     
    if address != "-":
        # output to file here
        return data_from_server
    
    # if rs returns failer, connect to ts server
    try:
        ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # connect to the server on local machine
    ts_server_binding = (hostname, tsListenPort) # the returned host from rs is the ts hostname
    ts.connect(ts_server_binding)
    
    # send data to server
    
    # Receive data from the server
    data_from_server = ts.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
    
    # close the client socket
    rs.close()
    ts.close()
    exit()
    
def main():
    if len(sys.argv) < 3:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    args = str(sys.argv)
    print args
    
    rsHostname = args[0]
    rsListenPort = args[1]
    tsListenPort = args[2]
    del args
    
    client(rsHostname, rsListenPort, tsListenPort)
    exit()

if __name__ == "__main__":
    main()
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Done.")
