import socket
import os
from tqdm import tqdm

HOST = '54.87.5.240'
PORT = 9001

def download():
    
    file_name = input('Specify File to Download: ')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(f'DOWNLOAD\n{file_name}', 'utf8'))
    
        data = s.recv(1024).decode('utf-8')

        if data.startswith('1'):
            print('Downloading File...')
            with open(os.path.join('client_files', file_name), 'wb') as f:
                pbar = tqdm()
                while(1):
                    data = s.recv(1024)
                    if not data:
                        break
                    f.write(data)
                    pbar.update(1)
        
            print('File Successfully Downloaded!')
        else:
            print(data)

def upload():

    file_name = input('Specify File to Upload: ')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # make sure the requested file exists
        if os.path.exists(os.path.join('client_files', file_name)):
            
            s.sendall(bytes(f'UPLOAD\n{file_name}', 'utf8'))
            
            # read file in chunks and send them
            with open(os.path.join('client_files', file_name), 'rb') as f:
                pbar = tqdm()
                r = f.read(1024)
                while(r):
                    s.sendall(r)
                    r = f.read(1024)
                    pbar.update(1)

            print('File Sent Successfully!')
        
        else:
            print("File Doesn't Exist on Client")

if __name__ == '__main__':
    print('FTP Client')

    mode = int(input('What do you want to do?\n1. Download\n2. Upload\nEnter Choice: '))

    if mode == 1:
        download()
    elif mode == 2:
        upload()
    else:
        print('Please Select a Valid Option')
    