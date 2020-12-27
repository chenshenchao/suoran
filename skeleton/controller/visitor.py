from suoran import route, view


class VistorController:
    '''
    '''

    @route.get('/visitor/index.html')
    async def index(self, request):
        '''
        '''
        return view.render('visitor/index.html')

    @route.get('/visitor/<vid>.html')
    async def info(self, request):
        '''
        '''

        return view.render('visitor/info.html')
