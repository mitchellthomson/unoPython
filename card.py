class Card:
    def __init__(self, color, special, number):
        self.color = color
        self.special = special
        self.number = number
        
    def __str__(self):
        return f"{self.get_special_card()} - {self.color}"
    
    def __repr__(self):
        return f"{self.get_special_card()} - {self.color}"

    def get_special_card(self):
        if self.number == None:
            return self.special
        else:
            return self.number