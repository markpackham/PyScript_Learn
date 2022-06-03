import numpy as np
import random
from utils import add_class

output_el = Element('output').element
# console.log(output_el)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# pyscript.write('output', f"{arr}")
output_el.innerHTML = f"{arr}"

def shuffle_array(*args):

    shuffled = sorted(arr, key=lambda k: random.random())

    # change color
    add_class(output_el, "text-blue-500")

    # pyscript.write('output',shuffled)
    output_el.innerHTML = shuffled