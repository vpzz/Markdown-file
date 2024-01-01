# 集中式和分布式版本控制系统

1. 目的是为了版本控制，最重要的就是历史记录，可回溯。有时候要对已有的功能进行更改，如果更改后觉得不好，则应该能够退回到之前的情况。
2. 集中化的有CVS，SVN等，有一个集中的服务器，所有的用户都要和服务器进行交互。C/S架构。好处是每个人都可以知道其他人修改的内容，管理员也可以掌控所有人的权限。缺点是如果中央服务器出现故障，则不能正常运作，因为此时==各个客户端只有最新的版本，所有的历史版本都保存在服务器上==，回不到过去的情况。同时，如果服务器宕机3小时，你在前一个小时，写了一个功能，后2个小时对这个功能进行了修改，那么想回到最初的1个小时的情况是不可以的。
3. 集中式的版本控制系统，用户在每写完一个功能或者觉得以后可能会回退到这个情况的时候，都应该在此时和服务器同步一下，让服务器记录一下。如果服务器临时宕机，也可以手动备份，手动做版本控制，等到服务器上线在分步上传。
4. 服务器宕机期间，所做的修改得不到保障；服务器硬盘损坏，项目的所有历史记录都没了，不过可以从客户端的快照中恢复一部分记录。
5. git是分布式的。客户端并不是之提取最新的文件快照，而是将整个代码仓库都克隆下来。相当于每个客户端都成了SVN的服务器。这也是分布式的概念，即没有中心服务器。因此分布式的版本控制系统的客户端存储的内容比使用集中式的要多。不过git可以做到只增加很少的存储空间，极致压缩。
6. git中也可以有中央服务器，他的重要性和每个客户端一样。主要是用来做代码仓库的，新用户直接从github克隆。中央服务器只是大家用来通信的公共平台，优点是24小时在线。
7. git诞生的原因是当时的linux内核代码越来越庞大，协作的人越来越多，使用集中式版本控制系统管理越来越费时。到2002年，开始使用BitKeeper的分布式系统，2005年该公司收回了使用的权利。迫使linus开发一个分布式版本控制系统。
8. git的优点：分支切换速度快，容量小，完全分布式，允许上千个并行开发的分支，能够有效管理大型项目。离线也能进行版本管理，可以等到有网络时再同步。
9. 由于各个用户在本地进行修改之后，版本之间存在差异，可以都将修改提交到中央服务器，来统一管理。
10. 局域网和公网上都可以有代码仓库。
11. 以往的版本控制系统存放的是版本之间的差异，就是增量备份，需要硬盘空间小。如果版本相距较远的话，回溯较慢，因为需要逐一回滚，应用修改。
12. Git存储的是项目的完整快照，对待数据更像是快照流，需要的硬盘空间相对较大，回滚速度极快。硬盘的提升成本较低，git的前景较大。
13. git的绝大多数操作都在本地进行，不需要联网，因此特别快。
14. git中的所有数据在存储前都会计算校验和，使用校验和来引用数据。这意味着不可能在git不知情的情况下修改任何文件或目录的内容，这个是git的设计哲学。
15. 校验和是SHA-1散列，160位，40个十六进制字符构成的字符串，基于Git中文件和目录结构计算出来的。Git之所以使用校验和而不是文件名来引用数据是因为文件内容改变时文件名不会变，而校验和会变，只用文件名无法区别。
16. Git一般只添加数据，很少删除数据，也就是说Git很少会执行导致文件不可恢复的操作。当更新未提交时，可能会丢失，一旦提交，就会永远留在项目历史中。
17. 版本是用户主动对文件做的一个标记，可以在未来的某个时间段恢复到这个状态。
18. Windows上的git是基于一个Git for windows的项目。

# 配置文件

1. 配置文件一共有3种：

   1. /etc/gitconfig	                            系统级配置文件             	git config --system     需要管理员权限才可以设置
   2. \~/.gitconfig或\~/.config/git/config  用户级配置文件            	git config --golbal
   3. .git/config	 		 		 		 	 仓库级配置文件          		git config --local    默认是这个

2. Windows下系统级配置文件在Msys的根目录下的etc/gitconfig文件。用户级配置文件在$HOME下的.gitconfig文件，仓库级的配置文件和linux下相同。

3. 配置文件中最重要的就是要协商user.name 和user.email    这些信息会记录到修改记录中，如果出问题的话，可以根据这些信息来追溯修改是谁做出的。

4. 一般的话只配置~/.gitconfig，因为一台计算机上可能有多个用户在使用，他们的信息一般是不同的。

5. ```shell
   git config --global user.name "ZJ"     #如果没有--global，则表示对当前项目使用，即修改.git/config文件。
   git config --global user.email 747056333@qq.com
   ```

6. 在项目中会依次读取系统→用户→仓库的配置文件，优先级依次升高。在仓库文件夹下，git config -l才会显示仓库级配置文件中的内容。在其他目录运行该命令只会显示用户配置文件中的内容。

   ```shell
   git config --list --show-origin  #显示所有的配置，并显示他们所在的文件。
   ```

7. 虚拟机的git可以通过设置代理来通过宿主机的vpn来科学上网：

   ```shell
   git config --global http.proxy http://192.168.80.1:10809   #设置全局http代理,其中192.168.80.1为虚拟机中宿主机的ip地址。
   git config --global http.proxy socks5://192.168.80.1:10808   #也可以使用socks5代理,如果不加socks5则表示使用http协议。
   git config --global --unset http.proxy  #取消代理
   
   #也可以手动在git的配置文件中添加如下项：
   [http]
           proxy = 192.168.80.1:10809
   ```

8. 还可以为系统设置统一的代理，最好写入到bashrc文件中：

   ```shell
   export http_proxy=192.168.80.1:10809
   export https_proxy=192.168.80.1:10809
   ```

9. 还应该设置默认的文本编辑器，git有时会打开文本编辑器，让用户填写一些信息，填写完保存后关闭即可。

   ```shell
   git config --global core.editor vim
   ```

10. git软件升级时不会删除配置文件。git config的设置都会立刻记录在配置文件中。

11. 检查某项配置

    ```shell
    git config user.name   #检查用户名的设置情况，可以加上 --show-origin 选项，来查看那个配置文件最后设置了该值。
    ```

# 基础

## init和clone

1. git init只是初始化了一个空的仓库，本地的文件都还没有进行追踪。如果是在一个非空的本地目录下init，应该先add所有的文件，建立初始commit。

2. git克隆的是该Git仓库的所有数据，而不仅仅是工作目录的文件。远程仓库里的每个文件的每个版本都会被拉取过来，然后从版本数据库中解压缩当前分支到工作目录。Clone会自动创建目录。

   ```shell
   git clone https://github.com/libgit2/libgit2  #会在当前目录下新建一个libgit2的目录
   git clone https://github.com/libgit2/libgit2 mylibgit   #新建的目录名为mylibgit
   ```

3. git支持多种数据传输协议：HTTPS，Git，SSH等。

4. 刚克隆完仓库，运行git status显示如下：

   ```shell
   git status
   On branch master
   Your branch is up-to-date with 'origin/master'.
   nothing to commit, working directory clean
   ```


## 文件状态

1. Git管理的文件可能处于以下三种情况之一：

   1. 已修改（modified），表示该文件已经被修改，且修改还没有被git保存。

   2. 已暂存（staged），表示一个已修改的文件已经被保存在暂存区，等待下一次提交。

   3. 已提交（committed），表示数据已经安全地存储到了git的仓库中，生成了一个新的版本。

2. 以上三种统称为已跟踪，还有一种是untracked 未跟踪，在之前的提交里没有这个文件，Git不会自动将它纳入管理范围。

3. 也可以add 目录，这会递归地add该目录下的所有文件。

   ```shell
   git add README                        # 将文件纳入Git管理，同时该文件会被加入到暂存区。
   git status
   On branch master
   Your branch is up-to-date with 'origin/master'.
   Changes to be committed:
   (use "git restore --staged <file>..." to unstage)    # 将该文件恢复为 未跟踪
   new file: README
   ```

4. 未被追踪的文件被追踪后，再进行修改，再暂存，再修改，得到的结果和刚被检出的文件进行修改，暂存，再修改相同。

