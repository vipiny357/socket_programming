# socket_programming
Using socket programming we can connect Two or more nodes in a network.
For Single server-client connection
In the Single server-client connection the server creates a connection between the server and client with the help of IP and Port.
#the server needs to be up and running before the client.py is launched.And change the Ip of server in client.py before running the program.
After successfull connection the reverse shell will be activated and commands from server can be executed into client remotely.

For Single server- Multiple client connection
In Single server- Multiple client connection , Multithreading is used to simultaneously accept new connection and another thread is used to handle the connections.
#the server needs to be up and running before the client.py is launched.And change the Ip of server in client.py before running the program.
After successfull connection the reverse shell will be activated and commands from server can be executed into client remotely.
Run the list command in the terminal to list the number of active connections.
Run the select command to select one of the connection the terminal will be changed to the connections reverse shell.
use exit or quit to exit the connection.
