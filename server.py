import http.server
import socketserver
import os
import ssl

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    cert_path = "cert.pem"
    key_path = "key.pem"
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(cert_path, key_path)
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
            print(f"Serving at https://localhost:{PORT}")
            httpd.serve_forever()
    except FileNotFoundError:
        print("SSL certificate files not found. Serving HTTP only. To enable HTTPS, place cert.pem and key.pem in the project directory.")
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at http://localhost:{PORT}")
            httpd.serve_forever() 