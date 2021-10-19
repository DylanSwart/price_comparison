class Solution(object):

    def combinationsum(self, food, target):
        result = []
        unique = {}
        food = list(set(food))
        self.solve(food, target, result, unique)
        return result

    def solve(self, food, target, result, unique, i=0, current=[]):

        if target == 0:
            temp = [i for i in current]
            temp1 = temp
            temp.sort()
            temp = tuple(temp)

            if temp not in unique:
                unique[temp] = 1
                result.append(temp1)
                return

        if target < 0:
            return

        for x in range(i, len(food)):
            current.append(food[x])
            self.solve(food, target-food[x], result, unique, i, current)
            current.pop(len(current)-1)


food_price_dict = {
    'Sea Salt Crackers': 2,
    'Griffins Snax': 2.5,
    'Pizza Shapes': 3.3,
    'Arnotts Cheds': 3.99,
    'Rosemary Wheat': 2,
    'Original Rice Crackers': 1.65
}

budget = float(input("Budget: $"))

ob1 = Solution()
print(ob1.combinationsum(food_price_dict.values(), budget))
