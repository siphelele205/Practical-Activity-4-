import pandas as pd

# Read the dataset
df = pd.read_csv("C:\Users\Maziya\Desktop\python programs\motor_data11-14Lats.csv")


print(df.head(10))


filtered_df = df[df["sets_num"] > 40]
print(filtered_df[["make", "usage"]])


import matplotlib.pyplot as plt

"""plt.scatter(df["carrying_capacity"], df["effective_yr"])
plt.xlabel("Carrying Capacity")
plt.ylabel("Effective Year")
plt.title("Carrying Capacity vs Effective Year")
plt.show()"""""
