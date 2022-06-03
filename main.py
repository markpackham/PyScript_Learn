import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

pyscript.write('output', f"{arr}")

def shuffle_array(*args):
    pyscript.write('output','This works')