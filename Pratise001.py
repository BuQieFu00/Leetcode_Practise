"""
version 1.0
Author : Neo
"""
import math

###1

###2第一个python程序
# print("hello world")
# print("您好，世界")

###3python中的变量
##3.1
# """
# 使用变量保存数据并进行加减乘除运算
# """
# a = 45        # 定义变量a，赋值45
# b = 12        # 定义变量b，赋值12
# print(a, b)   # 45 12
# print(a + b)  # 57
# print(a - b)  # 33
# print(a * b)  # 540
# print(a / b)  # 3.75

##3.2
# """
# 使用type函数检查变量的类型
# """
# a = 100
# b = 123.45
# c = 'hello, world'
# d = True
# print(type(a))  # <class 'int'>
# print(type(b))  # <class 'float'>
# print(type(c))  # <class 'str'>
# print(type(d))  # <class 'bool'>

##3.3
# """
# 变量的类型转换操作
# """
# a = 100
# b = 123.45
# c = '123'
# d = '100'
# e = '123.45'
# f = 'hello, world'
# g = True
# print(float(a))         # int类型的100转成float，输出100.0
# print(int(b))           # float类型的123.45转成int，输出123
# print(int(c))           # str类型的'123'转成int，输出123
# print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
# print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
# print(float(e))         # str类型的'123.45'转成float，输出123.45
# print(bool(f))          # str类型的' hello, world '转成bool，输出True
# print(int(g))           # bool类型的True转成int，输出1
# print(chr(a))           # int类型的100转成str，输出'd'
# print(ord('d'))         # str类型的'd'转成int，输出100


###4 语言中的运算符！
##4.1
# """
# 算术运算符
# """
# print(321 + 12)     # 加法运算，输出333
# print(321 - 12)     # 减法运算，输出309
# print(321 * 12)     # 乘法运算，输出3852
# print(321 / 12)     # 除法运算，输出26.75
# print(321 // 12)    # 整除运算，输出26
# print(321 % 12)     # 求模运算，输出9
# print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241

##4.2
# """
# 算术运算的优先级
# """
# print(2 + 3 * 5)           # 17
# print((2 + 3) * 5)         # 25
# print((2 + 3) * 5 ** 2)    # 125
# print(((2 + 3) * 5) ** 2)  # 625

##4.3
# """
# 赋值运算符和复合赋值运算符
# """
# a = 10
# b = 3
# a += b        # 相当于：a = a + b 13
# a *= a + 2    # 相当于：a = a * (a + 2) 13*15
# print(a)      # 大家算一下这里会输出什么

##4.4
# """
# 海象运算符
# """
# # SyntaxError: invalid syntax
# # print((a = 10))
# # 海象运算符
# print((a := 10))  # 10
# print(a)          # 10

##4.5
# """
# 比较运算符和逻辑运算符的使用
# """
# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not flag0
# print('flag0 =', flag0)     # flag0 = True
# print('flag1 =', flag1)     # flag1 = True
# print('flag2 =', flag2)     # flag2 = False
# print('flag3 =', flag3)     # flag3 = False
# print('flag4 =', flag4)     # flag4 = True
# print('flag5 =', flag5)     # flag5 = False
# print(flag1 and not flag2)  # True
# print(1 > 2 or 2 == 3)      # False

##4.6 Example1
# """
# 将华氏温度转换为摄氏温度
# """
# f1 = float(input('你好啊，请输入华氏温度：'))
# c1 = (f1 - 32)
# print('%.1i华氏度 = %.0f 摄氏度' % (f1, c1))
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.0f摄氏度' % (f, c))

##4.7
# """
# 将华氏温度转换为摄氏温度
# """
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

##4.8
# """
# 输入半径计算圆的周长和面积
# """
#
# radius1 = float(input('请输入圆的半径：'))
# perimeter = 2 * math.pi * radius1
# area = math.pi * radius1**2
# print('圆的周长：%.5f,圆的面积：%.5f' % (perimeter, area))
#
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * 3.1416 * radius
# area = 3.1416 * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

##4.9
# """
# 输入半径计算圆的周长和面积
# """
# import math
#
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius ** 2
# print(f'周长: {perimeter:.2f}')
# print(f'面积: {area:.2f}')

##4.10
# """
# 输入半径计算圆的周长和面积
# """
# import math
#
# radius = float(input('请输入圆的半径: '))  # 输入: 5.5
# perimeter = 2 * math.pi * radius
# area = math.pi * radius ** 2
# print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
# print(f'{area = :.2f}')       # 输出：area = 95.03

##4.11
# """
# 输入年份，闰年输出True，平年输出False
# """
# year = int(input('请输入年份: '))
# is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(f'{is_leap = }')

###5分支结构
##5.1
# """
# BMI计算器
# """
# height = float(input('身高(cm)：'))
# weight = float(input('体重(kg)：'))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# if 18.5 <= bmi < 24:
#     print('你的身材很棒！')

