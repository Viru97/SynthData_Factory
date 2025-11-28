# 🏭 SynthData-Factory: Industrial Sim2Real Pipeline

[![Isaac Sim](https://img.shields.io/badge/Sim-NVIDIA%20Isaac%20Sim-green)](https://developer.nvidia.com/isaac-sim)
[![Python](https://img.shields.io/badge/Code-Python%203.10-blue)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/Data-YOLOv8%20Format-orange)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

> **A robust Synthetic Data Generation (SDG) pipeline for robotic perception, capable of generating perfectly labeled training data with domain randomization and negative mining.**

---

## 📸 The Pipeline in Action
![gif alt](https://github.com/Viru97/SynthData_Factory/blob/319f771024aaaa311c05d6000bfeb24f2e20f59d/ezgif.com-optimize.gif)

## 🚀 Project Overview
Acquiring labeled data for industrial environments is expensive and slow. This project implements a **Digital Twin** workflow to generate infinite training data for Object Detection models.

It addresses the **Sim2Real gap** by utilizing:
1.  **Photorealistic Assets:** USD-based warehouse environments and textured target objects.
2.  **Domain Randomization:** Varying lighting, pose, and camera angles to prevent overfitting.
3.  **Negative Mining (Distractors):** Intentionally introducing "trash" objects (pallets) without labels to teach the AI what *not* to detect.

## ✨ Key Engineering Features

### 1. The "Virtual Director" (`scene_generator.py`)
* **Asset Loader:** Automatically locates NVIDIA Nucleus assets or falls back to S3 URLs.
* **Chaos Engine:** Randomizes 3D pose, light intensity/color, and camera jitter per frame.
* **Semantic Segmentation:** Assigns unique IDs to specific classes for auto-labeling.

### 2. Smart Post-Processing (`smart_converter.py`)
* **Format Agnostic:** Converts raw binary NumPy (`.npy`) data from Isaac Sim into normalized YOLOv8 text files.
* **Auto-ID Discovery:** Automatically parses JSON metadata to find the specific Semantic ID of the target (e.g., `industrial_box`), ensuring robust mapping even if asset IDs change.
* **Logic Filter:** Implements a strict filter to ignore distractor objects (pallets/shelves), ensuring high-quality "clean" labels.

## 🛠️ Tech Stack
* **Simulation Engine:** NVIDIA Isaac Sim (Replicator API)
* **Scripting:** Python 3.10
* **Data Format:** NumPy (Binary) -> YOLOv8 (Txt)
* **Assets:** Universal Scene Description (USD)

## 📂 Repository Structure
```text
SynthData-Factory/
├── src/
│   ├── scene_generator.py   # Main simulation script (The "Director")
│   ├── smart_converter.py   # Parsing logic & YOLO conversion (The "Translator")
│   └── visualize.py         # Verification tool (The "Quality Control")
├── output/                  # Generated Dataset (Images + Labels)
└── README.md

⚙️ How to Run

1. Generate the Simulation

Run src/scene_generator.py inside the NVIDIA Isaac Sim Script Editor.

    Input: 003_cracker_box.usd (Target), warehouse.usd (Env), Pallet_B1.usd (Distractor).

    Output: A folder of RGB images and raw .npy bounding box data.

2. Process the Data

Run the converter from your terminal to generate YOLO labels:

python src/smart_converter.py

Logic: Scans metadata -> Finds industrial_box ID -> Filters noise -> Normalizes coordinates.

3. Verify Quality

Run the visualizer to inspect the bounding boxes:

python src/visualize.py

```
📊 Results

![image alt](https://github.com/Viru97/SynthData_Factory/blob/3ff428182fed1675ccebec46b3dcf586098ed4f6/debug_vis_rgb_0000.png)
