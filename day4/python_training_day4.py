# Q2.
# class Person:
#     def __init__(this,name,age):                 # instead of self other variable can also be used
#         this.name = name
#         this.age = age
        
# person1 = Person("Vihas",20)
# print(f"person1 is an object with name={person1.name} and age={person1.age}")

# Q3.
# class Person:
#     def __init__(this,name,age):              # constructor
#         this.name = name
#         this.age = age
        
#     def greet(self):
#         print(f"Hello, my name is {self.name}")
        
# person1 = Person("Vihas",20)
# person1.greet()

# Q4.
# class Person:
#     def __init__(this,name,age):              # constructor
#         this.name = name
#         this.age = age
        
# class Student(Person):
#     def __init__(this, name, age,student_id):
#         super().__init__(name, age)
#         this.student_id = student_id
        
#     def greet(self):
#         print(f"Hello, my name is {self.name} and my student id is {self.student_id}")
        
# person1 = Student("Vihas",20,1234567)
# person1.greet()

# Q5.
# class Person:
#     def __init__(this,name,age):              # constructor
#         this.name = name
#         this.age = age
        
# class Student(Person):
#     def __init__(this, name, age,student_id):
#         super().__init__(name, age)
#         this.student_id = student_id
        
#     @staticmethod
#     def hello():
#         print("Hello, I am a student")
        
#     def greet(self):
#         print(f"Hello, my name is {self.name} and my student id is {self.student_id}")
        
# obj = Student("Vihas",20,1234567)
# obj.hello()
# obj.greet()

"""     Always keep this structure in mind while writing a program         
                        ---------------------
                        |       INPUT       |
                        ---------------------
                                  |
                                  |
                        ---------------------
                        |     ALGORITHM     |
                        ---------------------
                                  |
                                  |
                        ---------------------
                        |       OUTPUT      |
                        ---------------------
                        
"""

# linear search
# def linear_search(input_list,element):
#     for index, value in enumerate(input_list):
#         if value == element:
#             return index
#     return -1
# input_list = [3,4,1,6,14]
# element = 4
# print("Index position for the element x is: ",linear_search(input_list,element))

# square the numbers
# def square_no(n):
#     sq_no = []
#     for number in n:
#         sq_no.append(number*number)
#     return sq_no
# ls=[2,4,5,6,8,9]
# print(square_no(ls))

# factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# binary search
# def binary_search(arr,low,high,key):
#     while low <= high:
#         mid = int(low+(high-low)/2)
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1

# arr = [2,3,4,2,10,40]
# x=10
# result = binary_search(arr,0,len(arr)-1,x)
# print(result)

# merge sort
# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     mid_point = int(len(arr)/2)
#     first_half = arr[:mid_point]
#     second_half = arr[mid_point:]
    
#     half_a = merge_sort(first_half)
#     half_b = merge_sort(second_half)
    
#     return merge(half_a,half_b)

# def merge(first_sublist,second_sublist):
#     i = j = 0
#     merged_list = []
#     while i < len(first_sublist) and j < len(second_sublist):
#         if first_sublist[i] < second_sublist[j]:
#             merged_list.append(first_sublist[i])
#             i += 1
#         else:
#             merged_list.append(second_sublist[j])
#             j += 1
            
#     while i < len(first_sublist):
#         merged_list.append(first_sublist[i])
#         i += 1
#     while j < len(second_sublist):
#         merged_list.append(second_sublist[j])
#         j += 1
#     return merged_list

# print(merge_sort([2,8,5,6,3,4,9,1]))


# bubble sort
# def bubble_sort(unordered_list):
#     iteration_number = len(unordered_list) - 1
#     for i in range(iteration_number,0,-1):
#         for j in range(i):
#             if unordered_list[j] > unordered_list[j+1]:
                # temp = unordered_list[j]
                # unordered_list[j] = unordered_list[j+1]
                # unordered_list[j+1] = temp
                # OR
#                 unordered_list[j],unordered_list[j+1]=unordered_list[j+1],unordered_list[j]
                
#     return unordered_list

# print(bubble_sort([8,3,4,6,9,7,2]))

# insertion sort
# def insertion_sort(unsorted_list):
#     for index in range(1,len(unsorted_list)):
#         search_index = index
#         insert_value = unsorted_list[index]
#         while search_index > 0 and unsorted_list[search_index-1] > insert_value:
#             unsorted_list[search_index] = unsorted_list[search_index-1]
#             search_index -= 1
#         unsorted_list[search_index] = insert_value
        
# my_list = [8,3,4,6,9,7,2]
# print("Before sorting: ",my_list)
# insertion_sort(my_list)
# print("After sorting: ",my_list)

# selection sort
# def selection_sort(unsorted_list):
#     size_of_list = len(unsorted_list)
#     for i in range(size_of_list):
#         min_index = i
#         for j in range(i+1,size_of_list):
#             if unsorted_list[j] < unsorted_list[min_index]:
#                 min_index = j
#         unsorted_list[i],unsorted_list[min_index] = unsorted_list[min_index],unsorted_list[i]
#     return unsorted_list

# print(selection_sort([8,3,4,6,9,7,2]))

# quick sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr.pop()
#     items_greater = []
#     items_lower = []
#     for item in arr:
#         if item > pivot:
#             items_greater.append(item)
#         else:
#             items_lower.append(item)
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# print(quick_sort([8,3,4,6,9,7,2]))


# calculate the blank space between 2 words
# def calculate_blank_space_between_words(sentence):
#     words = sentence.split()
#     print(words)
#     if len(words) < 2:
#         return 0
#     first_word_end = sentence.find(words[0]) + len(words[0])
#     print(sentence.find(words[0]))
#     second_word_start = sentence.find(words[1])
#     return second_word_start - first_word_end

# # Test cases
# print(calculate_blank_space_between_words("Hello    world"))  # Output: 4
# print(calculate_blank_space_between_words("Python  programming"))  # Output: 2
# print(calculate_blank_space_between_words("   Leading and trailing spaces   "))  # Output: 3
# print(calculate_blank_space_between_words("SingleWord"))  # Output: 0
# print(calculate_blank_space_between_words(""))  # Output: 0

# rearrange the positive integer
# def rearrange(arr):
#     positive_nums = [num for num in arr if num > 0]
#     negative_nums = [num for num in arr if num < 0]
    
#     result = []
#     i, j = 0,0
#     while i < len(negative_nums) or j < len(positive_nums):
#         if i < len(negative_nums):
#             result.append(negative_nums[i])
#             i += 1
#         if j < len(positive_nums):
#             result.append(positive_nums[j])
#             j += 1
#     return result
# arr = [-1, 2, -3, 4, 5, -6]
# print(rearrange(arr))  # Output: [-1, 2, -3, 4, -6, 5]
