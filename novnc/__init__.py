import os
import sys
import zipfile
import tempfile
import argparse

__author__ = "Im Geek (Ankush Bhagat)"
__version__ = "0.99.9"

# Construct the path to the data folder
base_path = os.path.dirname(os.path.abspath(__file__))

def extract_zip(zip_file_path, extract_to_path):
    # Check if the file exists
    if not os.path.exists(zip_file_path):
        print(f"The file {zip_file_path} does not exist.")
        return

    # Check if the specified directory exists, if not, create it
    if not os.path.exists(extract_to_path):
        os.makedirs(extract_to_path)
    
    # Open the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all contents to the specified directory
        zip_ref.extractall(extract_to_path)

# Example usage
zip_file_path = os.path.join(base_path, "resources/server.py")
server_path = os.path.join(tempfile.gettempdir(), 'novnc_server')

extract_zip(zip_file_path, server_path)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--listen",
    metavar="HOST:PORT",
    default="0.0.0.0:5800",
    help="Set proxy/webserver ip address and port to listen. (Default: http://[::]:5800)"
)

parser.add_argument(
    "--target",
    metavar="HOST:PORT",
    required=True,
    help="Set VNC ip address and port to target."
)

parser.add_argument(
    "-v", "--version",
    action="version",
    version=f"{__version__}"
    )

args = parser.parse_args()

# Define the proxy mapping
listen_host, listen_port = args.listen.split(":")
target_host, target_port = args.target.split(":")

def main():
    try:
        # Start the proxy server
        os.system(f"websockify.exe {listen_host}:{listen_port} {target_host}:{target_port} --web {server_path}")
    except (KeyboardInterrupt, Exception):
        sys.exit(0)
