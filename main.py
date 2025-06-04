import face_recognition
import cv2
import os

# Load known faces
known_faces = []
known_names = []
dataset = "dataset"
tolerance = 0.6
MODEL = "cnn"  # or "hog" for faster CPU-only mode
frame_thickness = 3
font_thickness = 2

print("Loading known faces...")
for name in os.listdir(dataset):
    for filename in os.listdir(f"{dataset}/{name}"):
        image = face_recognition.load_image_file(f"{dataset}/{name}/{filename}")
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_faces.append(encodings[0])
            known_names.append(name)
        else:
            print(f"No face found in {filename}")

# Initialize webcam
video = cv2.VideoCapture(0)

print("Starting webcam face recognition... Press 'q' to quit.")
while True:
    ret, frame = video.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame, model=MODEL)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, tolerance)
        match = None
        if True in results:
            match = known_names[results.index(True)]

            top, right, bottom, left = [v * 4 for v in face_location]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), frame_thickness)
            cv2.rectangle(frame, (left, bottom), (right, bottom + 22), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, match, (left + 10, bottom + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), font_thickness)

    cv2.imshow("Webcam Face Recognition", frame)

    if cv2.waitKey(17) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
