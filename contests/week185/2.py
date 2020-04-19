from typing import List
from collections import OrderedDict
# import pandas as pd
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """
        ["David","3","Ceviche"],["Corina","10","Beef Burrito"],
        :param orders:
        :return:
        """
        ret = OrderedDict()
        food_list = []
        table_list = []
        for order in orders:
            name, table, food = order[0], int(order[1]),order[2]
            ret[table] = ret.get(table, OrderedDict())
            ret[table][food] = ret[table].get(food, 0)+1
            food_list.append(food)
            table_list.append(table)
        food_list = list(set(food_list))
        table_list = list(set(table_list))
        food_list.sort()
        table_list.sort()

        result = []
        food_list.insert(0, 'Table')
        result.append(food_list)
        for table in table_list:
            temp = [f"{table}"]
            for food in food_list[1:]:
                temp.append(f"{ret[table].get(food, 0)}")
            result.append(temp)

        # print(ret)
        return result

if __name__ == '__main__':
    s = Solution()
    ans = s.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])
    print(ans)
    #
    orders = [["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"],
                 ["Amadeus", "12", "Fried Chicken"], ["Adam", "1", "Canadian Waffles"],
                 ["Brianna", "1", "Canadian Waffles"]]
    ans = s.displayTable(orders)
    print(ans)

    orders = [["Laura", "2", "Bean Burrito"], ["Jhon", "2", "Beef Burrito"], ["Melissa", "2", "Soda"], ["Laura", "2", "Bean Burrito"]]
    ans = s.displayTable(orders)
    print(ans)