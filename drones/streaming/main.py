import cv2
from easytello import tello

maine = True
    # Initialize Tello drone
    my_drone = tello.Tello()

    # Start video stream
    my_drone.streamon()

    # OpenCV window to display stream
    cv2.namedWindow("Tello Camera Feed", cv2.WINDOW_AUTOSIZE)

    try:
        while True:
            # Get frame from Tello
            frame = my_drone.get_frame_read().frame

            # Resize the frame for better viewing (optional)
            frame = cv2.resize(frame, (640, 480))

            # Display the frame
            cv2.imshow("Tello Camera Feed", frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        # Cleanup
        my_drone.streamoff()
        cv2.destroyAllWindows()