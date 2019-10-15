import os
from datetime import datetime, timedelta
import subprocess
import sys
import requests
from random import randint, sample
import time


class SMCurlTolls:

    def __init__(self, path, domain, token):
        self.path = path
        self.domain = domain
        self.token = token

    @property
    def post_url(self):
        data = self.crate_url
        length = len(data).__str__()
        headers = {
            'User-Agent': 'curl/7.12.1',
            'Host': 'data.zz.baidu.com ',
            'Content-Type': 'text/plain',
            'Content-Length': length,
        }

        url = ' http://data.zz.baidu.com/urls?site=www-mipcdn-com-1236.aienao.com&token=tjH9outQeNMoDxNT&type=mip'

        response = requests.post(url=url, headers=headers, data=data, timeout=30)
        return response.content

    @property
    def crate_url(self):
        string = ''
        for x in range(0, 100):
            string += self.domain + '/html/' + self.rand_char() + '.html\n'
        string = string.strip('\n')
        return string

    @staticmethod
    def rand_char():
        date = datetime.now().strftime('%Y%m%d')
        string = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        return date + ''.join(sample(string, 5))


# 推送url到百度
def post_all_url(thread_num, domain, token, target_path, post_list):
    post = 'curl -H "Content-Type:text/plain" --data-binary @%s ' \
             '"http://data.zz.baidu.com/urls?site=%s&token=%s&type=mip"' % (target_path, domain, token)
    output = subprocess.Popen(post, shell=True, stdout=subprocess.PIPE)
    out, err = output.communicate()
    try:
        http = eval(out)
        print(http)
        if b'success' in out:
            sys.stdout.write('\n%s 任务 %s 推送成功条 %s 条 校验成功 %s 条 剩余额度 %s 目标网址 %s 栏目 %s\n'
                             % (print_time(), thread_num, http['success'], http['success_mip'], http['remain'],
                                domain, post_list))

            return int(http['remain'])
        else:
            sys.stdout.write('\n推送失败! error: %s \n' % http['message'])
            return 0
    except IndexError as index:
        sys.stdout.write("\n%s %s \n" % (index, '服务器未返回数据'))
        time.sleep(3)


def print_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# sm = SMCurlTolls('', 'www-mipcdn-com-1235.aienao.com', 'tjH9outQeNMoDxNT')
# result = sm.post_url
# print(result)

post_all_url(
    1,
    'www-mipcdn-com-1236.aienao.com',
    'tjH9outQeNMoDxNT',
    '../url/cache/1_lsj0000_www_xiandaoliaoli_com.txt',
    'lsj'
)