##5.2
# """
# BMI计算器
# """
# height = float(input('身高(cm)：'))
# weight = float(input('体重(kg)：'))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# if 18.5 <= bmi < 24:
#     print('你的身材很棒！')
# else:
#     print('你的身材不够标准哟！')

##5.3
# """
# BMI计算器
# """
# height = float(input('身高(cm)：'))
# weight = float(input('体重(kg)：'))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# if bmi < 18.5:
#     print('你的体重过轻！')
# elif bmi < 24:
#     print('你的身材很棒！')
# elif bmi < 27:
#     print('你的体重过重！')
# elif bmi < 30:
#     print('你已轻度肥胖！')
# elif bmi < 35:
#     print('你已中度肥胖！')
# else:
#     print('你已重度肥胖！')

##5.4
# status_code = int(input('响应状态码: '))
# if status_code == 400:
#     description = 'Bad Request'
# elif status_code == 401:
#     description = 'Unauthorized'
# elif status_code == 403:
#     description = 'Forbidden'
# elif status_code == 404:
#     description = 'Not Found'
# elif status_code == 405:
#     description = 'Method Not Allowed'
# else:
#     description = 'Unknown status Code'
# print('状态码描述:', description)

##5.5
# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400: description = 'Bad Request'
#     case 401: description = 'Unauthorized'
#     case 403: description = 'Forbidden'
#     case 404: description = 'Not Found'
#     case 405: description = 'Method Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)

##5.6
# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400 | 405: description = 'Invalid Request'
#     case 401 | 403 | 404: description = 'Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)

##5.7
# """
# 分段函数求值
# """
# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print(f'{y = }')

##5.8
# """
# 分段函数求值
# """
# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# else:
#     if x >= -1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
# print(f'{y = }')

##5.9
# """
# 百分制成绩转换为等级制成绩
# """
# score = float(input('请输入成绩: '))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print(f'{grade = }')

##5.10
# """
# 计算三角形的周长和面积
# """
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     perimeter = a + b + c
#     print(f'周长: {perimeter}')
#     s = perimeter / 2
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     print(f'面积: {area}')
# else:
#     print('不能构成三角形')

###6
##6.1
# """
# 每隔1秒输出一次“hello, world”，持续1小时
# """
# import time
#
# for i in range(3600):
#     print('hello, world')
#     time.sleep(1)

##6.2
# """
# 每隔1秒输出一次“hello, world”，持续1小时
# """
# import time
# for _ in range(3600):
#     print('hello, world')
#     time.sleep(1)

##6.3
# """
# 从1到100的整数求和
# """
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

##6.4
# """
# 从1到100的偶数求和
# """
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print(total)

##6.5
# """
# 从1到100的偶数求和
# """
# total = 0
# for i in range(2, 101, 2):
#     total += i
# print(total)

##6.6
# """
# 从1到100的偶数求和
# """
# print(sum(range(2, 101, 2)))

##6.7
# """
# 从1到100的整数求和
# """
# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 1
# print(total)

##6.8
# """
# 从1到100的偶数求和
# """
# total = 0
# i = 2
# while i <= 100:
#     total += i
#     i += 2
# print(total)

##6.9
# """
# 从1到100的偶数求和
# """
# total = 0
# i = 2
# while True:
#     total += i
#     i += 2
#     if i > 100:
#         break
# print(total)

##6.10
# """
# 从1到100的偶数求和
# """
# total = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         continue
#     total += i
# print(total)

##6.11
# """
# 打印乘法口诀表
# """
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}×{j}={i * j}', end='\t') ##\t是对齐
#     print()                                 ##是换行

##6.12
# """
# 输入一个大于1的正整数判断它是不是素数
# """
# num = int(input('请输入一个正整数: '))
# end = int(num ** 0.5)
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')

##6.13
# """
# 输入两个正整数求它们的最大公约数
# """
# x = int(input('x = '))
# y = int(input('y = '))
# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(f'最大公约数: {i}')
#         break

##6.14
# """
# 输入两个正整数求它们的最大公约数
# """
# x = int(input('x = '))
# y = int(input('y = '))
# while y % x != 0:
#     x, y = y % x, x
# print(f'最大公约数: {x}')

##6.15
# """
# 猜数字小游戏
# """
# import random
# answer = random.randrange(1, 101)
# counter = 0
# while True:
#     counter += 1
#     num = int(input('请输入: '))
#     if num < answer:
#         print('大一点.')
#     elif num > answer:
#         print('小一点.')
#     else:
#         print('猜对了.')
#         break
# print(f'你一共猜了{counter}次.')

###7
##7.1
# """
# 输出100以内的素数
# """
# for num in range(2,100):
#     is_prime = True
#     for i in range(2,int(num ** 0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

##7.2
# """
# 斐波拉切数列的前20个数
# """
# a,b=0,1
# for i in range(2,20):
#     a,b=b,a+b
#     print(a)

