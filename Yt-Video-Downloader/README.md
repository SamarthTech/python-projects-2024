# YouTube Video/Playlist Downloader
This project is a **YouTube Video and Playlist Downloader** that allows users to download individual videos or entire playlists from YouTube. It is implemented using **Python** and **Tkinter** for the graphical user interface (GUI) and **Pytube** for handling video and playlist downloads from YouTube.

## Features
- **Download Individual Videos**: Users can download single videos by pasting the video URL.
- **Download Playlists**: Users can download entire playlists by pasting the playlist URL.
- **OAuth Support**: This project uses YouTube's OAuth for authentication.
- **Error Handling**: Handles exceptions and provides feedback if any issues occur during the download.

## Project Structure
The project mainly consists of the following:
- **Tkinter GUI**: A simple GUI for inputting the video or playlist link and starting the download.
- **Pytube Integration**: Downloads videos or playlists from YouTube using the Pytube library.

## Requirements

- Python 3.x
- Libraries:
  - **Tkinter**: For creating the graphical user interface.
  - **Pytube**: For downloading YouTube videos and playlists.

### Install Required Libraries
You can install the required libraries using `pip`:

```bash
pip install pytube
```

## How to Use

1. **Run the Program**:
   - Execute the Python script to launch the Tkinter window.

   ```bash
   python main.py
   ```

2. **Copy and Paste the YouTube URL**:
   - Open the YouTube video or playlist in your browser.
   - Copy the link.
   - Paste the link into the text input field in the application window.

3. **Download**:
   - After pasting the link, click the **DOWNLOAD** button.
   - The program will automatically detect whether the link is for a single video or a playlist and download accordingly.
   - A message "DOWNLOADED!" will be displayed upon successful download.
   - In case of an error, an error message will be displayed in the GUI.

## Code Overview

1. **Mode Selector**:
   - This function checks the provided URL to determine whether the user is trying to download a single video or a playlist. Based on this, it calls either the `video_downloader` or `playlist_downloader` function.

   ```python
   def mode_selector():
       url = link.get()
       if "watch?v=" in url:
           video_downloader(url)
       elif "playlist?list=" in url:
           playlist_downloader(url)
       else:
           print("Invalid YouTube URL!")
   ```

2. **Video Downloader**:
   - Downloads a single YouTube video from the provided URL.
   - Uses the `pytube.YouTube` class to download the video.
   - Downloads the first stream available for the video.

   ```python
   def video_downloader(url):
       yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
       yt.streams.first().download()
   ```

3. **Playlist Downloader**:
   - Downloads each video in a YouTube playlist from the provided playlist URL.
   - Loops through all the videos in the playlist and calls `video_downloader` for each video.

   ```python
   def playlist_downloader(url):
       py = Playlist(url)
       for video in py.videos:
           video_downloader(video.watch_url)
   ```

4. **Tkinter GUI**:
   - A simple GUI with an input field for the YouTube URL and a button to start the download process.
   - It displays messages in the GUI if a download is successful or if an error occurs.

## Error Handling

- If the link is invalid, the program will print a message "Invalid YouTube URL!".
- If any errors occur during downloading a video or playlist, an error message is displayed in the GUI, showing the exception.

## Future Enhancements

- Option to select download quality.
- Progress bar to display download progress.
- Option to choose download location.

