# mydict = {
#     101: "Ankit",
#     102:"Nikita",
#     103:"Anjali",
#     104:"Pratik",
#     101:"Isha",
#     104:"Rushii"
# }
# print(mydict)


# with the help of key we have to print or acces
# a = mydict[101]
# print(a)

#we will replace old values by new values
# mydict[102]='peter'
# print(mydict)

#only print key x=0,1
# for x in mydict:
#     print(x)

# only print values
# for x in mydict.values():
#     print(x)

#printing key and vales both
# for x,y in mydict.items():
#     print(x,y)

#adding a nre key:value pair
# mydict["mobile_no"] = 9623674923
# print(mydict)

# '''mydict["Department"] =" Mangement"
# print(mydict)'''

#pop()method remove pair by specific key name
# mydict.pop(101)
# print(mydict)


#Question
# tuple as a key 
# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

#2 key not put at a time
# a={'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr = {}                #  {1: 2, '1': 2}
# arr[1]=1
# arr['1']=2
# arr[1] +=1
# print(arr)
# sum=0
# for k in arr:  #k=1  ,'1'
#     sum +=arr[k]
# print(sum)


# my_dict ={}
# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4
# print(my_dict)
# sum=0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)    

# my_dict ={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:
#     sum +=my_dict[k]
#     print(sum)
#     print(my_dict)


# box = {}
# jars ={}
# creates ={}
# box['biscuit'] =1
# box['cake']=3
# jars['jam']=4
# creates['box']=box
# creates['jars']=jars
# print(len(creates[box]))


# question          _play role of key

# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])


# rec ={"Name": "Python","Age":"20"}
# r=rec.copy()
# print(id(r)==id(rec)) 

# rec ={"Name": "Python","Age":"20"}
# r=rec.copy()
# print(id(r)==id(rec)) 
# print(id(rec))

# rec ={"Name": "Python","Age":"20","Addr": "NJ","Coumtry":"USA"}
# id1=id(rec)
# del rec
# rec ={"Name": "Python","Age":"20","Addr": "NJ","Coumtry":"USA"}
# id2=id(rec)
# print(id1== id2)

#find the maximum val in dicto
#i/p={"A":50,"B":30,"C":70}
#o/p="C"
#dict={"A":50,"B":30,"C":70}
# print(max(dict))

# dict={"X":20,"Y":10,"Z":30}
# min_val = None
# for i in dict.values():
#     if min_val is None or i < min_val:
#         min_val = i
# print("Minimum value is:", min_val)

# i/p=[1,2,2,3,4,3,5]
#o/p=["1":1,"2":2,"3":3,"4":1,"5":1]
# Count frequency of elements

# arr = [1, 2, 2, 3, 4, 3, 5]
# result = {}
# for i in arr:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1

# print(result)


##IMP TOPic

# num=123 #321
# a=num%10  #a=3
# num=num//10 #num=12
# b=num%10 #num b=2
# # num//10 #c=1
# c=num//10 
# rev=a*100 + b*10 + c*1
# print(rev)
# num = 123456
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# e = num % 10
# num = num // 10
# f = num % 10
# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
# print(rev)

#currency
