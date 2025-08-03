from mtcnn import MTCNN
import cv2
import os

def detect_and_crop_faces(image_dir='data/images', output_dir='data/faces'):
    detector = MTCNN()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(image_dir):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        img_path = os.path.join(image_dir, filename)
        img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
        results = detector.detect_faces(img)

        for i, res in enumerate(results):
            x, y, w, h = res['box']
            face = img[y:y+h, x:x+w]
            out_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_face{i}.jpg")
            cv2.imwrite(out_path, cv2.cvtColor(face, cv2.COLOR_RGB2BGR))

        print(f"Processed: {filename} — Faces found: {len(results)}")

if __name__ == "__main__":
    detect_and_crop_faces()
