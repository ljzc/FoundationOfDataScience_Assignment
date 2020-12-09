import codecs
import chardet
if __name__ == '__main__':
    content = codecs.open("source_code.html", "rb").read()
    print(chardet.detect(content)["encoding"])