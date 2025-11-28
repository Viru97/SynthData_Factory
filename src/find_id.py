import json
import glob
import os

# CONFIGURATION
DATA_DIR = "/home/apurv/SynthData_Factory/output/fancy_run"


def find_target_id():
    # 1. Look for the labels JSON file
    # It usually has 'labels' in the name, e.g., bounding_box_2d_tight_labels_0.json
    pattern = os.path.join(DATA_DIR, "*labels*.json")
    files = glob.glob(pattern)

    if not files:
        print("Could not find a labels JSON file.")
        print("Please look in your output folder manually for a .json file that isn't the 'prim_paths' one.")
        return

    # 2. Open the first one found
    target_file = files[0]
    print(f"Reading mapping file: {target_file}")

    with open(target_file, 'r') as f:
        data = json.load(f)

    # 3. Search for 'industrial_box'
    # The structure is usually { "class": { "industrial_box": 123 } }
    found_id = None

    if 'class' in data:
        class_map = data['class']
        print("\n--- Available Classes ---")
        for name, id_val in class_map.items():
            print(f"Name: {name} | ID: {id_val}")
            if name == "industrial_box":
                found_id = id_val

    print("\n-------------------------")
    if found_id is not None:
        print(f"✅ SUCCESS! The Semantic ID for 'industrial_box' is: {found_id}")
        print(f"Please use ID {found_id} in your converter script.")
    else:
        print("❌ ERROR: Could not find 'industrial_box' in the file.")


if __name__ == "__main__":
    find_target_id()