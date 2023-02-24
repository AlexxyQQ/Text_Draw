import numpy as np
import sys
import math
from tkinter import filedialog as fd


def create_text(arr):
    file = fd.asksaveasfile(mode='w', defaultextension=".txt")
    print(file.name)
    with open(f'{file.name}', 'w') as f:
        for i in arr:
            for j in i:
                if j == 1:
                    f.write('!')
                elif j == 2:
                    f.write('@')
                elif j == 3:
                    f.write('#')
                elif j == 4:
                    f.write('$')
                else:
                    f.write('0')
            f.write('\n')
    sys.exit()


def downsample_array(factor, grid_state):

    # Define the scale factor
    scale_factor = factor

    # Create a 2D NumPy array with random values
    arr = np.array(grid_state)
    # Determine the new dimensions of the downscaled array
    new_dim = tuple(np.array(arr.shape) // scale_factor)

    # Create a new, downscaled array
    downscaled_arr = np.zeros(new_dim)

    # Iterate over the downscaled array and compute the average of the corresponding elements in the original array
    for i in range(new_dim[0]):
        for j in range(new_dim[1]):
            orig_i = i * scale_factor
            orig_j = j * scale_factor
            downscaled_arr[i, j] = math.ceil(np.mean(
                arr[orig_i:orig_i+scale_factor, orig_j:orig_j+scale_factor]))

    create_text(downscaled_arr)
