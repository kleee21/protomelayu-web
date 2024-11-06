import PySimpleGUI as sg
import cv2

image_path = 'face.png'

#modul untuk baca wajah
def detect_faces(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #mengubah dan membaca gambar dari warna gelap
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #ambiil pola wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) #membaca wajah

    for(x,y,h,w) in faces :
        cv2.rectangle(image, (x, y), (x + w, y + h),(255, 0, 0), 2)

    output_path = image_path
    cv2.imwrite(output_path, image)
    return output_path

output_path = detect_faces(image_path)

layout = [
    [sg.Text('Ini adalah contoh citra digital / forensik media file')],
    [sg.Image(output_path)],
    [sg.Button('keluar')]
]


window = sg.Window('deteksi wajah',layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,'keluar') :
        break

window.close()