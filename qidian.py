import requests
import shutil
from bs4 import BeautifulSoup
import urllib.request
import shutil
import os
from ebooklib import epub
import time

# mobi格式简介 https://www.cnblogs.com/buptzym/p/5249662.html

s = requests.Session()
s.headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


epubTOC = []
book = epub.EpubBook()

# add copyright description
copyright = epub.EpubHtml(title="版权声明", file_name="copyright.html")
copyright.content = """<h1>版权声明</h1>
<p>本工具目的是将免费网络在线小说转换成方便kindle用户阅读的mobi电子书, 作品版权归原作者或网站所有, 请不要将该工具用于非法用途。</p>
<p>GitHub: https://github.com/fondoger/qidian2mobi<p>
"""
book.add_item(copyright)
epubTOC.append(epub.Link("copyright.html", "版权声明", "intro"))

def handle_url(url):
    # handle urls like `//example.com`
    if url[:2] == '//':
        return "http:" + url
    return url

def download_image(url, path):
    url = handle_url(url)
    urllib.request.urlretrieve(url, path)
    print("success saved book cover image:", url)

chapters_count = 0
def handle_chapter(chapter: "soup") -> 'EpubHtml':
    global chapters_count
    chapter_name = chapter.get_text()
    chapter_url = chapter.find('a')['href']
    print(chapter_name, handle_url(chapter_url))
    r = s.get(handle_url(chapter_url))
    soup = BeautifulSoup(r.content, features="html.parser")
    content = soup.find('div', {'class': 'read-content'})
    chapters_count += 1
    c = epub.EpubHtml(title=chapter_name,
            file_name="chapter_%d.html" % chapters_count)
    c.set_content("<h1>" + chapter_name + "</h1>" + str(content))
    book.add_item(c)
    # time.sleep(0 if random.randint(0, 10) < 8 else 1)
    return c

def handle_volume(volume: "soup"):
    volume_name = volume.find('h3').get_text()[56:]
    print("handling volume: " + volume_name)
    chapters = volume.find_all('li')
    global temp
    epub_chapters = []
    for chapter in chapters:
        c = handle_chapter(chapter)
        epub_chapters.append(c)
    epubTOC.append((epub.Section(volume_name), epub_chapters))

def main():
    print("请输入起点中文网小说URL")
    print("(形如: https://book.qidian.com/info/<小说id>#Catalog)")
    novel_url = input("请输入: ")
    r = s.get(novel_url)
    soup = BeautifulSoup(r.content, features="html.parser")
    book_cover_src = soup.find('a', {'id': 'bookImg'}).find('img')['src']
    book_info = soup.find('div', {'class': 'book-info'})
    book_title = book_info.find('em').string
    book_author = book_info.find('a').string
    # get all
    volumes = soup.find_all('div', {'class': 'volume'})
    for volume in volumes:
        handle_volume(volume)

    # set title
    book.set_title(book_title)
    # set author
    book.add_author(book_author)
    # set cover
    download_image(book_cover_src, "book_cover.jpg")
    book.set_cover('cover.jpg', open('book_cover.jpg', 'rb').read())
    # set book language
    book.set_language('zh_Hans')
    # set book's TOC
    book.toc = epubTOC
    # add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # save book
    epub.write_epub('book.epub', book)
    print(book_title + "-" + book_author, end=" ")
    print("successfully saved to book.epub")

    print("you can use kindlegen tool to convert epub to mobi")
    print("for example: `bin/kindlegen book.epub`")
    print("(choose executable file in bin/ directory depending on your operating system.)")


if __name__ == '__main__':
    main()
