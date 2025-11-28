import numpy as np
import os
import glob

# Configuration
DATA_DIR = "/home/apurv/SynthData_Factory/output/fancy_run"  # Output folder relative to this script
IMG_WIDTH = 1024
IMG_HEIGHT = 1024


def convert_to_yolo(x_min, y_min, x_max, y_max, width, height):
    """Converts bounding box to YOLO format [x_center, y_center, w, h]."""
    # Calculate center, width, and height
    x_center = ((x_min + x_max) / 2) / width
    y_center = ((y_min + y_max) / 2) / height
    w = (x_max - x_min) / width
    h = (y_max - y_min) / height

    return x_center, y_center, w, h


def main():
    # Look for .npy files instead of .json
    npy_files = glob.glob(os.path.join(DATA_DIR, "bounding_box_2d_tight_*.npy"))

    if not npy_files:
        print("No .npy files found! Check your DATA_DIR path.")
        return

    print(f"Found {len(npy_files)} files to process...")

    for npy_file in npy_files:
        # Load the numpy data
        try:
            data = np.load(npy_file)
        except Exception as e:
            print(f"Skipping {npy_file}: {e}")
            continue

        # Generate output filename:
        # Convert "bounding_box_2d_tight_0000.npy" -> "rgb_0000.txt"
        base_name = os.path.basename(npy_file)
        txt_name = base_name.replace("bounding_box_2d_tight_", "rgb_").replace(".npy", ".txt")

        # Create 'labels' folder
        out_path = os.path.join(DATA_DIR, "labels", txt_name)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        with open(out_path, 'w') as out_f:
            # Iterate through every object (row) in the file
            for row in data:
                # Extract fields using the names we found in inspection
                x_min = row['x_min']
                y_min = row['y_min']
                x_max = row['x_max']
                y_max = row['y_max']

                # Convert to YOLO
                xc, yc, w, h = convert_to_yolo(x_min, y_min, x_max, y_max, IMG_WIDTH, IMG_HEIGHT)

                # Write to file: Class_ID Center_X Center_Y Width Height
                # We force class ID to 0 (for single-class training)
                out_f.write(f"0 {xc:.6f} {yc:.6f} {w:.6f} {h:.6f}\n")

    print(f"Conversion Complete. Labels saved to: {os.path.abspath(os.path.join(DATA_DIR, 'labels'))}")


if __name__ == "__main__":
    main()