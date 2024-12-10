import os
import time
import json

input_file = "/shared_data/users.json"
output_file = "/updated_data/users_updated.json"

while True:
    if os.path.exists(input_file):
        with open(input_file, "r") as f:
            users = json.load(f)

        # Met à jour les mots de passe
        for user in users:
            user["password"] = "updated_" + user["password"]

        # Stocke les utilisateurs mis à jour
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w") as f:
            json.dump(users, f)

        print(f"Updated {len(users)} user passwords.")
    else:
        print("No user data found to update.")

    time.sleep(30)

