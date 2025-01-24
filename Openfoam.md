# 编译安装

1. OpenFOAM需要使用专用的paraview，因为这里边有专门为OpenFOAM编写的读取模块。

2. 如果使用源码编译OpenFOAM时，也可以不手动编译paraview，而使用官方仓库提供的编译好的paraview，然后需要添加paraview的bin目录到PATH中。

   ```shell
   sudo apt install paraviewopenfoam510 #这个只会单独安装paraview
   #添加到.bashrc中
   PATH=$PATH:/opt/paraviewopenfoam510/bin
   ```

3. 新版本的paraview已经原生支持OpenFOAM结果文件了，可以直接`sudo apt install paraview`安装即可。使用的时候，需要在对应的结果目录下创建一个任意的后缀名为.foam的文件即可。OpenFOAM官方推荐使用paraFoam来打开项目目录，此时会自动创建一个临时的.foam文件。也可以使用`paraFoam -touch`来创建一个永久的文件。

4. Ubuntu 22.04中只有paraview的5.10版本。可以从官网下载更新的版本来使用。可以为服务器端安装headless的版本（5.6版本开始提供），其中只有pvpython，pvserver等，不包含paraview GUI客户端，可以在没有X窗口的机器上渲染，分为egl和osmesa2个版本，前者是用显卡的opengl，后者是软件实现，适合于没有显卡的。

   ```shell
   #推荐将tar.gz文件解压缩到/opt目录。
   sudo ln -s /opt/ParaView-5.12.1-osmesa-MPI-Linux-Python3.10-x86_64/bin/pvserver /usr/bin/pvserver #创建pvserver的符号链接到/usr/bin目录下。
   ```

5. ThirdParty-11仓库中主要包含的是Scotch软件的源码，因为早期版本的Debian自带的Scotch版本比较落后，因此需要使用源码编译安装，不过在Ubuntu22.04中，可以使用`sudo apt install scotch`安装即可。

6. 源码目录中可能有冗余的文件，只有包含在Make/files中的文件才会被编译。这点可以从.dep文件的对应发现，例如：`platforms/linux64GccDPInt32Opt/src/conversion/meshTables`中的`boundaryRegion.C.dep`文件。

7. 源代码目录下的lnInclude目录中包含同级目录及其子目录的所有源文件，包括.C和.h。.C后缀名表示C++源文件

   ```shell
   zj@zj-hit:~/OpenFOAM/OpenFOAM-11/src/fileFormats$ tree
   .
   ├── lnInclude
   │   ├── NASCore.C -> ../nas/NASCore.C
   │   ├── NASCore.H -> ../nas/NASCore.H
   │   ├── OBJstream.C -> ../obj/OBJstream.C
   │   ├── OBJstream.H -> ../obj/OBJstream.H
   │   ├── STARCDCore.C -> ../starcd/STARCDCore.C
   │   ├── STARCDCore.H -> ../starcd/STARCDCore.H
   │   ├── vtkUnstructuredReader.C -> ../vtk/vtkUnstructuredReader.C
   │   ├── vtkUnstructuredReader.H -> ../vtk/vtkUnstructuredReader.H
   │   ├── vtkUnstructuredReaderTemplates.C -> ../vtk/vtkUnstructuredReaderTemplates.C
   │   ├── vtkWriteOps.C -> ../vtk/vtkWriteOps.C
   │   ├── vtkWriteOps.H -> ../vtk/vtkWriteOps.H
   │   ├── vtkWriteOpsTemplates.C -> ../vtk/vtkWriteOpsTemplates.C
   │   ├── vtkWritePolyData.H -> ../vtk/vtkWritePolyData.H
   │   └── vtkWritePolyDataTemplates.C -> ../vtk/vtkWritePolyDataTemplates.C
   ├── Make
   │   ├── files
   │   └── options
   ├── nas
   │   ├── NASCore.C
   │   └── NASCore.H
   ├── obj
   │   ├── OBJstream.C
   │   └── OBJstream.H
   ├── starcd
   │   ├── STARCDCore.C
   │   └── STARCDCore.H
   └── vtk
       ├── vtkUnstructuredReader.C
       ├── vtkUnstructuredReader.H
       ├── vtkUnstructuredReaderTemplates.C
       ├── vtkWriteOps.C
       ├── vtkWriteOps.H
       ├── vtkWriteOpsTemplates.C
       ├── vtkWritePolyData.H
       └── vtkWritePolyDataTemplates.C
   
   6 directories, 30 files
   ```

8. 总的配置文件为`/home/zj/OpenFOAM/OpenFOAM-11/etc/bashrc`。

10. debug 调试，可以对软件进行单步执行、堆栈跟踪、调试等操作来发现bug。

11. release 发行版，如果最终调试后程序没有明显bug，可以作为可用的软件分享给他人使用就可以使用这个选项编译。

12. profiling 性能分析。可以对软件执行过程中的cpu利用率，内存占有进行分析。也可以用来发现、分析异常、bug。

13. 常见的和路径相关的宏：

    ```shell
    #如果源码存放路径为/home/zj/OpenFOAM/OpenFOAM-11。
    export WM_PROJECT_INST_DIR=$FOAM_INST_DIR #结果为/home/zj/OpenFOAM
    export WM_PROJECT_DIR=$WM_PROJECT_INST_DIR/$WM_PROJECT-$WM_PROJECT_VERSION #结果为/home/zj/OpenFOAM/OpenFOAM-11
    export WM_DIR=$WM_PROJECT_DIR/wmake #结果为/home/zj/OpenFOAM/OpenFOAM-11/wmake
    export WM_THIRD_PARTY_DIR=$WM_PROJECT_INST_DIR/ThirdParty-$WM_PROJECT_VERSION #结果为/home/zj/OpenFOAM/ThirdParty-11
    export WM_PROJECT_USER_DIR=$HOME/$WM_PROJECT/$USER-$WM_PROJECT_VERSION #结果为/home/zj/OpenFOAM/zj-11，默认在用户的家目录下创建一个用户名-版本的目录，作为用户目录
    export WM_COLLECT_DIR=$WM_PROJECT_DIR/platforms/${WM_OPTIONS}/${PWD////_} #会被脚本检测，如果这个目录不存在则变量为空，默认时该目录不存在。最后一段表示将PWD变量中的/替换为_。
    
    export FOAM_INST_DIR=$(cd $(dirname ${BASH_SOURCE:-$0})/../.. && pwd -P) #结果为/home/zj/OpenFOAM。由于这行代码是在/home/zj/OpenFOAM/OpenFOAM-11/etc/bashrc中执行的，因此BASH_SOURCE就是该脚本文件的路径。获取bashrc的目录部分，然后向上寻找2级父目录，且获取的是物理目录而非符号链接。
    export FOAM_JOB_DIR=$WM_PROJECT_INST_DIR/jobControl #结果为/home/zj/OpenFOAM/jobControl，该目录默认不存在
    
    export ParaView_DIR=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER/ParaView-$ParaView_VERSION #结果为/home/zj/OpenFOAM/ThirdParty-11/platforms/linux64Gcc/ParaView-5.10.1
    export ParaView_INCLUDE_DIR=$ParaView_DIR/include/paraview-$ParaView_MAJOR #默认为空，只有在paraviewSrcDir目录存在时才会定义这个变量。
    export ParaView_LIB_DIR=$ParaView_DIR/lib$paraviewArch$paraviewLibSubDir #默认为空，只有在paraviewSrcDir目录存在时才会定义这个变量。
    ```


# bashrc配置文件

## etc/bashrc

1. 总的配置文件：`etc/bashrc`：

   ```shell
   export WM_PROJECT=OpenFOAM
   export WM_PROJECT_VERSION=11
   ############################################################################
   # 这一部分是用户可以自定义的，不过之后的更新可能会覆盖这个文件。
   # FOAM_INST_DIR是OpenFOAM将要安装到的目录，如果使用bash来执行此文件，则以此文件来推断得到对应的目录，这样和源码目录在一块。也可以手动指定为固定的目录。
   #下面的3行实际是一个表达式，用&&和||连接起来。[ -o ] 表示两侧的变量的或。第二部分是通过当前脚本文件推断源文件路径，第三部分是直接指定为用户的家目录。默认情况下这两个结果是一样的，都是/home/zj/OpenFOAM。
   [ "$BASH" -o "$ZSH_NAME" ] && \
   export FOAM_INST_DIR=$(cd $(dirname ${BASH_SOURCE:-$0})/../.. && pwd -P) || \
   export FOAM_INST_DIR=$HOME/$WM_PROJECT
   # export FOAM_INST_DIR=~$WM_PROJECT #用户名为OpenFOAM的家目录
   # export FOAM_INST_DIR=/opt/$WM_PROJECT #公共的区域，建议使用root安装
   # export FOAM_INST_DIR=/usr/local/$WM_PROJECT
   ############################################################################
   # 下面是一些配置选项，可以由~/.OpenFOAM等目录下的prefs.sh文件覆盖设置
   #- Compiler location: 编译器的位置
   #    WM_COMPILER_TYPE= system | ThirdParty (OpenFOAM)
   export WM_COMPILER_TYPE=system
   
   #- Compiler: 指定编译器名称，Icx是Intel的C++编译器
   #    WM_COMPILER = Gcc | Gcc48 ... Gcc62 | Clang | Icx
   export WM_COMPILER=Gcc
   unset WM_COMPILER_ARCH WM_COMPILER_LIB_ARCH
   
   #- Memory addressing: 内存寻址模式，会决定gcc -m32或-m64选项。在64位系统上可以是32或64，在32位系统上，只能是32
   #    WM_ARCH_OPTION = 32 | 64
   export WM_ARCH_OPTION=64
   
   #- Precision: 浮点数精度，LP是长双精度
   #    WM_PRECISION_OPTION = SP | DP | LP
   export WM_PRECISION_OPTION=DP
   
   #- Label size: 决定INT宏是int还是int64_t
   #    WM_LABEL_SIZE = 32 | 64
   export WM_LABEL_SIZE=32
   
   #- Optimised, debug, profiling: 优化或调试选项，Prof是性能分析
   #    WM_COMPILE_OPTION = Opt | Debug | Prof
   export WM_COMPILE_OPTION=Opt
   
   #- MPI implementation: MPI实现
   #    WM_MPLIB = SYSTEMOPENMPI | OPENMPI | SYSTEMMPI | MPICH | MPICH-GM | HPMPI
   #               | MPI | FJMPI | QSMPI | SGIMPI | INTELMPI
   export WM_MPLIB=SYSTEMOPENMPI
   
   #- Operating System: 操作系统，目前只支持POSIX兼容的
   #    WM_OSTYPE = POSIX | ???
   export WM_OSTYPE=POSIX
   
   #- Floating-point signal handling: 是否设置了浮点异常(除零或者数值溢出)信号处理
   #    set or unset
   export FOAM_SIGFPE=
   
   #- memory initialisation: 是否进行内存初始化
   #    set or unset
   #export FOAM_SETNAN=
   
   # 需要从环境变量中清除的旧目录
   foamOldDirs="$WM_PROJECT_DIR $WM_THIRD_PARTY_DIR \
       $HOME/$WM_PROJECT/$USER $FOAM_USER_APPBIN $FOAM_USER_LIBBIN \
       $WM_PROJECT_SITE $FOAM_SITE_APPBIN $FOAM_SITE_LIBBIN"
   
   # Location of installation 设置安装目录，和FOAM_INST_DIR变量相同
   export WM_PROJECT_INST_DIR=$FOAM_INST_DIR
   export WM_PROJECT_DIR=$WM_PROJECT_INST_DIR/$WM_PROJECT-$WM_PROJECT_VERSION
   
   if [ -d "$WM_PROJECT_DIR" ] #该目录默认存在，这段的功能是获取该目录的物理目录，避免使用符号链接。-d表示检查是否存在且为目录，-e表示检查是否存在。
   then
       WM_PROJECT_DIR_REAL=$(cd $WM_PROJECT_DIR && pwd -P) # -P表示显示物理目录
       if [ -d "$WM_PROJECT_DIR_REAL" -a -e "$WM_PROJECT_DIR_REAL/etc/bashrc" ]
       then
           export WM_PROJECT_DIR=$WM_PROJECT_DIR_REAL #用临时变量替换掉
       fi
       unset WM_PROJECT_DIR_REAL
   fi
   
   # 定位第三方软件目录
   export WM_THIRD_PARTY_DIR=$WM_PROJECT_INST_DIR/ThirdParty-$WM_PROJECT_VERSION
   
   if [ -d "$WM_THIRD_PARTY_DIR" ] #效果同上
   then
       WM_THIRD_PARTY_DIR_REAL=$(cd $WM_THIRD_PARTY_DIR && pwd -P)
       if [ -d "$WM_THIRD_PARTY_DIR_REAL" -a -e "$WM_THIRD_PARTY_DIR_REAL/etc/tools" ]
       then
           export WM_THIRD_PARTY_DIR=$WM_THIRD_PARTY_DIR_REAL
       fi
       unset WM_THIRD_PARTY_DIR_REAL
   fi
   
   # 确定本地的etc目录，一般是没有的
   # unset is equivalent to $WM_PROJECT_INST_DIR/site
   if [ -d "$WM_PROJECT_SITE" ] #这个变量默认为空，因此判断为假
   then
       export WM_PROJECT_SITE
   else
       unset WM_PROJECT_SITE
   fi
   
   # 定位用户文件
   export WM_PROJECT_USER_DIR=$HOME/$WM_PROJECT/$USER-$WM_PROJECT_VERSION
   
   # 导入函数_foamAddPath, _foamAddLib, _foamAddMan, _foamSource, _foamParams。
   . $WM_PROJECT_DIR/etc/config.sh/functions #执行脚本
   
   # Source当前用户或者本地的配置文件，_foamSource就是上一行导入的函数
   _foamSource `$WM_PROJECT_DIR/bin/foamEtcFile prefs.sh` # ` `中的命令是在配置文件目录中寻找名称为prefs.sh的文件。默认不存在这个pref.sh文件，所以_foamSource的参数为空，该函数会直接退出。
   
   # 处理当前脚本的命令行参数，写在系统的bashrc中，一般为空。可以用=键值对的方式来export或unset对应的变量。
   export FOAM_SETTINGS="$@"
   _foamParams $@
   
   # 清理标准环境变量 (PATH, LD_LIBRARY_PATH, MANPATH)
   foamClean=$WM_PROJECT_DIR/bin/foamCleanPath
   #注意，如果使用VSCODE Remote登录到Linux上时，即使在本脚本的开头echo $PATH，结果也会包含OpenFOAM的目录。因为Remote登录时已经将当前脚本完整执行一遍了。想要获得准确的结果可以用putty或者退出remote重新登陆
   #此时PATH为，清理前后不变
   /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/zj/.local/bin
   # 从PATH中清理foamOldDirs的目录，并重新赋值给PATH。
   cleaned=`$foamClean "$PATH" "$foamOldDirs"` && PATH="$cleaned"
   # 清理 LD_LIBRARY_PATH 前后都为空
   cleaned=`$foamClean "$LD_LIBRARY_PATH" "$foamOldDirs"` \
       && LD_LIBRARY_PATH="$cleaned"
   # 清理 MANPATH 前后都为空
   cleaned=`$foamClean "$MANPATH" "$foamOldDirs"` && MANPATH="$cleaned"
   
   export PATH LD_LIBRARY_PATH MANPATH
   
   # Source 项目配置文件
   _foamSource $WM_PROJECT_DIR/etc/config.sh/settings
   _foamSource $WM_PROJECT_DIR/etc/config.sh/aliases
   
   # 为可选软件包 Source用户配置文件
   _foamSource `$WM_PROJECT_DIR/bin/foamEtcFile config.sh/mpi`
   _foamSource `$WM_PROJECT_DIR/bin/foamEtcFile config.sh/paraview`
   _foamSource `$WM_PROJECT_DIR/bin/foamEtcFile config.sh/ensight`
   _foamSource `$WM_PROJECT_DIR/bin/foamEtcFile config.sh/gperftools`
   
   # 再次清理环境变量，本次只是去重，因为foamClean只有一个参数
   #- 清理 PATH
   cleaned=`$foamClean "$PATH"` && PATH="$cleaned"
   
   #- 清理 LD_LIBRARY_PATH
   cleaned=`$foamClean "$LD_LIBRARY_PATH"` && LD_LIBRARY_PATH="$cleaned"
   
   #- 清理 MANPATH (trailing ':' to find system pages)
   cleaned=`$foamClean "$MANPATH"`: && MANPATH="$cleaned"
   
   export PATH LD_LIBRARY_PATH MANPATH
   
   #- 清理 LD_PRELOAD
   if [ -n "$LD_PRELOAD" ] #检查字符串是否为非空，这里默认为空
   then
       cleaned=`$foamClean "$LD_PRELOAD"` && LD_PRELOAD="$cleaned"
       export LD_PRELOAD
   fi
   
   # 清理此脚本中用到的一些变量，避免污染shell执行环境
   unset cleaned foamClean foamOldDirs
   
   # 再次执行脚本，以卸载初始化函数
   . $WM_PROJECT_DIR/etc/config.sh/functions
   
   # 执行bash_completion脚本
   [ "$BASH" ] && . $WM_PROJECT_DIR/etc/config.sh/bash_completion
   ```


