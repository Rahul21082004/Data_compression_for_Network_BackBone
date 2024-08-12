# Data_compression_for_Network_BackBone

Data Compression for Backbone Networks
Overview
This project, developed by the Techno-Grads team, implements a robust data compression and decompression system designed for backbone networks. The system focuses on lossless data compression techniques to efficiently reduce data size for transmission without any loss of information. It includes a sender-receiver model where files are automatically compressed, transmitted, and decompressed upon reception, ensuring data integrity and efficiency.

Features
Multi-Compression Techniques: Utilizes multiple compression algorithms (e.g., Deflate, Gzip) for optimal data reduction.
Lossless Compression: Ensures no data loss during the compression and decompression process.
Automatic File Handling: Automatically compresses files before sending and decompresses them upon reception.
Streamlit GUI: User-friendly interface for uploading, sending, and receiving files.
Real-time Notifications: Displays notifications like "File sent successfully" and "File received and decompressed successfully."
Project Structure
markdown
Copy code
Data_compression/
│
├── src/
│   ├── compression/
│   │   ├── deflate_compression.py
│   │   ├── multi_compression.py
│   │   └── __init__.py
│   ├── network/
│   │   ├── sender.py
│   │   ├── receiver.py
│   │   └── __init__.py
│   ├── gui.py
│   └── __init__.py
│
├── README.md
├── requirements.txt
└── architecture.png
How It Works
Sender Side:

Users can upload a file through the Streamlit GUI.
The file is compressed using selected compression techniques.
Compressed data is sent over the network to the receiver.
Receiver Side:

The receiver listens for incoming compressed data.
Upon receiving, the data is automatically decompressed to its original form.
The decompressed file is displayed in the GUI, ensuring data integrity.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Data_compression.git
cd Data_compression
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run src/gui.py
Usage
File Upload: Use the Streamlit interface to upload the file you want to compress and send.
Sending Data: Enter the receiver’s IP address and port, then click "Send Data."
Receiving Data: On the receiver side, click "Receive Data" to decompress and display the file.

Future Enhancements
Multiple Receiver Support: Expand the system to handle multiple receivers.
Advanced Compression Algorithms: Integrate more advanced compression techniques for improved efficiency.
Security Enhancements: Add encryption to ensure data security during transmission.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you have suggestions or find any bugs.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Team Members: List the members of the Techno-Grads team.
Mentors/Support: Acknowledge any mentors or resources that supported the project.
This description provides an overview of the project, explains its functionality, includes installation instructions, and offers a glimpse into potential future enhancements. Customize it further according to your specific needs.
