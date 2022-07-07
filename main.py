from pytube import YouTube

YouTube(input("Enter the video URL: ")).streams.filter(file_extension="mp4").get_highest_resolution().download()