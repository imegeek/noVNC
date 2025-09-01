# noVNC

**noVNC** is a Python-based wrapper that bundles **websockify** and the **noVNC HTML client** to provide a **web-based VNC viewer**.It enables remote desktop access directly from the browser without requiring a standalone VNC client.

* * *

## ✨ Features

* **Easy Setup** – Start a proxy server in seconds and connect to your VNC server.
* **Web-based Access** – Use any modern browser as a VNC client.
* **Custom Arguments** – Supports both noVNC (`--listen`, `--target`) and all **websockify** options.
* **Secure Connection** – SSL/TLS support with `--ssl-only`, `--cert`, and `--key`.

* * *

## 📦 Requirements

* Python **3.7+**
* A running VNC server (e.g., **TigerVNC**, **TightVNC**, **RealVNC**)

* * *

## 🔧 Installation

### From PyPI

    pip install novnc

### From Source

1. Clone this repository:
  
      git clone https://github.com/ankushbhagats/noVNC
      cd noVNC
  
2. Install locally:
  
      pip install .
  

This installs **noVNC** and **websockify**.

* * *

## ⚙️ Options

| Option | Description | Default |
| --- | --- | --- |
| `--listen HOST:PORT` | Address and port to listen on for WebSocket + web server | `0.0.0.0:8080` |
| `--target HOST:PORT` | VNC server address and port to connect to | `127.0.0.1:5900` |
| `--web PATH` | Path to noVNC static files (auto-extracted to temp directory) | *(auto set)* |
| `--ssl-only` | Enable **TLS only** | Disabled |
| `--cert FILE` | Path to SSL certificate (PEM) | None |
| `--key FILE` | Path to SSL private key (PEM) | None |

> ✅ Any **websockify** arguments can also be passed through.

* * *

## 🚀 Usage

Start the proxy with your VNC server details:

    novnc --listen 0.0.0.0:8080 --target 127.0.0.1:5900

Then open in your browser:

    http://localhost:8080/vnc.html

* * *

## 🔒 HTTPS / WSS Setup

Generate a self-signed cert (for testing):

    openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem

Run with SSL:

    novnc --listen 0.0.0.0:443 --target 127.0.0.1:5900 --ssl-only --cert cert.pem --key key.pem

Access via:

    https://yourdomain.com/vnc.html

* * *

## 🛠 Troubleshooting

* **Connection refused** → Ensure your VNC server is running and reachable.
* **Black screen** → Verify the VNC server allows connections (sometimes password-protected).
* **Browser SSL warning** → Use a trusted CA (e.g., Let’s Encrypt) instead of self-signed certs.

* * *

## 📜 License

Licensed under the [MIT License](LICENSE).

* * *

## 🙏 Acknowledgments

* [noVNC](https://github.com/novnc/noVNC) – Browser-based VNC client (HTML5 + WebSockets)
* [websockify](https://github.com/novnc/websockify) – WebSockets proxy for any TCP service