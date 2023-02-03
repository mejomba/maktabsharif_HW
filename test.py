# import argparse
# from datetime import datetime
# parser = argparse.ArgumentParser()
# parser.add_argument('-f', '--full', type=str)
# parser.add_argument('-y', '--year', type=int)
# parser.add_argument('-m', '--month', type=int)
# parser.add_argument('-d', '--day', type=int)
# args = parser.parse_args()
#
# if args.full:
#     dif = datetime.now() - datetime.strptime(args.full, "%Y/%m/%d")
# else:
#     dif = datetime.now() - datetime.strptime(f'{args.year}/{args.month}/{args.day}', "%Y/%m/%d")
#
# print(f'You are {dif.days // 365} years old')
from datetime import timedelta




from test_lookup import home
print(home.codes.OK)

a = 5
print(home.__doc__)
