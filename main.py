import random
import argparse
from fractions import Fraction
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--range')
parser.add_argument('-n', '--time')
parser.add_argument('-e', '--efile')
parser.add_argument('-a', '--afile')

args = parser.parse_args()
# 以上命令行参数相关----------------------------
dict1 = {0: '+', 1: '-', 2: '*', 3: '÷'}
dict2 = {'+': 1, '-': 1, '*': 2, '÷': 2}
Path1 = "D:Python/Answers.txt"    # 为答案文件的路径，通过命令行输入
Path2 = "E:\\Grade.txt"    # 为成绩文件的路径，手动更改
Path3 = "D:/Python/Exerceses.txt"    # 为算式文件的路径，通过命令行输入
list_ans = []
list_answer = []
list_shizi = []
list_correct = []
list_wrong = []
ind = 1

# 主体函数，重复调用得到多道题目
def compute():
    # symbol = random.randint(0,3)    # 用0-3分别表示+，-，*，/
    global range
    list_num = []    # 存放数字
    list_fu = []    # 存放符号
    flag = random.randint(0, 1)
    if flag == 1:
        n = Fraction(random.randint(0, int(args.range)+1), random.randint(1, int(args.range)+1))
    else:
        n = random.randint(0, int(args.range))
    num = random.randint(1, 3)               # num代表符号个数
    str1 = ""                                      #str1用来储存算式
    list_num.append(n)    # 存放数
    # print("运算符号个数为：", num)
    # t_n = num
    # 写一条算式的代码，并将算数和运算符，计算结果和算式分别放到不同的列表存储
    while num >= 0:
        str1 += str(n)
        str_t = ""
        symbol = random.randint(0,3)
        while n == 0 and symbol == 1:
            symbol = random.randint(0,3)
        tem = dict1[symbol]    # tem为运算符
        list_fu.append(tem)    # 存放运算符
        str += tem
        num -= 1
        t1 = n
        flag = random.randint(0,1)
        if flag == 1:
            n = Fraction(random.randint(0, int(args.range)), random.randint(1, int(args.range)+1))
            if symbol == 1:
                while t1 < n:
                    n = Fraction(random.randint(0, int(args.range)), random.randint(1, int(args.range)+1))
            elif symbol == 3:
                n = Fraction(random.randint(1, int(args.range)+1), random.randint(1, int(args.range)+1))
        else:
            n = random.randint(0, int(args.range)+1)
            if symbol == 1:
                while t1 < n:
                    n = random.randint(0, int(args.range)+1)
            elif symbol == 3:
                n = random.randint(1, int(args.range)+1)
        list_num.append(n)
    list_fu.pop()
    list_num.pop()
    # 上两行为删掉多余的元素
    str_t = str1[:len(str1)-1]
    # --------------------------------以下为求和过程
    res = list_num[0]
    # nl = len(list_fu)    #list_fu的长度
    ln = []
    lf = []
    i_n = 0
    i_f = 0
    i = 0
    # try
    while i_n < len(list_num) or i_f < len(list_fu):
        if i_n < len(list_num):
            ln.append(list_num[i_n])
            i_n += 1

        if len(lf) > 1 and dict[lf[-1]] > dict[lf[-2]]:
            n1 = ln.pop()
            n2 = ln.pop()
            if lf[-1] == '*':
                tem = n1 * n2
            elif lf[-1] == '÷':
                tem = Fraction(n2,n1)
            lf.pop()
            ln.append(tem)
        if i_f < len(list_fu):
            lf.append((list_fu[i_f]))
            i_f += 1

    while i < len(lf):
        if lf[i] == '*':
            res *= ln[i + 1]
        elif lf[i] == '÷':
            res = Fraction(res, ln[i+1])
        elif lf[i] == '+':
            res = res + ln[i + 1]
        elif lf[i] == '-':
            res = res - ln[i + 1]
        i += 1
    if res > 0:
        # print("运算符号个数为：", num)
        list_ans.append(str(res))
        global ind
        str_t = str(ind) + '. ' + str_t + '='
        ind += 1
        list_shizi.append(str_t)
        return str_t