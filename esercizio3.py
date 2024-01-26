import pandas as pd
from matplotlib import pyplot as plt

nome_file = "./election.csv"
data = pd.read_csv(nome_file)

# Raggruppa i dati per distretto e somma i voti totali
totali_per_distretto = data.groupby("district")["total"].sum()

# Estrai i distretti e i voti totali
distretti = totali_per_distretto.index
totali_voti = totali_per_distretto.values

plt.bar(distretti, totali_voti)
plt.xlabel("Distretto")
plt.ylabel("Voti Totali")
plt.show()

