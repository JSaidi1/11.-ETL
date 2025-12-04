import pandas as pd
import requests


def main():
    """
    Main function: for Exercice 5
    """
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    # ========================================================================
    # Get envs:
    # ========================================================================

    env_file = Path(__file__).parent / "config" / "env" / "test.env"
    load_dotenv(dotenv_path=env_file)

    if not Path(env_file).exists():
        print(f"\n[WARNING]: ENV_FILE not found: {env_file}\n")

    # ========================================================================
    # Others operations:
    # ========================================================================
    API_KEY = os.getenv('OPENWEATHER_API_KEY')
    BASE_URL = os.getenv('BASE_URL')

    url = f'{BASE_URL}/weather'

    # --------- 1. Définir une liste de 10 villes françaises
    villes = ['Lille', 'Belfort', 'Strasbourg', 'Toulouse', 'Tourcoing', 'Roubaix', 'Marseille', 'Mulhouse', 'Nancy', 'Nice']
    temps_actuelles = []
    temps_ressenties = []
    humidites = []
    descriptions = []

    # --------- 2.Pour chaque ville, récupérer :
        # Température actuelle
        # Température ressentie
        # Humidité
        # Description

    for ville in villes:
        params = {
            'q': ville,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'fr'
        }

        # Appel HTTP GET vers l'API.
        response = requests.get(url, params=params)

        # Conversion de la réponse en JSON.
        data = response.json()
        print(data)

        print(f"Météo à {ville} :")
        print(f"Température actuelle : {data['main']['temp']}°C")
        print(f"Température ressentie : {data['main']['feels_like']}°C")
        print(f"Humidité : {data['main']['humidity']}%")
        print(f"Description : {data['weather'][0]['description']}.")

        # preparation pour la question 3:
        temps_actuelles.append(data['main']['temp'])
        temps_ressenties.append(data['main']['feels_like'])
        humidites.append(data['main']['humidity'])
        descriptions.append(data['weather'][0]['description'])

    df = pd.DataFrame({
        'ville': villes,
        'temp_actuelle': temps_actuelles,
        'temp_ressentie': temps_ressenties,
        'humidity': humidites,
        'description': descriptions
    })

    print(df)

    # --------- 4. Identifier la ville la plus chaude et la plus froide:
    ville_la_plus_froide = df.sort_values(by='temp_actuelle', ascending=True).head(1)
    ville_la_plus_chaude = df.sort_values(by='temp_actuelle', ascending=False).head(1)

    print("\nville_la_plus_froide:")
    print(ville_la_plus_froide[['ville', 'temp_actuelle']])
    print("\nville_la_plus_chause:")
    print(ville_la_plus_chaude[['ville', 'temp_actuelle']])

    # --------- 5. Calculer la température moyenne:
    temp_moyenne = df['temp_actuelle'].mean()
    print("\ntemp_moyenne:")
    print(temp_moyenne)

    # --------- 6. Sauvegarder dans meteo_villes.csv
    df.to_csv('./ex5/meteo_villes.csv', index=False)

    # --------- 7. Bonus : Ajouter une gestion d'erreur si une ville n'est pas trouvée:




















if __name__ == "__main__":
    main()