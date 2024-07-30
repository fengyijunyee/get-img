# 图片批量下载器

## 项目描述

这是一个Python脚本，用于批量下载随机图片API的图片。它支持多线程下载，可以配置下载次数以及是否对单张图片使用多个线程进行下载。此外，脚本还集成了日志记录和进度条显示功能，以增强用户体验。

## 安装与运行

确保你的环境中已安装以下Python库：

- `requests`：用于发起HTTP请求。
- `concurrent.futures`：用于多线程处理。
- `logging`：用于日志记录。
- `tqdm`：用于进度条显示。

你可以通过以下命令安装所需的库：

```bash
pip install requests tqdm
```
运行脚本：

```bash
python get-imgv4.py
```
## 如何使用

运行脚本后，按提示输入图片的URL、保存目录、线程数、重复下载次数及是否使用多线程下载每张图片的选项。
脚本将开始下载图片，并在控制台显示下载进度。
日志信息将实时输出至控制台，记录下载状态和任何可能发生的错误。

##功能特点

多线程下载：利用多线程加速下载过程。
重复下载：可以设置重复下载图片的次数。
日志记录：详细记录下载过程中的信息和警告。
进度条：直观显示下载进度。

##贡献指南

欢迎贡献者提交问题报告或代码改进。请遵循以下步骤：

叉取（fork）此仓库。
创建一个新的分支进行修改。
提交更改并推送至你的仓库。
发起一个拉取请求（pull request）。

##许可证

本项目采用GPL许可证。更多信息参见LICENSE文件。

如果你在使用过程中遇到任何问题，或者有改进建议，请随时通过GitHub Issue提出。我们期待你的反馈！