5. 如果一个文件自上次提交后，进行了修改，git status显示：

   ```shell
   git status
   On branch master
   Changes not staged for commit:                                 #以下的文件都是已修改，待暂存的
     (use "git add <file>..." to update what will be committed)   #将文件当前状态保存到暂存区。
     (use "git restore <file>..." to discard changes in working directory) #舍弃文件的修改，将该文件恢复为检出时的版本。
           modified:   xxx.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

6. 如果一个文件自上次提交后，进行了修改，又进行了暂存，git status显示：

   ```shell
   git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)    #将该文件从暂存区移出，也就是add的逆操作。不会改变工作目录中的文件
           modified:   xxx.txt
   ```

7. 如果一个文件自上次提交后，进行了修改，然后暂存，之后又进行了修改，git status显示：

   ```shell
   git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)  #将暂存区中该文件的暂存删除，执行后该文件好像从未暂存过，两次修改被视为一次。变成Changes not staged for commit
           modified:   xxx.txt
   
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed) #将修改后的文件暂存，会替换掉该文件之前的暂存。执行后，变为Changes to be committed
     (use "git restore <file>..." to discard changes in working directory) #舍弃文件的修改，将该文件恢复为暂存区的版本。执行后，工作目录中的文件会被暂存区的覆盖。变成 Changes to be committed。
           modified:   xxx.txt
   ```

8. 此时文件xxx.txt同时位于暂存区和非暂存区。如果此时commit，会提交位于暂存区的版本，而不是和工作目录相同的文件内容。

9. ![image-20220721001718319](Git.assets/image-20220721001718319.png)

10. 对于于上面的三种状态，也存在区域：

    1. 工作区，沙箱环境，是从Git仓库的压缩数据库中提取出来的，可以任意操作，且都可以恢复到最开始。Git不会管理这部分的内容。是执行git init或git clone时的目录。
    2. 暂存区，.git/index文件，保存了下一次要提交的文件列表信息，也成为索引。
    3. 版本库，.git目录，保存项目元数据和对象数据库的地方。最重要的部分，克隆项目时，就是复制这个文件夹。

11. git add是个多功能的命令：

    1. 可以用来跟踪一个从未被跟踪的文件。
    2. 可以暂存一个已经被修改的文件。
    3. 用于合并时把有冲突的文件标记为已解决状态。

12. 一个文件在暂存区只能保存一个，新的暂存会替换掉旧的。可以add一个没有修改过的文件，不会报错。

13. git status命令输出十分详细，可以用git status -s或 --short来更紧凑的输出：

    ```shell
    git status -s    #输出中有两栏，左侧为暂存区的状态，右侧为工作区的状态。
    M README           #在工作区修改了，尚未暂存。
    MM Rakefile        #已修改，暂存后又做了修改。
    A lib/git.rb       #新添加到暂存区的文件为A。
    M lib/simplegit.rb #修改过的文件有M标记。已修改且已暂存。
    ?? LICENSE.txt     #新添加的未跟踪的文件为??的标记。
    ```


## .gitignore

1. 使用.gitignore文件来指定不希望被追踪的文件，这样git status不会显示这些文件没有被追踪。通常是一些自动生成的文件，例如日志文件，编译过程产生的临时文件。

2. .gitignore中是要忽略的文件模式。应该在仓库初始化时就创建.gitignore文件，以免提交无用的文件。任何一个文件相对于.gitignore所在的目录都有一个相对路径。将这个相对路径来跟每个文件模式匹配，一旦有匹配的，则忽略该文件。

   ```shell
   *.[oa]    #忽略所有以.a或.o结尾的文件。一般是编译产生的中间文件。
   *~        #忽略所有以~结尾的文件。一些编辑器的文件副本都会以~结尾。
   !lib.a    #不忽略lib.a文件。
   /TODO     #只忽略当前目录的TODO文件，子目录下的TODO不忽略。
   build/    #忽略任何目录下名为build的文件夹。
   doc/*.txt #忽略doc目录下.txt结尾的文件，例如doc/xxx.txt，但是不忽略doc/aa/x.txt。
   doc/**/*.pdf #忽略doc目录及其所有子目录下以.pdf结尾的文件。
   ```

3. .gitignore文件规范：

   1. 所有的空行和#开头的行（注释）都会被git忽略。
   2. 可以使用标准的glob模式来书写规则，它会递归地应用到整个工作区中。 
   3. 匹配模式以/开头可以防止递归，默认是递归的。
   4. 匹配模式以/结尾用来指定目录，默认是文件。
   5. 要忽略指定模式以外的文件或目录，可以在模式前加！。

4. glob模式就是shell使用的，简化了的正则表达式。

   ```shell
   1. *匹配0个或多个任意字符
   2. ?匹配单个任意字符
   3. [abc]匹配方括号中的任意一个字符
   4. [0-9]匹配任意0到9数字，[a-z]匹配a到z的字符
   5. **匹配任意中间目录，a/**/z可以匹配a/z，a/b/z，a/b/c/d/z
   ```

5. 一般情况下，一个项目只在根目录下有一个.gitignore文件，它会递归地应用到整个项目中。然而子目录也可以有自己的.gitignore文件，不过该文件只会应用在所在的目录及其子目录中。

6. git命令也可以使用blob模式，不过要先经过shell的转义。例如要添加log目录下所有以.log结尾的文件。

   ```shell
   git add log/\*.log      #需要用\来为*转义。不适用shell的模式展开。
   ```


## diff

1. 使用git diff可以查看那些修改还未暂存，那些修改已经暂存。

   ```shell
   git diff   #这里是对刚检出的xxx.txt文件进行了修改，但还未暂存。 不加任何参数表示：工作目录中的文件相对于暂存区的修改，也就是还未暂存的修改。
   diff --git a/xxx.txt b/xxx.txt
   index ce8c77d..af7864b 100644
   --- a/xxx.txt
   +++ b/xxx.txt
   @@ -1,2 +1,3 @@
    123
    456
   +789
   
   git diff --staged   #查看暂存区文件相对于上一次提交的修改。等价于--cached参数。
   diff --git a/xxx.txt b/xxx.txt
   index 190a180..ce8c77d 100644
   --- a/xxx.txt
   +++ b/xxx.txt
   @@ -1 +1,2 @@
    123
   +456
   
   ```

2. 也可以使用图形化的工具来进行diff，git difftool --tool-help来查看系统支持的Git diff插件。运行git difftool来调用默认的图形化工具。


## commit

1. commit只会提交暂存区的文件版本。提交前建议运行git status，看看有没有未追踪的文件，或者未暂存的修改。commit不会修改工作区。

   ```shell
   git commit   #运行命令会启动默认的编辑器来编辑提交信息。默认使用SHELL的EDITOR环境变量，也可以使用 git config --global core.editor来设置喜欢的编辑器。
   ```

2. 编辑器的内容如下，默认包含了git status的结果，方便记录修改的内容，尤其是在修改较多的时候。#开头的行会被忽略，退出编辑器时，Git会丢弃这些行。第一行是空行，一般在这里填写提交信息。如果没有写入任何有效的信息就退出编辑器，则此次commit会失败。Aborting commit due to empty commit message。

   ```shell
   
   # Please enter the commit message for your changes. Lines starting
   # with '#' will be ignored, and an empty message aborts the commit.
   #
   # On branch master
   # Changes to be committed:
   #       modified:   xxx.txt
   #
   ```

3. 有时候暂存区的存在使得步骤繁琐，git commit -a可以将所有==已跟踪的文件==add一遍，然后再commit，对于未跟踪的文件则不会add。

4. commit可以使用-m选项来将提交信息和命令放在一行，这样就不会打开编辑器了

   ```shell
   git commit -m "First commit."
   [master 11cd002] First commit.      #提交的分支为master，本次commit对象的校验和为11cd002
    1 file changed, 2 insertions(+)    #有一个文件被修改，包含2处插入
   ```


## 删除和移动文件

1. 要从Git中移出某个文件，先取消对该文件的追踪（从暂存区移出），然后提交。有多种方法：

   1. 用git rm 该文件，然后commit即可。等价于先rm，再add。这也会删除工作目录的文件，这样该文件也不会出现在未跟踪列表中。

   2. 用rm命令删除文件，然后git add/rm 该文件，最后commit即可。

2. 如果先在工作目录用rm命令删除了某个文件，此时git status会显示

   ```shell
   git status
   On branch master
   Changes not staged for commit:
     (use "git add/rm <file>..." to update what will be committed) #将文件被删除这一修改保存到暂存区。
     (use "git restore <file>..." to discard changes in working directory)  #从历史提交中恢复该文件到工作目录。
           deleted:    xxx.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

3. 然后运行git add将删除操作保存到暂存区，最后提交就可以在git中真正删除文件了。

   ```shell
   git add xxx.txt   #等价于git rm xxx.txt
   
   git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)  #取消刚才的add或rm的效果。
           deleted:    xxx.txt
   
   git commit -m "delete xxx.txt"
   [master baec33d] delete xxx.txt
    1 file changed, 3 deletions(-)
    delete mode 100644 xxx.txt
   ```

4. 另一种情况是想在git仓库中删除该文件，但是保留工作目录中的文件，即不被git追踪。

   ```shell
   git rm --cached README 
   
   git commit -m "untracked README"  #rm之后，还要提交才可以生效。
   ```

5. 如果要删除的文件是已修改或已经被暂存了的，需要加上-f选项，丢弃工作目录和暂存的修改。

