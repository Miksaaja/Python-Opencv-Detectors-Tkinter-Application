from tkinter import *
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector

###########################
# Reading config.txt file
configFile = open("config.txt", "r")
maxFaces = configFile.read()
maxFaces = maxFaces.replace("maxFaces=", "")
print("Loading config file...")
if maxFaces == "":
    maxFaces = 1
elif maxFaces == "0":
    maxFaces = 1
    print("0 is not recognised, changing to 1...")
print("Ready")
maxFaces = int(maxFaces)
###########################

MeshDetector = FaceMeshDetector(maxFaces=int(maxFaces))
HeadDetector = FaceDetector()

app = Tk()
app.geometry("300x300")
app.title("Detectors")

def faceMesh():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        img, faces = MeshDetector.findFaceMesh(img)
        if cv2.waitKey(1) == ord("q"):
            cv2.destroyWindow("Face Mesh Detector")
            return
        cv2.imshow("Face Mesh Detector", img)
        cv2.waitKey(1)

def faceDetectoring():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        img, faces = HeadDetector.findFaces(img)
        if cv2.waitKey(1) == ord("q"):
            cv2.destroyWindow("Face Detector")
            return
        cv2.imshow("Face Detector", img)
        cv2.waitKey(1)

faceDetector_btn = Button(text="Face Detector", command=faceDetectoring)
faceDetector_btn.pack()

faceMeshDetector_btn = Button(text="Face Mesh Detector", command=faceMesh)
faceMeshDetector_btn.pack()

app.mainloop()
