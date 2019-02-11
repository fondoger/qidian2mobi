# qidian2mobi

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

![电子书目录](https://github.com/fondoger/qidian2mobi/raw/master/screenshots/screenshot2.png)


![电子书正文](https://github.com/fondoger/qidian2mobi/raw/master/screenshots/screenshot3.png)

