# -*-coding:utf-8-*-
import json
import random

import MarkovChainConfig


# 马尔科夫链生成器
def generator():
    generated = []
    with open(MarkovChainConfig.data_file, 'r', encoding='utf-8') as load_f:
        model = json.load(load_f)
    while True:
        if not generated:
            words = model['START']
        elif generated[-1] in model['END']:
            break
        else:
            words = model[generated[-1]]
        generated.append(random.choice(words))
    print(''.join(generated))


if __name__ == '__main__':
    for i in range(int(input('请输入生产个数（数字）：'))):
        generator()
    input('\n按任意键退出...')
