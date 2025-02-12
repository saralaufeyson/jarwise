from app import create_app
import json
import os

# Define the path for the JSON storage
DATA_FILE = "finance_tracker.json"

# Function to create the JSON file if it doesn't exist
def init_json_storage():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"users": [], "jars": [], "transactions": []}, f, indent=4)

app = create_app()

if __name__ == '__main__':
    init_json_storage()  # Initialize JSON file
    app.run(debug=True)
