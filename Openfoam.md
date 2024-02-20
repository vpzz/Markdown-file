# 编译安装

1. Openfoam需要使用专用的ParaView，因为这里边有专门为Openfoam编写的读取模块。

2. 如果使用源码编译Openfoam时，也可以不手动编译paraview，而使用官方仓库提供内编译好的paraview。然后需要添加paraview的bin目录到PATH中。

   ```shell
   sudo apt install paraviewopenfoam510 #这个只会单独安装paraview
   #添加到.bashrc中
   PATH=$PATH:/opt/paraviewopenfoam510/bin
   ```

3. 新版本的paraview已经原生支持openfoam结果文件了，可以直接`sudo apt install paraview`安装即可。使用的时候，需要在对应的结果目录下创建一个任意的后缀名为.foam的文件即可。使用paraFoam时，会自动创建一个临时的.foam文件。也可以使用`paraFoam -touch`来创建一个永久的文件。

4. ThirdParty-11仓库中主要包含的是Scotch软件的源码，因为早期版本的Debian自带的Scotch版本比较落后，因此需要使用源码编译安装，不过在Ubuntu22.04中，可以使用`sudo apt install scotch`安装即可。

5. 源码目录中可能有冗余的文件，只有包含在Make/files中的文件才会被编译。这点可以从.dep文件的对应发现。

6. 源代码目录下的lnInclude目录中包含同级目录及其子目录的所有源文件，包括.C和.h。

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

7. 总的配置文件为`/home/zj/OpenFOAM/OpenFOAM-11/etc/bashrc`。

8. 

9. 

10. 

11. debug 调试，可以对软件进行单步执行、堆栈跟踪、调试等操作来发现bug。

12. release 发行版，如果最终调试后程序没有明显bug，可以作为可用的软件分享给他人使用就可以使用这个选项编译。

13. profiling 性能分析。可以对软件执行过程中的cpu利用率，内存占有进行分析。也可以用来发现、分析异常、bug。

14. 常见的和路径相关的宏：

    ```shell
    #如果源码存放路径为/home/zj/OpenFOAM/OpenFOAM-11。
    export WM_PROJECT_INST_DIR=$FOAM_INST_DIR #结果为/home/zj/OpenFOAM
    export WM_PROJECT_DIR=$WM_PROJECT_INST_DIR/$WM_PROJECT-$WM_PROJECT_VERSION #结果为/home/zj/OpenFOAM/OpenFOAM-11
    export WM_DIR=$WM_PROJECT_DIR/wmake #结果为/home/zj/OpenFOAM/OpenFOAM-11/wmake
    export WM_THIRD_PARTY_DIR=$WM_PROJECT_INST_DIR/ThirdParty-$WM_PROJECT_VERSION #结果为/home/zj/OpenFOAM/ThirdParty-11
    export WM_PROJECT_USER_DIR=$HOME/$WM_PROJECT/$USER-$WM_PROJECT_VERSION #结果为/home/zj/OpenFOAM/zj-11，默认在用户的家目录下创建一个用户名-版本的目录，作为用户目录
    export WM_COLLECT_DIR=$WM_PROJECT_DIR/platforms/${WM_OPTIONS}/${PWD////_} #默认为空
    
    export FOAM_INST_DIR=$(cd $(dirname ${BASH_SOURCE:-$0})/../.. && pwd -P) #结果为/home/zj/OpenFOAM。这行代码是在etc/bashrc中执行的，因此BASH_SOURCE就是该bashrc的路径。获取bashrc的目录部分，然后向上寻找2级父目录，且获取的是物理目录而非符号链接。
    export FOAM_JOB_DIR=$WM_PROJECT_INST_DIR/jobControl #结果为/home/zj/OpenFOAM/jobControl，默认不存在
    
    export ParaView_DIR=$WM_THIRD_PARTY_DIR/platforms/$WM_ARCH$WM_COMPILER/ParaView-$ParaView_VERSION #结果为/home/zj/OpenFOAM/ThirdParty-11/platforms/linux64Gcc/ParaView-5.10.1
    export ParaView_INCLUDE_DIR=$ParaView_DIR/include/paraview-$ParaView_MAJOR #默认为空，只有在paraviewSrcDir目录存在是才会定义这个变量。
    export ParaView_LIB_DIR=$ParaView_DIR/lib$paraviewArch$paraviewLibSubDir #默认为空，只有在paraviewSrcDir目录存在是才会定义这个变量。
    ```

