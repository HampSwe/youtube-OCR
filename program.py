from ffpyplayer.player import MediaPlayer
from pytube import YouTube
import numpy as np
import math
import cv2


def download_yt_video(url, path, resolution, file_format):

    yt = YouTube(url)
    mp4_files = yt.streams.filter(file_extension=file_format)
    mp4_360p_files = mp4_files.get_by_resolution(resolution)
    mp4_360p_files.download(path)

    return yt.title


def play_video(path):
    cap = cv2.VideoCapture(path)

    if not cap.isOpened(): 
        print("Error opening video stream or file")

    while cap.isOpened():
        returned, frame = cap.read()

        if returned:
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else: 
            break

    cap.release()
    cv2.destroyAllWindows()


def calc_frame(minutes, seconds):
    length = 1183.0
    frames = 35476.0
    ratio = (60.0 * float(minutes) + float(seconds)) / length
    print(math.floor(frames * ratio))



def play_codes(path):
    cap = cv2.VideoCapture(path)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = round(frames / fps)

    timestamps_A = [(2903, 2922), (4752, 4770), (5899, 5918), (7927, 7945), (8430, 8448), (9693, 9711),
    (11952, 11971), (13302, 13321), (16442, 16461), (16672, 16691), (20049, 20067),
    (22180, 22200), (22440, 22459), (25262, 25281), (27256, 27275), (30801, 30820)]
 
    for code_interval in timestamps_A:
        for frame_number in range(code_interval[0], code_interval[1] + 1):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            returned, frame = cap.read()

            if returned:
                cv2.imshow('Frame', frame)
                print(frame_number)

                # Press N on keyboard to go to next frame
                while not ((cv2.waitKey(12) & 0xFF == ord('n'))):
                    pass

    cap.release()
    cv2.destroyAllWindows()


def play_sound(path):

    video=cv2.VideoCapture(path)
    player = MediaPlayer(path)

    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
            

    video.release()
    cv2.destroyAllWindows()


def analyze_video(path):
    cap = cv2.VideoCapture(path)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = round(frames / fps)

    print(frames)
    print(duration)

    frame_number = int(input())

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)



    # Press Q to exit
    while not (cv2.waitKey(25) & 0xFF == ord('q')):

        returned, frame = cap.read()

        if returned:
            cv2.imshow('Frame', frame)
            print(frame_number)

            # Press N on keyboard to go to next frame
            while not ((cv2.waitKey(12) & 0xFF == ord('n'))):
                pass

            # while (cv2.waitKey(12) & 0xFF == ord('n')):
            #     pass
        
        frame_number += 1

    cap.release()
    cv2.destroyAllWindows()


def main():

    url = "https://www.youtube.com/watch?v=NBXcEO6t2Ok"
    folder = "./videos"
    resolution = "360p"
    file_format = "mp4"

    video_name = download_yt_video(url, folder, resolution, file_format)
    #video_name = "I LAUGHED WAY TOO MUCH"

    video_path = folder + "/" + video_name + "." + file_format

    play_video(video_path)

    #analyze_video(video_path)

    #play_codes(video_path)

    #play_sound(video_path)


if __name__ == "__main__":
    main()
