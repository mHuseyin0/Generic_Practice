import cv2

height = 1400
width = 2048
xScalar = .5
yScalar = .5
realHeight = int(height*yScalar)
realWidth = int(width*xScalar)
margin = 50
rectHeight = 200
rectWidth = 250
circleRadius = 100
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread("Screen.jpg", cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, (width, height))
img = cv2.resize(img, (0,0), fx=xScalar, fy=yScalar) # Second argument must be (0,0) to multiply the size by some number.
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img = cv2.line(img,(0, margin),(realWidth, realHeight-margin),(100,100,100),3)
img = cv2.rectangle(img, (0, realHeight-margin-rectHeight), (rectWidth, realHeight-margin), (240,200,200), -1)
img = cv2.circle(img, (int(realWidth/2),int(realHeight/2)), circleRadius, (10,10,230), int(1.9*circleRadius))
img = cv2.putText(img, "TES(X)T", (int(realWidth/4), int(realHeight/2)), font, 5,(0,0,0), 4, cv2.LINE_AA)
cv2.imwrite("CV2Image.jpg", img)

print(img.shape) # height (px), width (px), channels (rgb, bgr)
print(img.shape[1])
a = 0
for i in range(margin):
    for j in range(img.shape[1]):
        img[i][j] = [255, a, a]
    a += 5

pattern = img[0:margin][0:realWidth+1]

img[realHeight:(realHeight-margin-1):-1][0:realWidth+1] = pattern

cv2.imshow("Image",img)
cv2.waitKey(0) # Max seconds to wait.(0 means infinite) If any key is pressed during this time program will pass to the next line.
cv2.destroyAllWindows()