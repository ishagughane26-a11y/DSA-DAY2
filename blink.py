# print('ishagughane777'.isalnum())
# print('ishagughane'.isalpha())
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('ISHAg'.isupper())
# print('My Name Is Isha'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))


# print("Isha".find("r"))
# print("Isha".index("s"))
# print("isha gughane".count("t"))

#Question            (Nested loop)       
# 1 1 1 
# 2 2 2 
# 3 3 3
#------------------------------------------------------
#i=1  , j=  ,(i,j= )

# for i in range(1,5):      #outer loop ==>row's
#     for j in range(1,5):   # inner loop ==>col's
#         print(i,end ="  ")
#     print()    

#
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()    

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*",end=" ")
#     print() 

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print() 

#  use of sleep function
# import time
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(1)
#         print("*",end=" ")
#     print()    


#product of Array Except self:
#i/p=[1,2,3,4]
#o/p=[24,12,8,6]


            

arr= [1,2,3,4]
product = 1
for i in arr:
 product=product*i
for i in range(0,len(arr)):
    arr[i]=product//arr[i]
print(arr)

       