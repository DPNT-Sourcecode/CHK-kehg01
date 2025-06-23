from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            'A' : 50,
            'B' : 30,
            'C' : 20,
            'D' : 15
        }

        offers = {
            'A' : (3, 130), #3A for 130
            'B' : (2,45) # 2B for 45
        }

        total = 0
        counts = Counter(skus)

        for item, count in counts.items():
            if item not in prices:
                return -1 #invalid item

            if item in offers:
                offer_qty, offer_prices = offers[item]
                total += (count // offer_qty) * offer_prices
                total +=(count % offer_qty) * prices[item]
            
            else:
                total += count * prices[item]

        return total


