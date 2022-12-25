import uuid


class Ticket:
    def __init__(self, ticket_type, ticket_amount=0):
        # M1 --> chargeable ticket
        # M2 --> one way ticket
        # M3 --> two way ticket
        self.ticket_type = ticket_type
        self.ticket_amount = ticket_amount
        self.ticket_serial = str(uuid.uuid4())
        self.status = True


class Client:
    def __init__(self, fname, lname, is_admin, ssn):
        self.fname = fname
        self.lname = lname
        self.is_admin = is_admin
        self.ssn = ssn
        self.id = str(uuid.uuid4())
        self.tickets = []

    def buy_ticket(self, ticket):
        if isinstance(ticket, Ticket):
            self.tickets.append(ticket)
        return self.tickets


class Gate:
    cost = 1500

    def __init__(self):
        pass

    def process_ticket(self, client, chosen_ticket_type):
        tickets = client.tickets
        use_ticket = object
        if not tickets:
            return -1
        else:
            for ticket in tickets:
                if ticket.status:
                    if ticket.ticket_type == chosen_ticket_type:
                        use_ticket = ticket
                        Gate.__use_ticket(use_ticket)
                        break

    @staticmethod
    def __use_ticket(use_ticket):
        if use_ticket.ticket_type == 1:
            if use_ticket.ticket_amount < 1500:
                return -2
            else:
                use_ticket.ticket_amount -= 1500
                return 0

    def __charge_ticket(self):
        pass


