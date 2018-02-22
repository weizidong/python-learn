# -*-coding:utf-8-*-
import json

import MarkovChainConfig

# 马尔科夫链训练器
if __name__ == '__main__':
    try:
        with open(MarkovChainConfig.data_file, 'r', encoding='utf-8') as load_f:
            model = json.load(load_f)
    except:
        model = {'START': [], 'END': []}
    print('1、单词与单词之间使用空格隔开\n'
          '2、保存训练结果并结束请输入"end"\n'
          '3、重新训练请输入"reset"\n'
          '4、保存训练结果请输入"save"')
    while True:
        ipt = input('请输入训练语句或命令：')
        if ipt == 'end':
            with open(MarkovChainConfig.data_file, 'w', encoding='utf-8') as f:
                json.dump(model, f, ensure_ascii=False)
            break
        elif ipt == 'save':
            with open(MarkovChainConfig.data_file, 'w', encoding='utf-8') as f:
                json.dump(model, f, ensure_ascii=False)
                f.close()
        elif ipt == 'reset':
            model = {'START': [], 'END': []}
        else:
            line = ipt.lower().split()
            for i, word in enumerate(line):
                if i == len(line) - 1:
                    model['END'] = model.get('END', []) + [word]
                else:
                    if i == 0:
                        model['START'] = model.get('START', []) + [word]
                    model[word] = model.get(word, []) + [line[i + 1]]
