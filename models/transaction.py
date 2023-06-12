class Transaction:
    # possible additions - user
    def __init__(self, amount, merchant, date, tag, id = None):
        self.amount = amount
        self.merchant = merchant
        self.date = date
        self.tag = tag
        self.id = id