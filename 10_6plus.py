# -*- coding: GBK -*
while True:
    print("��������������,����q�˳�")
    try:
        num_1 = input("�������һ�����֣� ")
        if num_1 == 'q':
            break
        num_2 = input("������ڶ������֣� ")
        if num_2 == 'q':
            break
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:
        print("��ȷ������������������֣�\n")
    else:
        count = num_1 + num_2
        print(str(num_1) + "��" + str(num_2) + "�������ĺ�Ϊ" + str(count) + '\n')
