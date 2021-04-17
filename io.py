# IN = input directory
# OUT = output directory

def savepic(image_id, IN, OUT):
    for _id in image_id:
        img = cv2.imread(os.path.join(IN, _id))        
        cv2.imwrite("{}/{}".format(myoutput, _id), img)
