from tkinter import *
from pygame import mixer
from tkinter.filedialog import *

root=Tk()
mixer.init()
root.configure(bg='black')
root.title("MUSIC_PLAYER")
root.resizable(False,False)
pause_status=False
song_list=[]
Font=("Javanese Text",9, "bold")
index=0
song_mane=StringVar()


def song_pause_play():
	global pause_status

	if pause_status==False:
		pause_status=True
		mixer.music.pause()

	elif pause_status==True:
		pause_status=False
		mixer.music.unpause()

def chose_folder():
	directory=askdirectory()
	os.chdir(directory)
	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			song_list.append(files)		
	for i in range(0,len(song_list)):
		try:
			listbox.insert((i+1),str(i+1)+"-->"+song_list[i])
		except:
			continue

def previous_song():
	global index
	index-=1
	song_name_label.config(text="Now-Playing-->"+str(song_list[index].replace(".mp3","")))
	listbox.activate(index)	
	mixer.music.load(song_list[index])
	mixer.music.play()

def next_song():
	global index
	index+=1
	song_name_label.config(text="Now-Playing-->"+str(song_list[index].replace(".mp3","")))
	listbox.activate(index)
	mixer.music.load(song_list[index])
	mixer.music.play()	

def song_start(event):
	global index
	index=listbox.curselection()[0]
	song_name_label.config(text="Now-Playing-->"+str(song_list[index].replace(".mp3","")))
	mixer.music.load(song_list[index])
	mixer.music.play()		

def rewind_song():
	mixer.music.rewind()



top_frame=Frame(root,bd=10,bg="black")
top_frame.pack(fill=BOTH,expand=False,side=RIGHT)		
bottom_frame=Frame(root,bd=10,bg="black")
bottom_frame.pack(fill=BOTH,expand=True,side=LEFT)		

previous_bt=Button(bottom_frame,text="Previous",bg="gray",activeforeground = "red",fg="yellow",bd=10, activebackground = "cyan",font=Font,command=previous_song)
previous_bt.grid(row=2,column=1)

play_bt=Button(bottom_frame,text="Play/Pause",bg="gray",activeforeground = "red",fg="yellow",bd=10,activebackground = "cyan",font=Font,command=song_pause_play)
play_bt.grid(row=1,column=2)

next_bt=Button(bottom_frame,text="Next",bg="gray",activeforeground = "red",bd=10,fg="yellow", activebackground = "cyan",font=Font,command=next_song)
next_bt.grid(row=2,column=3)

rewind_bt=Button(bottom_frame,text="Rewind",bg="gray",activeforeground = "red",bd=10,fg="yellow", activebackground = "cyan",font=Font,command=rewind_song)
rewind_bt.grid(row=2,column=2)

load_song=Button(bottom_frame,text="Load Song", bg="gray",fg="yellow",activeforeground = "red",bd=10, activebackground = "cyan",font=Font,command=chose_folder)
load_song.grid(row=3,column=2)



song_name_label=Label( bottom_frame, text="Now-Playing-->",font=Font,wraplength=105,fg="green",bg="black",underline=14,relief=RAISED)
song_name_label.grid(row=4,column=2)

listbox = Listbox(top_frame,width=100,bd=10,relief=RAISED,bg="black",fg="cyan",font=Font,)
listbox.bind('<Double-1>',song_start)
listbox.pack(fill=BOTH,expand=True)

label=Label(top_frame,text="Song-List",font=Font)
label.pack(fill=BOTH,expand=True)


root.mainloop()