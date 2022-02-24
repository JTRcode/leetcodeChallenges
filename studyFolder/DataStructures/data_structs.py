import array as arr
import numpy as np

list = [3, 6, 9, 12]
array_1 = arr.array("i", [3, 6, 9, 12])
array_2 = np.array(["numbers", 3, 6, 9, 12])
set = {3, 6, 9, 12}
tuple = (3, 6, 9, 12)
dic = {1:3, 2:6, 3:9, 4:12}

# TODO List functions

# Sorting 2 lists
list1 = [3,2,4,1, 1]
list2 = ['three', 'two', 'four', 'one', 'one2']
list1, list2 = zip(*sorted(zip(list1, list2)))
print(list1)
#(1, 1, 2, 3, 4)
print(list2) 
#('one', 'one2', 'two', 'three', 'four')
list1, list2 = zip(*sorted(zip(list1, list2), key=lambda x: x[1]))
print(list1)
#(1, 1, 2, 3, 4)
print(list2) 
#('one', 'one2', 'two', 'three', 'four')

# sort dictionary by value
dic = {1:3, 2:6, 3:9, 4:12}
sorted = sorted(dic.items(), key=lambda x: x[1])

# dynamic list