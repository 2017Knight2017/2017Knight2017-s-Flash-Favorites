import json
import random

# Path to your JSON file
json_file = input("Enter the path to your JSON file: ").strip('"')

# Load the JSON data
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Shuffle the 'games' list
if 'games' in data and isinstance(data['games'], list):
    random.shuffle(data['games'])

    # Write the updated JSON back to the file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    input("Playlist shuffled successfully. Press Enter to exit.")
else:
    print("'games' key not found or is not a list.")