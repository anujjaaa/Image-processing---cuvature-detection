import cv2
import numpy as np


def save_video(data):
    out = cv2.VideoWriter('post.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (width, height))
    while out.isOpened():
        ret, frame = data.read()
        if ret == True:
            # Write the frame into the file 'output.avi'
            out.write(frame)
            # Display the resulting frame
            cv2.imshow('frame', frame)
            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    out.release()


cap = cv2.VideoCapture(r'D:\anuja\advanced_lane_detection\vipul_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        ima = cv2.resize(frame, (700, 500))
        y = 0
        x = 225
        h = 500
        w = 700
        img_crop = ima[y:y + h, x:x + w]
        # cv2.imshow("image", img_crop)
        im = cv2.resize(img_crop, (700, 500))
        if ret == True:

            #----------------------q
            #set image size to 500x700
            #----------------------

            height = 500
            width = 700
            lower = np.array([85, 90, 88])# rgb without mask images 88 G: 90 B: 85
            upper = np.array([160, 177, 190]) #190 G: 177 B: 160
            shapeMask = cv2.inRange(im, lower, upper)

            #----------------------
            #crop image from top DELTA = 25%
            #----------------------

            top = round(height/4)
            y = 0
            x = 0
            h = height
            w = round(height/2)+30
            # crop1 = shapeMask[y:y + h, x:x + w]
            crop1 = shapeMask[top:top+h, x:x + w]
            # cv2.imshow('crop1', crop1)
            n_white_pix1 = np.sum(crop1 == 255)
            w1 = round(n_white_pix1/2)

            b = round(width / 2) + 70
            # c = height
            d = round(height / 2) + 30
            # crop2 = shapeMask[y:y + h, b:b + d]
            crop2 = shapeMask[top:top + h, b:b + d]
            n_white_pix2 = np.sum(crop2 == 255)
            # print('crop2 has:', n_white_pix2)
            # cv2.imshow('crop2', crop2)
            w2 = round(n_white_pix2/2)

            #----------------------
            #crop the center where delta = 10%
            #----------------------

            m = round(height / 2) + 30
            # n = height
            o = round(width / 5)
            # crop3 = shapeMask[y:y + h, m:m + o]
            crop3 = shapeMask[top:top + h, m:m + o]
            n_white_pix3 = np.sum(crop3 == 255)
            # print('crop3 has:', n_white_pix3)
            # cv2.imshow('crop3', crop3)

            def show_movment(text):
                return cv2.putText(im, text, (10, 450), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2)
            if n_white_pix3 > w1 and n_white_pix3 > w2:
                img_1 = show_movment("keep straight")  # print()
            elif n_white_pix1 > n_white_pix2:
                img_1 = show_movment("turn left")
            else:
                img_1 = show_movment("turn right")
            # image = cv2.putText(im, 'Hello World!', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            image = img_1
            Image = cv2.line(image, (round(width / 2), 0), (round(width / 2), height), (0, 0, 0), 2)
            # image = cv2.line(shapeMask, (round(width/2), 0), (round(width/2), height), (0, 0, 255), 3)
            cv2.imshow("Img", Image)

    else:
        break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    # save_video(Image)
cap.release()
cv2.destroyAllWindows()