import face_recognition
import pandas as pd
import pickle
from datetime import datetime

# Load stored encodings and metadata
try:
    with open('student_encodings.pkl', 'rb') as file:
        student_data = pickle.load(file)
except FileNotFoundError:
    print("Error: No student data found. Run the enrollment script first.")
    exit()

# Extract encodings and names
known_face_encodings = [student['encoding'] for student in student_data]
known_face_names = [student['name'] for student in student_data]
known_face_usns = [student['usn'] for student in student_data]

# Load the classroom image
classroom_image = face_recognition.load_image_file('sample1.jpg')
face_locations = face_recognition.face_locations(classroom_image)
face_encodings = face_recognition.face_encodings(classroom_image, face_locations)

# Prepare an attendance list
attendance_list = []

for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name, usn = "Unknown", "N/A"

    if True in matches:
        match_index = matches.index(True)
        name = known_face_names[match_index]
        usn = known_face_usns[match_index]

        # Add the student to the attendance list if not already added
        if usn not in [entry['USN'] for entry in attendance_list]:
            attendance_list.append({'Name': name, 'USN': usn, 'Time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

# Save the attendance to a text file
with open('attendance.txt', 'w') as file:
    file.write("Attendance Record:\n")
    file.write("Name\t\tUSN\t\tTime\n")
    file.write("="*40 + "\n")
    for entry in attendance_list:
        file.write(f"{entry['Name']}\t{entry['USN']}\t{entry['Time']}\n")

print("Attendance has been recorded successfully in 'attendance.txt'.")
