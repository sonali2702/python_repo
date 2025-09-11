count =0 

while True:
    count =count +1
    if count==3:
        continue
    print(f"looling count times{count}")
    if count>=10:
        break 
    
no=0
while no<10:

    if no%2==0:
         print(no)
    elif no%2==1:
        print(f"odd number {no}")
    else :
        print("nice ")
    no=no+1


########################

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

for i in range(0,5):
    message= ""
    for sub_message in range(i + 1):
         message += f"{sub_message}"
    print(message)







