import face_recognition
import pickle
from datetime import datetime

# Load stored encodings and metadata
try:
    with open('student_encodings.pkl', 'rb') as file:
        student_data = pickle.load(file)
except FileNotFoundError:
    print("Error: No student data found. Run the enrollment script first.")
    exit()

# Extract encodings, names, and USNs
known_face_encodings = [student['encodings'] for student in student_data]
known_face_names = [student['name'] for student in student_data]
known_face_usns = [student['usn'] for student in student_data]

# Flatten the list of encodings for comparison
flattened_encodings = [encoding for encodings in known_face_encodings for encoding in encodings]

# Ask user for the image path to be used for attendance detection
image_path = input("Enter the path to the classroom image (e.g., 'classroom.jpg'): ")

# Load the classroom image
try:
    classroom_image = face_recognition.load_image_file(image_path)
except Exception as e:
    print(f"Error loading the image: {e}")
    exit()

# Detect face locations and encodings in the classroom image
face_locations = face_recognition.face_locations(classroom_image)
face_encodings = face_recognition.face_encodings(classroom_image, face_locations)

# Prepare an attendance list
attendance_list = []

# Compare each detected face with the known faces
for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(flattened_encodings, face_encoding)
    name, usn = "Unknown", "N/A"

    if True in matches:
        match_index = matches.index(True)
        # Find the student who has this encoding
        student_index = 0
        while match_index >= len(known_face_encodings[student_index]):
            match_index -= len(known_face_encodings[student_index])
            student_index += 1
        name = known_face_names[student_index]
        usn = known_face_usns[student_index]

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
