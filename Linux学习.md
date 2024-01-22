# Linux系统简介

## Unix和Linux的历史

1. Unix和Linux之间的关系像父子。

2. 最早是MIT,GE,AT&T的贝尔实验室合作开发的Multics系统，但是由于追求的目标过于庞大复杂，项目进度落后，计划流产。后来贝尔实验室的肯·汤普森在pdp7上写出了Unix操作系统。最早命名为Unics，和Multics对立，因为二者读音相似，所以就叫做Unix。后来美国国防部的ARPAnet项目中ncp网络协议不够好，被重写的TCP/IP协议替代。由于AT&T的主营业务是电信，所以Unix就不受重视，后来TCP/IP协议捆绑到Unix系统上，面向大学发行非商业的许可。

3. 后来肯·汤普森的同事丹尼斯·里奇根据B语言开发了C语言，二人又合伙重写了Unix（最初的Unix是用汇编语言写的）。提高了Unix的可移植性。二人因此获得图灵奖。

4. 1970年，UNIX诞生→1979年UNIX商业化→1984Richard Stallman发起了GNU计划→1987年，GCC发布→1991年，Linus发布linux内核。

5. Unix的主要发行版本如下，Solaris可以在Intel微机平台安装，其他的Unix系统则不然。

   ```shell
   系统名称       公司      硬件平台
   AIX            IBM      PowerPC      (该CPU被早年MAC电脑使用)
   HP-UX          HP       PA-RISC
   Solaris        Sun      SPARC        (Sun公司后来被Oracle收购)
   ```

6. Mac OS，BSD也是一个Unix的主流分支。Linux可以看做是类Unix系统。

7. Linux诞生于1991年，芬兰大学生林纳斯在学习操作系统课程时，接触到了Minix系统，该系统是教授参考了Unix来开发的，不过声明编写的时候没有看源代码。当时的Unix系统是收费的。但是教授拒绝接受他人对系统漏洞的修复。Minix就没有流行开来，Linus参考率Minix，自己开发了linux。意思是Linus的Unix。

8. Linux的吉祥物是企鹅。www.kernel.org 是内核的网站。2.x时代的时候次版本号如果是偶数，则表示该版本是稳定版，否则是开发版。到了3.x以后，此规定不适合。2.6版本的时间跨度最大，从03年到11年，从2.6.0到2.6.39。其中2.6.12是使用Git工具管理的第一个版本。

## 发行版

1. Linux的发行版基本可以按照软件安装方式来分为2类：Redhat系列和Debian系列。
2. Redhat公司的RHEL是企业版，Fedora是个人版，此处的个人版并不是企业版的缩水版，可以看做是开发版，存在很多新的功能，经过验证稳定的功能会被合并到RHEL中。CentOS和RHEL基本相同，是社区维护版，是社区根据RedHat公布的RHEL源码来自行编译发行的。
3. <img src="Linux学习.assets/1587640856355.png" alt="1587640856355" style="zoom:67%;" />
4. 常见的Linux发行版

   1. RHEL    RedHat Enterprise Linux，企业版的系统。
   2. CentOS，Community Enterprise Operating System，社区版，去掉了RHEL收费的部分。二者使用起来几乎一样。被RedHat 收购。
   3. Fedora，也是有RedHat研发的，面向桌面的，类似于Windows Server和Win7的关系。
   4. OpenSUSE，来自德国。
   5. Gentoo，可定制性高。
   6. Debian，在国外具有很高的认可度。和RHEl旗鼓相当。
   7. Ubuntu，衍生自Debian，对新款硬件兼容性强，常用的桌面系统。
5. KNOPPIX可以不用安装，放在光盘或者U盘，现在其他的Linux发行版也都有Live CD版本了。


# 基础

   1. 开源软件的自由：使用自由，修改自由，传播自由，收费自由，创建衍生品自由。开源软件并不要求一定免费，提倡通过后续的服务收费。

   2. 常见的开源许可证，License：GNU GPL（Linux内核），BSD，Apache，MPL（Mozilla项目使用），MIT（限制最少的）。

   7. RHEL6和7的管理差异
      
      1. RHEL7之前的初始进程都是init，管理服务使用service。
      2. RHEL7的初始进程为systemd，管理服务使用systemctl。一个是服务名称，一个是管理服务的工具。
      
   8. Linux中的文件扩展名是为了方便用户识别文件类型，对于程序来说并没有实际的意义。不过有些程序会只读取特定后缀名的文件。

   9. Linux可以分为以下4个部分：linux内核，GNU工具链，图形桌面环境，应用软件。

10. 全世界的程序员都可以为linux内核贡献代码，是否并入内核取决于linus。

11. 内核不仅管理物理内存，还创建和管理虚拟内存（会使用硬盘上的交换空间swap来扩展可以使用的内存）。

   12. 机房里可能只有一台显示器，那个服务器需要维护，才会插上显示器维护。

13. Linux对主机名不敏感，可以重复，Windows则不然。

14. root用户的密码可以不符合密码原则，其他用户则必须符合。

   15. 以前在内核中插入驱动程序的方法只能是重新编译内核，每次添加新设备都要重新编译一次内核。这种方法会造成内核臃肿，效率低下。另一种方法是将驱动程序编译为内核模块，需要使用时插入，而不用重启内核。当设备不用时，可以将模块中内核中移走。

13. 设备文件有三类：

    1. 字符设备：每次只能处理1个字符，大多数的调制解调器和终端都是这类设备。
    2. 块设备：每次能处理一大块数据，例如硬盘。
    3. 网络设备文件：采用数据包的形式来收发消息，包括各种网卡和一个特殊的回环设备（允许进程使用网络协议跟自身通信）。

14. linux为系统上的每个设备都创建一个称为节点的特殊文件，与设备的所有通信都通过设备节点来完成。每个节点有内核提供的唯一的标识，一个主设备号，一个次设备号。类似的设备被划分到同一个主设备号下，次设备号用于标识主设备组中的特定设备。

15. GNU工具链中供Linux使用的核心工具称为coreutils软件包，主要提供三种功能：处理文件，操作文本，管理进程。bash(Bourne again shell)由GNU项目组负责开发，被当做Unix标准shell-Bourne shell的替代品。

16. 不同的shell有不同的特性，有的利用创建脚本，有的利用管理进程：

17. tcsh将C语言中的一些元素引入到shell中。

18. korn增加了对关联数组和浮点数的支持。

19. zsh结合了bash，tcsh，korn的特性。

   20. Android系统的底层就是Linux，可以在手机上安装ssh的服务器端软件，使用XShell通过ssh连接。

   21. 工作站和个人计算机在设计目的上有着区别，工作站要求稳定不宕机，运行完全正确，这也是它价格高的原因。

   22. 容量大小一般用二进制，速度大小一般用十进制，例如1GB=1024\*1024\*1024B，1GHz=1000\*1000\*1000Hz。网络传输方面一般使用位每秒作为单位，例如通常说的100M网速指的是100Mbit/s也就是12.5MB/s。硬盘厂商一般会以10进制来计数，例如一块500GB的硬盘，实际的大小有500\*1000\*1000\*1000B=466GB。这样做的原因是因为组成硬盘的最小单位是扇区，也就是512B，通常硬盘容量为多少个扇区，因此会用十进制来计数。

   23. CPU的频率表示它每秒钟的时钟周期数。CPU性能=IPC(CPU每一时钟周期内所执行的指令多少)×频率(一秒钟有多少时钟周期)。这也只能在同类型的CPU中比较，因为RISC和CISC的CPU一条指令的工作量不同。

   24. 早期的CPU通过北桥芯片和高速的设备例如内存和显卡相连接。不过由于他们之间的速度差异过大，而通信各方的工作频率又应保持一致，所以CPU厂商就在CPU内部再进行加速。于是就有了外频（CPU和外部组件协同工作的速度）和倍频（CPU内部相对于外频加速的倍数）。二者相乘才是CPU的真实频率。例如Intel Core 2 E8400的外频为333MHz，倍频为9，则频率为3.0GHz。

   25. 由于CPU的倍频是在出厂时就被锁死了，因此通常的超频指的是外频。

   26. 由于北桥芯片的瓶颈，现在的CPU都将它集成到了CPU内部，这样CPU可以直接和内存，显卡通信。也就没有了外频和倍频的概念，不过通过CPU-Z工具来查看的时候，还是可以看到的，例如外频变成了100MHz，倍频为30。

   27. 现在的CPU会在计算需求大的时候主动进行超频，同时CPU的频率是一直在变化的。计算量小的时候频率会很低，这样会极大地节约电量。

   28. CPU中的MMU（内存控制单元）是用来和内存交互的。它的频率和内存的频率是一致的，和CPU的频率无关。对于64位CPU来说每个时钟周期内可以传输的数据量为64位，这个称为总线位宽。

   29. CPU每次能够处理的数据量称为字长（Word size），这也是划分32位和64位CPU的主要依据。

   30. 内存通过系统总线带宽和CPU通信，显卡通过PCI-E的序列通道来和CPU通信。

   31. Intel 奔腾和赛扬分别被称为i586和i686，他们都是32位的。目前的64位CPU都被称为x86-64。目前很多程序都有对CPU级别进行限制，例如软件标注i586就表明它可以运行在i586及以上的平台上，包括最新的x86-64。如果标注了x86-64，那么不应给旧款奔腾赛扬处理器使用，容易出问题。

   31. 较高等级的硬件通常会兼容低版本的软件，例如x86-64平台，可以使用为i386，i686等平台编译的软件。

   32. CPU的超线程不同于操作系统的任务切换，本质上是一个内核内部有两份重要的寄存器，可以同时驻留两个程序，他们共同竞争运算单元。一个4核的CPU通过超线程技术，可以让操作系统检测到8个核，每个内核逻辑上分离。

   33. DDR的意思是Double Data Rate，即一个工作周期内可以进行两次数据的传输，类似于CPU的倍频。DDR2的倍频是4，DDR3的倍数是8。例如DDR2-800MHz的内部频率为200MHz，倍频为4。DDR3-1600的内部频率也是200MHz，倍频则为8。标准的DDR电压为1.5V，而笔记本上为了节能的需求，可以使用DDRL的规格，电压为1.35V。二者之间不通用，尺寸不同插不上。

   34. 两根内存条可以组建双通道，这样内存位宽就从64位变为了128位。双通道内存的读写是同步的。服务器中还提供三通道，四通道的内存。

   35. 对于服务器来说，内存的容量有时比CPU的速度还重要。

   36. 主板上的CMOS芯片记录着与主板相连的设备的配置信息和参数，他通过主板的电池供电，断电时仍然能够保持记录。BIOS只是一个程序，它在出厂时写入到了主板的一个只读存储器ROM上，不过现在通常是使用闪存flash或EEPROM，因此也是可以进行更新的。

   37. 计算机启动时，BIOS会读取CMOS中的信息来对设备进行配置。在BIOS设置界面的修改会保存到CMOS中。

   38. 固件firmware就是固定在硬件上的控制软件，出厂时就被安装到ROM中的。BIOS就是一个固件。路由器中也有固件，升级固件可以提供更多的功能。

   39. 以前的显卡是单纯的用来显示的，内部的显存存放着要显示的画面数据。图形的处理是有CPU来完成的，后来的显卡内部继承了3D加速的芯片，因此又称为GPU。

   40. PCI-E使用的是类似管道的概念，PCI-E1.0中每条管道的带宽为250MB/s，管道越多（最多有16条，为x16），总的带宽就越高。常见的为PCI-E3.0x16，即16个通道，每个通道的带宽为1GB/s。

   41. Intel和Broadcom的网卡比较好。

   42. 有相当多的组件都已经集成到了主板上，例如网卡，声卡等。

   43. PCI-E通道：

       1. 现在的主板上已经整合了相当多的设备组件了，包括声卡，网卡，USB控制卡等。
       2. PCI-E接口在个人电脑上x16比较常见，而在服务器上，x8比较常见。
       3. CPU有支持PCI-E的通道上限数量。如果是16，则表示支持1个x16，或者2个x8，或者1个x8，2个x4。但是一般的主板上的PCI-E接口的都比这个多。主板上的PCI-E插槽离CPU最近的那个是和CPU直接相连的，一般给显卡用，其他的一般是和南桥芯片相连，南桥和CPU相连的DMI通道速度比PCI-E慢。
       4. 为了让所有的扩展卡都可以安装在主板上，因此都制作成x16的，而其中的通道数可能只有8或者4，其余的都是空的，没有金手指。一张x16的卡安装在x16的插槽上，如果这个插槽只有x4的电路，也可以使用，不过只有原来1/4的速度上限了。

45. 有时命令行程序会征求用户的意见，是否执行某项操作，一般用y或n来回答，其中大写的字母表示默认的选项，直接敲回车就会执行默认的选项。

    ```shell
    Need to get 4,986 B of archives.
    After this operation, 1,024 B of additional disk space will be used.
    Do you want to continue? [Y/n]
    ```

# 虚拟机使用

1. VMWare要同时运行多个虚拟机，较大的内存至关重要。

2. 新建虚拟机的时候一般选择稍后再安装系统，如果选择安装光盘镜像，则可能会自动安装，不能自定义。

3. 内存分配过小，无法进入图形安装界面，CentOS6的阈值为628M。

4. 虚拟机可以创建快照，方便恢复和快速进入系统。

5. 虚拟机克隆可以生成一个完全一样的计算机，分为链接克隆（占用很小的空间，如果原始计算机删除，则克隆失效）和完整克隆（占用相同的空间）。

6. 硬盘分区后文件的读写效率会提高，因为某一个分区内的文件的块基本都在硬盘的同一块区域内，这样会减小磁头的旋转延迟。

7. 基于MBR，主分区最多只能有4个，扩展分区最多只能有1个，主分区+扩展分区最多只能有4个，扩展分区不能被格式化，不能写入数据，只能包含逻辑分区。以上的限制是硬盘的限制，不是Linux系统的限制。

8. 格式化分为高级和低级，低级格式化是硬盘的操作，高级格式化是操作系统的操作，也称为逻辑格式化。就是写入文件系统。分区完之后还要讲空间分为一个一个的小块Block（默认4KB），作为文件存储的基本单元。一个块只能存储一个文件的数据，10KB的文件要占用3个块。

9. 一个文件的数据块，一般不连续。每个文件都有一个独一无二的iNode号，因此文件系统还要保存一个INode和block的对应表格。

10. 硬件设备文件名：

    ```shell
    硬件                  设备文件名
    IDE硬盘               /dev/hd[a-d]
    SCSI/SATA/USB硬盘     /dev/sd[a-p]
    光驱                  /dev/cdrom或/dev/sr0
    软盘                  /dev/fd[0-1]
    打印机 (25针)         /dev/lp[0-2]
    打印机 (USB)          /dev/usb/lp[0-15]
    鼠标                  /dev/mouse
    ```

11. /是根目录，必须挂载。swap分区是虚拟内存，分配内存的2倍即可，一般不超过2GB，没有挂载点，因为他不是给用户用的，是内核直接调用的。

12. 设备文件名是固定的，系统自动检测，硬盘文件名后+1，2，3……就是分区设备文件名。

13. IDE是宽的针口，已淘汰。SCSI是宽的扁口，主要用在服务器。SATA硬盘是小的扁口。

14. 前4个分区号只能给主分区和扩展分区，不能给逻辑分区，可以跳着使用。

15. 一块新的硬盘要在Linux系统下使用，需要经过以下步骤：分区，格式化，挂载。只能挂载到空目录。

16. 挂载是将分区的设备文件名和目录连接起来。

17. 一般也会对\boot目录单独分区，200MB即可。防止出现根目录所在的分区写满后，系统无法启动。

18. 同时Home目录也会单独分区，便于做磁盘配额。

19. Linux中不存在将系统装在哪个分区的说法，因为安装系统时，会自动在\boot和一些其他目录下写入东西，这个目录可以是一个单独的分区，也可以不是。

20. 在分区的时候，分区号是自动分配的，先分配的，号大，不过挂载在\boot目录的分区总是会排在最前面的，例如sda1。

21. 根分区一般最后分配，一般把剩余的空间都给它。

22. 虚拟机的挂起相当于睡眠。

# 系统安装

1. 分区命令：

   1. 其中fdisk命令较为常用，但不支持大于 2TB 的分区；

      ```shell
      sudo fdisk -l #列出分区表
      sudo fdisk /dev/sda #进入fdisk的交互环境，以/dev/sda为对象。如果一个硬盘没有分区表，则会默认创建一个MBR的disk label，见下图。
      # fdisk环境下，所有的操作不会立即生效，只有在最后保存推出时才会生效，类似于BIOS的设置。m指令可以查看帮助
      ```

   3. 如果需要支持大于 2TB 的分区，则需要使用 parted命令。要注意的是，parted中所有的操作都是立即生效的（交互式环境也是如此），这一点和 fdisk 交互命令明显不同。

      ```shell
      #和fdisk不同，parted除了有交互模式外，还支持直接在命令行进行处理。
      sudo parted /dev/sda #进入parted的交互环境，以/dev/sda为对象。
      #输入help或m，可以查看命令提示
      mklabel msdos #创建一个mbr的分区表类型
      set 1 esp on #将编号1的分区设置为EFI系统分区
      ```
   
2. fdisk和parted都只能将disk label从一个设置成另一个，但是图形软件Utilities/Disk可以将disk label设置成无。

3. MBR格式的硬盘，安装系统时，是不需要花费EFI系统分区的。

4. 如果在一块全新的硬盘上安装操作系统，需要先给硬盘分区，分区格式有两种MBR和GPT。

   ```shell
   sudo fdisk -l
   ```
   
5. 如果将硬盘进行格式化时，分区表类型设置为MBR/DOS格式，则fdisk -l 会显示如下结果，Disklabel type：dos。

7. 全新的硬盘要先创建分区表，默认的类型为GPT分区表格式。这一点可以通过新建一个logical分区，观察是否为sda5来确定。若为sda5，则表示为MBR，否则为GPT。还有就是GPT格式创建新分区时，会在硬盘的开头多出来一个1MB的空间，留作Grub bios分区，这个分区不用也不能格式化。

8. 也可以通过fdisk命令手动设置为MBR分区格式。或者在live CD中启动Utilities/Disk软件，进行图形界面设置。点击右上角的三个点的图标，选择Format Disk，第一行默认选择快速格式化，即不实际删除数据。第二行选择MBR/DOS。

8. 然后逐个建立分区：

   ```shell
   bios grub分区 #大小1MB就够。设置类型为Reserved BIOS boot area，没有挂载点。
   eif分区 #大小100MB就够。设置类型为EFI System Partition，没有挂载点。
   boot分区 #200MB以上，一般500MB。普通的文件分区，挂载点为/boot。
   swap分区 #2048MB即可，类型为swap area，没有挂载点。
   根分区 #剩余所有的空间，普通的文件分区，挂载点为/。
   ```

17. 如果是全新的硬盘，如果没有分配这1MB的bios grub分区，则会提示。如果已经安装了Windows系统，则不会提示，因为它会公用Windows的那块区域。

20. 如果要用Ubuntu的引导器代替Windows的引导器，就选 /dev/sda。

21. 如果要保留Windows的引导器，就选 /boot分区，但这样一来，装完Ubuntu重启后，只能启动Windows，还必须在Windows上面安装Easybcd、Grub4dos等等之类软件来添加Ubuntu启动项。

22. 安装Ubuntu Server时，手动划分分区时，会出现无法设置分区类型为efi的情况，此时如果划分完城后再调用右上角的shell去使用parted来设置EFI分区的类型，会出现安装完毕后，EFI分区没有被自动挂载，因此/etc/fstab中没有这条记录。因此需要在一开始就进入shell，手动使用parted或fdisk划分好所有的分区，然后再安装。

25. Server安装环境中，“安装启动引导器的设备” 选择是哪个？？

29. 安装日志用于批量安装系统。CentOS系统中存在于如下位置：

    ```shell
    /root/install.log     #存储了安装在系统中的软件包及其版本信息
    /root/install.log.syslog  #存储了安装过程中留下的事件记录
    /root/anaconda-ks.cfg #以Kickstart配置文件的格式记录安装过程中设置的选项信息
    ```

30. 某些版本的Linux是禁止root用户远程登录的，需要先创建一个普通用户登录。

31. 远程工具如果出现乱码可能是没有选择中文字体。字符集选择GB2312，编码集选择UTF-8。

32. Linux每一个目录都是提前定义好了用处，软件安装会遵循这个约定。/bin和/usr/bin是任意用户都可以执行的系统命令。/sbin和/usr/sbin中的命令只有root可以执行。/usr下的命令在单用户模式下不能执行。类似于Windows中的安全模式。不过有时而这时软连接。

35. 从下图可以看出su命令不会改变当前的PATH等环境变量，而su -则会改变。

36. ![image-20201029104110601](Linux学习.assets/image-20201029104110601.png)

37. cat 如果不加文件名，则会读取标准输入，遇到回车，则会输出当前行，继续接收输入，在空白行遇到Ctrl+d，则会停止。

40. find 默认会递归，grep则不会，要加-R。

28. 字符终端有tty1-6，tty7是图形终端

# 系统启动过程与系统管理

1. CentOS6.x的启动过程：整体上分为4大块：

   1. 按电源后BIOS工作，进行加电开机自检，BIOS是固化在ROM芯片上的一段程序。此时CPU已经开始工作了。
   2. MBR中的引导程序开始工作，位于磁盘最外围的0磁道，0柱面，第一个扇区，bootsector。由文件系统对磁盘初始化时产生的。446（boot loader）+64（分区表）+2（55AA）=512字节
   3. 启动内核。内核有多个，但是只能启动一个。
   4. 启动第一个进程init，PID=1。

2. 按下电源键，给微控制器下达一条复位指令，各寄存器复位，最后下达一条跳转指令，读取主板上的BIOS程序，在这之前都是由硬件完成的，之后控制权交给BIOS。

3. BIOS随后加载CMOS（可读写的芯片）中的信息，里边存储着BIOS设置硬件参数的信息。BIOS借CMOS来取得主机的各项硬件配置信息，例如BIOS中的开机顺序等信息。

4. 主板的BIOS有一个专门供电的电池，拔掉电池，过几分钟，CMOS中的信息，就会消失。电池的寿命一般是5年以上。

5. 从CMOS取得信息后，BIOS进行加电自检POST，如果硬件异常会发出报警声。根据声音的长短个数，可以判断故障。

6. 然后BIOS加载硬件的驱动程序，对硬件进行初始化。

7. 然后BIOS会将自己复制到内存中继续执行。

8. 然后开始按顺序搜寻可引导设备。判断标准就是每个磁盘的第一个扇区的结尾是否是0x55AA，如果有就是可引导。BIOS中是没有文件系统的（空间太小）。引入MBR，可以让BIOS没有文件系统也可以读取硬盘的信息。MBR中存在一个boot loader。此时BIOS将控制权交给MBR。没有文件系统是不可以读取文件的，但是可以读取扇区。

9. boot loader的主要工作就是读取磁盘中的操作系统内核文件。

10. 不同的操作系统的文件格式不同，一个磁盘可以装多个操作系统。各个操作系统中也有自己的loader。

11. BootLoader找到操作系统的loader，将控制权转交过去。

12. 磁盘的第一个扇区不属于任何分区。每个分区的第一个扇区叫做boot sector，存放着操作系统的loader。所以一个分区通常只能装一个操作系统。没有系统的分区的第一个扇区为空。

13. boot loader提供转交给各个分区操作系统的loader的选择。

14. 安装Windows时，会复制系统的loader到MBR的BootLoader中，而linux不会这样。这样一来，MBR就会直接读取BootLoader中的loader了，启动默认的操作系统。因此安装双系统的话应该先安装Windows，再安装linux。然后手动将linux的loader复制到BootLoader中，覆盖掉Windows的。

15. linux的loader最常用的是grub，类似的还有LILO。GRand Unified Bootloader（大一统启动加载器）。如今的 GRUB 也被称作 GRUB 2。

16. /boot/grub目录

17. 

18. 使用单用户模式修复linux系统：在grub启动界面，选择正确的内核，编辑，在最后输入1（1表示单用户模式）再启动即可。对于RHEL 8将ro修改为rw，然后加上init=/bin/sh即可进入。

19. ![image-20210416165009813](Linux学习.assets/image-20210416165009813.png)

20. 单用户模式下是以root登录的，使用passwd即可修改root的密码。修改完要输入如下命令再重启：

    ```shell
    touch /.autorelabel #创建这样一个文件其实就是在告诉SELinux放行这个策略
    ```

21. 一些发行版使用/etc/inittab文件来管理系统开机时要启动的程序。Ubuntu则在/etc/init.d目录下存放各种开机启动的脚本。

23. 使用init进程的linux有5个运行级别，运行级别决定了init进程选择/etc/rcX.d中哪一个目录中的脚本来启动。

    1. 运行级别1表示单用户模式，只启动基本的系统进程和一个控制台终端进程。通常在系统有问题时，紧急用来修复时使用。
    2. 运行级别3表示多用户模式，在该模式下，大多数软件都会启动。
    3. 运行级别5表示图形化模式。

# Systemd

1. Systemd是Linux的系统工具，用来启动守护进程，已经成为大多数linux发行版的标配。最后的d是daemon守护进程的意思。systemd设计就是为了守护整个系统，它不是一个命令，而是一组命令。

2. 在systemd之前，linux的启动都是使用init进程的，该进程是系统的第一个进程（PID=1），随后启动其他进程。

   ```shell
   #启动服务
   sudo /etc/init.d/apache2 start
   #或者
   service apache2 start
   ```

   缺点如下：

   1. 串行启动，只有前一个进程启动完毕，才能启动下一个。
   2. 启动脚本复杂，init只是执行启动脚本，其他的事情一概不管，因此启动脚本就需要写的很复杂。

3. systemd取代了init进程，称为系统的第一个进程。

