import re
import http.client
import urllib.parse

# 定义一个字典来映射HTTP状态码和它们的中文含义
STATUS_CODE_MAPPING = {
    200: "成功",
    301: "永久移动",
    302: "临时移动",
    403: "禁止访问",
    404: "未找到",
    500: "服务器内部错误",
    # 可以根据需要添加更多的状态码和对应的中文含义
}


def check_urls_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 使用正则表达式匹配所有的网址
        urls = re.findall(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        for url in urls:
            try:
                parsed_url = urllib.parse.urlparse(url)
                conn = http.client.HTTPSConnection(
                    parsed_url.netloc, timeout=3) if parsed_url.scheme == 'https' else http.client.HTTPConnection(parsed_url.netloc, timeout=3)
                conn.request("GET", parsed_url.path)
                response = conn.getresponse()
                status_code = response.status
                if status_code != 200:
                    status_message = STATUS_CODE_MAPPING.get(
                        status_code, "未知状态码")
                    print(f"{url} 的状态码是 {status_code}，含义是 {status_message}")
                conn.close()
            except Exception as e:
                print(f"{url} 无法访问。错误信息: {e}")


# 调用函数并传入index.html文件的路径
check_urls_in_file('index.html')
