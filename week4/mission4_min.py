import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Q1
"""
idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19,11,5,97]
series = pd.Series(data, index=idx)
series = series[((10<series) & (series<20))]
print(series)


"""
Q2
"""
df1 = pd.DataFrame([["cherry", "Fruit", 100],
                    ["mango", "Fruit", 110],
                    ["potato", "Vegetable", 60],
                    ["onion", "Vegetable", 80]],
                    columns=["Name", "Type", "Price"])
df2 = pd.DataFrame([["pepper", "Vegetable", 50],
                    ["carrot", "Vegetable", 70],
                    ["banana", "Fruit", 90],
                    ["kiwi", "Fruit", 120]],
                    columns=["Name", "Type", "Price"])

df3 = pd.concat([df1,df2], axis=0)
print(df3)

df_fruit = df3.loc[df3["Type"] == 'Fruit'].sort_values(by=["Price"], ascending=False)
df_veg = df3.loc[df3["Type"] == 'Vegetable'].sort_values(by=["Price"], ascending=False)
print(df_fruit)
print(df_veg)
print("Sum of Top 2 Fruit Price : ", sum(df_fruit[:2]["Price"]))
print("Sum of Top 2 Vegetable Price : ", sum(df_veg[:2]["Price"]))


"""
Q3
"""
idx = ["Sue", "Ryan", "Jay", "Jane", "Anna"]
col = ["Round_1", "Round_2", "Round_3", "Round_4", "Round_5"]
data = [[55,65,60,66,57],
        [64,77,71,79,67],
        [88,81,79,89,77],
        [45,35,30,46,47],
        [91,96,90,97,99]]

df = pd.DataFrame(data, index = idx, columns=col)
col_round_6 = pd.Series([11,15,13,17,19], index=idx)
df["Round_6"] = col_round_6
print(df)
print(df.describe().loc[["mean","max", "min"]])


"""
Q4
"""
t = np.arange(0.,5.,0.2)
plt.plot(t,t,"r--")
plt.plot(t,t**2,"gs")
plt.plot(t,t**3,"b^")
plt.show()


"""
Q5
"""
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9,3))

plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('Categorical Plotting')
plt.show()