import jsonrpclib
from carrot.connection import BrokerConnection
from carrot.messaging import Consumer

conn = BrokerConnection(hostname="localhost", port=5672,
    userid="guest", password="guest",
    virtual_host="/")

consumer = Consumer(connection=conn,
    queue="po_box",
    exchange="sorting_room",
    routing_key="jason"
    )

def amqp_callback(message_data, message):
    server = jsonrpclib.Server('http://localhost:8080')
    server.ping(message_data)
    print jsonrpclib.history.response
    message.ack()

consumer.register_callback(amqp_callback)
consumer.wait() # Go into the consumer loop.
conn.close()
