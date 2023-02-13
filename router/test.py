from router import Router, Route, Callback
from test.views import *
from utils import get_digit

# router = Router(
#     Route('main', description='main description', chield=[
#         Route('name of route1', description='description',
#               chield=[
#                   Route('name of route 1-1', description='description', callback=('func', 'module.name')),
#                   Route('name of route 1-2', description='description', callback=('func', 'module.name')),
#                   Route('name of route 1-3', description='description', callback=('func', 'module.name'))
#               ]),
#         Route('name of route 2', description='description', callback=('func', 'module.name')),
#         Route('name of route 3', description='description', callback=('func', 'module.name')),
#         Route('name of route 4', description='description', callback=('func', 'module.name')),
#         Route('name of route 5', description='description',
#               chield=[
#                   Route('name of route 5-1', description='description', callback=('func', 'module.name')),
#                   Route('name of route 5-2', description='description', callback=('func', 'module.name')),
#                   Route('name of route 5-3', description='description', callback=('func', 'module.name'))
#               ])
#           ])
# )

# router()
# c = Callback('hello', 'test.views', 'dobare', kw='dsjfklsdfj')
# c()

routes = [
    Route('name 1/', test1, name='address_name'),
    Route('name 1/name 1-1', test1_1, name='address_name'),

    Route('name 1/name 1-2', test1_2, name='address_name'),
    Route('name 2/name 2-1', test2_1, name='address_name'),
    Route('name 2/name 2-2', test2_2, name='address_name'),
    Route('name 2/name 2-3', test2_3, name='address_name'),

    Route('name 2', test2, name='address_name'),

    Route('name 2/name 2-4', test2_4, name='address_name'),
    Route('name 2/name 2-4/name 2-4-1', test2_4_1, name='address_name'),
    Route('name 2/name 2-4/name 2-4-2', test2_4_2, name='address_name'),
]

router = Router(routes)
router.make()
Router.get_next_route(router)
# r = Router(routes)

# r.get_next_route()



# main = Route('main', description='main description', chield=[
#         Route('name of route1', description='description',
#               chield=[
#                   Route('name of route 1-1', description='description', callback=('func', 'module.name')),
#                   Route('name of route 1-2', description='description', callback=('func', 'module.name')),
#                   Route('name of route 1-3', description='description', callback=('func', 'module.name'))
#               ]),
#         Route('name of route 2', description='description', callback=('func', 'module.name')),
#         Route('name of route 3', description='description', callback=('func', 'module.name')),
#         Route('name of route 4', description='description', callback=('func', 'module.name')),
#         Route('name of route 5', description='description',
#               chield=[
#                   Route('name of route 5-1', description='description', callback=('func', 'module.name')),
#                   Route('name of route 5-2', description='description', callback=('func', 'module.name')),
#                   Route('name of route 5-3', description='description', callback=('func', 'module.name'))
#               ])
#           ])
#
# main()