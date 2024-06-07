import cv2
img=cv2.imread("solar-system.jpg")

cv2.putText(img,"sun",(20,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,255,255))
cv2.putText(img,"mercury",(150,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"venus",(200,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(img,"earth",(300,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(img,"mars",(370,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(img,"jupiter",(600,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(img,"saturn",(800,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(img,"uranus",(970,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(img,"neptune",(1100,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.imshow("output",img)
cv2.waitKey(0)