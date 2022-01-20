import dropbox

class TransferData:
    def __init_(self,access_token):
        self.access_token = access_token
    def Upload_File(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        relative_path = os.path.relapth(local_path,file_from)
        dropbox_path = os.path.join(file_to,relative_path)
        
            
        
        

        f = open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AbKQY7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kB4yn6O0erRD07aV-9JeaGvvRPoLFEVvwg3_p2AufnKjhGlCgTVtpR4YV0SKhk6nbU2-ztZAB'
    transferData = TransferData(access_token)
def file_to():
    if(fileName=="N"):
        file_from = input("Emter the file path to transfer:-")
        file_to = input("Enter the full path to upload to dropbox:-")
        

    

    transferData.upload_file(file_from,file_to)
    print("The file has been moved!!!")

main()   
    

