from pytube import *
import datetime


day = datetime.datetime.today().weekday()

#c0 = Channel('https://www.youtube.com/c/GoofyAhhProductions69/videos')
#c1 = Channel('https://www.youtube.com/c/QuandaleDingle1/videos')
#c2 = Channel('https://www.youtube.com/channel/UCFh6XzvSpOb7iG6VrJM0Gww/videos')
#c3 = Channel('https://www.youtube.com/channel/UC7gbitrt8tF0NGtpkiErQZg/videos')
#c4 = Channel('https://www.youtube.com/c/QuandaleDingle1/videos')
#c5 = Channel('https://www.youtube.com/c/GoofyAhhProductions69/videos')
#c6 = Channel('https://www.youtube.com/c/QuandaleDingle1/videos')


c0 = Channel('https://www.youtube.com/channel/UC-kyNoXnicQ-vCdFPoqQXFA/videos')
c1 = Channel('https://www.youtube.com/channel/UC-kyNoXnicQ-vCdFPoqQXFA/videos')
c2 = Channel('https://www.youtube.com/channel/UC-kyNoXnicQ-vCdFPoqQXFA/videos')
c3 = Channel('https://www.youtube.com/channel/UC-kyNoXnicQ-vCdFPoqQXFA/videos')
c4 = Channel('https://www.youtube.com/channel/UC-kyNoXnicQ-vCdFPoqQXFA/videos')
c5 = Channel('https://www.youtube.com/channel/UC-kyNoXnicQ-vCdFPoqQXFA/videos')
c6 = Channel('https://www.youtube.com/channel/UC-kyNoXnicQ-vCdFPoqQXFA/videos')



canale = [c0,c1,c2,c3,c4,c5,c6]




for video in canale[day].videos:
     video.streams.get_highest_resolution().download()
     break




print("fatto")