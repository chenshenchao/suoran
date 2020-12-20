from os import read
from sanic.response import json, html, redirect
from suoran import route


@route.get('/')
async def index(request):
    '''
    Sanic 类似的定义。
    '''
    return redirect('/index.html')


class IndexController:
    '''
    '''

    @route.get('/index.html')
    async def index(self, request):
        '''
        比 Sanic 多出 self 参数。
        '''

        with open('./view/index.html', 'r', encoding='utf8') as reader:
            return html(reader.read())
