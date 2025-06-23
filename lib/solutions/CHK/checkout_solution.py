from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            'A' : 50,'B' : 30,'C' : 20, 'D' : 15,'E' : 40,'F' : 10, 'G' :  20,'H' : 10, 'I' : 35 ,
            'J' : 60 ,'K' : 70 ,'L' : 90, 'M' : 15 ,  'N' : 40 ,
            'O' : 10 , 'P'  :50,'Q' : 30 ,    'R' : 50 ,   'S' : 20 ,    'T' : 20 ,    'U' : 40 ,
            'V' : 50 ,   'W': 20 ,   'X': 17 ,   'Y': 20 ,  'Z': 21

        }

        offers = {
            'A' : [(5, 200), (3,130)],
            'B' : [(2,45)],
            'H' : [(10,80), (5,45)],
            'K' : [(2,120)],
            'P' : [(5,200)],
            'Q' : [(3,80)],
            'V' : [(3,130), (2,90)]

        }

        free_offers = [
            ('E',2,'B'),
            ('F',2,'F'),
            ('N', 3, 'M'),
            ('R', 3, 'Q'),
            ('U', 3, 'U')

        ]

        group_offer_items = [ 'S', 'T', 'X', 'Y', 'Z']
        group_offer_price = 45
        group_offer_count = 3

        basket = Counter(skus)



        if not all(char in prices for char in skus):
            return -1

        #applu free item
        for trigger, qty, free_item in free_offers:
            eligible = basket[trigger] //qty
            basket[free_item] = max(0, basket[free_item] - eligible)



        total = 0
        group_counts = []

        # group[ discount
        for item in group_offer_items:
            group_counts.extend([item] * basket[item])



        group_counts.sort(key=lambda x: prices[x], reverse=True)

        while len(group_counts) >= group_offer_count:
            total += group_offer_price
            for _ in range(group_offer_count):
                removed = group_counts.pop(0)
                basket[removed] -= 1

        for item in group_counts:
            total += prices[item]

        # remaining items in group not covered
        # for item, qty in counts.items():
        # total += qty * prices[item]




        #apply multi buy offers
        for item, count in basket.items():
            if item not in prices:
                return -1
            item_total  = 0
            if item in offers:
                for offer_qty, offer_price in offers[item]:
                    offer_count = count //offer_qty
                    item_total += offer_count * offer_price
                    count %= offer_qty
                item_total += count * prices[item]
                total += item_total


        return total








