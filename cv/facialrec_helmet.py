import face_recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

obama_image = face_recognition.load_image_file("./img/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("./img/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Obama",
    "Joe Biden"
]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    # img1 = rgb_frame

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            print("accept!")
            # img1=frame.copy()
            # face=face_cascade.detectMultiScale(frame)[0]

        # Or instead, use the known face with the smallest distance to the new face
        # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        # best_match_index = np.argmin(face_distances)
        # if matches[best_match_index]:
        #     name = known_face_names[best_match_index]

        # Draw a box around the face
        # cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # img1=frame.copy()
        # face=face_cascade.detectMultiScale(frame)[0]

        f_x, f_y,f_w, f_h = left, top, right, bottom
        padding = 150
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

# print(f_x, f_y,f_w, f_h)
# plt.plot(f_x + (f_w // 2),f_y,'ro')
# plt.imshow(img)

        helmet=plt.imread("img/spacehelmet2.png")
        # print(right-left,top-bottom)
        helmet=cv2.resize(helmet,(int(abs(right-left) * 1.45),int(abs(top-bottom) * 1.45))) # width, height
        # print(f_y, f_x)
        print(helmet.shape) # f_y = height, f_x = width

        for i in range(helmet.shape[0]): # height
            for j in range(helmet.shape[1]): # width
                if (helmet[i,j,3]>0) and f_y + i < frame.shape[0] and f_x + j < frame.shape[1]:
                    # print(f_y+i,f_x+j)
                    frame[f_y+i-int(f_y * 0.2),f_x+j-int(f_x * 0.1), :] = helmet[i,j,:-1]

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()