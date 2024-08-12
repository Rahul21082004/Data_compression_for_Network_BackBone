import socket
import zlib
import os
import streamlit as st

def compress_data(data: bytes) -> bytes:
    """Compresses data using zlib."""
    return zlib.compress(data)

def send_data(file_path: str, host: str, port: int):
    """Reads a file, compresses its contents, saves intermediate compressed data, and sends it over a network socket."""
    try:
        filename = os.path.basename(file_path)  # Extract the original filename
        with open(file_path, 'rb') as file:
            data = file.read()

        # Compress the data
        st.info("Compressing data...")
        compressed_data = compress_data(data)

        # Save the compressed data to the "compressing" folder
        compressing_dir = 'compressing'
        os.makedirs(compressing_dir, exist_ok=True)
        compressed_file_path = os.path.join(compressing_dir, f"{filename}.txt")
        with open(compressed_file_path, 'wb') as file:
            file.write(compressed_data)
        
        st.info(f"Compressed data saved to {compressed_file_path}. Sending data...")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            # Send the filename length, filename, and compressed data
            s.sendall(len(filename).to_bytes(4, 'big') + filename.encode() + compressed_data)
            st.success(f"Data sent successfully from {file_path}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    """Main function to create the Streamlit interface for sending files."""
    st.title("Data Compression for Backbone Network - Sender")
    
    st.write("Select a file to send:")

    file_path = st.file_uploader("Choose a file", type=["txt", "csv", "png", "jpg", "pdf", "docx", "xlsx", "json", "xml", "zip", "gz"])

    if file_path is not None:
        # Write the file temporarily to disk
        temp_file_path = os.path.join("temp", file_path.name)
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
        with open(temp_file_path, "wb") as f:
            f.write(file_path.read())
        
        # Send button
        if st.button("Send File"):
            send_data(temp_file_path, 'localhost', 65432)

if __name__ == "__main__":
    main()
