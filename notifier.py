#! /usr/bin/env python

import irclib
import sys
import os

target = "#varal7"
server = "10.8.0.1"
port = 6667
nickname = "Lara"
password= "Password"
hls = ["varal", "quach"]

class Notifier(irclib.SimpleIRCClient):
    """A basic IRC notifier
    """

    def on_pubmsg(self, onnection, event):
        nickname = event.source().split("!")[0]
        message = event.arguments()[0]
        payload = nickname + ' on ' + event.target() + ':\n' + message
        for hl in hls:
            if hl in message.lower():
                notify(payload)


    def on_disconnect(self, connection, event):
        print("disconnect event received")
        sys.exit()

    def on_privmsg(self, connection, event):
        nickname = event.source().split("!")[0]
        message = event.arguments()[0]
        payload = nickname + ' (PV): \n' + message
        notify(payload)

def notify(payload):
    print("Notifying")
    os.system("sendsms \"+33635113309\" \"" + payload + "\" > /dev/null 2>&1 &")

client = Notifier()

def main():
    c = Notifier()
    try:
        c.connect(server, port, nickname, password=password)
    except irclib.ServerConnectionError, x:
        print x
        sys.exit(1)
    c.start()

if __name__ == "__main__":
    main()