15. 


# bashrc配置文件

## etc/bashrc

1. 总的配置文件：`etc/bashrc`：

   ```shell
   export WM_PROJECT=OpenFOAM
   export WM_PROJECT_VERSION=11
   ################################################################################
   # 这一部分是用户可以自定义的，不过之后的更新可能会覆盖这个文件。
   # FOAM_INST_DIR是OpenFOAM将要安装到的目录，如果使用bash来执行此文件，则以此文件来推断得到对应的目录，这样和源码目录在一块。也可以手动指定为固定的目录。
   [ "$BASH" -o "$ZSH_NAME" ] && \
   export FOAM_INST_DIR=$(cd $(dirname ${BASH_SOURCE:-$0})/../.. && pwd -P) || \
   export FOAM_INST_DIR=$HOME/$WM_PROJECT
   # export FOAM_INST_DIR=~$WM_PROJECT #OpenFOAM用户的家目录
   # export FOAM_INST_DIR=/opt/$WM_PROJECT #公共的区域，建议使用root安装
   # export FOAM_INST_DIR=/usr/local/$WM_PROJECT
   ################################################################################
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
   
   # Location of installation 定位安装目录
   export WM_PROJECT_INST_DIR=$FOAM_INST_DIR
   export WM_PROJECT_DIR=$WM_PROJECT_INST_DIR/$WM_PROJECT-$WM_PROJECT_VERSION
   
   if [ -d "$WM_PROJECT_DIR" ] #该目录默认存在，这段的功能是获取该目录的物理目录，避免使用符号链接。
   then
       WM_PROJECT_DIR_REAL=$(cd $WM_PROJECT_DIR && pwd -P) # -P表示显示物理目录
       if [ -d "$WM_PROJECT_DIR_REAL" -a -e "$WM_PROJECT_DIR_REAL/etc/bashrc" ]
       then
           export WM_PROJECT_DIR=$WM_PROJECT_DIR_REAL
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
   if [ -d "$WM_PROJECT_SITE" ]
   then
       export WM_PROJECT_SITE
   else
       unset WM_PROJECT_SITE
   fi
   
   # 定位用户文件
   export WM_PROJECT_USER_DIR=$HOME/$WM_PROJECT/$USER-$WM_PROJECT_VERSION
   
   # 导入一些初始化函数
   . $WM_PROJECT_DIR/etc/config.sh/functions
   
   # Source当前用户或者本地的配置文件
   _foamSource `$WM_PROJECT_DIR/bin/foamEtcFile prefs.sh` #默认不存在这个pref.sh文件
   
   # 处理bashrc脚本的命令行参数，export或unset对应的变量
   export FOAM_SETTINGS="$@"
   _foamParams $@
   
   # 清理标准环境变量 (PATH, LD_LIBRARY_PATH, MANPATH)
   foamClean=$WM_PROJECT_DIR/bin/foamCleanPath
   
   #此时PATH为:
   /home/zj/.vscode-server/bin/31c37ee8f63491495ac49e43b8544550fbae4533/bin/remote-cli:/home/zj/.local/bin:/home/zj/OpenFOAM/ThirdParty-11/platforms/linux64Gcc/gperftools-svn/bin:/home/zj/OpenFOAM/ThirdParty-11/platforms/linux64Gcc/cmake-*/bin:/home/zj/OpenFOAM/OpenFOAM-11/bin:/home/zj/OpenFOAM/OpenFOAM-11/wmake:/home/zj/OpenFOAM/zj-11/platforms/linux64GccDPInt32Opt/bin:/home/zj/OpenFOAM/site/11/platforms/linux64GccDPInt32Opt/bin:/home/zj/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/zj/.local/bin:/home/zj/.local/bin
   # 从PATH中清理foamOldDirs的目录
   cleaned=`$foamClean "$PATH" "$foamOldDirs"` && PATH="$cleaned"
   #此时PATH为:
   /home/zj/.vscode-server/bin/31c37ee8f63491495ac49e43b8544550fbae4533/bin/remote-cli:/home/zj/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
   # 清理 LD_LIBRARY_PATH
   # 此时LD_LIBRARY_PATH为：
   /home/zj/OpenFOAM/ThirdParty-11/platforms/linux64Gcc/gperftools-svn/lib:/home/zj/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/lib/openmpi-system:/home/zj/OpenFOAM/ThirdParty-11/platforms/linux64GccDPInt32/lib/openmpi-system:/usr/lib/x86_64-linux-gnu/openmpi/lib:/home/zj/OpenFOAM/zj-11/platforms/linux64GccDPInt32Opt/lib:/home/zj/OpenFOAM/site/11/platforms/linux64GccDPInt32Opt/lib:/home/zj/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/lib:/home/zj/OpenFOAM/ThirdParty-11/platforms/linux64GccDPInt32/lib:/home/zj/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/lib/dummy
   cleaned=`$foamClean "$LD_LIBRARY_PATH" "$foamOldDirs"` \
       && LD_LIBRARY_PATH="$cleaned"
   #此时LD_LIBRARY_PATH为：
   /usr/lib/x86_64-linux-gnu/openmpi/lib
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
   
   # 再次清理环境变量，本次只是去重
   #- Clean PATH
   cleaned=`$foamClean "$PATH"` && PATH="$cleaned"
   
   #- 清理 LD_LIBRARY_PATH
   cleaned=`$foamClean "$LD_LIBRARY_PATH"` && LD_LIBRARY_PATH="$cleaned"
   
   #- 清理 MANPATH (trailing ':' to find system pages)
   cleaned=`$foamClean "$MANPATH"`: && MANPATH="$cleaned"
   
   export PATH LD_LIBRARY_PATH MANPATH
   
   #- 清理 LD_PRELOAD
   if [ -n "$LD_PRELOAD" ]
   then
       cleaned=`$foamClean "$LD_PRELOAD"` && LD_PRELOAD="$cleaned"
       export LD_PRELOAD
   fi
   
   # 清理此脚本中用到的一些变量
   unset cleaned foamClean foamOldDirs
   
   # 再次执行脚本，以卸载初始化函数
   . $WM_PROJECT_DIR/etc/config.sh/functions
   
   # 执行bash_completion脚本
   [ "$BASH" ] && . $WM_PROJECT_DIR/etc/config.sh/bash_completion
   ```


