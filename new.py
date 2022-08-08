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
    #play_video_sound()

    #twilio_funcs.text("Hejsan")

    #twilio_funcs.call()

    channel_URL = "https://www.youtube.com/channel/UCt-PBc48GgrNP57gZLMXtuw" # min kanal

    latest_video_url = upload_event.check_upload_event(channel_URL)

    


if __name__ == "__main__":
    main()