from pydouyu.client import Client
import time
import sys

otype_to_str = {
    "0": "普通用户",
    "1": "房管",
    "2": "主播",
    "3": "超管"
}


def chatmsg_handler(msg):
    try:
        output = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()) + msg['nn'] + ": " + msg['txt']
        print(output)
        sys.stdout.flush()
    except Exception as e:
        print("chatmsg_handler failed. Exception: %s" % e)


def uenter_handler(msg):
    try:
        output = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()) + msg['nn'] + " 进入了直播间"
        print(output)
        sys.stdout.flush()
    except Exception as e:
        print("uenter_handler failed. Exception: %s" % e)


def newblackres_handler(msg):
    try:
        output = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()) + \
                 "[" + otype_to_str[msg['otype']] + "] " + \
                 msg['snic'] + " 封禁了 " + msg['dnic'] + " 到 " + msg['endtime']
        print(output)
        sys.stdout.flush()
    except Exception as e:
        print("newblackres_handler failed. Exception: %s" % e)


c = Client(room_id=562225)
c.add_handler('chatmsg', chatmsg_handler)
c.add_handler('uenter', uenter_handler)
c.add_handler('newblackres', newblackres_handler)
c.start()
