class Comment(object):
    def __init__(self, time, content, author=""):
        self.time = time
        self.content = content
        # self.author = author


class Comments(object):
    def __init__(self):
        self.comments = []

    def add_comment(self, comment: Comment):
        self.comments.append(comment)
