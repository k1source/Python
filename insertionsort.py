Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def insertionsort(Arr):
	for i in range(1,len(arr)):
		key = arr[i]

		
>>> def insertionsort(Arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j=i-1
		while j>=0 and key < arr[j]:
			arr[j+1]= arr[j]
			j-=1
		arr[j+1] = key

		
>>> 
>>> arr = [12,11,13,5,6]
>>> insertionsort(arr)
>>> print("sorted array is: ")
sorted array is: 
>>> for i in range(len(arr)):
	print(arr[i])

	
5
6
11
12
13
>>> 