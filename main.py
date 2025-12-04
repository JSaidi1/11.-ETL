from collections import Counter

import requests
import pandas as pd

# Ex 3:
#======

#--- 1. Récupérer tous les utilisateurs (/users)

# URL de base de l'API de test JSONPlaceholder.
BASE_URL = "https://jsonplaceholder.typicode.com"

# Cet endpoint renvoie les utilisateurs
users_url = f"{BASE_URL}/users"

# Envoi d'une requête GET pour récupérer tous les posts.
response = requests.get(users_url)

print("users = ", response.json())

#--- 2. Afficher le nom et l'email de chaque utilisateur
for user in response.json():
    print(f"user_id: {user.get('id')} => username:{user.get('username')} - email:{user.get('email')}")

#--- 3. Récupérer tous les posts de l'utilisateur avec userId=1
# Cet endpoint renvoie une liste de posts (articles de blog fictifs).
posts_url = f"{BASE_URL}/posts"
response = requests.get(posts_url)

print(response.json())

posts_user_1 = {'user_id': '1'}
# post = {'title':, 'body:'}
posts_list = []
posts = {}

for post in response.json():
    if post.get('userId') == 1:
        posts['title'] = post.get('title')
        posts['body'] = post.get('body')
        posts_list.append(posts)
        posts = {}

print("Les posts du userId=1 => ", posts_list)


#--- 4. Compter combien de posts chaque utilisateur a créé
users_id = []
for post in response.json():
    for userId in {post.get('userId')}:
        users_id.append(userId)

user_articles = Counter(users_id)

for user_id in user_articles:
    print(f"userId: {user_id} => {user_articles[user_id]}")

#--- 5. Récupérer les commentaires du post id=1:
comments_url = f"{BASE_URL}/comments"
response = requests.get(comments_url)
# print(response.json())
print(response.json()[0])

#--- 6. Créer un DataFrame Pandas avec :
# Colonnes : post_id, post_title, nombre_commentaires
# Pour les 10 premiers posts



# Exemple de données
post_ids = list(range(1, 11))
post_titles = [
    f"Post numéro {i}" for i in range(1, 11)
]
nombre_commentaires = [12, 5, 33, 7, 19, 4, 8, 21, 15, 2]

#dataFrame
df = pd.DataFrame({
    "post_id": post_ids,
    "post_title": post_titles,
    "nombre_commentaires": nombre_commentaires
})

print(df)





