import subprocess
import sys
import argparse
def find_files(files):
    subprocess.run("chcp 65001", shell=True)
    if not files.find("."):
        result = subprocess.run(f"dir /b *.{files}", shell=True, capture_output=True, text=True)
        splited = result.stdout.split("\n")
        #deleting the last index of array which is empty
        splited.pop()
        print(splited)
        for index, name in enumerate(splited):
            Thumbnail(name)
    else:
        Thumbnail(files)
    print("\n\n\nThank you for using our product ;)")
    print("buy me a coffee:BSC 0x46ba88b1d176af5e213139f37d8e1fd787b18f11\n\n")
def Thumbnail(name):
    try:
        ext = name.replace(f".{name}","-x")
    except:
        ext = name.replace(f"{name}","-x")
    command = f'ffmpeg -i "{name}" -ss 00:00:14.435 -frames:v 1 "{ext}.png"'
    subprocess.run(command, shell=True,text=True)
    command = f'ffmpeg -i "{name}" -i "{ext}.png" -map 1 -map 0 -c copy -disposition:0 attached_pic "attached_pic{name}"'
    subprocess.run(command, shell=True,text=True)
if len(sys.argv) > 1:
        # Create the parser
        parser = argparse.ArgumentParser(description="welcome to Auto Thumb:")

        # Add arguments
        parser.add_argument('-name', type=str, help='file name: -name atm.mp4 or gameofthrones.mkv')
        parser.add_argument('-all', type=str , help='all *.extention files in directory: -all mp4')
        parser.add_argument('--force', action = "store_true" , help='force the program to auto thumbnail note: this will change all files name!')
        # Parse the arguments
        args = parser.parse_args()

        # Use the parsed arguments
        if args.force:
            print(f"force the program to auto thumbnail note: this will change all files name!") 
            #creating and using autorename.bat to rename files: !python cannot realy work with names like شیشبسیبشسیب)(شسیجچ[شسیشی_02_10_谢谢你的帮助2019]).mp4
            #so let's turn them to a meaningfull name for python :)
            #the code is:
            """
                @echo off
                setlocal enabledelayedexpansion
                set count=0

                for %%f in (*.mp4) do (
                    ren "%%f" "!count!.mp4"
                    set /a count+=1
                )
            """
            with open('autorename.bat', 'w') as file:
                file.write("@echo off\nsetlocal enabledelayedexpansion\nset count=0\n\nfor %%f in (*.mp4) do (\n    ren '%%f' '!count!.mp4'\n    set /a count+=1\n)\n") 
            subprocess.run("batch.bat", shell=True)
        if args.name:
            print(f"Thumbnailing {args.name}")
            try:
                find_files(args.name)
            except:
                print("it seems the file name are not supported try --force note: This will change your files name!")
            if args.all:
                print("Ignoring all")
        elif args.all:
            print(f"all *.{args.all} files selected")
            try:
                find_files(args.all)
            except:
                print("it seems the files name are not supported try --force note: This will change your files name!")


