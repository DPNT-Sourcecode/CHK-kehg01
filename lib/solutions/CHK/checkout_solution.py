from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            'A' : 50,
            'B' : 30,
            'C' : 20,
            'D' : 15,
            'E' : 40 #2E get one B for free
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

            if 'E' in counts and 'B' in counts:
                free_b = counts['E'] // 2
                counts['B'] = max(0, counts['B'] - free_b)

            if 'A' in counts:
                a_count = counts['A']
                num_5A = a_count // 5
                rem_after_5A = a_count % 5
                num_3A = rem_after_5A // 3
                rem_after_3A = rem_after_5A % 3
                total += num_5A * 200 + num_3A * 130 + rem_after_3A * prices['A']
                counts['A'] = 0

            if 'B' in counts:
                b_count = counts['B']
                total += (b_count // 2) * 45 + (b_count % 2) * prices['B']

            for item in['C','D','E']:
                total += counts[item] * prices[item]

            return total