4. ![img](Linux学习.assets/bg2016030703.png)

## 主要命令

1. systemctl是systemd的主要命令：

   ```shell
   $ sudo systemctl reboot        # 重启系统
   $ sudo systemctl poweroff      # 关闭系统，切断电源
   $ sudo systemctl halt          # CPU停止工作
   $ sudo systemctl suspend       # 暂停系统
   $ sudo systemctl hibernate     # 让系统进入冬眠状态
   $ sudo systemctl hybrid-sleep  # 让系统进入交互式休眠状态
   $ sudo systemctl rescue        # 启动进入救援状态（单用户状态）
   ```

2. systemd-analyze用于查看启动耗时：

   ```shell
   $ systemd-analyze                             # 查看启动耗时
   $ systemd-analyze blame                       # 查看每个服务的启动耗时
   $ systemd-analyze critical-chain              # 显示瀑布状的启动过程流
   $ systemd-analyze critical-chain atd.service  # 显示指定服务的启动流
   ```

3. hostnamectl命令用于查看当前主机的信息：

   ```shell
   $ hostnamectl                          # 显示当前主机的信息
      Static hostname: zj-hit
            Icon name: computer-vm
              Chassis: vm
           Machine ID: 5b0657a23bb647a08acb4e8178a978fd
              Boot ID: 3913961aceaf45e9b43a7a37ad7b20ba
       Virtualization: vmware
     Operating System: Ubuntu 20.04.3 LTS
               Kernel: Linux 5.11.0-46-generic
         Architecture: x86-64
   $ sudo hostnamectl set-hostname rhel7  # 设置主机名。
   ```

4. localectl命令用于查看本地化设置：

   ```shell
   $ localectl                                  # 查看本地化设置
      System Locale: LANG=en_US.UTF-8
                     LC_NUMERIC=zh_CN.UTF-8
                     LC_TIME=zh_CN.UTF-8
                     LC_MONETARY=zh_CN.UTF-8
                     LC_PAPER=zh_CN.UTF-8
                     LC_NAME=zh_CN.UTF-8
                     LC_ADDRESS=zh_CN.UTF-8
                     LC_TELEPHONE=zh_CN.UTF-8
                     LC_MEASUREMENT=zh_CN.UTF-8
                     LC_IDENTIFICATION=zh_CN.UTF-8
          VC Keymap: n/a
         X11 Layout: us
          X11 Model: pc105
   $ sudo localectl set-locale LANG=en_GB.utf8  # 设置本地化参数。
   $ sudo localectl set-keymap en_GB
   ```

5. timedatectl命令用于查看当前时区设置：

   ```shell
   $ timedatectl                                     # 查看当前时区设置
                  Local time: Tue 2022-02-22 12:56:55 CST
              Universal time: Tue 2022-02-22 04:56:55 UTC
                    RTC time: Tue 2022-02-22 04:56:55
                   Time zone: Asia/Shanghai (CST, +0800)
   System clock synchronized: no
                 NTP service: active
             RTC in local TZ: no
   $ timedatectl list-timezones                      # 显示所有可用的时区
   $ sudo timedatectl set-timezone America/New_York  # 设置当前时区或者Asia/Shanghai
   $ sudo timedatectl set-time YYYY-MM-DD
   $ sudo timedatectl set-time HH:MM:SS
   ```

6. loginctl命令用于查看当前登录的用户：

   ```shell
   $ loginctl list-sessions     # 列出当前session
   SESSION  UID USER SEAT TTY
         1 1000 zj        pts/0
   
   1 sessions listed.
   $ loginctl list-users        # 列出当前登录用户
   $ loginctl show-user ruanyf  # 列出显示指定用户的信息
   ```

## Unit

1. systemd可以管理系统的所有资源，所有的资源都是unit，unit可以分为12种：

   1. Service Unit：系统服务
   2. Target Unit：多个 Unit 构成的一个组
   3. Device Unit：硬件设备
   4. Mount Unit：文件系统的挂载点
   5. Automount Unit：自动挂载点
   6. Path Unit：文件或路径
   7. Scope Unit：不是由 Systemd 启动的外部进程
   8. Slice Unit：进程组
   9. Snapshot Unit：Systemd 快照，可以切回某个快照
   10. Socket Unit：进程间通信的 socket
   11. Swap Unit：swap 文件
   12. Timer Unit：定时器

2. unit的相关操作：

   ```shell
   $ systemctl list-units                        # 列出正在运行的 Unit  192个
   $ systemctl list-units --all                  # 列出所有Unit，包括没有找到配置文件的或者启动失败的 366个
   $ systemctl list-units --all --state=inactive # 列出所有没有运行的 Unit   107个
   $ systemctl list-units --failed               # 列出所有加载失败的 Unit   0个
   $ systemctl list-units --type=service         # 列出所有正在运行的、类型为 service 的 Unit
   ```

3. systemctl status命令用于查看系统状态和单个 Unit 的状态：

   ```shell
   $ systemctl status  # 显示系统状态
    zj-hit
       State: running
        Jobs: 0 queued
      Failed: 0 units
       Since: Tue 2022-02-22 13:01:52 CST; 14min ago
      CGroup: /
              ├─user.slice               #用户进程组
              │ └─user-1000.slice
              │   ├─user@1000.service
              │   │ ├─gvfs-goa-volume-monitor.service
              │   │ │ └─1058 /usr/libexe
               ......
              └─system.slice             #系统进程组
                ├─irqbalance.service
                │ └─697 /usr/sbin/irqbalance --foreground
                ├─NetworkManager-d
              
   $ sysystemctl status bluetooth.service                      # 显示单个 Unit 的状态
   $ systemctl -H root@rhel7.example.com status httpd.service  # 显示远程主机的某个 Unit 的状态
   ```

4. 除了status命令，systemctl还提供了三个查询状态的简单方法，主要供脚本内部的判断语句使用：

   ```shell
   $ systemctl is-active application.service   # 显示某个 Unit 是否正在运行
   $ systemctl is-failed application.service   # 显示某个 Unit 是否处于启动失败状态
   $ systemctl is-enabled application.service  # 显示某个 Unit 服务是否建立了启动链接
   ```

5. Unit的管理：

   ```shell
   sudo systemctl start|stop|restart apache.service            #立即启动，停止，重启一个Unit。
   sudo systemctl kill apache.service                          #杀死一个Unit的所有子进程。有时候，stop命令可能没有响应，服务停不下来。这时候就不得不"杀进程"了，向正在运行的进程发出kill信号。
   sudo systemctl show httpd.service                           #显示某个Unit的所有底层参数。
   $ systemctl show -p CPUShares httpd.service                 # 显示某个Unit的指定属性的值。
   $ sudo systemctl set-property httpd.service CPUShares=500   # 设置某个Unit的指定属性。
   ```
   
6. Unit之间存在依赖关系，例如A依赖于B，这意味着systemd在启动A的时候，会先去启动B。

   ```shell
   systemctl list-dependencies ssh.service    #列出ssh.service这个unit的依赖。某些依赖是target，默认不会展开，可以使用 -all参数来展开target。
   ```

## 配置文件

1. 每个Unit都有一个配置文件，告诉systemd怎么去启动这个Unit，配置文件完全决定了Unit是如何启动的。systemd默认从/etc/systemd/system目录中读取配置文件，开机时，systemd只会启动 /etc/systemd/system目录下的配置文件。但是这里边存放的大多数是符号链接，指向 /usr/lib/systemd/system，这里才是真正存放配置文件的地方。systemctl enable命令用于在两个目录之间建立符号链接（因此为设置开机启动该Unit），systemctl disable 用于撤销符号链接。

   ```shell
   $ sudo systemctl enable clamd@scan.service
   
   Synchronizing state of ssh.service with SysV service script with /lib/systemd/systemd-sysv-install.
   Executing: /lib/systemd/systemd-sysv-install enable ssh
   Created symlink /etc/systemd/system/sshd.service → /lib/systemd/system/ssh.service.
   Created symlink /etc/systemd/system/multi-user.target.wants/ssh.service → /lib/systemd/system/ssh.service. #如果unit包含WantedBy参数，则还会在对应的target的wants文件夹中添加符号链接。
   
   # 等同于
   $ sudo ln -s '/usr/lib/systemd/system/clamd@scan.service' '/etc/systemd/system/multi-user.target.wants/clamd@scan.service'
   ```

2. 对于支持systemd的软件，安装时都会在/usr/lib/systemd/system目录下生成一个配置文件。

3. 配置文件的后缀名，就是该 Unit 的种类，比如sshd.socket。如果省略，Systemd 默认后缀名为.service，所以sshd会被理解成sshd.service。

4. 每个配置文件的状态有以下4种，注意并非unit的状态，而是unit-file的状态：

   1. enabled：已建立启动链接。
   2. disabled：没建立启动链接。
   3. static：该配置文件没有`[Install]`部分（无法执行），只能作为其他配置文件的依赖。
   4. masked：该配置文件被禁止建立启动链接。

5. 从配置文件的状态无法看出该unit是否在运行，必须要使用systemctl status xxx.unit来查看。

6. 一旦修改某个unit的配置文件，则要先让systemd载入配置文件，然后再重启该unit。

   ```shell
   sudo systemctl daemon-reload  #这个是重新加载所有修改过的配置文件
   sudo systemctl reload httpd.service #也可以只加载某个配置文件
   sudo systemctl restart httpd.service
   ```

7. systemctl cat就是输出配置文件，和cat一样。

8. 配置文件分为几个区块，每个区块的第一行用中括号括起来。配置文件的内容都是区分大小写的。

   ```shell
   [Unit]  #区块
   Description=ATD daemon  #字段，都是键值对，两侧不能有空格。
   
   [Service]
   Type=forking
   ExecStart=/usr/bin/atd
   
   [Install]
   WantedBy=multi-user.target
   ```

9. [Unit]区块通常是配置文件的第一个区块，用来定义整个unit的元数据，以及与其他unit之间的关系。主要字段如下：

   ```shell
   Description：简短描述
   Documentation：文档地址
   Requires：如果字段 Unit 启动失败或停止运行，当前 Unit 也必须退出 #强依赖,这里只涉及到依赖关系，不涉及启动顺序，默认是同时启动的。A依赖于B，不代表启动A的时候会去启动B。
   Wants：如果字段 Unit 启动失败或停止运行，当前 Unit 受影响        #弱依赖
   BindsTo：与Requires类似，它指定的 Unit 如果退出，会导致当前 Unit 停止运行
   Before：当前Unit必须在字段指定的Unit之前启动 #这里只涉及启动顺序，不涉及依赖关系
   After：当前Unit必须在字段指定的Unit之后启动  #例如某应用需要使用到网络，就应该在network.target之后启动。
   Conflicts：如果字段中的Unit正在运行，则当前Unit不能运行。
   Condition...：当前 Unit 运行必须满足的条件，否则不会运行
   Assert...：当前 Unit 运行必须满足的条件，否则会报启动失败
   
   #例如ssh.service
   [Unit]
   Description=OpenBSD Secure Shell server
   Documentation=man:sshd(8) man:sshd_config(5)
   After=network.target auditd.service
   ```

10. [Install]区块通常是配置文件的最后一个区块，定义如何安装这个配置文件，即如何设置启动，主要字段如下：

    ```shell
    WantedBy：它的值是一个或多个 Target(空格分隔)，当前 Unit 激活时（enable）,其配置文件的符号链接会放入/etc/systemd/system目录下面以 Target 名 + .wants后缀构成的子目录中,例如multi-user.target.wants
    RequiredBy：它的值是一个或多个 Target，当前 Unit 激活时，符号链接会放入/etc/systemd/system目录下面以 Target 名 + .required后缀构成的子目录中
    Alias：当前 Unit 可用于启动的别名
    Also：当前 Unit 激活（enable）时，会被同时激活的其他 Unit
    
    #例如ssh.service:
    [Install]
    WantedBy=multi-user.target
    Alias=sshd.service
    ```

11. 系统开机会启动  `systemctl get-default`这个target，即在/etc/systemd/system/multi-user.target.wants目录下的所有Unit。如果要将将一个Unit设置为开机启动，则要先在其配置文件中的WantedBy字段添加默认的target，然后使用命令`sudo systemctl enable`建立符号链接。

12. WantedBy字段只是表明可以使用enable来将当前Unit添加到某个target的启动列表里，并不表示该Unit会被启动，也不表示会开机启动。

13. [Service]区块用来 Service 的配置，只有 Service 类型的 Unit 才有这个区块，主要字段如下：

    ```shell
    Type：定义启动时的进程行为。它有以下几种值。
    Type=simple：默认值，执行ExecStart指定的命令，启动主进程。即服务进程在启动后会一直运行，并占据终端。当服务进程退出时，Systemd 认为服务已经停止运行。
    Type=forking：以 fork 方式从父进程创建子进程，创建后父进程会立即退出。守护进程推荐这种方式。在启动服务后，服务主进程会将控制权交给子进程来执行实际的任务。此时，服务主进程会退出，但服务并没有结束。当子进程退出时，Systemd 认为服务已经停止运行。不过守护进程需要脱离终端，因此需要程序将输出写入到日志中。
    Type=oneshot：一次性进程，Systemd 会等当前服务退出，再继续往下执行
    Type=dbus：当前服务通过D-Bus启动。   一个为应用程序间通信的消息总线系统, 用于进程之间的通信。
    Type=notify：当前服务启动完毕，会通知Systemd，再继续往下执行
    Type=idle：若有其他任务执行完毕，当前服务才会运行
    ExecStart：启动当前服务的命令   #重复定义会被覆盖
    ExecStartPre：启动当前服务之前执行的命令  #所有的pre和post可以定义多个，会依次生效
    ExecStartPost：启动当前服务之后执行的命令
    ExecReload：重启当前服务时执行的命令
    ExecStop：停止当前服务时执行的命令
    ExecStopPost：停止当其服务之后执行的命令
    RestartSec：自动重启当前服务间隔的秒数
    Restart：定义何种情况 Systemd 会自动重启当前服务，可能的值包括always（总是重启）、on-success、on-failure、on-abnormal、on-abort、on-watchdog
    TimeoutSec：定义 Systemd 停止当前服务之前等待的秒数
    Environment：指定环境变量
    RestartSec：Systemd 重启服务之前，需要等待的秒数
    
    #例如ssh.service
    [Service]
    EnvironmentFile=-/etc/default/ssh   #环境参数文件，本质是一个shell脚本，键值对的形式，可以用$key的方式在启动时使用。例如下面的第三行。所有的启动设置之前都可以在=后面加上一个-，表示这一行出错也不影响其他命令的执行。
    ExecStartPre=/usr/sbin/sshd -t
    ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
    ExecReload=/usr/sbin/sshd -t
    ExecReload=/bin/kill -HUP $MAINPID
    KillMode=process      #定义了如何停止该服务，process表示只杀死主进程，不停止任何子进程，这个设置不太常见，但对 sshd 很重要，否则你停止服务的时候，会连自己打开的 SSH session 一起杀掉。
    Restart=on-failure   #定义了服务退出后，system的重启它的方式 on-faliure表示非正常退出(退出状态码≠0)才会重启。对于守护进程，推荐设置为on-faliure
    RestartPreventExitStatus=255
    Type=notify
    RuntimeDirectory=sshd  #在/run目录下会创建一个对应的运行时目录，可供使用，不能是绝对目录。
    RuntimeDirectoryMode=0755
    ```

14. 启动计算机时，需要启动大量的unit，这是可以将一些关联的unit作为一个target组，当systemd启动某个target时，会启动其中包含的所有unit。target类似于状态点，启动某个target就好像达到了某个状态点。这个类似于传统的init启动模式中的运行级别runlevel，但是不同的运行级别是互斥的，不能同时启动，而target则不存在这个限制。

15. target配置文件中没有启动命令：

    ```shell
    $ systemctl cat multi-user.target
    
    [Unit]
    Description=Multi-User System
    Documentation=man:systemd.special(7)
    Requires=basic.target
    Conflicts=rescue.service rescue.target
    After=basic.target rescue.service rescue.target
    AllowIsolate=yes      #允许使用systemctl isolate切换到
    ```

16. target的操作：

    ```shell
    $ systemctl list-unit-files --type=target         # 查看当前系统的所有 Target
    $ systemctl list-dependencies multi-user.target   # 查看一个 Target 包含的所有 Unit
    $ systemctl get-default                           # 查看启动时的默认 Target
    $ sudo systemctl set-default multi-user.target    # 设置启动时的默认 Target,就是设置/etc/systemd/system/default.target链接到哪个文件。
    # 切换 Target 时，默认不关闭前一个 Target 启动的进程，
    # systemctl isolate 命令则会关闭前一个 Target 里面所有不属于后一个 Target 的进程，并启动后一个target中新增的进程。
    $ sudo systemctl isolate multi-user.target
    ```

17. 运行级别和target的对应：

    ```shell
    Runlevel 0           |    runlevel0.target -> poweroff.target    #关机
    Runlevel 1           |    runlevel1.target -> rescue.target      #救援模式，用于修复系统
    Runlevel 2           |    runlevel2.target -> multi-user.target  #多用户命令行
    Runlevel 3           |    runlevel3.target -> multi-user.target
    Runlevel 4           |    runlevel4.target -> multi-user.target
    Runlevel 5           |    runlevel5.target -> graphical.target   #图形界面，强依赖于multi-user.target
    Runlevel 6           |    runlevel6.target -> reboot.target      #重启
    ```

18. systemd统一管理所有unit的启动日志(内核日志和应用日志)，用journalctl来查看，其配置文件为/etc/systemd/journald.conf

    ```shell
    sudo journalctl -u nginx.service  #查看指定unit的日志
    #日志的优先级一共有8种：
    # 0: emerg
    # 1: alert
    # 2: crit
    # 3: err
    # 4: warning
    # 5: notice
    # 6: info
    # 7: debug
    journalctl -b   #查看本次启动的日志
    ```

19. unit的状态查看：

    ```shell
    zj@zj-hit:~$ systemctl status ssh.service
    ● ssh.service - OpenBSD Secure Shell server
         Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled #配置文件的位置,是否为开机启动。
         Active: active (running) since Thu 2022-02-24 09:29:56 CST; 1h 31min ago  #正在运行
           Docs: man:sshd(8)  #文档
                 man:sshd_config(5)
        Process: 769 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
       Main PID: 819 (sshd)  #主进程ID
          Tasks: 1 (limit: 3247)
         Memory: 5.0M
         CGroup: /system.slice/ssh.service 
                 └─819 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups  #应用的所有子进程
    #下方为日志块
    Feb 24 09:29:54 zj-hit systemd[1]: Starting OpenBSD Secure Shell server...
    Feb 24 09:29:56 zj-hit sshd[819]: Server listening on 0.0.0.0 port 22.
    Feb 24 09:29:56 zj-hit sshd[819]: Server listening on :: port 22.
    Feb 24 09:29:56 zj-hit systemd[1]: Started OpenBSD Secure Shell server.
    Feb 24 09:55:25 zj-hit sshd[1048]: Accepted password for zj from 192.168.80.1 p>
    Feb 24 09:55:25 zj-hit sshd[1048]: pam_unix(sshd:session): session opened for u>
    ```


## 开机启动的例子

1. 设置开机启动pvserver程序，用于paraview远程处理。

   ```shell
   [Unit]
   Description=Paraview remote server
   After=network.target multi-user.target #这两个target是独立的
   ConditionPathExists=/usr/bin/pvserver
   ConditionPathExists=/home/zj/OpenFOAM/zj-11/run
   ConditionPathExists=/usr/bin/start-pvserver.sh
   
   [Service]
   ExecStart=/usr/bin/start-pvserver.sh
   KillMode=process
   Restart=on-failure
   RestartPreventExitStatus=255
   Type=simple
   RuntimeDirectory=pvserver
   RuntimeDirectoryMode=0755
   
   [Install]
   WantedBy=multi-user.target
   ```

# SHELL

## 基础

1. Shell脚本的扩展名一般为.sh，也可以没有。脚本可以用来做环境配置，日志分析等。shell解释器是用C语言编写的。Shell具有以下功能：命令解释，启动程序，输入输出重定向，管道，文件名置换（字符串处理），变量维护，运行环境控制。

2. 常见的shell版本：

   1. Bourne shell，这是第一个流行的的shell，由Steven Bourne开发，可以简称为sh，路径为 /bin/sh。
   2. Bourne again shell，Linux下默认的shell，是Bourne shell的增强版，由GNU计划提供。路径为 /bin/bash。
   3. C shell，使用C语言兼容的语法，由Berkeley大学的Bill Joy研发的，随BSD系统分发。Sun公司的创始人就是Bill Joy，BSD最早就是他在Berkeley搞出来的，后来的Solaris也是Sun公司开发的，也将C shell作为默认的shell。路径为/bin/csh。
   4. tcsh，整合了C shell，提供更多的功能，更优化。路径为/bin/tcsh。

3. 系统支持的shell，可以在/etc/shells文件中查看。如果安装了新的shell，也会写入到此文件中，系统的某些服务在运行中，会检查当前用户可用的shell，就会查询这个文件。

   ```shell
   zj@ubuntu:~$ cat /etc/shells
   # /etc/shells: valid login shells
   /bin/sh -> /usr/bin/bash
   /usr/bin/sh -> /usr/bin/bash
   /bin/bash
   /usr/bin/bash
   /bin/rbash -> bash
   /usr/bin/rbash -> bash
   /bin/dash
   /usr/bin/dash
   /bin/zsh
   /usr/bin/zsh
   /bin/csh -> /bin/bsd-csh
   /usr/bin/csh
   /usr/bin/tmux
   /usr/bin/screen
   ```

4. 在用户登录时，系统会根据/etc/passwd文件中对应的用户的shell路径（一般为绝对路径）来打开一个shell供用户使用。

5. 还有一些shell不是给用户使用的，因此没有列出在/etc/shells文件中，例如/sbin/nologin，/bin/false，它们用于给特定的账号使用。

6. 每个用户家目录下的.bash_history文件会记录bash的历史命令。不过这里只会记录本次登录以前执行过的命令，而本次登录执行过的命令都缓存在内存中，退出登录时才会写入到该文件中，也可以手动要求写入到文件中。每次登录后，shell会从历史记录文件中读取内容，

   ```shell
   zj@ubuntu:~$ echo $HISTFILE  #历史记录文件的位置
   /home/zj/.bash_history
   zj@ubuntu:~$ echo $HISTFILESIZE  #历史记录文件的条目数量，也就是记录2000条，新来的会把旧的顶掉。
   2000
   zj@ubuntu:~$ echo $HISTSIZE  #历史记录条目数量
   1000
   history #查看历史记录文件和本次登录后运行的命令。
   -c #清除当前shell中的历史记录
   -n #列出最近的n条历史记录
   -a [histfile] #将新增的命令写入到histfile文件中，如果没有提供可选参数，则写入默认的位置。
   -w [histfile] #将目前的history记录写入到histfile中，如果没有提供可选参数，则写入默认的位置。
   -r [histfile] #将histfiles的内容读入到当前shell的history有中。
   ```

7. bash自带了命令和路径补全。如果在一串命令的第一个字后面按[Tab]，则会补全命令。如果在一串命令的第一个字后面按[Tab]，则会补全路径。如果安装了bash-completion软件，可以为某些命令的选项或参数提供补充。在`/usr/share/bash-completion/completions`目录下存放着各个应用程序的补全提示文件，安装新软件时，如果支持这个功能，则会向该目录添加自己的提示文件。

8. bash支持使用内置命令alias为命令设置别名。输入alias来查看已经定义的所有别名。alias的定义规则和变量的一样，=两侧不能有空格。例如：

   ```bash
   alias ll="ls -lh --color=auto"   #命令可以有参数，包含空格的需要用单或双引号包括
   alias la="ls -lah --color=auto"
   alias s=neofetch                 #如果没有空格，可以不用单或双引号包括
   alias updatedb="sudo updatedb"
   alias r=ranger
   alias cls=clear
   alias df="df -Th"
   alias du="du -sh"
   alias less="less -i"
   ```

9. 在命令前加上\，例如`\ll`，可以强制不使用alias转换。使用unalias取消别名设置。

   ```shell
   zj@ubuntu:~$ ll  #会被alias替换为 ls -lh --color=auto
   total 124K
   drwxr-xr-x 27 zj zj 4.0K May  6 15:23 apue.3e
   drwxrwxr-x  3 zj zj 4.0K May 10 16:45 Calculix
   drwxrwxr-x  4 zj zj 4.0K Apr 29 04:56 git_test
   zj@ubuntu:~$ \ll #不会被替换,因为没有命令叫ll,因此会报错。
   ll: command not found
   ```

10. DOS的清屏是cls，Linux的清屏是clear。

11. bash还支持作业管理，前、后台控制，使得可以在单一登录环境下，达到多任务的目的。

12. bash支持将命令写成脚本，然后批量执行，此时就是一个小型的编程语言。

13. bash还支持使用通配符。例如`ls -l /usr/bin/*sh`可以查询该目录下有多少以sh结尾的文件或目录。

14. 为了方便shell的操作，bash内置了很多命令，例如cd，umask等。使用type来确定命令是内置还是外部的。使用man来查看内部命令的帮助时会跳转到man bash其中的一节。type的结果有三种可能，内置，外部，别名。type只查找可执行文件，和which类似，用来查找命令。

    ```shell
    zj@ubuntu:~$ type cd
    cd is a shell builtin             #内置命令
    zj@ubuntu:~$ type systemctl 
    systemctl is /usr/bin/systemctl   #外部命令
    zj@ubuntu:~$ type ll
    ll is aliased to 'ls -lh --color=auto'  #别名
    zj@ubuntu:~$ type -t cd #以builtin，file或alias来输出结果，方便其他命令使用这个结果。
    builtin
    zj@ubuntu:~$ type -p systemctl #如果是外部文件，则只输出文件的路径。
    /usr/bin/systemctl
    zj@ubuntu:~$ type type 
    type is a shell builtin    #type本身也是内置命令
    zj@ubuntu:~$ type -a ls    #将和命令相关的所有条目都显示出来。
    ls is aliased to 'ls --color=auto'     #最先使用
    ls is /usr/bin/ls
    ls is /bin/ls
    zj@ubuntu:~$ type -a echo   #有些命令既有内置的又有外部版本,使用which只能查看到外部版本,不能因此断定使用的就是这个版本。
    echo is a shell builtin
    echo is /usr/bin/echo
    echo is /bin/echo
    ```

