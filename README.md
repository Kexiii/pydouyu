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

- 运行 Demo
    - ```git clone https://github.com/Kexiii/pydouyu.git```
    - ```cd pydouyu```
    - ```python3 example.py```
- 二次开发
    - 示例代码见 [example.py](https://github.com/Kexiii/pydouyu/blob/master/example.py)
    - 用户可以自定义handler函数，并且调用*Client.add_handler*注册
    - *Client.add_handler*传入的第一个参数为消息类型，有哪些消息类型见下文弹幕协议
    - msg是一个dict，其的各字段见下文中的弹幕协议
- [弹幕协议](https://github.com/Kexiii/pydouyu/releases)