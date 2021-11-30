	Tornado Web Server
	==================

```
pip install tornado
python tornado.py
```

![s1](https://raw.githubusercontent.com/c4pt000/tornado/master/p2p-html-server.png)
<br>
<br>
* probably requires Cython for python to c++ bridge to internally bind to c++ code as "transpiled" code for c++ from python .py
<br>
<br>
* each bitcoin "style wallet" -qt desktop wallet serves the listening request and grabs the current transaction hash output from a sent received transaction to populate the html "tornado" gui output
<br>
<br>
* to relinquish the need to host a blockexplorer on an html server remotely and to allow sent and received transaction lookups on ABE style and modern blockexplorer websites locally to serve to each wallet as a node remotely
<br>
<br>
<br>
<br>
<br>
<br>
<br>

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/tornadoweb/tornado
   :target: https://gitter.im/tornadoweb/tornado?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

`Tornado <http://www.tornadoweb.org>`_ is a Python web framework and
asynchronous networking library, originally developed at `FriendFeed
<http://friendfeed.com>`_.  By using non-blocking network I/O, Tornado
can scale to tens of thousands of open connections, making it ideal for
`long polling <http://en.wikipedia.org/wiki/Push_technology#Long_Polling>`_,
`WebSockets <http://en.wikipedia.org/wiki/WebSocket>`_, and other
applications that require a long-lived connection to each user.

Hello, world
------------

Here is a simple "Hello, blockexplorer" example web app for Tornado:

```
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("requires pip install torando")
        self.write("<br>")
        self.write("<br>")
        self.write("blockchain-transaction transaction hash here ")
        self.write("<br>")
        self.write("<br>")
        self.write("<br>")
        self.write("or this could be a css style gui with regular block-explorer output ")
        self.write("<br>")
        self.write("<br>")
        self.write("<br>")
        self.write("serving from bitcoin style wallet to wallet peer 8333 interchange 8888 or so via socket listen for requests incoming ports to serve out regular p2p design model ")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    ```
