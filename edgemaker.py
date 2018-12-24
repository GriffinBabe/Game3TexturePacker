import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import sys
from os import listdir
from os.path import isfile, join, isdir

_color_blue = [51, 102, 204, 255]
_color_red = [250, 61, 61, 255]


def detect_alpha_edges(img_array):
	"""Returns an array with the position of the first points 
	in the transparent/colored border in the transparent size"""
	coords_array = []
	previous_alpha = 0
	for line_index in range(0, len(img_array)):
		for row_index in range(0, len(img_array[line_index])):
			"""img_array[line_index][row_indew] is an array
			of 4 values corresponding to RGBa """
			if line_index > 0 and row_index > 0 and line_index < len(img_array)-1 and row_index < len(img_array[0])-1:
				if img_array[line_index][row_index][3] != 0 and img_array[line_index][row_index-1][3] == 0:
					coords_array.append((line_index, row_index-1)) #Appends a tupple with the coordinates
				if img_array[line_index][row_index][3] != 0 and img_array[line_index][row_index+1][3] == 0:
					coords_array.append((line_index, row_index+1))
				if img_array[line_index][row_index][3] != 0 and img_array[line_index-1][row_index][3] == 0:
					if (line_index-1, row_index) not in coords_array:
						coords_array.append((line_index-1, row_index))
				if img_array[line_index][row_index][3] != 0 and img_array[line_index+1][row_index][3] == 0:
					if (line_index+1, row_index) not in coords_array:
						coords_array.append((line_index+1, row_index))
	return coords_array


def create_empty_array(height, width):
	"""Input: a list with (x, y) tuple indicating the coordinates:
		Output: a numpy array containing a 2D matrix with 4 elements for each point of the matrice"""
	array = np.zeros( (len(img_array),  len(img_array[0]), 4), dtype=np.uint8 )
	return array


def thicken_edges(img_array, coordinates, color):
	for coord in coordinates: #coord = (x,y)
		cv2.circle(img_array, (coord[1], coord[0]), 1, color, thickness=3)
		img_array[coord[0]][coord[1]][3] = 255
	return img_array

def count_non_alpha_pixels(img_array):
	count = 0
	for line in img_array:
		for pixel in line:
			if pixel[3] != 0:
				count += 1
	print(count)
	return count


"""
old_time = time.time()

img = cv2.imread("s.png", -1)
img_array = np.array(img)
coordinates = detect_alpha_edges(img_array)
new_array = create_empty_array(len(img_array), len(img_array[0]))
new_array = thicken_edges(new_array, coordinates, _color_blue)

new_time = time.time()
print("Coord calculation took {} seconds.".format(new_time-old_time))



cv2.imwrite('image2.png', cv2.cvtColor(new_array, cv2.COLOR_RGBA2BGRA))
plt.imshow(new_array)
plt.show()
"""

file_count = 0
for d in listdir('in/'):
	for f in listdir('in/'+d):
		file_count += 1

completed_file = 1

for d in listdir('in/'):
	for f in listdir('in/'+d):
		old_time = time.time()

		img = cv2.imread('in/{}/{}'.format(d,f), -1)
		img_array = np.array(img)
		coordinates = detect_alpha_edges(img_array)
		new_array = create_empty_array(len(img_array), len(img_array[0]))
		new_array = thicken_edges(new_array, coordinates, _color_blue)
		cv2.imwrite('out/{}/{}'.format(d,f), cv2.cvtColor(new_array, cv2.COLOR_RGBA2BGRA))

		new_time = time.time()
		completed_file += 1
		print("Image process took {} seconds. Now processing file {}/{}".format(new_time-old_time, completed_file, file_count))
