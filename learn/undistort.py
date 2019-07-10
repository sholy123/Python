import cv2
import numpy as np
import os
path1 = "/home/sholy/Downloads/test/"
path2 = "/home/sholy/Downloads/undist/"
fx = 1841.29028307
fy = 1842.71788097
cx = 949.28771889
cy = 616.44805651

k1 = -0.46343471
k2 = 0.20453796
p1 = -0.0030903
p2 = 0.00271804
k3 = 0 

mtx = np.array([[fx, 0, cx],[0, fy, cy],[0, 0, 1]])
print(mtx)
dist = np.array([[k1],[k2],[p1],[p2]])
print(dist)
count = 0


filelist = os.listdir(path1)
for file in filelist:
    img = cv2.imread(path1+file)
    h, w = img.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),0,(w,h))
    # print(roi)
    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
    dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
    # print(dst.shape)
    x,y,w,h = roi
    dst = dst[y:y+h, x:x+w]
    print(dst.shape)
    cv2.imwrite(path2 + str(count)+'.jpg', dst)
    count = count+1







