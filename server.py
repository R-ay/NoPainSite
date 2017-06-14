#!/usr/bin/python3

import http.server

PORT = 8888
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/mnt/c/Users/R-ay/Documents/EPITA COURS/Projet_S2/No-Pain-Site$"]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()
