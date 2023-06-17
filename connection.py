import socket
import threading
from threading import Thread
import os
import sys

# https://superfastpython.com/extend-thread-class/

message = 0


class Channel():
    def __init__(self):
        # super()
        self.player = self.promptPlayer()
        self.conn = self.stablishConnection()

    # def run(self):
    #     self.player = self.promptPlayer()
    #     self.conn = self.stablishConnection()
    #     print( self.player, self.conn)

    def promptPlayer(self):
        return input('Choose mode: (1) Server (2) Client ')

    def stablishConnection(self):

        if (self.player == "1"):
            connection = self.start_server()
        elif (self.player == "2"):
            connection = self.start_client()
        else:
            print('Invalid mode. Default to client')
            # self.player == "2"
            # connection = start_client()
        #
        return connection

    def start_server(self):
        # host = "192.168.0.218"
        host = "localhost"
        port = 8000

        server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        server_socket.bind( (host, port) )
        server_socket.listen(1)
        print("server listening on host: ", host, " and port: ", port)
        print("")

        print("I'll stop here and wait for the other player to connect...")
        connection, address = server_socket.accept()

        print("The other player has connected!")
        return connection

    def start_client(self):
        # host = "192.168.0.218"
        host = "localhost"
        port = 8000

        client_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        client_socket.connect( (host, port) )
        print("connected to server host: ", host, " and port: ", port)

        # receive_thread = threading.Thread(target=receive_message, args=(client_socket, ))
        # receive_thread.start()

        # send_thread = threading.Thread(target=send_message, args=(client_socket, ))
        # send_thread.start()

        # receive_thread.join()
        # send_thread.join()

        return client_socket
    #


    def SendMessage(self, data):
        print("sending: ", data)
        print("I am player: ", self.player)
        print(self.conn)

        self.conn.send( data.encode("utf-8") )

    def ReceiveMessage(self):
        message = self.conn.recv(1024).decode("utf-8")
        print("received message: ", message)
        return message
        
#



# def receive_message(connection):
#     global message

#     while True:
#         try:
#             message = connection.recv(1024).decode("utf-8")
#             print("received message: ", message)
#             if (message == "exit"):
#                 raise SystemExit()
#             #
#         except ConnectionResetError:
#             break
#     #
# #

# def send_message(connection):
#     global message

#     while True:
#         message = input("Enter a message: ")
#         connection.send( message.encode("utf-8") )

#         if (message == "exit"):
#             raise SystemExit()
#         #        

#     #
# #

# def start_server():
#     host = "192.168.0.218"
#     port = 8000

#     server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
#     server_socket.bind( (host, port) )
#     server_socket.listen(1)
#     print("server listening on host: ", host, " and port: ", port)

        
#     connection, address = server_socket.accept()
    
#     receive_thread = threading.Thread(target=receive_message, args=(connection, ))
#     receive_thread.start()

#     send_thread = threading.Thread(target=send_message, args=(connection, ))
#     send_thread.start()

#     receive_thread.join()
#     send_thread.join()

#     #
#     # sys.exit()
# #

# def start_client():
#     host = "192.168.0.218"
#     port = 8000

#     client_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
#     client_socket.connect( (host, port) )
#     print("connected to server host: ", host, " and port: ", port)

#     receive_thread = threading.Thread(target=receive_message, args=(client_socket, ))
#     receive_thread.start()

#     send_thread = threading.Thread(target=send_message, args=(client_socket, ))
#     send_thread.start()

#     receive_thread.join()
#     send_thread.join()

# #


def getPlayer():
    return "B"

def getSquarePartnerTapped():
    return "sq1"

# def promptPlayer():
#     # Prompt the user to choose between server or client mode
#     player = input('Choose mode: (1) Server (2) Client ')

#     if player == "1":
#         start_server()
#     elif player == "2":
#         start_client()
#     else:
#         print('Invalid mode. Exiting...')
#     #
#     return player



