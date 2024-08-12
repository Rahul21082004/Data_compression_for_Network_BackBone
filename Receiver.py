import socket
import zlib
import os
import streamlit as st

def decompress_data(compressed_data: bytes) -> bytes:
    """Decompresses data using zlib."""
    return zlib.decompress(compressed_data)

def receive_data(host: str, port: int):
    """Receives compressed data over a network socket, decompresses it, saves intermediate decompressed data, and saves to a file."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            st.info(f"Listening on {host}:{port}...")

            conn, addr = s.accept()
            with conn:
                st.info(f"Connected by {addr}")
                
                # Receive the filename length
                filename_length_bytes = conn.recv(4)
                filename_length = int.from_bytes(filename_length_bytes, 'big')

                # Receive the filename
                filename = conn.recv(filename_length).decode()

                # Receive the compressed data
                compressed_data = conn.recv(1024 * 1024)  # Buffer size of 1 MB

                # Decompress the received data
                st.info("Decompressing data...")
                data = decompress_data(compressed_data)
                
                # Ensure the decompression directory exists
                decompressing_dir = 'decompressing'
                os.makedirs(decompressing_dir, exist_ok=True)
                
                # Save the decompressed data to the "decompressing" folder
                decompressed_file_path = os.path.join(decompressing_dir, f"{filename}.txt")
                with open(decompressed_file_path, 'wb') as file:
                    file.write(data)

                # Ensure the output directory exists
                output_dir = 'received_data'
                os.makedirs(output_dir, exist_ok=True)

                # Save the decompressed data to a file with its original name
                output_file_path = os.path.join(output_dir, filename)
                with open(output_file_path, 'wb') as file:
                    file.write(data)
                
                st.success(f"Data received and saved as {output_file_path}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    """Main function to create the Streamlit interface for receiving files."""
    st.title("Data Compression for Backbone Network - Receiver")
    
    if st.button("Start Receiving"):
        receive_data('localhost', 65432)

if __name__ == "__main__":
    main()
