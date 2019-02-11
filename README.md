# 起点小说转mobi电子书

由起点中文网的免费小说生成epub电子书或者方便kindle阅读的mobi电子书。

## 食用方法

1. 获取起点中文网小说目录的网址, 如下图

![小说网址](https://github.com/fondoger/qidian2mobi/raw/master/screenshots/screenshot1.png)

2. 运行脚本，下载并生成epub电子书

```
python3 qidian.py
```

3. 使用kindlegen将epub电子书转换成mobi电子书

```
qidian2mobi$ bin/kindlegen book.epub
```

## kindle 截图

![电子书目录](https://github.com/fondoger/qidian2mobi/raw/master/screenshots/screenshot2.jpg)


![电子书正文](https://github.com/fondoger/qidian2mobi/raw/master/screenshots/screenshot3.jpg)

## 写在最后 

1. 生成的电子书是有封面的，可是网站给的封面图太小了，kindle上面不会显示。
2. 由于网站可能改版，本脚本可能会失效，欢迎提出issue，我会及时改进。

附上一本转换好的mobi电子书《编程之战》供参考。


