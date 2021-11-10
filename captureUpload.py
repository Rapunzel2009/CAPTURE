import dropbox
import random
import time
import cv2

startTime=time.time()

def take_snapshot():
    num=random.randint(1,100)
    #initialising camera module
    videoCaptureObject = cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #imwrite method is used to save an image
        img = "img"+str(num)+".png"
        cv2.imwrite(img,frame)
        startTime = time.time()
        result = False

    return img
    print("Snapshot Taken")
    #release the camera
    videoCaptureObject.release()
    #close all the windows that might open in the process
    cv2.destroyAllWindows()

def uploadFiles(img):
    access_token = "7hO-PCCfNtEAAAAAAAAAAQZOZ1mS_NzYL9K7ptaPl6Kx9JcdZfb_S3dADEQCfy3B"
    file = img
    file_from = img
    file_to = "/test/"+img

    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")
        
def main():
    while(True):
        if((time.time()-startTime) >= 1):
            name=take_snapshot()
            uploadFiles(name)

main()





    



