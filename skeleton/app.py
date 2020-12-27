from suoran import new_application, view, model

app = new_application()


@app.listener('before_server_start')
async def initialize(app, loop):
    '''
    初始化。
    '''
    app.control('controller')
    app.static('/', './public')
    await model.init(app, initial=True)
    view.init('view')


@app.listener('after_server_stop')
async def uninitialize(app, loop):
    '''
    '''

    await model.exit(app)

app.apply()
