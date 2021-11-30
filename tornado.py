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