6. 移动文件：Git并不显式跟踪文件移动操作，元数据也不会体现出这是一次重命名操作。Git rm就是删除旧文件，添加新文件。

   ```shell
   git mv xxx.txt new.txt  #将xxx.txt重命名为new.txt，
   #相当于运行了三条命令，即使分开运行这三条命令，Git也会意识到这是一次重命名操作。
   # mv xxx.txt new.txt
   # git rm xxx.txt
   # git add new.txt
   
   git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           renamed:    xxx.txt -> new.txt             
   ```


## log

1. 查看日志：

   ```shell
   git log  #不加任何参数，会按照时间由近及远的顺序列出所有的commit，
   commit d0e2ba7ef3aa7c617287b89ea33fa714fb7f82b0 (HEAD -> master)   #SHA-1校验和
   Author: zj <747056333@qq.com>            #作者名，邮箱
   Date:   Tue Jul 26 11:19:23 2022 +0800   #时间日期
   
       rename xxx.txt -> new.txt            #提交信息
   
   commit 63ec6bb3c41ef349531fbba6e52e037c32ad63d1
   Author: zj <747056333@qq.com>
   Date:   Tue Jul 26 11:12:50 2022 +0800
   
       add xxx.txt
   git log -p  # --patch 以补丁格式显示每次新提交相对于旧提交的差异。
   commit d0e2ba7ef3aa7c617287b89ea33fa714fb7f82b0 (HEAD -> master)
   Author: zj <747056333@qq.com>
   Date:   Tue Jul 26 11:19:23 2022 +0800
   
       rename xxx.txt -> new.txt
   
   diff --git a/xxx.txt b/new.txt
   similarity index 100%
   rename from xxx.txt
   rename to new.txt
   
   commit 63ec6bb3c41ef349531fbba6e52e037c32ad63d1
   Author: zj <747056333@qq.com>
   Date:   Tue Jul 26 11:12:50 2022 +0800
   
       add xxx.txt
   
   diff --git a/xxx.txt b/xxx.txt
   new file mode 100644
   index 0000000..af7864b   #旧提交中，该文件的SHA-1也为全0。
   --- /dev/null            #这是新跟踪的文件，因此旧提交中该文件为空。
   +++ b/xxx.txt
   @@ -0,0 +1,3 @@
   +123
   +456
   +789
   ```

2. 其他选项

   ```shell
   -stat   #显示每次提交的简略信息，例如：
   README | 6 ++++++
   Rakefile | 23 +++++++++++++++++++++++
   lib/simplegit.rb | 25 +++++++++++++++++++++++++
   3 files changed, 54 insertions(+)
   --pretty=oneline  #将每个提交放在一行展示，在浏览大量提交时非常有用
   git log --pretty=format:"%h - %an, %ar : %s"   #以定制格式输出每次的提交。%h为简写的Hash，%an为作者名字，%ar为作者修订日期
   d0e2ba7 - zj, 32 minutes ago : rename xxx.txt -> new.txt
   63ec6bb - zj, 39 minutes ago : add xxx.txt
   c2de97f - zj, 2 days ago : delete README
   
   -p     #按补丁格式显示每个提交引入的差异。
   --stat #显示每次提交的文件修改统计信息。
   --shortstat #只显示 --stat 中最后的行数修改添加移除统计。
   --name-only #仅在提交信息后显示已修改的文件清单。
   --name-status #显示新增、修改、删除的文件清单。
   --abbrev-commit #仅显示 SHA-1 校验和所有 40 个字符中的前几个字符。
   --relative-date #使用较短的相对时间而不是完整格式显示日期（比如“2 weeks ago”）。
   --graph #在日志旁以 ASCII 图形显示分支与合并历史。
   --pretty #使用其他格式显示历史提交信息。可用的选项包括 oneline、short、full、fuller 和
   format（用来定义自己的格式）。
   --oneline #等于 --pretty=oneline --abbrev-commit 合用的简写。
   ```

3. oneline或format与--graph结合使用时尤其有用，可以形象地观察仓库的分支，合并历史：

   ```shell
   git log --pretty=format:"%h %s" --graph
   * 2d3acf9 ignore errors from SIGCHLD on trap
   * 5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
   |\
   | * 420eac9 Added a method for getting the current branch.
   * | 30e367c timeout code and tests
   * | 5a09431 add timeout protection to grit
   * | e1193f8 support for heads with slashes in them
   |/
   * d6016bc require time for xmlschema
   * 11d191e Merge branch 'defunkt' into local
   ```

4. 限制输出长度的选项：

   ```shell
   -n                  #只显示最近的n次提交
   --since, --after    #仅显示指定时间之后的提交。  --since="2022-07-30"  --since=2.weeks 或"2 weeks"
   --until, --before   #仅显示指定时间之前的提交。
   --author            #仅显示作者匹配指定字符串的提交。
   --committer         #仅显示提交者匹配指定字符串的提交。
   --grep              #仅显示提交说明中包含指定字符串的提交。可以有多个--grep，不过默认是或的关系，除非使用--all-match。
   -S                  #仅显示添加或删除内容匹配指定字符串的提交。 -S "修改内容"  这个是针对修改内容查找，实际上找patch。
   
   ```

5. 一次提交存在一个作者和一个提交者，一般来说作者和提交者是同一个人，但是在一个大项目中，系统只会给管理人员开放提交权限，其他人员修改好代码后，可以发出一个pull request 给远程仓库。远程仓库的管理员才会去拉取其他人员的提交，然后确认可以合并到主仓库后，再提交。此时该提交的作者就是真正的修改者，而提交者是管理人员。

6. Git默认会将输出传入到分页程序中，例如less，一次只会看到一页。

7. 按照你代码仓库的工作流程，记录中可能有为数不少的合并提交，它们所包含的信息通常并不多。 为了避免显示的合并提交弄乱历史记录，可以为 log 加上 --no-merges 选项。

8. 有些时候提交完才发现，有些文件忘了add，或者提交信息写错了。可以运行以下命令来重新提交：

   ```shell
   git commit --amend   #此命令会将当前暂存区的文件提交，如果自上次提交后没有修改过暂存区，那么这个命令就只会修改提交信息。Editor启动后，可以看到上一次的提交信息，重新编辑保存即可。
   ```

9. amend实际上是用一个新的提交来覆盖旧的，好像旧的从未存在过一样，也不会出现在仓库历史中。此选项适用于小修小补，使得仓库历史更好看些，因此不建议做太大的更改，大更改还是建议作为一个新的提交。

10. git reset确实是一个危险的命令，如果加上了--hard选项更为如此。

11. 在 Git 中任何 已提交 的东西几乎总是可以恢复的。 甚至那些被删除的分支中的提交或使用 --amend 选项覆盖的提交也可以恢复 （阅读 数据恢复 了解数据恢复）。 然而，任何你未提交的东西丢失后很可能再也找不到了。因此撤销工作目录中的修改要慎重。


## 远程仓库

1. 一个项目可以有多个远程仓库，通常某些对你只读，某些可以读写。实际上远程仓库可以在本机上，不过仍需要和操作真正的远程仓库一样来使用推拉等操作。

2. 查看远程仓库：

   ```shell
   git remote   #显示远程仓库的简写。克隆项目时，Git会自行添加远程仓库，默认名字就是origin。刚克隆完时，只有一个远程仓库。
   origin
   git remote -v  #显示远程仓库对应的URL，支持多种协议。
   origin https://github.com/schacon/ticgit (fetch) #表示有读取权限
   origin https://github.com/schacon/ticgit (push)  #表示有写入权限
   git remote show origin      #显示origin远程仓库的详细信息
   * remote origin
   Fetch URL: https://github.com/schacon/ticgit
   Push URL: https://github.com/schacon/ticgit
   HEAD branch: master    #远程仓库的当前分支
   Remote branches:       #远程仓库的各分支情况
   master tracked         #本地关于远程的master分支的数据是最新的
   dev-branch tracked     #dev-branch分支也是最新的
   Local branch configured for 'git pull':  #运行git gull时，实际执行的操作
   master merges with remote master
   Local ref configured for 'git push':
   master pushes to master (up to date)
   ```

3. 添加新的远程仓库：

   ```shell
   git remote add bobo https://github.com/paulboone/ticgit #添加一个新的远程 Git 仓库，同时指定一个方便使用的简写bobo。可以在命令中使用字符串bobo来代替整个URL
   ```

4. 从远程仓库拉取内容：

   ```shell
   git fetch bobo #拉取bobo仓库中有的，但是本地没有的信息，此后拥有远程仓库bobo所有分支的引用，可以随时合并或查看。此时bobo的xxx分支可以在本地通过bobo/xxx访问到。
   ```

5. fetch只会拉取内容，并不会自动合并或修改当前的工作。

