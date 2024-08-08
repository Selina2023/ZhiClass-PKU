# Update Log
- 8月9日
    - research模块和activity模块基本搭建完成（可能存在一些小bug但是不影响使用）。我在```./content/research/example```、```./content/activities/example```以及```./content/activities/example_2```中放了三个例子。展示了如何使用这两个模块。**请注意，research模块的配置参数经过特殊设计，请严格按照例子中的格式进行配置。**
    - 我按照我的需求调整了config中的一些参数，确保网页在```layout = "background"```模式以及```showCard=false```的情况下可以正常运行（当然其他参数可能也改了，我只写出我记得比较重要的两个）。
    - homepage的显示方式进行了调整，大家可以运行查看，主要改了```_index.md```的渲染方式，把标题居左并调整了宽度，我觉得这样比较美观。同时homepage的文章卡片是使用[shortcode](https://blowfish.page/zh-cn/docs/shortcodes/)的方式实现的，可以参考```_index.md```中的写法。
        - 请参考```./layouts\partials\article-link\simple.html```
    - 现在的research文章实现了以下的功能
        - 点标题跳arxiv
        - 点标签（arxiv, github...）跳相应网站
        - 作者名字加粗
        - 显示摘要
        - 请参考```./layouts\partials\article-meta\basic.html```以及```./layouts\partials\home\background.html```
    - activity的文章基本上是用blowfish的内置功能实现的，该有的都有了
    - 我按照[这篇文章](https://blowfish.page/zh-cn/docs/advanced-customisation/)的方法修改了源码（**请不要直接更改源码！！**），更改的文件放在：
        - ```./layouts\partials\article-link\simple.html```
        - ```./layouts\partials\article-meta\basic.html```
        - ```./layouts\partials\home\background.html```
    - 有任何问题请联系林宇辰

# TODO
- 修复显示cite.bib的问题
- 我们不需要fork，可以换一下submodule的源

