# pydouyu
![PyPI](https://img.shields.io/pypi/v/pydouyu.svg)  ![PyPI - Downloads](https://img.shields.io/pypi/dm/pydouyu.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pydouyu.svg)

斗鱼TV三方API、弹幕接口实现

# Feature
- 官方已公布的斗鱼三方API完整实现
- 自动重连
- 稳定、无（少）数据遗漏

# Install
- ```pip3 install pydouyu```

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