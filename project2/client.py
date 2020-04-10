import threading
import time
import random

import socket
import sys

def client(table, lsHostname, lsListenPort):

    resolve = open("RESOLVED.txt", "w")
    for name in table:

        try:
            ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[C]: Client socket created")
        except socket.error as err:
            print('socket open error: {} \n'.format(err))
            exit()
        
        # Define the port on which you want to connect to the server
        # port = 50007
        localhost_addr = socket.gethostbyname(socket.gethostname())

        # connect to the server on local machine
        ls_server_binding = (localhost_addr, lsListenPort)
        #print(rs_server_binding)
        ls.connect(ls_server_binding)
    
    
        # send data to the server
        ls.send( name )

        # Receive data from the server
        data_from_server = ls.recv(1000)
        print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

        # open text file to write
        #resolve = open("RESOLVED.txt", "w")

        #data = data_from_server.split()
        #hostname = data[0]
        #address = data[1]
        #flag = data[2]
        resolve.write(data_from_server)
        
    resolve.close()
        #exit()
    
def main():
    if len(sys.argv) < 3:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # convert arguments into strings to read into client
    lsHostname = str(sys.argv[1])
    lsListenPort = int(sys.argv[2])
    
    # read in file
    f = open("PROJ2-HNS.txt", "r")
    
    # set up list of hostnames 
    table = []
    read = f.readlines()
    
    # populate the list with hostnames
    for line in read:
        # check to see if the line is valid
        #print( line )
        
        # add the hostname into the list
        table.append( line )
    
    client(table, lsHostname, lsListenPort)
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
