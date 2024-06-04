from pytube import YouTube

# Paste the URL of the YouTube video you want to download
video_url = "https://www.youtube.com/watch?v=y7GEz67CCRA"

# Initialize a YouTube object with the video URL
yt = YouTube(video_url)

# Get the highest resolution video stream
video_stream = yt.streams.get_highest_resolution()

# Download the video to the current directory
video_stream.download()

print("Video downloaded successfully!")
