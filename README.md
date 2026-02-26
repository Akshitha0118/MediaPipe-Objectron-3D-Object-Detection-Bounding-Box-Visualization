
# MediaPipe Objectron – 3D Object Detection & Bounding Box Visualization

This project demonstrates 3D object detection and pose estimation using MediaPipe Objectron.  
It detects real-world objects from an image URL and visualizes 3D bounding boxes and rotation axes using OpenCV and Matplotlib.

---

## 🚀 Project Overview

MediaPipe Objectron enables monocular 3D object detection from a single RGB image.  
In this project, we:

- Load an image from a URL
- Detect 3D objects (Cup model)
- Draw 2D bounding box landmarks
- Visualize 3D rotation axis
- Display results using Matplotlib

---

## 🧠 Technologies Used

- Python
- OpenCV
- MediaPipe (Objectron)
- NumPy
- Matplotlib
- urllib (for image loading)

---


---

## ⚙️ Installation

### 1️⃣ Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate

### 2️⃣ Install Dependencies
pip install mediapipe==0.10.9 opencv-python numpy matplotlib
### ▶️ Run the Project
python object.py

---


## 🎯 Model Used

MediaPipe Objectron supports:

Shoe

Cup

Camera

Laptop

This project uses the Cup model.

## 📸 Output

2D Bounding Box Landmarks

3D Bounding Box

Rotation Axis (Pose Estimation)

## • Implemented monocular 3D object detection and pose estimation using MediaPipe Objectron, visualizing 3D bounding boxes and rotation axes from RGB images.
