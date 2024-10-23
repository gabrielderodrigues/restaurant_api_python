class MenuItem:
    def __init__(self, company, item, price, description):
        self.company = company
        self.item = item
        self.price = price
        self.description = description
        
    def __repr__(self):
        return f"{self.item} from {self.company} - Price: {self.price} - Description: {self.description}"