## etc/config.sh/functions

1. `etc/config.sh/functions`：

   ```shell
   if [ -z "$WM_BASH_FUNCTIONS" ] #判断字符串是否为空
   then
       WM_BASH_FUNCTIONS=loaded #一个标记变量，第一次执行时，会进入到这个分支，第二次执行时就会执行else分支，把上一次执行时定义的_foam系列函数都unset掉。
       
   # _foamSource会依次Source所有的参数，如果定义了FOAM_VERBOSE，则每Source一个文件就会输出一句Sourcing: 文件名。例如：
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/settings
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/compiler
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/aliases
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/mpi
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/paraview
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/ensight
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/gperftools
       _foamSource()
       {
           while [ $# -ge 1 ] #参数数量>=1
           do #PS1是shell的提示符，只有交互式shell才非空，此时才可以输出到终端。
               [ "$FOAM_VERBOSE" -a "$PS1" ] && echo "Sourcing: $1" 1>&2
               . $1 #一次source一个参数，然后移除
             shift
           done
       }
   #逐个处理命令行参数，只支持两种类型，name=和name=value
       _foamParams()
       {
           while [ $# -gt 0 ] #参数数量>0
           do
               case "$1" in
               -*) #以-开头的选项
                   # Stray option (not meant for us here) -> get out
                   break
                   ;;
               *=)
                   # name=，会执行unset name。也会受到FOAM_VERBOSE的影响
                   [ "$FOAM_VERBOSE" -a "$PS1" ] && echo "unset ${1%=}" 1>&2
                   eval "unset ${1%=}" # %=表示删除末尾的=
                   ;;
               *=*)
                   # name=value，会执行export name=value
                   [ "$FOAM_VERBOSE" -a "$PS1" ] && echo "export $1" 1>&2
                   eval "export $1"
                   ;;
               esac
               shift
           done
       }
       # 将参数逐个添加到PATH的开头
       _foamAddPath()
       {
           while [ $# -ge 1 ]
           do
               export PATH=$1:$PATH #用:拼接
               shift
           done
       }
       # 将参数逐个添加到LD_LIBRARY_PATH的开头，该变量默认为空
       _foamAddLib()
       {
           while [ $# -ge 1 ]
           do
               export LD_LIBRARY_PATH=$1:$LD_LIBRARY_PATH
               shift
           done
       }
       # 将参数逐个添加到MANPATH的开头
       _foamAddMan()
       {
           while [ $# -ge 1 ]
           do
               export MANPATH=$1:$MANPATH
               shift
           done
       }
   else
       # 再次运行脚本可以清理环境，unset所有定义的变量和函数
       unset WM_BASH_FUNCTIONS
       unset _foamAddPath _foamAddLib _foamAddMan
       unset _foamSource _foamParams
   fi
   ```


## bin/foamEtcFile

1. foamEtcFile：

   ```shell
   zj@zj-hit:~$ foamEtcFile -list #输出所有查找的目录，仅查找，不执行
   /home/zj/.OpenFOAM/11
   /home/zj/.OpenFOAM
   /home/zj/OpenFOAM/site/11/etc
   /home/zj/OpenFOAM/site/etc
   /home/zj/OpenFOAM/OpenFOAM-11/etc
   ```

2. `bin/foamEtcFile`：

   ```shell
   #!/bin/sh
   #搜寻OpenFOAM的配置文件，一般在安装的etc目录下，也可能出现在如下目录下，按照给出的顺序搜索。
   # user level: \${HOME}/.OpenFOAM
   # group level: \$FOAM_INST_DIR/site
   # other level: \$WM_PROJECT_DIR/etc
   error() {
       [ "${optQuiet:-$optSilent}" = true ] && exit 1 #如果指定了-quiet或-silent参数，则不输出错误提示，直接退出。
       exec 1>&2 #没有指定任何命令，因此会将当前shell的流1重定向到流2中，表示所有的输出都是错误信息。
       while [ "$#" -ge 1 ]; do echo "$1"; shift; done #逐一输出所有的参数。
       usage #执行usage函数。
       exit 1
   }
   # $0在这里是/home/zj/OpenFOAM/OpenFOAM-11/bin/foamEtcFile
   # bin目录，也就是当前脚本所在的目录: /home/zj/OpenFOAM/OpenFOAM-11/bin
   binDir="$(cd -- "$(dirname "$0")" >/dev/null 2>&1 || exit ; pwd -P)"
   
   # 项目目录: /home/zj/OpenFOAM/OpenFOAM-11
   projectDir="${binDir%/bin}" #从字符串的结尾删除/bin
   
   # 目录前缀(和$FOAM_INST_DIR一样): /home/zj/OpenFOAM
   prefixDir="${projectDir%/*}" #从字符串的结尾删除/*
   
   # 项目目录的名称: OpenFOAM-11
   projectDirName="${projectDir##*/}" #从字符串的开头删除*/
   
   # 为后续使用，先取消定义
   unset versionNum
   
   # 处理标准和Debian命名约定
   case "$projectDirName" in
       OpenFOAM-*)     # 标准命名约定 OpenFOAM-<VERSION>
           version="${projectDirName##OpenFOAM-}"
           ;;
       openfoam[0-9]*) # debian 命名约定，例如openfoam5
           versionNum="${projectDirName##openfoam}"
           case "$versionNum" in
           [4-9]) # v4-9
               version="$versionNum"
               ;;
           [1-2][0-9]) # v10 onwards
               version="$versionNum"
               ;;
           3[0-9]) # e.g. v3.0
               version=$(echo "$versionNum" | sed -e 's@\(.\)\(.\)@\1.\2@') #将32变为3.2
               ;;
           [1-2][0-9][0-9]) # e.g. v1.7.0
               version=$(echo "$versionNum" | sed -e 's@\(.\)\(.\)\(.\)@\1.\2.\3@') #将170变为1.7.0
               ;;
           *)
               version="$WM_PROJECT_VERSION"
               ;;
           esac
           ;;
       openfoam-dev) # debian 命名约定
           versionNum="${projectDirName##openfoam}" #为 -dev
           version="${versionNum##-}" #为 dev
           ;;
       *)
           echo "Error : unknown/unsupported naming convention"
           exit 1
           ;;
   esac
   
   # 默认模式是 'ugo'
   mode=ugo
   unset optAll optList optQuiet optSilent
   
   # 解析选项
   while [ "$#" -gt 0 ]
   do
       case "$1" in
       -h | -help)
           usage && exit 0
           ;;
       -a | -all)
           optAll=true
           ;;
       -l | -list)
           optList=true
           ;;
       -m | -mode)
           [ "$#" -ge 2 ] || error "'$1' option requires an argument"
           mode="$2" #该选项需要一个参数
           # sanity check:
           case "$mode" in
           *u* | *g* | *o* ) #只支持u g o三个参数
              ;;
           *)
              error "'$1' option with invalid mode '$mode'"
              ;;
           esac
           shift
           ;;
       -p | -prefix)
           [ "$#" -ge 2 ] || error "'$1' option requires an argument"
           prefixDir="$2"
           shift
           ;;
       -q | -quiet)
           optQuiet=true
           ;;
       -s | -silent)
           optSilent=true
           ;;
       -v | -version)
           [ "$#" -ge 2 ] || error "'$1' option requires an argument"
           version="$2"
           # 将 x.y.z 转化为 xyz，Debian命名约定使用
           if [ -n "$versionNum" ]
           then
               versionNum=$(echo "$version" | sed -e 's@\.@@g')
           fi
           shift
           ;;
       --)
           shift
           break
           ;;
       -*)
           error "unknown option: '$*'"
           ;;
       *)
           break
           ;;
       esac
       shift
   done
   
   # 调试代码，可以取消注释以输出中间变量的值:
   # echo "Installed locations:"
   # for i in projectDir prefixDir projectDirName version versionNum
   # do
   #     eval echo "$i=\$$i"
   # done
   
   # Save the essential bits of information
   # 去除掉开头的 ~OpenFOAM/ (used in Foam::findEtcFile)
   nArgs=$# #脚本参数个数
   fileName="${1#~OpenFOAM/}"
   
   # 定义要被搜索的各种路径:
   unset dirList
   case "$mode" in
   *u*)  # user
       userDir="$HOME/.${WM_PROJECT:-OpenFOAM}"
       dirList="$dirList $userDir/$version $userDir"
       ;;
   esac
   
   case "$mode" in
   *g*)  # group (site)
       siteDir="${WM_PROJECT_SITE:-$prefixDir/site}"
       dirList="$dirList $siteDir/$version/etc $siteDir/etc"
       ;;
   esac
   
   case "$mode" in
   *o*)  # other (shipped)
       if [ -n "$versionNum" ]
       then
           # debian packaging
           dirList="$dirList $prefixDir/openfoam$versionNum/etc"
       else
           # standard packaging
           dirList="$dirList $prefixDir/${WM_PROJECT:-OpenFOAM}-$version/etc"
       fi
       ;;
   esac
   set -- $dirList
   
   # The main routine
   exitCode=0
   if [ "$optList" = true ]
   then
       # list directories, or potential file locations
       [ "$nArgs" -le 1 ] || error
   
       # a silly combination, but -quiet does have precedence
       [ "$optQuiet" = true ] && exit 0
   
       for dir
       do
           if [ "$nArgs" -eq 1 ]
           then
               echo "$dir/$fileName"
           else
               echo "$dir"
           fi
       done
   else
       [ "$nArgs" -eq 1 ] || error
   
       # general error, eg file not found
       exitCode=2
   
       for dir
       do
           if [ -f "$dir/$fileName" ]
           then
               exitCode=0
               if [ "$optQuiet" = true ]
               then
                   break
               else
                   echo "$dir/$fileName"
                   [ "$optAll" = true ] || break
               fi
           fi
       done
   fi
   exit $exitCode #根据退出码退出
   ```

