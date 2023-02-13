from __future__ import annotations
from importlib import import_module
from typing import Union, List
from utils import get_digit


class Router:
    idx = 0
    pair_idx = list()

    def __init__(self, routes: List[Route]):
        self.routes = routes
        self.address = None
        self.routes_real_idx = None
        self.next_route = None

    def make(self):
        self.routes_real_idx = enumerate(self.routes, 1)

        for real_idx, route in self.routes_real_idx:
            address = route.address.strip('/')
            if address:
                r = address.split('/')
                if len(r) > 1:
                    pass
                else:
                    Router.idx += 1
                    Router.pair_idx.append((Router.idx, real_idx))
                    print(f'{Router.idx}: {address}')

    def get_next_route(self):
        if user_input := get_digit('> '):
            for idx, real_idx in Router.pair_idx:
                if user_input == idx:
                    self.next_route = self.routes[real_idx - 1]
                    print(self.next_route.address)
                    Router.idx = 0
                    self.make_route()
                    return
            else:
                print('wrong input')
        else:
            print('wrong input')

    def make_route(self):
        for route in self.routes:
            self.address = route.address.strip('/')
            if self.address:
                r = self.address.split('/')
                if len(r) > 1:
                    pass
                else:
                    Router.idx += 1
                    print(f'{Router.idx}: {self.address}')

    def __call__(self, *args, **kwargs):
        self.make_route()


class Route:
    idx = 0
    def __init__(self, address: str, callback: Callback = None, name=None):
        self.address = address
        self.name = name
        self.callback = callback
        self.idx = 0

    # def make_route(self):
    #     self.address = self.address.strip('/')
    #     r = self.address.split('/')
    #     if len(r) > 1:
    #         pass
    #     else:
    #         Route.idx += 1
    #         print(f'{Route.idx}: {self.address}')

    def get_next_route(self):
        if user_input := get_digit('> '):
            print('route')
        else:
            print('wrong input')

    def get_current_route(self):
        print(self.address)

    def __call__(self, *args, **kwargs):
        self.route = self._get_route()


class Callback:
    def __init__(self, func: Union[str, None], module_name: Union[str, None], *args, **kwargs):
        self.func = func
        self.module_name = module_name

        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        self.func = getattr(
            import_module(self.module_name or __name__),
            self.func if isinstance(self.func, str) else self.func.__name__)

        self.func(*self.args, **self.kwargs)



