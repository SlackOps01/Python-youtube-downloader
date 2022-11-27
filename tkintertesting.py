from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("550x250")


def download():
    url = inputbox.get()
    my_video = YouTube(url)
    nameLabel = Label(root, text=f'{my_video.title} is being downloaded')
    nameLabel.grid(row=4, column=0)
    downloader = my_video.streams.get_highest_resolution()
    print(f'Downloading {my_video.title}...')
    downloader.download()
    print(f'{my_video.title} has downloaded')
    nameLabel = Label(root, text=f'{my_video.title} has been downloaded')
    nameLabel.grid(row=4, column=0)
    
    
    
myLabel = Label(root, text="Youtube video download")
myLabel2 = Label(root, text="At the end of this project you would be able to download videos from youtube")
inputbox = Entry(root)
downloadbtn = Button(root, text="Download", command=download)


myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0, padx=15)
inputbox.grid(row=2, column=0, padx=15)
downloadbtn.grid(row=3, column=0)



root.mainloop()