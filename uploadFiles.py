from dropbox.files import WriteMode
import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        #upload a file to Dropbox using API v2
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to,relative_path)

        with open(local_path, 'rb', encode="utf-8") as f:
            dbx.files_upload(f.read(), dropbox_path, mode = WriteMode("overwrite"))

def main():
    access_token = 'sl.BH4s6G97Jv8ggRn9zTOi1-eVS29ccvwNypncnQhgvRKi1ZZ_gNdbyhRZKfMETfM1qfNGGYQ--yqyA145NvJfKmH47YXPBnq-OsRTHhvX8Ph-gh4vKL_T0418MQ3o6q3rDihvmVY'
    transferData = TransferData(access_token)

    file_from = 'C:\Users\Admin\Desktop\Python\PRO-C101\demo_folder'
    file_to = '/Project-2.0/demo_folder'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

    print("Your file has been uploaded!!!")

if __name__ == '__main__':
    main()