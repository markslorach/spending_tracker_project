class Transaction:
    # possible additions - date, time, user
    def __init__(self, amount, merchant, tag, id = None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.id = id