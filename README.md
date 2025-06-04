# Real-Time-Facial-Recognition

## Overview

This project implements a face recognition system using Python, [OpenCV](https://opencv.org/), and the [face_recognition](https://github.com/ageitgey/face_recognition) library. The system detects and recognizes faces in images by comparing them to a dataset of known individuals. It is designed for easy extensibility and can be adapted for real-time applications or batch processing.

## Features

- Detects faces in images using OpenCV and face_recognition
- Compares unknown faces to a dataset of known individuals
- Draws bounding boxes and labels on recognized faces
- Configurable tolerance for recognition strictness
- Easily extensible for webcam or video stream input
---

## Project Structure

```
face-recognition-opencv/
├── dataset/           \# Folder containing subfolders for each known person (with images)
├── Test Data/         \# Folder containing images for recognition/testing
├── main.py            \# Main script for running face recognition
├── requirements.txt   \# Python dependencies
└── README.md
```

---

## Getting Started

### 1. Clone the Repository

```

git clone https://github.com/your-profile/face-recognition-opencv.git
cd face-recognition-opencv

```

### 2. Install Dependencies

```

pip install -r requirements.txt

```

### 3. Prepare Your Data

- Place images of known people in `dataset/`, each person in their own folder.
- Place test images in `Test Data/`.

### 4. Run the Script

```

python main.py

```

---

## Example Usage

- The script will process each image in `Test Data/`, detect faces, and display the results with bounding boxes and labels.
- Adjust the `TOLERANCE` variable in `main.py` to change recognition strictness.

---

## References & Resources

- [face_recognition Library Documentation](https://github.com/ageitgey/face_recognition)
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- [Kaggle Datasets for Face Recognition](https://www.kaggle.com/datasets)

---

## Related Projects

- **[General Face Recognition with Machine Learning](https://github.com/ChinmayBabu/Facial-Recognition.git)**  
  Explore a more general ML-based approach to face recognition, including model training and evaluation, under the same GitHub profile.




