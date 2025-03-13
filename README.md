# Face Detection using OpenCV

This project implements face detection using OpenCV, allowing users to detect and recognize faces in real time using a webcam or pre-recorded images.

## Features
- Real-time face detection
- Supports multiple faces in a single frame
- Works with both webcam and image inputs
- Uses OpenCV's Haar Cascade and DNN-based models
- Lightweight and efficient

## Technologies Used
- Python
- OpenCV (cv2)
- NumPy
- Haar Cascade Classifier

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- OpenCV library (`cv2`)

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/ritesh8073/Face-detect-OpenCV.git
   cd Face-detect-OpenCV
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the face detection script:
   ```sh
   python face_detect.py
   ```

## How It Works
1. The script captures video input from the webcam.
2. OpenCV's Haar Cascade Classifier processes frames to detect faces.
3. Detected faces are highlighted with bounding boxes.
4. Optionally, users can input an image file for face detection.

## Customization
- Modify detection parameters in `face_detect.py`.
- Experiment with different OpenCV models for improved accuracy.
- Add facial recognition by integrating deep learning models.

## Future Enhancements
- Implement real-time face recognition
- Optimize detection speed using DNN models
- Add GUI for user-friendly interaction

## License
This project is open-source and available for modification and distribution.

## Author
[ritesh8073](https://github.com/ritesh8073)