##7.3
# """寻找水仙花数 100-999"""
# for num in range(100, 999):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)
# for num in range(10, 10000):
#     s = str(num)
#     power = len(s)
#     total = sum(int(d) ** power for d in s)
#     if total == num:
#         print(num)

##7.4
"""百钱白鸡问题"""
# for x in range(0,21):
#     for y in range(0,34):
#         for z in range(0,100,3):
#             if x+y+z==100 and 5 * x + 3 * y + z // 3 ==100:
#                 print(f'公鸡{x}只,母鸡{y}只,小鸡{z}只')
# for x in range(0, 21):
#     for y in range(0, 34):
#         z = 100 - x - y
#         if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
#             print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

##7.5
# import random
#
# def roll():
#     # randint 包含两端；等价于你用的 randrange(1, 7)
#     return random.randint(1, 6) + random.randint(1, 6)
#
# money = 1000
# while money > 0:
#     print(f'你的总资产为: {money}元')
#
#     # 安全读取下注
#     while True:
#         try:
#             debt = int(input('请下注: '))
#             if 0 < debt <= money:
#                 break
#             print('下注需为正整数，且不超过现有资金。')
#         except ValueError:
#             print('请输入数字。')
#
#     first_point = roll()
#     print(f'\n玩家摇出了 {first_point} 点')
#
#     if first_point in {7, 11}:
#         print('玩家胜!\n')
#         money += debt
#     elif first_point in {2, 3, 12}:
#         print('庄家胜!\n')
#         money -= debt
#     else:
#         # 进入点数循环
#         while True:
#             current_point = roll()
#             print(f'玩家摇出了 {current_point} 点')
#             if current_point == 7:
#                 print('庄家胜!\n')
#                 money -= debt
#                 break
#             if current_point == first_point:
#                 print('玩家胜!\n')
#                 money += debt
#                 break
#
# print('你破产了, 游戏结束!')

###8
##8.1.1创建列表
# import random
# f1, f2, f3, f4, f5, f6 = 0, 0, 0, 0, 0, 0
#
# for _ in range(6000):
#     num = random.randrange(1,7)
#     if num == 1:
#         f1 += 1
#     elif num == 2:
#         f2 += 1
#     elif num == 3:
#         f3 += 1
#     elif num == 4:
#         f4 += 1
#     elif num == 5:
#         f5 += 1
#     else:
#         f6 += 1
#
# print(f'1出现{f1}次')
# print(f'2出现{f2}次')
# print(f'3出现{f3}次')
# print(f'4出现{f4}次')
# print(f'5出现{f5}次')
# print(f'6出现{f6}次')

#8.1.2
"""升级版"""
# import random
# counts = [0] * 6
# for _ in range(6000):
#     num = random.randrange(1,7)
#     counts[num-1] +=1
# for i,counts in enumerate(counts):   ##enumerate 可以获取索引和索引值
#     print(f'{i+1}出现了{counts}次')

##8.2
"""列表的运算"""
# items5 = [35, 12, 99, 45, 66]
# items6 = [45, 58, 29]
# items7 = ['Python', 'Java', 'JavaScript']
# print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
# print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
# items5 += items6
# print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
# print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
# print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']
# print(29 in items6)  # True
# print(99 in items6)  # False
# print('C++' not in items7)     # True
# print('Python' not in items7)  # False
# items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# print(items8[0])   # apple
# print(items8[2])   # pitaya
# print(items8[4])   # watermelon
# items8[2] = 'durian'
# print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
# print(items8[-5])  # 'apple'
# print(items8[-4])  # 'waxberry'
# print(items8[-1])  # watermelon
# items8[-4] = 'strawberry'
# print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']
#
# print(items8[1:3:1])     # ['strawberry', 'durian']
# print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']
# print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']
# print(items8[-4:-2:1])   # ['strawberry', 'durian']
# print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']
#
# print(items8[1:3])     # ['strawberry', 'durian']
# print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
# print(items8[::2])     # ['apple', 'durian', 'watermelon']
# print(items8[-4:-2])   # ['strawberry', 'durian']
# print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']
#
# items8[1:3] = ['x', 'o']
# print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']
#
# nums1 = [1, 2, 3, 4]
# nums2 = list(range(1, 5))
# nums3 = [3, 2, 1]
# print(nums1 == nums2)  # True
# print(nums1 != nums2)  # False
# print(nums1 <= nums3)  # True

##8.3
"""元素的遍历"""
# languages = ['python', 'java', 'C++', 'kotlin']
# for index in range(len(languages)):
#     print(languages[index])

# languages = ['python', 'java']
# for language in languages:
#     print(language)

"""
将一颗色子掷6000次，统计每种点数出现的次数
"""
# import random
#
# counters = [0] * 6
# for _ in range(6000):
#     face = random.randrange(1, 7)
#     counters[face - 1] += 1
# for face in range(1, 7):
#     print(f'{face}点出现了{counters[face - 1]}次')
#

###9
##9.1
