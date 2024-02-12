import cv2
import pytesseract

#location of installed tesseract-ocr
pytesseract.pytesseract.tesseract_cmd="C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

#read image from which text needs to be etxracted
img = cv2.imread('R.png')

#Starting the preprocessing of image

#converting the image to gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#performing OTSU threshold
ret, thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)


#specify the structure shape and kernel  size
'''
kernel size increases or decreases the area of the rectangle
to be detected.
A smaller value like (10,10) will detect each word
instead of a sentence
'''

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18,18))

#applying dilation on the threshold image
dilation = cv2.dilate(thresh1,rect_kernel,iterations=1)

#finding contours
contours,hierachy= cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#creating a copy of the image
im2 = img.copy()

#a text file is created and flushed
file=open('recognized.txt',"w+")
file.write("")
file.close()

'''
looping through the identified contours,
then rectangular part is cropped and passed on to
the pytesseract for extracting text from iy
The extracted text is then written into the text file
'''

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)

    #drawing a rectangle on copied image
    rect = cv2.rectangle(im2,(x,y),(x+w,y+h),(0,255,0),2)

    #cropping the text block for giving input to OCR
    cropped = im2[y:y+h,x:x+w]

    #open the file in append mode
    file = open('recognized.txt',"a")

    #applying ocr on the cropped image
    text = pytesseract.image_to_string(cropped)

    #appending the text into file
    file.write(text)
    file.write("\n")

    #closing the file
    file.close()