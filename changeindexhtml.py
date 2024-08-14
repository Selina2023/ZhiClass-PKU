import re
import time

def change_html():
    # 读取HTML内容
    with open('./public/index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    html_content = re.sub(
        r'class="flex flex-col h-screen px-6 m-auto text-lg leading-7 max-w-7xl bg-neutral text-neutral-900 dark:bg-neutral-800 dark:text-neutral sm:px-14 md:px-24 lg:px-32 scrollbar-thin scrollbar-track-neutral-200 scrollbar-thumb-neutral-400 dark:scrollbar-track-neutral-800 dark:scrollbar-thumb-neutral-600">',
        lambda m: re.sub(r'(px-|sm:px-|md:px-|lg:px-)\d+', lambda n: n.group(1) + '0', m.group(0)),
        html_content
    )

    html_content = re.sub(
        r'class="flex flex-col h-screen px-0 m-auto text-lg leading-7 max-w-7xl bg-neutral text-neutral-900 dark:bg-neutral-800 dark:text-neutral sm:px-0 md:px-0 lg:px-0 scrollbar-thin scrollbar-track-neutral-200 scrollbar-thumb-neutral-400 dark:scrollbar-track-neutral-800 dark:scrollbar-thumb-neutral-600">',
        lambda m: re.sub(r'max-w-7xl', 'max-w-0xl', m.group(0)),
        html_content
    )

    html_content = re.sub(
        r'<div class="min-h-\[\d+px\]"></div>',
        '<div class="min-h-[0px]"></div>',
        html_content
    )

    
    # 在</main><footer id="site-footer" class="py-10 print:hidden">修改为<style>.stylecenter {margin-left: 30%;}</style></main><footer id="site-footer" class="py-10 print:hidden stylecenter">
    html_content = re.sub(
        r'</main><footer id="site-footer" class="py-10 print:hidden">',
        r'<style>.stylecenter {text-align: center; margin-left: auto; margin-right: auto;}</style></main><footer id="site-footer" class="py-10 print:hidden stylecenter">',
        html_content
    )
    


    # 寻找 <div class="mx-auto max-w-7xl p-0">，替换成<style>.container {max-width: 56rem;}</style><div class="mx-auto container p-0">
    # 前面边距修改后，后面内容的边距会与其他页面不一致，修改一下
    html_content = re.sub(
        r'<div class="mx-auto max-w-7xl p-0">',
        r'<style>.container {max-width: 64rem;}</style><div class="mx-auto container p-0">',
        html_content
    )


    with open('./public/index.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("替换完成，修改后的HTML已保存")


# 每0.5秒执行一次
while True:
    change_html()
    time.sleep(1)