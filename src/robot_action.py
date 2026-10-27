def move_robot(robot_x, robot_y):

    print("Robot action started")

    print("Moving to X:", robot_x)
    print("Moving to Y:", robot_y)

    print("Robot reached the target")

    return "Target reached"


# Test
robot_x = 55.22
robot_y = 82.08

result = move_robot(robot_x, robot_y)

print("Status:", result)