import os
import glob
from PIL import Image

def CropAndResizeOCTimages(OCTBMPList):
    for OCTImage in OCTBMPList:
        img_name = os.path.splitext(os.path.basename(OCTImage))[0]
        img = Image.open(OCTImage)
        crop_img = img.crop((496,0,1264,496))
        crop_img = crop_img.resize((640,640))
        crop_img.save("../ERMSource/YOLOv5Source/"+img_name+".png")  # 저장할 경로

def CropIRimages(patientinfo,type):
    img = Image.open(f"./Data/OCT Data(Type{type})/{patientinfo}/sonh000.bmp")
    if type==1:
        IRimage = img.crop((0,0,496,496)) # Type1
    elif type==2:
        IRimage = img.crop((0,0,168,166)) # Type1
    IRimage.save(f"./Data/IR Image/{patientinfo} IRimage(Type{type}).png")  # 저장할 경로

CropIRimages("0000021587",2)
# CropAndResizeOCTimages(PatientOCTbmpGlob("0000002460_OD 2016-10-24"))