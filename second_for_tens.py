import numpy
def second_for_tens():
    original_array = numpy.array(
    [[34, 43, 73],
    [82, 22, 12],
    [53, 94, 66]]) 
    new_column = numpy.array([[10,10,10]]) 
    
    original_array = numpy.delete(original_array, 1, 1)
    original_array = numpy.insert(original_array,1, new_column, 1)
    print(original_array)

second_for_tens()
