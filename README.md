# Socket_Programming
Using socket programming we can connect two or more nodes in a network.  
<ul>
<li>For Single server-client connection <br>  
In the Single server-client connection the server creates a connection between the server and client with the help of IP and Port. <br>
#the server needs to be up and running before the client.py is launched.And change the Ip of server in client.py before running the program.<br>
After successfull connection the reverse shell will be activated and commands from server can be executed into client remotely. <br></li>
<br>
<li>For Single server- Multiple client connection<br>
In Single server- Multiple client connection , Multithreading is used to simultaneously accept new connection and another thread is used to handle the connections.<br> 
#the server needs to be up and running before the client.py is launched.And change the Ip of server in client.py before running the program. <br>
After successfull connection the reverse shell will be activated and commands from server can be executed into client remotely. <br>
Run the list command in the terminal to list the number of active connections. <br>
Run the select command to select one of the connection the terminal will be changed to the connections reverse shell. <br>
Use exit or quit to exit the connection. </li>
