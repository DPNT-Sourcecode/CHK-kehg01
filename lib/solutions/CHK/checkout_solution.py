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



        if not all(char in prices for char in skus):
            return -1



        total = 0
        counts = Counter(skus)


        #apply free item offers
        for trigger, required, free_item in free_offers:
            if trigger in counts:
                free_qty = counts[trigger] // required
                if free_item in counts:
                    if trigger == free_item:
                        counts[free_item] -= free_qty
                    else:
                        counts[free_item] = max(0, counts[free_item] - free_qty)


        #group[ discount
        group_counts = []
        for item in group_offer_items:
            group_counts.extend([item] * counts[item])
            counts[item] = 0

        group_counts.sort(keys=lambda  x:prices[x], reverse=True)
        while len(group_counts) >= group_offer_count:
            total += group_offer_price
            for _ in range(group_offer_count):
                group_counts.pop(0)

        #remaining items in group not covered
        for item in group_counts:
            total+= prices[item]

        #apply multi buy offers
        for item, deals in offers.items():
            if item in counts:
                qty = counts[item]
                for deal_qty, deal_price in sorted(deals, reverse=True):
                    deal_count = qty //deal_qty
                    total+= deal_count * deal_price
                    qty %= deal_qty
                total += qty * prices[item]
                counts[item] = 0




        return total








