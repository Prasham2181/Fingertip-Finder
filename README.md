# Fingertip Finder: Real-Time Finger Detection with OpenCV

Fingertip Finder is a real-time computer vision project that detects and counts fingers using a webcam. Leveraging OpenCV's contour detection, convex hulls, and convexity defect analysis, this application provides an interactive and hands-on approach to gesture recognition.

---

## Features
- **Real-Time Detection**: Processes live webcam feed to detect hand gestures.
- **Finger Counting**: Identifies and counts fingers based on convexity defects.
- **Dynamic Visualization**: Highlights detected fingers and convex hulls in the live video feed.

---

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- OpenCV
- NumPy

---

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Prasham2181/Fingertip-Finder.git
   cd Fingertip-Finder

2. Install the required dependencies 
   ```bash
   pip install -r requirements.txt

3. Run the Following command to start the application 
   ```bash
   python fingertip_finder.py



# How It Works
Preprocessing:

    The live video feed is converted to grayscale and blurred to reduce noise.
    Thresholding is applied to create a binary image.

Contour Detection:

    Contours are extracted from the thresholded image, and the largest contour is identified as the hand.

Convex Hull & Convexity Defects:

    The convex hull of the hand is computed.
    Convexity defects (gaps between fingers) are analyzed to count the number of fingers.

Visualization:

    Fingers are highlighted with circles, and detected gestures are displayed as text in the video feed.




# Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.