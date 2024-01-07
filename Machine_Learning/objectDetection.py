import face_recognition
import cv2
from Machine_Learning.bot.botAPI import *

class object_detect:

    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.known_face_encodings = []
        self.i = 0
        
        self.known_face_names = [
            "Karthik",
            "Harsh"
        ]
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.face_list = {}
        self.process_this_frame = True

        for i in range(0,len(self.known_face_names) - 1):
            l = face_recognition.load_image_file("./pics/"+str(i)+".jpeg")
            print(len(face_recognition.face_encodings(l)))
            j = face_recognition.face_encodings(l)[0]
            self.known_face_encodings.append(j)
        
        for name in self.known_face_names:
            self.face_list[name] = 0

        
    def re_render(self , buffer):
        self.known_face_names.append(buffer)
        print(len(self.known_face_names))
        
        l = face_recognition.load_image_file("./pics/"+ str((len(self.known_face_names) - 1)) +".jpeg")
        j = face_recognition.face_encodings(l)[0]
        self.known_face_encodings.append(j)
        
        for name in self.known_face_names:
            self.face_list[name] = 0
        
    
    def new_friend(self , buffer):
        print("comes here 1")
        ret, frame = self.video_capture.read()
        index = len(self.known_face_names)
        cv2.imwrite("./pics/" + str(index) + ".jpeg" , frame)  
        self.re_render(buffer)
    
    def render_frame(self):
        # Grab a single frame of video
        ret, frame = self.video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if self.process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            face_names = []
            for face_encoding in self.face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_face_names[first_match_index]

                self.face_names.append(name)
                if not name is "Unknown":
                    if self.face_list[name] is 0:
                        self.face_list[name] = 1
                        botResponseReciever("Friend " + name)
                

        self.process_this_frame = not self.process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)


def initializer():
    obj = object_detect()

def render_looper():
    obj.render_frame()
"""
if __name__ == "__main__": 
    obj = object_detect()   
    while True:
        obj.render_frame()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release handle to the webcam
    obj.video_capture.release()
    cv2.destroyAllWindows()
"""
        
        
