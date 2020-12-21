# Q: What does [::-1} do?
# Ans: [::-1] is used to reverse the order of an array or a sequence.
# [::-1] reprints a reversed copy of ordered data structures such as an array or a list. the original array or list remains unchanged.
import array as arr

My_Array = arr.array('i', [1, 2, 3, 4, 5])
print(My_Array[::-1])
