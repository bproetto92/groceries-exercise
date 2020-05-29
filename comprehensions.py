# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here


#--------------
#ORIGINAL LIST: [1, 2, 3, 4, 5, 6, 7]
#--------------
#TOTAL COMPREHENSION...
#--------------
#MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]

#mapped_list = [____ for____in_____]
mapped_list = [i*100 for i in my_numbers]
print("MAPPED LIST",mapped_list)

new_numbers=[]
for i in my_numbers:
    new_numbers.append(i*100)

print("MAPPED LIST",new_numbers)


#--------------
#FILTERED LIST W/ MATCHES: [4, 5, 6, 7]

filtered_list = []
for i in my_numbers:
    if i >3:
        filtered_list.append(i)

print("FILTERED LIST",filtered_list)


#--------------
#FILTERED LIST W/O MATCHES: []
#--------------
#MAPPED AND FILTERED LIST: [400, 500, 600, 700]

