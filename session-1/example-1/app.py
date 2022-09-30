def price_updater(prices, increase_rate):
    
    new_price_list = []
    for price in prices:
        if isinstance(price, float) or isinstance(price, int):
            new_price = price + (price * increase_rate)
            new_price_list.append(new_price)
        else:
            return "Incorrect Price Detected!"
        
    return new_price_list