## bin/foamCleanPath

1. `bin/foamCleanPath`：

   ```shell
   #     Usage: foamCleanPath [-strip] path [wildcard] .. [wildcard]
   #         - 去除重复的目录
   #         - 去除和wildcard匹配的目录，可选参数
   #         - 去除不可访问的目录 (如果使用了 -strip选项)
   unset strip
   # 解析选项
   while [ "$#" -gt 0 ]
   do
       case "$1" in
       -h | -help)
           usage && exit 0
           ;;
       -strip)
           strip=true
           shift
           ;;
       -*)
           error
           ;;
       *)
           break
           ;;
       esac
   done
   
   [ "$#" -ge 1 ] || error #如果没有指定path参数，则报错
   
   dirList="$1" #获取path参数
   shift
   
   [ -n "$dirList" ] || exit 2    # 如果dirlist为空，则直接退出
   # 可以取消下一行的#DEBUG，以输出调试信息
   #DEBUG echo "input>$dirList<" 1>&2
   
   # 保存当前的IFS，设置新的IFS，使用:和空格分隔
   oldIFS="$IFS"
   IFS=': '
   
   # 将剩余的"wildcard1 ... wildcardN" 参数，可能通过1个参数传递，也可能包含:分隔符
   set -- $*
   
   # 使用sed清除掉wildcards
   while [ "$#" -ge 1 ]
   do
       wildcard=$1
       shift
       ##DEBUG echo "remove>$wildcard<" 1>&2
       if [ -n "$wildcard" ]
       then
           dirList=$(echo "$dirList:" | sed -e "s|${wildcard}[^:]*:||g")
       fi
   done
   # 使用:和空格分隔
   IFS=': '
   set -- $dirList
   
   ##DEBUG echo "intermediate>$dirList<" 1>&2
   
   # 重构list
   unset dirList
   for dir
   do
       ##DEBUG echo "check>$dir<" 1>&2
       if [ -e "$dir" ] # dir必须存在
       then
           duplicate=$(echo " $dirList " | sed -ne "s: $dir :DUP:p") #没有重复的dirs
           if [ ! "$duplicate" ]
           then
               dirList="$dirList $dir"
           fi
       elif [ "$strip" != true ]
       then
           # 如果不在strip模式下，则输出不存在的目录
           dirList="$dirList $dir"
       fi
   done
   
   # 使用空格分隔
   IFS=' '
   set -- $dirList
   
   # 使用':'组合
   IFS=':'
   dirList="$*"
   
   # 恢复IFS
   IFS="$oldIFS"
   
   ##DEBUG echo "output>$dirList<" 1>&2
   echo "$dirList"
   ```


## etc/config.h/settings

1. `etc/config.h/settings`：

   ```shell
   # 根据系统类型设置环境变量
   export WM_ARCH=`uname -s` #目前为Linux
   case "$WM_ARCH" in
   Linux)
       WM_ARCH=linux
       # 编译器设置
       case `uname -m` in #硬件架构
           i686) #Intel 32位CPU
               export WM_ARCH_OPTION=32
               export WM_CC='gcc'
               export WM_CXX='g++'
               export WM_CFLAGS='-fPIC'
               export WM_CXXFLAGS='-fPIC -std=c++0x'
               export WM_LDFLAGS=
           ;;
       x86_64) #Intel 64位CPU
           case "$WM_ARCH_OPTION" in #目标软件架构，对于64位CPU，可以是32或64，这个是在etc/bashrc中设置的
           32)
               export WM_COMPILER_ARCH=64
               export WM_CC='gcc'
               export WM_CXX='g++'
               export WM_CFLAGS='-m32 -fPIC'
               export WM_CXXFLAGS='-m32 -fPIC -std=c++0x'
               export WM_LDFLAGS='-m32'
               ;;
           64) #实际执行的是这个分支
               WM_ARCH=linux64 #对于32位的情况，WM_ARCH为linux
               export WM_COMPILER_LIB_ARCH=64
               export WM_CC='gcc'
               export WM_CXX='g++'
               export WM_CFLAGS='-m64 -fPIC'
               export WM_CXXFLAGS='-m64 -fPIC -std=c++0x'
               export WM_LDFLAGS='-m64'
               ;;
           *)
               echo "Unknown WM_ARCH_OPTION '$WM_ARCH_OPTION', should be 32 or 64" 1>&2
           ;;
           esac
           ;;
   
       aarch64) #arm64架构
           WM_ARCH=linuxArm64
           export WM_COMPILER_LIB_ARCH=64
           export WM_CC='gcc'
           export WM_CXX='g++'
           export WM_CFLAGS='-fPIC'
           export WM_CXXFLAGS='-fPIC -std=c++0x'
           export WM_LDFLAGS=
           ;;
   
       armv7l)
           WM_ARCH=linuxARM7
           export WM_ARCH_OPTION=32
           export WM_COMPILER_LIB_ARCH=32
           export WM_CC='gcc'
           export WM_CXX='g++'
           export WM_CFLAGS='-fPIC'
           export WM_CXXFLAGS='-fPIC -std=c++0x'
           export WM_LDFLAGS=
           ;;
       ppc64) #IBM PowerPC处理器
           WM_ARCH=linuxPPC64
           export WM_COMPILER_LIB_ARCH=64
           export WM_CC='gcc'
           export WM_CXX='g++'
           export WM_CFLAGS='-m64 -fPIC'
           export WM_CXXFLAGS='-m64 -fPIC -std=c++0x'
           export WM_LDFLAGS='-m64'
           ;;
       ppc64le) #小端
           WM_ARCH=linuxPPC64le
           export WM_COMPILER_LIB_ARCH=64
           export WM_CC='gcc'
           export WM_CXX='g++'
           export WM_CFLAGS='-m64 -fPIC'
           export WM_CXXFLAGS='-m64 -fPIC -std=c++0x'
           export WM_LDFLAGS='-m64'
           ;;
       *)
           echo Unknown processor type `uname -m` for Linux 1>&2
           ;;
       esac
       ;;
   SunOS)
       WM_ARCH=SunOS64
       WM_MPLIB=FJMPI
       export WM_COMPILER_LIB_ARCH=64
       export WM_CC='gcc'
       export WM_CXX='g++'
       export WM_CFLAGS='-mabi=64 -fPIC'
       export WM_CXXFLAGS='-mabi=64 -fPIC -std=c++0x'
       export WM_LDFLAGS='-mabi=64 -G0'
       ;;
   *)  # 不支持的操作系统
       /bin/cat <<USAGE 1>&2
   
       Your "$WM_ARCH" operating system is not supported by this release
       of OpenFOAM. For further assistance, please contact https://openfoam.org
   
   USAGE
       ;;
   esac
   
   # 作业控制的目录，默认不存在
   export FOAM_JOB_DIR=$WM_PROJECT_INST_DIR/jobControl
   
   # wmake 配置
   export WM_DIR=$WM_PROJECT_DIR/wmake
   export WM_LINK_LANGUAGE=c++
   export WM_LABEL_OPTION=Int$WM_LABEL_SIZE
   export WM_OPTIONS=$WM_ARCH$WM_COMPILER$WM_PRECISION_OPTION$WM_LABEL_OPTION$WM_COMPILE_OPTION #默认为linux64GccDPInt32Opt
   
   # 基础可执行/库文件的位置，也是编译链接结果存放的位置
   export FOAM_APPBIN=$WM_PROJECT_DIR/platforms/$WM_OPTIONS/bin
   export FOAM_LIBBIN=$WM_PROJECT_DIR/platforms/$WM_OPTIONS/lib
   
   # 外部(第三方)库位置
   export FOAM_EXT_LIBBIN=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER$WM_PRECISION_OPTION$WM_LABEL_OPTION/lib
   
   # 本地特定目录
   siteDir="${WM_PROJECT_SITE:-$WM_PROJECT_INST_DIR/site}" #默认为/home/zj/OpenFOAM/site，但不存在
   
   # 本地共享的可执行和库位置
   # 和~OpenFOAM类似的命名规范
   export FOAM_SITE_APPBIN=$siteDir/$WM_PROJECT_VERSION/platforms/$WM_OPTIONS/bin
   export FOAM_SITE_LIBBIN=$siteDir/$WM_PROJECT_VERSION/platforms/$WM_OPTIONS/lib
   
   # 用户的可执行/库文件的位置，推荐将用户自定义的APP放在这里
   export FOAM_USER_APPBIN=$WM_PROJECT_USER_DIR/platforms/$WM_OPTIONS/bin
   export FOAM_USER_LIBBIN=$WM_PROJECT_USER_DIR/platforms/$WM_OPTIONS/lib
   
   # 动态代码模板
   # 默认的位置是 "~OpenFOAM/codeTemplates/dynamicCode" 但是并不存在
   # export FOAM_CODE_TEMPLATES=$WM_PROJECT_DIR/etc/codeTemplates/dynamicCode
   
   # 一些辅助的目录变量
   export FOAM_ETC=$WM_PROJECT_DIR/etc
   export FOAM_APP=$WM_PROJECT_DIR/applications
   export FOAM_SRC=$WM_PROJECT_DIR/src
   export FOAM_TUTORIALS=$WM_PROJECT_DIR/tutorials
   export FOAM_UTILITIES=$FOAM_APP/utilities
   export FOAM_SOLVERS=$FOAM_APP/solvers
   export FOAM_MODULES=$FOAM_APP/modules
   export FOAM_RUN=$WM_PROJECT_USER_DIR/run
   
   # 将application，bins目录添加到PATH中，可以观察到有三个地方，USER，SITE，源代码目录中。
   #此时PATH为：
   /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/zj/.local/bin
   
   _foamAddPath $FOAM_USER_APPBIN:$FOAM_SITE_APPBIN:$FOAM_APPBIN #参数只有一个，而非3个
   #此时PATH为：
   /home/zj/OpenFOAM/zj-11/platforms/linux64GccDPInt32Opt/bin:/home/zj/OpenFOAM/site/11/platforms/linux64GccDPInt32Opt/bin:/home/zj/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/zj/.local/bin
   # 将wmake脚本的目录添加到PATH中，仅运行时环境不需要
   [ -d "$WM_DIR" ] && PATH=$WM_DIR:$PATH #增加了个/home/zj/OpenFOAM/OpenFOAM-11/wmake
   
   # 将OpenFOAM脚本目录添加到PATH中
   export PATH=$WM_PROJECT_DIR/bin:$PATH #增加了个/home/zj/OpenFOAM/OpenFOAM-11/bin
   
   # 将本地特定目录添加到PATH中
   if [ -d "$siteDir/bin" ] # 目录为/home/zj/OpenFOAM/site/bin，但是一般不存在
   then
       _foamAddPath "$siteDir/bin"
   fi
   if [ -d "$siteDir/$WM_PROJECT_VERSION/bin" ] # 也不存在
   then
       _foamAddPath "$siteDir/$WM_PROJECT_VERSION/bin"
   fi
   unset siteDir
   
   #将目录添加到LD_LIBRARY_PATH中，确保外部库的哑版本放在最后
   _foamAddLib  $FOAM_USER_LIBBIN:$FOAM_SITE_LIBBIN:$FOAM_LIBBIN:$FOAM_EXT_LIBBIN:$FOAM_LIBBIN/dummy
   
   # 编译器设置
   unset gcc_version gmp_version mpfr_version mpc_version
   unset MPFR_ARCH_PATH GMP_ARCH_PATH
   
   # 编译器的位置
   if [ -z "$WM_COMPILER_TYPE" ] #默认为system，在bashrc的开头设置，不为空
   then
       WM_COMPILER_TYPE=system
       echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
       echo "    WM_COMPILER_TYPE not set, using '$WM_COMPILER_TYPE'" 1>&2
   fi
   
   # 载入配置好的编译器版本，不管编译器类型
   _foamSource `$WM_PROJECT_DIR/bin/foamEtcFile config.sh/compiler` #会先找到/home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/compiler文件，然后source它。经过观察脚本，实际什么也不会执行
   
   case "$WM_COMPILER_TYPE" in
   OpenFOAM | ThirdParty)
   
       if [ -n "$gcc_version" ]
       then
           gccDir=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER_ARCH/$gcc_version
           gmpDir=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER_ARCH/$gmp_version
           mpfrDir=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER_ARCH/$mpfr_version
           mpcDir=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER_ARCH/$mpc_version
   
           # Check that the compiler directory can be found
           [ -d "$gccDir" ] || {
               echo 1>&2
               echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
               echo "    Cannot find $gccDir installation." 1>&2
               echo "    Please install this compiler version or if you wish to" \
                    " use the system compiler," 1>&2
               echo "    change the 'WM_COMPILER_TYPE' setting to 'system'" 1>&2
               echo
           }
   
           _foamAddMan     $gccDir/man
           _foamAddPath    $gccDir/bin
   
           # Add compiler libraries to run-time environment
           _foamAddLib     $gccDir/lib$WM_COMPILER_LIB_ARCH
   
           # Add gmp/mpfr libraries to run-time environment
           _foamAddLib     $gmpDir/lib$WM_COMPILER_LIB_ARCH
           _foamAddLib     $mpfrDir/lib$WM_COMPILER_LIB_ARCH
   
           # Add mpc libraries (not need for older gcc) to run-time environment
           if [ -n "$mpc_version" ]
           then
               _foamAddLib     $mpcDir/lib$WM_COMPILER_LIB_ARCH
           fi
       fi
       unset gcc_version gccDir
       unset gmp_version gmpDir  mpfr_version mpfrDir  mpc_version mpcDir
   
       if [ -n "$clang_version" ]
       then
           clangDir=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER_ARCH/$clang_version
   
           # Check that the compiler directory can be found
           [ -d "$clangDir" ] || {
               echo 1>&2
               echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
               echo "    Cannot find $clangDir installation." 1>&2
               echo "    Please install this compiler version or if you wish to" \
                    " use the system compiler," 1>&2
               echo "    change the 'WM_COMPILER_TYPE' setting to 'system'" 1>&2
               echo 1>&2
           }
   
           _foamAddMan     $clangDir/share/man
           _foamAddPath    $clangDir/bin
       fi
       unset clang_version clangDir
       ;;
   system)
       # 使用系统默认的编译器
       ;;
   *)
       echo "Warn: WM_COMPILER_TYPE='$WM_COMPILER_TYPE' is unsupported" 1>&2
       echo "   treating as 'system' instead" 1>&2
       ;;
   esac
   ```


