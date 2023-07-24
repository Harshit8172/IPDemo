import socket
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def get_public_ip():
    # Get the client's public IP address from the request headers
    client_ip = request.remote_addr
    print("IP address is =", client_ip)
    return f"Hello! Your Public IP Address: {client_ip}"

if __name__ == '__main__':
    app.run(debug=True)
