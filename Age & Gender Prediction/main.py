import cv2
from deepface import DeepFace

img=cv2.imread('vince.jpg')

results = DeepFace.analyze(img,actions=('gender','age','race'))

print(results)