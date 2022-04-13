# coding:utf-8
import jieba
# 词云需要将句子拆解，所以导入jieba库（中文分词工具）
import requests
from matplotlib import pyplot as plt
# 绘图工具 数据可视化 偏科研
from wordcloud import WordCloud
# 词汇
from PIL import Image
# 图片处理
import numpy as np
# 用于矩阵运算
import sqlite3 #数据库

# text = "1.111.987987..。。65757."
# username = "1.111.987987..。。65757."


# text = "在情感方面，D型人一个坚定果敢的人，酷好变化，喜欢控制，干劲十足，独立自主，超级自信。可是，由于比较不会顾及别人的感受，所以显得粗鲁、霸道、没有耐心、穷追不舍、不会放松。D型人不习惯与别人进行感情上的交流，不会恭维人，不喜欢眼泪，匮乏同情心。 在工作方面，D型人是一个务实和讲究效率的人，目标明确，眼光全面，组织力强，行动迅速，解决问题不过夜，果敢坚持到底，在反对声中成长。但是，因为过于强调结果， D型人往往容易忽视细节，处理问题不够细致。爱管人、喜欢支使他人的特点使得D型人能够带动团队进步，但也容易激起同事的反感。在人际关系方面， D型人喜欢为别人做主，虽然这样能够帮助别人做出选择，但也容易让人有强迫感。由于关注自己的目标， D型人在乎的是别人的可利用价值。喜欢控制别人，不会说对不起。描述性词语：积级进取、争强好胜、强势、爱追根究底、直截了当、主动的开拓者、坚持意见、自信、直率1.具强大动力与本意来达成目的与创意—固执顽固者。有宏大的愿景且能快速在众多外界事件中找出有意义的模范。对所承负职务，具良好能力于策划工作并完成。具怀疑心、挑剔性、独立性、果决，对专业水准及绩效要求高 "
# text = "如果解决不了，你要看看自己的编码，让二者匹配即可。有的时候应该这么写："
def ciyun(text, username):
    # 将结论拼接成一个连续的字符串
    # print(text)
    # 分词
    cut = jieba.cut(text)
    # print(cut)
    # 将每个分词之间加入空格
    string = ' '.join(cut)# 在每个单词中间加入空格
    print(string) #观察
    print(len(string)) #看分词的数量

    # 图1
    img = Image.open(r'base/CiYun/women.jpg') # 打开词云需要的遮罩图片
    img_array = np.array(img)# 将图片转换为数组
    # 定义输出的词云图片
    wc = WordCloud(
        background_color='white',
        mask=img_array,
        font_path="msyh.ttc",
        width=800,
        height=400,
        scale=3,
        min_font_size=2,
        max_words=120,

        # 字体所在位置：C:\Windows\Fonts
    #     微软雅黑字体
    )
    wc.generate_from_text(string)
    # 切好的词 词云的规则
    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off') # 是否显示坐标轴
    plt.savefig(r'./media/CiYun/'+username+'cy1')
    # plt.show() #显示生成的词云图片

    # 输出词云图片到文件
    # plt.savefig(r"\wordman.jpg",dpi=1500)# 输出文件并提高分辨率

    # 图2
    img = Image.open('base/CiYun/man.jpg') # 打开词云需要的遮罩图片
    img_array = np.array(img)# 将图片转换为数组
    # 定义输出的词云图片
    wc = WordCloud(
        background_color='white',
        mask=img_array,
        font_path="msyh.ttc",
        width=800,
        height=400,
        scale=3,
        min_font_size=2,
        max_words=120,
        # 字体所在位置：C:\Windows\Fonts
    #     微软雅黑字体
    )
    wc.generate_from_text(string)
    # 切好的词 词云的规则
    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off') # 是否显示坐标轴
    plt.savefig(r'./media/CiYun/'+username+'cy2')
    # plt.show() #显示生成的词云图片

    # 输出词云图片到文件
    # plt.savefig(r'wordwomen.jpg',dpi=1500)# 输出文件并提高分辨率
    return 111