15. type只会查找可执行文件，而不是一般文件名。

    ```shell
    zj@ubuntu:~$ type systemctl
    systemctl 是 /usr/bin/systemctl
    systemctl 是 /bin/systemctl
    zj@ubuntu:~$ sudo chmod a-x /usr/bin/systemctl
    [sudo] zj 的密码：
    zj@ubuntu:~$ type systemctl  #此时systemctl没有了可执行权限，则不会被type列出。
    bash: type: systemctl: 未找到
    ```

16. 如果命令太长，可以使用`\[Enter]`来换行，\后面不能有空格，要紧挨着Enter。因为\是用来转义[Enter]的。

    ```shell
    zj@ubuntu:~$ ls \
    > .                       #第二行会在开头自动出现一个>提示符。这个命令相当于 ls .
    ```

17. 如果不想执行已经输入了的命令，可以用Ctrl+C终止此行的输入，另起一行。

18. 

19. shell中具有特殊含义的符号：

    ```shell
    ~       #用户的家目录 可以和cd结合使用。
    -       #上一次的目录
    !p      #在命令历史记录寻找以p开头的最近的那个命令，并执行.  使用history命令来查看shell命令历史
    !!      #执行上一次命令
    !35     #执行第35号历史命令,在history命令的输出中有编号。
    $ABC    #获取变量ABC的内容
    +  -  *  /  %  #加减乘除，取余运算。
    &       #后台执行
    *       #shell中的通配符,匹配任意多个字符
    ?       #shell中的通配符,匹配除回车以外的1个字符。
    ;       #如果要在一行中执行多条命令，需要用分号分隔。
    |       #管道符,前一个命令的输出作为下一个命令的输入
    \       #转义符,例如将通配符*转义为乘号。
    `date`  #在命令中执行命令,例如 echo "dotay is `date +%F`"
    "ABC"   #字符串,不解释变量。echo "$USER"    输出为 root
    'ABC'   #字符串,会解释变量。echo '$USER'    输出为 $USER
    ''ABC'' #等价于"ABC"
    ```

20. 数学计算，expr和let都是shell的内建命令，都只能进行整数计算，不同的是let使用变量不用加$，而expr必须加

    ```shell
    expr 1 + 2  #expr只能计算整数的运算。符号和数字之间必须要有空格, expr 1 +2 也会报错。
    expr 1 - 2  #结果为-1
    expr 1 \* 2 #结果为2
    expr 1 / 2  #结果为0
    expr 10 % 3 #结果为1
    expr 1.1 + 3      #  expr: 非整数参数
    #可以利用expr来判断变量是否是整数
    let var1=3   #定义了一个新的变量var1,值为3
    expr 0 + $var1 &>/dev/null ; echo $?  #结果为0。计算0+$var1,将结果丢弃。然后输出上一条语句执行的返回值,如果是0表示执行成功,非0表示执行失败。
    var1=3.1
    expr 0 + $var1 &>/dev/null ; echo $?  #结果为2
    #let
    let num=2*3 #也是只能计算整数。
    let var1=3   #变量和表达式之间不能有空格
    var1++       #会提示未找到命令，这里shell认为var1++是一个命令或程序。
    let var1++   #此时var1的结果为4
    let var1+=5  #此时var1的结果为9
    ```

21. bc命令支持小数运算，它不是shell内建命令，不过bc是交互式的使用，shell脚本要通过管道来使用它。

    ```shell
    10/3     #结果为3
    scale=2  #保留2位小数
    10/3     #结果为3.33
    echo "scale=2;10/3"|bc #结果为3.33  这里的echo不能省略
    #输出内存使用率，一共1024，已使用212,保留两位小数
    echo "mem usage:`echo "scale=2;212*100/1024"|bc`%"    #这里涉及到了echo的嵌套使用。` `内部的字符串会被当做命令执行，用执行的结果替换。
    ```

22. $((  ))也可以进行整数计算，最为方便，格式也比较自由，内部可以自由加空格和括号：

    ```shell
    echo $(((1+2)*3))     #计算(1+2)*3的结果。
    i=1
    i=$((i + 1))          #此时变量i为2
    ```


## 脚本文件

1. Shell第一行必须指定脚本运行的环境，即解释器程序的路径。shell中使用#来表示注释，#!不是注释。开头还应该加上说明部分，这个可以在vim中自动配置。

   ```shell
   #!/usr/bin/bash         如果找不到该文件，执行时会报错。也可以写为    #!/usr/bin/env bash
   #Author: Jian Zhang
   #Create Time: 2021/09/01/ 13:55
   #Description: First study shell script
   ```

2. Shell脚本要用chmod给予执行权限。如果使用解释器，则不需要有执行权限：

   ```shell
   chmod 700 test.sh
   ./test.sh
   ##或者##
   chmod 600 test.sh #现在该文件不具备执行权限了
   bash test.sh      #也可以执行成功。这里的bash换成sh也可以，sh是bash的符号连接。/etc/shells文件中记录了支持的shell。
   ```

3. exit NUM  退出脚本，释放资源，NUM为返回值，有效的是0-255。可以在shell中用echo $?查看。

4. 脚本可以接受命令行参数：

   ```shell
   ./test.sh 3 5    #3个命令行参数，$0为./test.sh   $1为3   $2为5
   bash test.sh 3 5 #也是只有3个命令行参数，bash不计入
   ```

   

## 格式化输入输出

1. echo可以将内容输出到屏幕。

   ```shell
   echo "Hello World"  #输出对应字符串，并换行(LF,相当于C语言的\n)。 加上-n,可以取消默认的换行。一个空的echo表示一个换行
   echo -e "abc\ndef"  #-e选项表示解释转移字符,不当做一般字符输出。
   abc
   def   
   echo "abc\ndef"     #输出为abc\ndef,不会转义。
   #常见转移符号 \n换行 \t制表符
   ```

2. read接受键盘的输入，回车结束输入。用于脚本编写的时候进行互动。

   ```shell
   read -p "please input user name:" username  #用变量username存储输入的内容。
   -p   #后面是提示字符。
   -s   #选项可以取消回显，此时不会显示read命令本身。
   -t 5 #设置倒计时5秒,超时不允许输入，用于无人值守的情况，不会一直等待下去。
   -n 6 #表示最多接受6个字符。
   ```

## 变量

1. 每个用户登录后，都会获取一个bash，可以用mail命令接受属于自己的邮件，bash通过MAIL变量来区分那个邮箱是自己的。当用户zj登录时，他的bash中就存在一个MAIL变量，值为/bar/spool/mail/zj。使用变量就可以让mail一个命令来被多个用户使用。

2. 环境变量实际上是进程相关的概念，main函数的一个变体就接受环境变量字符串数组的指针。在shell进程中，环境变量一般是在用户使用bash之前就设置好了的，用来控制bash执行环境的。例如PATH，HOME，MAIL，SHELL。为了和自定义的变量进行区别，环境变量都是全大写字符表示。变量名严格区分大小写。

3. 使用echo查看变量的内容：

   ```shell
   zj@ubuntu:~$ echo $PATH   #也可以用${PATH}来获取变量的内容，这种方式更好，边界清晰。由于变量名不能有空格，所以第一种的$后面的单词会被认为是变量名。
   /home/zj/.vscode-server/bin/dfd34e8260c270da74b5c2d86d61aee4b6d56977/bin/remote-cli:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/zj/.local/bin:/home/zj/.local/bin #PATH使用:分隔的多个路径，Windows上的Path使用;分隔。
   zj@ubuntu:~$ echo $hh   #变量hh并没有被设置，但是echo它也不会报错，默认的内容为空。在某些shell中获取一个不存在变量的值会报错。
   
   hh=3    #定义一个变量，此时不需要加$，否则会报错。
   echo 12 34     #会输出12 34，如果要去掉中间的空格，可以用\b转义。\b表示删除光标前的那个字符。
   echo -e "12 \b34"  #但是需要使用-e选项来启用转义功能。结果为1234
   ```

4. 变量的定义和赋值都要符合以下规则：

   1. 等号两边都不能直接接空格，否则会被认为是命令和参数。

   2. 变量名称只能是英文字母，数字和下划线，但不能以数字开头。不能用bash关键字和标点符号。区分大小写。

   3. 变量内容中如果含有空格，可使用单或双引号包括起来，或者使用`\[空格]`转义。

      ```shell
      zj@ubuntu:~$ abc=12\ 3   #变量abc包含4个字符。也可以写为abc="12 3"或abc='12 3'。
      zj@ubuntu:~$ echo $abc
      12 3
      ```

5. 双引号和单引号是有区别的：双引号内的特殊字符如$，可以保持原有的特性；单引号内的特殊字符仅为一般字符，不进行转义：

   ```shell
   zj@ubuntu:~$ echo $LANG   #默认的环境变量，代表系统的语言。
   en_US.UTF-8
   zj@ubuntu:~$ var1="lang is $LANG"
   zj@ubuntu:~$ echo $var1
   lang is en_US.UTF-8
   zj@ubuntu:~$ var2='lang is $LANG'
   zj@ubuntu:~$ echo $var2
   lang is $LANG  #没有进行变量替换
   ```

6. \为转义符，可以为回车，空格，$，\，'，"，等字符转义。

   ```shell
   zj@ubuntu:~$ var=vbird\     #实现对回车的转义，
   > tsai
   zj@ubuntu:~$ echo $var
   vbirdtsai                   #可以发现回车并没有出现在变量内容中
   zj@ubuntu:~$ echo ${#var}   #变量的长度为9个字符。可以认为\[Enter]使回车消失了，好像在没有换行。
   9
   zj@ubuntu:~$ var="lang is \$LANG" #对$进行转义，这样就不会去引用LANG这个变量的值了，这句话等价于单引号的版本。
   zj@ubuntu:~$ name="vbird's name"  #内部有引号的，外部要用不同的引号包括起来，否则会认为没有输入完全。最好的方法就是将实际的引号用\转义,例如
   zj@ubuntu:~$ name=vbird\'s\ name   #将'和空格都进行了转义。
   ```

