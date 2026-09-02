class PriceAmount:
    def __init__(self , value , currency):
        self.value=value
        self.currency=currency.upper()
        
    def __str__(self):
        return f"{self.currency}  {self.value:.2f}"
    
    def __repr__(self):
        return f"PriceAmount(value={self.value:.2f}, currency='{self.currency}')"

    def __add__(self, other):
        if not isinstance(other,PriceAmount):
            raise ValueError(f"Cannot add price amounts with different currencies:{self.currency} and {other.currency}.")
        
        if self.currency != other.currency:
            raise ValueError(
                f"Cannot add price amounts with different currencies: "
                f"'{self.currency}' and '{other.currency}'."
            )
        
        return PriceAmount(self.value + other.value , self.currency)
    
    def __eq__(self, other):
        if not isinstance(other,PriceAmount):
            return False
        
        return self.value == other.value and self.currency == other.currency
            
p1 = PriceAmount(19.99, "usd")
p2 = PriceAmount(10.01, "USD")
p3 = PriceAmount(15.00, "EUR")

print(str(p1))      # Output: USD 19.99
print(repr(p1))     # Output: PriceAmount(value=19.99, currency='USD')

total = p1 + p2
print(str(total))   # Output: USD 30.00

print(p1 == PriceAmount(19.99, "USD")) # Output: True

try:
    bad_addition = p1 + p3
except ValueError as e:
    print(e)  # Output: Cannot add price amounts with different currencies: 'USD' and 'EUR'.