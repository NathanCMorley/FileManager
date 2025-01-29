import os
import shutil

SourceDir = "C:/Users/natec/Downloads"
DestinationDirImage = "C:/Users/natec/Images"
DestinationDirInstaller = "C:/Users/natec/Installers"
DestinationDirPDF = "C:/Users/natec/Documents/pdfs"
DestinationDirOther = "C:/Users/natec/Documents/other"
DestinationDirSounds = "C:/Users/natec/Documents/Sounds"
DestinationDirText = "C:/Users/natec/Documents/Text"



def move_files():
    for file in os.listdir(SourceDir):
        print(file)
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
            shutil.move(SourceDir + "\\" + file, DestinationDirImage)
        elif file.endswith(".exe") or file.endswith(".msi"):
            shutil.move(SourceDir + "\\" + file, DestinationDirInstaller)
        elif file.endswith(".pdf"):
            shutil.move(SourceDir + "\\" + file, DestinationDirPDF)
        elif file.endswith(".txt") or file.endswith(".doc") or file.endswith(".docx"):
            shutil.move(SourceDir + "\\" + file, DestinationDirText)
        elif file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
            shutil.move(SourceDir + "\\" + file, DestinationDirSounds)
        else:
            shutil.move(SourceDir + "\\" + file, DestinationDirOther)

move_files()