import datetime
import hashlib


def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

def convert_date(time):
    try:
        date = datetime.datetime.strptime(time, "%Y%m%d").date()
    except Exception as e:
        data = datetime.datetime.now().date()
    return date

if __name__ == '__main__':
    print(get_md5('http://www.baidu.com'))
    print(datetime.datetime.now())