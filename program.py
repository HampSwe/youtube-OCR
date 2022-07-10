from multiprocessing.spawn import old_main_modules
from ffpyplayer.player import MediaPlayer
from pytube import YouTube
import image_analysis
import upload_event
import numpy as np
import math
import cv2
import time


def download_yt_video(url, path, resolution, file_format):

    old = False

    if old:
        yt = YouTube(url)
        mp4_files = yt.streams.filter(file_extension=file_format)   
        mp4_360p_files = mp4_files.get_by_resolution(resolution)
        mp4_360p_files.download(path)
        return yt.title
    else:
        # yt = YouTube(url)
        # mp4_files = yt.streams.get_highest_resolution()
        # mp4_files.download(path)
        # return yt.title

        yt = YouTube(url)

        # for i in yt.streams:
        #     print(i.resolution)

        mp4_files = yt.streams.filter(file_extension=file_format, res=resolution)   
        #mp4_360p_files = mp4_files.get_by_resolution(resolution)
        mp4_files.first().download(path)
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
    # 650
    #length = 1183.0
    #frames = 35476.0

    #500
    length = 788
    frames = 47252


    ratio = (60.0 * float(minutes) + float(seconds)) / length
    print(math.floor(frames * ratio))



def play_codes(path):
    multiplier = 0.5

    cap = cv2.VideoCapture(path)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = round(frames / fps)

    timestamps_650 = [(2903, 2922), (4752, 4770), (5899, 5918), (7927, 7945), (8430, 8448), (9693, 9711),
    (11952, 11971), (13302, 13321), (16442, 16461), (16672, 16691), (20049, 20067),
    (22180, 22200), (22440, 22459), (25262, 25281), (27256, 27275), (30801, 30820)]

    timestamps_500 = [(13183, 13275), (15233, 15325), (16979, 17071), (18707, 18797), (20695, 20785),
    (27618, 27709), (37476, 37566), (41171, 41262), (44290, 44380)]


    timestamps = timestamps_500
 
    for code_interval in timestamps:
        for frame_number in range(math.ceil(code_interval[0] * multiplier), math.floor(code_interval[1] * multiplier) + 1):
            cap.set(cv2.CAP_PROP_POS_FRAMES, round(frame_number))
            returned, frame = cap.read()

            if returned:
                cv2.imshow('Frame', frame)
                print(round(frame_number))

                # Press N on keyboard to go to next frame
                while not ((cv2.waitKey(12) & 0xFF == ord('n'))):
                    pass

    cap.release()
    cv2.destroyAllWindows()



def analyze_codes(path):
    cap = cv2.VideoCapture(path)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = round(frames / fps)

    timestamps_650 = [(2903, 2922), (4752, 4770), (5899, 5918), (7927, 7945), (8430, 8448), (9693, 9711),
    (11952, 11971), (13302, 13321), (16442, 16461), (16672, 16691), (20049, 20067),
    (22180, 22200), (22440, 22459), (25262, 25281), (27256, 27275), (30801, 30820)]

    timestamps_500 = [(13183, 13275), (15233, 15325), (16979, 17071), (18707, 18797), (20695, 20785),
    (27618, 27709), (37476, 37566), (41171, 41262), (44290, 44380)]

    timestamps = timestamps_500
 
    for code_interval in timestamps:
        for frame_number in range(code_interval[0], code_interval[1] + 1):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            returned, frame = cap.read()

            if returned:
                #cv2.imshow('Frame', frame)
                #print(frame_number)

                image_analysis.analyze_frame(frame)

                # # Press N on keyboard to go to next frame
                # while not ((cv2.waitKey(12) & 0xFF == ord('n'))):
                #     pass

                
                input()



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



