from carrot.connection import BrokerConnection
from carrot.messaging import Publisher

import sys

conn = BrokerConnection(hostname="localhost", port=5672,
    userid="guest", password="guest",
    virtual_host="/")

publisher = Publisher(connection=conn,
    exchange="sorting_room",
    routing_key="jason")

publisher.send({"po_box": sys.argv[1]})
publisher.close()
