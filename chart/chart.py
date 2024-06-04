import matplotlib.pyplot as plt

years = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]
incidents = [ 50, 100,250, 500, 750, 1000, 1500, 2000]

plt.plot(years, incidents, marker='o')
plt.title("figure 1 : Évolution des Cybermenaces au Fil des Décennies")
plt.xlabel("Années")
plt.ylabel("Nombre d'Incidents Significatifs")
plt.grid(True)
plt.show()