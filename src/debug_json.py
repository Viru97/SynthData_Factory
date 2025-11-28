import numpy as np
import os
import glob

# Configuration
DATA_DIR = "/home/apurv/SynthData_Factory/output"


def inspect_npy():
    # Find the first .npy file
    npy_files = sorted(glob.glob(os.path.join(DATA_DIR, "bounding_box_2d_tight_*.npy")))

    if not npy_files:
        print("No .npy files found.")
        return

    target_file = npy_files[0]
    print(f"Inspecting file: {target_file}")

    # Load the data
    try:
        data = np.load(target_file)

        print(f"\n--- Data Structure ---")
        print(f"Shape: {data.shape}")
        print(f"Data Type (dtype): {data.dtype}")

        # Check if it has named columns (structured array)
        if data.dtype.names:
            print(f"Field Names: {data.dtype.names}")

        print("\n--- First Row of Data ---")
        print(data[0] if len(data) > 0 else "Empty Array")

    except Exception as e:
        print(f"Error loading numpy file: {e}")


if __name__ == "__main__":
    inspect_npy()