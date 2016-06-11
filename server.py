import BaseHTTPServer, CGIHTTPServer
adr = ("", 80)
serv = BaseHTTPServer.HTTPServer(adr, CGIHTTPServer.CGIHTTPRequestHandler)
serv.serve_forever()

