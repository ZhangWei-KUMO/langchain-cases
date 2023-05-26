# langchain-cases

这是一个开源的langchain实例集合，为什么要写这样一个开源库？原因很简单，官方库坑太多。原因如下：
1. 在使用langchain的时候终端Shell需要开启VPN;
2. 目前langchain只支持3.5;
3. 需要依赖nltk;
4. 需要依赖向量数据库chroma；
5. pip/python/numpy/urllib3存在版本号冲突问题。

在使用langchain的python版本原则上应在3.9,urllib3应为1.26.6 


加载[nltk](https://github.com/nltk/nltk_data/tree/gh-pages), 在报错提示的文件夹中创建nltk_data文件夹，下载文件中tokenizers和taggers文件架里的文件全部解压放入nltk_data文件夹。