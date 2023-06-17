import socket

class Channel():
    def __init__(self):
        self.player = self.promptPlayer()
        self.conn = self.stablishConnection()

    def promptPlayer(self):
        return input('Choose mode: (1) Server (2) Client ')

    def stablishConnection(self):
        if (self.player == "1"):
            connection = self.start_server()
        elif (self.player == "2"):
            connection = self.start_client()
        else:
            print('Invalid mode...')
        #
        return connection

    def start_server(self):
        host = "192.168.0.218"
        # host = "localhost"
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
        host = "192.168.0.218"
        # host = "localhost"
        port = 8000

        client_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        client_socket.connect( (host, port) )
        print("connected to server host: ", host, " and port: ", port)

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