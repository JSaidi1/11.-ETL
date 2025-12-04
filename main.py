# ================== Exercice 4 - REST Countries ==================
import requests
import pandas as pd



API_BASE_URL = "https://restcountries.com/v3.1"

# 1. Récupérer tous les pays d'Europe
response = requests.get(API_BASE_URL + "/region/europe")
response.raise_for_status()

for pays in response.json():
    print(f"\npays = {pays}")

# 2. Créer un DataFrame avec : nom, capitale, capitale, superficie
names = []
capitals = []
populations = []
areas = []

for pays in response.json():
    # print(f"\npays.name = {pays['name']['common']}")
    names.append(pays['name']['common'])
    capitals.append(pays['capital'][0])
    populations.append(pays['population'])
    areas.append(pays['area'])

df = pd.DataFrame({
    'name': names,
    'capital': capitals,
    'population': populations,
    'area': areas
})

print(df)

# 3. Calculer la densité de population (population / superficie)
print("\nAjout de la colonne 'density': ")
df['density'] = df['population'] / df['area']
print(df)

# 4. Identifier les 5 pays les plus peuplés d'Europe
print("\nTop 5 pays les plus peuplés d'europe: ")
top_5_country = df.sort_values(by='population', ascending=False).head(5)
print(top_5_country[['name', 'population']])

# 5. Calculer la population totale de l'Europe
population_europe = df['population'].sum()

print(f"Population totale de l'Europe : {population_europe:,} habitants")

# 6. Trouver le pays avec la plus grande densité
print("\nLe pays le plus 'dense' d'europe: ")
top_1_country = df.sort_values(by='density', ascending=False).head(1)
print(top_1_country[['name', 'density']]) # Monaco  19021.28712

# 7. Sauvegarder les résultats dans pays_europe.xlsx
df.to_excel('./ex4/pays_europe.xlsx', index=False)

