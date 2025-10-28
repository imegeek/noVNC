import os
import sys
import zipfile
import tempfile
import argparse
from websockify import websockify_init

__author__ = "Ankush Bhagat"
__version__ = "1.1.6"

# --- Extract noVNC server zip ---
base_path = os.path.dirname(os.path.abspath(__file__))
zip_file_path = os.path.join(base_path, "resources/novnc_server.zip")
server_path = os.path.join(tempfile.gettempdir(), "novnc_server")

def extract_zip(zip_file_path, extract_to_path):
    if not os.path.exists(extract_to_path):
        os.makedirs(extract_to_path)
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extract_to_path)

extract_zip(zip_file_path, server_path)


def main():
    # --- Custom args (only parsed here) ---
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--listen", help="Listen address:port")
    parser.add_argument("--target", help="Target host:port")
    args, remaining = parser.parse_known_args()

    # --- Build sys.argv for websockify ---
    sys.argv = [sys.argv[0]]
    if args.listen and args.target:
        sys.argv += [args.listen, args.target]  # positional style
    sys.argv += ["--web", server_path]         # always inject web dir
    sys.argv += remaining                      # forward everything else

    # --- Hand over to websockify ---
    websockify_init()


if __name__ == "__main__":
    main()
