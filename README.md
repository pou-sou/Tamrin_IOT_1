# TCP Chat Program:

- It's a basic Python-based TCP server-client application that allows two devices to communicate with each other using TCP/IP.
- this is my homework for IOT(?) 

## Files:

[server.py](https://github.com/pou-sou/Tamrin_aghaye_zare/blob/main/Source%20code/server.py): The server-side application that listens for incoming connections from clients.

[client.py](https://github.com/pou-sou/Tamrin_aghaye_zare/blob/main/Source%20code/client.py): The client-side application that connects to the server to send and receive messages. 
    
## Requirements:
  Python 3.x
  socket library (comes pre-installed with Python)

## How to use:

Someone will be the server which will be using the server.py code using python server.py using 'python server.py' while you are in the directory using 'cd e:\example'
the other person will be using the client.py using 'python server.py' when in the directory of python client.py.
both people on both ends should edit the .py codes and change the IP accordingly the port is set to 5050 just change it to the one you can **port forward** to if needed.
Also the server should allow the ports through firewall besides port forwarding.

after that they'll connect and they can communicate only one by one though.
