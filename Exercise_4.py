# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  # dividing the array
	if len(arr) > 1:
		mid = len(arr) // 2
		lhs = arr[0: mid]
		rhs = arr[mid:]
		mergeSort(lhs)
		mergeSort(rhs)

    # merging the array
		i, j = 0,0
		k = 0
		# merge_list =[]
		while i < len(lhs) and j < len(rhs):
			if lhs[i] < rhs[j]:
				arr[k] = lhs[i]
				# merge_list.append(lhs[i])
				i += 1
			else:
				arr[k] = rhs[j]
				# merge_list.append(rhs[j])
				j +=1 
			k += 1
		while i < len(lhs):
			arr[k] = lhs[i]
			# merge_list.append(lhs[i])
			i += 1
			k += 1
		while j < len(rhs):
			arr[k] = rhs[j]
			# merge_list.append(rhs[j])
			j +=1
			k +=1


# Code to print the list 
def printList(arr): 
    
    #write your code here
	print(arr)

# driver code to test the above code 
arr = [12, 11, 13, 5, 6, 7]  
print("Given array is", arr)  
printList(arr) 
mergeSort(arr) 
print("Sorted array is: ",arr) 
printList(arr) 
