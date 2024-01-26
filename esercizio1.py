import pandas as pd
from matplotlib import pyplot as plt

nome_files = "./stockdata.csv"
data = pd.read_csv(nome_files, usecols=["MSFT","Date"]) #estrazione determinate colonne
plt.plot(data["Date"],data["MSFT"], "r*-") #grafico sulla colonna MSFT
plt.show()

x = data["Date"].head(5) #estraiamo le prime 5 righe
y = data["MSFT"].head(5)
plt.plot(x,y)
plt.xlabel("Date", color="red") # aggiunge legenda all'asse x
plt.ylabel("MSFT", color="blue") # aggiunge legenda all'asse y
plt.show()

x1 = data["Date"].tail(5) #estraiamo le ultime 5 righe
y1 = data["MSFT"].tail(5)
plt.bar(x,y)
plt.xlabel("Date", color="g") # aggiunge legenda all'asse x
plt.ylabel("MSFT", color="m") # aggiunge legenda all'asse y
plt.show()