6. 如果当前分支设置了跟踪远程分支，则可以使用git pull来拉取并合并该远程分支到当前分支。默认情况下，clone操作会自动将本地的master分支跟踪克隆仓库的master分支（或其他名字的默认分支）

7. 推送数据到远程仓库：

   ```shell
   git push origin master  #将本地的master分支推送到远程仓库origin中。相当于远程仓库的所有者运行pull，从本地拉取并合并到远程仓库。
   ```

8. 只有当你对远程仓库具有写权限，且之前没有人推送过，这条命令才可以正确执行。如果在你上一次推送后其他人进行了推送，那么你就必须要先拉取远程仓库，合并他们的工作，然后再推送过去。

9. 远程仓库的重命名与删除：

   ```shell
   git remote rename origin bobo  #将远程仓库origin的名字修改为bobo，这样会自动修改远程跟踪分支的名字，过去的origin/master会变为bobo/master。
   git remote remove paul #删除某个远程仓库，该仓库的远程跟踪分支和配置信息也会一起被删除。
   ```


## 标签

1. 打标签，Git可以给仓库历史中的某一个提交打上一个标签，用来标记新版本，例如v1.0，v1.1等。默认是给当前分支的当前提交对象打标签。

2. tag会始终和对应的commit在一起，不会随着分支一起移动，可以看做不能动的分支。

3. 列出所有的标签：

   ```shell
   git tag  #按照字母顺序列出所有的标签
   v1.0
   v2.0
   git tag -l "v1.8.5*"  #以通配符查找标签
   v1.8.5
   v1.8.5-rc0
   v1.8.5-rc1
   v1.8.5.1
   v1.8.5.2
   ```

4. Git支持两种标签，通常建议创建附注标签，信息比较全面。

   1. 轻量（lightweight）标签，只是某个特定提交的引用。

   2. 附注（annotated）标签，是存储在git数据库中的一个完整对象，可以被校验。包含打标签者的名字，电子邮件，时间等。

5. 创建轻量标签：

   ```shell
   git tag v1.4-lw   #不需要 -a -m等选项，也不会打开编辑器。
   
   git show v1.4-lw      #只会看到提交的相关信息，而没有打标签者的信息。
   commit ca82a6dff817ec66f44342007202690a93763949
   Author: Scott Chacon <schacon@gee-mail.com>
   Date: Mon Mar 17 21:52:11 2008 -0700
   changed the version number
   ```

6. 创建附注标签：

   ```shell
   git tag -a v1.4 -m "my version 1.4"  #-a表示创建附注标签，-m表示标签信息，如果没有使用-m，则会打开编辑器要求输入。
   
   git show v1.4   #查看标签的详细信息
   tag v1.4
   Tagger: Ben Straub <ben@straub.cc>   #打标签者
   Date: Sat May 3 20:19:12 2014 -0700  #日期和时间
   my version 1.4                       #标签信息
   commit ca82a6dff817ec66f44342007202690a93763949  #对应的提交
   Author: Scott Chacon <schacon@gee-mail.com>      #提交的作者
   Date: Mon Mar 17 21:52:11 2008 -0700             #提交的时间
   changed the version number                       #提交的信息
   ```

7. 也可以对过去的提交打标签：

   ```shell
   git tag -a v1.2 9fceb02     #9fceb02是某个提交的部分校验和
   ```

8. 默认情况下，除非显式推送标签，否则git push不会将本地标签推送到远程仓库上。推送标签后，其他人从远程仓库拉取时，也会看到这些标签。

   ```shell
   git push origin v1.5   #推送v1.5标签到远程仓库，这样远程仓库也会出现一个v1.5，指向相同的提交对象。也可以使用 --tags来推送所有不在远程仓库的本地标签。该选项并不区分轻量或附注标签。
   ```

9. 删除本地标签：

   ```shell
   git tag -d v1.4-lw
   Deleted tag 'v1.4-lw' (was e7d5add)
   ```

10. 上述命令并不会从远程仓库删除标签，要删除的话应使用以下两个命令中的任意一个：

    ```shell
    git push origin :refs/tags/v1.4-lw   #删除远程仓库origin中的v1.4-lw 标签。本质上是将:前面的空标签名推送到origin上，变相地删除了该标签。
    To /git@github.com:schacon/simplegit.git
    - [deleted] v1.4-lw
    
    git push origin --delete v1.4-lw   #删除远程仓库origin中的v1.4-lw 标签
    ```

11. 如果想要查看某个标签所指向的文件版本，也就是该标签对应的提交对象的版本。可以使用以下命令，但这会使仓库处于“分离头指针（detached HEAD）”的状态，因为此时HEAD没有指向分支。

    ```shell
    git checkout v1.0
    Note: switching to 'v1.0'.
    
    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by switching back to a branch.
    
    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -c with the switch command. Example:
    
      git switch -c <new-branch-name>
    
    Or undo this operation with:
    
      git switch -
    
    Turn off this advice by setting config variable advice.detachedHead to false
    
    HEAD is now at c2de97f delete README    #HEAD指针目标指向c2de97f这个提交对象。
    ```

12. 分离HEAD指针

    ```shell
    cat .git/HEAD                #默认情况下，.git/HEAD文件内容为一个分支的文件路径
    ref: refs/heads/master
    cat .git/refs/heads/master   #master分支指向7de2f1提交对象。
    7de2f188fc74c4a0ef194c81aac3a6f664ca82a8
    #如果处于分离头指针的状态时，.git/HEAD文件的内容为提交对象的SHA-1值。
    cat .git/HEAD
    c2de97f9eb72d6828f65a043387332486cfca698
    ```

13. 在“分离头指针”状态下，如果你做了某些更改然后提交它们，标签不会发生变化， 但你的新提交将不属于任何分支，并且将无法访问，除非通过确切的提交哈希才能访问。 因此，如果你需要进行更改，比如你要修复旧版本中的错误，那么通常需要创建一个新分支：

    ```shell
    git checkout -b version2 v2.0.0   # -b 表示如果如果该分支不存在就创建一个
    Switched to a new branch 'version2'
    ```

14. 别名，可以通过git config为git的命令设置别名，只是简单地替换。

    ```shell
    git config --global alias.co checkout        #今后输入git co回车，就会自动执行git checkout命令。
    git config --global alias.last 'log -1 HEAD' #显示最后一次提交
    git config --global alias.visual "!gitk"     #!开头表示外部命令
    #也可以在配置文件.gitconfig中添加如下内容：
    [alias]
    	st = status
    	lg = log --oneline --decorate --graph --all
    ```

# 底层原理

1. Git本质上是一个内容寻址文件系统，并在此基础上提供了一个版本控制系统的界面。早期的Git更侧重于文件系统，用户界面做的不是很好，现在已经很好了。

2. Git中除了一些checkout，branch，remote等这些上层命令，还包括许多底层命令。这些命令被设计成可以和Unix命令行风格连接在一起使用。多数底层命令并不面向最终用户，更适合作为新工具的组件和自定义脚本的一部分。

3. Git中的三种对象：

   1. blob 数据对象
   2. tree 树对象
   3. commit 提交对象

4. 提交动作是对于整个项目或者是暂存区来说的，而已修改和已暂存指的是单个文件。

5. 之所以有暂存区这个概念，是因为以前的版本控制系统图形界面的比较多，在提交时可以勾选要提交哪些文件，而Git主要是基于命令行的，因此需要一个中间区域来记录。

6. 一般不会对一个文件修改一次就建立一个版本，一般来说积累到一定量的修改后，才会建立一个版本。这一系列的修改都放在暂存区。将暂存区的内容提交才会生成一个新的版本。

7. 工作流程：在工作区中修改→每次的修改都会记录到暂存区中→积累到一定量后，提交到版本库。

8. 通常有两种方法来获取Git项目仓库：

   9. 将一个尚未进行版本控制的本地目录(不一定是空目录)转化为git仓库。需要进入该目录运行git init来初始化仓库，也就是新建一个.git文件夹。

   10. 从其他服务器上Clone一个已经存在的仓库。不用创建并进入同名目录，

9. .git的文件夹如下，如果想备份或复制一个版本库，只需将此目录拷贝至另一处即可。

   ```shell
   hooks/       #包含客户端或服务端的钩子脚本,钩子脚本就是回调函数，可以设定在动作的前后进行操作
   info/        #包含一个全局性排除文件，用于放置那些不希望被记录在.gitignore中的忽略模式
   logs         #保存日志信息
   config       #包含项目特有的配置选项
   description  #显示对仓库的描述信息，供Gitweb使用
   HEAD         #指示目前被检出的分支
   index        #保存暂存区的信息，新仓库没有这个文件
   objects/     #存储所有的数据内容
   refs/        #存储所有指向数据(分支，远程仓库，标签)的提交对象的指针
   ```