## etc/config.sh/compiler

1. `etc/config.sh/compiler`：

   ```shell
   case "$WM_COMPILER_TYPE" in #默认是system，因此什么都不会执行
   OpenFOAM | ThirdParty)
       # GMP, MPFR and MPC的默认版本，可以覆盖
       gmp_version=gmp-5.1.2
       mpfr_version=mpfr-3.1.2
       mpc_version=mpc-1.0.1
   
       case "$WM_COMPILER" in
       Gcc55)
           gcc_version=gcc-5.5.0
           ;;
       Gcc65)
           gcc_version=gcc-6.5.0
           ;;
       Gcc74)
           gcc_version=gcc-7.4.0
           ;;
       Gcc82)
           gcc_version=gcc-8.2.0
           ;;
       Gcc95)
           gcc_version=gcc-9.5.0
           ;;
       Gcc111)
           gcc_version=gcc-11.1.0
           ;;
       Gcc121)
           gcc_version=gcc-12.1.0
           ;;
       Clang)
           # Using clang - not gcc
           export WM_CC='clang'
           export WM_CXX='clang++'
           clang_version=llvm-3.7.0
           ;;
       *)
           echo 1>&2
           echo "Warning in $WM_PROJECT_DIR/etc/config.sh/compiler:" 1>&2
           echo "    Unknown OpenFOAM compiler type '$WM_COMPILER'" 1>&2
           echo "    Please check your settings" 1>&2
           echo 1>&2
           ;;
       esac
       ;;
   esac
   ```

## etc/config.sh/aliases

1. `etc/config.sh/aliases`：

   ```shell
   # 编译选项设置
   alias wmSet='. $WM_PROJECT_DIR/etc/bashrc' #执行bashrc配置文件
   alias wm64='wmSet WM_ARCH_OPTION=64' #使用键值对指定bashrc脚本的参数
   alias wm32='wmSet WM_ARCH_OPTION=32'
   alias wmSP='wmSet WM_PRECISION_OPTION=SP'
   alias wmDP='wmSet WM_PRECISION_OPTION=DP'
   alias wmLP='wmSet WM_PRECISION_OPTION=LP'
   # 清除环境变量和alias
   alias wmUnset='. $WM_PROJECT_DIR/etc/config.sh/unset'
   # 打开或关闭 wmakeScheduler。也需要设置 WM_HOSTS
   alias wmSchedOn='export WM_SCHEDULER=$WM_PROJECT_DIR/wmake/wmakeScheduler'
   alias wmSchedOff='unset WM_SCHEDULER'
   # 切换目录
   alias foam='cd $WM_PROJECT_DIR'
   
   if [ -n "$WM_PROJECT_SITE" ]
   then
       alias foamSite='cd $WM_PROJECT_SITE'
   else
       alias foamSite='cd $WM_PROJECT_INST_DIR/site'
   fi
   alias src='cd $FOAM_SRC'
   alias lib='cd $FOAM_LIBBIN'
   alias app='cd $FOAM_APP'
   alias sol='cd $FOAM_SOLVERS'
   alias mod='cd $FOAM_MODULES'
   alias util='cd $FOAM_UTILITIES'
   alias tut='cd $FOAM_TUTORIALS'
   alias run='cd $FOAM_RUN'
   # 刷新环境变量
   # 为了向后兼容，在定义前，会先unalias wmRefresh，如果它是一个alias的话。实际上整个工程中只在这里定义了wmRefresh。
   if command -V wmRefresh 2> /dev/null | head -1 | grep -q "function" #wmRefresh是函数，在中文环境下，command -V 输出的第一行为 "wmRefresh 是函数"。功能类似于type。
   #第一次执行时，没有这个变量，因此判断为假，会unalias一个不存在的东西，无关紧要。第二次执行时，wmRefresh已经作为函数存在了，此时应该unset，而中文环境下，判断为假，还是回去执行unalias。不过也无关紧要。
   then
       unset wmRefresh
   else
       unalias wmRefresh 2> /dev/null
   fi
   wmRefresh() #定义wmRefresh函数
   {
       wmProjectDir=$WM_PROJECT_DIR
       foamSettings=$FOAM_SETTINGS
       . $wmProjectDir/etc/config.sh/unset #先unset所有变量
       . $wmProjectDir/etc/bashrc $foamSettings #再重新执行etc/bashrc
   }
   # 改变OpenFOAM版本
   unset foamVersion
   foamVersion() # 输出OpenFOAM的版本，默认为OpenFOAM-11。或者根据参数切换版本，例如foamVersion10会切换到OpenFOAM-10。
   {
       if [ "$1" ]; then #可以手动指定一个版本号，如果指定了本地不存在的版本号，则会导致环境错乱，需要重新运行bash。
           foamInstDir=$FOAM_INST_DIR
           wmUnset #为下一步执行bashrc，先取消所有的变量设置。
           . $foamInstDir/OpenFOAM-$1/etc/bashrc #执行对应版本的配置文件
           foam #切换到对应的目录
           echo "Changed to OpenFOAM-$1" 1>&2
       else
           echo "OpenFOAM-$WM_PROJECT_VERSION" 1>&2
       fi
   }
   # 改变Paraview版本
   unset foamPV
   foamPV()
   {
       . $WM_PROJECT_DIR/etc/config.sh/paraview ParaView_VERSION=$1 #带一个参数
       echo "paraview-$ParaView_VERSION  (major: $ParaView_MAJOR)" 1>&2
   }
   ```


## config.sh/unset

1. config.sh/unset：

   ```shell
   #   尽可能多地删除OpenFOAM的环境设置
   #-----------------------------------------------------------------------------
   # Clean standard environment variables (PATH, LD_LIBRARY_PATH, MANPATH)
   foamClean=$WM_PROJECT_DIR/bin/foamCleanPath
   [ -f "$foamClean" -a -x "$foamClean" ] || unset foamClean #检查路径名是否是文件，且可执行。默认第一部分为真，因此不用执行第二部分。
   
   # 需要用从环境变量中清理的旧目录
   foamOldDirs="$WM_PROJECT_DIR $WM_THIRD_PARTY_DIR \
       $HOME/$WM_PROJECT/$USER $FOAM_USER_APPBIN $FOAM_USER_LIBBIN \
       $WM_PROJECT_SITE $FOAM_SITE_APPBIN $FOAM_SITE_LIBBIN $ParaView_DIR"
   
   # Unset WM_* environment variables
   unset WM_ARCH
   unset WM_ARCH_OPTION
   unset WM_CC
   unset WM_CFLAGS
   unset WM_COMPILER
   unset WM_COMPILER_TYPE
   unset WM_COMPILER_LIB_ARCH
   unset WM_COMPILE_OPTION
   unset WM_CXX
   unset WM_CXXFLAGS
   unset WM_DIR
   unset WM_HOSTS
   unset WM_LABEL_OPTION
   unset WM_LABEL_SIZE
   unset WM_LDFLAGS
   unset WM_LINK_LANGUAGE
   unset WM_MPLIB
   unset WM_NCOMPPROCS
   unset WM_OPTIONS
   unset WM_OSTYPE
   unset WM_PRECISION_OPTION
   unset WM_PROJECT
   unset WM_PROJECT_DIR
   unset WM_PROJECT_INST_DIR
   unset WM_PROJECT_SITE
   unset WM_PROJECT_USER_DIR
   unset WM_PROJECT_VERSION
   unset WM_SCHEDULER
   unset WM_THIRD_PARTY_DIR
   
   # Unset FOAM_* environment variables
   unset FOAM_APPBIN
   unset FOAM_APP
   unset FOAM_CODE_TEMPLATES
   unset FOAM_ETC
   unset FOAM_EXT_LIBBIN
   unset FOAM_INST_DIR
   unset FOAM_JOB_DIR
   unset FOAM_LIBBIN
   unset FOAM_MPI
   unset FOAM_RUN
   unset FOAM_SETTINGS
   unset FOAM_SIGFPE
   unset FOAM_SIGNAN
   unset FOAM_SITE_APPBIN
   unset FOAM_SITE_LIBBIN
   unset FOAM_SOLVERS
   unset FOAM_MODULES
   unset FOAM_SRC
   unset FOAM_TUTORIALS
   unset FOAM_USER_APPBIN
   unset FOAM_USER_LIBBIN
   unset FOAM_UTILITIES
   
   # Unset MPI-related environment variables
   unset MPI_ARCH_PATH
   unset MPI_BUFFER_SIZE
   
   # Undefine OPAL_PREFIX if set to one of the paths on foamOldDirs
   if [ -z "$($foamClean "$OPAL_PREFIX" "$foamOldDirs")" ]
   then
       unset OPAL_PREFIX
   fi
   
   # Unset Ensight/ParaView-related environment variables
   unset ENSIGHT9_READER
   unset CMAKE_HOME
   unset ParaView_DIR
   unset ParaView_INCLUDE_DIR
   unset ParaView_LIB_DIR
   unset ParaView_MAJOR
   unset ParaView_VERSION
   unset ParaView_GL
   unset PV_PLUGIN_PATH
   
   # 分别从PATH, LD_LIBRARY_PATH, MANPATH中清理$foamOldDirs
   if [ -n "$foamClean" ]
   then
       cleaned=`$foamClean "$PATH" "$foamOldDirs"` && PATH="$cleaned"
       cleaned=`$foamClean "$LD_LIBRARY_PATH" "$foamOldDirs"` && LD_LIBRARY_PATH="$cleaned"
       cleaned=`$foamClean "$MANPATH" "$foamOldDirs"` && MANPATH="$cleaned"
   fi
   
   #如果对应的环境变量为空时，就unset它。因为这表示在执行OpenFOAM配置前，它也为空，也就是没有定义。
   [ -n "$LD_LIBRARY_PATH" ] || unset LD_LIBRARY_PATH
   [ -n "$MANPATH" ] || unset MANPATH
   [ -n "$LD_PRELOAD" ] || unset LD_PRELOAD
   
   unset cleaned foamClean foamOldDirs
   # Cleanup aliases
   unalias wmSet
   unalias wm64
   unalias wm32
   unalias wmSP
   unalias wmDP
   
   unalias wmUnset
   
   unalias wmSchedOn
   unalias wmSchedOff
   
   unalias foam
   unalias foamSite
   
   unalias src
   unalias lib
   unalias app
   unalias sol
   unalias util
   unalias tut
   unalias run
   
   unset wmRefresh
   unset foamVersion
   unset foamPV
   ```