## etc/config.sh/functions

1. `etc/config.sh/functions`：

   ```shell
   if [ -z "$WM_BASH_FUNCTIONS" ]
   then
       WM_BASH_FUNCTIONS=loaded #一个标记变量，第一次执行时，会进入到这个分支，第二次执行时就会执行else分支，把上一次执行时定义的_foam系列函数都unset掉。
       
   # _foamSource会依次Source所有的参数，如果定义了FOAM_VERBOSE，则输出一句Sourcing: 文件名。结果如下：
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/settings
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/compiler
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/aliases
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/mpi
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/paraview
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/ensight
       #Sourcing: /home/zj/OpenFOAM/OpenFOAM-11/etc/config.sh/gperftools
       _foamSource()
       {
           while [ $# -ge 1 ]
           do #PS1是shell的提示符
               [ "$FOAM_VERBOSE" -a "$PS1" ] && echo "Sourcing: $1" 1>&2
               . $1 #一次source一个参数，然后移除
             shift
           done
       }
   #逐个处理命令行参数，支持两种类型，name=和name=value
       _foamParams()
       {
           while [ $# -gt 0 ]
           do
               case "$1" in
               -*) #以-开头的选项是非法的
                   # Stray option (not meant for us here) -> get out
                   break
                   ;;
               *=)
                   # name=，会执行unset name。也会受到FOAM_VERBOSE的影响
                   [ "$FOAM_VERBOSE" -a "$PS1" ] && echo "unset ${1%=}" 1>&2
                   eval "unset ${1%=}"
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
               export PATH=$1:$PATH
               shift
           done
       }
       # 将参数逐个添加到LD_LIBRARY_PATH的开头，默认为控
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
   zj@zj-hit:~$ foamEtcFile -list #输出所有查找的目录
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
       exec 1>&2 #没有指定任何命令，因此会将当前shell的流1重定向到流2中。
       while [ "$#" -ge 1 ]; do echo "$1"; shift; done #逐一输出所有的参数。
       usage #执行usage函数。
       exit 1
   }
   # $0是/home/zj/OpenFOAM/OpenFOAM-11/bin/foamEtcFile
   # bin目录，也就是当前脚本所在的目录: /home/zj/OpenFOAM/OpenFOAM-11/bin
   binDir="$(cd -- "$(dirname "$0")" >/dev/null 2>&1 || exit ; pwd -P)"
   
   # 项目目录: /home/zj/OpenFOAM/OpenFOAM-11
   projectDir="${binDir%/bin}"
   
   # 目录前缀(和$FOAM_INST_DIR一样): /home/zj/OpenFOAM
   prefixDir="${projectDir%/*}"
   
   # 项目目录的名称: OpenFOAM-11
   projectDirName="${projectDir##*/}"
   
   # 为后续使用，先取消定义
   unset versionNum
   
   # 处理标准和Debian命名约定
   case "$projectDirName" in
       OpenFOAM-*)     # 标准命名约定 OpenFOAM-<VERSION>
           version="${projectDirName##OpenFOAM-}"
           ;;
       openfoam[0-9]*) # debian naming convention
           versionNum="${projectDirName##openfoam}"
           case "$versionNum" in
           [4-9]) # v4-9
               version="$versionNum"
               ;;
           [1-2][0-9]) # v10 onwards
               version="$versionNum"
               ;;
           3[0-9]) # e.g. v3.0
               version=$(echo "$versionNum" | sed -e 's@\(.\)\(.\)@\1.\2@')
               ;;
           [1-2][0-9][0-9]) # e.g. v1.7.0
               version=$(echo "$versionNum" | sed -e 's@\(.\)\(.\)\(.\)@\1.\2.\3@')
               ;;
           *)
               version="$WM_PROJECT_VERSION"
               ;;
           esac
           ;;
       openfoam-dev) # debian naming convention
           versionNum="${projectDirName##openfoam}"
           version="${versionNum##-}"
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
           mode="$2"
           # sanity check:
           case "$mode" in
           *u* | *g* | *o* )
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
           # convert x.y.z -> xyz version (if installation looked like debian)
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
   
   # 调试代码，可以取消注释以输出中间结果:
   # echo "Installed locations:"
   # for i in projectDir prefixDir projectDirName version versionNum
   # do
   #     eval echo "$i=\$$i"
   # done
   
   # Save the essential bits of information
   # 去除掉开头的 ~OpenFOAM/ (used in Foam::findEtcFile)
   nArgs=$#
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
   exit $exitCode
   ```

