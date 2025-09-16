############ Tuple #######
#Immutable

#creating a tuple
tup1=(1,2,3)
print(tup1)
print(type(tup1))

#access element in tuple
print(tup1[0])
print(tup1[1])

## unpacking the tupple
x,y,z=tup1
print(x)

####### sets #####

fruits={"apple","mango","banana","cherry"}
print(fruits)
print(type(fruits))

## add item in set

fruits.add("banana")
fruits.add("pinapple")
print(fruits)

## removing items from sets

fruits.remove("apple")
print(fruits)

### in and not in

print("banana" not in  fruits)
print("guava" in fruits)
print("apple" in fruits)

result="mango" in fruits
print(result)


#########################
   #Intersection :  same items are present in both sets
#########################
favourite_fruit={"apple","mango","banana","cherry","watermelon","licchi","lal","kalajamun"}
red_color_fruit={"apple","cherry","watermelon","licchi","laljamun","lalpapita"}


favourite_red_fruit=favourite_fruit.intersection(red_color_fruit)
print(favourite_red_fruit)


#########################
   #Union  : all items are present in both set
#########################

union_of_fruits=favourite_fruit.union(red_color_fruit)
print(union_of_fruits)

print(len(union_of_fruits))

#########################
   #Difference
#########################

# setB -set A == setB
favourite_fruit_butnot_red = red_color_fruit.difference(favourite_fruit)
print(favourite_fruit_butnot_red)

# setA - setB = setA

favourite_fruit_butnot_red = favourite_fruit.difference(red_color_fruit)
print(favourite_fruit_butnot_red)
