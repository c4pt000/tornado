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
<br>
<br>
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

Here is a simple "Hello, world" example web app for Tornado:

.. code-block:: python

    import tornado.ioloop
    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()

This example does not use any of Tornado's asynchronous features; for
that see this `simple chat room
<https://github.com/tornadoweb/tornado/tree/stable/demos/chat>`_.

Documentation
-------------

Documentation and links to additional resources are available at
https://www.tornadoweb.org
