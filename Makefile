rpcserver:
	PYTHONPATH=`pwd` python json-rpc-server.py
proxy:
	python amqp-rpc-proxy.py
amqp:
	python amqp-publisher.py "$${MESSAGE}"
