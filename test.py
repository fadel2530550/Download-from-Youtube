from pytube import Playlist
from pytube import YouTube


def playlist(link,str):
    
    """if(len(link) or len(str)):
        print('=========ERROR======================')
        print("the link or folder name is empty!!!")
        print('====================================')
    else:"""
    plist = Playlist(link)  
    for video in plist.videos:
        print(video.title)
        video.streams.get_highest_resolution().download(output_path='/py/testpy/'+str)
        print("Done!!")

def links(link,str):
    if(link=='' or str==''):
        print('=========ERROR======================')
        print("the link or folder name is empty!!!")
        print('====================================')
    else:
        v=YouTube(link)
        print(v.title)
        v.streams.get_highest_resolution().download(output_path="/py/testpy/"+str)
        print("Done")

while(True):
    print('**********************************')
    print('Do you Download playlist or link:')
    print('1-Play List videos.')
    print('2-Link video Views.')
    print('0-Exit.')
    inputs = input("Enter number:")

    if(inputs =='1'):
        print('**********************************')
        pl=input('Enter Playlist link:')
        linkplay=input('Enter file name:')
        playlist(pl,linkplay)
    elif(inputs=='2') :
        print('**********************************')
        link=input('Enter link:')
        fol=input('Enter file name:')
        links(link,fol)
    elif(inputs=='0'):
        break;
    
    else:
        break;




