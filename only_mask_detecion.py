import cv2

maskCascade=cv2.CascadeClassifier("Resources/haarcascade_mask.xml") #Eğitilmiş maske tespit eden xml alınır

def maske_tespit(img):  #maskeyi tespit eden fonksiyon
    masks = maskCascade.detectMultiScale(img, 1.1, 4)  #tespit edilen maskeleri masks dizisine atar

    for (x,y,w,h) in masks: #tespit edilen her maskenin x,y konumu ve w,h boyutları için

        cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2) #maskeli yüzün tespit edildiği konuma dikdörtgen çizer
        cv2.putText(img, "Maskeli Yuz",     #tespit edilen konuma maskeli yüz yazar
                    (x, y ), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                    (0, 0, 255), 2)


    cv2.imshow("PENCERE",img) #pencerede gösterilir



cap=cv2.VideoCapture(0)    #webcam referansı alınır
while True:  #her bir anlık görüntü için maske tespiti yapan döngü
    ret,frame=cap.read() #webcamdaki görüntü okunur
    if ret:  #okuma başarılıysa
        frame=cv2.flip(frame,1)  #görüntünün ayna şeklinde gözükmesi için x ekseninin tersi yönde çevrilir
        maske_tespit(frame)  #maske varlığını sorgulaması için fonksiyona verilir


    cv2.waitKey(1)

