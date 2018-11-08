def quicksort(list):
	if len(list) <= 1:
		return list
	else:
		smaller = [x for x in list[1:] if x < list[0]]
		bigger = [x for x in list[1:] if x >= list[0]]
		return quicksort(smaller) + [list[0]] + quicksort(bigger)

#if __name__== '__main__':
#	list = [1,4,2,3,5]
#	print(quicksort(list))