10. Git的核心是一个键值对的数据库，hash算法是SHA-1。向Git中插入任何类型的数据，都会返回一个唯一的键，通过该键可以在任意时刻取回该数据。

11. ```shell
    echo "test content" |git hash-object -w --stdin		#     -w表示将对象写入到数据库中。如果没有--stdin则需要给出文件路径。这一步会将数据直接写入到数据库中，跳过了暂存区。
    d670460b4b4aece5915caf5c68d12f560a9fe3e4    #内容的hash值。
    find .git/objects/ -type f      #只查看该目录下的文件
    .git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4  #系统会在.git/objects目录下创建一个d6的文件夹，文件名为后续的hash值，内容是经过压缩过的 原数据+头部信息。
    ```

12. 需要注意的是，SHA-1值并非该文件的校验和，而是压缩前数据的校验和。git通过将数据的校验和保存为文件的文件名的方式来记录，将来可以通过SHA-1值找到对应的文件，然后解压即可获得之前保存的数据。可以这么做的前提是文件的文件名和内容是分开存储的，目前的所有文件系统都是这么做的。

13. 该文件的内容经过了压缩，想要还原使用如下命令：

14. ```shell
    git cat-file -p d67046    #-p可以查看文件的内容。可以用简写的SHA-1值,可以按tab提示，不重复就行。
    test content
    git cat-file -t d67046    #-t可以查看对象的类型
    blob        #数据对象
    ```

15. 一串SHA-1值，不仅标识一个键，还表示一个具体的文件，在.git/objects中，还表示特定的git对象。

16. 无论是文件还是内容，存储到Git数据库中都是blob类型的，就是键值对。

17. Git使用快照而不是增量，例子如下：

    1. 新建文件，hash一下，数据库中会生成一个新的对象
    2. 然后修改文件，再hash一下，又会生成一个新的对象。
    3. cat-file查看第二个对象，显示的不是增量内容。而是hash时的快照。

18. 每一次的改动后hash-object都会生成一个Git对象，存储在.git/objects。

19. 一个Git对象对应于一个文件的一个状态。一个文件经历过多次修改，就会有多个对象。

20. Git对象并没有保存文件名，只保存了文件的内容，文件名保存在所在的目录文件中，保存目录文件需要使用树对象。

21. 记住文件的每一个版本并不现实，因为文件的改动比较频繁，只需要记住项目的版本即可。

22. 树对象存储目录项，数据对象存储文件内容。一个树对象包含了一条或多条树对象记录（entry），每条记录含有一个指向数据对象或子树对象的SHA-1指针，以及访问模式，文件名，类型等信息。某项目中当前对应的最新树对象可能是这样的，

    ```shell
    git cat-file -p master^{tree}  #master^{tree}表示master分支上最新的提交所指向的树对象，仓库中一共包含2个文件，一个目录。
    100644 blob a906cb2a4a904a152e80877d4088654daad0c859 README   #文件，访问权限为644，对应的数据对象SHA-1值为a906cb
    100644 blob 8f94139338f9404f26296befa88755fc2598c289 Rakefile #文件
    040000 tree 99f1a6d12cb4b6f19c8655fca46c3ecf317074e0 lib      #目录
    
    git cat-file -p 99f1a6  #lib目录中只有一个文件
    100644 blob 47c6340d6459e05787f644c2447d2595f5d3a54b simplegit.rb
    ```

23. Git通过某一时刻的暂存区所表示的状态创建并记录一个树对象。可以通过update-index暂存一些文件创建一个或更新暂存区，并通过write-tree生成树对象。

    ```shell
    echo "version 1" > test.txt #创建test.txt文件
    git hash-object -w test.txt  #获取该文件的SHA-1值，并将该文件保存为blob对象。如果这里没有-w选项的话，后面write-tree会遇到致命错误。
    83baae61804e65cc73a7201a7252750c76066a30
    
    git update-index --add --cacheinfo 100644 83baae61804e65cc73a7201a7252750c76066a30 test.txt   # --add 将一个未被Git追踪的文件添加到缓存区
      # --cacheinfo 文件模式 git对象的SHA-1值 路径名     直接将相关信息插入到index文件中。这命令并不会检查路径名的存在或有效与否。
    
    #此时运行git status会显示test.txt文件已暂存，等待commit。
    #如果给了一个错误的sha-1的值，则会认为该文件又被修改了，所以才会和给定的sha-1值对不上。
    #如果给定的是一个不存在的文件名test1.txt，则会认为对应的文件test1.txt已经被删除了。同时也不会追踪test.txt文件。
    
    git ls-files -s     #查看暂存区的内容。
    100644 d9b5ce2c5fef8492db4a42d6be37a2b3ac393b05 0	test.txt
    git write-tree      #为暂存区生成一个树对象，放到版本库中。
    d8329fc1cc938780ffdd9f94e0d364e0ea74f579
    git cat-file -p d8329f
    100644 blob 83baae61804e65cc73a7201a7252750c76066a30    test.txt
    #可以看出来tree对象存储的是该目录下文件或文件夹的hash指针。
    git cat-file -t d8329f
    tree
    git ls-files -s	    #生成树对象的时候，不会清空暂存区
    100644 d9b5ce2c5fef8492db4a42d6be37a2b3ac393b05 0	test.txt 
    ```

24. 此时修改test.txt的内容，创建一个新的文件new.txt，然后再暂存这俩文件，再提交。

25. ```shell
    echo 'version 2' > test.txt #修改test.txt文件
    git hash-object -w test.txt #再对当前的test.txt文件创建的新的blob对象，注意，并不会删除掉旧的test.txt对应的blob对象。
    1f7a7a472abf3dd9643fd615f6da379c4acb3e3a
    git update-index --cacheinfo 100644 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a test.txt #因为test.txt文件已经被追踪，因此不需要再使用--add选项。
    
    echo "new file" > new.txt      #创建一个新的文件
    git update-index --add new.txt #之前没有加入暂存区，所以要用--add。可以省略hash值，会自动计算并生成对应的blob对象。默认的权限为100644。
    
    git ls-files -s    #此时的暂存区
    100644 fa49b077972391ad58037050f2a75f74e3671e92 0       new.txt
    100644 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a 0       test.txt  #覆盖掉了同文件名的旧的记录
    
    git write-tree #生成项目的第二个版本
    0155eb4229851634a0f03eb265b69f5a2d56f341
    
    git cat-file -p 0155eb
    100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
    100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt
    
    #读入1个树对象到暂存区。
    git read-tree --prefix=bak d8329f
    
    git ls-files -s #查看暂存区
    100644 83baae61804e65cc73a7201a7252750c76066a30 0       bak/test.txt #bak目录下的test.txt文件
    100644 fa49b077972391ad58037050f2a75f74e3671e92 0       new.txt
    100644 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a 0       test.txt
    
    git write-tree #项目的第三个版本
    3c4e9cd789d88d8d89c1073707c3585e41b0e614
    
    git cat-file -p 3c4e9c #包含了两个文件和一个目录
    040000 tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579    bak
    100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
    100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt
    ```

26. 树对象已经能够标识项目的版本了，但是如果想要访问三个版本的内容。则需要使用hash值。除此之外树对象无法记录保存作者，时间，提交注释等相关信息，因此出现了对树对象的进一步封装，也就是提交对象。

27. ```shell
    echo 'first commit' | git commit-tree d8329f   #生成一个提交对象，接受一个树对象的hash值。
    91115056f7e148e5d0a7b37281cfd81c46bc6216  #这里的SHA-1值受提交时间和作者信息的影响，一般不会相同。
    git cat-file -p 911150
    tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579 #该提交对象所绑定的tree对象
    author zj <747056333@qq.com> 1659285651 +0800
    committer zj <747056333@qq.com> 1659285651 +0800
    
    first commit
    
    git cat-file -t  911150  #类型为commit
    commit
    
    #生成第二个提交对象，并指定第一个提交对象be4c68作为他的父对象。
    echo "second commit" | git commit-tree 0155eb -p 911150
    8534308db0bae232cb5d2adae255abb1720eb985
    
    git cat-file -p 853430
    tree 0155eb4229851634a0f03eb265b69f5a2d56f341    #树对象
    parent 91115056f7e148e5d0a7b37281cfd81c46bc6216  #父对象，也就是first commit提交对象。
    author zj <747056333@qq.com> 1659285849 +0800
    committer zj <747056333@qq.com> 1659285849 +0800
    
    second commit
    
    echo 'third commit' | git commit-tree 3c4e9c -p 853430  #第三次提交
    cc647a75d59355b5cf648a8ede6dcc8b67d90dbd
    
    git cat-file -p cc647a
    tree 3c4e9cd789d88d8d89c1073707c3585e41b0e614
    parent 8534308db0bae232cb5d2adae255abb1720eb985
    author zj <747056333@qq.com> 1659285929 +0800
    committer zj <747056333@qq.com> 1659285929 +0800
    
    third commit
    
    git log  #此时运行git log看不到任何的commit，需要更新当前分支的head的值，是指指向我们的commit对象。
    fatal: your current branch 'master' does not have any commits yet
    
    git update-ref refs/heads/master cc647a     #将当前分支master指向最后的一个提交对象。
    
    git log
    commit cc647a75d59355b5cf648a8ede6dcc8b67d90dbd (HEAD -> master)
    Author: zj <747056333@qq.com>
    ......
    ```

