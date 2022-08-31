import numpy as np
import cv2

solar = cv2.imread("solar-system.jpg")
imshow = ("Solarsystem",solar)
cv2.putText(solar, "Sol", (100,180),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255)) 
cv2.putText(solar, "Mercurio", (150,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
cv2.putText(solar, "venus", (200,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
cv2.putText(solar, "terra", (250,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
cv2.putText(solar, "marte", (300,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
cv2.putText(solar, "jupiter", (350,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
cv2.putText(solar, "saturno", (400,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))  
cv2.putText(solar, "urano", (450,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))  
cv2.putText(solar, "netuno", (500,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))  
cv2.waitKey(0)
