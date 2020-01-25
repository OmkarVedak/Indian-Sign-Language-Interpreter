def rev(txt):
	import cv2
	import numpy as np

	# print("Say something !!!")
	# say = input()

	mylist = []

	for x in txt :
		if x == " ":
			continue

		img = cv2.imread("TrainData\\" + x + "_1.jpg")
		mylist.append(img)


	result = np.concatenate(mylist, axis = 1)
	cv2.imshow(txt, result)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
		
if __name__ == "__main__":
	
	rev(input("Say Something !!\n"))