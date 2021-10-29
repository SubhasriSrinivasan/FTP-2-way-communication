import os
import socket
from tqdm import tqdm

HOST = '0.0.0.0'
PORT = 9001

print('FTP Server')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print(f'Client {addr} connected')

            data = conn.recv(1024).decode('utf-8')

            mode, file_name = data.split('\n')

            if mode == 'DOWNLOAD':
                print('Sending Files to Client...')

                # make sure the requested file exists
                if os.path.exists(os.path.join('server_files', file_name)):
                    
                    conn.sendall(b"1: Sending File")
                    
                    # read file in chunks and send them
                    with open(os.path.join('server_files', file_name), 'rb') as f:
                        pbar = tqdm()
                        
                        r = f.read(1024)
                        while(r):
                            conn.sendall(r)
                            r = f.read(1024)
                            pbar.update(1)

                    print('File Sent Successfully!')
                
                else:
                    conn.sendall(b"0: Requested File Doesn't Exist")
                    print("Requested File Doesn't Exist")

            elif mode == 'UPLOAD':
                print('Receiving Files from Client...')

                with open(os.path.join('server_files', file_name), 'wb') as f:
                    pbar = tqdm()
                    while(1):
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        pbar.update(1)
                
                print('File Successfully uploaded to Server!')