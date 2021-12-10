"""
return the taker/maker commission rate
"""

class CommissionRate:
    def __init__(self):
        self.symbol = ""
        self.makerCommissionRate = 0.0
        self.takerCommissionRate = 0.0

    @staticmethod
    def json_parse(json_data):
        result = CommissionRate()
        result.symbol = json_data.get_string("symbol")
        result.makerCommissionRate = json_data.get_float("makerCommissionRate")
        result.takerCommissionRate = json_data.get_float("takerCommissionRate")
        return result