7. 可以嵌套执行命令，使用\`命令\`或\$(命令)，例如将一个命令的输出作为另一个命令的一部分：

   ```shell
   zj@ubuntu:~$ echo `uname`    #先执行` `内部的命令，然后将命令的输出替换到对应的位置，再执行剩下的命令。
   Linux
   zj@ubuntu:~$ echo $(uname)   #注意和${uname}不一样，括号内的uname被当做命令执行，{}内的uname被当做变量解读。
   Linux
   zj@ubuntu:~$ cd /lib/modules/$(uname -r)/kernel  #进入到内核的模块目录，即/lib/modules/5.15.0-30-generic/kernel
   zj@ubuntu:~$ ll `locate crontab`  #将locate和ll结合，来查看详细的文件信息。
   -rw-r--r-- 1 root root    1.2K Mar 23 13:49 /etc/crontab
   -rw-r--r-- 1 root root    1.2K Feb  2  2020 /snap/core20/1405/usr/share/bash-completion/completions/crontab
   ```

8. 扩增变量内容的常用方法，以PATH为例：

   ```shell
   zj@ubuntu:~$ PATH="$PATH":/home/zj     #在环境变量PATH的末尾添加一个新的目录，要手动添加分隔符:。shell会先计算=右侧的结果，在赋值给左侧变量。必须要用双引号。
   zj@ubuntu:~$ PATH=${PATH}:/home/zj     #结果同上，最推荐使用这个。
   zj@ubuntu:~$ PATH=$PATH:/home/zj       #结果同上，不建议用，因为等号右侧$所取变量之所以是PATH，是因为:不是有效的变量名字符。但不应这样假设其他情况也这么幸运。
   ```

9. export 可以新增，修改和删除环境变量。可以export一个已经存在的变量，或者不存在的，此时会一并定义并export：

   ```shell
   abc=3
   export abc #导出一个已经存在的变量
   export def=4 #定义的同时导出
   ```

10. 使用export来将一个自定义变量导出成环境变量，由于exec时会传递环境变量给子进程，因此就可以在子进程（不一定要是另一个shell）中也使用该变量了。环境变量是隶属于进程的，普通的shell变量是隶属于shell的。除此之外，二者没有区别，都是一样的使用。export的效力仅限于该次登录操作，除非写入到配置文件中。环境变量会存在以所有后代进程，包括孙子进程中。

    ```shell
    zj@ubuntu:~$ var=3      #var不是环境变量，因此在子进程中变量var是未定义
    zj@ubuntu:~$ bash       #进入子进程
    zj@ubuntu:~$ echo $var  #结果为空，因为没有定义过var变量
    
    zj@ubuntu:~$exit        #退出子进程，回到刚才的bash
    exit
    zj@ubuntu:~$ echo $var  #结果为3，变量还在
    3
    #-------------------------------------------------
    zj@ubuntu:~$ var=3      #自定义变量
    zj@ubuntu:~$ export var #将var导出为环境变量,后续在其子进程中也都会有var的定义。
    zj@ubuntu:~$ bash       #进入子进程
    zj@ubuntu:~$ echo $var  #结果为3，var是子进程的环境变量
    3
    zj@ubuntu:~$exit        #退出子进程，回到刚才的bash
    exit
    zj@ubuntu:~$ echo $var  #结果为3，环境变量还在
    3
    zj@ubuntu:~$ export -n var #将var取消设置为环境变量，不过并不会删除该变量，还原为自定义变量。
    zj@ubuntu:~$ bash       #进入子进程
    zj@ubuntu:~$ echo $var  #结果为空，因为var在父进程中不是环境变量了。
    
    zj@ubuntu:~$exit        #退出子进程，回到刚才的bash
    exit
    zj@ubuntu:~$ echo $var  #结果为3，变量还在
    3
    ```

11. 使用unset来取消变量的设置（对环境变量也有效），unset一个未设置的变量不会报错：

    ```shell
    zj@ubuntu:~$ var=3
    zj@ubuntu:~$ unset var
    zj@ubuntu:~$ echo $var    #输出为空
    
    ```

12. 使用env命令来查看当前shell的所有环境变量。export命令的内容相同，只不过形式不同。

    ```shell
    zj@ubuntu:~$ env
    SHELL=/bin/bash  #当前正在使用的shell的路径
    PWD=/home/zj     #当前工作目录(进程属性)
    LOGNAME=zj       #用来登录的账号名
    XDG_SESSION_TYPE=tty
    MOTD_SHOWN=pam
    HOME=/home/zj    #用户的家目录     cd ~就会使用到该环境变量
    LANG=en_US.UTF-8 #语系相关
    LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:  #这里只显示一部分，这个环境变量控制ls命令的颜色。:分隔不同的设置。可以根据文件后缀名来设置不同的颜色。
    SSH_CONNECTION=192.168.80.1 6703 192.168.80.144 22
    LESSCLOSE=/usr/bin/lesspipe %s %s
    XDG_SESSION_CLASS=user
    TERM=xterm     #终端类型
    LESSOPEN=| /usr/bin/lesspipe %s  #控制less的行为
    USER=zj    #使用者的名称
    SHLVL=1
    XDG_SESSION_ID=15
    XDG_RUNTIME_DIR=/run/user/1000
    SSH_CLIENT=192.168.80.1 6703 22
    XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/zj/.local/bin  #PATH
    DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
    SSH_TTY=/dev/pts/0   #SSH的终端设备文件
    _=/usr/bin/env
    #-------------------------------------
    zj@ubuntu:~$ env |wc -l    #统计一下环境变量的个数。
    24
    zj@ubuntu:~$ export |wc -l #export比env少了一个变量，_=/usr/bin/env。这个变量记录着上一个命令的最后一个参数，没有参数的话就记录上一个命令。实际上他并不是环境变量，因为不会被继承到子进程中。
    23
    ```

13. 使用set命令可以查看所有变量，包括环境变量和用户自定义的变量，因此这里的结果比env的多。实际上自定义变量中也不都是由用户定义的，有些是系统的配置脚本定义的。下面都是自定义变量：

    ```shell
    BASH_VERSINFO=([0]="5" [1]="1" [2]="16" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")  #数组标识的版本号,使用${BASH_VERSINFO[4]}来获取数组内的元素，结果为release。
    BASH_VERSION='5.1.16(1)-release'
    HISTFILE=/home/zj/.bash_history     #历史命令记录存储所在的文件。
    HISTFILESIZE=2000                   #存储在文件中的历史命令数量。
    HISTSIZE=1000                       #内存中的历史命令数量。
    HOSTNAME=ubuntu    #计算机的主机名
    HOSTTYPE=x86_64    #主机类型
    IFS=$' \t\n'       #默认的分隔符号
    LINES=11           #当前终端的行数
    COLUMNS=80         #当前终端的列数
    PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '   #命令提示符
    PS2='> '           #当使用\转义[Enter]来将命令分行输入时的命令提示符。
    PS4='+ '           #
    RANDOM=30781       #内置随机数，每个发行版都内置了一个随机数生成器/dev/random，可以通过和这个随机数生成器关联的环境变量RANDOM来获取一个0-32767之间随机数。echo $RANDOM。
    SAVEIFS=$' \t\n'   #
    UID=1000           #用户ID
    $=1791             #当前shell进程的PID,有的shell也用_来存储。echo $$或echo $_可以查看
    ?=0                #刚执行完的命令执行的返回值。正常的返回值为0。
    ```

14. PS1变量，每次执行完命令后，都要读取该变量的值，来显示新的命令提示符。详细的转义字符可以在man bash的PROMPTING一节中找到。

    ```shell
    zj@ubuntu:~$ echo $PS1
    \[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$
    #-------------------这些符号都有特殊的含义，可以设置颜色
    \u  #用户名
    \H  #完整的主机名，例如 study.cemtos.vbrid
    \h  #主机名的第一个小数点之前的名字，主机名一般是域名。例如study
    \w  #完整的工作目录，家目录会以~替换。
    \W  #使用basename函数获取工作目录，仅包含最后一个目录名。家目录也会以~替换。
    \$  #如果有效UID=0,则为#，否则为$。一般作为提示符的最后一个字符。
    \#  #命令的计数
    ```

15. 默认情况下，变量的类型为字符串，因此int1=1+2+3，是不是计算=右边的。bash中只能进行整数间的运算。

16. declare和typeset都可以用来声明变量的类型。如果declare后没有任何参数，则会显示所有的变量，就像set一样。

    ```shell
    declare -a arr1  #将变量定义为数组
    declare -i int1=1+2+3  #将变量定义为整型，int1最终为6。不能先定义int1=1+2+3，然后再declare -i int1，这样不会计算1+2+3的，必须在定义的时候赋值。
    declare -r rovar #将变量设置为只读的，不能修改内容，也不能unset。只读变量不能变回一般变量，没有+r选项。只能通过重新登录来恢复变量的类型。
    declare -x exp1  #将exp1变为环境变量，等价于 export exp1
    declare +x exp1  #将环境变量exp1变为自定义变量。
    declare -p int1  #显示变量的属性和值。如果int1从未设置过，则会报错。根据这个可以区分空值变量和未设置的变量。
    ```

## 变量内容的微调

1. 匹配删除，查找替换，注意以下方法都不会修改变量本身：

   ```shell
   ${变量#关键词}   #从变量内容的开头对关键词进行匹配，将符合条件的最短数据删除。
   ${变量##关键词}  #从变量内容的开头对关键词进行匹配，将符合条件的最长数据删除。也就是贪婪匹配。
   ${变量%关键词}   #从变量内容的末尾对关键词进行匹配，将符合条件的最短数据删除。
   ${变量%%关键词}  #从变量内容的末尾对关键词进行匹配，将符合条件的最长数据删除。也是贪婪匹配。
   ${变量/旧字符串/新字符串}   #在变量内容中查找旧字符串替换新字符串，只有第一个会被替换。
   ${变量//旧字符串/新字符串} #在变量内容中查找旧字符串替换新字符串，所有都会被被替换。注意第二个/还是只有一个
   
   path=/usr/local/bin:/usr/bin:/home/dmtsai/.local/bin:/home/dmtsai/bin
   echo ${path#*:}  #只删除第一项。通配符*匹配任意多个字符，包括0个。匹配到了/usr/local/bin:，因此将其从path中删除，结果为/usr/bin:/home/dmtsai/.local/bin:/home/dmtsai/bin
   echo ${path##*:} #只保留最后一项
   echo ${path%:*}  #只删除最后一项
   echo ${path%%:*} #只保留第一项
   echo ${path/dmtsai/zj} #将第一个dmtsai替换为zj，结果为/usr/local/bin:/usr/bin:/home/zj/.local/bin:/home/dmtsai/bin
   echo ${path//dmtsai/zj} #将所有的dmtsai替换为zj，结果为/usr/local/bin:/usr/bin:/home/zj/.local/bin:/home/zj/bin 
   ```

2. 测试与内容替换，这种工作也可以通过if then来完成：

   ```shell
   #有时候需要判断变量是否设置，如果存在的话就使用它，否则赋予一个新的值。有时也会判断变量是否为空。
   ${str-expr}   #如果str设置，结果为str的值，否则为expr的值。
   ${str:-expr}  #如果str设置且不为空，结果为str的值，否则为expr的值。
   ${str+expr}   #如果str没设置，结果为str的值(也就是空)，否则为expr的值。正好和${str-expr}相反
   ${str:+expr}  #如果str没设置或为空，结果为str的值(也就是空)，否则为expr的值。
   
   ${str=expr}   #如果str没设置，则执行赋值操作，表达式结果为${str}。=和-类似，只是前者会修改str，后者不会。
   ${str:=expr}  #如果str没设置或为空，则执行赋值操作，表达式结果为${str}
   ${str?expr}   #如果str没设置，将expr输出到stderr，否则结果为str的值。
   ${str:?expr}  #如果str没设置或为空，将expr输出到stderr，否则结果为str的值。
   #-----------------------------
   var=0   #var  已设置且不为空
   var1=   #var1 已设置但为空
           #var2 是未设置
   echo ${var-3}   #0
   echo ${var1-3}  #空
   echo ${var2-3}  #3
   echo ${var:-3}  #0
   echo ${var1:-3} #3
   echo ${var2:-3} #3
   #-----------------------------
   echo ${var+3}   #3
   echo ${var1+3}  #3
   echo ${var2+3}  #空
   echo ${var:+3}  #3
   echo ${var1:+3} #空
   echo ${var2:+3} #空
   ```

## 数组

1. 基本操作：

   ```shell
   zj@ubuntu:~$ ARR=(1 2 "hha" 34)   #定义数组，用空格分隔。元素类型任意。等价于 declare -a ARR=([0]="1" [1]="2" [2]="hha" [3]="34")
   zj@ubuntu:~$ ARR=(1,2,"hha",34)   #这个数组只有一个元素，逗号不能用于分隔元素。等价于 declare -a ARR=([0]="1,2,hha,34")
   #读取数组元素的内容
   zj@ubuntu:~$ echo $ARR            #输出为1,相当于echo ${ARR[0]}，输出第0个元素。
   zj@ubuntu:~$ echo ${ARR[2]}       #获取编号为2的元素,即hha
   #数组元素的赋值
   zj@ubuntu:~$ ARR[2]="hehe"        #会修改对应位置的元素。
   zj@ubuntu:~$ ARR[5]=88            #会在对应的位置添加一个新元素。而跳过的ARR[4]依然是空。
   
   zj@ubuntu:~$ ls
   cg  linux  OpenFOAM  test  test.sh  ThirdParty-8-version-8.tar.gz
   ARR=(`ls `)           #将ls输出的内容作为数组元素，一共6个。
   #通过declare -a查看shell中的数组变量。
   zj@ubuntu:~$ declare -a
   declare -a ARR=([0]="cg" [1]="linux" [2]="OpenFOAM" [3]="test" [4]="test.sh" [5]="ThirdParty-8-version-8.tar.gz")
   ```

2. 访问元素，不能省略`{ }`，因为这样会将ARR当作一个单独的变量，[作为前一个变量的结束标志：

   ```shell
   echo ${ARR[@]}     #访问数组中所有元素，等价于echo ${ARR[*]}   这里*匹配任何长度的字符
   echo ${#ARR[@]}    #统计数组中元素的个数。
   echo ${!ARR[@]}    #获取数组元素的索引,当数组跳跃赋值时，索引也是不连续的。
   echo ${ARR[@]:1}   #输出数组中从下标1开始到末尾的所有元素。即ARR[1],ARR[2],...
   echo ${ARR[@]:1:2} #数组数组中从下标1开始的2个元素,即ARR[1]和ARR[2]。
   ```

3. 如果不加声明的使用，就是基本数组，下标只能是序号。关联数组是键值对。

   ```shell
   #逐个赋值
   declare -A ARR   #声明变量ARR为关联数组
   ARR[name]="test" #逐个赋值
   ARR[age]=18
   echo ${ARR[@]}   #输出为18和test,数组元素个数为2。
   #一次性赋值多个
   declare -A ARR1
   ARR1=([name]="test" [age]=18)
   echo ${#ARR1[@]} #
   
   zj@ubuntu:~$ declare -A |grep ARR*   #可以通过declare -A查看已经定义了的关联数组
   declare -A ARR=([age]="18" [name]="test" )
   declare -A ARR1=([age]="18" [name]="test" )
   ```


## 运算

1. 以下都是使用test来进行判断的。test expr 和[ expr ]是相同的。test的基本作用是：判断整数，判断文件，判断字符串。

   ```shell
   test 3 -gt 2 ;echo $?    #0
   [ 3 -gt 2 ];echo $?      #
   ((3>2));echo $?          #
   ```

2. 整数比较大小，一共6种，不能直接使用<之类的符号，只可以使用-lt之类的选项：

   ```shell
   3 -eq 4   #返回false，因为3不等于4,-ne为不等于,-ge为>=,-gt为>,-le为<=,-lt为<。
   test 1 -eq 2;echo $?  #结果为1,即false。test命令只会做判断，不会输出结果。
   test 1 -ne 2;echo $?  #结果为0,即true
   ```

3. 文件的比较和检查：

   ```shell
   -d #检查文件是否存在，且为目录 directory
   -e #检查文件是否存在          exist
   -f #检查文件是否存在，且为文件 file
   -r #检查文件是否存在，且可读   read    读写执行权限的检查对root无效。
   -w #检查文件是否存在，且可写   write
   -x #检查文件是否存在，且可执行 excute
   -s #检查文件是否存在，且不为空 
   -O #检查文件是否存在，且拥有者是否为当前用户  owner
   -G #检查文件是否存在，且当前用户在文件的所属组内 group
   file -nt file2 #检查file1是否比file2新，这里比较的是最后修改时间  newer than
   file -ot file2 #检查file1是否比file2旧                          older than
   file -ef file2 #检查file1和file2的iNode号是否相同。硬链接的两个文件具有相同的iNode号。
   ```

4. 字符串比较运算：

   ```shell
   #字符串记得用引号包括起来
   ==    #检查2个字符串是否相等
   !=    #检查2个字符串是否不等
   -n    #检查字符串是否不为空。
   -z    #检查字符串是否为空。
   ```

5. 逻辑运算：

   ```shell
   #  &&  ||  !   分别表示与或非
   test 1 -lt 2 && test 4 -lt 2;echo $?  #结果为1
   test 1 -lt 2 && test 4 -lt 5;echo $?  #结果为0
   test ! 1 -lt 2;echo $?                #结果为1,对test 1 -lt 2的结果取反。
   #分支语句中使用逻辑运算应该套上[]
   if [ $1 -eq $2 ] && [ $3 -lt $4 ]
   then
   	echo "OK"
   else
   	echo "Not OK"
   fi
   #shell中的逻辑运算都是短路的，可以用它来设置出错报警
   ls || echo "bad"       #当第一个命令执行失败，才会执行第二个命令。
   ls && echo "good"      #当第一个命令执行成功，才会执行第二命令
   ```

6. `[[ ]]`是shell的内置命令。支持字符串的模式匹配。

## 流程控制

1. if判断语句：

   ```shell
   #如果条件为真，则会执行then之后的代码块，否则执行else之后的代码块。也可以只有then代码块。
   if [ 1 -lt 3 ]    #[]前后必须有空格
       then          #只要是单独在一行即可，不一定需要缩进
           ls  #实际执行的代码块可以有多行。
       else
           ls -al  #这里不能使用alias定义的别名，因为不是变量，更不是环境变量。
   fi          #必须要有
   #也可以有递进判断：
   if [ $1 -lt $2 ]
       then
           echo "$1<$2"
       elif [ $1 -gt $2 ]
           then      #任何一个条件语句后都要跟上then
           echo "$1>$2"
       else
           echo "$1=$2"
   fi
   ```

2. if的条件可以用((  ))来计算表达式，也可以用[[  ]]来进行字符串匹配

   ```shell
   if (($1>$2))   #这里需要使用>符号，而不能使用 -gt
       then
           echo "$1>$2"
       else
           echo "$1<=$2"
   fi
   #字符串匹配是否是a开头的。
   if [[ $1 == a* ]]   #[[ ]]前后的空格不可省略
       then
           echo "$1 is a* start"
       else
           echo "$1 is not a* start"
   fi
   ```

3. for循环：

   ```shell
   for i in a bd cc   #会依次将字符串"a" "bd" "cc"赋值给变量i。in后面可以是变量,对于字符串变量，会被用空格拆分开。
   do             #do和done之间是循环体。
           echo $i
   done
   #可以用seq来生成对应的等差数列
   seq 1 9      #1 2 3 .. 9
   seq 1 2 9    #1 3 5 7 9
   seq 9 -1 1   #9 8 7 ... 1
   #类C语言的写法
   for ((i=;i<5;i++))    #for ((;;))表示死循环
   do
   	echo $i
   done
   ```

4. while循环：

   ```shell
   while read i
   do
       echo "$i"
   done < $1     #将命令行参数通过输入重定向传递给read
   ```

5. until循环，类似于do...while循环：

   ```shell
   until [ ]
   do
   	echo "ok"
   done
   ```

6. case多条件分支语句，服务的管理脚本就是判断$1来进行启动，重启等操作的：

   ```shell
   read -p "输入一个数字" N
   case $NUM in
   1)       #当NUM的值为1时，执行下面的代码块，直到;;为止。
   	echo "hha"
   ;;
   2|3|4)  #当NUM的值为2或3或4
   	echo "hhe"
   ;;
   *)
   	echo "huhu"
   ;;
   esac
   ```

7. sleep 3可以让程序睡眠3秒钟。continue可以跳过本次循环，执行下一次循环。break退出最近的循环。break N可以跳出N层循环。

8. Shell的内置变量：

   ```shell
   $*      #代表所有命令行参数，参考IFS
   $@      #代表所有命令行参数，不参考IFS
   $N      #第N个命令行参数,N从0开始
   $#      #命令行参数的个数
   $$      #代表脚本执行的进程号
   $_      #代表最后一个执行的命令
   $-      #当前SHELL的选项，可以有himBH
   ```

## 函数

1. 函数：

   ```shell
   func1 () {  #()内不能写参数.      这一行也可以写为function func1 {
       return 0  #返回值可有可无
   }
   func1 1 2 r    #调用函数,可以传入参数,在函数体内使用$0-3来引用
   ```


## 正则表达式

1. 常见的支持正则的命令有grep，sed，awk。在这些命令意外，特殊字符有自己的含义。

2. 如果^$同时使用就是精确匹配，否则是模糊匹配

   ```shell
   grep -E "^ab" file  #在file文件中搜索,匹配以ab开头，后面任意。也可以用egrep
   egrep "bc$" file    #匹配以bc结尾的字符串
   egrep "^a.c$" file  #a开头,c结尾,中间一个任意字符，除了回车。
   egrep "^ab*c$" file #以a开头,c结尾，中间可以有>=0个b。 ?表示<=1次，+表示>=1次。{3}正好3次，{2,5}表示2到5次,闭区间。
   ```

3. 除了特殊字符外，还支持POSIX字符：

   ```shell
   [:alpha:]   #任意字母,也就是a-z A-Z
   [:digit:]   #任意数字,也就是0-9
   [:alnum:]   #任意字母+数字
   [:graph:]   #非空格的控制字符
   [:lower:]   #小写字母,也就是a-z
   [:upper:]   #大写字母,也就是A-Z
   [:cntl:]    #控制字符
   [:print:]   #可打印的字符
   [:punct:]   #标点符号
   [:blank:]   #空格和tab
   [:xdigit:]  #16进制数字,也就是0-9 a-f A-F
   [:space:]   #所有空白字符，空格，tab，换行
   #使用
   grep -E "^a[[:alnum:]]c$" file   #相当于"^a[0-9a-zA-Z]c$"
   ```

4. ip地址匹配：

   ```shell
   ^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)    #表示三段,第一段为250-255,第二段为200-249,第三段为0-199
   [01]?[0-9][0-9]? #第三段需要认真分析,当两个?都表示没有时，可以匹配0-9;当第一个?表示没有，第二个?表示有时，可以匹配00-99;当第一个?表示有，第二个?表示没有时，可以匹配00-09 10-19这些;当两个?都表示有时,可以匹配000-099 100-199。综上来看这段除了可以匹配0-199，还会多余一些内容。
   ^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3} #加上点,重复3遍。
   ^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$  #补上最后一段，最终版本。
   ```

## sed

1. sed命令是行编辑器，从文件(可以是管道)读入数据，一次处理一行，默认输出到屏幕，不会对源文件进行修改。

   ```shell
   sed [option] "{command}{flags}" [filename]
   #常见的选项option有:
   -r   #使用正则表达式
   -n   #抑制内存输出，一般，防止匹配的行重复打印
   #常见的命令command有:
   a #在匹配后面追加 append
   i #在匹配前插入  insert
   p #打印 print
   d #删除
   s #查找替换
   c #更改,意识是不查找，直接替换
   y #转换,适用于单个字符，一般用来做大小写转换
   / / #开启匹配模式，类似于在每一行中搜索，如果满足就对改行执行操作，这个不开启正则也可以使用，就是普通的搜索。
   #常见的标志flags：
   数字   #替换每行第N个匹配的内容
   g     #用新文本替换现有文本的全部实例
   p     #打印原始内容
   w filename # 将替换的结果写入到文件中
   ```
   
2. 例子，sed的所有命令都是对一行而言的，追加和插入相当于vim的o和O操作，即在当前行的前或后插入一个新行，然后把内容插入进去。匹配模式是对所有行进行匹配，只对满足匹配的行进行后面的操作。都不能在行内进行插入，除非进行整行的修改：

   ```shell
   [zj@manjaro ~]$ cat sedfile      #实例文件内容
   1 the quick brown fox jumps over the lazy dog.
   2 the quick brown fox jumps over the lazy dog.
   3 the quick brown fox jumps over the lazy dog.
   sed "a\hello world" sedfile    #读取sedfile文件，在每一行的末尾追加hello world，这里的末尾是指在换行符后面，即到下一行了。\可有可无。
   1 the quick brown fox jumps over the lazy dog.
   hello world
   2 the quick brown fox jumps over the lazy dog.
   hello world
   3 the quick brown fox jumps over the lazy dog.
   hello world
   sed "i\hello world"  sedfile   #在每行的前面插入
   hello world
   1 the quick brown fox jumps over the lazy dog.
   hello world
   2 the quick brown fox jumps over the lazy dog.
   hello world
   3 the quick brown fox jumps over the lazy dog.
   sed "2i\hello world" sedfile    #只在第2行前面插入,也可以修改为2,4表示在2-4行追加。
   1 the quick brown fox jumps over the lazy dog.
   hello world
   2 the quick brown fox jumps over the lazy dog.
   3 the quick brown fox jumps over the lazy dog.
   sed "/2 the/a\hello world" sedfile     #/ /内部是要匹配的内容。然后再匹配的内容后面追加hello world
   1 the quick brown fox jumps over the lazy dog.
   2 the quick brown fox jumps over the lazy dog.       #这里只有第二行能匹配上。
   hello world
   3 the quick brown fox jumps over the lazy dog.
   sed "2d" sedfile      #删除第二行
   1 the quick brown fox jumps over the lazy dog.
   3 the quick brown fox jumps over the lazy dog.
   sed "s/dog/cat/" sedfile        #将dog修改为cat。
   1 the quick brown fox jumps over the lazy cat.
   2 the quick brown fox jumps over the lazy cat.
   3 the quick brown fox jumps over the lazy cat.
   sed "c\hello world"  sedfile   #这里的更改实际上是将每一行删除，然后再插入上hellworld
   hello world
   hello world
   hello world
   sed "2,3c\hello world"  sedfile     #这里是将2-3行删除，再插入一行。
   1 the quick brown fox jumps over the lazy dog.
   hello world
   sed "y/abc/ABH/" sedfile       #一一对应的转换
   1 the quiHk Brown fox jumps over the lAzy dog.
   2 the quiHk Brown fox jumps over the lAzy dog.
   3 the quiHk Brown fox jumps over the lAzy dog.
   sed "p" sedfile	     #打印输出，即使没有p命令，每一行也会被打印，再加上p命令，因此一共有6行被打印。
   1 the quick brown fox jumps over the lazy dog.
   1 the quick brown fox jumps over the lazy dog.
   2 the quick brown fox jumps over the lazy dog.
   2 the quick brown fox jumps over the lazy dog.
   3 the quick brown fox jumps over the lazy dog.
   3 the quick brown fox jumps over the lazy dog.
   sed "2p" sedfile    #只打印第2行
   1 the quick brown fox jumps over the lazy dog.
   2 the quick brown fox jumps over the lazy dog.
   2 the quick brown fox jumps over the lazy dog.
   3 the quick brown fox jumps over the lazy dog.
   sed -n "2p" sedfile #抑制内存输出。
   2 the quick dog fox jumps over the lazy dog.
   ```

3. 标志：

   ```shell
   [zj@manjaro ~]$ cat sedfile      #要处理的文本
   1 the quick dog fox jumps over the lazy dog.
   2 the quick dog fox jumps over the lazy dog.
   3 the quick dog fox jumps over the lazy dog.
   sed "s/dog/cat/" sedfile         #虽然在每行可以搜索到多个dog，但是默认只替换第一个。
   1 the quick cat fox jumps over the lazy dog.
   2 the quick cat fox jumps over the lazy dog.
   3 the quick cat fox jumps over the lazy dog.
   sed "s/dog/cat/2" sedfile       #替换第二个搜索到的内容,如果只能搜索不到第二个，那么就不会执行替换。
   1 the quick dog fox jumps over the lazy cat.
   2 the quick dog fox jumps over the lazy cat.
   3 the quick dog fox jumps over the lazy cat.
   sed "2s/dog/cat/w mfile" sedfile  #将第二行的第一个dog替换为cat然后修改过的行写入到mfile文件中。
   1 the quick dog fox jumps over the lazy dog.
   2 the quick cat fox jumps over the lazy dog.
   3 the quick dog fox jumps over the lazy dog.
   cat mfile #该文件中只有一行，因为上面的替换操作只有第二行能匹配。
   2 the quick cat fox jumps over the lazy dog.
   ```

4. 选项：

   ```shell
   sed -e "s/dog/brown/;s/lazy/good/" sedfile   #-e可以同时对一行执行多个操作。用分号隔开。
   1 the quick brown fox jumps over the good dog.
   2 the quick brown fox jumps over the good dog.
   3 the quick brown fox jumps over the good dog.
   sed -f sed.sh sedfile  # -f 从文件读入命令
   sed -i "s/dog/brown/" sedfile      #修改在源文件上进行修改,该选项会抑制屏幕输出。
   sed -i.bak "s/dog/brown" sedfile   #将源文件备份为sedfile.bak，在sedfile文件上修改。
   echo "tom zhen shuai" | sed "s/tom/zj/"   #sed命令也支持管道
   zj zhen shuai
   sed -n "$=" sedfile #统计行号
   3
   ```

## awk

1. 可以替代grep，cut，tr命令进行过滤提取运算。

2. awk将文件看做一行一行的，每一行由多个字段组成，分隔符为一个或多个空格，制表符。

   ```shell
   awk  [options] [BEGIN]{program} [END][file]#会按照BEGIN→program→END的顺序进行操作。
   #选项:
   -F            #指定每行的字段分隔符，默认为空格
   -f awk.sh     #从awk.sh文件中读取命令
   -v var=value  #指定可以附加变量和值,可以在awk中使用
   ```

3. 数据提取：

   ```shell
   cat awkfile     #原始数据
   1 the quick brown fox jumps over the lazy cat . dog
   2 the quick brown fox jumps over the lazy cat . dog
   3 the quick brown fox         jumps over the lazy cat . dog
   4 the quick brown fox jumps over the lazy cat . dog
   5 the quick brown fox jumps over the lazy cat . dog
   #$0代表整行,$3代表第3个字段,$NF代表最后一个字段
   awk '{print $2}' awkfile    #这里必须用单引号。
   the
   the
   the
   the
   the
   awk 'NR==3{print $0}' awkfile     #NR==3表示第三行
   3 the quick brown fox         jumps over the lazy cat . dog
   awk 'NR==3{print $1,$3,$5}' awkfile  #打印第3行的1,3,5列。
   3 quick fox
   awk 'NR==3{print $1"-"$3"-"$5}' awkfile  #列之间用"-"拼接,默认为空格
   3-quick-fox
   awk -F ":" 'NR==1{print $NF}' /etc/passwd   #以:为分隔符。也可以写为 -F:
   /bin/bash
   ```

4. BEGIN和END

   ```shell
   #BEGIN指定开始处理数据流之前要做的事情。END指定数据流处理结束后要做的事情。BEGIN没有数据流也能执行，program和END则不行。
   awk 'BEGIN{print "hello"}NR==3{print $0}END{print "world"}'  awkfile   
   hello   #BEGIN的结果
   3 the quick brown fox         jumps over the lazy cat . dog
   world   #END的结果
   awk 'END{print NF}' awkfile   #统计文件一共有多少列
   awk 'END{print NR}' awkfile   #统计文件一共有多少行
   ```

5. awk就是一门语言，可以定义变量和数组。

   ```shell
   [zj@manjaro ~]$ head -2 /proc/meminfo
   MemTotal:        4000552 kB
   MemFree:         3510864 kB
   #通过awk输出内存的使用率
   head -2 /proc/meminfo | awk 'NR==1{total=$2}NR==2{free=$2;print (total-free)*100/total"%"}' #可以将字段赋值给变量。
   12.2401%
   awk 'BEGIN{arr[0]="bai";arr[1]="sm";print arr[0],arr[1]}'   #数组的使用
   bai sm
   #awk支持的运算:=赋值,> >= < <= == !=比较运算,+ - * / % ** ++ --数学运算,&& || ！逻辑运算,~ !~模糊匹配
   awk 'BEGIN{print "a">="b"}'  #结果为假,返回0
   awk 'BEGIN{print "c">="b"}'  #结果为真,返回1
   seq 1 9| awk '$1>=5{print $0}'   #管道传入的内容是9行，每行一个数字。只有满足$1>5的行才会被print。
   5
   6
   7
   8
   9
   awk 'BEGIN{print (1<2 && 4>3)}'  #结果为真,输出为1
   awk 'BEGIN{print !(1<2)}' #结果为假,输出为0
   awk -v "count=4" 'BEGIN{count++;print count}'  #输出为5,定义了一个变量count=4.
   awk -F: '$1=="root"{print $0}' /etc/passwd     #精确匹配
   awk -F: '$1~"ro"{print $0}' /etc/passwd        #模糊匹配,反之可以用!~
   ```

6. awk内置变量：

   ```shell
   awk 'BEGIN{FIELDWIDTHS="5 2 8"}NR==1{print $1,$2,$3}' /etc/passwd  #通过字符个数来分列，第1,2,3列分别为5,2,8个字符宽度。这里不应该在指定分隔符。
   root: x: 0:0::/ro
   awk 'BEGIN{FS=":";OFS="-";RS="\n"}NR==1{print $1,$2,$3}' /etc/passwd   #设置输入的分隔符为:，相当于 -F:。设置输出的分隔符为-。设置输入的行分隔符为\n，一般不会修改这个。如果设置RS="",那么
   root-x-0
   ```

7. 流程控制：

   ```shell
   seq 1 9|awk '{if($1>5)print $0}'
   6
   7
   8
   9
   seq 1 9| awk '{if($1<5)print $1*2;else print $1/2}'  #if和else之间要加分号。
   2
   4
   6
   8
   2.5
   3
   3.5
   4
   4.5
   #for循环
   cat num2
   60 50 100
   150 30 10
   70 100 40
   awk '{sum=0;for (i=1;i<4;i++)sum+=$i;print sum}' num2  #累加一行的各个字段。
   210
   400
   610
   #while循环
   awk '{sum=0;i=1;while(i<4){sum+=$i;i++}print sum}' num2
   210
   190
   210
   ```

## ulimit

1. 根据用户来进行资源管理，ulimit是shell内置功能。

   ```shell
   [zj@manjaro ~]$ ulimit -a #列出所有的限制大小，注意单位，使用对应的选项来修改
   real-time non-blocking time  (microseconds, -R) unlimited
   core file size              (blocks, -c) 0          #转储文件core dump的允许大小，单位为块，0表示不允许生成该文件。
   data seg size               (kbytes, -d) unlimited  #进程数据段的大小上限
   scheduling priority                 (-e) 0          #最大调度优先级，也就是nice值
   file size                   (blocks, -f) unlimited  #可建立的单个文件大小上限，block的大小和文件系统有关。
   pending signals                     (-i) 15115      #等待的信号数量上限
   max locked memory           (kbytes, -l) 497896     #可用于锁定的内存最大大小
   max memory size             (kbytes, -m) unlimited  #驻留集最大大小
   open files                          (-n) 1024       #可以同时开启的文件最大数量
   pipe size                (512 bytes, -p) 8          #管道缓冲区大小
   POSIX message queues         (bytes, -q) 819200     #POSIX消息队列的最大大小。
   real-time priority                  (-r) 0          #实时调度的最大优先级
   stack size                  (kbytes, -s) 8192       #栈的最大大小
   cpu time                   (seconds, -t) unlimited  #可使用的最大CPU时间
   max user processes                  (-u) 15115      #用户进程的最大数量
   virtual memory              (kbytes, -v) unlimited  #虚拟内存大小
   file locks                          (-x) unlimited  #文件锁的最大数量
   #设置
   ulimit -H #严格的限制，绝对不允许超过。
   ulimit -h #警告的限制，允许超过对应值，但会给予警告。因此通常<上面的值。
   ulimit -f 10240  #设置创建的文件最大为10240块，这里1block=1KB，因此限制为10240KB=10MB。
   dd if=/dev/zero of=123 bs=1M count=20  #只会写入10M的内容，同时提示File size limit exceeded (core dumped)
   ```

2. 一般用户只能修改降低自己的限制值，主动降低后就不能提高了。注销重新登陆就能恢复默认的限制值。

3. 如果管理员要管控用户的ulimit值，可以使用pam。



# 重定向

   1. shell命令默认会将结果都显示在屏幕上，无论是执行成功的信息，还是发生错误的信息。实际上这两个信息是流经不同的管道，最后又汇聚到屏幕上，标准输出的文件描述符1，标准错误输出的文件描述符2。可以用输出重定向的方法来将对应的信息保存到文件中。例如：

   2. ```bash
      ls > ls.txt       #命令运行成功,从标准输出直接存储到文件，屏幕上不会有任何消息。>等价于1>
      lsss > ls.txt     #命令运行错误,标准输出没有内容(虽然被重定向)，标准错误输出有内容且没有被重定向，所以输出到屏幕。
      lsss 2> ls.txt    #命令运行错误,标准输出没有内容，标准错误输出有内容且被重定向，所以输出到该文件。
      ```

   3. ```bash
      cat file1 file2 > file3    #合并两个文件。
      #也可以将上面的步骤拆分为两次重定向
      cat file1 > file3
      cat file2 >> file3         #第二个文件需要追加写入。重定向默认是覆盖，而不是追加。>>表示追加。
      ```

   4. ```bash
      >file1      #对于已存在的文件，会被清空内容。对于不存在的文件， 会新建该文件。
      ```

   5. ```bash
      ls > ls.txt 2>&1        #将标准输出重定向到文件，同时将标准错误重定向到标准输出。&不能省略
      ls &> ls.txt            #和上一行有同样的效果，这样任何内容都不会输出到屏幕上了。
      ```

   6. 输出重定向的目标如果为/dev/null，则表示丢弃输出的内容。

   7. 标准输入的文件描述符为0，默认来自于键盘。标准输入重定向是将本来应该有键盘输入的内容改为从文件读取。

   8. ```bash
      read A                 #从键盘输入的内容会作为变量A的值
      
      read B < input.txt     #input.txt文件的内容会作为变量B的值。
      ```

   9. 管道符  |  是将前一个命令的输出作为后一个命令的输入。

   10. 输出和输入重定向的目标和源都只能是文件，不能讲输出重定向到一个命令中。管道符是命令之间传输数据。

   11. ```bash
       grep ed               #该命令会从标准输入中查找对应的内容。
       ls /bin | grep ed     #会从标准输入读入ls命令的输出。
       ```

   12. /dev/null，外号叫无底洞，输入到这里的任何数据都会消失，一般用来丢弃输出的数据，重定向到这里即可。

13. /dev/zero，可以从中读取无限多的0。一般用来初始化文件。

14. 重定向的本质是流的传输。输出重定向到文件时，如果文件不存在，会创建该文件：

    ```shell
    echo haha > ./test.txt  #将echo的输出重定向到./test.txt文件,默认是输出到屏幕,会覆盖原数据。
    cat a.txt >> b.txt      #将a.txt的内容复制追加到b.txt的末尾。>> 是追加到末尾。
    wc -l < /etc/passwd     #将wc命令的输入重定向到一个文件,默认是从键盘接受输入。这里会统计/etc/passwd文件的行数。
    wc -l /etc/passwd       #这里不使用输入重定向流,而是使用文件。
    fdisk /dev/sdb <<EOF    #<< 是追加,交互式的命令需要用到这个。这个命令会在sdb硬盘上新建一个1G的主分区
    n
    p
    3
    
    +1G
    w
    EOF
    ```




# 磁盘分区

1. 各个组件在linux下都是文件，这个是延续自Unix的。硬件的驱动程序一般由厂商提供，linux下一般提供C语言的源文件，用户自行编译；Windows下，一般提供二进制安装文件。驱动一般编译为内核模块 .ko文件。这样的好处是不用重新编译内核。

2. 各个硬件在linux中的文件名，几乎所有的硬件文件都在/dev目录下。

3. 主流硬盘的尺寸分别为3.5和2.5英寸，分别用在台式机和笔记本上。

6. 现在IDE已经被SATA取代，SCSI已经被SAS取代。SAS接口的硬盘主要用在服务器上，比SATA的贵。

8. 一个SATA接口的硬盘和系统有两条线相连，一条是信号线，一条是电源线。目前SATA已经升级到了第3代。理论带宽是6Gbit/s，但是速度为600Mbyte/s，因为每传输10个bit，就有2个是校验用的，另外8个是数据位。因此比率为1：10。而实际SATA3硬盘的速度也就是150~200Mbytes/s左右。

9. USB3.0的实际速度上限在100Mbytes/s左右。

10. 固态之所以比机械硬盘快，是因为机械硬盘寻道需要花费大量的时间。如果数据比较分散，寻道花费时间更多。固态硬盘的接口有SATA和M.2

11. 个人计算机常见的硬盘接口有IDE，SATA，SCSI，SAS。不过近年来为了统一处理，大部分Linux distribution 已经将IDE 界面的磁盘文件名也仿真成跟SATA 一样了。

12. 由于SATA/USB/SAS 等磁盘接口都是使用SCSI 模块来驱动的， 因此这些接口的磁盘装置文件名都是/dev/sd[a-p]的格式。因此==文件名取决于linux侦测到他们的顺序==。主板上的SATA口比USB先被检测到，SATA口之间序号(主板上会标注出)小的，先被检测到。

13. 一个扇区sector的大小一般为512Bytes或者4KBytes（为了适应大容量的硬盘，减少数据量的拆解）。由于内圈的周长小，所以内圈的扇区数量少，因此读写一般先从外圈开始。扇区是最小存储物理单位，即一个文件只能占用整数个扇区的体积，即使用不完，也不能给其他文件使用。

14. 整个磁盘的第一个扇区(编号为0)最重要，他记录了整个磁盘的重要信息，早期其中记录的是MBR(Master Boot Record)。但是MBR格式只能支持2TB以内的硬盘（超过2TB的分区无法识别）。于是有了新的GPT（GUID Partition table）分区。MBR中通过柱面号来记录分区的位置，而GPT通过扇区号来记录。

15. MBR格式是Windows支持的，第一个扇区包括两部分：主引导记录（安装启动引导程序的地方，446Bytes）和分区表（DPT（Disk Partition Table）64Bytes）还有2个字节的校验0x55AA。

16. ![img](Linux学习.assets/v2-039771e933fc23590ca888821fd6903f_720w.png)

17. 因为分区表只有64个字节，最多只能有4个记录区，每个记录区记录了该分区的起始和结束的柱面号。如下例中，一共有400个柱面，1-100，101-200，201-300，301-400。分了4个分区，一个分区100个柱面。

18. ![image-20201127124214617](Linux学习.assets/image-20201127124214617.png)

19. 分区的最小单位是柱面，分区是物理隔离的，所以不同分区的数据不会影响。对硬盘进行分区就是对分区表那64个字节进行设置。

20. 主分区和扩展分区加起来最多有4个，扩展分区最多有1个。扩展分区可以有多个逻辑分区组成。逻辑分区必须连续。扩展分区的目的是使用额外的扇区记录分区信息，其本身并不能被格式化，扩展分区内的逻辑分区记录在扩展分区指向的那个区块。

21. 主分区和逻辑分区可以被格式化，存储数据。逻辑分区编号从5开始，1-4是留给主分区和扩展分区的。

22. ![image-20201127125040317](Linux学习.assets/image-20201127125040317.png)

23. 一个磁盘有多个盘片组成。一个盘片的同心圆上的所有扇区构成一个磁道track。所有盘片上的对应磁道构成一个柱面cylinder。外侧磁道包含的扇区数量更多。

24. 柱面数=磁道数。最初的寻址方式是CHS，柱面（cylinder），磁头（header），扇区（sector）。通过这三个参数，可以索引到具体的扇区。现在都是LBA方式，从0开始，适合硬盘和闪存类的存储设备，方便寻址。

25. ```
    #lba=(#c*H+#h)*S+#s-1
    其中：
    #c、#h、#s分别是柱面、磁头、扇区的编号
    #lba是逻辑区块编号
    H=heads per cylinder，每个磁柱的磁头数，一般为255个
    S=sectors per track，每磁道的扇区数，一般为63个。
    ```

26. <img src="Linux学习.assets/image-20201127133047094.png" alt="image-20201127133047094"  />

27. 以E盘为例，CHS分别为从26110/0/1→73889/254/63。起始LBA为419457150，终止LBA为1187042849，一共包含767585699个扇区，分区大小为366.0GB。

28. 单碟的如果是双面存储，就是两个磁头，如果是单面存储就只有一个磁头。这里显示255个磁头，并不是真有真么多，是因为现在的硬盘，这些参数都是模拟的了。又如每个磁道的扇区数均为63，这也和实际不符，因为外圈磁道的扇区比内圈多。在DG中读取到的磁盘，磁头都是255个，磁道的扇区都是63个，只有柱面数不同。

29. 固态硬盘：

    1. 固态硬盘有颗粒和主控组成，颗粒存储内容，主控负责调度，颗粒有3种，SLC，MLC，TLC。分别是1个存储单元存储1，2，3个bit的数据，TLC的最慢，因为他在找到存储单元后，还要进行存储单元内的bit数据选择。
    2. 固态硬盘和内存连接的总线有两种，SATA（理论速度为600MB/s）和PCI-E总线（速度和具体使用的通道数有关）。
    3. PCI-E总线有x1，x2，x4，x8，x16几种。固态硬盘一般使用x2（理论速度为1GB/s）和x4（1.5~3GB/s）的，可以根据金手指的长度分辨出，另一个使用PCI-E接口的设备是显卡，一般都是x16的。
    4. 固态硬盘的缓存有两种，DDR（和内存一样的），SLC颗粒。一般MLC颗粒的SSD，在缓存用完后都会出现掉速的现象。
    5. 固态硬盘的接口：SATA接口的SSD，走SATA总线；
    6. 走PCI-Ex4总线的SSD如果支持NVME协议，则能达到3GB/s，不支持的，只能达到1.5GB/s。
    8. SSD有两种速度，顺序读写和4KB随机读写速度。顺序读写一般用在读取大文件时，用MB/s标识，4K随机读写用在小文件中，用IOPS标识。
    10. 固态硬盘的容量越大，寿命就越长，它会自动将坏块屏蔽掉。
    9. 机械硬盘的随机读写速度比顺序读写差很多，固态硬盘在这方面就好多了。
    10. 由于少了机械硬盘的转动，固态硬盘更省电。机械硬盘不应该直接拔电源进行关机，因为在不使用时，应该让磁头归位，避免破坏。

# 特殊权限

1. ACL（acess control list）权限，是独立于传统的所有者，所属组，其他人的权限类型。用来解决身份不足的问题的。是一种用户操作文件的权限。

2. 例如：一个工程的文件夹的权限，项目经理为所有者，项目成员在所属组中，权限为rwxrwx---。如果此时有一个其他项目的人要参观，那么需要给他r-x的权限（防止修改增删文件）。这种情况是传统权限解决不了的。

3. 类似于Windows中的方法，单独指定某个用户对某个文件（夹）的权限，而不是使用所有者，所属组方法。

4. 要想使用ACL权限，需要分区的支持。显示acl则表示分区支持ACL。

   ```
   dumpe2fs -h /dev/sda3
   
   Defualt mount options:   User_xattr acl
   ```

5. 临时开启分区的ACL权限。永久生效需要修改/etc/fstab文件。

   ```shell
   mount -o remount,acl /       #重新挂载根分区，并加入acl权限。
   
   UUID=c2ca6f57-b15c-43ea-bca0-f239083d8bd2 / ext4 defaults,acl 1 1
   # 加入ACL
   ```

6. 修改完fstab文件后，重启或者重新挂载文件系统使得修改生效。

7. 一般不会开机自动挂载光盘，因为当没有光盘时会导致启动崩溃。

8. linux的默认的分区挂载选项defaults（可以修改的）中就已经支持acl了。

9. ```shell
   getfacl 文件名      #查看文件的ACL权限
   setfacl 选项 文件名  #设置ACL权限。
   # -m 设定ACL权限
   # -x 删除指定的ACL权限
   # -b 删除所有的ACL权限
   # -d 设定默认ACL权限
   # -k 删除默认ACL权限
   # -R 递归设定ACL权限
   ```

10. ```shell
    setfacl -m u:zj:rx  /project        手动设置权限，给用户zj对文件夹/project设置rx权限。
    普通权限后面多了一个+，表示该文件夹存在ACL权限。
    drwxrwx---+ 2 root tgroup 4096 1月 6 21:02 /project/
    ```

11. ```shell
    getfacl /project       #第一行表示该命令不支持绝对路径的方式。
    #     user::表示所有者。user:st:表示st用户。
    #     group::表示所属组。
    ```

    ![image-20201226101107007](Linux学习.assets/image-20201226101107007.png)

12. mask，最大有效权限，是指用户或组能够拥有的最大ACL权限，不能超过该值。实际的权限是分配的权限和该mask相与后的结果。例如分配的权限是rwx mask为r-x 实际的权限是r-x

13. ```shell
    setfacl -m m:rx /project       #修改该文件夹的mask权限。 只影响ACL权限，不影响传统权限。
    ```

14. ```shell
    setfacl -x u:st /project      #只删除/project文件夹中用户st的ACL权限。
    setfacl -b /project           #删除/project文件夹的所有ACL权限。
    ```

15. 递归设定ACL权限的意思是，在父目录设置里ACL权限，会自动给所有的子文件和子目录也会拥有相同的ACL权限。

    ```shell
    setfacl -m u:st:rx -R /project   #-R要放在后面。
    ```

16. 命令执行后，再加入的文件不会有ACL权限。这种情况需要设置默认的ACL权限，使得该文件夹下所有新来的文件都有指定的ACL权限（默认不递归，也可以配合递归使用）。这个命令并不会改变现有的文件的ACL权限。

17. 如果给父目录设置了默认的ACL权限，那么目录中的新建的文件都会继承父目录的ACL权限。

    ```shell
    setfacl -m d:u:st:rx -R  /project
    ```

18. 文件的特殊权限 SUID SGID SBIT        都是讲可执行文件的x位替换为s。

19. SetUID：只有可执行的二进制程序才可以设置SUID权限。普通的文件和目录设置了没有意义。命令的执行者必须对该程序有x权限。

20. 如果某程序有SUID权限，则任意命令的执行者（对该文件有x权限）在执行该程序时会获得该程序所有者的身份。SUID权限只在程序执行过程中有效。

21. 最常见的就是passwd程序。可以看到该文件设置了SUID，因此所有者的x属性变成了s。

    ```shell
    zj@zjhit:~$ ll /bin/passwd
    -rwsr-xr-x 1 root root 67K Jul 15 06:08 /bin/passwd
    ```

22. 这样的设置，使得普通用户在修改密码时，也可以修改/etc/shadow密码记录文件（权限---------）。

23. 同样cat命令没有SUID权限，所以不可以查看其所有者root才可以查看的/etc/shadow文件。

24. ```shell
    设置方法：
    chmod 4755 文件名     #后三个为传统权限。第一个4表示给文件赋予SUID，2表示赋予SGID。1表示赋予SBIT权限。
    chmod u+s  文件名
    取消方法：
    chmod 755 文件名
    chmod u-s  文件名
    ```

25. 当改文件不是可执行程序时，s会变成S。

26. 用户一般不需要进行SUID设置，更不应该修改系统自带的文件的SUID。

27. 如果给编辑程序vim设置了SUID，那么其他用户都可以用vim程序修改系统的文件了。

28. 应该定期检查系统中的有SUID权限的文件，观察是否有系统默认之外的。

29. SGID除了可以对可执行的文件设置（和SUID类似，任意用户执行时，该用户会变成文件的所属组内的成员，程序结束后则不是），还可以对目录设置。

30. locate程序文件就是有SGID的。locate程序会搜索/var/lib/mlocate/mlocate.db文件。该文件的权限为root:slocate 640。locate文件的权限为root:slocate rwxr-s--x。

31. 任意用户对mlocate.db是没有读取权限的，但是通过locate命令查找的时候，就会变成slocate组的成员，然后就对mlocate文件具有r-x的权限。此时不易赋予SUID，因为这样会使得任意用户变成root，则具有写的权限，不安全。

32. SGID针对目录的作用：普通用户对该目录有rx权限，即可以进入该目录和读取其中的文件。普通用户在进入该目录时，其有效组会变成该目录的所属组。如果该目录的所属组具有w权限，那么普通用户在该目录下新建的文件的所有者为该用户，所属组为该目录的所属组，而不是该用户的组。

33. ```shell
    chmod 7755 文件名       这里第一个数字7表示同时具有SUID,SGID,SBIT。不过这样设置没有意义。
    ```

34. Sticky BIT  粘滞位权限。只能给目录分配。如果普通用户对该目录具有w（删除改名复制粘贴文件）和x（进入目录）的权限，该目录赋予了SBIT，那么普通用户只可以删除该目录下自己建立的文件。root无视这一规定。

35. 如果一个目录有多个用户在使用，通过设置文件的权限，可以让其他用户不能修改自己的文件，但是由于所有其他用户对上一级目录具有写权限，那么就可以删除该用户的文件。有了SBIT就可以妥善保管每个用户的文件。

36. /tmp目录就有SBIT权限。rwxrwxrwt。

# 用户和用户组的配置文件

1. Linux的用户和组还有对应的密码都存储在文件中。用户和组的操作命令实际是修改用户的配置文件。

2. /etc/passwd文件，一行代表一个用户，一共有7列，冒号分割。

   ```shell
   account:password:UID:GID:GECOS:Home Directory:Shell
   
   用户名:密码标志:用户ID:初始组ID:用户的详细信息,备注:家目录:登录之后的shell
   ```

5. 早期的linux中，是直接将密码存放在第二列中，但是现在都存在/etc/shadow（权限为000）中，不过不是明文，是SHA512摘要算法。

6. 密码摘要中的 x表示该用户有密码，如果没有x，则表示没密码，系统登录时，就不会去和shadow文件中的摘要对比。

7. SSH协议对于没有密码的用户，只允许本机登录，不允许远程登录。

8. UID应该唯一（如果两个用户的UID相同，那么他们的任何行为在系统看来是一样）   0为root，1-499为系统用户（伪用户），500-65535都为普通用户。CentOS以1000为界限。

9. linux中用户名为root的用户不一定是管理员，而UID的为0的用户一定是管理员。

10. linux讲一个用户变为管理员，就是把该用户的UID变为0。Windows是讲该用户加入到管理员组内，即修改GID。

11. 伪用户不能删除，他是给系统启动服务用的，不能登录。所有的伪用户的shell都是/sbin/nologin。将普通用户的shell修改为/sbin/nologin，就可以限制其登录。

12. linux中的组分为初始组和附加组。

    1. linux每添加一个新的用户，都会自动创建一个和用户名相同的组，成为初始组，用户在初始组中。每个用户的初始组是可以修改的，但是不建议。
    2. 每个用户可以加入多个组，进而拥有该组对文件的权限。这样的组就是附加组。

13. Windows中新添加的用户都属于users组。

14. /etc/shadow文件是/etc/passwd的影子。9个字段。

15. 用户名：摘要后的密码：密码的最后一次修改日期：修改密码的最小间隔：密码有效期：密码到期前警告的天数：密码到期后的宽限天数：账号的失效时间戳：保留字段，暂时没用。

16. 之前的摘要算法是md5，现在是SHA512。如果第二段为!!或者*则表示没有密码，不能登录。如果想要禁止用户登录，可以在密码摘要前添加！，因为hash512的结果是不会有！的。

17. 密码修改时间用时间戳表示，从1970年1月1日到该时间经历了多少天。

18. 账号的失效和密码不同，账号的有效期到了，不能通过修改密码。这个一般用在计时收费的项目上。

19. 

    ```shell
    date -d "1970-01-01 16066 days"             #把时间戳换算成日期
    2013年12月27日 星期五 00:00:00 CST
    echo $(($(date --date="2014/01/06" +%s)/86400+1))     #把日期换算成时间戳
    16076
    ```

20. 组信息文件/etc/group，每行代表一个组，有4个字段        组名：组密码标志：组ID：组中附加用户

21. 该文件中看不到组的初始用户，初始用户在/etc/passwd文件中。把一个用户添加进某个组中，就是在添加组中附加用户。

22. 组密码保存的文件/etc/gshadow，一般不给组设置密码。组管理员可以代root管理组内的用户。

23. 普通用户的家目录权限为    用户名：用户初始组 700

24. root用户的家目录权限为     root：root  550

25. 把一般用户的初始组ID变成0，并不会是该用户变为管理员。他只是有了文件的权限，组的目的只是为了对文件进行管理。

26. shell 提示符为#表示当前用户为root，为$表示当前用户为一般用户。

27. linux中的邮箱和网络邮箱不一样，是用于系统内的用户发消息的。/vat/spool/mail/用户名是用户的邮箱。

28. /etc/skel为用户模板目录。新建的用户会自动拷贝该目录下的所有文件。

27. useradd 添加新用户，可以用选项设置/etc/password中的各个字段。

    ```shell
    useradd [选项] 用户名  
    # -u UID 指定用户的UID号,否则会自动分配一个可用的最小号(在UID_MIN到UID_MAX之间)。
    # -d 家目录 指定用户的家目录,否则会在/home目录下新建一个和用户名相同的目录。
    # -c 用户说明 指定用户的详细信息备注,否则为空。
    # -g 组名 指定用户的初始组。
    # -G 组名 指定用户的附加组
    # -s shell路径 指定用户的登录shell,默认为/bin/shell
    ```

30. useradd 然后passwd，用户才算创建完成。会修改4个文件（passwd shadow group gshadow），新增一个目录（家目录），新增一个文件（邮箱）

29. 用户的默认值文件，/etc/default/useradd  现在的linux多为私有模式，用户默认组ID就是用户ID。

    ```shell
    GROUP=100      #用户默认组
    HOME=/home     #用户家目录
    INACTIVE=-1    #密码过期宽限天数(shadow文件中第7个字段)
    EXPIRE=        #密码失效时间(shadow文件中第8个字段)
    SHELL=/bin/sh  #默认的shell
    SKEL=/etc/skel #模板目录
    CREATE_MAIL_SPOOL=yes #是否建立邮箱
    ```

30. shadow文件中的其他字段由/etc/login.defs文件定义。

    ```shell
    PASS_MAX_DAYS 99999 #密码最长有效期(shadow文件中第5个字段)
    PASS_MIN_DAYS 0 #密码最小修改间隔
    PASS_MIN_LEN 5 # 密码最小5位,这一字段已经被废弃,现在由pam来管理。
    PASS_WARN_AGE 7 #密码到期前7天开始警告。
    UID_MIN 1000 # 最小和最大的UID范围
    UID_MAX 60000
    GID_MIN 1000 # 最小和最大的GID范围
    GID_MAX 60000
    ENCRYPT_METHOD SHA512 #密码的加密模式,一般都是单向的摘要算法。
    ```

37. Linux-PAM(linux可插入认证模块)是一套共享库，使本地系统管理员可以随意选择程序的认证方式。换句话说，不用(重新编写)重新编译一个包含PAM功能的应用程序，就可以改变它使用的认证机制. 这种方式下，就算升级本地认证机制，也不用修改程序。

32. 如果没有设置密码的，不能登录该用户，也不能切换到该用户。

33. ```shell
    passwd [选项] 用户名
    # -S 查询用户的密码状态(就是shadow文件中的字段),普通用户只能查询自己的，root可以查询所有人的。
    # -l 暂时锁定用户,仅root可用
    # -u 解锁用户,仅root可用
    # --stdin 从标准输入中读入用户的密码,一般配合管道符|来使用。
    ```

34. passwd 不加用户名表示该自己的密码，只要root才可以改其他人的密码，passswd 用户名  即可。

35. 普通用户自己改密码需要输入当前密码，root不用。

36. 普通用户不可以设置简单密码，root可以。密码可以包含非显示字符，例如退格键。

37. 锁定密码其实就是在shadow文件的密码摘要字段，添加!!。

38. --stdin的方法用在shell编程时，批量生成用户和密码。不过会留下明文，可以要求每个用户登录后修改自己的密码。

39. usermod可以修改用户信息。  UID，附加组等。和useradd的选项差不多。

40. chage修改用户密码状态：

    ```shell
    -l       #列出用于的详细密码状态
    -d 日期  #修改密码最后一次的更改日期(shadow的第3个字段)
    -m 天数  #两次密码修改的间隔(4字段)
    -M 天数  #密码有效期(5字段)
    -W 天数  #密码过期前警告的天数(6字段)
    -I 天数  #密码过期后宽限的天数(7字段)
    -E 日期  #账号失效的时间(8字段)
    ```

41. ```shell
    chage -d 0 用户名      #将最后一次修改密码的日期设为1970年1月1日。这意味着用户一登录就要修改密码。一般可以直接修改配置文件，这个命令可以用于批量创建新用户时，设置简单的密码，强制用户登录后必须修改密码，然后再登录才可以。
    ```

42. ```shell
    userdel -r 用户名   #删除用户，并删除其家目录
    id 用户名           #查看用户的UID,GUID和附加组
    ```

43. su切换身份，普通用户之间相互切换，普通用户切换为root都需要密码。root切换为普通用户不需要密码。

44. ```shell
    su 用户名        #输入密码后即可切换到该用户。不切换环境变量
    su - 用户名      #输入密码后即可切换到该用户。切换环境变量
    exit 或者Ctrl+D可以退出当前环境。
    su - root -c "useradd user3"     #切换一次执行命令，命令结束后立即切换回来。
    ```

45. 用户组管理命令：

46. ```shell
    groupadd -g GID 组名                #添加新用户组(空组，没有任何用户)，指定GID。不指定的话，在已有的顺序追加。
    groupmod -g GID -n 新组名  组名      #修改GID或组名，一般不建议修改，可以删除后新建。
    groupdel 组名                       #如果组的初始用户还存在，不能删除。如果只有附加用户，可以删除组，附加用户不受影响。
    gpasswd -a 用户名 -d 用户名 组名     #把用户加入组，或把用户从组中删除。修改的都是附加用户。
    ```

47. 文件系统属性权限chattr。设置的属性针对root用户也有效（提示权限不足）。不过root可以修改chattr，然后在操作。

    ```shell
    chattr [+-=] [选项] 文件名或目录    #添加，删除，赋予权限。
    lsattr [选项] 文件名或目录          #查看文件系统属性   -a 查看所有的文件和目录 -d 只显示目录，不显示其中的文件。这两个参数和ls一样。
    ```

48. 文件夹的内容保存的就是文件名等信息。

49. i属性，可以防止误操作：

    1. 对文件来说，不允许删除文件，重命名，不能修改文件的内容，即文件的任何都不可以修改，相当于把文件锁定起来了。
    2. 对目录来首，只能修改目录下的文件的数据，但不允许新建或删除文件。

50. a属性，不能用VIM编辑，因为无法判断是否是追加，只能用 >> 重定向：

    1. 对文件来说，只能在文件中增加数据，不能删除或修改数据。但是可以删除文件或重命名。
    2. 对目录来说，不能删除文件，只能新建或修改现有的文件。

51. linux中 > 表示覆盖原文件内容（文件的日期也会自动更新），>> 表示追加内容（会另起一行，文件的日期也会自动更新）。echo 333 >> a.txt   追加内容。

53. chattr不是用来限制root用户的操作的(SELinux)，是防止用户误操作的。

54. sudo权限，也称为系统命令权限。操作对象为系统命令。可以帮助root授权普通用户管理系统。不用告诉普通用户管理员的密码。

55. visudo命令可以用默认编辑器打开/etc/sudoers文件。root将一些命令授权给普通用户，然后普通用户才可以使用对应的命令。

    ```shell
    root ALL=(ALL)  ALL
    #用户名 被管理主机的地址=(可使用的身份) 授权命令(绝对路径)
    %wheel ALL=(ALL) ALL            #第一个字段可以是组名，之前要加%。
    ```

56. 这里被管理的主机地址可以是网段或IP地址。这个和远程登录的IP没有关系。ALL就是本机IP。

57. 可使用的身份指的是sudo的时候讲前面的用户转变为那个用户。可以省略

58. ```shell
    sc    ALL=    /sbin/shutdown -r now    #指定sc用户可以在本机上使用sudo来重启。也可以不写命令的选项，那么sc用户可以执行任意选项。
    ```

59. 授权后的用户可以使用sudo +原命令来执行管理员赋予的命令。sudo -l 可以查看管理员赋予的命令。

60. 不能将VIM等编辑程序赋予普通用户，否则他将可以编辑重要文件。



# 文件系统管理

1. 对于一块新的硬盘，在使用前需要先分区（fdisk），再格式化（mkfs.ext4），最后挂载（mount）。

2. 每个硬盘都要建立一个分区表，可以是MBR或GPT类型的。MBR分区表中，主分区+扩展分区最多有4个，其中扩展分区只能有一个。扩展分区的提出是为了弥补分区数量的不足。扩展分区不能存储数据和格式化，只能在里边划分逻辑分区。

3. 逻辑分区的分区号默认从5开始。前4个只能留给主分区和扩展分区。例如一个主分区sda1，其余的空间都是扩展分区sda2，扩展分区内又有三个逻辑分区sds5/6/7。

4. 给分区格式化就是写入文件系统。ext3相比ext2增加了日志功能，可以在崩溃后进行恢复。现在常用的有ext4和xfs。

5. 使用df命令(display filesystem)查看文件系统，只有存在文件系统的分区才会显示在这里：

   ```shell
   [root@ZJ ~]# df -Th      #-T显示文件系统类型，-h方便人为查看。
   文件系统               类型      容量  已用  可用 已用% 挂载点
   devtmpfs               devtmpfs  1.5G     0  1.5G    0% /dev
   tmpfs                  tmpfs     1.5G     0  1.5G    0% /dev/shm
   tmpfs                  tmpfs     1.5G  8.8M  1.5G    1% /run
   tmpfs                  tmpfs     1.5G     0  1.5G    0% /sys/fs/cgroup
   /dev/mapper/cl_zj-root xfs        76G  3.5G   73G    5% /
   /dev/nvme0n1p1         xfs       2.0G  305M  1.7G   15% /boot
   tmpfs                  tmpfs     299M     0  299M    0% /run/user/1000
   ```

6. 使用du命令(disk usage)查看目录或文件实际占用的大小。对于目录来说，使用ll查看到的只是其中保存的子目录的名称所占用的空间。du命令会扫描目录下的所有文件，不建议在服务器高负载时执行。

   ```shell
   [root@ZJ ~]# du -sh /etc    #-s只看该目录，不查看子目录的。-h方便人为查看。
   23M     /etc
   ```

7. df是在文件系统的层面查看，看剩余空间更准确。du是在文件的层次查看，看文件大小更准确。

8. ```shell
   [root@ZJ ~]# df
   文件系统               类型      容量  已用  可用 已用% 挂载点
   devtmpfs               devtmpfs  1.5G     0  1.5G    0% /dev
   tmpfs                  tmpfs     1.5G     0  1.5G    0% /dev/shm
   tmpfs                  tmpfs     1.5G  8.8M  1.5G    1% /run
   tmpfs                  tmpfs     1.5G     0  1.5G    0% /sys/fs/cgroup
   /dev/mapper/cl_zj-root xfs        76G  3.5G   73G    5% /
   /dev/nvme0n1p1         xfs       2.0G  305M  1.7G   15% /boot
   tmpfs                  tmpfs     299M     0  299M    0% /run/user/1000
   [root@ZJ ~]# du /
   du: 无法访问'/proc/1833/task/1833/fd/4': No such file or directory
   du: 无法访问'/proc/1833/task/1833/fdinfo/4': No such file or directory
   du: 无法访问'/proc/1833/fd/3': No such file or directory
   du: 无法访问'/proc/1833/fdinfo/3': No such file or directory
   3.2G    /      #可以看到根目录下所有文件一共有3.2G。他应该等于根分区和boot分区所有文件所占大小的和，即3.5G+305M。实际上df内统计的使用量不仅包含分区内的文件，还包含系统占用的各种分块数据。
   ```

9. 使用fsck修复文件系统，这个一般不用用户自己执行，而是在每次开机时会自动执行。

10. 使用dumpe2fs查看ext2/3/4文件系统的状态信息，命令中的e2指的是ext2；对于xfs文件系统，应使用xfs_info查询。

    ```shell
    [root@ZJ ~]# xfs_info /boot
    meta-data=/dev/nvme0n1p1         isize=512    agcount=4, agsize=131072 blks
             =                       sectsz=512   attr=2, projid32bit=1
             =                       crc=1        finobt=1, sparse=1, rmapbt=0
             =                       reflink=1
    data     =                       bsize=4096   blocks=524288, imaxpct=25
             =                       sunit=0      swidth=0 blks
    naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
    log      =internal log           bsize=4096   blocks=2560, version=2
             =                       sectsz=512   sunit=0 blks, lazy-count=1
    realtime =none                   extsz=4096   blocks=0, rtextents=0
    
    ```

11. 磁盘碎片整理的作用是尽量将文件的块移动到一起，加快读取速度。

12. ```shell
    mount [-t 文件系统] [-L 卷标] [-o 特殊选项] 设备文件名 挂载点
    ```

13. 挂载命令mount，只能作用于分区，不能作用于整个硬盘：

    ```shell
    [root@ZJ ~] mount #不加任何参数表示查看当前系统已经挂载的设备，-a 根据/etc/fstab进行挂载。
    sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime,seclabel)
    proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
    devtmpfs on /dev type devtmpfs (rw,nosuid,seclabel,size=1511024k,nr_inodes=377756,mode=755)
    ...
    /dev/mapper/cl_zj-root on / type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota)  #挂载为根目录，可读可写。
    /dev/nvme0n1p1 on /boot type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota)
    ```

14. 光盘的文件系统为iso9660，Windows的fat16分区使用fat，fat32分区使用vfat。

15. -o 特殊选项。多个选项之间用逗号分隔。remount适用于修改了文件系统的挂载选项后，可以重新挂载使其生效。

16. <img src="Linux学习.assets/image-20210421231537585.png" alt="image-20210421231537585" style="zoom:80%;" />

17. Linux默认使用atime选项，即每次在磁盘上读取或写入数据时都会产生一个记录，这是为服务器设计的，对桌面意义不大。

18. /etc/fstab文件的例子：

    ```shell
    # /etc/fstab: static file system information.
    # <file system> <mount point>   <type>  <options>       <dump>  <pass>
    UUID=3b0fd5f5-d371-48ef-8709-75650a37aee5 / ext4 errors=remount-ro 0       1
    /swapfile none swap sw 0 0
    /dev/sdb2 /media/zj/数据 ntfs defaults 0 0
    ```

19. 第一列可以使设备文件名，也可以使用设备的UUID或者label(文件系统标签)。第一种方法和磁盘的顺序有关，如果插拔设备，更换位置可能会导致挂载无效。UUID是mkfs.\*工具在写入文件系统时生成的。可以通过lsblk -f 来查看所有分区的UUID和label，或者使用blkid /dev/sda1查询某个分区的UUID：

    ```shell
    zj@zj-hit:~$ lsblk -f
    NAME   FSTYPE   LABEL UUID FSAVAIL FSUSE% MOUNTPOINT
    sda                                                                       
    └─sda1 ext4 3b0fd5f5-d371-48ef-8709-75650a37aee5 87.7G 15% /
    sdb                                                                       
    ├─sdb1 ntfs 系统 7C6A67921935CFCC
    └─sdb2 ntfs 数据 F50F52CBBB8B0B1C 298.3G 9% /media/zj/数据
    
    zj@zj-hit:~$ blkid /dev/sda5
    /dev/sda5: UUID="2f47cd6b-0f70-4be0-aacd-778491914ac8" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="8f6186d2-1de8-40e8-9d6b-a59dc763dead"
    ```

20. \<dump\>表示该分区是否会被dump命令作用，dump是一个用来给分区做备份的命令，默认为0，表示不做备份。

21. \<pass\>表示是否检验扇区，默认为0，不检验。开机的过程中，系统默认会以fsck检验我们系统是否为完整（clean）。当其值为0时，永远不检查；而 / 根目录分区永远都为1。其它分区从2开始，数字越小越先检查，如果两个分区的数字相同，则同时检查。

22. tmpfs 是一个临时文件系统，驻留于你的交换分区或是内存中（取决于你的使用情况）。使用它可以提高文件访问速度，并能保证重启时会自动清除这些文件。经常使用 tmpfs 的目录有 /tmp, /var/lock and /var/run. 不要将之使用于 /var/tmp, 因为这一目录中的临时文件在重启过程中需要被保留。

23. 硬盘的挂载是系统在开机阶段自动进行的（根据/etc/fstab配置文件）。挂载的作用是将设备文件名和目录树联系起来。通过访问挂载目录来访问设备中的内容。

24. U盘和光盘一般不推荐进行自动挂载，因为不能保证这些设备每次开机都存在，如果不在的话，可能会启动失败。

25. 如果挂载的路径中有空格，可以使用 "\040" 转义字符来表示空格。外部设备在插入时挂载，在未插入时忽略。这需要`nofail`选项，可以在启动时若设备不存在直接忽略它而不报错.例如：

    ```shell
    UUID=47FA-4071 /home/username/Camera\040Pictures vfat  defaults,noatime 0 2
    ```

26. dump 工具通过它决定何时作备份。

27. 

28. 内核必须在编译时就加入对特定文件系统的支持。所有分区都必须得格式化为内核支持的一种文件系统才可以使用。内核在不同的文件系统上还添加了一层虚拟文件系统VFS，以提供统一的编程接口。

    ```shell
    ext      #Linux扩展文件系统，最早的Linux文件系统
    ext2     #第二扩展文件系统，在ext的基础上提供了更多的功能
    ext3     #第三扩展文件系统，支持日志功能
    ext4     #第四扩展文件系统，支持高级日志功能
    hpfs     #OS/2高性能文件系统
    jfs      #IBM日志文件系统
    iso9660  #ISO 9660文件系统（CD-ROM）
    minix    #MINIX文件系统
    msdos    #微软的FAT16
    ncp      #Netware文件系统
    nfs      #网络文件系统
    ntfs     #支持Microsoft NT文件系统
    proc     #访问系统信息
    ReiserFS #高级Linux文件系统，能提供更好的性能和硬盘恢复功能
    smb      #支持网络访问的Samba SMB文件系统
    sysv     #较早期的Unix文件系统
    ufs      #BSD文件系统
    umsdos   #建立在msdos上的类Unix文件系统
    vfat     #Windows 95文件系统（FAT32）
    XFS      #高性能64位日志文件系统
    ```


# 进程管理

   1. 集群服务器的运维可以使用专门的监控服务器来管理。

   2. ps命令查看系统中所有的进程，ps aux更常用：

          1. ps aux    查看系统中所有的进程，使用BSD系统的命令格式，不加-。 a 表示所有前台进程，x 表示所有后台进程，u 查看产生进程的用户。
          2. ps -le     查看系统中所有的进程，使用linux标准命令格式。 -l 是显示详细信息 -e 是显示所有进程。

   3. ```shell
      USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
      root           1  0.0  0.4 179532 13724 ?        Ss   18:49   0:02 /usr/lib/systemd/systemd --switched-root --system --deserialize 16
      root           2  0.0  0.0      0     0 ?        S    18:49   0:00 [kthreadd]
      root           3  0.0  0.0      0     0 ?        I<   18:49   0:00 [rcu_gp]
      root           4  0.0  0.0      0     0 ?        I<   18:49   0:00 [rcu_par_gp]
      ...
      root         999  0.0  0.0      0     0 ?        I<   18:49   0:00 [kworker/0:1H-kblockd]
      root        1527  0.0  0.3 158120 11576 ?        Ss   18:50   0:00 sshd: zj [priv]
      zj          1535  0.0  0.3  93980  9716 ?        Ss   18:50   0:00 /usr/lib/systemd/systemd --user
      zj          1539  0.0  0.1 248880  4776 ?        S    18:50   0:00 (sd-pam)
      zj          1545  0.0  0.2 158120  6160 ?        R    18:50   0:04 sshd: zj@pts/0
      zj          1546  0.0  0.2 237212  7624 pts/0    Ss   18:50   0:00 -bash
      root        3999  0.0  0.2 336972  6276 pts/0    S    20:17   0:00 su
      root        4003  0.0  0.1 237744  6116 pts/0    S    20:17   0:00 bash
      ```

   4. 一行表示一个进程：

          1. %MEM：当前进程占用物理内存的百分比。
          2. VSZ：当前进程占用虚拟内存的大小，单位是KB。
          3. RSS：当前进程占用物理内存的大小，单位为KB。
          4. TTY：当前进程是由哪一个终端产生的，绝大多数的系统进程不是由终端产生的。
          5. STAT：当前进程的状态，R表示正在运行，S表示正在睡眠，T表示处于停止状态。s表示包含子进程，+表示位于后台。可以看到绝大多数的进程都处于休眠状态。
          6. START：当前进程的启动时间，如果超过一天，则会显示日期。
          7. TIME：进程占用CPU的运行时间。
          8. COMMAND：产生此进程的命令名

   5. linux的终端有tty1-6（本地字符终端），tty7(本地图形终端)，pts/0-255代表虚拟终端，远程登录来的。各终端之间没有区别的，他就是为了方便用户的登录。如果在本地想要演示多个登录用户时，可以通过切换不同的终端来完成。还有就是如果一个中断中的程序卡死了，可以切换到其他中断，使用root登录，杀死该进程即可。

   6. 使用Ctrl+Alt+F1-7来切换不同的终端。

   7. top程序可以查看系统的健康状态。默认每3秒更新一次，使用-d参数修改。进程默认按照CPU的占用率排序。类似于Windows的任务管理器。

   8. ```shell
      top - 21:53:55 up  3:04,  1 user,  load average: 0.00, 0.00, 0.00
      Tasks: 208 total,   1 running, 207 sleeping,   0 stopped,   0 zombie
      %Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
      MiB Mem :   2987.4 total,   2168.3 free,    293.7 used,    525.4 buff/cache
      MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   2453.5 avail Mem
      ```

   9. 21:53:55表示系统的当前时间，up后面是当前系统运行的时间，精确到分钟。1 user 表示当前登陆了一个用户。

   10. load average后面的三个数字分别表示系统在之前的1，5，15分钟内的平均负载。一般以逻辑核数作为参考。

   11. 第一行的输出结果，可以使用uptime查看。

   12. zombie，僵尸进程指的是进程正在终止，但是没有终止完成。一般过一会再看就没了，如果没有，则需要手动杀死。

   13. 第三行描述的是CPU的使用情况，us用户模式占用，sy系统模式占用，ni改变过优先级的进程占用，id空闲CPU，wa等待输入输出的进程占用。hi，si分别表示硬，软中断请求服务占用CPU的百分比。st表示虚拟时间占用，和虚拟机相关的。最重要的是id字段，CPU的空闲<20%则表示负载较大。

   14. 第四行描述的是物理内存的使用情况，total=free+used+buff/cache。单位是MB。

   15. 第五行描述的是虚拟内存的使用情况，total=free+used。单位是MB。

   16. top命令和任务管理器本身都是比较耗费资源的。

   17. pstree查看进程树，查看父子进程关系。-p显示进程的PID 。 -u 显示进程所属的用户。

   18. buffer和cache的区别：

   19. buffer是缓冲，cache是缓存。二者的存在是由于内存和硬盘之间的速度存在较大的差异。一般来说内存从硬盘中读取的数据使用完后，不会立刻丢弃，还会滞留一会，为了下次使用更方便。而缓冲一般用在需要频繁写入硬盘时，可以先将内容写入到缓冲中，积累够一定的数据后再一次性写入硬盘。

   20. CPU中也有一二三级缓存，分别称为L123。缓存和缓冲的空间是不能分配给进程的，只能有linux内核调配。

   21. 终止进程的命令，父进程被终止时，子进程也会终止。

          ```shell
          kill -l   #查看可用的进程信号
          1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
          6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
          11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
          16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
          21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
          26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
          31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
          38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
          43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
          48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
          53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
          58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
          63) SIGRTMAX-1  64) SIGRTMAX
          kill 进程号 -信号代号    #默认发送15号信号，正常结束信号
          ```

   22. 常用信号的含义：

             ```shell
          1 SIGHUP   #该信号让进程立即关闭，然后重新读取配置文件后重启
          2 SIGINT   #该信号让程序终止，用于终止前台进程，相当于Ctrl+C
          8 SIGFPE   #该信号在发生指明的算数运算错误时发出，不仅包括浮点运算错误，还包括除数为0的其他所有算数错误。
          9 SIGKILL  #该信号用来立即结束程序的运行，本信号不能被阻塞、处理和忽略。一般用于强制终止进程。
          14 SIGALRM #时钟定时信号。调用alarm函数后，会在指定秒数后收到该信号。
          15 SIGTERM #该信号用来正常结束进程，kill命令默认发送该信号。有时当进程已经发生问题时，该信号是无法正常终止进程的，需要发送SIGKILL才可以终止。
          18 SIGCONT #该信号可以让暂停的进程恢复执行，不能被阻断。
          19 SIGSTOP #该信号可以暂停前台进程，相当于Ctrl+Z，不能被阻断。
             ```

   23. killall命令可以给同名的所有进程发送信号，和pkill的功能相同：

          ```shell
          killall -9 httpd    #给所有的进程名为httpd的进程发送信号。-i 表示交互式的，会逐个询问。-I表示忽略大小写区别。
          ```

   24. 可以通过kill用户的登录进程来将特定的用户踢出服务器。还可以通过pkill -9 -t tty1来根据终端名称踢特定的用户。

   25. 一般来说，应该先通过systemctl来关闭服务，进而关闭进程。只有这样无法终止的进程，才会使用kill。

# 工作管理

   1. 使用&或Ctrl+Z都可以将进程放入后台：

      ```shell
      tar -zcf etc.tar.gz /etc &      #将进程放入后台运行，进程仍然会执行。
      top  Ctrl+Z                     #将进程放入后台暂停，直到被切换到前台才会恢复运行。
      ```

   2. 可以将执行耗时的进程放到后台执行，这样不耽误用户继续使用shell。

   3. jobs命令可以查看后台的进程，-l，显示PID。

      ```shell
      [zj@ZJ ~]$ jobs -l
      [1]-  5017 Stopped (signal)        top     #使用&放入后台的。
      [2]+  5018 Stopped                 neofetch  #使用Ctrl+Z放入后台的。
      #工作号为1。+表示这是最后一个放入后台的工作，也是默认最先恢复的。-表示这是倒数第二个放入后台的工作。
      ```

   4. 使用fg命令将后台工作恢复到前台：

      ```shell
      fg %1   #将工作号1的工作，恢复到前台执行。%可以省略。
      bg %1   #将工作号1的工作，放到后台执行。 不过有些进程例如top,vim需要和用户交互，在后台就无法执行。压缩，打包，查找之类的就可以放到后台执行。
      
      [zj@localhost ~]$ jobs
      [3]+ Stopped           top
      [4]- Running           tar -zcf root.tar.gz / &
      ```

# 系统资源查看

   1. vmstat命令监控系统资源：

      ```shell
      [zj@ZJ ~]$ vmstat 2 3     #每隔两秒输出一次，一共输出三次。输出的内容和top命令类似。
      procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
       r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
       1  0      0 2542004   3164 232828    0    0   516   103  196  242  3  3 90  4  0
       0  0      0 2541824   3164 232860    0    0     0     0   71  125  0  0 100  0  0
       1  0      0 2541792   3164 232860    0    0     0    26   65  115  0  0 100  0  0
      ```

   2. dmesg命令查看开机自检信息，几乎所有的硬件信息都在这里，一般会联合grep搜索：

      ```shell
      [zj@ZJ ~]$ dmesg    #开机时在屏幕上显示的信息会被存储起来，使用该命令查看。
      [    0.000000] Linux version 4.18.0-240.22.1.el8_3.x86_64 (mockbuild@kbuilder.bsys.centos.org) (gcc version 8.3.1 20191121 (Red Hat 8.3.1-5) (GCC)) #1 SMP Thu Apr 8 19:01:30 UTC 2021
      [    0.000000] Command line: BOOT_IMAGE=(hd0,msdos1)/vmlinuz-4.18.0-240.22.1.el8_3.x86_64 root=/dev/mapper/cl_zj-root ro crashkernel=auto resume=/dev/mapper/cl_zj-swap rd.lvm.lv=cl_zj/root rd.lvm.lv=cl_zj/swap
      [    0.000000] Disabled fast string operations
      ```

   3. free命令查看内存的使用状态：

      ```shell
      [zj@ZJ ~]$ free -h   #-bkmg 分别以B,kB,MB,GB作为单位显示，默认是kB，进制都是1024。-h会选用合适的单位。
                    total        used        free      shared  buff/cache   available
      Mem:          2.9Gi       276Mi       2.4Gi        16Mi       302Mi       2.4Gi
      Swap:         2.0Gi          0B       2.0Gi
      #used是linux真正占用的内存。buff/cache是用于缓冲和缓存的内存大小。二者相加才是真正已经使用了的内存空间。
      ```

   4. cat /pro/cpuinfo查看CPU的信息，该文件存在于内存中，启动初始化后，存在该位置：

      ```shell
      [zj@ZJ ~]$ cat /proc/cpuinfo
      processor       : 0
      vendor_id       : GenuineIntel
      cpu family      : 6
      model           : 158
      model name      : Intel(R) Core(TM) i5-9400F CPU @ 2.90GHz
      stepping        : 10
      microcode       : 0xb4
      cpu MHz         : 2904.002
      cache size      : 9216 KB  #L2二级缓存大小。
      physical id     : 0
      ...
      processor       : 1
      vendor_id       : GenuineIntel
      cpu family      : 6
      model           : 158
      model name      : Intel(R) Core(TM) i5-9400F CPU @ 2.90GHz
      stepping        : 10
      ...
      processor       : 2  #可以看到有三个核心
      vendor_id       : GenuineIntel
      cpu family      : 6
      model           : 158
      model name      : Intel(R) Core(TM) i5-9400F CPU @ 2.90GHz
      ```

   5. uptime查看开机时间，运行时间和平均负载，和top，w命令的第一行类似。

   6. uname查看内核相关信息，/etc/redhat-release查看redhat系列发行版的信息。

      ```shell
      [zj@ZJ ~]$ uname -a    #显示全部的信息,第二个字段为主机名,存储在/etc/hostname中,-r显示内核版本。
      Linux ZJ.HIT 4.18.0-240.22.1.el8_3.x86_64 #1 SMP Thu Apr 8 19:01:30 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
      #内核版本中的el8_3表示RHEL8.3。x86_64表示x86架构的64位。如果是i686之类的，则是32位。
      ```

   7. 也可以通过file一下可执行文件来查看操作系统的位数。一般的系统命令文件的位数就是OS的位数：

      ```shell
      [zj@ZJ ~]$ file /bin/ls #可以发现是64位的操作系统。
      /bin/ls: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=056dda3f1b77919163a7de5563a2b9d9d245554c, stripped
      ```

   8. 使用lsb_release命令查看发行版的版本，对于Redhat系列的，也可以查看/etc/redhat-release文件：

      ```shell
      [zj@ZJ ~]$ lsb_release  -a     #可以使用yum安装redhat-lsb-core软件包。
      LSB Version:    :core-4.1-amd64:core-4.1-noarch
      Distributor ID: CentOS
      Description:    CentOS Linux release 8.3.2011
      Release:        8.3.2011
      Codename:       n/a
      [zj@ZJ ~]$ cat /etc/redhat-release  #RedHat系列发行版的信息。
      CentOS Linux release 8.3.2011
      [zj@ZJ default]$ cat /etc/system-release #所有发行版都可以。
      CentOS Linux release 8.3.2011
      ```

   9. 使用lsof查看某个进程或用户使用的文件：

      ```shell
      [zj@ZJ ~]$ lsof -u zj    #查看用户zj打开的文件。-c根据进程名来查看,-p根据进程ID来查看。
      COMMAND   PID USER   FD      TYPE             DEVICE  SIZE/OFF       NODE NAME
      systemd  1534   zj  cwd       DIR              253,0       224        128 /
      systemd  1534   zj  rtd       DIR              253,0       224        128 /
      systemd  1534   zj  txt       REG              253,0   1609248     283115 /usr/lib/systemd/systemd
      ...
      ```

# 网络命令

1. write 给用户发消息，所有用户都可以执行。write 用户名 按回车后会进入标准输入模式，ctrl+退格键可以删除内容，Ctrl+D保存结束。       只有收信方在线才可以受到消息，也会显示那个用户在几点发送的。
2. wall 给所有在线用户发消息，write all。所有用户都可以执行。wall 消息  即可。广播信息，执行者自己也会收到。
3. ping -c 3 IP地址。可以指定ping3次就结束，否则不会停止。
4. ifconfig 网络设置命令  lo是本地回环网卡，127.0.0.1，不插网线都可以ping通。本机通信使用的。ifcongfig eth0 192.168.1.100   手动给eth0网卡，设置IP,临时生效。
5. mail 用户名 执行后进入标准输入，写发信的内容，这样用户不在线也可以收到。直接运行mail的话，则会进入用户自己的邮箱。可以逐个查看。有的程序会给root发邮件，都是很重要的信息。
6. last 统计登录过的用户登录计算机的时间，时长，还有重启命令执行的时间。
7. lastlog 统计所有用户（包括伪用户）最后一次登录的时间


# 定时任务

   1. 备份，杀毒之类的任务应该定时执行，且一般在夜间执行。

   2. 定时任务需要开启crond服务来管理。一般来说，都是默认安装并开机启动的。在CentOS7下，已经被systemd取代管理。

   3. crontab命令可以编辑查询用户的定时任务，-e编辑（会用编辑器打开一个临时文件），-l查看，-r删除当前用户的所有crontab任务。

   4. 定时任务的文件中，每一行都是一个cron表达式。由5个时间部分（分时日月星期）和一个命令(可以是shell脚本，也可以是命令)部分组成。只能精确到分钟。

         1. 第1个*表示一个小时内的第几分钟，取值范围为0-59。

         2. 第2个*表示一天内的第几个小时，取值范围为0-23。

         3. 第3个*表示一个月内的第几天，取值范围为1-31。

         4. 第4个*表示一年内的第几个月，取值范围为1-12。

         5. 第5个*表示一周内的星期几，取值范围为0-7，0和7都表示星期天。

   5. 特殊符号：

      ```shell
      *   #代表任何时间。比如第一个*就表示一小时中每分钟都执行一次。第三个*表示一个月的每天都执行。
      ,   #代表不连续的时间，比如 0 8,12,16 * * *表示每天的8点0分，12点0分，16点0分都执行一次。
      -   #连续的时间范围，比如 0 5 * * 1-6表示每个周一到周六的5点0分执行命令。
      */n #代表间隔多久执行一次，比如 */10 * * * * 表示每隔10分钟就执行一次。
      ```

   6. 例子：

      ```shell
      10 * * * * #每月每天每个小时的第10分钟都会执行一次。也就是在0:10 1:10 2:10等等时间都会执行。
      * 10 * * * #每月每天的10点钟的每一分钟都会执行1次，即10:0 10:1 10:2等，一共60次。
      0 8,10,12,14 * * * #每月每天的第8,10,12,14点整的时候执行一次。
      0 5 * * 1-6 #每周1-6的5点整都会执行一次。这个和月日不联动。
      */10 5 * * * #每天的5点每隔10分钟执行一次。即只在一天的5:0 5:10 5:20 5:30等执行，一共6次。
      0 0 1,15 * 1 #每月1和15号，和周一的0点整都会执行一次。这个和日月联动，不建议使用，容易弄混。
      ```


# 软件安装

1. 软件安装主要有一下几种方式：

      1. 源码包安装，从GitHub或官网下载程序的源代码，在本地编译然后安装，这种方式是自由度最高的，用户可以定义安装哪些模块，安装的位置等等。一般情况下，源码包中都会自带安装脚本，只需要执行该脚本，或加上少量自定义的参数即可。
      2. 安装打包好的软件，例如rpm，deb包，这些是有发行商对市面上的常用的软件进行打包(都是编译好的)，然后放到网络上，用户下载后使用对应的包管理器进行安装。现在有了下载和安装一体化的包管理器，例如yum和apt。

2. 源码包的安装：

     1. 一般下载的都是压缩文件，例如.tar.gz或.tar.bz2等，先解压

          ```shell
          tar   -zxvf   xx.tar.gz
          tar   -jxvf    xx.tar.bz2
          ```

     2. 有Readme文件的话，应该先读完该文件。
        
     3. 进入解压后的目录，运行configure脚本来生成Makefile文件。configure脚本主要探测系统环境，编译器的版本，函数库和版本，linux内核版本，头文件版本，以生成可行的Makefile文件。
        
     4. 执行make命令，编译出程序所有的库文件和可执行文件。如果缺少对应的依赖库，make会报错。
        
     5. 执行make install，将make出来的程序文件安装到系统的指定位置，并修改环境变量。这个位置是在configure步时设置好的。

3. configure脚本有大量的命令行选项，对于不同的软件包，大部分是相同的。常用的选项如下：

4. ```shell
      --prefix=DIR    #默认情况下，软件的根目录会被安装到/usr/local目录下，即可执行文件会被复制到/usr/local/bin下，库文件会被复制到/usr/local/lib目录下。可以使用这个命令来修改安装目录，这个是最常用的了。
      --includedir=DIR   #指定C头文件的安装位置。
      ```

5. 如果安装的是库，例如gsl，会在/usr/local目录下出现一个gsl目录，其下有三个子目录lib（存放.so动态库文件），bin(存放可执行文件，有的库没有)，include(存放.h头文件)。为了使得编译器能够找到对应的头文件和动态库文件，需要设置gcc命令行或设置环境变量：

      ```shell
      gcc –Lyour_path/lib –Iyour_path/include your_code –lgsl –lgslcblas#这里-l出现了2次，是因为gsl库的特殊性，它需要调用gslcblas
      #设置环境变量，这样就可以省略-I和-L，但是-l还是需要的
      export C_INCLUDE_PATH=$C_INCLUDE_PATH:your_path/include
      export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:your_path/include #C++的头文件搜索路径
      export LIBRARY_PATH=$LIBRARY_PATH:your_path/lib
      ```

6. 运行可执行程序时，还需要保证链接时使用到的动态库可以被链接器找到：

      ```shell
      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:your_path/lib #shell脚本
      your_path/lib #或者在/etc/ld.so.conf或/etc/ld.so.conf.d下的某个.conf配置文件中添加目录即可，要单独占用一行。然后运行ldconfig命令，让系统重新读取该配置文件。
      ```

7. linux下的软件主要分为两类：脚本（shell脚本，perl脚本，Python脚本）和二进制文件（大部分的程序）。实际上有些脚本是对二进制程序的一个封装，便于使用。

8. linux下安装软件主要有以下几部分组成：可执行文件，编译用的头文件，运行时的共享库，配置文件，man手册，帮助文档等。

9. 不论是直接安装软件包还是运行编译安装脚本，都是将上述对应的文件放到正确的位置。这样程序才能运行起来。使用配置文件来进行配置的好处是，如果想要重装软件（软件升级或部分文件损坏等）或者在其他系统中安装，只需要备份配置文件，然后重新安装软件后，再恢复原来的配置文件即可。

10. 如果程序运行出了故障，提示缺少某些文件，也可以从网上下载或从另一台完好的计算机上拷贝过来对应的文件即可。这是和Windows很不一样的地方，Windows的大型软件都要和系统的注册表打交道，没有做到解耦合。注册表是一个集中的配置数据库，windows系统和应用程序的配置都在其中，确实提高了配置效率和安全性，但是稳定性或易用性降低了，备份也不方便。

11. RPM，RedHat Package Manager是由二进制可执行文件+安装规则构成，安装规则说明了依赖关系，可执行文件使用的编译选项，版本，说明等，目的是降低安装难度。

12. yum仓库是将大量的经过检验的rpm包放在本地或互联网上，用yum工具统一管理。

13. rpm包：bind-9.8.2-0.47.rc1.el6.x86_64.rpm：

             1. 软件名bind
             2. 9.8.2是主版本，次版本，修正版本号。47是发布版本号，表示这个rpm包是第47次编译生成的。rc1表示release candidate，也就是候选发布的版本，一般要经过几个rc版本之后，才会定型为正式的版本。
             3. el6表示适用于发行版rhel6版本的。
             4. x86_64或i686或noarch表示当前软件的适用的硬件平台，一定不能安装错了。
             5. 有些包还有对应的开发版本，如bind-devel   开发版本一般会带.h头文件。

14. yum将常用到的一些包进行组合，形成了一些group，安装一个group就相当于安装了一堆rpm包。

          ```shell
          [zj@z] ~]$ yum grouplist
          已加载插件: fastestmirror
          没有安装组信息文件
          Maybe run: yum groups mark convert (see man yum)
          loading mirror speeds from cached hostfile
           * base: mirror.zu.edu.cn
           * extras: mirror.lzu.edu.cn
           * updates: mirrors.bfsu.edu.cn
          可用的环境分组:
            最小安装
            基础设施服务器
            计算节点
            文件及打印服务器
            基本网页服务器
            虚拟化主机
            带 GUI 的服务器
            GNOME桌面
            KDE Plasma Workspaces
            开发及生成工作站
          可用组:
            传统 UNIX 兼容性
            兼容性程序库
            图形管理工具
            安全性工具
            开发工具
            控制台互联网工具
            智能卡支持
            科学记数法支持
            系统管理
            系统管理工具
          完成
          ```

15. 可以使用yum的downloadonly 插件来只下载，不安装对应的rpm包，依赖的包也会下载。

16. 使用yum或dnf下载rpm包，解压rpm包。

             ```shell
              sudo yum download --downloadonly  tmux    #默认下载到当前路径下
              rpm -qpl *.rpm      #查看rpm包内的文件 
              rpm2cpio *.rpm | cpio -div     #将rpm格式转化为cpio格式，然后输出到当前目录下。
             ```

17. https://pkgs.org/这个网站可以查询各个发行版的软件包。



# 日志管理

1. 系统出现问题应该先看日志，日志中存在程序的输出，报错信息等。
2. centos6之后rsyslogd已经取代了syslogd服务，更先进。
3. 一般通过判断进程是否存在来判断服务是否启动，例如 ps aux | grep 服务的进程名
4. chkconfig

# 备份与恢复

1. 得益于UNIX的一切皆文件的设计，备份文件就可以备份整个系统。重要数据需要异地备份。

2. 常见的需要备份的目录：

   ```shell
   /root root用户的家目录
   /home 普通用户的家目录
   /etc 重要的配置文件保存目录
   /var/spool/mail 邮件目录
   /var/log 日志目录
   特定软件的特定目录，例如网页服务器的网页主目录，数据库的数据库文件。
   ```

3. /bin目录没必要备份，重新安装软件就可以啦。

4. 重要的服务器一般都有从服务器做容灾设计，二者之间会定时发送心跳包，一旦主服务器宕机，从服务器会立刻替代。

5. 增量备份：后续每天都是当天和前一天备份之间的差异。一般备份的数据都会压缩。恢复起来要从头开始。

6. ![image-20210416182703527](Linux学习.assets/image-20210416182703527.png)

7. 差异备份：后续每天都是当前和第一次备份之间的差异。数据量介于增量备份和完全备份之间。

8. ![image-20210416182845555](Linux学习.assets/image-20210416182845555.png)

9. 完全备份的话，可以自己写脚本用tar打包压缩对应的目录。手动实现增量备份比较麻烦。dmup和restore是系统提供的增量备份的工具，在dump包中。

   ```shell
   dump [选项] 备份之后的文件名 源文件或目录
   -level  #0-9的十个备份级别
   -f 文件名 #指定备份后的文件名
   -u #备份成功之后，把备份时间记录在/etc/dumpdates文件中
   -v #显示备份过程中更多的输出信息
   -j #调用bzlib库压缩备份文件，格式为.bz2
   -W #显示允许被dump的分区的备份等级及备份时间
   ```

10. 备份分区：

    ```shell
    dump -0uj -f dump_boot.bak.bz2 /boot   #将/boot所在的分区压缩备份到当前目录下，名字为dump_boot.bak.bz2 并写入备份文件。
    dump -1uj -f dump_boot.bak1.bz2 /boot#执行增量备份
    ```

11. 查看备份记录文件/etc/dumpdates。

    ```shell
    cat /etc/dumpdates
    /dev/sda1 0 Wed May 14 01:27:14 2014 +0800
    /dev/sda1 1 Wed May 14 01:29:33 2014 +0800
    ```

12. 查看可以被dump的各个分区的备份等级及备份时间，可以看出sda2和sda5从没有备份过。sda1备份过2次，

    ```shell
    dump -W
    Last dump(s) done (Dump '>' file systems):
    > /dev/sda5 (     /) Last dump:never
      /dev/sda1 ( /boot) Last dump:Level 1, Date Wed May 14 01:29:33 2014
    > /dev/sda2 ( /home) Last dump:never
    ```

13. dump命令只有备份分区的时候才可以进行增量备份。对于普通目录只能完全备份：

    ```shell
    dump -oj -f  dump_etc.bak.bz2 /etc #完全备份/etc目录,一般来说etc目录的文件也是不大的。
    ```

14. restore 恢复备份的数据：

    ```shell
    restore [模式选项] [选项]
    模式选项：restore命令常用的模式有一下4种，不能混用
    -C #比较备份数据和实际数据的变化
    -i #进入交互模式，手工选择需要恢复的文件
    -t #查看模式，用于查看备份文件种拥有哪些数据
    -r #还原模式，用于数据还原。
    选项
    -f 指定备份文件的文件名
    ```

15. 还原的时候要从最开始备份的开始还原，默认会解压到当前目录下。

    ```shell
    restore -r -f dump_boot.bak.bz2   #不需要指定还原到的目录或分区，会自动记录的
    restore -r -f dump_boot.bak1.bz2
    ```

20. dump和restore命令只能对ext2/3/4文件系统进行备份。对于xfs文件系统，需要使用xfsdump和xfsrestore来备份和恢复。这个命令没有压缩选项可以使用其他的软件进行压缩。

21. ```shell
    xfsdump -f dump_boot.bak.gz /dev/sda1 -l0 -L First_dump_sda1 -M sda1     #-l0表示是备份的级别,-L指定本次备份的说明,-M指定本次备份的媒介说明。如果不指定这两个选项会进入交互式的场景。这两个选项类似于Git提交的时候要写入的信息一样。 分区可以写挂载点，也可以写设备文件名。
    [root@ZJ ~] xfsdump -I   #查看备份的信息。记录在/var/lib/xfsdump/inventory目录下。
    ...
                    mount point:    ZJ.HIT:/boot
                    device:         ZJ.HIT:/dev/nvme0n1p1
                    time:           Fri Apr 16 20:01:17 2021
                    session label:  "dump_bodump_boot"
    ...
                    stream 0:
                            pathname:       /home/zj/dump_boot.bak
                            start:          ino 133 offset 0
                            end:            ino 3145861 offset 0
    ...
                                    mfile end:      ino 3145861 offset 0
                                    media label:    "sda1"
                                    media id:       fd6f4df7-77f7-4e77-80f6-9570a8c6a5b5
    xfsdump: Dump Status: SUCCESS
    ```

22. 如果想不对整个分区进行备份，而是只对分区内的某个文件或目录进行备份，方法如下：

    ```shell
    xfsdump -f dump_boot.bak.gz -s grub2/grub.cfg /boot -l0 -L First_dump_sda1 -M sda1 #备份boot分区内的grub2/grub.cfg文件。此时的路径从分区的根开始写，而不是/。
    ```

23. 使用-l来实现增量备份：

    ```shell
    [root@ZJ ~] xfsdump -l1 -f dump_boot.bak2 /boot -L disancibeifen -M boot    #不用指定level0的备份文件，会自动识别。
    xfsdump: using file dump (drive_simple) strategy
    xfsdump: version 3.1.8 (dump format 3.0) - type ^C for status and control
    xfsdump: level 1 incremental dump of ZJ.HIT:/boot based on level 0 dump begun Fri Apr 16 22:27:42 2021
    ```

24. 使用挂载点来备份分区时，不能再目录的最后加/，例如：

    ```shell
    [root@ZJ ~] xfsdump -f dump_boot.bak1 /boot/ -L diercibeifen -M boot   #使用/boot就没事了。
    xfsdump: using file dump (drive_simple) strategy
    xfsdump: version 3.1.8 (dump format 3.0) - type ^C for status and control
    xfsdump: ERROR: /boot/ does not identify a file system
    ```

25. 使用xfsrestore将备份文件恢复到指定目录：

    ```shell
    xfsrestore -f dump_boot.bak /boot #
    xfsrestore -f dump_boot.bak1 /boot #按照备份的顺序恢复。
    ```

# PACMAN包管理器

1. pacman 是一个在线包管理器，类似apt和yum。

2. 三大类指令:

   ```shell
   -S 同步，即安装软件
   -R 删除软件
   -Q 查询软件
   ```

3. 选项一般由一个大写字母+多个小写字母组合而成。

4. 安装软件：

5. ```shell
   1. sudo pacman -S vlc     #安装vlc软件 如果没有安装过，会提示下载大小和安装大小。如果已经安装了，则会提示是否重新安装。
   2. sudo pacman -Sy        #从软件源中获取最新的情报，如果最近执行过，则会直接提示已经已经是最新，不会同步。
   3. sudo pacman -Syy       #强制从软件源中同步。
   4. sudo pacman -Syyu     #强制同步并更新软件，如果没有参数，则表示更新所有的软件。       这是使用频率最高的一条指令。
   ```

6. 查询软件：

7. ```shell
   sudo pacman -Ss vim      #搜索名字和介绍中包含vim的软件     也支持正则表达式，例如     sudo pacman -Ss ^vim   搜索以vim开头的软件。
   sudo pacman -Sc          #pacman会保留安装过的软件的安装包，不会自动删除。 该指令可以删除缓存。
   ```

8. 删除软件：

   ```shell
   sudo pacman -R vim       #删除vim软件，但是这只会删除软件本身，但是安装软件时安装的依赖则不会被删除。
   sudo pacman -Rs vim      #删除vim和安装时的依赖。
   sudo pacman -Rns vim     #删除vim和安装时的依赖。同时删除全局配置文件。
   ```

9. 查询本地以安装的软件：

   ```shell
   pacman -Q                #列出以安装的所有软件
   pacman -Q | wc -l 	     #统计一共安装了多少软件，也可以在neofetch中看到。      1231个
   pacman -Qe               #用户自己安装的软件，不包含系统自带的。                303个
   pacman -Qeq              #不显示版本号，可以处理一下，保存下来，用于以后新装电脑时使用。
   pacman -Qs  vim          #查找本地和vim有关的软件
   pacman -Qdt              #查找孤包
   pacman -Qdtq              #查找孤包，不显示版本号。
   sudo pacman -R $(pacman -Qdtq)    #删除孤包
   ```

10. 孤包：作为依赖被安装，但是原软件被卸载了，不再被依赖，但是还安装在系统中。

11. 全局配置文件为     /etc/pacman.conf

12. 添加archlinuxcn源=。可以只添加清华的镜像，还要安装archlinuxcn-keyring包才可以使用：

    ```shell
    [archlinuxcn]
    SigLevel = Optional TrustAll
    Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
    ```

13. 也可以添加一个镜像列表，例如：

    ```shell
    [archlinuxcn]
    SigLevel = Optional TrustAll
    Include = /etc/pacman.d/archlinuxcn-mirrorlist
    ```

14. 其中/etc/pacman.d/archlinuxcn-mirrorlist的内容为：

15. ```shell
    ## Arch Linux CN community repository mirrorlist
    ## Generated on 2019-12-03
    
    ## 清华大学 (ipv4, ipv6, http, https)
    Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
    
    ## 网易 (ipv4, http, https)
    Server = https://mirrors.163.com/archlinux-cn/$arch
    
    ## Our main server (ipv4, ipv6, http, https)
    #Server = https://repo.archlinuxcn.org/$arch
    
    ## 中国科学技术大学 (ipv4, ipv6, http, https)
    Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
    
    ## 上海科技大学 (上海) (ipv4, http, https)
    #Server = https://mirrors-wan.geekpie.club/archlinuxcn/$arch
    
    
    ## 腾讯云 (ipv4, https)
    Server = https://mirrors.cloud.tencent.com/archlinuxcn/$arch
    
    ## 重庆大学 (ipv4, http, https)
    Server = https://mirrors.cqu.edu.cn/archlinuxcn/$arch
    
    ## SJTUG 软件源镜像服务 (ipv4, https)
    #Server = https://mirrors.sjtug.sjtu.edu.cn/archlinux-cn/$arch
    
    ## 莞工 GNU/Linux 协会 开源软件镜像站 (ipv4, http, https)
    #Server = https://mirrors.dgut.edu.cn/archlinuxcn/$arch
    
    ## 浙江大学 (浙江杭州) (ipv4, ipv6, http, https)
    Server = https://mirrors.zju.edu.cn/archlinuxcn/$arch
    
    ## xTom (Hong Kong server) (Hong Kong) (ipv4, ipv6, http, https)
    #Server = https://mirror.xtom.com.hk/archlinuxcn/$arch
    
    ## xTom (US server) (US) (ipv4, ipv6, http, https)
    #Server = https://mirror.xtom.com/archlinuxcn/$arch
    
    ## xTom (Netherlands server) (Netherlands) (ipv4, ipv6, http, https)
    #Server = https://mirror.xtom.nl/archlinuxcn/$arch
    
    ## Open Computing Facility, UC Berkeley (Berkeley, CA, United States) (ipv4, ipv6, http, https)
    #Server = https://mirrors.ocf.berkeley.edu/archlinuxcn/$arch
    ```

# APT包管理器

1. apt 是 Debian 系操作系统的包管理工具。同类的还有apt-get和apt-cache。

2. 早期的配置文件为/etc/apt/apt.conf，现在多存放在/etc/apt/apt.conf.d目录下。

3. 命令格式：

   ```shell
   apt [options] command
   #常用的选项：
   list - 可以显示满足特定条件的软件包，默认显示所有可安装的软件。 --installed 列出已安装 --upgrade 列出可升级的。
   search - 在所有可安装软件的描述中搜索。
   show - 查看特定软件包的详细信息。
   install - 安装特定软件包。
   reinstall - 重新安装软件包。
   remove - 删除软件包，但是保留配置文件。
   purge - 删除软件包和配置文件。
   autoremove - 删除自动安装的，已经不再被依赖的软件。一般是依赖关系更改或者需要他们包已经被删除。
   update - 从配置的源更新软件包信息。总是应该在安装或升级软件之前执行该操作。
   upgrade - 更新软件，但是不会删除旧版。
   full-upgrade - 更新软件包，会删除旧版。
   edit-sources - 用默认编辑器打开软件源文件。
   satisfy - satisfy dependency strings
   ```

4. 作为依赖被安装的软件包，会显示[automatic]。

5. 软件源：/etc/apt/sources.list文件和/etc/apt/sources.list.d目录下的文件。

6. 可以在`/var/log/dpkg.log`文件中查看apt日志。


# snap，AppImage，Flatpak

1. 这些软件封装格式是将软件本体和其所有的依赖共同打包的，可以较好地使用linux各个发行版之间的区别。不同的发行版配置的共享库的数量和版本是不同的。同时他们都自带沙箱，与宿主操作系统隔离，程序运行在容器中，允许安装同一个软件的多个版本。
2. snap是Ubuntu的母公司Canonical开发的，也被移植到了其他的linux发行版上。安装软件的方式和apt类似，可以从官方的仓库安装，也可以自己下载对应的包来安装。 

# SSH

1. SSH（Secure Shell）是一种网络协议，广泛用于服务器登录和各种加密通信。任何网络服务都可以用这个协议来加密。

2. 官方的SSH2是收费的，OpenBSD的开发者根据SSH1的最后一个开源版本（1.2.12）开发的。Linux的发行版都自带OpenSSH，目前最新版本为8.2。通常说的ssh也是指的OpenSSH的实现。

3. SSH的架构是C-S模式，客户端程序为ssh，服务器端程序为sshd。约定SSH表示协议，ssh表示客户端程序。

4. OpenSSH还提供了一些辅助工具：ssh-keygen，ssh-agent，和专门的客户端工具：scp，sftp。

5. ```shell
   sudo apt install openssh-client    #安装ssh客户端。
   sudo apt install openssh-server    #安装ssh服务端。
   sudo apt install ssh               #安装ssh的客户端和服务端，默认是OpenSSH。
   ```

6. ssh登录：

   ```shell
   ssh hostname         #hostname可以是域名，IP地址，也可以是局域网内其他的主机名。不指定用户名的情况下，会使用当前系统登录的用户名。
   ssh user@hostname    #指定用户名。
   ssh -l user hostname #用户名也可以用-l参数来指定
   ssh -p 8822 hostname #ssh默认使用22端口,-p参数可以指定使用其他端口。
   ```

7. ssh每连接一个新的服务器时，都会先获取这个服务器的公钥，然后计算hash值，这个称为服务器的指纹，用来识别服务器。ssh会将本机连接过的所有服务器公钥的指纹存储在~/.ssh/known_hosts中。之所以保存在用户目录中，是因为ssh客户端的使用情况是因用户而异的。而ssh服务端的公钥和私钥都保存在系统的目录/etc/ssh中，且公钥对于任意用户都是可读的，而私钥只对于root有读写权限。

   ```shell
   ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key.pub #输出本机用椭圆曲线数字签名算法生成的公钥的指纹。
   256 SHA256:GpjlTm6trSzBvXGPkV27nciEfVLQceFWoIcVfaycX9k root@zj-hit (ECDSA)
   
   zj@zj-hit:~$ ll /etc/ssh
   total 568K
   -rw-r--r-- 1 root root 523K Jul 23  2021 moduli
   -rw-r--r-- 1 root root 1.6K Jul 23  2021 ssh_config               #客户端配置文件
   drwxr-xr-x 2 root root 4.0K Jul 23  2021 ssh_config.d             #客户端配置目录
   -rw-r--r-- 1 root root 3.3K Jul 23  2021 sshd_config              #服务端配置文件
   drwxr-xr-x 2 root root 4.0K Jul 23  2021 sshd_config.d            #服务端配置文件
   -rw------- 1 root root  505 Dec 18 02:53 ssh_host_ecdsa_key       #使用椭圆曲线签名算法生成的私钥
   -rw-r--r-- 1 root root  173 Dec 18 02:53 ssh_host_ecdsa_key.pub   #使用椭圆曲线签名算法生成的公钥
   -rw------- 1 root root  399 Dec 18 02:53 ssh_host_ed25519_key     #使用ed25519算法生成的私钥
   -rw-r--r-- 1 root root   93 Dec 18 02:53 ssh_host_ed25519_key.pub #使用ed25519算法生成的公钥
   -rw------- 1 root root 2.6K Dec 18 02:53 ssh_host_rsa_key         #使用rsa算法生成的私钥
   -rw-r--r-- 1 root root  565 Dec 18 02:53 ssh_host_rsa_key.pub     #使用ras算法生成的公钥
   -rw-r--r-- 1 root root  342 Dec 18 02:53 ssh_import_id
   ```

8. ssh命令的配置在三个地方，优先级依次为：命令行选项>用户配置文件>系统配置文件，用户配置文件为`~/.ssh/ssh_config`，系统配置文件为`/etc/ssh/ssh_config`，同时`/etc/ssh/ssh_config.d`目录下的.conf后缀的文件也会被当成配置文件读取。

9. 当远程主机提供的公钥指纹和本机之前存储的公钥指纹不一致时，ssh会报警，拒绝连接，此时可能是远程主机重装了系统，重新生成了密钥，或者发生了中间人攻击（有人冒充远程主机）。

   ```shell
   ssh-keygen -R hostname   #将本机保存的hostname对应的公钥指纹删除，此时再重新连接即可。
   ```

10. 登陆之后就显示的是远程主机的命令行提示符，不过也可以利用ssh来单独执行一条命令然后自动退出：

    ```shell
    ssh user@hostname cat /etc/ssh/ssh_config   #登录后立即执行  cat /etc/ssh/ssh_config  不过这样对于需要交互式shell的程序会报错，例如vim。此时需要使用-t 选项。
    ```

11. SSh握手阶段，客户端向服务器发送多个自己所支持的加密参数集，服务器从中选择一个自己支持的来和客户端通信。每个加密参数集由若干个加密参数构成，

    ```shell
    Cipher Suites   #下面是客户端发给服务器的自己支持的加密参数集，一共8个。
        Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256”
        Suite: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
        Suite: TLS_RSA_WITH_AES_128_GCM_SHA256
        Suite: TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
        Suite: TLS_DHE_RSA_WITH_AES_128_CBC_SHA
        Suite: TLS_RSA_WITH_AES_128_CBC_SHA
        Suite: TLS_RSA_WITH_3DES_EDE_CBC_SHA
        Suite: TLS_RSA_WITH_RC4_128_SHA
    #加密参数的含义：
    TLS:加密通信协议
    RSA:密钥交换算法
    AES:加密算法
    128:加密算法的强度
    CBC:加密算法的模式
    SHA:数字签名的Hash函数
    ```

12. 命令行选项：

    ```shell
    -c blowfish  #指定加密算法为blowfish,多个加密算法可以用逗号分隔
    -C           #将数据压缩传输
    -D 1080      #指定本机的socks监听端口为1080,当该端口收到请求时，都将转发给远程主机
    -F /usr/local/ssh/ssh_config  #使用指定的配置文件
    -i xxx       #使用指定的私钥,默认使用~/.ssh/xxx_dsa (dsa算法)或~/.ssh/xxx_rsa (rsa算法)。
    -L 9999
    -p 2035      #指定服务器端口为2035。
    -4           #使用ipv4协议，这是默认的，还可以指定-6表示只是用ipv6链接。
    ```

13. `~/.ssh`目录除了含有客户端的用户配置文件，还有用户个人的密钥。

14. 配置文件的格式：

    ```shell
    host *           #对所有目标主机都生效
    	port 2222   #键值对的形式,也可以用=连接。#开头的行表示注释。
    host .edu        #以下配置对所有定义域名为edu的地址都生效
    host server1  #下面的配置仅对 ssh server1 命令生效,优先级高于上面的*
    	hostname xxx.com   #指定ssh server1时要链接的目标主机
    	user neo
    	port 3322
    #有了上面的配置  ssh server1  相当于  ssh -p 3322 neo@xxx.com
    ```

15. SSH默认采用密码登录，但是密钥登录更为安全，密钥是一个非常大的数字，SSH登录采用的是非对称加密，私钥必须私密保存，每一个私钥都有且只有一个公钥。使用私钥加密一般称为签名。

16. SSH密钥登录的过程：

    1. 客户端先将自己的公钥放入到要登录的服务端的指定位置中。
    2. 客户端向服务端发送登录请求。
    3. 服务端收到请求，发送一些随机数据给客户端，让客户端用自己的私钥签名。这一步是为了让客户端证明自己的身份。
    4. 客户端收到服务端发来的随机数据，用自己的私钥签名，再发给服务端。
    5. 服务端将收到的签名数据用客户端声称的公钥解密，如果还原了一开始的随机数据，那么认为客户端完成了身份验证，允许登录，反之不允许。

17. ssh-keygen工具可以用来生成密钥：

    ```shell
    zj@zj-hit:~$ ssh-keygen  #默认使用rsa加密算法，也可以用-t dsa来指定使用dsa算法。
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/zj/.ssh/id_rsa): #指定私钥的存放位置和文件名。公钥会存放在相同的目录，文件名会多个.pub。
    Enter passphrase (empty for no passphrase):  #这里是询问是否要为私钥文件设置密码保护，这样可以在私钥文件被非法获取后，避免被破解。
    Enter same passphrase again:
    Your identification has been saved in /home/zj/.ssh/id_rsa  #私钥
    Your public key has been saved in /home/zj/.ssh/id_rsa.pub  #公钥
    The key fingerprint is:
    SHA256:pvP9K3TBOoBOgss/SnqE9PRc+Lv6WPUBVnJb2JY22zs zj@zj-hit  #公钥的指纹
    The key's randomart image is:
    +---[RSA 3072]----+
    |         . oo..  |
    |          +.o*   |
    |   .  .. o oo +  |
    | .....o.o . o. . |
    |.oo.o+o So o .  .|
    |. +. o.+. = o  E |
    | ...  o... +    .|
    | o. o o+ ..      |
    |.... +ooo .oo.   |
    +----[SHA256]-----+
    ```

18. 公钥和私钥都是文本文件，二者的权限如下：

    ```shell
    -rw------- 1 zj zj 2.6K Mar 10 12:40 id_rsa  #公钥和私钥的所有者都是密钥的创建者。这能够被root轻易查看。
    -rw-r--r-- 1 zj zj  563 Mar 10 12:40 id_rsa.pub
    ```

19. 公钥内容如下，实际上是一行。末尾的zj@zj-hit是公钥的注释，用来识别不同的公钥，表明这个公钥是哪台计算机的哪个用户的，可有可无。

    ```
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDmEnDh9R/9cXhLXYkeHzzXv2h4ibGmbRIA5H4QQDwis6l4K/30qgVNqj1N0Ek9ZHLdhfMS89YYQOmD2knhgaeIPyqsG6Sg6RCIirYLwgPFpEnRfqJ2gxMOhWp7COXs8yFcza2+nwkAu0T2M0bi1WmBpjjH1iHkl9RbrtdzPdhV4TeJn3FZSfaEpsrXTXiLXNYt0oia1D6RJ2twkCmDerwAXddAN/nFCJWBuR+XGHRDtpw19kxFnQKKwZBjNGrcYCXxielhMa3i146UQu7gcooM9g3Sh6eD7Pfw/MIDiW6iUDstWbDB/F6LVuSs1rgwOX0BAHqDNLmXocDHqZRSyXgDXkdhxpNDdVDbX+79V38i7fY56kuTYZMsfy1exfhw/0LlD7U3eEQZknXyigO7+wkgBsKWugGfLm3kh9W8O0EakfhyC9TzSNdhHaYCmuP3RYBppEfl1YI4qLQ1c9C75HJhbV8hFFWQ4gXCGIGsAhrGZYQSCWjfhvEQ2+SjnVzeYxs= zj@zj-hit
    ```

20. ssh-keygen选项：

    ```shell
    -b 2048    #设置密钥的位数为2048位,最少也要有1024,位数越高越不容易被破解，但是加密和解密的开销也越大。
    -f xxx     #指定私钥文件的目录和文件名,默认是在当前目录下。
    -N 123     #指定私钥文件的密码为123。
    -F xx.com  #检查xx.com是否在know_hosts文件中。
    -R xx.com  #将xx.com移出known_hosts。
    -t dsa     #设置密钥算法为dsa,默认为rsa。
    ```

21. OpenSSH规定，用户公钥保存在服务端的\~/.ssh/authorized_keys。这里的~指的是要登录的那个用户名在服务端的家目录。每个公钥占据该文件的一行，粘贴进去即可。这一步可以通过U盘拷贝进去也可以通过密码登录进去，命令如下：

    ```shell
    cat ~/.ssh/id_rsa.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"   
    #管道符连接内容，>>追加到文件的末尾。user@host为服务端的用户名和主机名。
    ```

22. authorized_keys文件的权限要设置为644，只有所有者可以写，其他人只能读，如果权限不正确，SSH服务器可能会拒绝登录。

23. 不用客户端使用相同的用户名登录后，服务器无法分辨他们谁是谁，一般来说一个用户名应该只给予一个人。

# 代理

1. 可以通过设置环境变量来设置终端代理：

   ```shell
   export http_proxy=192.168.80.1:10809     #协议默认为http://,可以省略。
   export https_proxy=192.168.80.1:10809    #设置HTTPS代理。
   export all_proxy=192.168.80.1:10809      #可以代替以上两行。
   #也可以使用socks5的代理,不过要写明协议和对应的端口,例如：
   export all_proxy=socks5://192.168.80.1:10808
   #有些软件不支持all_proxy的设置，有些也不支持socks5协议代理。最稳靠的方法还是最上面的两行。
   ```

2. v2ray显示：

   ```
   SOCKS5 127.0.0.1:10808  HTTP 127.0.0.1:10809  PAC http://127.0.0.1:10810/pac/?t=133741
   ```

3. 可以通过curl google.com来检测是否配置成功代理。ping google.com是无效的，因为ping命令使用的是ICMP协议，而http代理只能代理http协议，在应用层；socks5代理只能代理tcp或udp协议。

4. 以上设置的代理可能会对apt命令无效，可以单独为其设置代理：

   ```shell
   #新建一个文件/etc/apt/apt.conf.d/95proxy.conf 文件名不重要，之所以这么起是为了表明功能
   Acquire::http::Proxy "http://192.168.80.1:10811";
   Acquire::https::Proxy "http://192.168.80.1:10811";
   ```


# tmux

   1. terminal multiplexer  终端复用器，它的作用是在纯命令行的界面，模拟出图形界面下terminal的多窗口的功能。

   2. 命令行的通常用法是，打开一个terminal终端窗口，和计算机进行交互，这就成为一个session会话。窗口和其中的进程是关联，关闭窗口，会导致会话关闭，会话内的进程也会被关闭。例如，通过ssh登录到远程服务器时，执行了一个耗时的命令，这时如果断开ssh连接，是找不到上次执行的命令的，因为窗口关闭，上次的会话已经被释放了。

   3. 为了解决上述问题，将会话和窗口解绑是比较可行的做法。即窗口关闭前，将会话和窗口解绑，这样会话不会终止，再次需要时，可以再让窗口绑定会话，进行操作。

   4. 类似的终端复用器来由GNU Screen。

   5. ```shell
      sudo yum install tmux        安装tmux
      ```

   6. 输入tmux，进行tmux环境，窗口底部会显示当前会话编号和名称，默认是从0开始。可以创建多个会话，分别执行不同的任务。

   7. Tmux 窗口有大量的快捷键。所有快捷键都要通过前缀键唤起。默认的前缀键是`Ctrl+b`，即先按下`Ctrl+b`，快捷键才会生效。

   8. ```shell
      tmux new -s <session-name>       创建一个新的会话，指定名称。
      ```

   9. Ctrl+b d或者输入tmux detach，使得窗口和当前会话分离开。上面命令执行后，就会退出当前 Tmux 窗口，但是会话和里面的进程仍然在后台运行。

   10. `tmux ls` 或`tmux list-session`命令可以查看当前所有的 Tmux 会话。

   11. ```shell
       # 将窗口和会话重新绑定
       $ tmux attach -t 0        使用会话编号
       $ tmux attach -t <session-name>           使用会话名称
       ```

   12. ```shell
       # 杀死会话
       $ tmux kill-session -t 0                    使用会话编号
       $ tmux kill-session -t <session-name>       使用会话名称
       ```

   13. ```shell
       # 切换会话
       $ tmux switch -t 0                         使用会话编号
       $ tmux switch -t <session-name>            用会话名称
       # 重命名会话
       tmux rename-session -t 0 <new-name>
       ```

   14. 使用tmux的一般流程如下：

       1. 新建会话`tmux new -s my_session`。
       2. 在 Tmux 窗口运行所需的程序。
       3. 按下快捷键`Ctrl+b d`将会话分离。
       4. 下次使用时，重新连接到会话`tmux attach-session -t my_session`。

   15. tmux也具有一些窗格管理，允许将一个窗口分隔成多个部分，分别绑定不同的会话。类似于vim。

   16. ```bash
       # 划分上下两个窗格
       $ tmux split-window
       
       # 划分左右两个窗格
       $ tmux split-window -h
       ```

   17. 除了可以在一个窗口内划分窗格，还支持创建多个窗口

   18. Ctrl+B ? 可以查看tmux的帮助，里边包含了所有的快捷键

   19. tmux默认不支持鼠标操作。支持vim和EMACS两种操作模式。

   20. tmux支持远程协作，两个人同时连接到服务器中的一个session，可以同时编辑一个文件。

# 字体相关

1. fc-list查看本机已经安装的字体，可能需要安装 yum install -y fontconfig mkfontscale：

   ```shell
   [zj@ZJ fonts]$ fc-list
   /usr/share/fonts/dejavu/DejaVuSerif-Bold.ttf: DejaVu Serif:style=Bold #三部分，路径名，字体名，样式
   /usr/share/fonts/paratype-pt-sans/PTS76F.ttf: PT Sans:style=Bold Italic
   ...
   [zj@ZJ fonts]$ fc-list :lang=zh    #查看中文字体
   /usr/share/fonts/google-noto-cjk/NotoSansCJK-DemiLight.ttc: Noto Sans CJK TC,Noto Sans CJK TC DemiLight:style=DemiLight,Regular
   ...
   ```

2. 安装字体的步骤：

   1. 拷贝ttf文件到/usr/share/fonts目录。可以为字体族新建一个文件夹。
   2. cd到该目录，依次以root身份运行 mkfontscale，mkfontdir，fc-cache这三个命令，建议字体索引即可。


# Locale

1. 使用man查询文档和ls，date是显示的日期都会使用到locale的相关设置。

   ```shell
   zj@ubuntu:~$ locale -a  #查询Linux支持的所有语系,一种语言可以使用多种编码，大部分的语言都支持utf-8编码。
   C
   C.utf8
   en_US.utf8
   POSIX
   zj@ubuntu:~$ locale   #当前的配置。值的设定为 语言_国家.编码
   LANG=en_US.UTF-8
   LANGUAGE=
   LC_CTYPE="en_US.UTF-8"       #文字符号
   LC_NUMERIC="en_US.UTF-8"     #数字
   LC_TIME="en_US.UTF-8"        #时间日期显示格式
   LC_COLLATE="en_US.UTF-8"     #比较和排序习惯
   LC_MONETARY="en_US.UTF-8"    #货币单位
   LC_MESSAGES="en_US.UTF-8"    #提示信息，错误信息，标题，按钮菜单等
   LC_PAPER="en_US.UTF-8"       #默认纸张尺寸
   LC_NAME="en_US.UTF-8"        #姓名书写方式
   LC_ADDRESS="en_US.UTF-8"     #地址书写方式
   LC_TELEPHONE="en_US.UTF-8"   #电话号码书写方式
   LC_MEASUREMENT="en_US.UTF-8" #度量衡
   LC_IDENTIFICATION="en_US.UTF-8" #对locale自身包含信息的概述
   LC_ALL=
   ```

2. 可以逐个设置这些变量，如果其他语系变量都没设置，只有LANG或LC_ALL设置了，那么其他语系变量就会被这两个变量所替换。一般来说仅设置LANG或LC_ALL就够了。只有将LC_ALL设置为空(LC_ALL=)，才可以修改其他的LC_变量。

3. 优先级为：LANGUAGE > LC_ALL > LC_* > LANG。一般的系统中前两个都是不设置的，只设置LANG。

4. 终端(tty1-tty6)的shell上如果设置了中文，即LANG=zh_CN.utf-8，也会出现乱码。这是因为终端是无法显示中文这样的复杂的编码文字。而通过ssh远程链接的话，是可以看到中文的。

5. 每个用户都可以设置自己的语系。而系统也有默认的语系，保存在/etc/locale.conf中。

6. locale的定义存放在/usr/share/i18n/locales目录下，比如zh_CN表示中国大陆的习惯，存放在zh_CN文件内：

   ```shell
   #以下为其中一个部分,记录了文字的信息
   LC_CTYPE
   % This is a copy of the "i18n" LC_CTYPE with the following modifications:
   % - Additional classes: hanzi
   
   copy "i18n"
   
   translit_start
   include  "translit_combining";""
   translit_end
   
   class   "hanzi"; /       #汉字，使用Unicode编码来记录字符范围
   %       <U3400>..<U4DBF>;/
           <U4E00>..<U9FA5>;/
           <UF92C>;<UF979>;<UF995>;<UF9E7>;<UF9F1>;<UFA0C>;<UFA0D>;<UFA0E>;/
           <UFA0F>;<UFA11>;<UFA13>;<UFA14>;<UFA18>;<UFA1F>;<UFA20>;<UFA21>;/
           <UFA23>;<UFA24>;<UFA27>;<UFA28>;<UFA29>
   END LC_CTYPE
   ```

7. 字符映射（也就是编码方案）都定义在/usr/share/i18n/charmaps目录下，比如GB18030为/usr/share/i18n/charmaps/GB18030.gz

8. 生成一个locale有两种方法，以下两种方法都会向/usr/lib/locale/locale-archive写入新的locale。名称为zh_CN.utf8，推荐使用第二种：

   1. 第一种是使用localedef命令，利用locale定义和字符映射编译出对应的locale。

      ```shell
      zj@ubuntu:~$ sudo localedef -f UTF-8 -i zh_CN zh_CN.utf8  #locale定义为zh_CN，字符映射为UTF-8(不能是小写)。
      zj@ubuntu:~$ locale -a
      C
      C.utf8
      en_US.utf8
      zh_CN.utf8
      POSIX
      zj@ubuntu:~$ sudo localedef --delete-from-archive zh_CN.utf8 #可以删除已有的locale
      ```

   2. 第二种是使用locale-gen自动生成locale，首先修改/etc/locale-gen，取消对应locale前面的注释，例如zh_CN.utf8，然后执行locale-gen。locale-gen会读取/etc/locale-gen，该文件中每个没有被#注释的locale都会生成一个locale。执行完毕后，也运行locale -a可以查看到：

      ```shell
      zj@ubuntu:~$ sudo locale-gen  #实际上也可以直接执行locale-gen zh_CN.utf8来生成对应的locale，而不修改/etc/locale.gen文件。不过不推荐
      Generating locales (this might take a while)...
        en_US.UTF-8... done
        zh_CN.UTF-8... done
      Generation complete.
      zj@ubuntu:~$ locale -a
      C
      C.utf8
      en_US.utf8
      POSIX
      zh_CN.utf8
      ```

9. 临时使用新的locale，修改环境变量LANG即可：

   ```shell
   zj@ubuntu:~$ date   #此时还是en_US.UTF-8
   Sat Dec  3 12:51:20 PM UTC 2022
   export LANG=zh_CN.utf8   #虽然utf-8也可以，但是还是推荐使用locale -a 中的结果，此处的export可以不加。
   zj@ubuntu:~$ date
   2022年 12月 03日 星期六 12:52:52 UTC
   ```

10. 如果要永久生效，应该修改配置文件/etc/default/locale。

11. 如果出现如下警告locale: Cannot set LC_CTYPE to default locale: No such file or directory。则表示LANG或LC_ALL被设置为了本地没有的locale。

12. 使用了新的locale之后，还需要有一些本地资源文件，来完成具体的工作，例如ls xxx时，要想出现中文的找不到文件或路径的错误提示，还需要

13. strace记录下进程使用的系统调用和接收到的信号。

    ```shell
    zj@ubuntu:~$ strace ls xxx #以下只显示一部分
    execve("/usr/bin/ls", ["ls", "xxx"], 0x7ffd1bcb1078 /* 23 vars */) = 0  #替换镜像，2个命令行参数，传递23个环境变量。
    brk(NULL)                               = 0x55ef51711000  #内存分配
    ...
    openat(AT_FDCWD, "/usr/share/locale/zh_CN.UTF-8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)  #可以看到程序会在很多相似的路径下寻找coreutils.mo这个文件。
    openat(AT_FDCWD, "/usr/share/locale/zh_CN.utf8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale/zh_CN/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)  #Ubuntu 22.04的.mo文件在此目录下，但是没有这个文件。
    openat(AT_FDCWD, "/usr/share/locale/zh.UTF-8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale/zh.utf8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale/zh/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale-langpack/zh_CN.UTF-8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale-langpack/zh_CN.utf8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale-langpack/zh_CN/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale-langpack/zh.UTF-8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale-langpack/zh.utf8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/share/locale-langpack/zh/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
    write(2, "ls: ", 4ls: )                     = 4
    write(2, "cannot access 'xxx'", 19cannot access 'xxx')     = 19
    ...
    ```

14. 可以使用apt安装对应的.mo文件：

    ```shell
    sudo apt-get install language-pack-zh-hans  #安装简体中文的语言包，.mo文件会存放在/usr/share/locale-langpack/zh_CN/LC_MESSAGES中。实际上在安装这个包的时候会自动创建zh_CN.utf8和zh_SG.utf8两个locale。SG表示新加坡。
    ```

15. .mo文件多是由.po 文件生成的语言文件。.po文件(Portable Object)是GNU gettext项目的一套应用规范。使用msgunfmt程序将.mo文件反编译成.po文件进行修改，然后再使用msgfmt程序将.po文件编译成.mo文件就可以完成类似汉化的工作。windows下可以用poEdit修改.po文件。例如：

    ```shell
    zj@ubuntu:~$ msgunfmt /usr/share/locale/zh_CN/LC_MESSAGES/apt.mo
    msgid ""
    msgstr ""
    "Project-Id-Version: apt 2.3.15\n"
    "Report-Msgid-Bugs-To: APT Development Team <deity@lists.debian.org>\n"
    "PO-Revision-Date: 2022-02-03 13:55-0500\n"
    "Last-Translator: Boyuan Yang <073plan@gmail.com>\n"
    "Language-Team: Chinese (simplified) <debian-l10n-chinese@lists.debian.org>\n"
    "Language: zh_CN\n"
    "MIME-Version: 1.0\n"
    "Content-Type: text/plain; charset=UTF-8\n"
    "Content-Transfer-Encoding: 8bit\n"
    "Plural-Forms: nplurals=1; plural=0;\n"
    "X-Generator: Poedit 3.0.1\n"
    
    msgid "  Candidate: "
    msgstr "  候选："
    
    msgid "  Installed: "
    msgstr "  已安装："
    
    msgid "  Missing: "
    msgstr "  缺失："
    ```

# Samba 服务

1. SMB协议是Windows平台的局域网文件共享协议。Samba是Unix平台上为了兼容SMB协议而逆像开发的软件。

2. 安装步骤：

   ```shell
   sudo apt-get install samba #安装samba软件包
   sudo samba                 #运行samba软件
   systemctl status smbd      #检查smbd守护进程运行状态
   sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak  #备份配置文件
   sudo smbpasswd -a zj   #添加用户zj，并设置密码
   sudo systemctl restart smbd  #重启服务，使配置文件生效
   ```

3. 在配置文件最后添加一个共享目录：

   ```shell
   [work]
   comment=samba home directory
   path=/home/zj     #共享路径
   public=yes
   browseable=yes
   writeable=yes
   read only=no
   valid users=zj    #这里的用户是samba的用户，用于文件共享权限管理，和Linux登录的用户无关。
   create mask=0777
   directory mask=0777
   #force user=nobody
   #force group=nogroup
   available=yes
   ```

4. 在Windows的我的电脑中选择映射网络驱动器。

6. work为目标服务器上的samba配置文件中的用[ ]包裹起来的标签，就是之前在配置文件中添加的那部分。默认情况下会使用本机的用户名和密码来登录。也可以勾选“使用其他凭据连接”来手动输入用户名和密码。

7. <img src="Linux学习.assets/image-20220706224823346-16571968881572.png" alt="image-20220706224823346"  />


# Paraview远程可视化

1. 使用Client/Server模式，先在Linux服务器上运行pvserver，然后在Windows上运行paraview程序，点击Connect按钮，Add server，选择Client/Server模式，填写服务器的IP和端口（默认为11111）。

   ```shell
   zj@zj-virtual-machine:~/OpenFOAM/zj-9/run/pitzDaily$ pvserver  #运行服务端程序
   Waiting for client...
   Connection URL: cs://zj-virtual-machine:11111
   Accepting connection(s): zj-virtual-machine:11111   #等待客户端连接
   Client connected. #连接成功
   Exiting...        #退出连接
   ```

2. ![image-20220707105841023](Linux学习.assets/image-20220707105841023-16571968881573.png)

3. 还有Reverse Connection 也就是反向链接，将本机当作服务端，由远程的服务器主动连接客户端。这用在某些服务器不能正常开启pvserver的情况。此时-p就不表示服务器端监听的端口，而是客户端监听的端口。

4. 这个pvserver设计有个不太好的点，就是在客户端断开连接后，服务端会自动终止。如果要避免这种情况，就需要书写一个shell脚本`start-pvserver.sh`来控制：

   ```shell
   #!/usr/bin/bash
   # start pvserver
   while true; do #repeatedly execute after disconnect
       pvserver
   done
   ```


# VMware和主机剪贴板互通

1. 安装VMware扩展：

   ```shell
   sudo apt-get install open-vm-tools-desktop # open-vm-tools-desktop是open-vm-tools的扩展，专注于提供与桌面虚拟机相关的增强功能。安装open-vm-tools-desktop将包括open-vm-tools提供的所有功能。
   ```

2. 然后打开虚拟机设置→选项→客户机隔离→两个可以都勾选上。

3. 然后重启虚拟机即可。



# 缺少libgfortran.so.4

1. Calculix2.20需要链接libgfortran.so.4，而ubuntu22.04后，默认使用gcc-11，默认仓库也不再提供libgfortran.so.4。使用ldd命令来查看可执行文件需要的动态库，参数需要是完整路径名。=>表示在本机匹配到的具体路径名。

   ```shell
   zj@zj-virtual-machine:~$ ldd /usr/local/bin/ccx
           linux-vdso.so.1 (0x00007ffcaab24000)
           libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007ff8e9cac000)
           libgfortran.so.4 => /lib/x86_64-linux-gnu/libgfortran.so.4 (0x00007ff8e9acb000)
           libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007ff8e99e4000)
           libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ff8e97bc000)
           libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x00007ff8e9770000)
           libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007ff8e9750000)
           libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007ff8e9708000)
           /lib64/ld-linux-x86-64.so.2 (0x00007ff8e9cc4000)
   ```

2. 需要修改/etc/apt/sources.list文件，然后运行sudo apt update，sudo apt install gfortran-7。

   ```shell
   deb [arch=amd64] http://cn.archive.ubuntu.com/ubuntu focal main universe
   ```


# VSCode登录问题

1. 一个虚拟机如果可以使用putty顺利登陆，双向ping也都顺畅，但是使用VSCode远程登陆虚拟机时，可能会报错如下：过程试图写入的管道不存在。这是由于：当前 known_hosts 文件保存的是之前连接的秘钥，现在没有更新。可以打开本地`C:\Users\你的用户名\.ssh\known_hosts`，并删掉远程主机对应的那行秘钥，重新连接即可。或者删掉整个文件即可。


# bash执行

1. 执行bash时可能会报如下错误：

   ```shell
   -bash: ./test.sh: /bin/bash^M: bad interpreter: No such file or directory
   #这是因为该脚本在Windows下编辑后保存的，行尾是CRLF，在VSCode右下角修改为LF即可。
   ```

# 默认编辑器

1. 第一次使用ranger或某些命令行程序时，会提示要使用的默认编辑器，安装过Vim后，可能会出现vim.basic和vim.tiny两个，如果要使用vim，选择basic即可。后续如果要更改默认的编辑器，可以运行select-editor命令，重新选择即可。