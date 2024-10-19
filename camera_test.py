import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import threading

class VideoRecorder:
    def __init__(self, buffer_seconds=5, record_seconds=5, fps=30, width=640, height=480, camera=0):
        self.buffer_seconds = buffer_seconds
        self.width = width
        self.height = height
        self.record_seconds = record_seconds
        self.fps = fps
        self.buffer_frames = buffer_seconds * fps
        self.record_frames = record_seconds * fps
        self.cap = cv2.VideoCapture(camera)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.buffer = []
        self.recording_thread = None
        self.is_recording = False
        self.start_buffering()  # Start buffering immediately

    def start_buffering(self):
        """Start the video buffering in a separate thread."""
        def buffer_video():
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                self.buffer.append(frame)
                if len(self.buffer) > self.buffer_frames:
                    self.buffer.pop(0)  # Keep only the last BUFFER_FRAMES

        self.recording_thread = threading.Thread(target=buffer_video, daemon=True)
        self.recording_thread.start()

    def start_recording(self):
        """Start the recording process."""
        if not self.is_recording:
            self.is_recording = True
            print("Recording started!")

            recording_frames = []
            # Add buffered frames to the recording
            recording_frames.extend(self.buffer)

            # Record for the specified duration
            for _ in range(self.record_frames):
                ret, frame = self.cap.read()
                if not ret:
                    break
                recording_frames.append(frame)

            # Save the recording
            self.save_recording(recording_frames)

            self.is_recording = False

    def save_recording(self, frames):
        """Save the recorded frames to a file."""
        output_filename = 'recorded_video.mp4'  # Change output filename to mp4
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for MP4
        out = cv2.VideoWriter(output_filename, fourcc, self.fps, (self.width, self.height))

        for frame in frames:
            out.write(frame)

        out.release()
        print(f"Recording saved as {output_filename}")

    def release_resources(self):
        """Release the video capture resources."""
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Example usage
    recorder = VideoRecorder(width=1920, height=1080)

    try:
        while True:
            input("Press Enter to start recording...")  # Replace with actual trigger
            recorder.start_recording()
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        recorder.release_resources()