## bin/foamCleanPath

1. `bin/foamCleanPath`：

   ```shell
   #     Usage: foamCleanPath [-strip] path [wildcard] .. [wildcard]
   #         - 去除重复的目录
   #         - 区域和wildcard匹配的目录
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
   # 可以取消下行的#DEBUG，以输出调试信息
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
       case `uname -m` in
           i686) #Intel 32位CPU
               export WM_ARCH_OPTION=32
               export WM_CC='gcc'
               export WM_CXX='g++'
               export WM_CFLAGS='-fPIC'
               export WM_CXXFLAGS='-fPIC -std=c++0x'
               export WM_LDFLAGS=
           ;;
       x86_64) #Intel 64位
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
               WM_ARCH=linux64
               export WM_COMPILER_LIB_ARCH=64
               export WM_CC='gcc'
               export WM_CXX='g++'
               export WM_CFLAGS='-m64 -fPIC'
               export WM_CXXFLAGS='-m64 -fPIC -std=c++0x'
               export WM_LDFLAGS='-m64'
               ;;
           *)
               echo "Unknown WM_ARCH_OPTION '$WM_ARCH_OPTION', should be 32 or 64"\
                    1>&2
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
   
   # 作业控制的目录
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
   
   # 将application bins目录添加到PATH中，可以观察到有三个地方，USER，SITE，源代码目录中。
   #此时PATH为：
   /home/zj/.vscode-server/bin/31c37ee8f63491495ac49e43b8544550fbae4533/bin/remote-cli:/home/zj/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
   _foamAddPath $FOAM_USER_APPBIN:$FOAM_SITE_APPBIN:$FOAM_APPBIN
   #此时PATH为：
   /home/zj/OpenFOAM/zj-11/platforms/linux64GccDPInt32Opt/bin:/home/zj/OpenFOAM/site/11/platforms/linux64GccDPInt32Opt/bin:/home/zj/OpenFOAM/OpenFOAM-11/platforms/linux64GccDPInt32Opt/bin:/home/zj/.vscode-server/bin/31c37ee8f63491495ac49e43b8544550fbae4533/bin/remote-cli:/home/zj/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
   # 将wmake脚本的目录添加到PATH中，仅运行时环境不需要
   [ -d "$WM_DIR" ] && PATH=$WM_DIR:$PATH
   
   # 将OpenFOAM脚本目录添加到PATH中
   export PATH=$WM_PROJECT_DIR/bin:$PATH
   
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
   if [ -z "$WM_COMPILER_TYPE" ] #默认为system，不为0
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
   alias wm64='wmSet WM_ARCH_OPTION=64' #使用键值对指定参数
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
   if command -V wmRefresh 2> /dev/null | head -1 | grep -q "function" #wmRefresh是函数，再中文环境下，command -V 输出的第一行为 "wmRefresh 是函数"。
   then
       unset wmRefresh
   else
       unalias wmRefresh 2> /dev/null
   fi
   wmRefresh() #定义wmRefresh
   {
       wmProjectDir=$WM_PROJECT_DIR
       foamSettings=$FOAM_SETTINGS
       . $wmProjectDir/etc/config.sh/unset #先unset所有变量
       . $wmProjectDir/etc/bashrc $foamSettings #再重新执行etc/bashrc
   }
   # 改变OpenFOAM版本
   unset foamVersion
   foamVersion() # 输出OpenFOAM的版本，默认为OpenFOAM-11
   {
       if [ "$1" ]; then #可以手动指定一个版本号，如果制定了本地不存在的版本号，则会导致环境错乱，需要重新运行bash。
           foamInstDir=$FOAM_INST_DIR
           wmUnset #为下一步执行bashrc，先取消所有的变量设置
           . $foamInstDir/OpenFOAM-$1/etc/bashrc
           foam
           echo "Changed to OpenFOAM-$1" 1>&2
       else
           echo "OpenFOAM-$WM_PROJECT_VERSION" 1>&2
       fi
   }
   # 改变Paraview版本
   unset foamPV
   foamPV()
   {
       . $WM_PROJECT_DIR/etc/config.sh/paraview ParaView_VERSION=$1
       echo "paraview-$ParaView_VERSION  (major: $ParaView_MAJOR)" 1>&2
   }
   ```


