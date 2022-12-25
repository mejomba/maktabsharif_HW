from models import *
import pickle
import os


print('Welcome to the metro App.')

while True:
    login_type = int(input('''
please select:
    1. Client Login
    2. Admin Login
> '''))
    if login_type in [1, 2]:
        break
    else:
        print('wrong input')

if login_type == 1:
    print('client login')
elif login_type == 2:
    print('admin login')

print("""
    1. buy a ticket
    2. Trip
    3. exit
""")
option = int(input())
for ticket in client.tickets:
    print(ticket.ticket_type)

selected_ticket_type = int(input('choose one of ticket types: '))

if option == 1:
    pass
elif option == 2:
    gete=Gate()
    gate.process_ticket(client, selected_ticket_type)
elif option == 3:
    pass


# if not (clients := os.listdir('clients')):
#     print("No client found")
# else:
#     print(f'you have {len(clients)} client')
