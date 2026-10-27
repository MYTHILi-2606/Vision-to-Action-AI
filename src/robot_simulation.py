import time


class RobotSimulator:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.gripper = "OPEN"

    def move_to(self, x, y, z):
        print()
        print("ROBOT MOVING")
        print(f"Target coordinates: X={x:.2f} cm, Y={y:.2f} cm, Z={z:.2f} cm")

        time.sleep(1)

        self.x = x
        self.y = y
        self.z = z

        print("Robot reached target.")

    def open_gripper(self):
        self.gripper = "OPEN"
        print("Gripper: OPEN")
        time.sleep(0.5)

    def close_gripper(self):
        self.gripper = "CLOSED"
        print("Gripper: CLOSED")
        time.sleep(0.5)

    def pick(self, x, y):

        print()
        print("=== PICK ACTION ===")

        # Move above the object
        self.move_to(x, y, 10)

        # Move down toward object
        self.move_to(x, y, 3)

        # Open gripper
        self.open_gripper()

        # Grab object
        self.close_gripper()

        # Lift object
        self.move_to(x, y, 10)

        print("Object PICKED successfully!")

    def place(self, x, y):

        print()
        print("=== PLACE ACTION ===")

        # Move to destination
        self.move_to(x, y, 10)

        # Move down
        self.move_to(x, y, 3)

        # Release object
        self.open_gripper()

        # Lift robot
        self.move_to(x, y, 10)

        print("Object PLACED successfully!")


# --------------------------------
# TEST THE ROBOT
# --------------------------------

robot = RobotSimulator()

print("================================")
print("   VISION TO ACTION AI")
print("   ROBOT SIMULATION")
print("================================")

# Example target position
target_x = 24.38
target_y = 14.17

# Destination position
destination_x = 5
destination_y = 5

print()
print("Target detected!")
print(f"Target position: X={target_x} cm, Y={target_y} cm")

# Pick the object
robot.pick(target_x, target_y)

# Place the object
robot.place(destination_x, destination_y)

print()
print("================================")
print("TASK COMPLETE")
print("Object successfully PICKED and PLACED")
print("================================")