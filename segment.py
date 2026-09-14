import jieba

sentence = "我来到北京清华大学参观学习"

seg_list = jieba.cut(sentence, cut_all=False)
print("精确模式: " + "/ ".join(seg_list))

seg_list = jieba.cut(sentence, cut_all=True)
print("全模式: " + "/ ".join(seg_list))

seg_list = jieba.cut_for_search(sentence)
print("搜索引擎模式: " + "/ ".join(seg_list))
