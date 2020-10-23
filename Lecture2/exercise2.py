cover_price = 24.95
discount = 0.6  #factor
shipping = 3
shipping_extra = 0.75
copies = 60

cost = copies * (cover_price * discount) + (copies - 1) * shipping_extra + 3
