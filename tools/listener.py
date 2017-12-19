import socket
import requests

def get_external_ip(cache={}):
    if 'ip' in cache:
        return cache['ip']
    r = requests.get('https://ipv4.jsonip.com')
    ip = r.json()['ip']
    cache['ip'] = ip
    return ip

def listen_once(port, connection_timeout=60, read_timeout=5):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen()
    print("Listening on port", port)
    s.settimeout(connection_timeout)
    conn, addr = s.accept()
    s.close()
    print ("New connection from", addr)
    conn.settimeout(read_timeout)
    
    out = b""
    while True:
        try:
            block = conn.recv(512)
        except socket.timeout:
            block = None
        if not block:
            break
        out += block
    conn.close()
    return out

if __name__ == "__main__":
    resp = listen_once(44445)
    print(resp)