## config.sh/mpi

1. config.sh/mpi：

   ```shell
   # MPI启动脚本
   unset MPI_ARCH_PATH MPI_HOME FOAM_MPI_LIBBIN
   
   case "$WM_MPLIB" in
   SYSTEMOPENMPI) #默认是这个，使用系统自带的openmpi，通过mpicc程序来获得库的目录
       export FOAM_MPI=openmpi-system
       # Undefine OPAL_PREFIX if set to one of the paths on foamOldDirs
       if [ -z "$($foamClean "$OPAL_PREFIX" "$foamOldDirs")" ]
       then
           unset OPAL_PREFIX
       fi
       # mpicc --showme:link会输出链接选项，-L/usr/lib/x86_64-linux-gnu/openmpi/lib -lmpi。
       libDir=`mpicc --showme:link | sed -e 's/.*-L\([^ ]*\).*/\1/'` #结果为/usr/lib/x86_64-linux-gnu/openmpi/lib
   
       # 去掉末尾的lib，结果为/usr/lib/x86_64-linux-gnu/openmpi
       export MPI_ARCH_PATH="${libDir%/*}"
   
       _foamAddLib     $libDir
       unset libDir
       ;;
   
   OPENMPI)
       export FOAM_MPI=openmpi-2.1.1
       # Optional configuration tweaks:
       _foamSource `$WM_PROJECT_DIR/bin/foamEtcFile config.sh/openmpi`
   
       export MPI_ARCH_PATH=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER/$FOAM_MPI
   
       # Tell OpenMPI where to find its install directory
       export OPAL_PREFIX=$MPI_ARCH_PATH
   
       _foamAddPath    $MPI_ARCH_PATH/bin
   
       # 64-bit on OpenSuSE 12.1 uses lib64 others use lib
       _foamAddLib     $MPI_ARCH_PATH/lib$WM_COMPILER_LIB_ARCH
       _foamAddLib     $MPI_ARCH_PATH/lib
   
       _foamAddMan     $MPI_ARCH_PATH/share/man
       ;;
   
   SYSTEMMPI)
       export FOAM_MPI=mpi-system
   
       if [ -z "$MPI_ROOT" ]
       then
           echo 1>&2
           echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
           echo "    Please set the environment variable MPI_ROOT to point to" \
                " the base folder for the system MPI in use." 1>&2
           echo "    Example:" 1>&2
           echo 1>&2
           echo "        export MPI_ROOT=/opt/mpi" 1>&2
           echo 1>&2
       else
           export MPI_ARCH_PATH=$MPI_ROOT
   
           if [ -z "$MPI_ARCH_FLAGS" ]
           then
               echo 1>&2
               echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
               echo "    MPI_ARCH_FLAGS is not set. Example:" 1>&2
               echo 1>&2
               echo "        export MPI_ARCH_FLAGS=\"-DOMPI_SKIP_MPICXX\"" 1>&2
               echo 1>&2
           fi
   
           if [ -z "$MPI_ARCH_INC" ]
           then
               echo 1>&2
               echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
               echo "    MPI_ARCH_INC is not set. Example:" 1>&2
               echo 1>&2
               echo "        export MPI_ARCH_INC=\"-isystem \$MPI_ROOT/include\"" 1>&2
               echo 1>&2
           fi
   
           if [ -z "$MPI_ARCH_LIBS" ]
           then
               echo 1>&2
               echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
               echo "    MPI_ARCH_LIBS is not set. Example:" 1>&2
               echo 1>&2
               echo "        export MPI_ARCH_LIBS=\"-L\$MPI_ROOT/lib -lmpi\"" 1>&2
               echo 1>&2
           fi
       fi
       ;;
   
   MPICH)
       export FOAM_MPI=mpich2-1.1.1p1
       export MPI_HOME=$WM_THIRD_PARTY_DIR/$FOAM_MPI
       export MPI_ARCH_PATH=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER/$FOAM_MPI
   
       _foamAddPath    $MPI_ARCH_PATH/bin
   
       # 64-bit on OpenSuSE 12.1 uses lib64 others use lib
       _foamAddLib     $MPI_ARCH_PATH/lib$WM_COMPILER_LIB_ARCH
       _foamAddLib     $MPI_ARCH_PATH/lib
   
       _foamAddMan     $MPI_ARCH_PATH/share/man
       ;;
   
   MPICH-GM)
       export FOAM_MPI=mpich-gm
       export MPI_ARCH_PATH=/opt/mpi
       export MPICH_PATH=$MPI_ARCH_PATH
       export GM_LIB_PATH=/opt/gm/lib64
   
       _foamAddPath    $MPI_ARCH_PATH/bin
   
       # 64-bit on OpenSuSE 12.1 uses lib64 others use lib
       _foamAddLib     $MPI_ARCH_PATH/lib$WM_COMPILER_LIB_ARCH
       _foamAddLib     $MPI_ARCH_PATH/lib
   
       _foamAddLib     $GM_LIB_PATH
       ;;
   
   MV2MPI)
       export FOAM_MPI=mvapich2
       libDir=`mpicc -show -cc= | sed -e 's/.*-L\([^ ]*\).*/\1/'`
       export MPI_ARCH_PATH="${libDir%/*}"
       _foamAddLib $libDir
       unset libDir
       ;;
   
   HPMPI)
       export FOAM_MPI=hpmpi
       export MPI_HOME=/opt/hpmpi
       export MPI_ARCH_PATH=$MPI_HOME
   
       _foamAddPath $MPI_ARCH_PATH/bin
   
       case `uname -m` in
       i686)
           _foamAddLib $MPI_ARCH_PATH/lib/linux_ia32
           ;;
   
       x86_64)
           _foamAddLib $MPI_ARCH_PATH/lib/linux_amd64
           ;;
       *)
           echo Unknown processor type `uname -m` 1>&2
           ;;
       esac
       ;;
   
   MPI)
       export FOAM_MPI=mpi
       export MPI_ARCH_PATH=/opt/mpi
       ;;
   
   FJMPI)
       export FOAM_MPI=fjmpi
       export MPI_ARCH_PATH=/opt/FJSVmpi2
   
       _foamAddPath    $MPI_ARCH_PATH/bin
       _foamAddLib     $MPI_ARCH_PATH/lib/sparcv9
       _foamAddLib     /opt/FSUNf90/lib/sparcv9
       _foamAddLib     /opt/FJSVpnidt/lib
       ;;
   
   QSMPI)
       export FOAM_MPI=qsmpi
       export MPI_ARCH_PATH=/usr/lib/mpi
   
       _foamAddPath    $MPI_ARCH_PATH/bin
       _foamAddLib     $MPI_ARCH_PATH/lib
       ;;
   
   SGIMPI)
       # No trailing slash
       [ "${MPI_ROOT%/}" = "${MPI_ROOT}" ] || MPI_ROOT="${MPI_ROOT%/}"
   
       export FOAM_MPI="${MPI_ROOT##*/}"
       export MPI_ARCH_PATH=$MPI_ROOT
   
       if [ ! -d "$MPI_ROOT" -o -z "$MPI_ARCH_PATH" ]
       then
           echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
           echo "    MPI_ROOT not a valid mpt installation directory or ending" \
                " in a '/'." 1>&2
           echo "    Please set MPI_ROOT to the mpt installation directory." 1>&2
           echo "    MPI_ROOT currently set to '$MPI_ROOT'" 1>&2
       fi
   
       if [ "$FOAM_VERBOSE" -a "$PS1" ]
       then
           echo "Using SGI MPT:" 1>&2
           echo "    MPI_ROOT : $MPI_ROOT" 1>&2
           echo "    FOAM_MPI : $FOAM_MPI" 1>&2
       fi
   
       _foamAddPath    $MPI_ARCH_PATH/bin
       _foamAddLib     $MPI_ARCH_PATH/lib
       ;;
   
   INTELMPI)
       # No trailing slash
       [ "${MPI_ROOT%/}" = "${MPI_ROOT}" ] || MPI_ROOT="${MPI_ROOT%/}"
   
       export FOAM_MPI="${MPI_ROOT##*/}"
       export MPI_ARCH_PATH=$MPI_ROOT
   
       if [ ! -d "$MPI_ROOT" -o -z "$MPI_ARCH_PATH" ]
       then
           echo "Warning in $WM_PROJECT_DIR/etc/config.sh/settings:" 1>&2
           echo "    MPI_ROOT not a valid mpt installation directory or ending" \
                " in a '/'." 1>&2
           echo "    Please set MPI_ROOT to the mpt installation directory." 1>&2
           echo "    MPI_ROOT currently set to '$MPI_ROOT'" 1>&2
       fi
   
       if [ "$FOAM_VERBOSE" -a "$PS1" ]
       then
           echo "Using INTEL MPI:" 1>&2
           echo "    MPI_ROOT : $MPI_ROOT" 1>&2
           echo "    FOAM_MPI : $FOAM_MPI" 1>&2
       fi
   
       _foamAddPath    $MPI_ARCH_PATH/bin64
       _foamAddLib     $MPI_ARCH_PATH/lib/release
       ;;
   *)
       export FOAM_MPI=dummy
       ;;
   esac
   
   # 增加(non-dummy)MPI实现
   # Dummy MPI already added to LD_LIBRARY_PATH and has no external libraries
   if [ "$FOAM_MPI" != dummy ]
   then
       _foamAddLib $FOAM_LIBBIN/$FOAM_MPI:$FOAM_EXT_LIBBIN/$FOAM_MPI #第一个为/home/zj/OpenFOAM/ThirdParty-11/platforms/linux64GccDPInt32/lib/openmpi-system
   fi
   
   # 设置最小的MPI缓冲大小 (各平台通用，除了SGI MPI)
   : ${minBufferSize:=20000000}
   #如果MPI_BUFFER_SIZE比20000000小，则修正为20000000。也就是19M左右
   if [ "${MPI_BUFFER_SIZE:=$minBufferSize}" -lt $minBufferSize ]
   then
       MPI_BUFFER_SIZE=$minBufferSize
   fi
   export MPI_BUFFER_SIZE
   
   # Cleanup environment:
   unset minBufferSize
   ```


## config.sh/paraview

