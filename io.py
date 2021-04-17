# image_id = list with the images name
# IN = input directory
# OUT = output directory

def savepic(image_id, IN, OUT):
    if not os.path.isdir(OUT):
        os.mkdir(OUT)
    for _id in image_id:
        img = cv2.imread(os.path.join(IN, _id))        
        cv2.imwrite("{}/{}".format(OUT, _id), img)
