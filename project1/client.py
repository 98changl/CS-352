import threading
import time
import random

import socket
import sys

def client(table, rsHostname, rsListenPort, tsListenPort):
    # connect to rs server
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    # port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    rs_server_binding = (localhost_addr, rsListenPort)
    rs.connect(rs_server_binding)
    
    while name in table:
        # send data to the server
        rs.send( name )

        # Receive data from the server
        data_from_server = rs.recv(100)
        print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

        # open text file to write
        resolve = open("RESOLVED.txt", "w")

        data = data_from_server.split()
        hostname = data[0]
        address = data[1]
        flag = data[2]

        if address != "-":
            # output to file here
            resolve.write( data )
        else:
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
            ts.send( name )

            # Receive data from the server
            data_from_server = ts.recv(100)
            print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
            
            # write to file
            resolve.write( data_from_server )
    
    # close the client socket
    resolve.close()
    rs.close()
    ts.close()
    exit()
    
def main():
    if len(sys.argv) < 3:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    args = str(sys.argv)
    print ( args )
    
    # convert arguments into strings to read into client
    rsHostname = args[0]
    rsListenPort = args[1]
    tsListenPort = args[2]
    del args
    
    # read in file
    f = open("PROJI-HNS.txt", "r")
    
    # set up list of hostnames 
    table = []
    read = f.readlines()
    
    # populate the list with hostnames
    for line in read:
        # check to see if the line is valid
        print( line )
        
        # add the hostname into the list
        table.append( line )
    
    client(table, rsHostname, rsListenPort, tsListenPort)
    exit()

if __name__ == "__main__":
    main()
    #t1 = threading.Thread(name='server', target=server)
    #t1.start()

    #time.sleep(random.random() * 5)
    #t2 = threading.Thread(name='client', target=client)
    #t2.start()

    #time.sleep(5)
    print("Done.")
