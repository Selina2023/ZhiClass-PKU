import requests
from bs4 import BeautifulSoup
import re
import os

def fetch_wechat_article(url):
    # 获取页面内容
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page content: {response.status_code}")
    
    return response.text

def parse_article(html):
    soup = BeautifulSoup(html, 'html.parser')

    # import pdb; pdb.set_trace()
    
    title = soup.find('h1', class_='rich_media_title').get_text(strip=True)
    # extract tag from title (before ' | ')
    tag = "其他"
    tags = re.search(r'(.+?)\s\|', title)
 
    if tags:
        tag = tags.group(1)
    

    # import pdb; pdb.set_trace()
    # 解析发布日期
    # date_string = soup.find('span', id='publish_time').get_text(strip=True)
    # import pdb; pdb.set_trace()
    # date = soup.find('em', id='publish_time').get_text(strip=True)
    # date = None

    # date_element = soup.find('em')  # 如果可能的话，检查所有的 <em> 标签
    # if date_element:
    #     date = date_element.get_text(strip=True)
    # if not date:
    #     # 也可以检查其他可能的标签或属性
    #     date_element = soup.find('span', class_='publish_time')  # 示例class
    #     if date_element:
    #         date = date_element.get_text(strip=True)
    # import pdb; pdb.set_trace()
    # 假设作者信息是通过某个 class 找到的，例如 'rich_media_meta_text'
    # 并且作者是多个，可以从中提取出来
    author_elements = soup.find_all('span', class_='rich_media_meta_text')
    authors = [author.get_text(strip=True) for author in author_elements]
    if not authors:
        authors = ["智学会"]


    return {
        "title": title,
        "tags": tag,
        "authors": authors
    }


def generate_md_content(article_info, url, date, summary=""):

    md_content = f"""---
title: "{article_info['title']}"
date: {date}
externalUrl: {url}
draft: false
showAuthor: true
authors:
    - "{article_info['authors'][0]}"
showAuthorBadges: true
summary: {summary}
tags: [{article_info['tags']}]
---
"""
    return md_content

def save_md_file(md_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(md_content)
    print(f"File saved as {filename}")

def main():
    url = "https://mp.weixin.qq.com/s/8iRJp-JQ_tUN9MDLUVdp9g"
    html = fetch_wechat_article(url)
    article_info = parse_article(html)
    output_dir = "./activities/2022-11-03_0/"
    #parse date from output_dir
    date = re.search(r'\d{4}-\d{2}-\d{2}', output_dir).group(0)
    # import pdb; pdb.set_trace()
    md_content = generate_md_content(article_info, url, date)
    os.makedirs(output_dir, exist_ok=True)
    save_md_file(md_content, output_dir+'index.md')

if __name__ == "__main__":
    main()

