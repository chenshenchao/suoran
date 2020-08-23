from pkgutil import iter_modules
from importlib import import_module
from sanic import Sanic


class Application(Sanic):
    '''
    '''

    def __init__(
        self,
        name=None,
        router=None,
        error_handler=None,
        load_env=True,
        request_class=None,
        strict_slashes=False,
        log_config=None,
        configure_logging=True
    ):
        super().__init__(
            name=name,
            router=router,
            error_handler=error_handler,
            load_env=load_env,
            request_class=request_class,
            strict_slashes=strict_slashes,
            log_config=log_config,
            configure_logging=configure_logging
        )

    def control(self, module, deep=True):
        '''
        加载控制器。
        '''

        # 加载路由。
        if hasattr(module, '___router___'):
            router = getattr(module, '___router___')
            router.route(self)

        # 是否深入解析。
        name = module.__name__
        if deep and module.__loader__.is_package(name):
            for _, child, _ in iter_modules(module.__path__):
                mn = '{}.{}'.format(name, child)
                m = import_module(mn)
                self.control(m, deep)
