# from org.transcrypt.stubs.browser import *
# import random

# def gen_random_int(number, seed):

# 	ls = []
# 	random.seed(seed)

# 	for i in range(number):

# 		ls.append(i)

# 	random.shuffle(ls)

# 	return ls
		

# 	pass

# def generate():
# 	number = 10
# 	seed = 200

# 	# call gen_random_int() with the given number and seed
# 	# store it to the variable array
# 	pass

# 	array = gen_random_int(number, seed)

	
# 	# convert the items into one single string 
# 	# the number should be separated by a comma
# 	# and a full stop should end the string.
# 	pass

# 	array_str = ""

# 	for i in array:

# 		i = str(i)

# 	array_str = ", ".join(array)

# 	array_str = array_str + "."

# 	# This line is to placed the string into the HTML
# 	# under div section with the id called "generate"	
# 	document.getElementById("generate").innerHTML = array_str

# def insertationsort(array):

# 	n = len(array)

# 	for i in range(1,n):

# 		temp = array[i]

# 		while(i> 0):

# 			if(temp < array[i-1]):
# 				array[i] = array[i-1]

# 			else: 
# 				break

# 			i -= 1
		
# 		array[i] = temp

		

# def sortnumber1():
# 	'''	This function is used in Exercise 1.
# 		The function is called when the sort button is clicked.

# 		You need to do the following:
# 		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
# 		- create a list of integers from the string of numbers
# 		- call your sort function, either bubble sort or insertion sort
# 		- create a string of the sorted numbers and store it in array_str
# 	'''
# 	pass

# 	array_str = document.getElementById("generate").innerHTML

# 	array_str = array_str[:-1]
# 	array= array_str.split(", ")

# 	insertationsort(array)

# 	for i in array:

# 		i = str(i)

# 	array_str = ", ".join(array)
# 	array_str += "."
	
# 	document.getElementById("sorted").innerHTML = array_str

# def sortnumber2():
# 	'''	This function is used in Exercise 2.
# 		The function is called when the sort button is clicked.

# 		You need to do the following:
# 		- Get the numbers from a string variable "value".
# 		- Split the string using comma as the separator and convert them to 
# 			a list of numbers
# 		- call your sort function, either bubble sort or insertion sort
# 		- create a string of the sorted numbers and store it in array_str
# 	'''
# 	# The following line get the value of the text input called "numbers"
# 	value = document.getElementsByName("numbers")[0].value

# 	# Throw alert and stop if nothing in the text input
# 	if value == "":
# 		window.alert("Your textbox is empty")
# 		return

# 	# Your code should start from here
# 	# store the final string to the variable array_str
# 	#Converting String into a list for sorting
# 	value = value.replace(" ","") 				#Remove any possible space that user type
# 	array = list(value.split(","))				#Split them based on , and convert them to list for sorting


# 	for i in range(len(array)): #Issue
		
# 		try:
# 			array[i] = float(array[i])
# 		except ValueError:
# 			window.alert("Invalid Symbols. Please key in numbers and seperate it by comma!") 	#Exit when there is non-number
# 			return 
		
# 		if array[i] != array[i]:
# 			window.alert("Invalid Symbols. Please key in numbers and seperate it by comma!")
# 			return
		
# 	#Insertion Sort
# 	n = len(array)
# 	for outer_index in range (1,n):
# 		inner_index = outer_index
# 		temp = array[inner_index]
# 		while (inner_index>0 and temp < array[inner_index-1]):
# 			array[inner_index] = array[inner_index-1]
# 			inner_index= inner_index - 1
# 		array[inner_index] = temp


# 	#Convert List into String
# 	array_str = ""
# 	for i in range(n):
# 		array_str += array[i]
# 		if (i+1) != n:
# 			array_str += ","
	
	
# 	document.getElementById("sorted").innerHTML = array_str


from org.transcrypt.stubs.browser import *
import random


def gen_random_int(number, seed):

	ls = []
	random.seed(seed)

	for i in range(number):

		ls.append(i)

	random.shuffle(ls)

	return ls
		



def list_to_string(array): #convert list to string
	array_str = ""
	for i in array:
		i = str(i)

	array_str = ", ".join(array)
	array_str += "."
	return array_str
	
	


def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array

	array = gen_random_int(number, seed)

	
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = list_to_string(array)
    # This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def insertionsort(array): #insertion sort

	n = len(array)

	for i in range(1,n):

		temp = array[i]

		while(i> 0):

			if(temp < array[i-1]):
				array[i] = array[i-1]

			else: 
				break

			i -= 1
		
		array[i] = temp

		

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''

	array_str = document.getElementById("generate").innerHTML

	array_str = array_str[:-1]
	array= array_str.split(", ")
	insertionsort(array)
	
	array_str = list_to_string(array)
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	#Processing of input
	value = value.replace(" ","") 				#Remove any possible space that user type
	array = list(value.split(","))				#Split them based on , and convert them to list for sorting

	#To check the validity of input
	for i in range(len(array)): 
		
		try:
			array[i] = float(array[i])
		except ValueError:
			window.alert("Invalid Symbols. Please key in numbers and seperate it by comma!") 	#Error when there is non-number
			return 
		
		if array[i] != array[i]:
			window.alert("Invalid Symbols. Please key in numbers and seperate it by comma!")	#Account for NaN cases 
			return

    
	insertionsort(array)
	array_str = list_to_string(array)

	document.getElementById("sorted").innerHTML = array_str



