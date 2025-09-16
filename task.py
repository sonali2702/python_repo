
# "Task": "Create a list of squares of numbers from 1 to 5"
'''"Out_put"=  [1, 4, 9, 16, 25]'''
list1=[]
for i in range(1,6):
    sqaure=i*2
    list1.append(sqaure)

print(list1)    

### better way 
list1=[i*2 for i in range(1,11)]
print(list1)

# "Task": "Create a list of even numbers from 1 to 10"
'''"Out_put"= [2, 4, 6, 8, 10]
'''
list2=[]
for i in range(1,11):
    if i%2 == 0:
        list2.append(i)
print(list2)

### beteer way 

list2=[ i for i in range(1,11) if i%2==0]
print(list2)
    

# "Task": "Convert the list ['apple', 'banana', 'cherry'] to uppercase"
'''"Out_put"= ['APPLE', 'BANANA', 'CHERRY']
'''
list3=["apple","banana","cherry","gauva"]
new_list=[]
for i in list3:
    new_list.append(i.upper())
print(new_list)

##### Better way ### 
new_list=[ item.upper() for item in list3]
print(new_list)


# "Task": "From range(1, 11), get only numbers divisible by 3"
'''"Out_put"= [3, 6, 9]'''
list4=[]
for i in range(1,11):
    if i%3==0:
        list4.append(i)
print(list4)

#### better way
list4=[ i for i in range(1,11) if i%3==0]
print(list4)

# "Task": "Get the length of each word in ['Python', 'is', 'fun']"
'''"Out_put"= [6, 2, 3]'''
word=['Python', 'is', 'fun']
len_word=[]

for ch in word:
   len_word.append(len(ch))
print(len_word)

#### better way 

len_word=[len(ch) for ch in word]
print(len_word)

# Task = flatten the list 
'''nested_list  = [['a', 'b'], ['d', 'c']]
output = ['a', 'b', 'd' ,'c' ]'''




'''🟢 Easy Dictionary Exercises with in / not in
'''
# Exercise 1: Simple Dictionary Lookup

fruits = {"apple": 10, "banana": 5, "mango": 8}

# # Check if "apple" is in the dictionary

print("apple" in fruits)      # True
print("grapes" not in fruits) # True

# 👉 Task for students:

# Try checking "banana" in fruits


# Try checking "orange" not in fruits



'''_____________________________________________________________________'''

# Exercise 2: Add Item Only If Not Present

stock = {}

# Add 'pen' only if not already present
if "pen" not in stock:
    stock["pen"] = 5

print(stock)  # {"pen": 5}

# 👉 Task:

# Add "pencil" only if not in stock.


# If "pen" is already in stock, Overwrite "pen" with new value.



'''______________________________________________________________'''

# Exercise 3: Count Word Manually
sentence = ["apple", "banana", "apple", "orange"]

counts = {}
for word in sentence:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)  # {'apple': 2, 'banana': 1, 'orange': 1}

# 👉 Task:

# Try with another list: ["cat", "dog", "cat", "dog", "dog"]
pets = ["cat", "dog", "cat", "dog", "dog"]
new_pet={}
for  item in pets:
    if item in new_pet:
        new_pet[item] +=1
    else:
        new_pet[item] = 1
        
print(new_pet)


'''______________________________________________________________________________'''

# Exercise 4: Student Attendance
attendance = {"Rahul": "Present", "Neha": "Absent"}

# Check if a student exists
print("Rahul" in attendance)   # True
print("Amit" not in attendance) # True

# 👉 Task:

# Add "Amit" as "Present" only if not already in attendance.


# Ask: "Is Neha in the attendance dictionary?"



'''__________________________________________________________________________'''


# Exercise 5: Letter Counter (Intro to Frequency Counter)

word = "balloon"
letters = {}

for ch in word:
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1

print(letters)                              # {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}


# 👉 Task:


# Try with "success".
letter1="success"
letter1_count={}

for word in letter1:
    if word in letter1_count:
        letter1_count[word] += 1
    else:
        letter1_count[word] =1
print(letter1_count)


# Try with "banana".
letter2='banana'
letter2_count={}

for ch in letter2:
    if ch in letter2_count:
        letter2_count[ch] += 1
    else:
        letter2_count[ch] =1
print(letter2_count)

'''__________________________________________________________________'''


'''
task:  digit to word
'''

number_list=[
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def digit_to_word(num:int):
    wrd=[]
    num=str(num)
    for i in num:
        wn=number_list[int(i)]
        wrd.append(wn)
    
    return " ".join(wrd)

print(digit_to_word(123))


print("hello")

'''
task : word cound 
'''

state = 'The cat is the dog when the cat is'
new_state ={}

state=state.lower()
state=state.split()
for word in state:
    if word in new_state:
        new_state[word] += 1
    else:
        new_state[word] = 1 
print(new_state)

'''
task :
Anagram Groups
Group words that are anagrams.

'''
#Example ["listen", "silent", "enlist", "rat", "tar"] → [["listen","silent","enlist"], ["rat","tar"]]


'''
task: anagram check
'''

word1 = 'tar'
word2 = 'rat'    
d1={}
d2={}

def is_anagram(w1, w2):
    for ch in w1:
        if ch in d1:
            d1[ch] += 1
        else:
            d1[ch] = 1 
    for ch in w2:
        if ch in d2:
            d2[ch] += 1
        else:
            d2[ch] =1
    
    return d1 == d2

print(is_anagram(word1 , word2))

'''
reverse string
'''
def reverse_string(string):
    empty_string=""
    for ch in string:
        empty_string=ch+empty_string
    return empty_string

print(reverse_string("sonali"))
print(reverse_string("damini"))
print(reverse_string("akash"))
print(reverse_string("nagesh"))
    