1. config.sh/paraview：

   ```shell
   #     paraview-[4-5].x的配置文件
   #     对于构建插件，需要环境变量ParaView_DIR和ParaView_MAJOR
   # 清理PATH
   cleaned=$($WM_PROJECT_DIR/bin/foamCleanPath "$PATH" \
           "$ParaView_DIR \
            $WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER/cmake- \
            $WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER/paraview-" \
           ) \
           && PATH="$cleaned"
   
   # 确定要使用的cmake
   unset CMAKE_HOME CMAKE_ROOT
   for cmake in $WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER/cmake-* #并不存在该目录
   do
       if [ -d $cmake ]
       then
           if [ -z $CMAKE_HOME ] || \
               $WM_PROJECT_DIR/bin/tools/foamVersionCompare $CMAKE_HOME lt $cmake
           then
               export CMAKE_HOME=$cmake
               export CMAKE_ROOT=$cmake
           fi
       fi
   done
   if [ -n $CMAKE_HOME ]
   then
       export PATH=$cmake/bin:$PATH
   fi
   
   #- ParaView 版本, 自动确定大版本号
   #export ParaView_VERSION=5.6.3
   export ParaView_VERSION=5.10.1
   export ParaView_MAJOR=detect
   
   #export ParaView_GL=system
   export ParaView_GL=mesa #使用软件实现的OpenGL
   
   # 定义函数，来处理命令行参数
   _foamParaviewEval()
   {
       while [ $# -gt 0 ]
       do
           case "$1" in
           ParaView*=*)
               # 形如：name=value
               eval "export $1"
               ;;
           esac
           shift
       done
   }
   
   # 来处理命令行参数
   _foamParaviewEval $@
   
   # 根据版本号设置对应的大版本号，例如从5.10.1中提取出5.10
   # ParaView_MAJOR is "<digits>.<digits>" from ParaView_VERSION
   case "$ParaView_VERSION" in
   "$ParaView_MAJOR".* )
       # Version and major appear to correspond
       ;;
   
   [0-9]*)
       # Extract major from the version
       ParaView_MAJOR=$(echo $ParaView_VERSION | \
                      sed -e 's/^\([0-9][0-9]*\.[0-9][0-9]*\).*$/\1/')
       ;;
   esac
   export ParaView_VERSION ParaView_MAJOR
   
   # Set the binary and source directories
   # 设置二进制和源码目录，如果要自己编译ParaView的话。
   export ParaView_DIR=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER/ParaView-$ParaView_VERSION
   paraviewSrcDir=$WM_THIRD_PARTY_DIR/ParaView-$ParaView_VERSION
   
   # 如果二进制和源码目录存在的话，将他们添加到对应的路径中
   if [ -d $ParaView_DIR -o -d $paraviewSrcDir ]
   then
       export ParaView_INCLUDE_DIR=$ParaView_DIR/include/paraview-$ParaView_MAJOR
   
       paraviewArch=
       if [ -d $ParaView_DIR/lib64 ]
       then
           paraviewArch=64
       fi
       paraviewLibSubDir=
       if $WM_PROJECT_DIR/bin/tools/foamVersionCompare $ParaView_VERSION lt 5.5.0
       then
           paraviewLibSubDir=/paraview-$ParaView_MAJOR
       fi
       export ParaView_LIB_DIR=$ParaView_DIR/lib$paraviewArch$paraviewLibSubDir
   
       export PATH=$ParaView_DIR/bin:$PATH
       export LD_LIBRARY_PATH=$ParaView_LIB_DIR:$LD_LIBRARY_PATH
       export PV_PLUGIN_PATH=$FOAM_LIBBIN/paraview-$ParaView_MAJOR
   
       if [ "$FOAM_VERBOSE" -a "$PS1" ]
       then
           echo "Using paraview"
           echo "    ParaView_DIR         : $ParaView_DIR"
           echo "    ParaView_LIB_DIR     : $ParaView_LIB_DIR"
           echo "    ParaView_INCLUDE_DIR : $ParaView_INCLUDE_DIR"
           echo "    PV_PLUGIN_PATH       : $PV_PLUGIN_PATH"
       fi
   
       # Add in python libraries if required
       paraviewPython=$ParaView_DIR/Utilities/VTKPythonWrapping
       if [ -r $paraviewPython ]
       then
           if [ "$PYTHONPATH" ]
           then
               export PYTHONPATH=$PYTHONPATH:$paraviewPython:$ParaView_LIB_DIR
           else
               export PYTHONPATH=$paraviewPython:$ParaView_LIB_DIR
           fi
       fi
   
       # Alias paraview to launch with mesa if necessary
       if [ "$ParaView_GL" = mesa ]
       then
           alias paraview='LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ParaView_LIB_DIR/mesa paraview'
       fi
   else
       unset PV_PLUGIN_PATH
   fi
   
   unset _foamParaviewEval
   unset cleaned cmake paraviewInstDir paraviewPython
   ```


## config.sh/ensight

1. config.sh/ensight：

   ```shell
   # Fallback value
   if [ ! -d "$CEI_HOME" ]
   then
       export CEI_HOME=/usr/local/ensight/CEI
   fi
   
   if [ -r $CEI_HOME ]
   then
   
       # Special treatment for 32bit OpenFOAM and 64bit Ensight
       if [ "$WM_ARCH" = linux -a `uname -m` = x86_64 ]
       then
           export CEI_ARCH=linux_2.6_32
       fi
   
       # Add to path if required
       if [ "$CEI_HOME/bin/ensight" != "`which ensight 2>/dev/null`" ]
       then
           export PATH=$CEI_HOME/bin:$PATH
       fi
   
       export ENSIGHT9_INPUT=dummy
       export ENSIGHT9_READER=$FOAM_LIBBIN
   else
       unset CEI_HOME
   fi
   ```


## config.sh/gperftools

1. config.sh/gperftools：

   ```shell
   version=svn
   gperftools_install=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER
   
   GPERFTOOLS_VERSION=gperftools-$version
   GPERFTOOLS_ARCH_PATH=$gperftools_install/$GPERFTOOLS_VERSION
   
   export PATH=$GPERFTOOLS_ARCH_PATH/bin:$PATH
   export LD_LIBRARY_PATH=$GPERFTOOLS_ARCH_PATH/lib:$LD_LIBRARY_PATH
   ```


# wmake配置文件

## Allwmake

1. 执行根目录下的Allwmake，来构建整个项目：

   ```shell
   #!/bin/sh
   cd ${0%/*} || exit 1    # 将工作目录切换到当前脚本所在的目录，%/*表示从右侧删除/*的部分，即获取目录部分。
   
   # 解析库编译的参数
   . wmake/scripts/AllwmakeParseArguments
   
   # 进行各种检查，检查当前工作目录是否是对应的参数
   wmakeCheckPwd "$WM_PROJECT_DIR" || {
       echo "Allwmake error: Current directory is not \$WM_PROJECT_DIR"
       echo "    The environment variables are inconsistent with the installation."
       echo "    Check the OpenFOAM entries in your dot-files and source them."
       exit 1
   }
   
   [ -n "$FOAM_EXT_LIBBIN" ] || {
       echo "Allwmake error: FOAM_EXT_LIBBIN not set"
       echo "    Check the OpenFOAM entries in your dot-files and source them."
       exit 1
   }
   
   # 编译wmake所需的程序，共2个
   # dirToString，从标准输入读入，将a/b/c/dd变为abcdd输出。
   # wmkdep，扫描文件，寻找-Idir，生成依赖文件列表，类似于cpp -M的行为，但是由于使用了hashtable，速度更快，且输出不重复。
   (cd wmake/src && make)
   
   # 编译第三方库
   if [ -d "$WM_THIRD_PARTY_DIR" ]
   then
       $WM_THIRD_PARTY_DIR/Allwmake
   else
       echo "Allwmake: no ThirdParty directory found - skipping"
   fi
   
   # 执行src目录下的Allwmake，默认情况下targetType为空。$*为-fromWmake
   src/Allwmake $targetType $*
   
   # 执行applications目录下的Allwmake
   applications/Allwmake $targetType $*
   ```


## wmake/scripts/AllwmakeParseArguments

1. wmake/scripts/AllwmakeParseArguments：

   ```shell
   # 使用source来执行本脚本，这样原脚本的所有参数在这里仍然可用
   
   Script=${0##*/} #获取执行该脚本的脚本的文件名，就是Allwmake
   
   if [ -z "$WM_PROJECT_DIR" ]
   then
       echo "$Script error: The OpenFOAM environment is not set."
       echo "    Check the OpenFOAM entries in your dot-files and source them."
       echo "    If in doubt, please read:"
       echo "       http://openfoam.org/download/source/setting-environment"
       exit 1
   fi
   
   usage() {
       exec 1>&2
       while [ "$#" -ge 1 ]; do echo "$1"; shift; done
   
       # Print normal usage options
       cat<<USAGE
   
   Usage: $Script [OPTIONS]
   
   Executing $Script is equivalent to
   
      wmake -all [OPTIONS]
   USAGE
   
       wmake -help
       exit 1
   }
   
   # 解析参数和选项
   fromWmake=
   qOpt=
   #默认情况下$@为-fromWmake
   for arg in "$@"
   do
       # Remove arg
       shift
       case "$arg" in
           -h | -help)
               usage
               exit 0
               ;;
           # Check if called from wmake to avoid recursion
           # 检查是否从wmake中调用，避免出现递归。
           -fromWmake)
               fromWmake="fromWmake"
               ;;
           -q)
               qOpt="-q"
               # 永久去除参数
               continue
               ;;
           # 构建目标的类型
           lib | libo | libso | dep | objects)
               targetType=$arg
               ;;
       esac
   
       # 重新插入参数
       set -- "$@" "$arg"
   done
   # 执行 wmake -all 如果不是从wmake调用的话。
   if [ -z "$fromWmake" ]
   then
       exec wmake -all $qOpt $*
   else
       # Print command
       [ -z "$targetType" ] || targetSpace=" "
       echo "$Script $targetType$targetSpace$(echo $PWD | sed s%$WM_PROJECT_DIR/%% )"  #会输出Allwmake src或Allwmake src/Pstream等。sed会将路径的开头部分删除掉。
   fi
   
   # 如果 WM_CONTINUE_ON_ERROR 没有设置，则激活shell选项 "stop on error"
   if [ -z "${WM_CONTINUE_ON_ERROR}" ]
   then
       set -e
   fi
   
   # 清除本地变量和函数
   unset Script usage fromWmake
   ```


## src/Allwmake

1. src/Allwmake：

   ```shell
   #!/bin/sh
   cd ${0%/*} || exit 1
   
   # 解析库编译时的参数
   . ../wmake/scripts/AllwmakeParseArguments
   
   # 进行各种各样的检查
   wmakeCheckPwd "$WM_PROJECT_DIR/src" || {
       echo "Allwmake error: Current directory is not \$WM_PROJECT_DIR/src"
       echo "    The environment variables are inconsistent with the installation."
       echo "    Check the OpenFOAM entries in your dot-files and source them."
       exit 1
   }
   
   [ -n "$FOAM_EXT_LIBBIN" ] || {
       echo "Allwmake error: FOAM_EXT_LIBBIN not set"
       echo "    Check the OpenFOAM entries in your dot-files and source them."
       exit 1
   }
   
   # 如果需要的话，更新OpenFOAM version字符串
   # 如果没有git信息，则第一部分输出no git description found，返回0，在shell中返回0表示成功，所以不会执行第二部分。
   # wrmo 是用来删除指定的.o文件。
   wmakePrintBuild -check || wrmo OpenFOAM/global/global.o 2>/dev/null
   
   Pstream/Allwmake $targetType $*
   
   OSspecific/${WM_OSTYPE:-POSIX}/Allwmake $targetType $*
   wmake $targetType OpenFOAM #OpenFOAM是目录名称
   
   wmake $targetType fileFormats
   wmake $targetType surfMesh
   wmake $targetType triSurface
   wmake $targetType genericPatches
   wmake $targetType meshTools
   
   # Decomposition methods needed by dummyThirdParty
   # (dummy metisDecomp, scotchDecomp etc) needed by e.g. meshTools
   dummyThirdParty/Allwmake $targetType $*
   
   wmake $targetType finiteVolume
   wmake $targetType lagrangian/basic
   wmake $targetType genericPatchFields
   
   wmake $targetType mesh/extrudeModel
   wmake $targetType dynamicMesh
   
   # Compile scotchDecomp, metisDecomp etc.
   parallel/Allwmake $targetType $*
   
   wmake $targetType conversion
   wmake $targetType sampling
   
   wmake $targetType fvMeshStitchers
   wmake $targetType fvMeshMovers
   fvMeshTopoChangers/Allwmake $targetType $*
   wmake $targetType fvMeshDistributors
   
   wmake $targetType ODE
   wmake $targetType randomProcesses
   
   wmake $targetType physicalProperties
   
   thermophysicalModels/Allwmake $targetType $*
   twoPhaseModels/Allwmake $targetType $*
   multiphaseModels/Allwmake $targetType $*
   MomentumTransportModels/Allwmake $targetType $*
   ThermophysicalTransportModels/Allwmake $targetType $*
   wmake $targetType radiationModels
   wmake $targetType combustionModels
   mesh/Allwmake $targetType $*
   renumber/Allwmake $targetType $*
   fvAgglomerationMethods/Allwmake $targetType $*
   wmake $targetType fvMotionSolver
   
   wmake $targetType fvModels
   wmake $targetType fvConstraints
   functionObjects/Allwmake $targetType $*
   
   lagrangian/Allwmake $targetType $*
   
   wmake $targetType sixDoFRigidBodyMotion
   wmake $targetType sixDoFRigidBodyState
   wmake $targetType rigidBodyDynamics
   wmake $targetType rigidBodyMeshMotion
   wmake $targetType rigidBodyState
   wmake $targetType specieTransfer
   wmake $targetType atmosphericModels
   wmake $targetType waves
   ```

## wmake/wmake

