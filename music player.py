from tkinter import *
import time
from tkinter import filedialog,messagebox
import pygame
import os 
import threading 


root=Tk()
root.title("music player")
root.geometry("400x600")
root.configure(background="grey")
root.resizable(False,False)
pygame.mixer.init()
# Create a function to open a file
# Global variable to keep track of the current index in the playlist
current_index = 0
is_paused = False

def AddMusic():
    global path, current_index
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

        # Set the current index to the first song in the playlist
        current_index = 0

def PlayMusic():
    global path, current_index
    global is_paused
    # Retrieve the name of the currently selected song in the playlist
    Music_Name = Playlist.get(ACTIVE)
    label=Label(root,text=f"{Music_Name}",height=2,font=("Times new roman", 10), bg="#D9DBE2", fg="grey", bd=0,wraplength=400).place(x=0,y=250)
    if is_paused:
       pygame.mixer.music.unpause()
       is_paused = False
    else:
    # Load and play the selected song
        pygame.mixer.music.load(os.path.join(path, Music_Name))
        pygame.mixer.music.play()

def PlayNextSong():
    global current_index
    # Increment the current index to play the next song
    current_index = (current_index + 1) % Playlist.size()
    # Select and play the next song
    Playlist.selection_clear(0,END)
    Playlist.selection_set(current_index)
    Playlist.activate(current_index)
    Playlist.see(current_index)
    PlayMusic()


def PlayPreviousSong():
    global current_index
    # Decrement the current index to play the previous song
    current_index = (current_index - 1) % Playlist.size()
    # Select and play the previous song
    Playlist.selection_clear(0, END)
    Playlist.selection_set(current_index)
    Playlist.activate(current_index)
    Playlist.see(current_index)
    PlayMusic()


def thread():
     thread=threading.Thread(target=online)
     thread.start()

def online():
     try:
       global s
       global driver
       s=search.get()
       import time
       from selenium import webdriver
       from selenium.webdriver.chrome.options import Options
       chrome_options = Options()
       chrome_options.add_argument("--headless")
       driver = webdriver.Chrome(options=chrome_options)
       driver.get(f"{s}")
       play_button = driver.find_element("css selector", ".ytp-play-button")
       play_button.click()

       # Prompt the user to interact before quitting
       
       # Close the WebDriver
       driver.quit()
     except:
          messagebox.showinfo("error","cannot reach to the server")
     

# Example usage


    
    

frame=Frame(root,width=400,height=100)
frame.place(x=0,y=300)


# Button
ButtonPlay = PhotoImage(file="E:/python/mp3player/play.png")
Button(root, image=ButtonPlay, bg="#F0F0F0", bd=0, height = 60, width =60,
       command=PlayMusic).place(x=170, y=300)

ButtonStop = PhotoImage(file="E:/python/mp3player/stop1.png")
Button(root, image=ButtonStop, bg="#F0F0F0", bd=0, height = 60, width =60,
       command=pygame.mixer.music.stop).place(x=80, y=300)
def PauseMusic():
    global is_paused
    pygame.mixer.music.pause()
    is_paused = True
ButtonPause = PhotoImage(file="E:/python/mp3player/pause1.png")
Button(root, image=ButtonPause, bg="#F0F0F0", bd=0, height = 60, width =60,
       command=PauseMusic).place(x=260, y=300)

# Global variable to store previous volume level
previous_volume = 0.5  # Default volume level

# Function to toggle mute/unmute
def mute():
    global previous_volume
    if pygame.mixer.music.get_volume() == 0:
        # If currently muted, restore previous volume level
        pygame.mixer.music.set_volume(previous_volume)
    else:
        # Otherwise, store current volume and set volume to 0 (mute)
        pygame.mixer.music.get_volume()== previous_volume
        pygame.mixer.music.set_volume(0)

Buttonvolume = PhotoImage(file="E:/python/mp3player/volume.png")
but=Button(root, image=Buttonvolume, bg="#F0F0F0", bd=0, height = 30, width =30,
       command=mute).place(x=15, y=364)




image=PhotoImage(file="E:/python/image/play-circle.png")
root.iconphoto(False,  image)
menu=PhotoImage(file="E:/python/image/menu.png")
Label(root,image=menu).place(x=0,y=400)
Button(root, text="Browse Music", width=50, height=1, font=("calibri",12, "bold"), fg="Black", bg="#FFFFFF",command=AddMusic).place(x=0, y=400)
def handle_paste(event=None):
    clipboard_content = root.clipboard_get()
    search.insert(END, clipboard_content)

def show_popup(event):
    popup_menu.post(event.x_root, event.y_root)

       
Button(root,text="online", height=1, font=("calibri",12, "bold"), fg="Black", bg="#FFFFFF",command=thread).place(x=50,y=550)
search=Entry(root,width=30,bg="#333333", fg="grey")
search.place(x=130,y=560)
popup_menu = Menu(root, tearoff=0)
popup_menu.add_command(label="Paste", command=handle_paste)
search.bind("<Button-3>", show_popup)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=450, width=400, height=100)
       
Button(root,text="<<<", height=1, font=("calibri",12, "bold"), fg="Black", bg="#FFFFFF",command=PlayPreviousSong).place(x=10,y=320)
Button(root,text=">>>", height=1, font=("calibri",12, "bold"), fg="Black", bg="#FFFFFF",command=PlayNextSong).place(x=340,y=320)
# Global variable to store current volume level
current_volume = 0.5  # Default volume level

# Function to update volume based on slider position
def update_volume(volume):
    global current_volume
    current_volume = float(volume) / 100  # Scale slider value to between 0.0 and 1.0
    pygame.mixer.music.set_volume(current_volume)

volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=update_volume)
volume_slider.set(50)  # Set initial value to 50 (50%)
volume_slider.place(x=50,y=349)
image1= PhotoImage(file="E:\python\image\music.png")
Label(root,image=image1).place(x=0,y=-5)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)  
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

root.mainloop()
