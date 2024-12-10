import os
import time
import random
import string
import json

output_file = "/shared_data/users.json"

def generate_random_username():
    return "user_" + "".join(random.choices(string.ascii_lowercase, k=8))

def generate_random_password():
    return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=128))

while True:
    users = []
    for _ in range(5):  # Génère 5 utilisateurs à la fois
        username = generate_random_username()
        password = generate_random_password()
        users.append({"username": username, "password": password})

    # Écrit les utilisateurs dans un fichier partagé
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(users, f)

    print(f"Generated {len(users)} users and passwords")
    time.sleep(30)

