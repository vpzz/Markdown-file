import os

target_directory = "."
os.chdir(target_directory)  # 切换工作目录

with open("dirs.txt", encoding="utf-8") as dirstxt:
    dirs = eval(dirstxt.readlines()[0])
    for folder in dirs:
        for pic in dirs[folder]:
            if pic[1] == 0:
                print("folder:  " + folder + "   pic: " + pic[0])
                os.remove(folder+".assets/"+pic[0])
        if dirs[folder] == []:
            os.rmdir(folder+".assets")  # 空目录
