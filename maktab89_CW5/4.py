import random


def lottery(n):
    tickets = []
    while len(tickets) < n:
        # if (x := random.randrange(1_000_000_000, 9_999_999_999)) not in tickets:
        #     tickets.append(x)
        tickets.add(random.randrange(1_000_000_000, 9_999_999_999))
    print(tickets)
    return tickets


number = int(input('number of tickets: '))


winners = random.sample(lottery(number), k=2)
print(f'🤩 lucky Winners: {winners[0]} 🏆 , {winners[1]} 🏆')


