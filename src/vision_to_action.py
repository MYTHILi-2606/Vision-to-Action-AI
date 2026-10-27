from ultralytics import YOLO
import cv2

# -----------------------------
# SETTINGS
# -----------------------------

WIDTH = 640
HEIGHT = 480

TABLE_WIDTH_CM = 30
TABLE_HEIGHT_CM = 20

# Load YOLO
model = YOLO("yolo11n.pt")

# Open camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera cannot be opened")
    exit()

print("Vision to Action AI")
print("--------------------")
print("Looking for a bottle...")
print("Press Q to exit")


# -----------------------------
# PIXEL TO REAL-WORLD MAPPING
# -----------------------------

def pixel_to_cm(pixel_x, pixel_y):

    real_x = (pixel_x / WIDTH) * TABLE_WIDTH_CM
    real_y = (pixel_y / HEIGHT) * TABLE_HEIGHT_CM

    return real_x, real_y


# -----------------------------
# MAIN LOOP
# -----------------------------

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

            # -----------------------------
            # AI DECISION
            # -----------------------------

            if object_name == "bottle" and confidence > 0.5:

                # Convert pixels to centimetres
                robot_x, robot_y = pixel_to_cm(
                    center_x,
                    center_y
                )

                print("TARGET FOUND")
                print("Object:", object_name)
                print("Confidence:", round(confidence, 2))

                print(
                    "Pixel position:",
                    round(center_x),
                    round(center_y)
                )

                print(
                    "Robot position:",
                    round(robot_x, 2),
                    "cm,",
                    round(robot_y, 2),
                    "cm"
                )

                print("ACTION: PICK")
                print("--------------------")

    # Draw detections
    annotated_frame = results[0].plot()

    cv2.imshow(
        "Vision to Action AI",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -----------------------------
# CLEANUP
# -----------------------------

camera.release()
cv2.destroyAllWindows()

print("System stopped")