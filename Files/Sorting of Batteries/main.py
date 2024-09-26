import camera
import epson_controller as robot
import gripper
import utils
from ultralytics import YOLO

# Load YOLO model
model = YOLO('best.pt')

# Define box positions (example coordinates)
box_positions = {
    'AA': (100, 200, 0),
    '9V': (200, 300, 0),
    'D': (300, 400, 0),
}

def main():
    gripper.setup_gripper()
    
    for frame in camera.get_frame():
        results = model(frame)
        frame = utils.draw_bounding_boxes(frame, results, model.names)
        cv2.imshow('Battery Detection', frame)
        
        frame_height, frame_width, _ = frame.shape
        for box in results.xyxy[0].cpu().numpy():
            x1, y1, x2, y2, conf, cls = box
            battery_type = model.names[int(cls)]
            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            robot_x, robot_y, robot_z = utils.convert_to_robot_coords(x_center, y_center, frame_width, frame_height)
            robot.pick_and_place(robot_x, robot_y, robot_z, box_positions[battery_type])

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    gripper.cleanup_gripper()

if __name__ == '__main__':
    main()
