from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("test.jpg")

for result in results:
    for box in result.boxes:

        x1, y1, x2, y2 = box.xyxy[0]

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        print("-------------------------")
        print("Object:", class_name)
        print("X1:", float(x1))
        print("Y1:", float(y1))
        print("X2:", float(x2))
        print("Y2:", float(y2))
        print("Center X:", float(center_x))
        print("Center Y:", float(center_y))