import os 
import sys

args = sys.argv
try:
    if args[1] == "h" or args[1] == "help":
        print("C/c\tWill compress after asking a few questions.\nT/t\tWill trim the video after asking for timestamps.\nG/g\tWill convert video to gif.")
    if len(args) > 3:
        if args[3] == 'c' or args[3] == 'C':
            crf = input("Compression value (15-35) ")
            if int(crf)>35:
                input("WARNING: Compression value too high. Video quality might be unwatchable.")
            os.system(f'ffmpeg -i {args[1]} -c:v libx264 -crf {crf} -c:a copy {args[2]}')
        
        if args[3] == 't' or args[3] == 'T':
            start = input("Start time stamp (can be left blank) ")
            end = input("End time stamp (can be left blank) ")
            if start !="" and end == "":
                os.system(f"ffmpeg -i {args[1]} -ss {start}  -c:a copy {args[2]}")
            elif start == "" and end != "":
                os.system(f"ffmpeg -i {args[1]} -t {end} -c:a copy {args[2]}")
            else:
                os.system(f"ffmpeg -i {args[1]} -ss {start} -to {end}  -c:a copy {args[2]}")
        
        if args[3] == 'g' or args[3] == 'G':
            frames = input("Framerate value: ")
            os.system(f'ffmpeg -i {args[1]} -vf "fps={frames},scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 {args[2]}')
    else:
        if args[2] == 'c' or args[2] == 'C':
            crf = input("Compression value (15-35) ")
            if int(crf)>35:
                input("WARNING: Compression value too high. Video quality might be unwatchable.")
            os.system(f'ffmpeg -i {args[1]} -c:v libx264 -crf {crf} -c:a copy {args[1].split(".")[0] + "_compressed.mp4"}')
        
        if args[2] == 't' or args[2] == 'T':
            start = input("Start time stamp (can be left blank) ")
            end = input("End time stamp (can be left blank) ")
            if start !="" and end == "":
                os.system(f"ffmpeg -i {args[1]} -ss {start}  -c:a copy {args[1].split(".")[0] + "_cut.mp4"}")
            elif start == "" and end != "":
                os.system(f"ffmpeg -i {args[1]} -t {end} -c:a copy {args[1].split(".")[0] + "_cut.mp4"}")
            else:
                os.system(f"ffmpeg -i {args[1]} -ss {start} -to {end}  -c:a copy {args[1].split(".")[0] + "_cut.mp4"}")
        
        if args[2] == 'g' or args[2] == 'G':
            frames = input("Framerate value: ")
            os.system(f'ffmpeg -i {args[1]} -vf "fps={frames},scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 {args[1].split(".")[0] + ".gif"}')
except IndexError:
    print("Usage: pympeg [input_name] [OPTIONAL output_name] [Flag]")
except ValueError:
    print("Incorrect value.")