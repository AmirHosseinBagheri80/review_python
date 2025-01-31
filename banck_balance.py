class Card: 
    def __init__(self, card_number, expiry_date, cvv2, card_holder, balance): 
        self.card_number = card_number 
        self.expiry_date = expiry_date 
        self.cvv2 = cvv2 
        self.card_holder = card_holder 
        self.balance = balance 
    def __str__(self):
            return f"Card Holder: {self.card_holder}, Card Number: {self.card_number}, Expiry Date: {self.expiry_date}, CVV2: {self.cvv2}, Balance: {self.balance} Toman"
cards=[
     Card("1111 1111 0011 1111","04/11","112","akbar",1200000),
     Card("1111 5612 0011 1111","07/10","312","amir",9910020),
     Card("1111 1211 0011 1111","04/12","122","armin",1200)
]
for card in cards:
     if card.balance > 5000:
          print("acount balance:",card)