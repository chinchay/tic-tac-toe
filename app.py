from flask import Flask, render_template
from connection import getPlayer

app = Flask(__name__)

@app.route("/")
def index():
    player = getPlayer() # "A" or "B"
    return render_template("index.html", player=player)
#

if __name__ == "__main__":
    app.run(debug=True)