28. 正常的操作是，每一次write-tree后，都应该生成一个提交对象，做好注释。后一次的提交对象也应该使用-p选项，指定他的父提交对象SHA-1值，这样构成一个提交对象的链。

29. 真正代表项目的一个版本的是提交对象，不仅包含了项目的文件内容，还包含了提交时的信息。

30. Git对象的存储例子，所有的git对象均以这种方式存储，不同的地方是头部信息可能为tree或commit。数据对象的内容可以是任意的，而树对象和提交对象的内容有各自的形式。

    ```shell
    #假设要存储的字符串为 "what is up, doc?" 一共16个字符。
    #首先会构造一个头部信息，"blob 16\u0000"  blob表示这个对象是blob对象，后面一个空格，然后是内容的长度，最后是一个Unicode空字符。
    #然后将头部信息和原始数据拼接起来，并计算这一条内容的SHA-1校验和 即SHA-1("blob 16\u0000"+"what is up, doc?")，结果为bd9dbf5aae1a3862dd1526723246b20206e5fc37。
    #最后Git会使用zlib压缩头部信息和原始数据拼接的结果，然后将压缩后的数据写入到磁盘的文件中，文件储路径为.git/objects/bd/9dbf5aae1a3862dd1526723246b20206e5fc37。
    
    echo -n "what is up, doc?" |git hash-object --stdin  #可以看到和git计算的SHA-1值是一样。
    bd9dbf5aae1a3862dd1526723246b20206e5fc37
    ```

31. Git引用：就是一个具有简单名字文件，用来保存复杂的SHA-1值。引用应该保存在.git/refs目录下：

    ```shell
    .git/refs/heads  #其内的文件都是分支
    .git/refs/tags   #其内的文件都是标签
    cat .git/refs/heads/master
    cc647a75d59355b5cf648a8ede6dcc8b67d90dbd   #最后一个提交对象的SHA-1值
    #不提倡直接编辑引用文件，可以使用update-ref来完成这个工作：
    git update-ref refs/heads/test 853430  #会创建一个新的文件.git/refs/heads/test，内容就是853430的完整版。
    git log --pretty=oneline test
    8534308db0bae232cb5d2adae255abb1720eb985 (test) second commit
    91115056f7e148e5d0a7b37281cfd81c46bc6216 first commit
    ```

32. 使用git branch <分支名>来创建新分支时，底层就是执行update-ref，参数是当前分支最新提交的SHA-1值。

33. Git是通过.git/HEAD文件记录当前分支最新提交的SHA-1值。

    ```shell
    cat .git/HEAD
    ref: refs/heads/master  #通常情况下该文件的内容会是一个引用，也就是某个分支。当检出标签，提交，远程分支时，会处于分离头指针的情况下，HEAD的内容会是某个git对象的SHA-1值。
    git checkout test
    Switched to branch 'test'
    cat .git/HEAD
    ref: refs/heads/test  #会随着分支的切换而改变
    #不建议手动编辑该文件，可以使用git symbolic-ref来修改HEAD的内容
    git symbolic-ref HEAD refs/heads/test  #相当于checkout到test分支上。
    ```

34. 实际上Git还有第四种对象，标签对象。它非常类似于一个提交对象，区别在于它指向的不是树对象，而是一个提交对象。像是一个永远不会移动的分支，永远指向某个固定的提交对象。可以认为是给这个提交对象起了个简单地名字。

    ```shell
    git update-ref refs/tags/v1.0 853430  #创建一个轻量标签，不会创建新的git对象
    cat .git/refs/tag/v1.0
    8534308db0bae232cb5d2adae255abb1720eb985
    
    git tag -a v1.1 cc647a -m "version 1.1"  #创建一个附注标签
    cat .git/refs/tags/v1.1
    a1cc9a392e7eee50412201ebf79330f600145f1d  #创建了一个新的标签对象
    git cat-file -p a1cc9a
    object cc647a75d59355b5cf648a8ede6dcc8b67d90dbd  #打标签对象的SHA-1值
    type commit        #表示对一个commit对象打的标签。
    tag v1.1          
    tagger zj <747056333@qq.com> 1659371144 +0800
    
    version 1.1
    
    git cat-file -t a1cc9a
    tag  #tag对象
    ```

35. 可以对任意类型的Git对象打标签，例如在Git源码中，GPG公钥被添加为一个blob对象，并被打了个标签。Linux内核版本库中同样有不指向提交对象的标签对象，例如首个被创建的标签对象就是指向最初被引入版本库的那个树对象。linux内核直到2.6才开始使用git管理。

    ```shell
    git cat-file blob junio-gpg-pub   #查看GPG公钥
    ```

36. 第三种引用是远程引用，如果添加了一个远程服务器，并对它执行过push操作，Git会记录下最近一次push时每一个分支所对应的值，保存在.git/refs/remotes目录下。

    ```shell
    ls .git/refs/remotes/origin/  #每个服务器一个单独的目录。里边也有HEAD指针和master引用
    HEAD  master
    ```

37. 远程引用和本地分支的区别是，远程引用是只读的，虽然可以git checkout 到某个远程引用上，但是不会修改本地的HEAD文件。因此不能通过commit来更新远程引用。Git使用这些远程引用来记录服务器上各分支最后的状态。

38. 包文件：

39. 对于大文件进行一次小修改，分别提交，前后两次会对该文件生成2个blob对象，而这两个对象的大小近似。这会很浪费存储空间。

    ```shell
    curl https://raw.githubusercontent.com/mojombo/grit/master/lib/grit/repo.rb > repo.rb
    git add repo.rb
    git commit -m "added repo.rb"
    git cat-file -p master^{tree}
    100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
    100644 blob 033b4468fa6b2a9547a70d88d1bbe8bf3f9ed0d5    repo.rb
    100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt
    git cat-file -s 033b44  #查看对象的大小，22k左右
    22044
    echo "# testing" >> repo.rb
    git commit -am "modified repo.rb"
    $ git cat-file -p master^{tree}
    100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
    100644 blob b042a60ef7dff760008df33cee372b945b6e884e    repo.rb
    100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt
    git cat-file -s b042a6  #对象增加了写内容
    22054
    #可以看到两个blob对象实际都被压缩到了7k左右。
    ls -l .git/objects/b0/42a60ef7dff760008df33cee372b945b6e884e
    -r--r--r-- 1 ZhangJian 197121 6893 Aug  3 00:19 .git/objects/b0/42a60ef7dff760008df33cee372b945b6e884e
    
    ls -l .git/objects/03/3b4468fa6b2a9547a70d88d1bbe8bf3f9ed0d5
    -r--r--r-- 1 ZhangJian 197121 6886 Aug  3 00:17 .git/objects/03/3b4468fa6b2a9547a70d88d1bbe8bf3f9ed0d5
    ```

40. 这种存储方式Git称之为松散lose对象格式，但是Git会是不是地将多个对象打包成一个包文件，以节省空间。当版本库中有太多的松散对象，或手动执行git gc命令，或者向远程服务器推送时，Git都会进行打包。

    ```shell
    git gc
    Enumerating objects: 19, done.
    Counting objects: 100% (19/19), done.
    Delta compression using up to 6 threads
    Compressing objects: 100% (14/14), done.
    Writing objects: 100% (19/19), done.
    Total 19 (delta 1), reused 0 (delta 0), pack-reused 0
    find .git/objects/ -type f   #此时objects目录下大部分对象都不见了，在pack目录下出现了一对新的文件。
    .git/objects/info/commit-graph
    .git/objects/info/packs
    .git/objects/pack/pack-4ddc67782cebaff3720d8422c59c971c87bf2de6.idx
    .git/objects/pack/pack-4ddc67782cebaff3720d8422c59c971c87bf2de6.pack
    
    #查看包文件内的对象
    git verify-pack -v .git/objects/pack/pack-4ddc67782cebaff3720d8422c59c971c87bf2de6.idx
    ...
    b042a60ef7dff760008df33cee372b945b6e884e blob   22054 5799 1538
    033b4468fa6b2a9547a70d88d1bbe8bf3f9ed0d5 blob   9 20 7337 1 b042a60ef7dff760008df33cee372b945b6e884e 
    ...
    non delta: 18 objects
    chain length = 1: 1 object
    .git/objects/pack/pack-4ddc67782cebaff3720d8422c59c971c87bf2de6.pack: ok
    ```

