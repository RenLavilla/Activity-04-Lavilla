import cv2
import os

while True:
	Fname = input("Name of your file[add '.jpg' at the end]:")

	if os.path.exists(Fname):
		imge= cv2.imread(Fname, 1)
		cv2.imshow(Fname, imge)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break

	else:
		print(" File name is invalid......................")