import cv2 

def faceRecognition(window_name):
    face_cascade = cv2.CascadeClassifier('haarcascade.xml') 
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    cam = cv2.VideoCapture(0)
    img_counter = 0
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    try:
        while True:
            _, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            roi_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            fullbodies = face_cascade.detectMultiScale(gray, 1.1, 4)
            eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)
            mouths = eye_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (200, 100, 0), 2)
                cv2.putText(img, 'human', (x + 6, y - 6), font, 1.0, (0, 255, 0), 2)
                print("Human detected")    
                
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(img, (ex,ey), (ex+ew,ey+eh), (255, 255, 0), 2)
                    print("Eye detected")
          
            cv2.imshow(window_name, img)
    
            k = cv2.waitKey(30) & 0xff
            if k==27:
                print("Escape key has been hit. Closing...")
                break
            
            elif k%256 == 32:
                print("Saving screenshot...")
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, img)
                print("{} written!".format(img_name))
                img_counter += 1

        cam.release()   
        cv2.destroyAllWindows()

    except(Warning):
        print("An error has occured")    