
# -*- coding: GBK -*-
def print_models(unprinted_designs, completed_models):
    """ģ���ӡÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ,
    ��ӡÿ����ƺ󣬶������Ƶ��б�completed_models��
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # ģ������������3D��ӡģ�͵Ĺ���
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """��ʾ��ӡ�õ�����ģ��"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
