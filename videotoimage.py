import cv2

# vc = cv2.VideoCapture('/home/sholy/Downloads/ffmpeg/test.mp4')
# c = 1
# if vc.isOpened():
#     rval,frame = vc.read()
# else:
#     rval = False
#
# timeF = 100
# while rval:   #循环读取视频帧
#     rval, frame = vc.read()
#     if(c%timeF == 0): #每隔timeF帧进行存储操作
#         cv2.imwrite('/home/sholy/Downloads/ffmpeg/'+str(c) + '.png',frame) #存储为图像
#     c = c + 1
#     cv2.waitKey(1)
# vc.release()
img = cv2.imread('/home/sholy/Downloads/ffmpeg/out85.jpg')
print(img.shape)