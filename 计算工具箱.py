#1.乘法表
# def Multipulication_table():
#     i=int(input("您想要几阶的乘法表？"))
#     for a in range(1,i+1):
#         j=1
#         while j<=a:
#             print(f'{j}*{a}=',j*a,end=' ')
#             if j==a:
#                 print("\n")
#             j+=1
# Multipulication_table()

#2.列表统计器
# data=(input('输入你要处理的数据：'))
# data_list=[float(x.strip()) for x in data.split(',')]
# print(f'当前列表：{data_list}')
# def average():
#     avg=sum(data_list)/len(data_list)
#     return avg
# def maximum():
#     max=data_list[0]
#     for i in data_list:
#         if i>max:
#             max=i
#             print(f'最大值：{max}')
#     return max
# def minimum():
#     min=data_list[0]
#     for i in data_list:
#         if i<min:
#             min=i
#             print(f'最小值：{min}')
#     return min
# def delete_duplicates():
#     unique_list=[]
#     for i in data_list:
#         if i not in unique_list:
#             unique_list.qppend(i)
#     print(f'去重后的列表：{unique_list}')
#     return unique_list
# requests=int(input('请输入你要进行的操作：1.平均值 2.最大值 3.最小值 4.去重:'))
# if requests==1:
#     print(f'平均值：{average()}')
# elif requests==2:
#     print(f'最大值：{maximum()}')
# elif requests==3:
#     print(f'最小值：{minimum()}')
# elif requests==4:    
#     print(f'去重后的列表：{delete_duplicates()}') 
# else:print("非法输入！请重新输入！")

#3.猜数字游戏
# import random
# num=random.randint(1,100)
# print("Welcome to the guess number game!I've already prepared a number for you toguess,it's betweeen 1 and 100.And you have 10 chances\n")
# guess_num=int(input("please enter your guess number:"))
# chances=1
# while chances<=10:
#     if guess_num<num:
#         print("Too low! Try again.","you still have",10-chances,'chances lest.\n')
#         guess_num=int(input("please enter your guess number again:"))
#         chances+=1
#     elif guess_num>num: 
#         print("Too high! Try again.you still have",10-chances,'chances left.\n')
#         guess_num=int(input("please enter your guess number again:"))
#         chances+=1
#     else:   
#         print(f"Congratulations! You've guessed the number in {chances} chances!")
#         break
#     if chances>10:
#         print(f"Sorry! You've used all 10 chances. The number was {num}.")

#4.筛选列表
# data=input("请输入一系列数据，以逗号分隔：")
# data_list=[float(x.strip()) for x in data.split(',')]
# print(f"当前列表是：{data_list}")
# def eve_numbers(data_list):
#     even_list=[]
#     for i in data_list:
#         if  i%2==0:
#             even_list.append(i)
#     print(f"偶数列表：{even_list}")
#     return even_list

# def odd_numbers(data_list):
#     odd_list=[]
#     for i in data_list:
#         if  i%2!=0:   
#             odd_list.append(i)
#     print(f"奇数列表：{odd_list}")
#     return odd_list

# def numbers_greater_than_10(data_list):
#     greater_than_10_list=[]
#     for i in data_list:
#         if   i>10:
#             greater_than_10_list.append(i)
#     print(f"大于10的数列表：{greater_than_10_list}")
#     return greater_than_10_list

# print("请选择你要进行的操作：1.筛选偶数 2.筛选奇数 3.筛选大于10的数")
# requests=int(input("请输入你的选择："))
# if requests==1:   
#     eve_numbers(data_list)
# elif requests==2:
#     odd_numbers(data_list)
# elif requests==3:
#     numbers_greater_than_10(data_list)
# else:print("非法输入！请重新输入！")  

#5.字符串统计
# scentence=input("请输入一段文本：")
# a=str(input("请输入你要统计的字符："))
# count=0
# for i in scentence:
#     if i==a:
#         count+=1
# print(f"字符'{a}'在文本中出现了{count}次！")

# #矢量计算器
# def vector_addition(vector1,vector2):
#     if len(vector1)!=len(vector2):
#         print("THEY SHOULD BE THE SAME DIMENTION!")
#         return None
#     if len(vector1)==len(vector2):
#         result = [a + b for a, b in zip(vector1, vector2)]
#         print(f"vector addition result is:{result}")

# def vector_reduction(vector1,vector2):
#     if len(vector1)!=len(vector2):
#         print("THEY SHOULD BE THE SAME DIMENTION!")
#         return None
#     if len(vector1)==len(vector2):
#         result = [a - b for a, b in zip(vector1, vector2)]
#         print(f"vector reduction result is:{result}")

# def vector_dot_product(vector1,vector2):
#     if len(vector1)!=len(vector2):
#         print("THEY SHOULD BE THE SAME DIMENTION!")
#         return None
#     if len(vector1)==len(vector2):
#         result = [a * b for a, b in zip(vector1, vector2)]
#         print(f"vector dot product result is:{result}")

# def vector_cross_product(vector1,vector2):
#     if len(vector1)!=len(vector2):
#         print("THEY SHOULD BE THE SAME DIMENTION!")
#         return None
#     if len(vector1)==len(vector2):
#         if len(vector1)==3:
#              result = [
#         v1[1] * v2[2] - v1[2] * v2[1],
#         v1[2] * v2[0] - v1[0] * v2[2],
#         v1[0] * v2[1] - v1[1] * v2[0],
#              ]
#              print(f"vector cross product result is:{result}")
#         else:print("CROSS PRODUCT IS ONLY DEFINED FOR 3-DIMENTIONAL VECTORS!")
#         return result
# vector1=[float(x.strip()) for x in input("请输入第一个向量，以逗号分隔：").split(',')]
# vector2=[float(x.strip()) for x in input("请输入第二个向量，以逗号分隔：").split(',')]
# print("请选择你要进行的操作：1.向量加法 2.向量减法 3.向量点积 4.向量叉积")
# requests=int(input("请输入你的选择：")) 
# if requests==1:   
#     vector_addition(vector1,vector2)    
# elif requests==2:   
#     vector_reduction(vector1,vector2)
# elif requests==3:
#     vector_dot_product(vector1,vector2)
# elif requests==4:
#     vector_cross_product(vector1,vector2)
# else:print("非法输入！请重新输入！")
