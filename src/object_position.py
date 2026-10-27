from ultralytics import YOLO
from coordinate_mapping import map_coordinates

model = YOLO("yolo11n.pt")

image_path = "test.jpg"

results = model(image_path)

robot_width = 100
robot_height = 100

for result in results:

    frame_height, frame_width = result.orig_shape

    for box in result.boxes:

        x1, y1, x2, y2 = box.xyxy[0]

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        robot_x, robot_y = map_coordinates(
            float(center_x),
            float(center_y),
            frame_width,
            frame_height,
            robot_width,
            robot_height
        )

        print("-----------------------------")
        print("Object:", class_name)
        print("Camera X:", float(center_x))
        print("Camera Y:", float(center_y))
        print("Robot X:", robot_x)
        print("Robot Y:", robot_y)