def rotate_image_crop(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result


def rotate_image(mat, angle):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """

    height, width = mat.shape[:2] # image shape has 3 dimensions
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat



def analyze_codes_rotated(path):
    cap = cv2.VideoCapture(path)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = round(frames / fps)

    timestamps_650 = [(2903, 2922), (4752, 4770), (5899, 5918), (7927, 7945), (8430, 8448), (9693, 9711),
    (11952, 11971), (13302, 13321), (16442, 16461), (16672, 16691), (20049, 20067),
    (22180, 22200), (22440, 22459), (25262, 25281), (27256, 27275), (30801, 30820)]

    timestamps_500 = [(13183, 13275), (15233, 15325), (16979, 17071), (18707, 18797), (20695, 20785),
    (27618, 27709), (37476, 37566), (41171, 41262), (44290, 44380)]

    timestamps_selected = [(11952, 11971)]

    timestamps = timestamps_selected
 
    for code_interval in timestamps:
        for frame_number in range(code_interval[0], code_interval[1] + 1):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            returned, frame = cap.read()

            if returned:
                #cv2.imshow('Frame', frame)
                #print(frame_number)

                #rotated_frame = rotate_image(frame, -25)
                image_analysis.analyze_frame(frame, angle=-25)
                print(frame_number)

                # Press N on keyboard to go to next frame
                while not ((cv2.waitKey(12) & 0xFF == ord('n'))):
                    pass

    cap.release()
    cv2.destroyAllWindows()

def analyze_time_codes(path, multiplier=1):
    t1 = time.time()

    #multiplier = 0.5

    cap = cv2.VideoCapture(path)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = round(frames / fps)

    timestamps_650 = [(2903, 2922), (4752, 4770), (5899, 5918), (7927, 7945), (8430, 8448), (9693, 9711),
    (11952, 11971), (13302, 13321), (16442, 16461), (16672, 16691), (20049, 20067),
    (22180, 22200), (22440, 22459), (25262, 25281), (27256, 27275), (30801, 30820)]

    timestamps_500 = [(13183, 13275), (15233, 15325), (16979, 17071), (18707, 18797), (20695, 20785),
    (27618, 27709), (37476, 37566), (41171, 41262), (44290, 44380)]

    selected_timestamp = [timestamps_650[4]]

    timestamps = selected_timestamp
 
    for code_interval in timestamps:
        for frame_number in range(math.ceil(code_interval[0] * multiplier), math.floor(code_interval[1] * multiplier) + 1):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            returned, frame = cap.read()

            if returned:
                #print(frame_number)'
                #cv2.imshow('Frame', frame)

                image_analysis.analyze_frame(frame)

                # # Press N on keyboard to go to next frame
                while not ((cv2.waitKey(12) & 0xFF == ord('n'))):
                    pass

    total_time = time.time() - t1
    print(total_time)

    cap.release()
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

def filter_name(name):
    tmp = ""
    filter = ["$", ","]

    for i in name:
        if not i in filter:
            tmp += i
    
    return tmp


def main():

    url_650 = "https://www.youtube.com/watch?v=NBXcEO6t2Ok" #vriden text + stjärna. vit text
    url_500 = "https://www.youtube.com/watch?v=WxHRKCgCtDM" #svart text, enkel
    url_400 = "https://www.youtube.com/watch?v=Brje__8Xvmk&list=PL6_iWvoCGAJm--GrgiAHz7H6oLQ0LM8dE&index=5" #svart text, enkel
    url_broke = "https://www.youtube.com/watch?v=fNQe3ClfujU&list=PL6_iWvoCGAJm--GrgiAHz7H6oLQ0LM8dE&index=9" #vit text, enkel
    url_300 = "https://www.youtube.com/watch?v=BeJ1rnFJHfI&list=PL6_iWvoCGAJm--GrgiAHz7H6oLQ0LM8dE&index=11" #typ omöjliga att läsa av. DOCK: konstig bugg, kan ej ladda ner. tror svart text
    url_smile = "https://www.youtube.com/watch?v=4_TyhOeTWyQ&list=PL6_iWvoCGAJm--GrgiAHz7H6oLQ0LM8dE&index=14" #claim code först
    url_first = "https://www.youtube.com/watch?v=L69Wt-5d8rE&list=PL6_iWvoCGAJm--GrgiAHz7H6oLQ0LM8dE&index=16" #claim code först

    url = url_650
    folder = "./videos"
    resolution = "1080p"
    file_format = "mp4"

    video_name = download_yt_video(url, folder, resolution, file_format)
    video_name = filter_name(video_name)

    #video_name = "I LAUGHED WAY TOO MUCH"
    #video_name = "500 EVERYTIME I LAUGH"

    video_path = folder + "/" + video_name + "." + file_format

    #play_video(video_path)

    #analyze_video(video_path)

    #play_codes(video_path)

    #play_sound(video_path)

    #analyze_codes(video_path)

    #analyze_codes_rotated(video_path)

    analyze_time_codes(video_path, multiplier=2)


if __name__ == "__main__":
    main()