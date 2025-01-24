import os.path
import re
import os
import shutil

# 主要处理函数 delimit_char为正则表达式末尾的界定字符 flag表示文件是否需要重新修改
def match_replace(match, md_file_name, linenumber, delimit_char, flag):
    if not match.group(3):
        print("filepos: "+match.group(2)+"    "+md_file_name)
        return
    folder_name = match.group(3)[:-7]
    pic_name = match.group(4)
    if folder_name == md_file_name:  # 引用的文件夹名==.md文件名
        for figure in dirs[md_file_name]:
            if pic_name == figure[0]:
                figure[1] = 1  # 标记一下，表示这个图片已经正确的文件被引用了
    else:
        flag = 1  # 标记一下
        for figure in dirs[folder_name]:
            if pic_name == figure[0]:
                figure[1] = 1  # 标记一下，表示该文件已被移动走
                shutil.move(folder_name+".assets"+"/"+pic_name,
                            md_file_name + ".assets")  # 移动到应该的文件夹中
        line = lines[linenumber]
        lines[linenumber] = line[:match.start()]+match.group(1) + md_file_name + \
            ".assets" + "/" + pic_name + delimit_char + line[match.end():]


# 文件目录处理
target_directory = "."
os.chdir(target_directory)  # 切换工作目录
# 获取所有的md文件和目录中的图片
files = []  # 保存外层的.md文件
dirs = {}   # 保存.assets目录中的图片，键为目录名，值为其下文件的列表。
for outer_name in os.listdir("."):
    if os.path.isfile(outer_name) and outer_name.endswith(".md"):  # .md文件
        #files[outer_name] = []
        files.append(outer_name[:-3])  # 将xxx.md文件的xxx添加到files列表种
    elif os.path.isdir(outer_name) and outer_name.endswith(".assets"):  # 目录
        dirs[outer_name[:-7]] = []  # 添加文件夹名称对应的键
        file_size = 0
        for name in os.listdir(outer_name):
            dirs[outer_name[:-7]].append([name, 0])
            file_size += os.stat(outer_name+"/"+name).st_size
        print(outer_name + " : " + str(file_size/1024.0/1024.0) + "MB")
    else:
        pass  # 其他文件，例如.gitignore或.git文件夹

# 读取.md文件，正则匹配其中的图片引用。
for md_file_name in files:
    lines = 0
    flag = 0  # 用于标识文件是否需要修改
    with open(md_file_name+".md", "r", encoding="utf-8") as mdfile:
        # 三种图片插入的形式，正则如下：
        # <img src="((.*?)/(.*?))"
        # !\[.*?\]\(((.*?)/(.*?))\)
        # 同上

        #  <img src="Make.assets/image-20200604012451718.png" alt="image-20200604012451718"  />
        #  ![image-20200604012922240](Make.assets/image-20200604012922240.png)
        #  ![1590760102831](Python.assets/1590760102831.png)
        # 逐行进行正则匹配
        lines = mdfile.readlines()
        for linenumber in range(len(lines)):
            line = lines[linenumber]
            match1 = re.search(r'(<img src=")((.*?)/(.*?))"', line)
            match2 = re.search(r'(!\[.*?\]\()((.*?)/(.*?))\)', line)
            if match1:
                match_replace(match1, md_file_name, linenumber, '\"', 0)
            elif match2:
                match_replace(match2, md_file_name, linenumber, ')', 0)
    if not flag:  # 如果flag没有被置1，则表示文件不需要被修改
        continue
    stinfo = os.stat(md_file_name+".md")  # 保存文件的修改时间
    stinfo.st_size()
    with open(md_file_name+".md", "w", encoding="utf-8") as mdfile:
        mdfile.seek(0)
        mdfile.writelines(lines)
    os.utime(md_file_name+".md", (stinfo.st_atime, stinfo.st_mtime))  # 恢复修改时间

# 输出一下一共有多少图片从未被引用过，接下来要删除这些图片
for folder in dirs:
    for pic in dirs[folder]:
        if pic[1] == 0:
            print("folder:  "+folder+"   pic: "+pic[0])
# 保存dirs到文件
with open("dirs.txt", "w", encoding="utf-8") as dirtxt:
    dirtxt.write(str(dirs))
