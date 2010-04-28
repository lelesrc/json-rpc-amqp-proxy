Prerequirements
---------------

* [carrot](http://github.com/ask/carrot)
		$ easy_install carrot

* [jsonrpclib](http://code.google.com/p/jsonrpclib/)
		Move to the cloned directory 
		  $ cd json-rpc-amqp-proxy
		  $ svn co http://jsonrpclib.googlecode.com/svn/trunk/jsonrpclib


Run
---
You need three terminals.

Terminal 1:
	$ make rpcserver

Terminal 2:
	$ make proxy

Terminal 3:
	$ make amqp MESSAGE="--message data--"

