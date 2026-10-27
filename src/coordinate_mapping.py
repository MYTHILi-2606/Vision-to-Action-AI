def map_coordinates(x, y, frame_width, frame_height, robot_width, robot_height):

    robot_x = (x / frame_width) * robot_width
    robot_y = (y / frame_height) * robot_height

    return robot_x, robot_y