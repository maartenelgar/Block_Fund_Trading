






class Account:
    """
    Main account class
    Store settings and trades data
    """
    fee = FEES

    def __init__(self, initial_capital, fee=None):
        self.initial_capital = initial_capital
        self.buying_power = initial_capital
        self.number = 0
        self.date = None
        self.equity = []
        self.positions = []
        self.opened_trades = []
        self.closed_trades = []
        self.opened_orders = []
        if isinstance(fee, dict):
            self.fee = fee

    def total_value(self, current_price):
        """
        Return total balance with open positions
        :param current_price:
        :return:
        """
        # print(self.buying_power)
        # for p in self.positions: print(p)  # positions
        # for ot in self.opened_trades: print(ot)  # open trades
        in_pos = sum(
            [p.size * current_price for p in self.positions
             if p.type_ == 'Long']) + sum(
            [p.size * (p.entry_price - current_price + p.entry_price)
             for p in self.positions
             if p.type_ == 'Short'])
        return self.buying_power + in_pos
