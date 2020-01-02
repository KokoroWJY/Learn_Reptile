class Content:
    """
    所有文章/网页的共同基类
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        用灵活的打印函数控制结果
        """
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY: {}".format(self.body))

class Website:
    """
    描述网站结构的信息
    """
    # 储存关于如何抓取数据的命令
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag