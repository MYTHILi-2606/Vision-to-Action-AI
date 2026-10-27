from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera cannot be opened")
    exit()

print("Vision to Action AI started")
print("Looking for a bottle...")
print("Press Q to exit")

while True:

    ret, frame = camera.read()

    if not ret:
        print("Cannot read camera")
        break

    results = model(frame)

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            object_name = model.names[class_id]

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            # AI decision
            if object_name == "bottle" and confidence > 0.5:

                print("TARGET FOUND")
                print("Object:", object_name)
                print("Confidence:", round(confidence, 2))
                print("Position:", round(center_x), round(center_y))
                print("ACTION: PICK")
                print("--------------------")

    annotated_frame = results[0].plot()

    cv2.imshow(
        "Vision to Action AI - Decision",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("System stopped")