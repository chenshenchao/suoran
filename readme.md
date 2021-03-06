# [suoran](https://github.com/chenshenchao/suoran)

## 使用

```bash
# 安装
pip install suoran

# 创建骨架
suoran new myapp

# 也可以在现有的目录内生成文件
suoran init
```

### 扩展 Sanic 控制器相关的路由

```python
# app.py
from suoran import new_application

app = new_application()

@app.listener('before_server_start')
async def initialize(app, loop):
    '''
    初始化。
    '''

    # 加载控制器包
    app.control('controller')

app.apply()
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

## 源码

### 开发

```bash
# 安装到本地环境
pip install -e . -i https://pypi.python.org/pypi

# 指定源更新
pip install --upgrade suoran -i https://pypi.python.org/pypi
```

### 测试

```bash
# 所有测试
python -m unittest discover test/unit -p *.py

# 指定测试
python -m unittest test.route
```

### 发布

```bash
# 安装发布工具
pip install twine wheel

# 打包
python setup.py sdist bdist_wheel

# 上传
twine upload dist/*
```
