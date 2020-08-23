from snownlp import SnowNLP

List = ['如果大口大口喝，这是一款清爽而令人愉悦的饮料','市场不会超过48','现在就可以买发布错了不是6号是现在','75一箱24罐也不便宜','激动了一下，还以为24瓶一箱的，整小两百瓶呢','还以为是*24的，差评','3.1一瓶？感觉要比可乐便宜才划算','这价格，买这么多，爆料人你下得去手吗？','...基本上平时也是这个价格吧，没什么诚意的活动','喝瓶巴黎水起码有味儿!','纸箱臭的一b回收垃圾料做的','36.8是原味啊','好羡慕我们这里夏天持续到11月中旬','买了买了家里还有两箱好价感谢','下了4箱屯着','很便宜，不过夏天快结束了～(￣▽￣～>~','我很好奇，这个就是个没味道的气泡水，6块多一瓶…真有那么好喝吗？','气泡水可以说是一种风靡世界的明星饮料了，它不含糖无余的热量摄入，对人体无负担，而深受大家的喜爱','我怎么看到是119','还有隐藏优惠券？我怎么只能3件打8折也到不了你这个价格？']

def dataAnalysis(text):
    return SnowNLP(text).sentiments

if __name__=='__main__':
    for comment in List:
        result = SnowNLP(comment).sentiments
        print(result)
