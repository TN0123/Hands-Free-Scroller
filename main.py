import cv2
import dlib
import time
import sys
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def captureFaceLandmarks():
    cap = cv2.VideoCapture(0)
    hog_face_detector = dlib.get_frontal_face_detector()
    dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    return cap, hog_face_detector, dlib_facelandmark

def openURL():
    url = input('Paste a URL to use the scroller with: ')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    try:
        browser = webdriver.Chrome(options=options)
        browser.get(url)
        browser.maximize_window()
        browser.implicitly_wait(5)
        return browser
    except Exception as e:
        print("Invalid URL")
        sys.exit(1)

def setup(cap):
    countdown = 5
    starttime = time.time()
    elapsed = 1

    while countdown > 0:
        _, frame = cap.read()
        
        cv2.putText(frame, "Align the bottom of your nose with the line", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.line(frame, (0, 300), (1000, 300), (0, 255, 0), 1) 
        
        currtime = time.time()
        
        if (currtime - starttime) > elapsed:
            print(countdown)
            countdown -= 1
            elapsed += 1
        
        cv2.imshow("Face Landmarks", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

def scroll(cap, hog_face_detector, dlib_facelandmark):
    ogset = False
    ogpos = 0

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = hog_face_detector(gray)

        for face in faces:

            face_landmarks = dlib_facelandmark(gray, face)
            
            x1 = face_landmarks.part(33).x - 10
            x2 = face_landmarks.part(33).x + 10
            y1 = face_landmarks.part(33).y - 20
            y2 = face_landmarks.part(33).y

            if (not ogset):
                ogpos = y2
                ogset = True

            if (y2 > ogpos):
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                pyautogui.scroll(-10)
            elif (y2 < ogpos - 30):
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
                pyautogui.scroll(10)
            else:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)

        cv2.imshow("Face Landmarks", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    browser = openURL()
    cap, hog_face_detector, dlib_facelandmark = captureFaceLandmarks()
    setup(cap)
    scroll(cap, hog_face_detector, dlib_facelandmark)