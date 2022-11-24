# # ages = []
# # for _ in range(3):
# #     ages.append(int(input()))
# #
# # ages.sort()
# # print("min", ages[0])
# # print("max", ages[-1])
# #
# # print("max: ", max(ages))
# # print('min: ',min(ages))
# #
# #
# #
# #
# # 'a'.replace()
# # grade = int(input("grade: "))
# # if grade < 25:
# #     print("F")
# # elif 25 <= grade < 45:
# #     print("E")
# # elif 45 <= grade < 50:
# #     print("D")
# # elif 50 <= grade < 60:
# #     print("E")
# # elif 60 <= grade < 80:
# #     print("B")
# # elif grade > 80:
# #     print("A")
# #
# #
# #
# # temp = input().upper()
# # c = int(temp[:-1])
# # f = int(temp[:-1])
# # #
# # if 'C' in temp:
# #     f = c * (9 / 5) + 32
# #     print(f'{int(f)}F')
# # else:
# #     c = (f-32) * (5/9)
# #     print(f"{int(c)}C")
# #
# # # number = int(input())
# # # for i in range(1, 11):
# # #     print(i * number)
# # #
# # # print([number*i for i in range(1, 11)])
# # #
# # income = int(input("income: "))
# # tax = 0
# # if income < 10000:
# #     print(tax)
# # elif income < 20000:
# #     tax = (income - 10000) * 0.1
# #     print(tax)
# # else:
# #     tax = ((income - 20000) * 0.2) + 1000
# #     print(tax)
# #
# #
#
#
# # inp = input().split(',')
# # sym = ['@', '#', '!']
# # for email in inp:
# #     upper_flag = False
# #     lower_flag = False
# #     digit_flag = False
# #     symbol_flag = False
# #     if 6 < len(email) < 12:
# #         for ch in email:
# #             if ch.isupper():
# #                 upper_flag = True
# #             if ch.islower():
# #                 lower_flag = True
# #             if ch.isdigit():
# #                 digit_flag = True
# #             if ch in sym:
# #                 symbol_flag = True
# #
# #         if upper_flag and lower_flag and digit_flag and symbol_flag:
# #             print(email)
#
# # import re
# # inp = input().split(',')
# # pattern = r'(?=.*[A-Za-z])(?=.*\d)(?=.*[@$#&])[A-Za-z\d@$#&]{6,12}$'
# # for password in inp:
# #
# #     result = re.findall(pattern, password)
# #     print(*result)
#
# # print(sum('12'))
# from hashlib import sha256
# from _md5 import md5
# # from _sha256 import sha256
# # x = sha256('fsdfdsfsdfdsfsdf'.encode('utf-8')).hexdigest()
# # print(x)
# # 1d7ae6ca9e689a549f4f47ba797e73dd9506182111a8e4157ad0945ca6ee419f
# # 09b6f1b098ba521ff3492b1105974cc888d75d37d8457814123bf8cfc11e572f
# # n = int(input())
# # x = lambda n: not [i for i in range(2, n) if not (n%i)]
# # y = lambda N: [i for i in range(2, N+1) if x(i)]
# # print(y(n))
#
# # def is_primal(n):
# #     n = int(n)
# #     assert n > 0
# #     for i in range(2, int(n**0.5)+1):
# #         if not (n % i):
# #             return False
# #     return True
# #
# # l = list(map(lambda x: is_primal(x), range(2, 12)))
# # print(l)
# # print(any(l), all(l))
#
# # s1 = list(range(10))
# # s2 = "hello ali!"
# # x1 = zip(s1, s2)
# # x2 = enumerate(s2)
# # x = list(x1)
# # y = list(x2)
# # print(x == y)
# # print(list(x1))
# # print(y)
#
# # s = '1 - hellow / n2 - 5 +'\
# #     '3 hello'
# # x = list(filter(lambda x: not x.isalpha(),s))
# # print(x)
# # x = list(reversed(x))
# # print(x)
# # x = [str(ord(c)) if c.isnumeric() else c for c in x if c != ' ']
# # print(x)
# # x = ''.join(x)
# # print(x)
# # x = eval(x)
# # print(x)
# # x = round(x, 3)
# # print(x)
# # x = hex(int(x*10))
# # print(x)
#
# # a_dict = {'a': 1, 'b': 2}
# # a_l_of_tuple = [('a', 1), ('b', 2)]
# # def tuple_dict_converter(data):
# #     if isinstance(data, dict):
# #         return list(map(lambda item: item, data.items()))
# #     else:
# #         return dict(map(lambda item: item ,data))
# #
# # print(tuple_dict_converter(a_l_of_tuple))
#
# # from math import factorial
# #
# # # input n
# # m = 0
# # n = 5
# # for i in range(n):
# #     # for j in range(n - i + 1):
# #     #     for left spacing
# #         # print(end=" ")
# #
# #     for j in range(i + 1):
# #         # nCr = n!/((n-r)!*r!)
# #         print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
# #
# #     # for new line
# #     print()
# # print(id(n))
# # print(id(m))
# # a = ['1', ['2'], '3', '3']
# # x = set(a)
# # print(x)
# # from hashlib import sha256
# # print(sha256('1'.encode('utf-8')).hexdigest())
# # print(sha256('2'.encode('utf-8')).hexdigest())
# # print(sha256('3'.encode('utf-8')).hexdigest())
# # print(sha256('3'.encode('utf-8')).hexdigest())
#
#
# def palindrom(s):
#     if s == s[::-1]:
#         print('palindrome')
#     else:
#         print('not palindrome')
#
#
# # def show_employee(name, salary=9000):
# #     print(f'name: {name} salary: {salary}')
# #
# #
# # name = 'jafar'
# # salary = 25000
# # show_employee(name)
#
# # def func(*args):
# #     for i in args:
# #         print(i)
# # my_list = list(range(3))
# # func(*my_list)
#
#
# # num = ((1,2,3,4),(20,30,5,4))
# # for j in range(len(num[0])):
# #     x = 0
# #     for i in num:
# #         x += i[j]
# #     print(x/len(num))
# # for j in range(len(num[0])):
# #     # x = 0
# #     avg = sum(map(lambda x: x[j], num))/len(num)
# #     print(avg)
# # data = range(1000_000)
# # print(list(filter(lambda x: True if x%1000==0 else False, data)))
# # data = (1,3,2)
# # from functools import reduce
# # print(reduce(lambda x, y: x + y, data ))
#
# # data = [1,3,5,6]
# # for i, j in enumerate(data, start=10):
# #     print(i, j)
#
# #
# # '''Get the index and the value as a tuple for items in the
# # list ["hi", 4, 8.99, 'apple', ('t,b','n')].
# # Result would look like [(index, value), (index, value)]'''
# #
# # data = ["hi", 4, 8.99, 'apple', ('t,b','n')]
# # out = [(idx, value) for idx, value in enumerate(data)]
# # print(out)
# #
# # sentence = "on a summer day somner smith went simming in the sun and his red skin stung"
# # data = sentence.split(' ')
# #
# # out1 = list(filter(lambda x: len(x)>= 4,data))
# # out2 = list(filter(lambda x: len(x)< 4,data))
# # print(out1)
# # print(out2)
# #
# #
# # data = {'T-shirt':45.5, 'Pants':35, 'Sneakers':41.30, 'Hat':55, 'Backpack': 24}
# # def top3(d):
# #     # sorted_dict = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
# #     sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
# #     print(sorted_dict)
# #     dic = dict()
# #     for i in range(3):
# #         a, b = sorted_dict.popitem()
# #         dic[a] = b
# #     return dic
# #
# # # print(top3(data))
# # #########
# #
# # lst1=["Mike", "Danny", "Jim", "Annie"]
# # lst2=[4, 12, 7, 19]
# #
# # data = list(zip(lst1, lst2))
# # print(data)
# # sorted_data = sorted(data)
# # print(sorted_data)
# #
# #
# # from string import ascii_lowercase
# # data = "The quick brown fox jumps over the lazy og"
# #
# # def pangram(s):
# #     alphabet = ascii_lowercase
# #     for i in alphabet:
# #         if i  not in s.lower():
# #             return False
# #     return True
# #
# # print(pangram(data))
#
# # data = {'jafar': 'dd'}
# # data.pop('jafar')
# # print(data)
#
# # from datetime import datetime
# # import time
#
# # class Person():
# #     class_public_var = 'class_public_var'
# #     __class_private_var = '__class_private_var'
# #
# #     def __init__(self, name, famili):
# #         self.name = name
# #         self.__famili = famili
# #
# #     def public_method(self):
# #         print('public method', self.__famili)
# #
# #     def __private_method(self):
# #         print('private method', self.__famili)
# #
# #     def get_famili(self):
# #         log_file = open('text.txt', 'a')
# #         print(f'{datetime.now()}: {self.name} {self.__famili}', file=log_file, flush=True)
# #         log_file.close()
# #         return self.__famili
# #
# #     def set_name(self, value):
# #         self.class_public_var = value
# #
# #
# # p = Person('mojtaba', 'aminzadeh')
# # d = Person('mamad', 'ahamadi')
# # print(p.class_public_var)
# # print(d.class_public_var)
# # p.set_name('jafar')
# # print(p.class_public_var)
# # print(d.class_public_var)
# from functools import reduce
# from string import digits
# # s = '1155522333222233'
# # print('3'>'2')
#
# # import time
# # data = [1, 2, -20, -1, 0]
# # def solution(array):
# #     max_index = len(array) - 1
# #     jump = 0
# #     idx = 0
# #     history = []
# #     while not (idx > max_index):
# #         if idx < 0:
# #             return -1
# #         history.append(idx)
# #         print(history, idx)
# #         idx = array[idx] + idx
# #         if idx in history:
# #             return -1
# #         jump += 1
# #         time.sleep(1)
# #     return jump
# # print(solution(data))
# # data = (1, 3, 5)
# # data = "string"
# # import itertools
# # x = itertools.accumulate(data, lambda x, y: x+y)
# # x = itertools.chain(data, data)
# # x = itertools.chain.from_iterable([data,data])
# # x = itertools.compress(data, '101')
# # print(x)
# # print(list(x))
#
#
#
# # l1 = []
# # for x in range(10):
# #     l1.append(x)
# #
# # l2 = [x for x in range(10)]
# # print(l1)
# # print(l2)
#
#
# # a = 1
# # b = '10'
# #
# # try:
# #     print(a + b)
# # except TypeError as e:
# #     print(e)
# # else:
# #     print('hello')
# # finally:
# #     print('finally')
#
# #
# # def outer(x):
# #     def inner():
# #         print('hellow')
# #         x()
# #     return inner
# #
# #
# # # @outer
# # def name():
# #     print('hello')
# #
# # p = outer(name)
# # p()
# #
#
# #
# # def number():
# #     return 10
# #
# # def number2():
# #     yield 10
# #     yield 20
# #     yield 50
# #     yield 60
#
# # print(number())
# # x = number2()
# #
# # print(next(x))
# #
# #
# # for i in x:
# #     print(i)
# #
# # print(list(x))
# # print(list(number2()))
# # for i in number2():
# #     print(i)
#
# # x = open('text.txt', 'r+')
# # print(x)
# # x.write('ssdfdsfdsfsdf')
# # x.seek(0)
# # # print(x.read())
# # x.seek(0)
# # for i in x:
# #     for j in i:
# #         print(j)
# # x.seek(0)
# # print(x.read(200))
# # # print(x.readlines())
# # # x.seek(0)
# # # print(x.readline(3500))
# # x.close()
#
#
# # with open('text.txt', 'rb') as x:
# #     if x.read(1) in [b'\x89', b'\x50', b'\x4e', b'\x47']:
# #         x.seek(0)
# #         for i in range(10):
# #             pass
# #         with open('newpic.png', 'wb') as new_file:
# #             new_file.write(x)
#
#     # print(x.readlines())
#     # x.seek(0)
#     # print(x.read())
# import itertools
# # a = [1, 2, 4, 5, 4, 6]
# # b = [True, False, True, True, False, True]
# # out = []
# # for i, j in zip(a, b):
# #     if j:
# #         out.append(i)
# # print(out)
# # print(list(zip(a, b)))
# # print(list(filter(lambda x: x[1] ,zip(a, b))))
# # out = list(itertools.compress(a, b))
# # print(out)
# # print(list(range(1000)))
# # def adad():
# #     for i in range(1000):
# #         yield i
# # data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]
# # data2 = range(1000)
# # print(data.__sizeof__())
# # print(data2.__sizeof__())
# # x = adad()
# # print(next(x))
#
#
# # data = [1,2,3,4]
# # x = itertools.compress(data, [0, 1, 0, 0])
# # print(list(x))
# # data = [1,2,3,4]
#
#
# # print((not 1) > 1)
# # print(False > 1)
# # print((not 1) < 1)
# # print(not 1 == 1)
#
# # print(list(itertools.dropwhile(lambda x: not x >= 2, data)))
# # print(list(itertools.filterfalse(lambda x: x>3, data)))
# # print(list(list(itertools.groupby(data, key=lambda x: x))[0][1]))
# # data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
# # # print(list(itertools.groupby(data, key=lambda x: x[0])))
# # # print(list(itertools.groupby(data, key=lambda x: x[0]))[0][1])
# # d = dict()
# # x = itertools.groupby(data, key=lambda x: x[0])
# # for k, v in x:
# #     d[k]= list(v)
# # print(d)
# #
# # L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
# #
# # # Key function
# # key_func = lambda x: x[0]
# #
# # for key, group in itertools.groupby(L, key_func):
# #         print(key + " :", list(group))
#
#
# # data = '23456'
# # print(data)
# # print(*data)
# # print(pow(5, 5))
#
# # print(list(itertools.islice(data, 3, None)))
# # print(list(itertools.starmap(pow, data)))
# # print(list(map(lambda x : pow(x[0], x[1]), data)))
# # x = list(itertools.tee(data, 3))
# # for i in x:
# #     print(list(i))
# # print(list(itertools.tee(data)[0]))
# # print(list(itertools.tee(data)[1]))
# # data = [2, 3, 4]
# # data2 = [20, 30, 40]
# # data3 = [20, 30, 40]
# # print(list(itertools.permutations(data, 3)))
# # print(list(itertools.combinations_with_replacement(data, 2)))
# # file = open('text.txt', 'r+')
# # from string import printable
# # print(ord(printable[99]))
# # print(ord('\t'))
# # print(chr(12), file=file)
#
# # class A():
# #     pass
# #
# #
# # def abc():
# #     yield 'jafar'
# #
# # x = abc()
#
# # from types import MappingProxyType, AsyncGeneratorType, BuiltinFunctionType,GeneratorType, FunctionType
# # print(MappingProxyType)
# # print(type(A.__dict__) == MappingProxyType)
# # print(AsyncGeneratorType)
# # print(BuiltinFunctionType == type(max))
# # print(type(abc()) == GeneratorType)
# import time
#
#
#
#
# # data = {'asdfsad': 'val1',
# #         'key': 'val2'
# #         }
# # file = open('text2.txt', 'w')
# # # file.write('data')
# # file.writelines(data)
#
#
# # try:
# #   print(1 / 0)
# # except ZeroDivisionError:
# #   raise ValueError
# # assert 1+2==5
# # iter()
# # from random import randint
# # from functools import partial
# # x = partial(randint, 5, 10)
# # print(x)
# # print(randint(5, 10))
#
# # from cmath import inf
# # print(inf > 10)
# # from typing import io
#
# # query = input('> ')
# # with open('text.txt', 'r') as file:
# #     out = list(filter(lambda x: query in x, file))
# # print(out)
#
#
# # from os import name, system
# # print(name)
#
# # import contextlib
# # import time
# #
# # @contextlib.contextmanager
# # def Timer(user_input):
# #     if user_input == 'second':
# #         start = time.time()
# #         yield
# #         end = time.time()
# #         print(f'time: {end - start}')
# #     elif user_input == 'ns':
# #         start = time.time_ns()
# #         yield
# #         end = time.time_ns()
# #         print(f'time_ns: {end - start}')
# #
# #
# # with Timer(input('Enter "second" or "ns": ')):
# #     li = []
# #     for i in range(1000):
# #         for j in range(1000):
# #             li.append((i,j))
# #
# #
# # with Timer(input('Enter "second" or "ns": ')):
# #     x = [(i,j) for i in range(1000) for j in range(1000)]
#
# # names = ["John", "Oscar", "Jacob"]
# #
# # file = open("names.txt", "w+")
# # #write down the names into the file
# # for item in names:
# #     file.write(item+'\n')
# # file.close()
# #
# # file= open("names.txt", "r")
# # #output the content of file in console
# # print(file.read())
# #
# # file.close()
# # root = ['jafar', 'mamad', 2, 6,3, 5]
# # root[:] = [root, root, None, None]
# # print(root[0][0])
# # for i in root:
# #     print(i)
#
#
# # import math
# #
# # x = int(input('Please enter a positive number:\n'))
# #
# # try:
# #     print(f'Square Root of {x} is {math.sqrt(x)}')
# # except ValueError as ve:
# #     print(f'You entered {x}, which is not a positive number.')
# #
# #
#
# # def range(start, end=None, step=1):
# #     while start != end:
# #         yield start
# #         start += step
# #
# #
# # x = range(0, 5)
# #
# # for i in range(0, 5):
# #     print(i)
#
#
# def timer_process():
#     def outer(func):
#         def wraper(data):
#             start = time.time()
#             func(data)
#             end = time.time()
#             return f'process time for fibo({data}) : {round(end - start, 6)} s'
#             # return out
#         return wraper
#     return outer
#
#
# def cache(func):
#
#     def wrapper(data):
#         func(data)
#         return result
#     return wrapper
#
#
# # @timer_process()
# @cache
# def fibo(n):
#     if n == 0:
#         return 0
#     if n in {1, 2}:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# x = fibo(36)
# print(x)

# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# print(nums)
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))

# def power(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x, y - 1)
#
#
# print(power(2, 3))


# class Vector():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # def __add__(self, other):
#     #     return Vector(self.x + other.x, self.y + other.y)
#
#     def __add__(self, other):
#         self.x += other.x
#         self.y += other.y
#         return self
#
#
# obj1 = Vector(2, 3)
# obj2 = Vector(4, 3)
# obj3 = obj1 + obj2
# print(obj1.x, obj1.y)
# print(obj2.x, obj2.y)
# print(obj3.x, obj3.y)
# import time
# from functools import lru_cache
#
#
# def timer_process(func):
#     def wraper(data):
#         start = time.time()
#         out = func(data)
#         # write_file(data, out)
#         end = time.time()
#         return f'process time for fibo({data}) : {round(end - start, 6)} s'
#         # return out
#         # return out
#     return wraper
#
#
# @timer_process
# @lru_cache
# def fibo(n):
#     if n == 0:
#         return 0
#     if n in {1, 2}:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# x = fibo(50)
# print(x)
#
# class A(object):
#     def __init__(self):
#         print('init')
#
#     def __del__(self):
#         pass
#
# a = A()

# while True:
#     pass
# del a
# a = 5

# Python program to illustrate destructor

# class A:
# 	def __init__(self, bb):
# 		self.b = bb
#
# class B:
# 	def __init__(self):
# 		self.a = A(self)
# 	# def __del__(self):
# 	# 	print("die")
#
# def fun():
# 	b = B()
#
# fun()
#
#
# class Base:
#     def __init__(self):
#         # Protected member
#         self.a = 2
#
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling protected member of base class: ",
#               self.a)
#
#         # Modify the protected variable:
#         self._a = 3
#         print("Calling modified protected member outside class: ",
#               self.a)
#
#
# obj1 = Derived()
#
# obj2 = Base()
# obj1.
#
# # Calling protected member
# # Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)
#
# # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)


