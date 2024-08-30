# Import the required module for text to speech conversion
from gtts import gTTS
from pypdf import PdfReader
import tkinter as tk
from tkinter import filedialog
import os

#Setting a global variable to use when saving file
file_name = ""

#Defining a function to browse pdf on button press
def browse_pdf():
    global file_name
    filetypes = [("PDF files", "*.pdf")]
    path = filedialog.askopenfilename(filetypes=filetypes)

    info_label.config(text="Note: Your audio will be ready in few seconds.",fg="red")

    file_name = path.split("/")[-1].split(".")[0] #Getting hold of file name

    # creating a pdf reader object
    reader = PdfReader(path)

    #Updating the info label
    info_label.config(text=f"Audio file created as {file_name}.mp3.", fg="green")

    # extracting text from pages
    complete_text = ""
    for page in reader.pages:
        text = page.extract_text()
        complete_text += text

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
    myobj = gTTS(text=complete_text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save(f"{file_name}.mp3")

    #Updating select button
    select_pdf_button.config(text=f"Play {file_name}.mp3", command=lambda:play_audio(file=file_name))

    # Playing the converted file
    def play_audio(file):
        os.system(f"start {file}.mp3")

#Creating a window
window = tk.Tk()
window.title("PDF to Audio Converter")
window.minsize(width=500,height=500)

#Creating a frame
frame = tk.Frame(master=window)
frame.pack(padx=10,pady=10)

#Creating widgets
title_label = tk.Label(master=frame, text="PDF to Audio Converter", font=("Calibri",20,"bold"), fg="green")
title_label.grid(row=0,column=0,columnspan=2,pady=5)

info_label = tk.Label(master=frame, text="", font=("Calibri",14,"normal"))
info_label.grid(row=1, column=0,columnspan=2,pady=5)

select_pdf_button = tk.Button(master=frame, text="Select PDF", command=browse_pdf)
select_pdf_button.grid(row=2,column=0,columnspan=2)

window.mainloop()
