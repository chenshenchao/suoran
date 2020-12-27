from suoran import route, view
from model.visitor import Visitor


class VistorController:
    '''
    '''

    @route.get('/visitor/index.html')
    async def index(self, request):
        '''
        '''
        page = request.args.get('p', [1])[0]
        limit = 20
        offset = (page - 1) * limit
        r = await Visitor.all().offset(offset).limit(20)
        return view.render('visitor/index.html', visitors=list(r))

    @route.get('/visitor/<vid:int>.html')
    async def info(self, request, vid):
        '''
        '''

        return view.render('visitor/info.html')
