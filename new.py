from numpy import number
import twilio_funcs
import program as youtube_funcs
import upload_event


def play_video_sound():

    url = "https://www.youtube.com/watch?v=NBXcEO6t2Ok"

    folder = "./videos"
    resolution = "1080p"
    file_format = "mp4"

    video_name = youtube_funcs.download_yt_video(url, folder, resolution, file_format)
    video_name = youtube_funcs.filter_name(video_name)
    video_path = folder + "/" + video_name + "." + file_format

    youtube_funcs.play_sound(video_path)



def main():
    workers = {"Hampus": "+46708792939", "Jonte": "+46724499546"}

    channel_URL = "https://www.youtube.com/channel/UCt-PBc48GgrNP57gZLMXtuw" # min kanal

    #latest_video_url = upload_event.check_upload_event(channel_URL, pause=3)

    msg = "Hej schonne \n whats up"

    for name, number in workers.items():
        twilio_funcs.text(msg, number=number)
        print("Sent text message to " + name)


    #play_video_sound()
    #twilio_funcs.text("Hejsan")
    #twilio_funcs.call()




if __name__ == "__main__":
    main()