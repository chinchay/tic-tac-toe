# Overview

The purpose of this application is to demonstrate the basic ideas of networking and having fun in the meantime. In this application, two different devices can communicate over the local network and use this communication to update on the screen the state of the other device, in this case, the cell that have been tapped. This gives real time interaction between two players.


# How to use it

Follow the recipe:

```console
$ git clone https://github.com/chinchay/habit-tracker.git
$ cd habit-tracker
$ python app.py
```

the open the url address shown in the terminal on a web browser. Your partner's device should be sharing the same wi-fi connection.


# How it works

The tic-tac-toe game relies on the Python language and the socket package to communicate over the local network. It uses the server-to-client model, so the server side would need to be initiated first to begin with the game:

```console
$ python app.py
Choose mode: (1) Server (2) Client
```

after choosing option 1, it will wait for the other partner to connect

```console
I'll stop here and wait for the other player to connect...
```

and the other player should type `python app.py` and choose the client side `(2)`. Flask will render on the screen the tic-tac-toe game and the program is listening now if the user is tapping on one of the cells.

A demonstration of the software running and a walkthrough of the code can be found [here](https://youtu.be/59-zcpUUY28). For this demonstration, I used a MacOS and an iPad with Python installed in both of them.



# Network Communication

For this client/server arquitecture, the TCP (Transmission Control Protocol) transport layer protocol is used, since it is required both players to be connected. The data needs to be reliable and ordered sent so that the screen can properly update the state of the other player's move. The program is based on the `bind()` and `connect()` functions of the socket package. To establish a connection, the local network is used and one of the devices acting as a server listening at port `8000`. This same information is used for the client side.

After the connection is established and whenever a tic-tac-toe cell is tapped on the screen, the program will convert it to a text label through the use of html and javascript functions. The label is a fixed-length string indicating what square has been tapped, for example: `sq1` for square 1, or `sq2` for square 2. The implemented channel class is able to send an receive this type of message, and delivering it for proper rendering on the other player's screen.



# Development Environment

* __Editor__: Visual Studio Code
* __Languages__: Python 3.10.5 and JavaScript
* __Python packages__: [Socket](https://docs.python.org/3/library/socket.html), [Flask](https://pypi.org/project/Flask/)
* __Version control system__: Git
* __Cloud repository__: GitHub


# Useful Websites

* [Socket Programming in Python](https://realpython.com/python-sockets/)
* [Talking to Python from JavaScript (and Back Again!)](https://healeycodes.com/talking-between-languages)

## Nice to know

You can use your smartphone or tablet to play this game, if you don't want to use virtual machines. I have used the [iSH](https://ish.app/) application which is a Linux shell iOS. Installing the required softare would be: 


```console
$ apk update && apk upgrade
$ apk add git
$ apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
$ apk add py-pip # to install pip
$ apk add vim
$ pip install flask # required to render the html file on the web browser
$ git clone https://github.com/chinchay/tic-tac-toe.git
```



# Future Work

* Each player takes turns to play, so this program should implement an exception handling if this is not the case
* This software should automatically identify the local IP address of the host server and an available port
* Tic-tac-toe rules should me implemented
