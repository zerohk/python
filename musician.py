# -*- coding: GBK -*-
def build_person(first_name, last_name, age=''):
    """����һ���ֵ䣬���а����й�һ���˵���Ϣ"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
