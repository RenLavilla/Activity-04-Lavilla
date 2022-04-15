import cv2
filepath ="sooyaaa.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("sooyaaa",image)
cv2.waitKey(0)
cv2.destroyAllWindows()