1. wmake/wmake：

   ```shell
   #!/bin/bash
   #------------------------------------------------------------------------------
   # =========                 |
   # \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   #  \\    /   O peration     | Website:  https://openfoam.org
   #   \\  /    A nd           | Copyright (C) 2011-2020 OpenFOAM Foundation
   #    \\/     M anipulation  |
   #------------------------------------------------------------------------------
   # License
   #     This file is part of OpenFOAM.
   #
   #     OpenFOAM is free software: you can redistribute it and/or modify it
   #     under the terms of the GNU General Public License as published by
   #     the Free Software Foundation, either version 3 of the License, or
   #     (at your option) any later version.
   #
   #     OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
   #     ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
   #     FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
   #     for more details.
   #
   #     You should have received a copy of the GNU General Public License
   #     along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.
   #
   # Script
   #     wmake
   #
   # Description
   #     General, easy to use make system for multi-platform development
   #     with support for local and network parallel compilation.
   #
   #     This updated wmake supports out-of-tree object and dependency files to
   #     avoid the clutter which accumulates in the source-tree with the original
   #     wmake system.  Now when building the OpenFOAM package both the object and
   #     dependency files are now located in a tree with the same structure as the
   #     source tree but in the platforms/$WM_OPTIONS sub-directory of
   #     $WM_PROJECT_DIR.
   #
   #     When building user libraries and applications which are not located in the
   #     OpenFOAM source-tree the object and dependency files are located in a tree
   #     with the same structure as the source tree but in the Make/$WM_OPTIONS
   #     sub-directory.
   #
   #     The disadvantage of the out-of-tree compilation is that the dependency
   #     files are harder to find but are sometimes useful to study which header
   #     files are included.  For those who need access to the dependency files the new wdep script is provided to locate them.  See the wdep script header or   run:
   #         wdep -h
   # 
   # See also
   #     wmakeLnInclude, wmakeLnIncludeAll, wmakeCollect, wdep, wrmdep, wrmo,
   #     wclean, wcleanPlatform, wcleanLnIncludeAll
   Script=${0##*/}
   
   # 执行wmakeFunctions脚本，其中定义了几个函数
   # shellcheck是一个静态的脚本分析工具，可以在执行前分析一下，提前发现错误。
   # shellcheck source=scripts/wmakeFunctions 
   . "${0%/*}/scripts/wmakeFunctions"
   
   error() {
       exec 1>&2
       while [ "$#" -ge 1 ]; do echo "$1"; shift; done
       usage
       exit 1
   }
   
   usage() {
       cat<<USAGE
   
   Usage: $Script [OPTION] [dir]
          $Script [OPTION] target [dir [MakeDir]]
   
   options:
     -silent   | -s    Quiet mode (does not echo commands)
     -all      | -a    wmake all sub-directories, running Allwmake if present
     -queue    | -q    wmakeCollect all sub-directories, running Allwmake if present
     -non-stop | -k    Compile without stopping when errors occur
     -j                Compile using all local cores/hyperthreads
     -j <N>    | -j<N> Compile using N cores/hyperthreads
     -no-scheduler     Compile without wmakeScheduler
     -update           Update lnInclude directories, dep files, remove deprecated
                       files and directories
     -help     | -h    Print the usage
   
   
   A general, easy-to-use make system for multi-platform development
   with support for local and network parallel compilation.
   
   The 'target' is a Makefile target: #可以是一个具体的.o文件
     e.g., platforms/linux64GccDPOpt/.../fvMesh.o
   
   or a special target: #也可以是一个通用的target
     all               wmake all sub-directories, running Allwmake if present
     queue             wmakeCollect all sub-directories, running Allwmake if present
     exe               Compile statically linked executable #静态链接的可执行文件
     lib               Compile statically linked archive lib (.a) #静态库
     libo              Compile statically linked lib (.o) #目标文件
     libso             Compile dynamically linked lib (.so) #动态库
     dep               Compile lnInclude and dependencies only
     objects           Compile but not link #编译但不链接
   
   USAGE
   }
   
   # 默认的make是PATH中找到的make
   make="make"
   
   # 设置 WM_NCOMPPROCS 为本地计算机的核心数
   useAllCores()
   {
       if [ -r /proc/cpuinfo ] #查询/proc/cpuinfo文件
       then
           WM_NCOMPPROCS=$(grep -Ec "^processor" /proc/cpuinfo)
       else
           WM_NCOMPPROCS=1
       fi
   
       export WM_NCOMPPROCS
   }
   
   # 解析选项和参数
   # 默认只编译本地目标
   all=
   update=
   
   while [ "$#" -gt 0 ]
   do
       case "$1" in
           # Print help
           -h | -help)
               usage && exit 0
               ;;
           -s | -silent)
               export WM_QUIET=1
               ;;
           -a | -all | all)
               all="all"
               ;;
           -q | -queue | queue)
               all="queue"
               ;;
           # 在本地机器上使用所有核心并行编译
           -j)
               useAllCores
               [ $# -ge 2 ] && [ "$2" -gt 0 ] > /dev/null 2>&1 \
                   && shift && export WM_NCOMPPROCS=$1
               echo "Compiling enabled on $WM_NCOMPPROCS cores"
               ;;
           # 在特定数量的核心上并行编译
           -j*)
               export WM_NCOMPPROCS=${1#-j} #获取-j后面的数字
               echo "Compiling enabled on $WM_NCOMPPROCS cores"
               ;;
           # 遇到错误不停止编译
           -k | -non-stop)
               export WM_CONTINUE_ON_ERROR=1
               ;;
           # 关闭并行编译调度功能
           -no-scheduler)
               unset WM_SCHEDULER
               ;;
           # Meant to be used following a pull, this will: 一般在从源代码仓库pull之后使用，
           # - remove dep files that depend on deleted files;
           # - remove stale dep files;
           # - update lnInclude directories;
           # - remove empty directories, along with deprecated object directories
           #   and respective binaries.
           -update)
               update="true"
               [ -z "$all" ] && all="all"
               ;;
           --)
               shift
               break
               ;;
           -*)
               error "unknown option: '$*'"
               ;;
           *)
               break
               ;;
       esac
       shift
   done
   
   # Check environment variables
   
   checkEnv
   
   # 除了静态构建一个单独的exe文件之外，都要设置WM_PROJECT 和 WM_PROJECT_DIR
   [ "$1" = exe ] || { [ "$WM_PROJECT" ] && [ "$WM_PROJECT_DIR" ]; } || {
       echo "$Script error:" 1>&2
       echo "    environment variable \$WM_PROJECT or " \
            "\$WM_PROJECT_DIR not set" 1>&2
       echo "    while building project library" 1>&2
       exit 1
   }
   
   # 设置并行编译
   # Set WM_NCOMPPROCS automatically when both WM_HOSTS and WM_SCHEDULER are set
   if [ -z "$WM_NCOMPPROCS" ] && [ -n "$WM_HOSTS" ] && [ -n "$WM_SCHEDULER" ]
   then
       WM_NCOMPPROCS=$(wmakeScheduler -count) || unset WM_NCOMPPROCS
   fi
   
   if [ -n "$WM_NCOMPPROCS" ]
   then
       parOpt="-j $WM_NCOMPPROCS"
   
       if [ "$WM_NCOMPPROCS" -gt 1 ] && [ -z "$MAKEFLAGS" ]
       then
           lockDir=$HOME/.$WM_PROJECT/.wmake
   
           if [ -d "$lockDir" ]
           then
               rm -f "$lockDir/*"
           else
               mkdir -p "$lockDir"
           fi
   
           make="$make --no-print-directory $parOpt"
       fi
   fi
   
   # 检查参数，切换目录，来运行wmake
   unset dir targetType
   MakeDir=Make
   
   if [ $# -ge 1 ]
   then
       if [ -d "$1" ]
       then
           dir=$1
       else
           targetType=$1
       fi
   
       # 指定目录名称:
       [ $# -ge 2 ] && dir=$2
   
       # Specified alternative name for the Make sub-directory:
       [ $# -ge 3 ] && MakeDir=$3
   
       if [ "$dir" ]
       then
           cd "$dir" 2>/dev/null || {
               echo "$Script error: could not change to directory '$dir'" 1>&2
               exit 1
           }
       fi
   
       # 显示命令
       [ -z "$targetType" ] || targetSpace=" "
       echo "$Script $targetType$targetSpace${dir:-.}"
   fi
   
   # Recurse the source tree to compile "all" targets
   
   if [ -n "$update" ]
   then
       wrmdep -update
       wrmdep -old
       wmakeLnIncludeAll -update "$parOpt"
       wclean empty
       export WM_UPDATE_DEPENDENCIES=yes
   elif  [ -z "$all" ]
   then
       wmakeLnIncludeAll -dep "$parOpt"
   fi
   
   
   # Recurse the source tree to compile "all" targets
   
   if [ "$all" = "all" ]
   then
       if [ -e Allwmake ]
       then
           ./Allwmake -fromWmake "$targetType"
           exit $?
       else
           # Have to keep track of the main exit code for the call to "make"
           makeExitCode=0
   
           # Find all the sub-directories containing a 'Make' directory
           FOAM_APPS=$(\
                          for d in *; \
                          do [ -d "$d" ] && [ "$d" != Optional ] && [ "$d" != Make ] \
                             && echo "$d"; \
                          done | xargs \
                    )
           if [ ! "$FOAM_APPS" = "" ]
           then
               # Compile all applications in sub-directories
               $make ${WM_CONTINUE_ON_ERROR:+-k} \
                     -f "$WM_DIR/makefiles/apps" \
                     TARGET="$targetType" FOAM_APPS="$FOAM_APPS"
               makeExitCode=$?
           fi
           # If the current directory contains a 'Make' directory continue
           # otherwise exit, or always exit in case of error
           if [ ! -d "$MakeDir" ] || [ "$makeExitCode" -ne 0 ]
           then
               exit $makeExitCode
           fi
   
           # Clean up tracking variable
           unset makeExitCode
       fi
   fi
   
   # Recurse the source tree to compile "all" targets using wmakeCollect
   
   if [ "$all" = "queue" ]
   then
       [ -n "$update" ] || wmakeLnIncludeAll "$parOpt"
   
       (
           export WM_COLLECT_DIR=$WM_PROJECT_DIR/platforms/${WM_OPTIONS}/${PWD////_}
           export WM_SCHEDULER=wmakeCollect
           trap '$WM_SCHEDULER -kill' TERM INT
           $WM_SCHEDULER -clean                                                   \
        && wmake -all objects                                                     \
        && $WM_SCHEDULER
       ) && wmake -all
       exit $?
   fi
   
   # Search up the directory tree for the Make sub-directory,
   # check the existence of the 'files' file and build there if present
   
   cdSource
   
   # Transform options
   
   # Transform no option to "libso" if that looks appropriate or remove it
   # so that the call to make builds the application
   if [ "$targetType" = "" ]
   then
       unset targetType
       if grep -q -e '^ *LIB *=' "$MakeDir/files"
       then
           targetType=libso
       fi
   elif grep -q -e '^ *EXE *=' "$MakeDir/files"
   then
       # Application. Remove any nonsense targetType
       case "$targetType" in
         lib*)
           unset targetType
           ;;
       esac
   fi
   
   # Created the objectsDir directory
   
   objectsDir=$MakeDir/$WM_OPTIONS
   expandPath "$PWD"
   if [[ "$exPath" = *"$WM_PROJECT_DIR"* ]]
   then
       platformPath=$WM_PROJECT_DIR/platforms/${WM_OPTIONS}
       objectsDir=$platformPath${exPath//$WM_PROJECT_DIR/}
   fi
   
   mkdir -p "$objectsDir"
   
   # Create $objectsDir/files from $MakeDir/files if necessary
   # Spawn a sub-shell and unset MAKEFLAGS in that sub-shell to avoid
   # $objectsDir/files being built in parallel
   
   if ! grep -q "SOURCE" "$MakeDir/files"; then
       (
           unset MAKEFLAGS
   
           $make -s -f "$WM_DIR/makefiles/files" MAKE_DIR="$MakeDir" \
                 OBJECTS_DIR="$objectsDir"
       )
   
       # Check the $objectsDir/files file was created successfully
       [ -r "$objectsDir/files" ] || {
           echo "$Script error: file '$objectsDir/files'" \
                "could not be created in $PWD" 1>&2
           exit 1
       }
   fi
   
   
   # Make the dependency files
   
   # For libraries create lnInclude ...
   case "$targetType" in
       lib | libo | libso | dep )
           # ... but only if 'LIB' is declared in 'Make/files'
           if grep -q -e '^ *LIB *=' "$MakeDir/files"
           then
               $make -s -f "$WM_DIR/makefiles/general" MAKE_DIR="$MakeDir" \
                     OBJECTS_DIR="$objectsDir" lnInclude
           fi
           ;;
   esac
   
   
   # When WM_UPDATE_DEPENDENCIES is set, use forced dependency files update
   
   if [ -n "$WM_UPDATE_DEPENDENCIES" ]
   then
   
       $make -f "$WM_DIR"/makefiles/general MAKE_DIR="$MakeDir" \
           OBJECTS_DIR="$objectsDir" dep
       makeExitCode=$?
   
       if [ $makeExitCode -ne 0 ]
       then
           exit $makeExitCode
       fi
   
       unset makeExitCode
   fi
   
   # Make the dependency files or object files and link
   
   # shellcheck disable=SC2093,SC2086
   exec $make -f "$WM_DIR/makefiles/general" MAKE_DIR="$MakeDir" \
        OBJECTS_DIR="$objectsDir" $targetType
   
   # Cleanup local variables and functions
   
   unset Script usage error useAllCores update expandPath findTarget
   ```

