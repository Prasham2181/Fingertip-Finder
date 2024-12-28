import cv2 as cv
import numpy as np
import math

cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        break

    # Draw ROI
    # cv.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 1)
    # crop_img = img[100:300, 100:300]

    # Preprocessing
    # gray = cv.cvtColor(crop_img, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blurred_ = cv.GaussianBlur(gray, (35, 35), 0)
    _, threshold = cv.threshold(blurred_, 127, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # Contour and convex hull
    contours, _ = cv.findContours(threshold.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    if contours:
        count1 = max(contours, key=lambda x: cv.contourArea(x))
        hull = cv.convexHull(count1, returnPoints=False)
        defects = cv.convexityDefects(count1, hull)

        # Convexity defect analysis
        count_defects = 0
        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(count1[s][0])
                end = tuple(count1[e][0])
                far = tuple(count1[f][0])

                # Calculate distances and angle
                a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                angle = math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * 57

                # Count defects
                if angle <= 90:
                    count_defects += 1
                    # cv.circle(crop_img, far, 5, [0, 0, 255], -1)
                    cv.circle(img, far, 5, [0, 0, 255], -1)

                # cv.line(crop_img, start, end, [0, 255, 0], 2)
                cv.line(img, start, end, [0, 255, 0], 2)

        # Finger count display
        if count_defects == 1:
            cv.putText(img, "2 fingers", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 2:
            cv.putText(img, "3 fingers", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 3:
            cv.putText(img, "4 fingers", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 4:
            cv.putText(img, "5 fingers", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        else:
            cv.putText(img, "1 finger", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

    # Display results

    cv.imshow("Main Window", img)
    cv.imshow("Threshold", threshold)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