## config.sh/unset

1. config.sh/unset：

   ```shell
   # Description
   #     Clear as many OpenFOAM environment settings as possible
   #
   #------------------------------------------------------------------------------
   
   # Clean standard environment variables (PATH, LD_LIBRARY_PATH, MANPATH)
   foamClean=$WM_PROJECT_DIR/bin/foamCleanPath
   [ -f "$foamClean" -a -x "$foamClean" ] || unset foamClean
   
   # The old dirs to be cleaned from the environment variables
   foamOldDirs="$WM_PROJECT_DIR $WM_THIRD_PARTY_DIR \
       $HOME/$WM_PROJECT/$USER $FOAM_USER_APPBIN $FOAM_USER_LIBBIN \
       $WM_PROJECT_SITE $FOAM_SITE_APPBIN $FOAM_SITE_LIBBIN $ParaView_DIR"
   
   #------------------------------------------------------------------------------
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
   
   #------------------------------------------------------------------------------
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
   
   #------------------------------------------------------------------------------
   # Unset MPI-related environment variables
   
   unset MPI_ARCH_PATH
   unset MPI_BUFFER_SIZE
   
   # Undefine OPAL_PREFIX if set to one of the paths on foamOldDirs
   if [ -z "$($foamClean "$OPAL_PREFIX" "$foamOldDirs")" ]
   then
       unset OPAL_PREFIX
   fi
   
   #------------------------------------------------------------------------------
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
   
   #------------------------------------------------------------------------------
   # Cleanup environment
   # PATH, LD_LIBRARY_PATH, MANPATH
   
   if [ -n "$foamClean" ]
   then
       cleaned=`$foamClean "$PATH" "$foamOldDirs"` && PATH="$cleaned"
       cleaned=`$foamClean "$LD_LIBRARY_PATH" "$foamOldDirs"` && LD_LIBRARY_PATH="$cleaned"
       cleaned=`$foamClean "$MANPATH" "$foamOldDirs"` && MANPATH="$cleaned"
   fi
   
   
   [ -n "$LD_LIBRARY_PATH" ] || unset LD_LIBRARY_PATH
   [ -n "$MANPATH" ] || unset MANPATH
   [ -n "$LD_PRELOAD" ] || unset LD_PRELOAD
   
   
   unset cleaned foamClean foamOldDirs
   #------------------------------------------------------------------------------
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
   SYSTEMOPENMPI) #默认是这个
       # Use the system installed openmpi, get library directory via mpicc
       # 使用系统自带的openmpi，通过mpicc程序来获得库的目录
       export FOAM_MPI=openmpi-system
   
       # Undefine OPAL_PREFIX if set to one of the paths on foamOldDirs
       if [ -z "$($foamClean "$OPAL_PREFIX" "$foamOldDirs")" ]
       then
           unset OPAL_PREFIX
       fi
       # mpicc --showme:link会输出链接选项，-L/usr/lib/x86_64-linux-gnu/openmpi/lib -lmpi。
       libDir=`mpicc --showme:link | sed -e 's/.*-L\([^ ]*\).*/\1/'` #结果为/usr/lib/x86_64-linux-gnu/openmpi/lib
   
       # Bit of a hack: strip off 'lib' and hope this is the path to openmpi
       # include files and libraries.
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
   #如果MPI_BUFFER_SIZE比20000000小，则修正为20000000。
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
   
   # 确定要使用的cmake Take the most recent.
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
   # 设置二进制和源码目录，如果要自己编译的话。
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

1. 执行Allwmake，来构建整个项目：

   ```shell
   #!/bin/sh
   cd ${0%/*} || exit 1    # 将工作目录切换到当前脚本所在的目录
   
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
   
   # 编译wmake所需的程序
   (cd wmake/src && make)
   
   # 编译第三方库
   if [ -d "$WM_THIRD_PARTY_DIR" ]
   then
       $WM_THIRD_PARTY_DIR/Allwmake
   else
       echo "Allwmake: no ThirdParty directory found - skipping"
   fi
   
   # 执行src目录下的Allwmake
   src/Allwmake $targetType $*
   
   # 执行applications目录下的Allwmake
   applications/Allwmake $targetType $*
   ```


## wmake/scripts/AllwmakeParseArguments

1. wmake/scripts/AllwmakeParseArguments：

   ```shell
   # 使用source来执行本脚本，这样所有的参数都会保留
   
   Script=${0##*/} #获取执行该脚本的脚本的文件名
   
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
           # 目标类型
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
       echo "$Script $targetType$targetSpace$(echo $PWD | sed s%$WM_PROJECT_DIR/%% )"
   fi
   
   # 如果 WM_CONTINUE_ON_ERROR 没有设置，则 激活shell选项 "stop on error"
   
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
   cd ${0%/*} || exit 1    # Run from this directory
   
   # Parse arguments for library compilation
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
   
   # Update OpenFOAM version strings if required
   wmakePrintBuild -check || wrmo OpenFOAM/global/global.o 2>/dev/null
   
   Pstream/Allwmake $targetType $*
   
   OSspecific/${WM_OSTYPE:-POSIX}/Allwmake $targetType $*
   wmake $targetType OpenFOAM
   
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

2. 


## wmake

1. wmake：

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
   #     files are included.  For those who need access to the dependency files the
   #     new wdep script is provided to locate them.  See the wdep script header or
   #     run:
   #         wdep -h
   #
   # See also
   #     wmakeLnInclude, wmakeLnIncludeAll, wmakeCollect, wdep, wrmdep, wrmo,
   #     wclean, wcleanPlatform, wcleanLnIncludeAll
   #
   #------------------------------------------------------------------------------
   Script=${0##*/}
   
   # Source the wmake functions
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
   
   The 'target' is a Makefile target:
     e.g., platforms/linux64GccDPOpt/.../fvMesh.o
   
   or a special target:
     all               wmake all sub-directories, running Allwmake if present
     queue             wmakeCollect all sub-directories, running Allwmake if present
     exe               Compile statically linked executable
     lib               Compile statically linked archive lib (.a)
     libo              Compile statically linked lib (.o)
     libso             Compile dynamically linked lib (.so)
     dep               Compile lnInclude and dependencies only
     objects           Compile but not link
   
   USAGE
   }
   
   
   # Default make is the "make" in the path
   make="make"
   
   
   #------------------------------------------------------------------------------
   # Set WM_NCOMPPROCS to number of cores on local machine
   #------------------------------------------------------------------------------
   
   useAllCores()
   {
       if [ -r /proc/cpuinfo ]
       then
           WM_NCOMPPROCS=$(grep -Ec "^processor" /proc/cpuinfo)
       else
           WM_NCOMPPROCS=1
       fi
   
       export WM_NCOMPPROCS
   }
   
   
   #------------------------------------------------------------------------------
   # Parse arguments and options
   #------------------------------------------------------------------------------
   
   # Default to compiling the local target only
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
           # Parallel compilation on all cores of local machine
           -j)
               useAllCores
               [ $# -ge 2 ] && [ "$2" -gt 0 ] > /dev/null 2>&1 \
                   && shift && export WM_NCOMPPROCS=$1
               echo "Compiling enabled on $WM_NCOMPPROCS cores"
               ;;
           # Parallel compilation on specified number of cores
           -j*)
               export WM_NCOMPPROCS=${1#-j}
               echo "Compiling enabled on $WM_NCOMPPROCS cores"
               ;;
           # Non-stop compilation, ignoring errors
           -k | -non-stop)
               export WM_CONTINUE_ON_ERROR=1
               ;;
           # Disable scheduled parallel compilation
           -no-scheduler)
               unset WM_SCHEDULER
               ;;
           # Meant to be used following a pull, this will:
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
   
   
   #------------------------------------------------------------------------------
   # Check environment variables
   #------------------------------------------------------------------------------
   
   checkEnv
   
   # When compiling anything but a standalone exe WM_PROJECT and WM_PROJECT_DIR
   # must be set
   [ "$1" = exe ] || { [ "$WM_PROJECT" ] && [ "$WM_PROJECT_DIR" ]; } || {
       echo "$Script error:" 1>&2
       echo "    environment variable \$WM_PROJECT or " \
            "\$WM_PROJECT_DIR not set" 1>&2
       echo "    while building project library" 1>&2
       exit 1
   }
   
   
   #------------------------------------------------------------------------------
   # Setup parallel compilation
   #------------------------------------------------------------------------------
   
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
   
   
   #------------------------------------------------------------------------------
   # Check arguments and change to the directory in which to run wmake
   #------------------------------------------------------------------------------
   
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
   
       # Specified directory name:
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
   
       # Print command
       [ -z "$targetType" ] || targetSpace=" "
       echo "$Script $targetType$targetSpace${dir:-.}"
   fi
   
   
   #------------------------------------------------------------------------------
   # Recurse the source tree to compile "all" targets
   #------------------------------------------------------------------------------
   
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
   
   
   #------------------------------------------------------------------------------
   # Recurse the source tree to compile "all" targets
   #------------------------------------------------------------------------------
   
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
   
   
   #------------------------------------------------------------------------------
   # Recurse the source tree to compile "all" targets using wmakeCollect
   #------------------------------------------------------------------------------
   
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
   
   
   #------------------------------------------------------------------------------
   # Search up the directory tree for the Make sub-directory,
   # check the existence of the 'files' file and build there if present
   #------------------------------------------------------------------------------
   
   cdSource
   
   
   #------------------------------------------------------------------------------
   # Transform options
   #------------------------------------------------------------------------------
   
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
   
   
   #------------------------------------------------------------------------------
   # Created the objectsDir directory
   #------------------------------------------------------------------------------
   
   objectsDir=$MakeDir/$WM_OPTIONS
   expandPath "$PWD"
   if [[ "$exPath" = *"$WM_PROJECT_DIR"* ]]
   then
       platformPath=$WM_PROJECT_DIR/platforms/${WM_OPTIONS}
       objectsDir=$platformPath${exPath//$WM_PROJECT_DIR/}
   fi
   
   mkdir -p "$objectsDir"
   
   
   #------------------------------------------------------------------------------
   # Create $objectsDir/files from $MakeDir/files if necessary
   #
   # Spawn a sub-shell and unset MAKEFLAGS in that sub-shell to avoid
   # $objectsDir/files being built in parallel
   #------------------------------------------------------------------------------
   
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
   
   
   #------------------------------------------------------------------------------
   # Make the dependency files
   #------------------------------------------------------------------------------
   
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
   
   
   #------------------------------------------------------------------------------
   # When WM_UPDATE_DEPENDENCIES is set, use forced dependency files update
   #------------------------------------------------------------------------------
   
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
   
   
   #------------------------------------------------------------------------------
   # Make the dependency files or object files and link
   #------------------------------------------------------------------------------
   
   # shellcheck disable=SC2093,SC2086
   exec $make -f "$WM_DIR/makefiles/general" MAKE_DIR="$MakeDir" \
        OBJECTS_DIR="$objectsDir" $targetType
   
   # Cleanup local variables and functions
   
   unset Script usage error useAllCores update expandPath findTarget
   ```

2. 

3. 

4. 

5. 
