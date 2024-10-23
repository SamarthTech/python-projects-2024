import tkinter as tk
from tkinter import filedialog, ttk
import cv2
from PIL import Image, ImageTk
import threading
import time

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Video Player")
        
        # Video variables
        self.cap = None
        self.is_playing = False
        self.total_frames = 0
        self.current_frame = 0
        self.play_thread = None
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Create video frame
        self.video_frame = ttk.Frame(self.root)
        self.video_frame.pack(expand=True, fill='both')
        
        # Create video label
        self.video_label = ttk.Label(self.video_frame)
        self.video_label.pack(expand=True, fill='both')
        
        # Create control frame
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(fill='x', padx=5, pady=5)
        
        # Create progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Scale(
            self.control_frame,
            from_=0,
            to=100,
            orient='horizontal',
            variable=self.progress_var,
            command=self.seek
        )
        self.progress_bar.pack(fill='x', padx=10, pady=5)
        
        # Create buttons frame
        self.buttons_frame = ttk.Frame(self.control_frame)
        self.buttons_frame.pack(fill='x')
        
        # Create buttons
        ttk.Button(
            self.buttons_frame,
            text="Open",
            command=self.open_file
        ).pack(side='left', padx=5)
        
        self.play_pause_button = ttk.Button(
            self.buttons_frame,
            text="Play",
            command=self.play_pause
        )
        self.play_pause_button.pack(side='left', padx=5)
        
        ttk.Button(
            self.buttons_frame,
            text="Stop",
            command=self.stop
        ).pack(side='left', padx=5)
        
        # Create speed control
        self.speed_var = tk.DoubleVar(value=1.0)
        ttk.Label(
            self.buttons_frame,
            text="Speed:"
        ).pack(side='right', padx=2)
        self.speed_scale = ttk.Scale(
            self.buttons_frame,
            from_=0.25,
            to=2.0,
            orient='horizontal',
            variable=self.speed_var,
            length=100
        )
        self.speed_scale.pack(side='right', padx=5)
        
        # Display time
        self.time_label = ttk.Label(self.buttons_frame, text="0:00 / 0:00")
        self.time_label.pack(side='right', padx=10)
        
    def open_file(self):
        """Open a file dialog to choose a video file"""
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Video files", "*.mp4 *.avi *.mkv *.mov"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.load_video(file_path)
    
    def load_video(self, file_path):
        """Load the selected video file"""
        if self.cap is not None:
            self.stop()
            
        self.cap = cv2.VideoCapture(file_path)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.duration = self.total_frames / self.fps
        
        # Read and display first frame
        ret, frame = self.cap.read()
        if ret:
            self.display_frame(frame)
            self.update_time_label()
    
    def play_pause(self):
        """Toggle between play and pause"""
        if self.cap is None:
            return
            
        if self.is_playing:
            self.is_playing = False
            self.play_pause_button.config(text="Play")
        else:
            self.is_playing = True
            self.play_pause_button.config(text="Pause")
            if self.play_thread is None or not self.play_thread.is_alive():
                self.play_thread = threading.Thread(target=self.play_video)
                self.play_thread.daemon = True
                self.play_thread.start()
    
    def play_video(self):
        """Play the video in a separate thread"""
        while self.is_playing and self.cap is not None:
            ret, frame = self.cap.read()
            if not ret:
                self.stop()
                break
                
            self.current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            self.display_frame(frame)
            self.update_progress()
            self.update_time_label()
            
            # Control playback speed
            delay = 1 / (self.fps * self.speed_var.get())
            time.sleep(delay)
    
    def display_frame(self, frame):
        """Convert and display a frame"""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Resize frame to fit the window while maintaining aspect ratio
        window_width = self.video_frame.winfo_width()
        window_height = self.video_frame.winfo_height()
        
        if window_width > 1 and window_height > 1:  # Only resize if window dimensions are valid
            frame_height, frame_width = frame_rgb.shape[:2]
            aspect_ratio = frame_width / frame_height
            
            if window_width / window_height > aspect_ratio:
                new_height = window_height
                new_width = int(window_height * aspect_ratio)
            else:
                new_width = window_width
                new_height = int(window_width / aspect_ratio)
                
            frame_rgb = cv2.resize(frame_rgb, (new_width, new_height))
        
        image = Image.fromarray(frame_rgb)
        photo = ImageTk.PhotoImage(image=image)
        self.video_label.configure(image=photo)
        self.video_label.image = photo
    
    def stop(self):
        """Stop the video playback"""
        self.is_playing = False
        if self.cap is not None:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()
            if ret:
                self.display_frame(frame)
        self.current_frame = 0
        self.progress_var.set(0)
        self.play_pause_button.config(text="Play")
        self.update_time_label()
    
    def seek(self, value):
        """Seek to a specific position in the video"""
        if self.cap is None:
            return
            
        frame_no = int((float(value) / 100) * self.total_frames)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = self.cap.read()
        if ret:
            self.display_frame(frame)
            self.current_frame = frame_no
            self.update_time_label()
    
    def update_progress(self):
        """Update the progress bar"""
        if self.total_frames > 0:
            progress = (self.current_frame / self.total_frames) * 100
            self.progress_var.set(progress)
    
    def update_time_label(self):
        """Update the time display"""
        current_time = self.current_frame / self.fps
        total_time = self.total_frames / self.fps
        
        current_time_str = time.strftime('%M:%S', time.gmtime(current_time))
        total_time_str = time.strftime('%M:%S', time.gmtime(total_time))
        
        self.time_label.config(text=f"{current_time_str} / {total_time_str}")

def main():
    root = tk.Tk()
    root.geometry("800x600")
    app = VideoPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()