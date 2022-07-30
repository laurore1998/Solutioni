import numpy

lst = [13, 4, 20, 15, 6, 20, 20]

lst = numpy.array(lst)

result = numpy.where(lst == 20)

print(result)