from sanic.response import json, html
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