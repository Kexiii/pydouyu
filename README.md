# pydouyu
斗鱼TV三方API、弹幕接口实现

# Install
- Install python3 & pip3
- Install pydouyu
    - pip3 install pydouyu

# Example
````python
from pydouyu.client import Client
import time
import sys


def chatmsg_handler(msg):
    output = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()) + msg['nn'] + ": " + msg['txt']
    print(output)
    sys.stdout.flush()


def uenter_handler(msg):
    output = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()) + msg['nn'] + " 进入了直播间"
    print(output)
    sys.stdout.flush()


c = Client(room_id=562590)
c.add_handler('chatmsg', chatmsg_handler)
c.add_handler('uenter', uenter_handler)
c.start()

````

# Usage
- TODO