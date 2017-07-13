import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

df = pd.read_csv("ds-all-data.csv")
df["InterestRate"].plot.bar(figsize=(50,10), fontsize=55)
# this is a bad data visualization, please never do this.
plt.show()
