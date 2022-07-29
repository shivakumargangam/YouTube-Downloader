import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog ,ttk
import os
import webbrowser

def Widgets():


      link_label = Label(root,text="YouTube link :",bg="#E8D579")
      link_label.grid(row=1,column=0,pady=10,padx=10)

      root.linkText = Entry(root,width=40,textvariable=video_Link)
      root.linkText.grid(row=1,column=1,pady=5,padx=5)

      save = Label(root,text="Save As :",bg="#E8D579")
      save.grid(row=2,column=0,pady=10,padx=10)

      root.saveAsText = Entry(root,width=40,textvariable=save_as)
      root.saveAsText.grid(row=2,column=1,pady=5,padx=5)

      browse_B = Button(root,text="Search",command=openutube,width=10,bg="#05E8E0")
      browse_B.grid(row=1,column=2,pady=1,padx=1)

      destination_label = Label(root,text="Destination :",bg="#E8D579")
      destination_label.grid(row=3,column=0,pady=5,padx=5)

      root.destinationText = Entry(root,width=40,textvariable=download_Path)
      root.destinationText.grid(row=3,column=1,pady=5,padx=5)

      browse_B = Button(root,text="Browse",command=Browse,width=10,bg="#05E8E0")
      browse_B.grid(row=3,column=2,pady=1,padx=1)

      Download_B = Button(root,text="DOWNLOAD",command=Download,width=20,bg="#05E8E0")
      Download_B.grid(row=6,column=1,pady=3,padx=3)


      label_choice=Label(root,text="Choose Download Type",fg='green',bg='yellow')
      label_choice.grid(row=4,column=1,pady=3,padx=3)

def openutube():
      webbrowser.open('https://www.youtube.com')

def Browse():

      download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
      download_Path.set(download_Directory)
      f=filedialog.asksaveasfile(mode='w')


def Download():

      choice=choicesyt.get()
      Youtube_link = video_Link.get()
      download_Folder = download_Path.get()
      saveas=save_as.get()

      if 'youtube' in Youtube_link:
            getVideo = YouTube(Youtube_link)
            if len(saveas)>1:
                  getVideo.title=saveas
            try:
                  if(choice==choices[0]):
                        videoStream=getVideo.streams.filter(res='720p',).first()
                        videoStream.download(download_Folder)
                        messagebox.showinfo("SUCCESSFULL",getVideo.title+"\nDOWNLOADED AND SAVED IN\n"+ download_Folder)
                  elif(choice==choices[1]):
                        videoStream=getVideo.streams.filter(progressive=True,file_extension='mp4').last()
                        videoStream.download(download_Folder)
                        messagebox.showinfo("SUCCESSFULL",getVideo.title+"\nDOWNLOADED AND SAVED IN\n"+ download_Folder)
                  elif(choice==choices[2]):
                        t=getVideo.streams.get_audio_only()
                        out_file=t.download(download_Folder)
                        base, ext = os.path.splitext(out_file)
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)
                        messagebox.showinfo("SUCCESSFULL",getVideo.title+"\nDOWNLOADED AND SAVED IN\n"+ download_Folder)
                  else:
                        messagebox.showinfo("UNSUCCESSFULL","PLEASE SELECT DOWNLOAD TYPE\n")
            except:
                  messagebox.showinfo("UNSUCCESSFULL","CONNECTION ERROR\n")
      else:
            messagebox.showinfo("UNSUCCESSFULL","PASTE CORRECT LINK\n")



root = tk.Tk()

root.geometry("600x200")
root.resizable(False, False)
root.title("YouTube_Video_Downloader")
root.config(background="#000000")


video_Link = StringVar()
download_Path = StringVar()
save_as = StringVar()

choices=['720p','360p','mp3']
choicesyt=ttk.Combobox(root,values=choices)
choicesyt.grid(row=5,column=1,pady=3,padx=3)
Widgets()

root.mainloop()
