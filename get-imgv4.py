import os
import requests
import time
import concurrent.futures
import logging
from tqdm import tqdm

class TqdmHandler(logging.Handler):
    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)
        except Exception:
            self.handleError(record)

# 配置日志
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = TqdmHandler()
formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(threadName)s] %(message)s', '%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
log.addHandler(handler)

def save_image(url, directory, progress_bar=None):
    """
    从给定的URL下载图像并保存到指定目录。
    
    参数:
    url (str): 图像的URL。
    directory (str): 保存图像的目录路径。
    progress_bar (tqdm.tqdm): 进度条对象，用于更新进度。
    
    返回:
    无
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 获取图片的名称，这里简单地使用时间戳作为文件名
            filename = f"{int(time.time())}_{os.getpid()}.jpg"
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            log.info(f"Image saved to {filepath}")
            if progress_bar is not None:
                progress_bar.update(1)
        else:
            log.warning("Failed to retrieve image")
    except Exception as e:
        log.error(f"Error saving image: {e}")

def download_images(url, directory, num_threads, num_repeats, multi_thread_per_image):
    """
    使用多线程下载同一图像多次，并显示下载进度。
    
    参数:
    url (str): 图像的URL。
    directory (str): 保存图像的目录路径。
    num_threads (int): 并发下载的线程数。
    num_repeats (int): 重复下载的次数。
    multi_thread_per_image (bool): 是否使用多线程下载每一张图片。
    """
    if multi_thread_per_image:
        # 如果启用多线程下载每张图片，则创建线程数等于num_threads的任务
        total_tasks = num_threads * num_repeats
        urls = [url] * total_tasks
        
        # 使用tqdm的thread_map显示进度
        list(concurrent.futures.ThreadPoolExecutor(max_workers=num_threads).map(lambda u: save_image(u, directory), urls))
    else:
        # 否则，每个重复下载使用一个线程
        with tqdm(total=num_repeats, desc="Downloading images") as pbar:
            for _ in range(num_repeats):
                save_image(url, directory, progress_bar=pbar)

def main():
    """
    主函数，用于交互式获取图像URL、保存目录、线程数、重复次数和多线程下载选项，然后下载图像。
    """
    # 请求用户输入保存图片的目录
    directory = input("请输入保存目录（绝对路径）: ")
    
    # 检查目录是否存在，如果不存在则创建
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 请求用户输入图片的URL
    url = input("请输入图片的URL: ")

    # 请求用户输入线程数
    num_threads = int(input("请输入并发下载的线程数: "))

    # 请求用户输入重复下载的次数
    num_repeats = int(input("请输入重复下载的次数: "))

    # 请求用户选择是否使用多线程下载每张图片
    multi_thread_per_image = input("是否使用多线程下载每张图片？(y/n): ").lower().startswith('y')

    # 连续下载图片
    download_images(url, directory, num_threads, num_repeats, multi_thread_per_image)

if __name__ == "__main__":
    main()