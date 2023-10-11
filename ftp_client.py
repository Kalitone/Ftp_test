import os
from ftplib import FTP

def main():
    ftp = FTP()
    ftp.connect('localhost', 2121)
    ftp.login(user='user', passwd='12345')
    
    print(ftp.getwelcome())
    
    while True:
        # List the files in the current directory
        ftp.retrlines('LIST')
        
        # Ask user for action choice
        action = input("Do you want to upload or download a file? (Enter 'u' for upload, 'd' for download, 'q' to quit): ").lower()
        
        if action == 'u':
            # List the first 5 files in the Downloads directory
            download_path = 'C:/Users/bradl/Downloads'   # Change this to your Downloads directory
            files = os.listdir(download_path)
            print("First 5 files in your Downloads directory:")
            for file in files[:5]:
                print(file)
            
            # Prompt user for the file to upload
            filename_to_upload = input("Enter the name of the file you want to upload: ")
            with open(f'{download_path}/{filename_to_upload}', 'rb') as f:
                ftp.storbinary(f'STOR {filename_to_upload}', f)
            
            # List the files again to show the new file
            ftp.retrlines('LIST')
        
        elif action == 'd':
            # Prompt user for the file to download
            filename_to_download = input("Enter the name of the file you want to download: ")
            downloaded_filename = f'downloaded_{filename_to_download}'
            # Download the file
            with open(downloaded_filename, 'wb') as f:
                ftp.retrbinary(f'RETR {filename_to_download}', f.write)
        elif action == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
    
    ftp.quit()

if __name__ == "__main__":
    main()