# [suoran](https://github.com/chenshenchao/suoran)

## 安装

```bash
pip install suoran
```

## 扩展 Sanic 控制器相关的路由

```python
# app.py
from suoran import Application
from . import controller # 定义控制器的模块或包

app = Application()

@app.listener('before_server_start')
async def initialize(app, loop):
    '''
    初始化。
    '''
    app.control(controller)
```

```python
# controller/__init__.py
from sanic.response import json
from suoran import route

@route.get('/')
async def index(request):
    '''
    Sanic 类似的定义。
    '''
    return json({ 'index': 1 })

class IndexController:
    '''
    '''

    @route.get('/index.html')
    async def index(self, request):
        '''
        比 Sanic 多出 self 参数。
        '''
        return json({ 'index': 2 })
```

## 测试

```bash
# 所有测试
python -m unittest discover test/unit -p *.py

# 指定测试
python -m unittest test.route
```
