def decide_action(object_name, robot_x, robot_y):

    if object_name == "vase":
        action = "Move to vase"

    elif object_name == "potted plant":
        action = "Move to potted plant"

    else:
        action = "Object not recognized"

    return action


# Test
object_name = "vase"
robot_x = 55.22
robot_y = 82.08

action = decide_action(object_name, robot_x, robot_y)

print("Object:", object_name)
print("Robot X:", robot_x)
print("Robot Y:", robot_y)
print("Action:", action)