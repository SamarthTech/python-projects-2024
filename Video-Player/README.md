# Python Video Player

A lightweight, feature-rich video player built with Python using OpenCV and Tkinter. This application provides a clean graphical user interface for playing various video formats with essential playback controls.


## Features

- 🎥 Support for multiple video formats (MP4, AVI, MKV, MOV)
- ⏯️ Basic playback controls (Play, Pause, Stop)
- 🎚️ Progress bar with seeking capability
- ⚡ Variable playback speed (0.25x to 2x)
- ⏲️ Real-time duration display
- 🖼️ Automatic video resizing while maintaining aspect ratio
- 🧵 Threaded playback for smooth performance
- 🎯 User-friendly GUI built with Tkinter

## Prerequisites

Before running the application, ensure you have Python 3.6 or higher installed on your system. You can check your Python version by running:

```bash
python --version
```

## Using the player:
   - Click the "Open" button to choose a video file
   - Use the Play/Pause button to control playback
   - Click Stop to reset the video to the beginning
   - Drag the progress bar to seek to different parts of the video
   - Adjust the playback speed using the speed slider (0.25x to 2x)
   - The time display shows current position and total duration

## Controls

| Control | Action |
|---------|--------|
| Open | Opens file dialog to select a video file |
| Play/Pause | Toggles between playing and pausing the video |
| Stop | Stops playback and resets to beginning |
| Progress Bar | Seeks to different positions in the video |
| Speed Slider | Adjusts playback speed between 0.25x and 2x |

## File Support

The video player supports the following formats:
- MP4 (.mp4)
- AVI (.avi)
- Matroska (.mkv)
- QuickTime (.mov)
- Other formats supported by OpenCV

## Project Structure

```
python-video-player/
│
├── main.py                # Main application file
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── venv/                 # Virtual environment (after setup)
```

## Technical Details

The application is built using:
- **Tkinter**: For the graphical user interface
- **OpenCV**: For video processing and playback
- **PIL (Pillow)**: For image processing and display
- **Threading**: For smooth video playback
- **Time**: For playback control and time display

## Performance Considerations

- The application uses threading to ensure smooth playback
- Video frames are automatically resized to match the window size
- Memory usage is optimized by processing one frame at a time
- Playback speed is controlled through frame delay timing

## Troubleshooting

Common issues and solutions:

1. **Video won't play**
   - Ensure the video file format is supported
   - Check if OpenCV is properly installed
   - Verify the video file isn't corrupted

2. **Choppy playback**
   - Try reducing the playback speed
   - Close other resource-intensive applications
   - Check if your system meets the minimum requirements

3. **No video display**
   - Ensure the video file path is correct
   - Check if the video file is accessible
   - Verify that PIL is properly installed


## Future Improvements

Planned features and improvements:

- [ ] Add support for playlists
- [ ] Implement frame-by-frame navigation
- [ ] Add keyboard shortcuts
- [ ] Include audio volume control
- [ ] Add screenshot capability
- [ ] Implement subtitle support
- [ ] Add more video filters and effects
- [ ] Create a portable executable version

---
