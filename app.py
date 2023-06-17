from flask import Flask, render_template, request
from connection import Channel

app = Flask(__name__)

@app.route("/")
def index():
    player =  channel.player # "1" or "2"

    return render_template( "index.html", player = player)
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
    return message
#

if __name__ == "__main__":
    channel = Channel()

    if (channel.player == "1"):
        app.run( port=5001)
    elif (channel.player == "2"):
        app.run( port=5002)
    #