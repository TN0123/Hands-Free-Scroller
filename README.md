# Hands Free Scroller

A program that allows you to scroll up and down by slightly tilting your head. Navigate through web pages or documents seamlessly by tilting your head slightly in the desired direction!

## Technologies
- OpenCV: Utilized for capturing video frames from the webcam, converting color spaces, and drawing overlays on the video frames for visual feedback.
- dlib: Employed for face detection using a Histogram of Oriented Gradients (HOG) feature and facial landmark detection
- Selenium: Integrated for web automation, enabling the opening of URLs in a browser window
- PyAutoGUI: Used for simulating scroll actions on the system, allowing hands-free scrolling based on head movement
- shape_predictor_68_face_landmarks.dat: Pre-trained facial landmark detection model provided by dlib for accurately locating facial features.

## Installation and Usage
1. Clone the Repository
   ```sh
   https://github.com/TN0123/Hands-Free-Scroller.git
   ```
2. Run the application
   ```
   python main.py
   ```
