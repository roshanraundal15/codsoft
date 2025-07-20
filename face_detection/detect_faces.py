import cv2
import sys
import numpy as np

# Usage: python detect_faces.py <image_path>
# Example: python detect_faces.py sample.jpg

def non_max_suppression_fast(boxes, overlapThresh=0.3):
    if len(boxes) == 0:
        return []
    boxes = np.array(boxes)
    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")
    pick = []
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,0] + boxes[:,2]
    y2 = boxes[:,1] + boxes[:,3]
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)
    while len(idxs) > 0:
        last = idxs[-1]
        pick.append(last)
        suppress = [last]
        for pos in idxs[:-1]:
            xx1 = max(x1[last], x1[pos])
            yy1 = max(y1[last], y1[pos])
            xx2 = min(x2[last], x2[pos])
            yy2 = min(y2[last], y2[pos])
            w = max(0, xx2 - xx1 + 1)
            h = max(0, yy2 - yy1 + 1)
            overlap = float(w * h) / area[pos]
            if overlap > overlapThresh:
                suppress.append(pos)
        idxs = np.delete(idxs, [np.where(idxs == s)[0][0] for s in suppress])
    return boxes[pick].astype("int")

def main():
    if len(sys.argv) < 2:
        print('Usage: python detect_faces.py <image_path>')
        return
    image_path = sys.argv[1]
    img = cv2.imread(image_path)
    if img is None:
        print(f'Could not load image: {image_path}')
        return
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Increase minNeighbors to reduce false positives
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(60, 60))
    # Apply non-maximum suppression
    faces_nms = non_max_suppression_fast(faces, overlapThresh=0.3)
    print(f'Found {len(faces_nms)} face(s) after NMS')
    for (x, y, w, h) in faces_nms:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Face Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('faces_detected.jpg', img)
    print('Result saved as faces_detected.jpg')

if __name__ == '__main__':
    main()

# To install dependencies:
# pip install opencv-python numpy 