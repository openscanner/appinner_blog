# Appinner Blog

## Base on pelican

- HomePage http://blog.getpelican.com/
- Manual http://docs.getpelican.com/
- Theme http://pelicanthemes.com/ https://github.com/getpelican/pelican-themes
- Plugin https://github.com/getpelican/pelican-plugins

## install 

```sh
pip install pelican markdown

cd appinner_blog
git submodule update --init --recursive

```


## meta

Markdown 格式博客开头如下, 注意:
1. lang 表示语言,现在支持两种语言: en/英文 和 cn/中文
2. Slug 表示博客地址页, 注意 多个语言的要 一致
```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
lang: en
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.
```

## 插件
https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites

## 主题
https://github.com/talha131/pelican-elegant

## 撰写博客

1. 博客内容放在 content 中
2. 图片放在 content/images 中

## 发布

生成静态页面

```
make html 
```

发布到 github page, 这里使用了 master分支 docs 目录,所以不用 提交到 gh-pages 分支。

将 docs 和 content目录提交到 master 即可

## 访问地址

https://openscanner.github.io/appinner_blog/