41. 如果此时还有对象，则可能是单独创建的为被任何提交对象记录的悬空dangling对象。

42. Git 在打包对象时，会查找命令和大小相近的文件，并只保存文件不同版本之间的差异内容。git往往保存新版本的文件，旧文件则以相对于新文件的修改保存。因为新文件会被经常使用到，这样会加快读取速度。

43. 引用规范：

44. 添加一个远程仓库，会在.git/config文件中添加一个小节。

    ```shell
    git remote add origin https://github.com/schacon/simplegit-progit
    cat .git/config 
    [remote "origin"]
            url = https://github.com/schacon/simplegit-progit
            fetch = +refs/heads/*:refs/remotes/origin/*  #用于获取操作的引用规范
    ```

45. 引用规范的格式由一个可选的+和其后的<src>:<dst>组成。其中src是一个模式，代表远程版本库的引用，dst是本地跟踪的远程引用的位置。

46. 

47. 

# 高层命令

1. 分为CURD     新增，修改，重命名删除，查询

2. 一个文件重复add，则会生成多个Git对象。不过暂存区的内容会被顶替到。提交前的最后一次add会被记录到tree对象，然后封装成commit对象。

8. 一个完整的流程最少包含1个git对象，1个tree对象，1个commit对象。

9. 一次提交，只会有1个tree对象，1个commit对象，但是可以有很多的git对象。

10. commit命令把暂存区的内容生成一个tree对象，然后打包，生成一个commit对象。

11. ```shell
    git commit -m "First commit"
    [master（根提交） dd955ca] First commit
     1 file changed, 1 insertion(+)
     create mode 100644 test.txt
    git status
    位于分支 master
    尚未暂存以备提交的变更：
      （使用 "git add <文件>..." 更新要提交的内容）
      （使用 "git restore <文件>..." 丢弃工作区的改动）
    	修改：     test.txt			#可以看出commit不会主动add修改暂存区。
    修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
    git ls-files -s
    100644 915c628f360b2d8c3edbe1ac65cf575b69029b61 0	test.txt
    git cat-file -p 915c
    test v1
    
    ```

12. 

13. ```shell
    ~/.../.git/objects >>> tree
    ├── 72
    │   └── 203871fa4668ad777833634034dcd3426879db	（tree对象）
    ├── 91
    │   └── 5c628f360b2d8c3edbe1ac65cf575b69029b61	（blob对象，文件的第一个版本）
    ├── dd
    │   └── 955cae0853c672877f67c30be88dea9cfcedaa	（commit对象，项目的第一个版本）
    ```

14. 在写代码的时候，如果觉得以后可能会想要回到文件的当前状态，则可以add一次，因为此时就会生成一个Git对象，到时候可以用于回复文件。如果觉得需要给项目保存一个版本，则可以commit。

15. add命令是hash-object 和update-index这两个命令的集合。所有修改了的文件才会生成新的git对象，没有修改的文件hash值不变，git对象也和原来一样。

18. commit命令是write-tree和commit-tree这两个命令的集合。

22. git rm --cached test.txt              将test.txt变为未跟踪的状态。

31. git通过hash值来判断文件的内容有没有被修改，不参考文件的修改日期。

14. 如果真实删除文件：此时版本库中不包含test.txt文件，不过之前的该文件的git对象仍然会保留。commit对象的树对象中不包含test.txt文件的git对象了。


# 分支功能

1. 使用git协作开发时，一般一个人一个分支。每个人自己也可以在自己的主分支上再开分支。

2. 使用分支的目的是为了将开发工作从主线中分离出来，避免影响主线。在很多的版本控制系统（例如SVN，不过SVN的分支只能在服务器上创建）中，创建分支这是一个低效的过程，常常需要创建一个源代码的副本，而git的分支模型极其高效。

3. Git的分支就是一个指向某个提交对象的活动指针。

4. 默认是master分支，也叫主分支。master分支并不是一个特殊的分支，只不过是init的时候默认的分支就是master。

5. 每一次commit时，master指针不断变换，总是指向最新的那次commit对象。

6. .git/HEAD文件指示当前的分支。

7. ```shell
   ~/git-test/.git >>> cat HEAD
   ref: refs/heads/master
   ~/git-test/.git >>> cat refs/heads/master
   bcc1c4e5b5d8c0e6c4d9cd0e51fa3e628a593184      #这个是最新的commit对象的hash值。
   git log --oneline
   bcc1c4e (HEAD -> master) rename mv.txt
   
   git branch test      #创建一个新的分支，指向当前分支最新的commit对象。并不会自动切换到该分支上。
   git log --oneline
   bcc1c4e (HEAD -> master, test) rename mv.txt
   ```

8. 如果此时再进行提交，则HEAD指向的master分支会指向最新的commit对象，test分支则还是指向之前的那个分支。

9. ```shell
   git checkout test
   切换到分支 'test'
   bcc1c4e (HEAD -> test, master) rename mv.txt
   ```

10. master分支上运行的是稳定的代码，如果要新增功能，则应该新建一个分支，然后切换到该分支去，进行开发，之后的commit都在新分支下，如果新功能完善后，可以合并到master分支。如果分支失败，要记得删除，否则占空间。

11. 在测试分支上操作，提交。

12. ```shell
    echo "test v1" >test.txt
    git add .
    git commit -m "add test.txt"
    git log --oneline
    2797b92 (HEAD -> test) add test.txt
    bcc1c4e (master) rename mv.txt
    ```

13. 分支一般只从master上创建。

14. ```shell
    git branch     #显示当前的分支 *表示HEAD指向的，活动分支。
      master
    * test
    
    git checkout master  #切换到分支 'master'
    
    #查看所有分支的修改历史。如果切换到旧的分支，则在log中默认不显示新分支的修改历史，使用以下命令。
    git log --oneline --decorate --graph --all 。
    
    git branch -d test
    error: 分支 'test' 没有完全合并。     #也就是说该分支的修改没有被其他分支继承。
    如果您确认要删除它，执行 'git branch -D test'。    #对于没有合并的分支，删除要用-D
    git branch -D test
    已删除分支 test（曾为 2797b92）。
    ```

15. 新建一个分支，并指向特定的commit对象。用于版本穿梭。

16. ```shell
    git branch hah 9a3e6ac
    
    * bcc1c4e (HEAD -> master) rename mv.txt
    ...
    * 9a3e6ac (hah) hahha
    * aaf0f30 test.txt new
    * 18d1fba First commit
    
    ls
    mvv.txt
    git checkout hah	#切换到刚才新建的分支
    切换到分支 'hah'
    ls
    test.txt            #文件的修改日期不是原来的了。
    ```

17. 分支切换会改变工作目录中的文件，修改HEAD指针，工作目录会恢复到该分支最后一次提交时的状态。不会修改暂存区。

18. ```shell
    git chechout -b test       #新建test分支，并切换到该分支。
    ```

19. 因此每次切换分支前都应该使用git status查看当前分支的修改有没有被提交。

20. 在切换分支时，

    1. 如果当前分支有未暂存的修改，或未提交的暂存，且该文件从未被提交过，则可以切换分支，因为此时git不知道该文件到底属于那个分支，该文件会保留到任何分支，因为git认为该文件可以在任意分支被提交。

    2. 如果该文件在任意分支被提交过一次，且有未暂存的修改，或未提交的暂存，则不可以切换分支，必须提交分支，处理完毕后才可以切换。

21. 如果master分支的代码出现bug需要修复，则应该新增一个分支iss53，进行修改，如果在修改的过程中，出现了一个紧急的问题，那么就应该先commit 分支iss53，切回主分支，然后创建一个新的分支hotfix，用于修复紧急问题。此时git的提交对象链出现分叉。

22. ![image-20201203104616856](Git.assets/image-20201203104616856.png)

23. 合并是有方向的，应该是主分支合并修改分支，父分支合并子分支。

24. 

25. ![image-20201203105559321](Git.assets/image-20201203105559321.png)

26. 如果此时hotbug修复完成，想要合并到master分支上线：

    ```shell
    git checkout master
    切换到分支 'master'
    git merge hotbug
    更新 5db99bd..e8f1a14
    Fast-forward	#父分支合并子分支，可以快进合并，将master指向hotbug指向的commit对象即可。
     a.txt | 1 +
     1 file changed, 1 insertion(+)
    ```

27. ![image-20201203105854106](Git.assets/image-20201203105854106.png)

28. 此时hotbug分支可以删除了，删除hotbug后，分支如下。

29. ![image-20201203110140823](Git.assets/image-20201203110140823.png)

30. 

31. 此时再对iss53的问题进行修改，提交一次，查看log可以发现，iss53跑到master上面了，因为它的链比较长。

32. ![image-20201203110631196](Git.assets/image-20201203110631196.png)

33. 如果iss53也修复好了，需要合并到主分支，此时不能再进行快速合并。因为iss53是从之前的主分支延伸过来的，他也具有hotbug的问题。

