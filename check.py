import requests
from bs4 import BeautifulSoup


def check_url(url):
    """
    检查给定的URL是否有效。
    """
    检查给定的URL是否有效。

    Args:
        # url(str): 要检查的URL地址。
    Args:
        url(str): 要检查的URL地址。

    Returns:
        bool: 如果URL有效，则返回True；否则返回False。
    Returns:
        bool: 如果URL有效，则返回True；否则返回False。

    """
    max_retries = 2
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.RequestException:
            if attempt < max_retries - 1:
                continue
            else:
                return False
    """
    max_retries = 2
    for attempt in range(max_retries):
        try:
            # 发送HTTP GET请求
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                # 如果响应状态码为200，表示URL有效
                return True
            else:
                # 如果响应状态码不为200，表示URL无效
                return False
        except requests.RequestException:
            # 如果捕获到requests.RequestException异常
            if attempt < max_retries - 1:
                # 如果重试次数未达到最大次数，继续重试
                continue
            else:
                # 如果重试次数达到最大次数，返回False
                return False


def extract_and_check_urls(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    all_links = soup.find_all('a', href=True)
    for link in all_links:
        url = link['href']
        if check_url(url):
            # print(f"网址 {url} 存在")
            pass
        else:
            print(f"网址 {url} 不存在")


if __name__ == "__main__":
    html_file_path = "index.html"
    extract_and_check_urls(html_file_path)
