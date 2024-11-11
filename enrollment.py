import face_recognition
import cv2
import numpy as np
import pickle  # For storing encodings and data
from matplotlib import pyplot as plt

# Capture a live photo from the camera
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not access the camera.")
else:
    ret, frame = video_capture.read()
    if ret:
        # Display the captured frame using matplotlib as an alternative to cv2.imshow
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.imshow(frame_rgb)
        plt.title('Capture Photo')
        plt.show()

        # Encode the face in the captured frame
        face_encodings = face_recognition.face_encodings(frame)
        if face_encodings:
            face_encoding = face_encodings[0]  # Assuming one student per photo

            # Input student details
            name = input("Enter the student's name: ")
            usn = input("Enter the student's USN: ")

            # Load existing data or create a new list
            try:
                with open('student_encodings.pkl', 'rb') as file:
                    student_data = pickle.load(file)
            except FileNotFoundError:
                student_data = []

            # Append the new student's encoding and details
            student_data.append({
                'name': name,
                'usn': usn,
                'encoding': face_encoding
            })

            # Save the updated data back to the file
            with open('student_encodings.pkl', 'wb') as file:
                pickle.dump(student_data, file)

            print("Student data has been saved successfully.")
        else:
            print("No face detected. Please try again.")
    else:
        print("Error: Could not read a frame from the camera.")

video_capture.release()
