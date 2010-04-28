from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def ping(msg):
    print msg
    return msg

server = SimpleJSONRPCServer(('localhost', 8080))
server.register_function(pow)
server.register_function(lambda x,y: x+y, 'add')
server.register_function(ping, 'ping')
server.serve_forever()
