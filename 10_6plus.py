# -*- coding: GBK -*
while True:
    print("请输入两个数字,输入q退出")
    try:
        num_1 = input("请输入第一个数字： ")
        if num_1 == 'q':
            break
        num_2 = input("请输入第二个数字： ")
        if num_2 == 'q':
            break
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:
        print("请确保你输入的是两个数字！\n")
    else:
        count = num_1 + num_2
        print(str(num_1) + "和" + str(num_2) + "两个数的和为" + str(count) + '\n')
