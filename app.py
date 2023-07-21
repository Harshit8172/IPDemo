import socket
from flask import Flask, render_template

app = Flask(__name__)

def get_user_private_ip_address():
    request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    request.connect(("8.8.8.8", 53))
    ip_address = request.getsockname()[0]
    request.close()

    private_ip_prefixes = ('10.', '172.', '192.')
    for prefix in private_ip_prefixes:
        if ip_address.startswith(prefix):
            return ip_address

    return None

@app.route('/')
def index():
    private_ip = get_user_private_ip_address()
    return render_template('index.html', private_ip=private_ip)

if __name__ == '__main__':
    app.run(debug=True)
