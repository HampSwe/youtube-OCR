from pytube import YouTube
import cv2


# Kolla specifikt try-not-to-laugh? Nja, vet ändå inte om den handlar om pengar... men kanske kan starta om manuellt annars


# Väntar tills 'channel' (i form av en URL till kananels startsida) har lagt upp en ny video
# och returnerar URL:en till den senaste videon
# Väntar 'wait' sekunder mellan varje uppdatering av kanalen
def check_upload_event(channel, wait=1):
    pass

#//*[@id="video-title"]


def main():
    channel_URL = "https://www.youtube.com/user/KSIOlajidebtHD"

    latest_video = check_upload_event(channel_URL)

    print(latest_video)


if __name__ == "__main__":
    main()