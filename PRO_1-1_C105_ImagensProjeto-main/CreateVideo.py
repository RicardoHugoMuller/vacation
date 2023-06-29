import os
import cv2


path = "c:/Users/mary_/Downloads/PRO_1-1_C105_ImagensProjeto-main/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
alt=cv2.VideoWriter("Ferias.mp4",cv2.VideoWriter_fourcc(*"DIVX"),1,size)
for i in range(count-1,0,-1):
    frame=cv2.imread(images[i])
    alt.write(frame)
alt.release()
print("YOU WIN")