2. wdep工具：

   ```shell
   zj@zj-hit:~$ wdep argList.C #会输出该文件对应的.dep文件的路径。不要求参数在当前目录下，它会自动搜索。
   /home/zj/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/src/OpenFOAM/global/argList/argList.C.dep
   ```

3. 新版的wmake会在s'rc同级的目录中创建一个paltform目录，将所有的输出文件都放在这里。

4. wmakeFilesAndOptions程序会读取当前目录下的所有文件夹和文件，然后在同级的Make文件夹中生成files和options文件。不过如果已经存在这两个文件，则不会修改已有的文件。

5. OpenFOAM发布的源码中，是包含Make/files和Make/options的文件，但是不包含lnInclude目录。

# 编译结果

1. 编译前后目录结构的变化：

   ```shell
   #编译前，在src路径下,fileFormats模块
   zj@zj-hit:~/OpenFOAM/OpenFOAM-11/src/fileFormats$ tree
   .
   ├── lnInclude #将当前模块中所有的文件都通过符号链接包含到这里
   │   ├── NASCore.C -> ../nas/NASCore.C
   │   ├── NASCore.H -> ../nas/NASCore.H
   │   ├── OBJstream.C -> ../obj/OBJstream.C
   │   ├── OBJstream.H -> ../obj/OBJstream.H
   │   ├── STARCDCore.C -> ../starcd/STARCDCore.C
   │   ├── STARCDCore.H -> ../starcd/STARCDCore.H
   │   ├── vtkUnstructuredReader.C -> ../vtk/vtkUnstructuredReader.C
   │   ├── vtkUnstructuredReader.H -> ../vtk/vtkUnstructuredReader.H
   │   ├── vtkUnstructuredReaderTemplates.C -> ../vtk/vtkUnstructuredReaderTemplates.C
   │   ├── vtkWriteOps.C -> ../vtk/vtkWriteOps.C
   │   ├── vtkWriteOps.H -> ../vtk/vtkWriteOps.H
   │   ├── vtkWriteOpsTemplates.C -> ../vtk/vtkWriteOpsTemplates.C
   │   ├── vtkWritePolyData.H -> ../vtk/vtkWritePolyData.H
   │   └── vtkWritePolyDataTemplates.C -> ../vtk/vtkWritePolyDataTemplates.C
   ├── Make
   │   ├── files #
   │   └── options
   ├── nas
   │   ├── NASCore.C
   │   └── NASCore.H
   ├── obj
   │   ├── OBJstream.C
   │   └── OBJstream.H
   ├── starcd
   │   ├── STARCDCore.C
   │   └── STARCDCore.H
   └── vtk
       ├── vtkUnstructuredReader.C
       ├── vtkUnstructuredReader.H
       ├── vtkUnstructuredReaderTemplates.C
       ├── vtkWriteOps.C
       ├── vtkWriteOps.H
       ├── vtkWriteOpsTemplates.C
       ├── vtkWritePolyData.H
       └── vtkWritePolyDataTemplates.C
   
   6 directories, 30 files
   #编译后，在platforms路径下
   zj@zj-hit:~/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/src/fileFormats$ tree
   .
   ├── files
   ├── nas
   │   ├── NASCore.C.dep #抛弃.H文件，将.C编译成.O文件，同时生成一个.C.dep的供make使用的依赖文件。
   │   └── NASCore.o
   ├── obj
   │   ├── OBJstream.C.dep
   │   └── OBJstream.o
   ├── starcd
   │   ├── STARCDCore.C.dep
   │   └── STARCDCore.o
   └── vtk
       ├── vtkUnstructuredReader.C.dep
       ├── vtkUnstructuredReader.o
       ├── vtkWriteOps.C.dep
       └── vtkWriteOps.o
   
   4 directories, 11 files
   ```

2. Make文件夹中的内容：

   1. file文件，第一部分负责记录本模块中需要编译的源文件，也是源文件依赖。LIB变量记录要生成的共享库的路径，这里是。省略了.so

      ```sh
      #可以看到虽然vtk文件夹下有5个.C文件，由于这里只包含了2个文件，因此编译后platforms中的vtk目录下，也只有2个文件名的.C.dep和.o文件。
      vtk/vtkWriteOps.C
      vtk/vtkUnstructuredReader.C
      nas/NASCore.C
      starcd/STARCDCore.C
      obj/OBJstream.C
      
      LIB = $(FOAM_LIBBIN)/libfileFormats
      #~/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/lib/libfileFormats.so
      ```

   2. option文件

      ```shell
      #头文件寻找路径，因为src目录下的.C文件中，包含头文件时都是使用" "，也就是去本地目录下寻找，而这个目录就在gcc -I参数指定的路径中。
      EXE_INC = \
          -I$(LIB_SRC)/fileFormats/lnInclude \
          -I$(LIB_SRC)/finiteVolume/lnInclude \
          -I$(LIB_SRC)/dynamicMesh/lnInclude \
          -I$(LIB_SRC)/meshTools/lnInclude
      #链接时需要的库的名称
      LIB_LIBS = \
          -lfileFormats \
          -lfiniteVolume \
          -ldynamicMesh \
          -lmeshTools
      ```

3. src目录中的文件编译后，只会在platforms目录下的lib目录中生成.so库文件。而用户具体执行的求解器和工具程序则是由bin目录下的。

4. 用户执行bin目录下的以Foam结尾的脚本时，会提示这个文件已经被替换了，需要使用foamRun -solver来替代。而foamRun程序是通过编译applications中的源码来连接起来各种共享库得到的。例如：

   ```shell
   #~/OpenFOAM/OpenFOAM-11/applications/solvers/foamRun/Make/files目录的内容
   setDeltaT.C
   foamRun.C
   
   EXE = $(FOAM_APPBIN)/foamRun #这表示要生成一个可执行文件
   ```

5. 有一些程序是以脚本的形式存在的，存放在源码目录`/home/zj/OpenFOAM/OpenFOAM-11/bin`中，不用编译就可以使用。

6. `/home/zj/OpenFOAM/OpenFOAM-11/applications/modules`中的源文件编译后连接后，也会产生共享库。

7. platforms目录下的applications目录中存放的内容都是.C.H和.O文件，类似于src目录。

8. applications目录下的这几个目录的作用：

   ```shell
   legacy    #生成可执行文件，存放在platforms下的bin目录     $(FOAM_APPBIN)
   modules   #生成库文件，存放在platforms下的lib目录         $(FOAM_LIBBIN)
   solvers   #生成可执行文件，存放在用户自己的platforms下的bin目录  $(FOAM_APPBIN)
   test      #生成可执行文件，存放在platforms下的bin目录     $(FOAM_USER_APPBIN)
   utilities #生成可执行文件，存放在platforms下的bin目录     $(FOAM_APPBIN)
   ```

9. src目录下的所有目录或子目录最终都会生成一个对应的共享库。

10. 共享库一共有143个，可执行文件一共有157个。


# 教程

1. 每一个教程目录下都有一个Allrun脚本：

   ```shell
   #!/bin/sh
   cd ${0%/*} || exit 1    #首先将当前目录切换到此脚本所在的目录
   
   # 执行教程所需的函数
   . $WM_PROJECT_DIR/bin/tools/RunFunctions
   
   application="$(getApplication)"
   
   runApplication blockMesh -dict $FOAM_TUTORIALS/resources/blockMesh/pitzDaily
   runApplication $application
   ```

2. RunFunctions：

   ```shell
   isTest(){
       for i in "$@"; do
           if [ "$i" = "-test" ]
           then
               return 0
           fi
       done
       return 1
   }
   
   getNumberOfProcessors(){
       foamDictionary -entry numberOfSubdomains -value system/decomposeParDict
   }
   
   getApplication(){ #去system/controldict这个字典中查找键名为application的项的值。
       foamDictionary -entry application -value system/controlDict #结果为foamRun
   }
   
   getSolver(){
       foamDictionary -entry solver -value system/controlDict #结果为incompressibleFluid
   }
   
   runApplication(){
       APP_RUN=
       LOG_IGNORE=false
       LOG_APPEND=false
       LOG_SUFFIX=
   
       # 解析选项和可执行文件
       while [ $# -gt 0 ] && [ -z "$APP_RUN" ]; do
           key="$1"
           case "$key" in
               -append|-a)
                   LOG_IGNORE=true
                   LOG_APPEND=true
                   ;;
               -overwrite|-o)
                   LOG_IGNORE=true
                   ;;
               -suffix|-s)
                   LOG_SUFFIX=".$2"
                   shift
                   ;;
               *)
                   APP_RUN="$key"
                   APP_NAME="${key##*/}"
                   LOG_SUFFIX="${APP_NAME}${LOG_SUFFIX}"
                   ;;
           esac
           shift
       done
   
       if [ -f log.$LOG_SUFFIX ] && [ "$LOG_IGNORE" = "false" ]
       then
           echo "$APP_NAME already run on $PWD:" \
                "remove log file 'log.$LOG_SUFFIX' to re-run"
       else
           echo "Running $APP_RUN on $PWD"
           if [ "$LOG_APPEND" = "true" ]; then
               $APP_RUN "$@" >> log.$LOG_SUFFIX 2>&1 #具体执行的指令
           else
               $APP_RUN "$@" > log.$LOG_SUFFIX 2>&1  #具体执行的指令
           fi
       fi
   }
   
   runParallel(){
       APP_RUN=
       LOG_IGNORE=false
       LOG_APPEND=false
       LOG_SUFFIX=
       nProcs=$(getNumberOfProcessors) #获取处理器数量
   
       # Parse options and executable
       while [ $# -gt 0 ] && [ -z "$APP_RUN" ]; do
           key="$1"
           case "$key" in
               -append|-a)
                   LOG_IGNORE=true
                   LOG_APPEND=true
                   ;;
               -overwrite|-o)
                   LOG_IGNORE=true
                   ;;
               -suffix|-s)
                   LOG_SUFFIX=".$2"
                   shift
                   ;;
               -np|-n)
                   nProcs="$2"
                   shift
                   ;;
               *)
                   APP_RUN="$key"
                   APP_NAME="${key##*/}"
                   LOG_SUFFIX="${APP_NAME}${LOG_SUFFIX}"
                   ;;
           esac
           shift
       done
   
       if [ -f log.$LOG_SUFFIX ] && [ "$LOG_IGNORE" = "false" ]
       then
           echo "$APP_NAME already run on $PWD:" \
                "remove log file 'log.$LOG_SUFFIX' to re-run"
       else
           echo "Running $APP_RUN in parallel on $PWD using $nProcs processes"
           if [ "$LOG_APPEND" = "true" ]; then
               ( mpirun -np $nProcs $APP_RUN -parallel "$@" < /dev/null >> log.$LOG_SUFFIX 2>&1 )
           else
               ( mpirun -np $nProcs $APP_RUN -parallel "$@" < /dev/null > log.$LOG_SUFFIX 2>&1 )
           fi
       fi
   }
   
   compileApplication(){
       echo "Compiling $1 application"
       wmake $1
   }
   
   cloneCase(){ #克隆case目录
       from=$1
       to=$2
   
       if [ ! -d $from ]
       then
           echo "Case $from does not exist"
           return 1
       elif [ -d $to ]
       then
           echo "Case already cloned: remove case directory $to to clone"
           return 1
       else
           echo "Cloning $to case from $from"
           mkdir -p $to
           for f in 0 system constant
           do
               cp -R $from/$f $to
           done
           return 0
       fi
   }
   
   cloneMesh(){ #克隆网格
       from=$1/constant/polyMesh
       to=$2/constant/polyMesh
   
       if [ ! -d $from ]
       then
           echo "Mesh $from does not exist"
           return 1
       elif [ -d $to ]
       then
           echo "Mesh already cloned: remove mesh directory $to to clone"
           return 1
       else
           echo "Cloning $to mesh from $from"
           cp -pr $from $to
           return 0
       fi
   }
   ```
