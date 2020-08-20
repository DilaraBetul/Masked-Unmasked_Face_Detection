import cv2

maskCascade=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml") #Eğitilmiş yüz tespit eden xml alınır

def yuz_tespit(img):  #yüzü tespit eden fonksiyon
    faces = maskCascade.detectMultiScale(img, 1.1, 4)  #tespit edilen yüzleri faces dizisine atar

    for (x,y,w,h) in faces: #tespit edilen her yüzün x,y konumu ve w,h boyutları için

        cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2) #ma yüzün tespit edildiği konuma dikdörtgen çizer
        cv2.putText(img, "Yuz",     #tespit edilen konuma  yüz yazar
                    (x, y ), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                    (0, 0, 255), 2)


    cv2.imshow("PENCERE",img) #pencerede gösterilir



cap=cv2.VideoCapture(0)    #webcam referansı alınır
while True:  #her bir anlık görüntü için maske tespiti yapan döngü
    ret,frame=cap.read() #webcamdaki görüntü okunur
    if ret:  #okuma başarılıysa
        frame=cv2.flip(frame,1)  #görüntünün ayna şeklinde gözükmesi için x ekseninin tersi yönde çevrilir
        yuz_tespit(frame)  #maske varlığını sorgulaması için fonksiyona verilir


    cv2.waitKey(1)

