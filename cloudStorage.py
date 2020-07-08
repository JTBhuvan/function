import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token="N3-jcTTuHnAAAAAAAAAADTVqZt71-ytjSYQ4KLUbfxR4CIjzOqi0IFHiaXkwNges"
    transferData=TransferData(access_token)
    file_from=input("enter the filefrom path to transfer")
    file_to=input("enter the full path to upload")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")
main()    