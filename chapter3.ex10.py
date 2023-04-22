# number=int(input())
# price_quality_list=[]
# i=1
# while i<=number:
#     price_quality=map(int,input().split())
#     price_quality_list.append(list(price_quality))
#     i+=1
#
# # print(price_quality_list)
# a=0
# a1=[]
# for i in range (len(price_quality_list)):
#     print("i= ",i)
#     print(price_quality_list[i][0])
#     if price_quality_list[i][0]>price_quality_list[i][1]:
#         a="false"
#         a1.append(a)
#     else:
#         a="true"
#         a1.append(a)
# print("a1= ",a1 )
# b=a1.count("false")
# c=a1.count("true")
# if c>b:
#     print("happy irsa")
# else:
#     print("poor irsa")
number=int(input())
price_quality_list=[]
i=1
while i<=number:
    price_quality=map(int,input().split())
    price_quality_list.append(list(price_quality))
    i+=1

# print(price_quality_list)
a=0
for i in range (len(price_quality_list)):
    if price_quality_list[i][0]<=price_quality_list[i][1] and price_quality_list[i-1][0]<=price_quality_list[i][0]:
        a="false"
    else:
        a="true"

if a=="true":
    print("happy irsa")
else:
    print("poor irsa")
