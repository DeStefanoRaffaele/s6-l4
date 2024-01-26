import pandas as pd
from matplotlib import pyplot as plt

nome_files = "./stockdata.csv"
data = pd.read_csv(nome_files, usecols=["AAPL","Date"]) #estrazione determinate colonne
x = data["Date"].head(20) #estraiamo le prime 5 righe
y = data["AAPL"].head(20)
plt.plot(x,y, color="r", linestyle="--", marker="o",markerfacecolor="black",linewidth=2)
plt.xlabel("Data")
plt.ylabel("Valore")
plt.title("Azioni Apple")
plt.show()

data2 = pd.read_csv(nome_files) #estrazione file
x , y = data2["Date"], data2["IBM"]
x1 , y1 = data2["Date"], data2["SBUX"]
x2 , y2 = data2["Date"], data2["MSFT"]
x3 , y3= data2["Date"], data2["AAPL"]
x4 , y4= data2["Date"], data2["GSPC"]
plt.plot(x,y, "b")
plt.plot(x1,y1, "r")
plt.plot(x2,y2, "g")
plt.plot(x3,y3, "m")
plt.plot(x4,y4, "y")
plt.legend("legenda", loc="lower right")
plt.show()
