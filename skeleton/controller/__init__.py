from sanic.response import redirect
from suoran import route
from suoran.view import render


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

        return render('index.html')

    @route.get('/about.html')
    async def about(self, request):
        return render('about.html')
