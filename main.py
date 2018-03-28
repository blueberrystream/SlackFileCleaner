import json
import logging
import urllib.request
import os
from datetime import datetime
import time

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class PostJson(object):
    def __init__(self):
        self.LEGACY_TOKEN = os.environ['LEGACY_TOKEN']

    def headers(self):
        return {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': 'Bearer {0}'.format(self.LEGACY_TOKEN)
        }

    def file_list(self, page):
        return {
            'token': self.LEGACY_TOKEN,
            'count': '100',
            'page': page
        }

    def file_delete(self, file):
        return {
            'token': self.LEGACY_TOKEN,
            'file': file
        }


def handler(event, context):
    CLEAN_AFTER_DAYS = os.environ['CLEAN_AFTER_DAYS']
    # list all files / you can only get 100 files/1 page at files.list
    for cnt_page in range(1, 100):
        url = 'https://slack.com/api/files.list'
        post_body = PostJson().file_list(cnt_page)
        req = urllib.request.Request(
            url,
            urllib.parse.urlencode(post_body).encode('utf-8'))
        res = urllib.request.urlopen(req)
        files = json.loads(res.read().decode('utf-8'))
        # get files info
        for file in files.get('files'):
            logger.info('check file timestamp: %s ', file.get('id', ''))
            # get timestamp of the file
            ts = file.get('timestamp',
                          '1000000000')  # epoch 2001/9/9 10:46:40 if blank
            ts_datetime = datetime.fromtimestamp(float(ts))
            now_datetime = datetime.now()
            diff_datetime = now_datetime - ts_datetime
            # check old file
            if (int(diff_datetime.days) > int(CLEAN_AFTER_DAYS)):
                logger.info('delete file: %s', file.get('id', ''))
                # Delete files / require scope : Legacy-token & Administrator role
                post_data = PostJson().file_delete(file.get('id', ''))
                post_head = PostJson().headers()
                url = 'https://slack.com/api/files.delete'
                req = urllib.request.Request(
                    url,
                    data=json.dumps(post_data).encode('utf-8'),
                    method='POST',
                    headers=post_head)
                res = urllib.request.urlopen(req)
                # tmp = json.loads(res.read().decode('utf8')) #dbg
                # print (tmp) #dbg
                logger.info('message result: %s', res.msg)
        # exit if all files are checked
        if len(files.get('files', 0)) < 100:
            print('done! :' + str(len(files.get('files', 0))))
            break
    return 'ok'
