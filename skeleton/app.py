from suoran import Application

app = Application()

@app.listener('before_server_start')
async def initialize(app, loop):
    '''
    初始化。
    '''
    app.control('controller')
    app.static('/', './public')

app.apply()