34. iss53如果修改了hotbug修改的同一行的内容。合并就会出现冲突，而快进合并不会出现分支。

35. 合并出现冲突，在a.txt中

36. ![image-20201203111350154](Git.assets/image-20201203111350154.png)

37. ![image-20201203151139549](Git.assets/image-20201203151139549.png)

38. 打开冲突的文件a.txt，删除不需要的行，留下有用的行。

39. ```shell
    a.txt v1
    <<<<<<< HEAD
    a.txt v2
    =======
    a.txt v2 for iss53
    >>>>>>> iss53
    ```

40. 然后add commit即可。解决冲突之后，可以删除iss53分支。

41. 查看分支历史如下。

42. ![image-20201203151053425](Git.assets/image-20201203151053425.png)

43. 一般合并完分支之后，需要推送到远程仓库，更新线上的功能。

44. 一般开发有一个主线分支master，还有一个开发分支develop。不同团队有各自的分支，团队内的人员有各自的分子，每个人在开发新功能的时候也会开分支，开发完善之后，再合并到自己的分支，自己的分支会定期合并到团队的分支，团队的分支会定期合并到开发分支中，开发分支定期合并到主分支中。

45. ![image-20201203151919778](Git.assets/image-20201203151919778.png)

46. .git/refs/heads保存着分支及其对应的提交对象。分支名就是文件名，内容就是提交对象的hash值。

47. HEAD指针存放在.git/HEAD文件中。

    ```shell
    cat HEAD
    ref: refs/heads/master
    ```

# 存储和撤销

1. 有时候，当在一个分支上进行了一定的工作，所有的东西都进入了混乱的状态，而此时想要切换到另一个分支进行别的工作，但是又不想为这些为晚上的工作使用一次提交。

2. ```
   git stash			#将当前状态压入该分支对应的栈中。
   保存工作目录和索引状态 WIP on master: 99cb4bc fix conflict
   git stash list
   stash@{0}: WIP on master: 99cb4bc fix conflict
   git st			工作区干净。git帮助用户提交了，不过不会记录在历史记录中。
   位于分支 master
   无文件要提交，干净的工作区
   ```

3. 使用git log看不到，但是使用--all参数就可以看到。

4. 一般进入一个分支，要先看下栈里边有没有未完成的工作。

5. git stash apply 会应用栈顶元素，还原入栈时的状态，但是不会删除他。如果末尾加上元素名（例如stash@{0}），则表示恢复该元素对应的状态，

6. git stash drop 元素名        移除栈中对应的元素。

7. git stash pop 元素名         应用元素并删除。    最常用的

8. 一般栈中只存放一个元素，不宜复杂。

9. 撤销的三个级别：

   1. 撤销文件未暂存的修改：git restore b.txt

      ```
      git st
      位于分支 master
      尚未暂存以备提交的变更：
        （使用 "git add <文件>..." 更新要提交的内容）
        （使用 "git restore <文件>..." 丢弃工作区的改动）
      	修改：     b.txt
      
      修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
      cat b.txt
      b.txt v1
      b.txt v2
      b.txt v3
      git restore b.txt     #也可以用  git checkout -- b.txt
      git st
      位于分支 master
      无文件要提交，干净的工作区
      cat b.txt
      b.txt v1
      b.txt v2
      ```

   2. 撤销文件的暂存状态，使之变为已修改的状态，不过工作目录中文件的内容不会变，但是暂存区的文件会变回文件上一次暂存的状态：git restore --staged b.txt

      ```
      git add .
      git st
      位于分支 master
      要提交的变更：
        （使用 "git restore --staged <文件>..." 以取消暂存）
      	修改：     b.txt
      
      git restore --staged b.txt
      cat b.txt
      b.txt v1
      b.txt v2
      b.txt v3
      git restore --staged b.txt
      git st
      位于分支 master
      尚未暂存以备提交的变更：
        （使用 "git add <文件>..." 更新要提交的内容）
        （使用 "git restore <文件>..." 丢弃工作区的改动）
      	修改：     b.txt
      
      修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
      git ls-files -s
      100644 cc69edf97d2bafc195735bc0e28998de089790c0 0	a.txt
      100644 540515ccf0cf8d304906938e13863a3171531297 0	b.txt
      git cat-file -p 5405
      b.txt v1
      b.txt v2
      ```
   
   3. 覆盖之前的提交

      ```
      git add .
      git commit -m "b.txt 3line"
      [master 6d9b58d] b.txt 3line
       1 file changed, 1 insertion(+)
      git st
      位于分支 master
      无文件要提交，干净的工作区
      ```
   
10. git reflog 显示详细的历史记录，撤销动作不会显示在git log中，但是会显示在reflog中。只要head变化，就会记录。

11. 如果对于提交时的内容不满意，可以修改文件的内容，添加到暂存区，然后可以用git commit --amend -m "" 来覆盖原来的提交，也可以修改注释。

12. 现在的状态

13. ![image-20201203183819918](Git.assets/image-20201203183819918.png)

14. amend之后

15. ![image-20201203184031146](Git.assets/image-20201203184031146.png)

16. reset

17. ```
    git reset --soft HEAD~       #将HEAD指针移动到当前HEAD指针的上一次提交对象上。最后的参数也可以是commit对象的hash值。
    ```

18. git reset 的操作和checkout不同，checkout是移动head指针到新的分支上，而reset是移动head和当前分支，指向新的commit对象，这里不涉及别的分支。本质上是撤销了上一次的commit命令。log中也看不到了。下一次再提交时，就会覆盖掉reset前的那个commit。

19. git commit --amend  就是git reset --soft HEAD~ 然后再git commit -a

20. --soft表示只移动head，不修改工作目录和暂存区。

21. ```
    git reset [--mixed] HEAD~       #默认参数是--mixed，修改head和暂存区，不修改工作目录
    git reset --hard HEAD~          #修改head，暂存区和工作目录
    ```

22. --hard是reset唯一危险的用法， 因为它会修改工作目录。因为如果此时存在未被git管理的文件，reset --hard之后，工作目录中的文件被强制覆盖。

23. 如果给reset制定一个路径参数，则不会修改head，只会修改暂存区和工作目录。只有--mixed后可以加路径。

24. ```
    git reset HEAD file.txt      如果不加文件名，则会全部回退。1个commit对象对应很多个对象，很多个文件。commit对象可以是任意的。
    就是用HEADcommit对象对应的file.txt文件的状态覆盖当前暂存区中的file.txt文件的状态。
    ```

25. checkout 和reset --hard的区别。

26. ![image-20201203204915431](Git.assets/image-20201203204915431.png)

27. git checkout commithash  \<filename\> 会修改暂存区和工作目录中的对应文件。

# 远程协作

1. 远程协作的基本流程：

   1. 项目经理创建空的GitHub远程仓库

   2. 项目经理创建本地仓库

   3. 项目经理为远程仓库配置别名和用户信息

      ```
      git remote add MyVimrc https://github.com/vpzz/MyVimrc.git    为远程仓库指定一个别名。
      git remote -v     #显示已配置的别名
      MyVimrc	https://github.com/vpzz/MyVimrc.git (fetch)
      MyVimrc	https://github.com/vpzz/MyVimrc.git (push)
      如果此仓库的信息和--global的不一样，则需要配置一下。
      ```

   4. 项目经理推送本地项目到远程仓库

      ```
      git push MyVimrc master	输入远程仓库的别名和要提交的分支。则会提交该分支的最新版本到github。
      ```

   5. 团队成员克隆远程仓库

      ```
      git clone https://github.com/vpzz/MyVimrc.git     #clone不需要init和新建文件夹。
      ```

   6. 项目经理将团队成员加入到GitHub的团队中，允许他们Push。在项目的settings中的collaborators中，搜索GitHub用户的邮箱或者用户名，发出邀请，团队成员在邮箱或者打开邀请的链接，接受即可。![image-20201204100037409](Git.assets/image-20201204100037409.png)

   7. 团队成员推送commit到远程仓库

   8. 项目经理更新成员的提交到本地。git fetch 仓库别名，然后在本地分支master，merge远程跟踪分支。

3. clone到本地的文件夹名和远程仓库的仓库名相同。clone下来的仓库中自动会有远程仓库的别名，默认是origin。

4. 可以发现在log中，存在一个远程跟踪分支origin/master。

5. ![image-20201204100756961](Git.assets/image-20201204100756961.png)

6. 一共有三种分支：本地分支（本地仓库的状态），远程跟踪分支（本地认为的远程仓库的状态），远程仓库分支（仓库的标准状态）。

7. 远程跟踪分支要定期和远程仓库分支进行同步，以便接受其他成员的修改。是本地分支和远程分支中间的过渡点。

8. 在push和clone之后本地才会有远程跟踪分支。
