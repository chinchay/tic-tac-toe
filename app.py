from flask import Flask, render_template, request, jsonify
from connection import getPlayer, getSquarePartnerTapped
# from connection import promptPlayer
from connection import Channel
import threading

import socket
import threading
from threading import Thread
import os
import sys

app = Flask(__name__)

# channelThread = threading.Thread(target=)
# channel = Channel()
# channel.start()

@app.route("/")
def index():
    # player =  promptPlayer() #getPlayer() # "A" or "B"
    player =  getPlayer() # "A" or "B"
    squarePartnerTapped = getSquarePartnerTapped()

    return render_template(
        "index.html",
        player = player,
        squarePartnerTapped = squarePartnerTapped
    )
#

@app.route("/send", methods=["POST"])
def send():
    if request.method == "POST":
        data = request.get_data().decode('ascii')
        print("data I received at python from javascript: ", data)

        channel.SendMessage(data)
    return ""
    #
#

@app.route("/receive")
def receive():
    message = channel.ReceiveMessage()
    # message = {"message": message}
    # return jsonify(message=message)
    return message

# def start_server():
#     host = "192.168.0.218"
#     port = 8000

#     server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
#     server_socket.bind( (host, port) )
#     server_socket.listen(1)
#     print("server listening on host: ", host, " and port: ", port)

        
#     # connection, address = server_socket.accept()
#     # return connection

#     return server_socket

if __name__ == "__main__":

    # host = "192.168.0.218"
    # port = 8000

    # server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    # server_socket.bind( (host, port) )
    # server_socket.listen(1)
    # print("server listening on host: ", host, " and port: ", port)

    # channel = None
    # if (channel is not None):
    #     channel = Channel()

    channel = Channel()
    print("hola")

    app.run( )