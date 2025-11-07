# Drowsiness Eye Detection

This project is a real-time drowsiness detection system using computer vision and machine learning. It utilizes a Flask web application to stream video from a webcam and detect if the user's eyes are closed, potentially indicating drowsiness. An alert sound is played when drowsiness is detected.

## Prerequisites

- Python 3.7 or higher
- Webcam (for real-time detection)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd drowsiness-eye-detection
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage


1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0
.0.1:5000/` to access the application.

3. The application will start capturing video from your webcam and display it on the webpage. If drowsiness is detected (eyes closed for a certain period), an alert sound will play.

## Project Structure

- `app.py`: Main Flask application file.
- `prepare_data.py`: Script for preparing training data.
- `train_model.py`: Script for training the eye detection model.
- `realtime_detection.py`: Script for real-time detection (if applicable).
- `utils/detector.py`: Utility functions for drowsiness detection.
- `model/eye_model.h5`: Pre-trained TensorFlow model for eye state classification.
- `templates/index.html`: HTML template for the web interface.
- `static/`: Directory containing CSS and JavaScript files.
- `music/music.wav`: Alert sound file.
- `mrlEyes_2018_01/`: Dataset directory (extracted from the zip file).

## Notes

- The model (`eye_model.h5`) and data (`X.npy`, `y.npy`) are already included in the repository.
- If you need to retrain the model, use `prepare_data.py` and `train_model.py`.
- Ensure your webcam is accessible and not in use by other applications.