# Python program to
# demonstrate private members

# Creating a Base class


# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks A"
#         self._c = "GeeksforGeeks __C"
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.a)
#         print(self._c)
#
#
# obj = Derived()
# print(obj.__dict__)


# xs = [22, 13, 45, 50, 98, 69, 43, 44, 1]
# x = [x+1 if x >= 45 else x+5 for x in xs]
# x = [x+1 for x in xs if x >= 45]
# print(x)



# class Adam:
#     hands = 2
#     def __init__(self, name, age, id, phone):
    #     self.__name = name
    #     self._age = age
    #     self.id = id
    #     self.phone = phone
    #     self._x = 10
    #     print('class Adam created')
    #
    # def information(self):
    #     print(f'my name is {self.__name} and age is {self._age}')
    #
    # def __add__(self, other):
    #     return self.age + other.age
    #
#     def phone_add_id(self):
#         with open('log.txt', 'w') as file:
#             print(f'{self} add', file=file)
#         return int(self.phone) + self.id
#
#     def __len__(self):
#         return len(self.__name)
#
#     def __str__(self):
#         return f'man {self.__name} hastam'
#
#     def __del__(self):
#         print('tamom shod...')
#
# a = Adam('akbar', 20, 5, '2')
# b = Adam('jafar', 20, 5, '2')
# del a
# # print(len(a))
# # print(a)
#
# print(b)
#
# class mard():
#
#     def __init__(self, name, age, ghad):
#         self.ghad = ghad
#         # super().__init__(name, age)
#         Adam.__init__(self, name, age)
#         self.adam = Adam()
#
#     def information(self):
#         print('man mard hastam')
#         # super().information()
#         # Adam.information(self)
#
# class bache(mard, Adam):
#     pass
#
# print(bache.__mro__)
# # x = bache()
#
#
# class A():
#     def __init__(self, name):
#         self.name = name
#         name = 100
#
# a1 = A('jafar')
#
# print(a1.name)
# x = range(-10)
# print(x)
# for i in range(-10):
#     print(i)

