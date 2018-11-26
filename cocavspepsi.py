from matplotlib import pylab as plt
import pandas

df1 = pandas.read_csv("KO.csv")
print(df1.head())
df1['Date'] = pandas.to_datetime(df1.Date)

df2 = pandas.read_csv("PEP.csv")
print(df2.head())
df2['Date'] = pandas.to_datetime(df2.Date)
indexes = []

plt.title('Coca Cola vs Pepsi')

plt.plot(df1.Date, df1.Close, "r:", label="Coke", linewidth=0.5, ms=0.5)
plt.plot(df2.Date, df2.Close, "b:", label="Pepsi", linewidth=0.5, ms=0.5)

plt.legend(loc="upper left")
plt.xlabel("Month")
plt.ylabel("Price")
plt.show()