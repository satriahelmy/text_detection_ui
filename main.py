import cv2
import easyocr
import matplotlib.pyplot as plt

#import image
image_path = r'C:\Data\Portfolio\Computer Vision\text_detection\data\test1.jpeg'
img = cv2.imread(image_path)

#reader
reader = easyocr.Reader(['en'], gpu=False)

#detect
text_ = reader.readtext(img)

threshold = 0.25

for t in text_:
    bbox, text, score = t
    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()