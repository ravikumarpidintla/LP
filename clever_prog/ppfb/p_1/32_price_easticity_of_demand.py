import pandas as pd
data = pd.DataFrame({"Demand": [20, 30, 31, 33, 30, 33, 35],
                     "Price": [2000, 1800, 1850, 1700, 1800, 1700, 1600]})

# print(data)
# adding new fields now
data["% Change in demand"] = data["Demand"].pct_change()
data["% Change in price"] = data["Price"].pct_change()
data["Price Elasticity"] = data["% Change in demand"] / data["% Change in price"]
print(data)