# xhzrm_dict_for_Rime

Rime输入法词库。其中，单字字库采用小鹤双拼+自然码辅助码(按;输入辅助码)，词库采用小鹤双拼编码。

词库来自若干开源项目，详见《文件说明》。本词库有根据本人需求所做精简，旨在满足日常输入需求的前提下缩减词库。不然输入法会卡。

目前包含输入法的设置，可以直接导入。

## 1. 文件说明

### THUOCL_***.dict.yaml

THUOCL（THU Open Chinese Lexicon）是由清华大学自然语言处理与社会人文计算实验室整理推出的一套高质量的中文词库，词表来自主流网站的社会标签、搜索热词、输入法词库等。项目地址: https://github.com/thunlp/THUOCL

本项目精简了这个词库。

### sougou_***.dict.yaml

搜狗词库。

### clover_***.dict.yaml

四叶草拼音输入方案提供的词库。项目地址: https://github.com/fkxxyz/rime-cloverpinyin

本项目精简了这个词库，并增加了自然码辅助码。

### clover_double_pinin.schema.yaml

基于四叶草拼音方案的输入法配置文件。针对双拼词库进行了修改。在小狼毫可以即插即用。

### 其他

一些小狼毫的设置文件。可以无视。

## 2. 输入方案简介

小鹤双拼
![小鹤双拼方案](/xiaohe.png)
自然码辅助码
![自然码辅助码](/fzm.png)

自然码方案的项目地址: https://github.com/copperay/ZRM_Aux-code

## 3. 为什么会有这套方案

小鹤双拼是目前比较有名并且活跃度很高的双拼方案，上手非常简单，容易记，兼容性好。

拼音输入方案的一个问题在于，中文有太多多音字了。当输入一个拼音，会出现很多字让我们选择。一页一页翻找是非常花时间的。那么能不能用字形特征帮助我们筛选呢？这就是辅助码的基本想法。

小鹤也提供辅助码，然而小鹤的方案门槛是属于略高了。因为小鹤追求降低重码，必然会规定特定的“拆字”规则，增加拆字的难度。

自然码的辅助码的设计比较亲民。自然码的辅助码中，所有声母都代表偏旁的读法。例如，输入“飒”，输入sa;l(立)f(风)，即可选中。每个字的编码不唯一，非常宽松。例如，sa;fl也可以打出“飒”。特殊规则比较少，只有会写字，按直觉输入辅助码，大概率可以得到想要的结果。

那么为什么要重建词库？rime中提供的双拼方案是用schema.yaml的algebra中的正则表达式，加辅助码就要改正则。但我不会，且并没有搜到满足需求的方案。与其折腾正则并且不知道可能出什么bug，还不如几分钟写个脚本把词库转换了干脆、省心。

## 4. 其他

1. 其他软件的词库转到rime词库可以使用深蓝词库转换，项目地址:https://github.com/studyzy/imewlconverter

2. 如果要使用本词库的辅助码，需要在schema.yaml文件中的speller:algebra:加入- derive/^(\w+);\w+$/$1/。
