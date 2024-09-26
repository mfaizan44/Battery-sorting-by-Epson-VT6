def move_to_position(x, y, z):
    # Use Epson RC+ commands to move the robot
    pass

def pick_and_place(x, y, z, box_position):
    move_to_position(x, y, z)
    activate_gripper()
    move_to_position(*box_position)
    deactivate_gripper()
