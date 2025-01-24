# 编译记录

1. 下载Calculix.tar.gz文件，解压后会出现CCX目录，内部含有SPOOLES2.2，ARAPCK和Calculix三个文件夹。

2. 先构建SPOOLES2.2和ARAPCK，最后构建Calculix。三个文件夹放在同一级目录中，但不要求都放在用户家目录中，因为makefile中大多数为相对路径。

3. SPOOLES2.2的Tree/src/makeGlobalLib文件中包含了一个错误的引用应该将drawTree.c 改成draw.c，因为drawTree.c不存在。

4. 进入SPOOLES.2.2中执行 make CC=gcc lib。如果不加CC=gcc会报错:/usr/lang-4.0/bin/cc: No such file or directory。

5. 进入ARPACK文件夹，先根据README修改ARmake.inc文件。
   1. 修改home为ARPACK文件夹路径
   2. 修改PLAT = INTEL
   3. 修改`FFLAGS = -O -fallow-argument-mismatch`。这里去除了-cg89的选项，增加了-fallow-argument-mismatch
   4. 修改UTIL/second.f，在EXTERNAL   ETIME的最开头添加*注释
   5. 最后运行make lib即可
   6. 在Makefile的cleanlib目标下添加`rm -f libarpack*.a`，方便后续make clean清理编译结果。

6. 在Calculix/ccx_2.20/src中执行make。如果遇到 Interface mismatch in dummy procedure ‘f’ at (1): ‘fun’ is not a function的错误。单独编译该文件，应该加上 --std=legacy的选项。

7. 执行`./ccx_2.20 ../test/beamp`，检查是否出现beamp.dat文件，可以beamp.dat.ref校对检验软件是否成功编译。

8. 也可以调用test/compare脚本来检验软件是否成功编译。这一步会计算test中的所有inp文件并比较。

9. 整个工程的Makefile，位置和ARPACK文件夹平级，推荐使用：

   ```makefile
   all: ARPACK SPOOLES.2.2 CalculiX
   	cd ARPACK; make lib #不能使用-j并行,会报错
   	cd SPOOLES.2.2; make CC=gcc -j lib
   	cd CalculiX/ccx_2.20/src; make -j
   install:
   	sudo ln -sf /home/zj/CCX/CalculiX/ccx_2.20/src/ccx_2.20 /usr/bin/ccx
   clean:
   	cd ARPACK; make clean
   	cd SPOOLES.2.2; make clean
   	cd CalculiX/ccx_2.20/src; make clean
   	cd CalculiX/ccx_2.20/test; make clean
   ```

10. cubtri.f：

    ```fortran
    !将SUBROUTINE CUBRUL中的
          REAL*8 A1, A2, S, SN, DZERO, DONE, DTHREE, DSIX,f,
         &  point5,x,y
    !修改为如下，将real*8的f，修改为external f
          REAL*8 A1, A2, S, SN, DZERO, DONE, DTHREE, DSIX,
         &  point5,x,y
          EXTERNAL F
    ```

   11. 使用正则表达式在VSCODE中搜索中文，`.*[\u4E00-\u9FA5]+`。

# 缺少libgfortran.so.4

1. 官方发布的Calculix2.20可执行文件`ccx_2.20`是动态连接的，需要libgfortran.so.4，而ubuntu22.04后，默认使用gcc-11，默认仓库也不再提供libgfortran.so.4。使用ldd命令来查看可执行文件需要的动态库，参数需要是完整路径名。=>表示在本机匹配到的具体路径名。

   ```shell
   zj@zj-virtual-machine:~$ ldd /usr/local/bin/ccx
           linux-vdso.so.1 (0x00007ffcaab24000)
           libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007ff8e9cac000)
           libgfortran.so.4 => not found
           libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007ff8e99e4000)
           libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ff8e97bc000)
           libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x00007ff8e9770000)
           libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007ff8e9750000)
           libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007ff8e9708000)
           /lib64/ld-linux-x86-64.so.2 (0x00007ff8e9cc4000)
   ```

2. 需要修改/etc/apt/sources.list文件，添加下面一行，然后运行sudo apt update，sudo apt install gfortran-7。

   ```shell
   deb [arch=amd64] http://cn.archive.ubuntu.com/ubuntu focal main universe
   #上下两行的功能一样，就是源不同。
   deb [arch=amd64] http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main universe
   ```

3. 用户自己的编译链接的ccx_2.20，可以发现比官方发布的少了libpthread，libgomp。同时使用了更新的libgfortran。

   ```shell
   zj@zj-hit:~/CCX/CalculiX/ccx_2.20/test$ ldd ccx_2.20
           linux-vdso.so.1 (0x00007fff637fe000)
           libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x000074d731400000)
           libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000074d7321e7000)
           libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000074d731000000)
           libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x000074d7321c7000)
           libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x000074d7317b8000)
           /lib64/ld-linux-x86-64.so.2 (0x000074d7322e3000)
   ```

# 文件结构

1. Spooles2.2：可以用来求解稀疏实数/复数线性方程组。非稀疏矩阵使用LU分解及其变种，稀疏矩阵使用Krylov迭代法的变种。使用C语言编写，支持多线程并行计算。

2. Arpack：使用隐式重启Arnoldi方法（IRAM）或对称矩阵的Lanczos算法的相应变体来计算大型稀疏或结构化矩阵（结构化意味着矩阵向量积需要n阶而不是通常的n**2阶浮点运算）的几个特征值和相应的特征向量。普通和广义特征值问题都可以求解，实数和复数都可以处理。针对带状矩阵有优化，可以进行奇异值分解。使用Fortran77编写，支持多线程并行计算，Parpack。

3. 当矩阵对称时，IRAM简化为Lanczos过程的一种变体，称为隐式重启Lanczos方法（IRLM）。

4. 这些变体可以被视为Arnoldi/Lanczos过程与适用于大规模问题的隐式移位QR技术的合成。对于许多标准问题，不需要矩阵分解。只需要矩阵对向量的作用。存储要求大约为n*k个位置。不需要辅助存储。计算了所需k维特征空间的一组Schur基向量，该向量在数值上与工作精度正交。可根据要求提供数字精确的特征向量。

5. ARPACK使用反向通信接口（类似于排序函数，需要用户自己提供用于比较两个元素的回调函数），使用户能够轻松使用任何稀疏矩阵格式，或提供定制的稀疏矩阵向量乘法子程序。当需要矩阵操作时，它将控制权交给调用程序，并带有一个标志，指示需要什么操作。然后，调用程序必须执行该操作，并再次调用ARPACK例程以继续。这些操作通常是矩阵向量积和求解线性系统。本软件中会将arpack的矩阵操作分派给spooles。

6. 由于上游开发停滞不前，ARPAСK已被分叉为ARPACK-NG，作为依赖ARPACK的各个团体合作的一种形式。

7. 在计算数学中，无矩阵方法是一种求解线性方程组或特征值问题的算法，它不显式存储系数矩阵，而是通过计算矩阵向量积来访问矩阵。当矩阵太大，即使使用稀疏矩阵的方法，存储和操作它也会花费大量的内存和计算时间，此时这种方法可能更可取。许多迭代方法允许无矩阵实现，包括：

   1. 幂迭代

   2. Lanczos算法

   3. 共轭梯度法

   4. Krylov子空间迭代法

8. 注意CalculiX.h的X是大写，书写Makefile的依赖和包含头文件时不要写错。

9. 程序内有Bug，如果修改SFREE的宏，使得其每次释放内存后，都将指针置为NULL，则运行时会报错，卡住在extraploate.f90，ielorien指针在这里已经是NULL了，结果这里还使用了它。当然也不排除是因为修改了太多的源代码导致的。

10. dyna.c文件中出现如下笔误：

   ```c
   SFREE(xboundiff), SFREE(xbodydiff); //如果SFREE不包含将指针置为NULL的动作，则不会有问题，反之则会报错。
   ```

11. 源文件目录中

    1. 一共有942个.f90文件，但是gauss.f90和xlocal.f90只是被include到其他文件中，并不会单独编译，因此Makifile.inc中SCCXF一共包含940个.f90文件。
    2. 一共有176个.c源文件，而主文件ccx_2.20.c需要单独编译，因此Makefile.inc中SCCXC只包含175个.c文件。

12. 使用代码统计工具cloc统计文件数，空白行，注释行，代码行的总数：

    ```shell
    zj@zj-hit:~/CCX/CalculiX/ccx_2.20/src$ cloc *.f90 *.c *.h
        1127 text files.
        1127 unique files.
           0 files ignored.
    
    github.com/AlDanial/cloc v 1.90  T=0.78 s (1439.7 files/s, 384720.1 lines/s)
    -------------------------------------------------------------------------------
    Language                     files          blank        comment           code
    -------------------------------------------------------------------------------
    Fortran 90                     942            489          65562         144406
    C                              176          10206          10620          64229
    C/C++ Header                     9            794            168           4681
    -------------------------------------------------------------------------------
    SUM:                          1127          11489          76350         213316
    -------------------------------------------------------------------------------
    ```

13. 经过统计，代码行比较多的文件如下：

    ```shell
    cloc *.f90 *.c *.h --by-file -out stat.cloc
        1127 text files.
        1127 unique files.
           0 files ignored.
    
    github.com/AlDanial/cloc v 1.90  T=0.82 s (1373.6 files/s, 367056.2 lines/s)
    ----------------------------------------------------------------------------------
    File                                           blank        comment           code
    ----------------------------------------------------------------------------------
    CalculiX.h                                       681             52           4040
    nonlingeo.c                                      584            425           3653
    steadystate.c                                    486            273           3294
    bdfill.c                                         147            274           2572
    arpackcs.c                                       325            182           2486
    allocation.f90                                     0            124           2174
    trafontmortar2.c                                 150            275           2119
    frd.c                                            406            159           2066
    objectivemain_se.c                               513            244           2054
    dyna.c                                           299            194           1961
    complexfreq.c                                    304            169           1899
    readfrd.c                                        105            145           1780
    electromagnetics.c                               308            209           1587
    ccx_2.20.c                                        10            171           1553
    ccx_2.20step.c                                     1            238           1535
    e_c3d_se.f90                                       0            219           1495
    e_c3d.f90                                          0            159           1428
    e_c3d_duds.f90                                     0            215           1413
    compfluidfem.c                                   284            153           1346
    e_c3d_cs_se.f90                                    2            246           1338
    calinput.f90                                       0             77           1322
    ddebdf.f90                                         8           1606           1306
    multimortar.c                                    150            272           1208
    dgesv.f90                                          0            853           1143
    ddeabm.f90                                        10           2785           1118
    arpack.c                                         175            106           1096
    umat_single_crystal.f90                            0            160           1095
    pastix.c                                         239            196           1045
    linstatic.c                                      206            116           1029
    us3_sub.f90                                        6            459           1009
    ```

14. Makefile的实际执行顺序为：

    ```shell
    #1.编译ccx_2.20.c主文件
    gcc -O2  -I ../../../SPOOLES.2.2 -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT -g   -c -o ccx_2.20.o ccx_2.20.c
    #2.编译SCCXF中的940个.f90文件
    ...
    gfortran -O2 --std=legacy  -c str2mat.f90
    ...
    #3.编译SCCXC中的175个.c文件
    ...
    gcc -O2  -I ../../../SPOOLES.2.2 -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT -g   -c -o writeoldmesh.o writeoldmesh.c
    ...
    #4.打包所有的目标文件到静态库文件
    ar vr ccx_2.20.a absolute_relative.o ...
    #5.修改三个重要文件中的时间标志
    ./date.pl;
    #6.重新编译ccx_2.20.c，不过前面修改了三个文件，这里只重新编译了一个。
    gcc -O2  -I ../../../SPOOLES.2.2 -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT -g -c ccx_2.20.c;
    #使用gfortran链接所有的文件，生成可执行文件ccx_2.20
    gfortran  -Wall -O2 -o ccx_2.20 ccx_2.20.o ccx_2.20.a ../../../SPOOLES.2.2/spooles.a ../../../ARPACK/libarpack_INTEL.a -lpthread -lm -lc -fopenmp
    ```

15. Makefile：

    ```makefile
    CFLAGS = -g -Wall -Wno-unused-function -Wno-unused-but-set-variable -Wno-unused-variable -Wno-maybe-uninitialized -I ../../../SPOOLES.2.2 -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT #指定SPOOLES头文件的目录，定义宏SPOOLES和ARPACK表示使用这两个库，-g调试。
    FFLAGS = -g -Wall -Wno-unused-label -Wno-maybe-uninitialized -Wno-unused-dummy-argument -Wno-unused-variable --std=legacy #设置--std=legacy会使得gfortran8及以上的编译器在编译老代码中不再被支持的特性时，不会报错。
    CC=gcc
    FC=gfortran
    %o : %c
    	$(CC) $(CFLAGS) -c $<
    %o : %f90
    	$(FC) $(FFLAGS) -c $<
    include Makefile.inc #其中定义了三个变量，分别为一堆文件名SCCXF包含940个.f90源文件，SCCXC包含176个.c源文件，SCCXCXX包含一个umat_dl.cpp文件。第一个字母表示source，中间的CCX表示Calculi下，最后一个F表示Fortran
    SCCXMAIN = ccx_2.20.c #主文件，main函数所在位置
    #分别进行后缀名替换，创建对应的目标文件集合的变量名
    OCCXF = $(SCCXF:.f90=.o)
    OCCXC = $(SCCXC:.c=.o)
    OCCXMAIN = $(SCCXMAIN:.c=.o)
    DIR=../../../SPOOLES.2.2
    #设置要链接的库名和位置
    LIBS = $(DIR)/spooles.a \
    	../../../ARPACK/libarpack_INTEL.a \
        -lpthread -lm -lc
    ccx_2.20: $(OCCXMAIN) ccx_2.20.a  $(LIBS)
    	#./date.pl; #修改三个重要文件中的时间标志，可以定期单独在shell中执行该命令
    	$(CC) $(CFLAGS) -c ccx_2.20.c; #单独编译主文件
    	$(FC) $(FFLAGS) -o $@ $(OCCXMAIN) ccx_2.20.a $(LIBS) -fopenmp #使用gfortran进行链接。
    #打包所有的目标文件到静态库文件
    ccx_2.20.a: $(OCCXF) $(OCCXC)
    	ar vr $@ $?
    clean:
    	rm -f *.o *.a ccx_2.20
    	rm -f *.expand *.png *.pdf callgrind.out.*
    	rm -f input.* spooles.out #并不需要了，因为已经添加了修改工作目录的代码
    	rm -f .vscode-ctags .ctags tags
    test:
    	rm -f callgrind.out.*
    	valgrind --tool=callgrind --compress-strings=no --compress-pos=no --collect-jumps=yes ./ccx_2.20 -i ../test/beamp
    	kcachegrind callgrind.out.*
    ```

16. date.pl，功能是在ccx_2.20.c，frd.c中插入当前编译的时间，方便编译调试：

    ```perl
    #!/usr/bin/env perl
    chomp($date=`date -R`); #执行shell命令date，获取日期时间，存储到date变量中，chomp表示去掉结尾的换行符。使用-R选项，使之始终输出英文格式，如果在程序开始时修改LC_TIME环境变量，则会默认输出美国时区。
    # update the date in ccx_2.20.c
    @ARGV="ccx_2.20.c";
    $^I=".old"; #先将ccx_2.20.c打开，并另存为ccx_2.20.c.old，然后再ccx_2.20.c上修改
    while(<>){ #<>表示从@ARGV中读取内容
        s/You are using an executable made on.*/You are using an executable made on $date\\n");/g; #正则表达式，搜索然后替换
        print;
    }
    
    # update the date in frd.c
    @ARGV="frd.c";
    $^I=".old";
    while(<>){
        s/COMPILETIME.*/COMPILETIME       $date\\n", p1);/g;
        print;
    }
    system "rm -f ccx_2.20.c.old"; #删除掉备份的旧文件，保留修改后的文件
    system "rm -f ccx_2.20step.c.old";
    system "rm -f frd.c.old";
    ```

17. cleanupcode，功能和make clean不同，此处是用来清理无关的源文件的，例如想把ccx中和流体网络相关的功能都删除，可以在Makefile.inc中删除对应行，然后运行此文件即可删除对应文件：

    ```shell
    #!/bin/sh
    for x in *.f90 *.c; do #遍历所有的.f90和.c文件文件
        if [ "$x" = "ccx_2.20.c" ]; then
            #echo $x "is kept"
            continue
        fi
        if [ "$x" = "gauss.f90" ]; then
            #echo $x "is kept"
            continue
        fi
        if [ "$x" = "xlocal.f90" ]; then
            #echo $x "is kept"
            continue
        fi
    
        if grep -q $x Makefile.inc; then #观察文件是否是Makefile.inc记录的
            #echo $x "is kept"
            continue
        else
            echo $x "is deleted"
            rm -f $x
        fi
    done
    
    ```

18. hwloc可以显示CPU拓扑，比较方面地查看CPU各级缓存以及各个核、物理CPU之间，可以共享哪一级别的CPU cache。

    ```shell
    zj@zj-hit:~/CCX/ARPACK$ hwloc-ls
    Machine (1923MB total)
      Package L#0
        NUMANode L#0 (P#0 1923MB)
        L3 L#0 (9216KB)
          L2 L#0 (256KB) + L1d L#0 (32KB) + L1i L#0 (32KB) + Core L#0 + PU L#0 (P#0)
          L2 L#1 (256KB) + L1d L#1 (32KB) + L1i L#1 (32KB) + Core L#1 + PU L#1 (P#1)
      HostBridge
        PCI 00:07.1 (IDE)
        PCI 00:0f.0 (VGA)
        PCI 00:10.0 (SCSI)
          Block(Disk) "sda"
        PCIBridge
          PCI 02:00.0 (Ethernet)
            Net "ens32"
          PCI 02:03.0 (SATA)
    ```

# Calculix.h文件

1. 在ccx_2.20.c中包含了，主要是定义了有些简短的宏，用来简化函数调用：

   ```c
   //所有的Fortran函数都用Fortran(A,B)宏包装，编译参数中定义了-DARCH="Linux"，因此
   #define Linux 1
   #define IRIX 2
   #define IRIX64 3
   #define HP 4
   //编译参数 -DARCH="Linux"
   #if ARCH == Linux 
   #define FORTRAN(A,B) A##_  B
   #elif ARCH == IRIX || ARCH == IRIX64
   #define FORTRAN(A,B) A##_##B
   #elif ARCH == HP
   #define FORTRAN(A,B) A##B
   #endif
   
   #if ARCH == Linux
   #define CEE(A,B) A##_  B
   #elif ARCH == IRIX || ARCH == IRIX64
   #define CEE(A,B) A##_##B
   #elif ARCH == HP
   #define CEE(A,B) A##B
   #endif
   //给整个数组赋予相同的值
   //串行，就是使用for循环
   #define DMEMSET(a,b,c,d) for(im=b;im<c;im++)a[im]=d
   //并行，会调用两个函数，分别设置DOU类型和ITG类型
   #define DOUMEMSET(a,b,c,d) setpardou(&a[b],d,c-b,num_cpus)
   #define ITGMEMSET(a,b,c,d) setparitg(&a[b],d,c-b,num_cpus)
   //内存分配，重分配，释放，其中a为指针，b为类型，c为元素个数
   //为double real类型数据分配内存，然后并行初始化为0
   #define DNEW(a,b,c) {a=(b *)u_malloc((c)*sizeof(b),__FILE__,__LINE__,#a); \
           DOUMEMSET(a,0,c,0.);}
   //为ITG类型数据分配内存，然后并行初始化为0
   #define INEW(a,b,c) {a=(b *)u_malloc((c)*sizeof(b),__FILE__,__LINE__,#a); \
           ITGMEMSET(a,0,c,0);}
   //仅分配，不初始化
   #define MNEW(a,b,c) a=(b *)u_malloc((c)*sizeof(b),__FILE__,__LINE__,#a)
   //分配并串行初始化为0，calloc函数默认就会将内存初始化为0
   #define NNEW(a,b,c) a=(b *)u_calloc((c),sizeof(b),__FILE__,__LINE__,#a)
   //重新分配，但不初始化
   #define RENEW(a,b,c) a=(b *)u_realloc((b *)(a),(c)*sizeof(b),__FILE__,__LINE__,#a)
   //释放内存
   #define SFREE(a) u_free(a,__FILE__,__LINE__,#a)
   //定义ITG为32位还是64位，也会修改printf的格式化参数
   #ifdef LONGLONG
   #define ITG long long
   #define ITGFORMAT "lld"
   #else
   #define ITG int
   #define ITGFORMAT "d"
   #endif
   //Fortran函数定义包装，一般来说只有需要从C函数中调用的Fortran函数才需要包装，如果一个Fortran函数只会被Fortran函数调用，则不用包装。整个程序中不会出现Fortran调用C的情况
   void FORTRAN(actideacti, (char* set, ITG* nset, ITG* istartset, ITG* iendset,
          ITG* ialset, char* objectset, ITG* ipkon, ITG* ibject,
          ITG* ne));
   //C函数定义
   void* addmt(ITG* i);
   ```

# 自定义的内存分配和释放

1. 一共4个文件和函数：

   ```c
   u_calloc.c u_free.c u_malloc.c u_realloc.c
   ```

2. u_malloc

   ```c
   //增加了检查环节，确保不会返回NULL指针，还接收文件名，行号和内存块指针变量名字符串，以便更好地报告错误。
   extern int log_realloc; //是否将内存分配释放相关操作记录到日志中，默认为-1，即不记录
   void *u_malloc(size_t size,const char *file,const int line, const char* ptr_name){
     void *a;
     char *env;
   
     if(size==0){ //直接返回
       a=NULL;
       return(a);
     }
   
     a=malloc(size);
     if(a==NULL){ //分配失败
       printf("*ERROR in u_malloc: error allocating memory\n");
       printf("variable=%s, file=%s, line=%d, size=%ld\n",ptr_name,file,line,size);
       if(size<0){ //??
   	printf("\n It looks like you may need the i8 (integer*8) version of CalculiX\n");
       }
       exit(16); //错误退出码
     }
     else {
       if(log_realloc==-1) { //默认就是-1
         log_realloc=0;
         env=getenv("CCX_LOG_ALLOC"); //从环境变量中读取，如果有的话，就是用环境变量定义的
         if(env) {log_realloc=atoi(env);}
       }
       if(log_realloc==1) { //只有当log_realloc为1时，才记录
   	printf("\033[1;32;40m%3d-\033[0mALLOC   %s, file %s, line=%d, size=%ld, "
              "addr= %p\n", count, ptr_name, file, line, size, a); //\033可以改变终端文字的颜色，这里是黑色背景，绿色文字。
   	count++;
       }
       return(a); 
     }
   }
   ```

3. printf输出颜色的方式，使用ANSI转义码来设置文本样式和颜色可能会因为不同的终端软件和操作系统而产生不同的效果。 同时，这种方式也只适用于在终端上输出：

   ```c
   printf("\033[显示方式;字体颜色;背景颜色m 字符串 \033[0m"); //其中显示方式;字体颜色;背景颜色，可以任意组合，使用分号隔开即可。
   // \033[ 表示转义序列的开始，会设置随后的字体格式，转义序列是以ESC开头，ESC的ASCII码是27，用八进制表示的33。
   // 显示方式：0：默认值  1：高亮 、22：非粗体、4：下划线、24：非下划线、5：闪烁、25：非闪烁、7：反显、27：非反显
   // 字体颜色：30: 黑 31: 红 32: 绿 33: 黄 34: 蓝 35: 紫 36: 深绿 37: 白色
   // 背景颜色：40: 黑 41: 红 42: 绿 43: 黄 44: 蓝 45: 紫 46: 深绿 47: 白色
   // 'm'表示转义序列的结束
   // 结尾的 \033[0m 表示恢复默认值，即\033[0;30;47m
   ```

4. 为方便打印字符串为不同颜色，我们可以将一些常用的颜色定义成宏，并将系统提供的printf函数做一个封装：

   ```c
   #define HL_GRN          "\033[1;32m"    //高亮绿色
   #define PF_CLR  "\033[0m"       //清除
   
   #define myprintf(color, format, args...) \
       do{                                  \
               printf(color);               \
               printf(format, ##args);      \
               printf(PF_CLR);              \
       }while(0)
   //使用方法：
   myprintf(HL_YEL,"%s\n","yikoulinux");
   ```

5. 可以在.bashrc中添加`export CCX_LOG_ALLOC=1`，来输出内存释放分配的日志，它会混合原来的求解器输出到屏幕上。


# 统计时间

1. 统计计算时间

   ```c
   #include <time.h>
   struct timespec totalCalculixTimeStart, totalCalculixTimeEnd; //用来记录运行时间的结构体
   /*
   struct timespec {
   	time_t tv_sec; // 秒
   	long tv_nsec; //纳秒
   };
   */
   int main(int argc, char* argv[]) {
       double totalCalculixTime; //用来保存消耗的秒数
       clock_gettime(CLOCK_MONOTONIC, &totalCalculixTimeStart); //获取开始的时刻,CLOCK_MONOTONIC表示从系统启动这一刻起开始计时,不受系统时间被用户改变的影响
       //...计算消耗
       clock_gettime(CLOCK_MONOTONIC, &totalCalculixTimeEnd);//获取结束的时刻
       totalCalculixTime = (totalCalculixTimeEnd.tv_sec - totalCalculixTimeStart.tv_sec) * 1e9;//转换成纳秒
       totalCalculixTime = (totalCalculixTime + (totalCalculixTimeEnd.tv_nsec - totalCalculixTimeStart.tv_nsec)) * 1e-9; //再转换成秒
       printf("________________________________________\n\n");
       printf("Total CalculiX Time: %lf\n", totalCalculixTime);
       printf("________________________________________\n");
       return 0;
   }
   ```

# 命令行参数处理

1. 命令行参数处理

   ```c
     if (argc == 1) { //没有任何参数
       printf("Usage: CalculiX.exe -i jobname\n");
       FORTRAN(stop, ()); //会调用自定义的Fortran函数stop,该函数会调用自定义closefile函数,然后再调用exit(201)。
     } else {
       for (i = 1;i < argc;i++) {
         if (strcmp1(argv[i], "-i") == 0) { //自定义的函数
           strcpy(jobnamec, argv[i + 1]); //C专用，因为C的字符串以\0作为结尾，因此使用标准库
           strcpy1(jobnamef, argv[i + 1], 132); //Fortran专用，指定最大长度
           jin++;
           break;
         }
         if (strcmp1(argv[i], "-v") == 0) {
           printf("\nThis is Version 2.20\n\n");
           FORTRAN(stop, ());
         }
       }
       if (jin == 0) { strcpy(jobnamec, argv[1]);strcpy1(jobnamef, argv[1], 132); }
       /* next lines deactivated on March 18, 2020 */
   
       /*    for(i=1;i<argc;i++){
         if(strcmp1(argv[i],"-o")==0){
     strcpy(output,argv[i+1]);break;}
     }*/
     }
     putenv("CCX_JOBNAME_GETJOBNAME=jobnamec");
   ```

2. stop.f90：

   ```fortran
   subroutine stop()
       implicit none
       call closefile()
       call exit(201)
   end
   ```

3. closefile.f90：

   ```fortran
   subroutine closefile()
       implicit none
   !计算结束时关闭所有文件
       logical rout
   !关闭.inp文件，全程只读
       close(1)
   !关闭.dat文件，可以刷新一下
   !   flush(5)
       close(5)
   !关闭.sta文件
       close(8)
   !关闭.cvg文件
       close(11)
   !关闭.rout文件
       inquire(15,opened=rout) !查询该文件是否处于打开状态，如果是，则关闭
       if(rout) close(15)
       return
   end
   ```

# 字符串处理函数

1. strcmp1，判断s1和s2的一方是否是另一方的连续首子串：

   ```c
   //s1应为一个变化的域，s2应为一个固定的字符串
   ITG strcmp1(const char* s1, const char* s2) {
     ITG a, b;
     do {
       a = *s1++;//逐个从s1中取出字符，然后移动指针
       b = *s2++;
       if (b == '\0') {
         a = '\0';
         b = '\0';
         break;
       }
       if (a == '\0') {
         a = '\0';
         b = '\0';
         break;
       }
     } while (a == b);
     return(a - b);
     //如果s1或s2为空字符串，则会退出上面的循环，且a=b=0,此时返回0。
     //若二者都不为空串则依次比较，出现a或b为0，则退出循环，此时a=b=0,此时返回0。
   }
   // "","-i" 结果为0
   // "a","-i" 结果为52
   // "-i","-i" 结果为0
   // "-input","-i" 结果为0
   ```

2. strcmp2，逻辑同上，不过只比较两个字符串的前length（下标为0，1，...，length-1）个字符：

   ```c
   ITG strcmp2(const char* s1, const char* s2, ITG length) {
     ITG a, b, i;
     i = 0;
     do {
       a = *s1++;
       b = *s2++;
       if (b == '\0') {
         a = '\0';
         b = '\0';
         break;
       }
       if (a == '\0') {
         a = '\0';
         b = '\0';
         break;
       }
       i++;
     } while ((a == b) && (i < length));
     return(a - b);
   }
   // "-inout","-inp",4 结果为-1
   // "-inout","-inp",3 结果为0，因为仅比较下标为 0,1,2的字符
   ```

3. strcpy1：

   ```c
   ITG strcpy1(char* s1, const char* s2, ITG length) {
       //将s2的0到length-1下标的元素复制给s1，如果s2的元素不够多，则只复制s2的内容，然后在s1末尾添加空格字符' '。
     ITG b, i, blank = 0;
     for (i = 0;i < length;i++) {
       if (blank == 0) {
         b = *s2;
         if (b == '\0')
           blank = 1; //b的意义何在?为什么不直接判断*s2呢?
       }
       if (blank == 0) {
         *s1 = *s2;
         s2++;
       } else
         *s1 = ' ';
       s1++;
     } //注意到，一旦blank变为1后，不会再变为0
     return 0;
   }
   // "-inp",5 s1为['-','i','n','p',' '] 不会添加'\0'
   // "-inp",3 s1为['-','i','n'] 也不会添加'\0'
   ```


# 改装

1. 在每个函数的开头添加一个被调用时输出的日志，可以更方便地观察执行流：

   ```shell
   #define NNEW(a,b,c) a=(b *)u_calloc((c),sizeof(b),__FILE__,__LINE__,#a)
   
   #Fortran文件
   write(*,*) 'Call file = '
   
   #C文件
   #ifdef DEBUG_CALL_TRACE
     printf("Call file = %s\n", __FILE__);
   #endif
   
   #使用宏定义，有一点不太好，就是修改Makefile的CFLAGS后，还必须全部编译所有的文件才会生效。
   #可以使用一个全局变量，从环境变量读入，然后再每个函数内进行判断，决定是否调用call trace
   ```


# 使用到的工程文件

1. 流号和文件名对应，所有的文件都是使用Fortran的open函数打开。

   ```shell
   #在整个源代码工程中搜索open（Fortran）和fopen（C）函数，统计所有的文件读写
   #流号  文件名
   1      jobname.inp #输入文件
   2      jobname.rfn.inp #网格refine后的inp文件
   5      jobname.dat #输出的结果
   7      jobname.frd #结果数据库文件，类似于abaqus的.odb文件
   8      jobname.sta #
   9      TetMasterSubmodel.frd #四面体网格
   10     jobname.vwf #辐射分析中的viewfactor
   10     vector_.out #矢量数据，调试会用到
   10     matrix_.out #矩阵数据，调试会用到
   11     jobname.cvg #收敛状态文件
   12     jobname.fcv #收敛数据
   12     jobname.mtx #子结构的矩阵
   15     jobname.rout#重启动相关
   16     input.inpc #对inp文件进行初步处理后的结果
   16     input.ipoinp
   16     input.inp
   16     input.ipoinpc
   18     spooles_matrix #spooles矩阵
   20     jobname.equ #
   27     jobname.cel #接触单元
   27     jobname.sen0 #敏感性分析
   27     jobname_force#复数形式的力
   40     jobname.nam #质量缩放
   40     jobname_WarnNodeMissMultiStage.nam #多阶段MPC
   50     jobname.lhs #trilinos的左侧
   50     jobname.rhs #trilinos的右侧
   50     jobname.rig #trilinos的刚体模式
   88     jobname.wb  #
          spooles.out #spooles的输出
          jobname.eig #特征值和质量矩阵
          jobname.stm #刚度矩阵
          jobname.dof #自由度
          jobname.sti #刚度矩阵
          jobname.mas #质量矩阵
          jobname.con #热传导矩阵
          jobname.sph #比热容矩阵
   ```

2. Fortran使用//拼接字符串，这句代码会被翻译成多个函数调用：

   ```fortran
   fndat=jobname(1:i)//'.dat' !如果在调试时，需要跳过过程才可以跳过这一行
   ```

# 修改工作目录

1. 在读取到.inp文件的路径后，立刻修改工作目录，这样所有求解产生的文件都会和.inp在一个目录下：

   ```c
   // 修改工作目录为inp文件所在的目录。因为dirname会修改参数，所以需要一个临时的字符串
   strcpy(tmpjobname, jobnamef);
   if (chdir(dirname(tmpjobname)) < 0) {
       printf("Error: Cannot change into the .inp directory.\n");
       FORTRAN(stop, ());
   }
   ```

# VSCode 工程配置

1. 如果要进行debug，不建议打开O2，因为有些代码可能会被gcc优化的变形严重，跳转的位置不对。同时还有可能出现局部变量被优化，在调试器的变量面板中出现optimized out的情况。

2. 使用Fortran宏包括的Fortran函数，需要使用ctags才可以在vscode内跳转。

3. 安装Ctags Companion扩展。然后执行终端→运行任务→显示所有任务→Ctags Companion: rebuild ctags即可生成`tags`文件。之后可以使用F12，CTRL+单击来进行跳转。

4. ctags在Ubuntu22.04有两个版本，exuberant ctags 和 universal ctags。universal ctags是exuberant ctags的继续开发。

   ```shell
   sudo apt install universal-ctags #安装ctags
   ```

5. VSCode的配置默认只有用户，当程序同时打开了一个目录时，会增加一个工作区的设置。当使用remote时，还会增加一个远程的设置。配置存放的位置分别为：

   1. 用户配置，并不存放在本地机的用户家目录下，而是在"C:\Users\zj\AppData\Roaming\Code\User\settings.json"。

   2. 远程配置，存放在远程机用户家目录下的.vscode目录中的settings文件。

   3. 工作区配置，存放在打开的目录的.vscode目录中的settings文件。

6. 账号同步的内容是用户配置文件的内容。

7. 三个位置的优先级从低到高依次为：用户→远程→工作区。

8. VSCode的每个配置对每个选项都有一个默认值，如果仅在用户区修改了某些选项，则也会覆盖工作区的默认值。此时只有在工作区也修改该选项才会覆盖用户区的选项。

9. 有时候更改完设置后，没有效果，可以重启vscode试试。

10. 也可以将多个文件夹添加到同一个工作区, 此时, 工作区需要单独保存为一个 code-workspace 文件。

11. 如果在VSCode remote中使用ranger，右键打开文件时，报错：`xdg-open unexpected option: '--'`。此时可以进行如下操作：

    ```shell
    ranger --copy-config=all #命令行执行如下命令，生成ranger的配置文件，在~/.config/ranger目录下。
    #在~/.config/ranger/rifle.conf文件中找到下面的内容。将下面的 xdg-open -- "$@"改为${VISUAL:-$EDITOR} -- "$@"。这样就会使用select-editor选中的编辑器打开了。
    label open, has xdg-open = ${VISUAL:-$EDITOR} -- "$@"
    label open, has open     = open -- "$@"
    ```

12. 有时需要不格式化保存文件，可以使用Ctrl+Shift+P，选择保存但不格式化，save without formatting即可。

13. task.json，用于生成可执行文件，点击菜单栏的终端→运行生成任务，可以执行默认任务，需要打开该项目的一个文件，否则会提示无法解析fileDirname变量：

    ```json
    {
        "tasks": [
            {
                "type": "cppbuild",
                "label": "构建ccx",
                "command": "make", //调用make
                "args": [
                    "-j" //并行构建
                ],
                "options": {
                    "cwd": "${fileDirname}"
                },
                "presentation": {
                    "revealProblems": "onProblem", //只有在构建遇到问题时才会显示问题
                    "close": true //自动关闭构建结果面板
                },
                "problemMatcher": [
                    "$gcc"
                ],
                "group": {
                    "kind": "build",
                    "isDefault": true //设置为默认的task
                },
                "detail": "调试器生成的任务。"
            },
            {
                "type": "shell",
                "label": "Ctags Companion: rebuild ctags",
                "command": "ctags",
                "args": [
                    "-R",
                    "--fields=+nKz"
                ],
                "problemMatcher": []
            }
        ],
        "version": "2.0.0"
    }
    ```

14. launch.json，用于启动调试：

    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "(gdb) 启动",
                "type": "cppdbg",
                "request": "launch",
                "program": "${workspaceFolder}/ccx_2.2*", //设置可执行文件的完整路径，${workspaceFolder}为当前工作空间的位置，是/home/zj/CCX/CalculiX/ccx_2.2*/src。
                "args": [ //命令行参数
                    "-i",
                    "../test/beamp"
                ],
                "preLaunchTask": "${defaultBuildTask}", //在debug启动之前，先执行构建的task，这样可以保证在每次修改完代码后，再调试时，行号能够对应的上。
                "stopAtEntry": false,
                "cwd": "${fileDirname}",
                "environment": [],
                "externalConsole": false,
                "MIMode": "gdb",
                "setupCommands": [
                    {
                        "description": "为 gdb 启用整齐打印",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    },
                    {
                        "description": "将反汇编风格设置为 Intel",
                        "text": "-gdb-set disassembly-flavor intel",
                        "ignoreFailures": true
                    }
                ]
            }
        ]
    }
    ```

15. settings.json，这里保存工作区的设置：

    ```json
    {
        "files.associations": {
            "*.f": "FortranFixedForm",
            "*.f90": "FortranFreeForm"
        }
    }
    ```
    
16. c_cpp_properties.json，用于控制IntelliSense的高亮：

    ```json
    {
        "configurations": [
            {
                "name": "Linux", // 系统名称
                "includePath": [ // 头文件路径
                    "../../../SPOOLES.2.2",
                    "../../../ARPACK"
                ],
                "compilerPath": "/usr/bin/gcc",
                "defines": [ // 添加全局宏定义
                    "ARCH=Linux",
                    "SPOOLES",
                    "ARPACK",
                    "MATRIXSTORAGE",
                    "NETWORKOUT"
                ],
                "cStandard": "gnu99", // 采用的C标准
                "intelliSenseMode": "linux-gcc-x64"
            }
        ],
        "version": 4
    }
    ```

# 仓库备份

1. 在根目录执行make clean，恢复源码目录。

2. 回到上级目录，执行如下命令打包并压缩：

   ```shell
   tar -czvf CalculiX-`date +%F`.tar.gz --exclude=CCX/CalculiX/ccx_2.20/test/*.inp --exclude=CCX/CalculiX/ccx_2.20/test/*.ref CCX #会生成一个类似CalculiX-2024-03-05.tar.gz的文件。--exclude=PATTERN 排除以 PATTERN 指定的文件。
   # 只保留test文件下的除了.inp和.ref以外的文件，也就是datacheck.pl，frdcheck.pl，compare，Makefile。
   ```

3. 执行如下命令解压缩：

   ```shell
   tar -xzvf CalculiX*.tar.gz #或者使用x命令。
   ```

# CalculiXstep

1. 这个文件允许将ccx作为一个库，被其他函数调用，他就是将ccx_2.20.c做了封装，一般用不上，这里就删除了。

2. 该函数的说明：

   ```c
   /* in FORTRAN convention:
        nelemload(1,i) (ITG): element for loading i
        nelemload(2,i) (ITG): node for the environmental temperature
                              (heat transfer analysis)
        xload(1,i) (double): magnitude of load at end of a step or, for heat
                             transfer analyses, the convection or the radiation
                             coefficient
        xload(2,i) (double): the environment temperature (only for heat transfer
                             analyses)
        nload (ITG): number of distributed loads
        sideload(i): load label; indicates element side to which load is applied
        timepar(1) (double): time increment
        timepar(2) (double): step length
        timepar(3) (double): minimum time increment allowed
        timepar(4) (double): maximum time increment allowed
        timepar(5) (double): time increment for CFD-calculations
        ne (ITG): highest element number
        ipkon(i) (ITG): pointer for element i into field kon
        kon(ipkon(i)+1,....ipkon(i)+nope) (ITG): topology (node numbers) for
                                                 element i; "nope" depends on the
                                                 element type (stored in lakon)
        lakon(i) (character*8): label for element i
        nk (ITG): highest node number
        co(1..3,i) (double): coordinates of node i
        vold(0,i) (double): temperature in node i
        vold(1,i) (double): displacement in global x in node i
        vold(2,i) (double): displacement in global y in node i
        vold(3,i) (double): displacement in global z in node i
        veold(0..3,i) (double): first time derivative of field vold
        accold(0..3,i) (double): second time derivative of field vold
        nboun (ITG): number of single point constraints (SPC)
        ikboun(i) (ITG): sorted degrees of freedom corresponding to the SPC's.
                         The degree of freedom corresponding to global direction
                         k in node j is idof=8*(j-1)+k. Applicable directions
                         are 0 (temperature), 1 (global x-dir), 2 (global y-dir)
                         and 3 (global z-dir)
        ilboun(i) (ITG): SPC number corresponding to the sorted degrees of freedom
                         in ikboun
        xboun(i) (double): value of the SPC
        nmethod (ITG): nmethod=1: static analysis
        nmethod=2: frequency analysis
        nmethod=3: buckling analysis
        nmethod=4: (linear or nonlinear) dynamic analysis
        nmethod=5: steady state dynamics analysis
        nmethod=6: Coriolis frequency calculation
        nmethod=7: flutter frequency calculation
        nmethod=8:  magnetostatics
        nmethod=9:  magnetodynamics
        nmethod=10: electromagnetic eigenvalue problems
        nmethod=11: superelement creation or Green function calculation
        nmethod=12: sensitivity analysis
        externalfaces: (81 characters) surface name of the faces in contact with
                       the fluid; for this surface the work will be calculated at
                       the end of the present routine before returning the control
                       to the calling program. The surface must be defined in the
                       CalculiX input deck as a facial surface, i.e. consisting of
                       faces (not nodes). In the calling program of CalculiXstep
                       there must be a blank behind this name.
        delexternalwork (double): total external work on the faces contained in
                                  the surface defined by externalfaces performed
                                  during this call
        inputsteps (ITG): number of steps to be read from the input deck. This
                          requires (inputsteps) calls to CalculiXstep.c. Call
                          (inputsteps+1) is the first call for which the input
                          deck is not further read, i.e. in this call the
                          information from step (inputsteps) is taken, possibly
                          modified by the information transferred by the user into
                          CalculiXstep.c through the argument list.
        iperturb(1) (ITG): perturbation parameter: specifies which nonlinear
                           procedure is to be selected. Should not be changed by
                           the calling program
        iperturb(2) (ITG): if 0: geometrically linear calculation (linearized
                                 strain)
                           if 1: geometrically nonlinear calculation (quadratic
                                 terms in the strain are taken into account)
                                 can be changed by the calling program
        irstrt(1) (ITG): if   0: no restart (neither READ nor WRITE)
                         if > 0: every irstrt steps the results are stored in file
                              jobname.rout
                      Remark: reading a restart file is obtained by inserting
                              *restart,read as first executable statement in a
                              CalculiX input deck
        irstrt(2) (ITG): if 0: no OVERLAY while writing a restart file
                         if 1: OVERLAY while writing a restart file
        filab(87*nlabel): character field telling which fields have to be stored
                          for which sets (cf. CalculiX manual for more details).
                          Setting this field to blank suppresses any
                          frd-output
        nlabel: total number of labels.
     */
     // start change DLR
     /* the contents of all variables has to be kept between two calls of
        CalculiXstep, therefore they are declared as static */
   ```

# readinput.c

1. MATERIAL类别包括：

   ```
   *CONDUCTIVITY
   *CREEP
   *CYCLICHARDENING
   *DAMPING
   *ELASTIC
   *DEFORMATIONPLASTICITY
   *DENSITY
   *DEPVAR
   *ELECTRICALCONDUCTIVITY
   *EXPANSION
   *FLUIDCONSTANTS
   *HYPERELASTIC
   *HYPERFOAM
   *MAGNETICPERMEABILITY
   *MATERIAL
   *PLASTIC
   *SPECIFICGASCONSTANT
   *SPECIFICHEAT
   *USERMATERIAL
   ```

# test/compare

1. 官方提供的例子，也可以用于检验编译结果是否正确，类似于abaqus安装完要运行的verification：

   ```shell
   #!/bin/sh
   export OMP_NUM_THREADS=1
   rm -f error.*      #删除掉之前生成的错误文件
   tempfile=temp.$$   #$$表示当前进程的PID，一般用于生成唯一的文件名
   errorfile=error.$$
   #逐个对每个.inp文件进行处理
   for i in *.inp; do
   # 不处理以下.inp文件，因为它们是通过运行其他例子产生的
   	if [ $i = circ10pcent.rfn.inp ]
   	then
   	    continue
   	fi
   	
   	if [ $i = circ10p.rfn.inp ]
   	then
   	    continue
   	fi
   	
   	if [ $i = segmentsmooth.rfn.inp ]
   	then
   	    continue
   	fi
   	
   	if [ $i = segmentsmooth2.rfn.inp ]
   	then
   	    continue
   	fi
   
   	if [ $i = input.inp ] #这是ccx输出的调试文件
   	then
   	    continue
   	fi
   	echo "example ${i%.inp}"
   # 删除掉之前运行产生的对应的.dat和.frd文件
   	rm -f ${i%.inp}.dat  #${i%.inp}表示从变量i的末尾去掉.inp，这句话要删除的是xx.inp对应的xx.dat。
   	rm -f ${i%.inp}.frd
   # 执行Calculix，生成.dat和.frd文件，将命令行输出保存到tempfile文件。需要的话可以修改可执行文件的路径
       ccx -i ${i%.inp} >> $tempfile 2>&1
   # 检查是否生成了对应的.dat和自带的.dat.ref文件是否存在
   	if [ ! -f ${i%.inp}.dat ]; then
   	   echo "${i%.inp}.dat does not exist" >> $errorfile #将错误输出到errorfile中
   	   continue
   	fi
   	if [ ! -f ${i%.inp}.dat.ref ]; then
   	   echo "${i%.inp}.dat.ref does not exist" >> $errorfile
   	   continue
   	fi
   # 检查.dat和.dat.ref这两个文件行数是否一致
   	export sum1=`wc -l ${i%.inp}.dat | awk '{print$1}'`
   	export sum2=`wc -l ${i%.inp}.dat.ref | awk '{print$1}'`
   	if [ $sum1 != $sum2 ]; then
   	   echo "${i%.inp}.dat and ${i%.inp}.dat.ref do not have the same size !!!!!!!!!!" >> $errorfile
   	   echo " ">> $errorfile
   	   continue
   	fi
   # 检查.dat文件中是否存在NaN
   	if grep "NaN" ${i%.inp}.dat ; then
   	   echo "${i%.inp}.dat contains NaN !!!!!!!!!!" >> $errorfile
   	   echo " " >> $errorfile
   	   continue
   	fi
   # 检查.dat和.dat.ref文件中数字的偏差是否在允许范围内，具体由datcheck.pl负责
   	./datcheck.pl ${i%.inp} >> $errorfile
   # 检查.frd和.frd.ref文件是否存在
   	if grep "^ -5" ${i%.inp}.frd >| abc  ||[ -f ${i%.inp}.frd.ref ] ; then
   		if [ ! -f ${i%.inp}.frd ]; then
   			echo "${i%.inp}.frd does not exist" >> $errorfile
   			continue
   		fi
   		if [ ! -f ${i%.inp}.frd.ref ]; then
   			echo "${i%.inp}.frd.ref does not exist" >> $errorfile
   			continue
   		fi
   # 检查.dat和.dat.ref这两个文件行数是否一致
   		export sum1=`wc -l ${i%.inp}.frd | awk '{print$1}'`
   		export sum2=`wc -l ${i%.inp}.frd.ref | awk '{print$1}'`
   		if [ $sum1 != $sum2 ]; then
               echo "${i%.inp}.frd and ${i%.inp}.frd.ref do not have the same size !!!!!!!!!!!!!!!!!!!!!!" >> $errorfile
               echo " ">> $errorfile
               continue
   		fi
   # 检查.dat和.dat.ref文件中数字的偏差是否在允许范围内，具体由frdcheck.pl负责
   	    ./frdcheck.pl ${i%.inp} >> $errorfile
           fi
   done
   rm -f *.rfn.inp #删除掉生成的中间文件
   rm -f $tempfile #删除掉生成的命令行输出文件
   if [ ! -s $errorfile ] #由于前面的命令行，会导致无论是否检出错误，都会生成errorfile。如果错误文件为空，则删除它。
   then
   	rm -f $errorfile
   	echo "Verification Passed!"
   else
   	echo "Verification Not Passed!"
   	echo "Check the errorfile of file $errorfile"
   fi
   ```
   
2. 为test文件夹添加一个Makefile，来清理运行过程中产生的文件：

   ```makefile
   clean:
   	rm -f input.* spooles.out error.*
   	rm -f *.12d *.cvg *.dat *.frd *.sta
   ```


# UMAT

1. 和abaqus不同，ccx的umat不需要在命令行中指定`user=xxx.for`，如果要使用官方自带的umat，可以直接将`*MATERIAL`关键字的NAME参数命名为指定的名称，同时包含`*USER MATERIAL`子关键字，ccx此时会自动调用对应的umat。

   ```shell
   # inp文件中这样使用
   *MATERIAL,NAME=ANISO_PLAS
   *USER MATERIAL,CONSTANTS=15
   500000.,157200.,500000.,157200.,157200.,500000.,126200.,126200.,
   126200.,0.,0.,0.,1.E-10,5,0.
   *DEPVAR
   14
   ```

2. 上述流程在`umat_main.f`中规定。

   ```fortran
         elseif(amat(1:10).eq.'ANISO_PLAS') then
            amatloc(1:70)=amat(11:80)
            amatloc(71:80)='          '
            call umat_aniso_plas(amatloc,
        &        iel,iint,kode,elconloc,emec,emec0,
        &        beta,xikl,vij,xkl,vj,ithermal,t1l,dtime,time,ttime,
        &        icmd,ielas,mi(1),nstate_,xstateini,xstate,stre,stiff,
        &        iorien,pgauss,orab,nmethod,pnewdt)
   ```

3. 


# 变量

1. ccx_2.20.c文件开头的部分：

   ```c
   FILE *f1 = NULL; //公用的一个文件流指针
   char *sideload = NULL,
        *set = NULL,
        *matname = NULL,
        *orname = NULL,
        *amname = NULL,
        *filab = NULL,
        *lakon = NULL,
        *labmpc = NULL,
        *prlab = NULL,
        *prset = NULL,
         jobnamec[792] = "", //132*6个字符，直接拷贝完-i的参数，后续的都是\0，是C风格的字符串。
         jobnamef[132] = "", //同样拷贝-i的参数，不够132个字符的部分都会被填充成空格
         tmpjobname[132] = "",
         output[5] = "",
        *typeboun = NULL,
        *inpc = NULL, //包含简化后的inp文件的内容，去掉了换行，通过
        *tieset = NULL,
        *cbody = NULL,
         fneig[132] = "",
        *sideloadtemp = NULL,
         kind1[2] = "",
         kind2[2] = "",
        *heading = NULL,
        *objectset = NULL;
   
   ITG *kon = NULL,
       *nodeboun = NULL,
       *ndirboun = NULL,
       *ipompc = NULL,
       *nodempc = NULL,
       *nodeforc = NULL,
       *ndirforc = NULL,
       *nelemload = NULL,
        im = 0,
       *inodesd = NULL,
        nload1 = 0,
       *idefforc = NULL,
       *nactdof = NULL,
       *icol = NULL,
       *ics = NULL,
        itempuser[3] = {0},
       *jq = NULL,
       *mast1 = NULL,
       *irow = NULL,
       *rig = NULL,
       *idefbody = NULL,
       *ikmpc = NULL,
       *ilmpc = NULL,
       *ikboun = NULL,
       *ilboun = NULL,
       *nreorder = NULL,
       *ipointer = NULL,
       *idefload = NULL,
       *istartset = NULL,
       *iendset = NULL,
       *ialset = NULL,
       *ielmat = NULL,
       *ielorien = NULL,
       *nrhcon = NULL,
       *nodebounold = NULL,
       *ndirbounold = NULL,
       *nelcon = NULL,
       *nalcon = NULL,
       *iamforc = NULL,
       *iamload = NULL,
       *iamt1 = NULL,
       *namta = NULL,
       *ipkon = NULL,
       *iamboun = NULL,
       *nplicon = NULL,
       *nplkcon = NULL,
       *inotr = NULL,
       *iponor = NULL,
       *knor = NULL,
       *ikforc = NULL,
       *ilforc = NULL,
       *iponoel = NULL,
       *inoel = NULL,
       *nshcon = NULL,
       *ncocon = NULL,
       *ibody = NULL,
       *ielprop = NULL,
       *islavsurf = NULL,
       *ipoinpc = NULL, //整数数组，nline个元素，存储着inp文件中的每一行的开头在inpc字符数组中的下标。
        mt = 0,
        nxstate = 0,
        nload0 = 0,
        iload = 0,
       *iuel = NULL,
       *ne2boun = NULL,
       *irandomtype = NULL,
        irobustdesign[3] = {0},
       *iparentel = NULL,
        ifreebody = 0,
       *ipobody = NULL,
        inewton = 0,
       *iprfn = NULL,
       *konrfn = NULL;
   ITG  nk = 0,
        ne = 0,
        nboun = 0, //约束的自由度总数，整型
        nmpc = 0,
        nforc = 0,
        nload = 0,
        nprint = 0,
        nset = 0,
        nalset = 0,
        nentries = 18, //需要按照顺序解析的关键字组
        nmethod = 0,
        neq[3] = {0},
        i = 0,
        mpcfree = 0,
        mei[4] = {0},
        j = 0,
        nzl = 0,
        nam = 0,
        nbounold = 0,
        nforcold = 0,
        nloadold = 0,
        nbody = 0,
        nbody_ = 0,
        nbodyold = 0,
        network = 0,
        nheading_ = 0,
        k = 0,
        nzs[3] = {0},
        nmpc_ = 0,
        nload_ = 0,
        nforc_ = 0,
        istep = 0,
        istat = 0,
        nboun_ = 0,
        nintpoint = 0,
        iperturb[2] = {0},
        nmat = 0,
        ntmat_ = 0,
        norien = 0,
        ithermal[2] = {0}, //热力耦合的情况，这个参数不是从属于某个特定的分析步，而是整个分析的，而且它的取值和关键字出现的顺序有关。
   // 如果只有这3个力学分析步的关键字（*STATIC，*VISCO或*DYNAMIC），则ithermal[1]为0或1(如果*INITIALCONDITIONS包含TYPE=TEMPERATURE参数)。
   // 如果只有*HEATTRANSFER关键字，则ithermal[1]=2。
   //如果先是力学分析步关键字，后是热传导关键字，则ithermal[1]=2或3(如果*INITIALCONDITIONS包含TYPE=TEMPERATURE参数)。
   // 如果先是热传导关键字，后是力学分析步关键字，则ithermal[1]=3。
   // 如果包含*COUPLEDTEMPERATURE-DISPLACEMENT，则ithermal[1]=3。
   // 如果包含*UNCOUPLEDTEMPERATURE-DISPLACEMENT，则ithermal[1]=3。
   // 如果包含*ELECTROMAGNETICS，则ithermal[1]=3。
        nmpcold = 0,
        iprestr = 0,
        kode = 0,
        isolver = 0,
        nslavs = 0,
        nkon_ = 0,
        ne0 = 0,
        nkon0 = 0,
        mortar = 0,
        jout[2] = {0},
        nlabel = 0,
        nkon = 0,
        idrct = 0,
        jmax[2] = {0},
        iexpl = 0,
        nevtot = 0,
        ifacecount = 0,
        iplas = 0,
        npmat_ = 0,
        mi[3] = {0}, //mi(1)为单元的积分点个数，mi(2)为每个节点的自由度个数，mi(3)为单元的层数，复合材料中使用。
        ntrans = 0,
        mpcend = 0,
        namtot_ = 0,
        iumat = 0,
        iheading = 0,
        icascade = 0,
        maxlenmpc = 0,
        mpcinfo[4] = {0},
        ne1d = 0,
        ne2d = 0,
        infree[4] = {0},
        callfrommain = 0,
        nflow = 0,
        jin = 0, //记录命令行参数中-i的个数，处理完命令行会检测，如果为0，则表示没有-i参数，会将第1个参数当作jobname。
        irstrt[2] = {0},
        nener = 0,
        jrstrt = 0,
        nenerold = 0,
        nline = 0, //整个inp文件经过简化后的总行数。
       *ipoinp = NULL,//2*nentries个元素的数组，可以认为是nentries行，2列的数组，每一行的第0列表示在该类在inp数组中的起始行号，第1列表示该类在inp数组中的结束行号。
       *inp = NULL, //存储inp_size个元素，可以当作inp_size/3行，3列的数组，存储一个链状数据，同类的行都在同一个链上。
        ntie = 0,
        ntie_ = 0,
        mcs = 0,
        nprop_ = 0,
        nprop = 0, //属性的个数，整型
        itpamp = 0,
        iviewfile = 0,
        nkold = 0,
        nevdamp_ = 0,
        npt_ = 0,
        cyclicsymmetry = 0,
        nmethodl = 0,
        iaxial = 0,
        inext = 0,
        icontact = 0,
        nobject = 0,
        nobject_ = 0,
        iit = 0,
        nzsprevstep[3] = {0},
        memmpcref_ = 0,
        mpcfreeref = 0,
        maxlenmpcref = 0,
       *nodempcref = NULL,
       *ikmpcref = NULL,
        isens = 0,
        namtot = 0, //amplitude的总数据点个数。*AMPLITUDE的一个数据行最多4个数据点。
        nstam = 0,
        ndamp = 0,
        nef = 0,
        inp_size = 0, //存储inp数组的元素个数
       *ipoinp_sav = NULL, //ipoinp数组的备份
       *inp_sav = NULL, //inp数组的备份
        irefineloop = 0,
        icoordinate = 0,
       *nodedesi = NULL,
        ndesi = 0,
        nobjectstart = 0,
        nfc_ = 0,
        ndc_ = 0,
        nfc = 0,
        ndc,
       *ikdc = NULL;
   
   
   ITG *meminset = NULL, //存储着set数组中对应的集合中的元素个数，整型数组。meminset(i)表示第i个set中元素的个数。
       *rmeminset = NULL; //缩减的元素个数，使用了generate的造成的，整型数组。
   ITG  nzs_ = 0,
        nk_ = 0,
        ne_ = 0,
        nset_ = 0, //逐行解析inp文件得到的set的数量，包括*ELEMENT，*ELSET，*NODE，*NSET，*SURFACE，*SUBMODEL关键字，其中1个*SUBMODEL关键字会增加2个set。
        nalset_ = 0,
        nmat_ = 0,
        norien_ = 0,
        nam_ = 0, //!amplitude的计数
        ntrans_ = 0,
        ncs_ = 0,
        nstate_ = 0,
        ncmat_ = 0,
        memmpc_ = 0,
        nprint_ = 0,
        nuel_ = 0; //用户自定义单元的种类，也就是*USERELEMENT关键字的出现次数。
   
   double *co = NULL,
          *xboun = NULL,
          *coefmpc = NULL,
          *xforc = NULL,
          *clearini = NULL,
          *xload = NULL,
          *xbounold = NULL,
          *xforcold = NULL,
          *randomval = NULL,
          *vold = NULL,
          *sti = NULL,
          *xloadold = NULL,
          *xnor = NULL,
          *reorder = NULL,
          *dcs = NULL,
          *thickn = NULL,
          *thicke = NULL,
          *offset = NULL,
          *elcon = NULL,
          *rhcon = NULL,
          *alcon = NULL,
          *alzero = NULL,
          *t0 = NULL,
          *t1 = NULL,
          *prestr = NULL,
          *orab = NULL,
          *amta = NULL,
          *veold = NULL,
          *accold = NULL,
          *t1old = NULL,
          *eme = NULL,
          *plicon = NULL,
          *pslavsurf = NULL,
          *plkcon = NULL,
          *xstate = NULL,
          *trab = NULL,
          *ener = NULL,
          *shcon = NULL,
          *cocon = NULL,
          *cs = NULL,
          *tietol = NULL,
          *fmpc = NULL,
          *prop = NULL,
          *t0g = NULL,
          *t1g = NULL,
          *xbody = NULL,
          *xbodyold = NULL,
          *coefmpcref = NULL,
          *dacon = NULL,
          *vel = NULL,
          *velo = NULL,
          *veloo = NULL,
          energy[5] = {0},
          *ratiorfn = NULL,
          *dgdxglob = NULL,
          *g0 = NULL,
          *xdesi = NULL,
          *coeffc = NULL,
          *edc = NULL;
   
   double ctrl[57] = {0};
   double fei[3] = {0},
         *xmodal = NULL,
          timepar[5] = {0},
          alpha[2] = {0},
          ttime,
          qaold[2] = {0},
          physcon[14] = {0};
   double totalCalculixTime = 0.0; //
   ```

2. 


# test

1. 测试例子：

   ```shell
   achtel2.inp  # equations with 2 terms
   achtel29.inp # mixture of equations with 2 and 9 terms
   achtel9.inp  # equations with 9 terms
   achtelc.inp
   ```

2. 对应的Makefile：

   ```makefile
   clean:
   	rm -f *.sta *.frd *.out *.12d *.cvg *.dat
   	rm -f *.eig *.nam input*  abc temp* error*
   	rm -f *.equ *.rout *.net *.fbd *.stm *.mtx
   ```

# BUG记录

1. 运行`ccx -i beamd10dy`时，会在文件`steadystatedynamicss.f`中报告段错误。不过此inp文件中并没有*CYCLIC SYMMETRY MODEL关键字。同样的问题也出现在`complexfrequencys.f`和`modaldynamics.f`。

   ```fortran
   if((mcs.ne.0).and.(cs(2,1).ge.0.d0)) then !观察到在此之前，从未给cs分配空间，因此这里的调用会报错。实际上这里mcs为0，and的第一部分已经为假了，因此不应该进行cs取值。
       cyclicsymmetry=1
   endif
   ... !问题同上，可以将这两段注释掉，这样运行该例子可以成功，但是会导致无法正确处理循环对称的情况。
   if((cyclicsymmetry.eq.1).and.(mcs.ne.0).and.(cs(2,1)<0.d0))
   &         cs(2,1)=0.d0
   !有两种解决方法：手动进行短路逻辑操作，或者为为cs分配空间，然后收回即可，后者会更改逻辑，可能引入新的bug，因此推荐前者。
   if(mcs.ne.0) then
       if(cs(2,1).ge.0.d0) then
           cyclicsymmetry=1
       endif
   endif
   ...
   if ((cyclicsymmetry.eq.1).and.(mcs.ne.0)) then
       if(cs(2,1)<0.d0) then
           cs(2,1)=0.d0
       endif
   endif
   ```

2. 同上，在calinput.f中也存在类似的情况，但是这个逻辑表达式非常复杂，因此推荐使用另一种方法：

   ```fortran
   if((nmethod.eq.1).or.(nmethod.eq.3).or.(nmethod.eq.4).or.((nmethod.eq.2).and.((mcs.eq.0).or.(cs(2,1).lt.0)))) then
   ...
   endif
   !改为如下，将原来的语句块，用如下if包括起来，loc是获取变量的地址，如果为0表示未分配空间，因此不能进行cs(2,1)操作。
   if (loc(cs).ne.0) then
   ...
   endif
   ```

3. 同上，`extrapolatefem.f,extrapolate.f,extrapolate_se.f`。

   ```fortran
   if (loc(ielorien).ne.0) then
       if((iorienloc.ne.0).and.(ielorien(1,i).ne.0)) then
   
       endif
   endif
   ```



# 文件分类

1. 所有带main的函数，都是为了并行计算而创造的，分配任务，调用对应的功能函数。

2. 处理所有关键字的函数应该都放到前处理文件夹中。

3. 分析ccx_2.20.c的架构。

4. 工具函数分为：

   ```shell
   # 系统功能
   getSystemCPUs,stop,exit,stopwithout201,closefile,openfile,getversion,u_free,u_calloc,u_realloc,u_malloc,dattime
   #输入
   getnewline,inputwarning,inputerror,inputinfo,strcpy1,strcmp1,strcmp2,stoi,stof,stos,splitline,compare,strsplt,frecord,
   #输出
   writeturdir,writemaccs,writemac,writeheading,writeevcscomplex,writeevcomplex,writeev,writeview,writestadiv,writesta,writeim,writeboun,writebv,writepf,writeevcs,writeturdircs,writeelem,writeinput,writematrix,writempc,writevector,writere,writehe,frdheader
   #查找位置插入
   cident81,nidentk,nidentll,ident2,identamta,nident2,ident,nident,
   #排序
   dsort,bsort,dsort,insertsortd,insertsorti,isortic,isortiddc,isortid,isorti,isortiiddc,isortiid,isortii,isortiii,qsorti,
   #形函数，特点是不会调用其他函数，但是会被其他函数大量调用
   shape10tet,shape15w,shape20h_ax,shape20h,shape20h_pl,shape2l,shape3l,shape3tri,shape4q,shape4tet,shape6tri,shape6tritilde,shape6tritilde_lin,shape6w,shape7tri,shape8h,shape8hr,shape8hu,shape8humass,shape8q,shape8qtilde,shape8qtilde_lin,shape9q,evalshapefunc,dualshape3tri,dualshape4q,dualshape6tritilde,dualshape6tritilde_lin,dualshape8qtilde,dualshape8qtilde_lin,
   #几何操作
   near2d,near3d,attach_1d,attach_2d,attach_3d,attachline,straighteq3d,straighteq3dpen,straighteq2d,approxplane,neartriangle,plane_eq,planeeq,getlocno,getnumberofnodes,eplane,
   #外部库中的矩阵计算
   ddot,dscal,dswap,dgesv,ddebdf,ddeabm,dgmres,dgmres1,drfftf,dlzhes,dlzit,dsptrf,dsptri,dgetrs,drffti,cubtri,daxpy,dcopy,xermsg,hybsvd,rs,cgsolver,
   #作者编写的矩阵计算，坐标变换
   op,opas,op_corio,opnonsymt,opnonsym,transformatrix,addimd,modf,add_rect,mult,multvec,multi_rect,multi_rectv,mulmatvec_asym,machpi,matvec,insert,transpose,insertas_ws,insertas,calceigenvalues,matrixsort
   #CFD相关
   topocfdfem,rearrangecfd,flux,orifice,moehring,ts_calc,initialchannel,initialnet,resultnet,flowoutput,gapcon,
   #重要的函数入口，后续会调用一堆函数，omit这些只是为了减少调用图的复杂度
   umat_main,e_c3d_u,extrapolate_u,resultsmech_u,calinput
   ```

5. 还需要对循环对称，1d/2d扩展为3d进行单独处理。

6. 和传热有关的都保留，例如辐射，但是和流动有关的都删除，例如孔口，渠道，CFD。

7. 应该将请求的结果存储在一个结构化的数据对象中，然后输出成文本或二进制文件。

8. arpack有三个变体，arpack，arpackbu（屈曲），arpackcs（循环对称）

9. 使用Egypt对源码目录处理：

   ```shell
   # -callees main 选项能够只显示从main调用的文件。忽略一些工具函数等。
   egypt *.expand -callees main --omit  getSystemCPUs,stop,exit,stopwithout201,closefile,openfile,getversion,u_free,u_calloc,u_realloc,u_malloc,dattime,getnewline,inputwarning,inputerror,inputinfo,strcpy1,strcmp1,strcmp2,stoi,stof,stos,splitline,compare,strsplt,writeturdir,writemaccs,writemac,writeheading,writeevcscomplex,writeevcomplex,writeev,writeview,writestadiv,writesta,writeim,writeboun,writebv,writepf,writeevcs,writeturdircs,writeelem,writeinput,writematrix,writempc,writevector,writere,writehe,frdheader,cident81,nidentk,nidentll,ident2,identamta,nident2,ident,nident,dsort,bsort,dsort,insertsortd,insertsorti,isortic,isortiddc,isortid,isorti,isortiiddc,isortiid,isortii,isortiii,qsorti,shape10tet,shape15w,shape20h_ax,shape20h,shape20h_pl,shape2l,shape3l,shape3tri,shape4q,shape4tet,shape6tri,shape6tritilde,shape6tritilde_lin,shape6w,shape7tri,shape8h,shape8hr,shape8hu,shape8humass,shape8q,shape8qtilde,shape8qtilde_lin,shape9q,evalshapefunc,dualshape3tri,dualshape4q,dualshape6tritilde,dualshape6tritilde_lin,dualshape8qtilde,dualshape8qtilde_lin,near2d,near3d,attach_1d,attach_2d,attach_3d,attachline,straighteq3d,straighteq3dpen,straighteq2d,approxplane,neartriangle,plane_eq,planeeq,getlocno,getnumberofnodes,eplane,ddot,dscal,dswap,dgesv,ddebdf,ddeabm,dgmres,dgmres1,drfftf,dlzhes,dlzit,dsptrf,dsptri,dgetrs,drffti,cubtri,daxpy,dcopy,xermsg,hybsvd,rs,cgsolver,op,opas,op_corio,opnonsymt,opnonsym,transformatrix,addimd,modf,add_rect,mult,multvec,multi_rect,multi_rectv,mulmatvec_asym,machpi,matvec,insert,transpose,insertas_ws,insertas,calceigenvalues,matrixsort,topocfdfem,rearrangecfd,flux,orifice,moehring,ts_calc,initialchannel,initialnet,resultnet,flowoutput,gapcon,umat_main,e_c3d_u,extrapolate_u,resultsmech_u,calinput | dot -Gsize=8.5,11 -Grankdir=LR -Tpdf -o callgraph.pdf
   
   #删除如下文件，确认为非必须文件
   rm crackpropagation.c.245r.expand
   rm robustdesign.c.245r.expand
   rm refinemesh.c.245r.expand
   rm readnewmesh.c.245r.expand
   rm sensi_coor.c.245r.expand
   rm sensi_orien.c.245r.expand
   rm feasibledirection.c.245r.expand
   rm compfluidfem.c.245r.expand
   rm objectivemain_se.c.245r.expand
   rm electromagnetics.c.245r.expand
   rm objective_shapeener_dx.f90.245r.expand
   rm printoutfluidfem.f90.245r.expand
   rm mafillnet.f90.245r.expand
   rm labyrinth.f90.245r.expand
   rm film.f90.245r.expand
   rm envtemp.f90.245r.expand
   ```

10. 所有的文件：

   ```shell
   absolute_relative.f90 #孔口单元
   acctube.f90 #ACC tube单元，在flux.f90中调用
   acctube_one.f90 #同上
   actideacti.f90 #激活/取消激活set中的单元，在敏感性计算objectivemain_se中调用
   actideactistr.f90 # 停用与STRESS目标函数集合中的节点不相邻的单元，同上。
   add_bo_st.f90 #在稀疏矩阵格式的刚度矩阵的(i,j)位置存储上值为value的边界刚度系数。
   addimd.f90 #将实体node添加到字段imd中，
   addimdnodecload.f90 #添加用户定义的集中力施加到imdnode的自由度
   addimdnodedload.f90 #添加用户定义的面力施加到imdnode的自由度
   addimdnodedof.f90 #节点由用户在模态动力学计算中保存
   addizdofcload.f90 #将施加集中力的自由度添加到iznode、izdof，如果用户自定义负载，也添加到imdnode
   addizdofdload.f90 #将属于面力的节点施加到iznode、izdof，如果用户自定义负载，也添加到imdnode
   add_rect.c #计算稀疏矩阵A,B的加法
   addshell.f90 #更新真实壳体的平移和旋转自由度
   add_sm_ei.f90 #刚度矩阵以系数矩阵格式存储，质量矩阵以集中质量矩阵格式存储。会在稀疏矩阵填充的mafill系列函数中被调用。
   add_sm_fl.f90 #存储流体矩阵的系数
   add_sm_st.f90 #在稀疏矩阵格式的刚度矩阵的(i,j)位置存储上值为value的刚度系数。
   add_sm_st_as.f90 #同上
   add_sm_st_corio.f90 #为科里奥利力修正，此矩阵是反对称的。
   adjacentbounodes.f90 #根据邻接性对裂纹边界节点进行排序
   adjustcontactnodes.f90 #如果用户要求，调整接触节点
   advecforc.f90 #计算对流单元的刚度，对流单元由具有强制对流膜条件的face和网络节点组成
   advecstiff.f90 #同上
   air_valve.f90 #私有功能
   allocation.f90 #读取inpc,依次处理每个关键字及其参数和数据行,预估一下每个域需要分配的空间大小
   allocation_rfn.f90 #同上
   allocont.f90 #计算对接触主曲面进行三角剖分所需的三角形数量
   amplitudes.f90 #读取关键字*AMPLITUDE
   angsum.f90 #计算与节点相邻的单元边的所有空间角之和。内部还包含一个工具函数spaceangle，计算法向量
   anisomaxwavspd.f90 #计算各向异性材料的波速，最多可达21个常数
   anisonl.f90 #替换e_c3d.f90中关于各向异性材料的内容。
   anisotropic.f90 #将21个各向异性弹性常数展开为3x3x3x3矩阵，也就是四阶张量
   applybounfem.f90 #将温度和速度SPC应用于不可压缩流体
   applybounp.f90 #应用速度边界条件
   approxplane.f90 #计算穿过四边形边缘并平行于向量xn的平面，以及垂直于xn并穿过四边形四角点重心的平面的方程
   arpackbu.c #屈曲程序；仅适用于机械应用
   arpack.c #调用Arnoldi包（ARPACK），在ccx_2.20.c中调用
   arpackcs.c #调用Arnoldi包（ARPACK）进行循环对称计算
   assigndomtonodes.f90 #将节点所属的域分配给此节点，电磁计算用到
   attach_1d.f90 #将节点附着到曲线上，曲线由最多9个节点表示。会找出曲线上距离最近的点的距离和参数坐标，还有所有节点的权重。
   attach_2d.f90 #将节点附着到face上，
   attach_3d.f90 #同上
   attachline.f90 #返回一个面和直线交点的局部坐标。
   auglag_inclusion.f90 #接触相关，在massless中调用。
   autocovmatrix.f90 #计算自协方差矩阵的值
   basemotions.f90 #读取关键字*BASE MOTION
   basis.f90 #将场从主网格插值到任意位置p处的新节点上。
   bdfill.c #计算耦合矩阵B_d和d_d，并将其插入数据结构中
   beamextscheme.f90 #为横截面既不是矩形也不是椭圆形的梁提供了外推方案
   beamgeneralsections.f90 #读取*BEAM SECTION关键字，对于PIPE,BOX,GENERAL类型的截面
   beamintscheme.f90 #提供非矩形或椭圆截面的梁的积分格式
   beammpc.f90 #为彼此保持恒定距离的两个节点生成MPC。
   beamsections.f90 #读取关键字*BEAM SECTION
   biosav.c #计算电磁计算中phi域电流引起的磁强度
   biotsavart.f90 #同上
   bodyadd.f90 #将体积dload条件添加到数据库中
   bodyforce.f90 #通过ipobody域，将体积力施加给单元
   bounadd.f90 #将一个边界条件添加到数据库中
   bounaddf.f90 #添加一个面力边界条件到数据库中
   boundaryfs.f90 #读取关键字*BOUNDARYF，CFD计算使用
   boundarys.f90 #读取关键字*BOUNDARY
   bsort.f90 #桶排序，内部调用了快速排序qsort
   buckles.f90 #读取关键字*BUCKLE
   buildtquad.c #计算四元法或四元林法的变换矩阵T和T^{-1}，在inimotar中调用
   calcdatarget.f90 #计算裂纹扩展增量
   calcdev.f90 #计算解的变化，CFD中使用
   calcdhds.f90 #计算管道中的摩擦系数
   calceigenvalues.f90 #计算对称3x3矩阵al的特征值，特征值按升序排序
   calcenergy.f90 #在*DYNAMIC计算中计算能量
   calcexternalwork.f90 #计算和打印升力和阻力
   calcgeomelemnet.f90 #用户子程序计算柔性网络单元和用户定义网络单元的横截面
   calch0interface.f90 #电磁计算使用
   calcheatnet.f90 #用户子程序film
   calc_ider_cross_split.f90 #计算cross_split导数，在交叉单元cross_split中调用
   calc_residual_cross_split.f90 #计算cross_split残差
   calc_ider_tee.f90 #计算tee导数，在T型三通tee中调用
   calc_residual_tee.f90 #计算tee残差
   calc_ider_wye.f90 #计算wye导数，在Y型三通wye中调用
   calc_residual_wye.f90#计算wye残差
   calcmac.f90 #计算模态保证标准MAC
   calcmach.f90 #计算绝热系数和马赫数
   calcmass.f90 #计算单元的质量
   calcmechstrain.f90 #根据位移梯度和热拉伸计算机械应变
   calcnormal.f90 #确定单元的某个面上的局部法线。
   calcresidual.c #计算残差
   calcresidual_em.c #计算残差，用于电磁计算
   calcshapef.c #确定流体网格的形函数及其导数
   calcspringforc.f90 #计算弹簧力和弹簧能量（node-to-face罚方法）
   calcstabletimeinccont.f90 #根据显式动力学计算的库朗准则计算接触弹簧单元的临界时间增量（CTI）
   calcstabletimeincvol.f90 #计算材料中的传播波速，在各向同性、单晶和各向异性材料之间选择适当的程序。
   calcstressheatfluxfem.f90 #计算积分点处的粘性应力和热流（CBS法）
   calcsurf.f90 #计算由节点n1、n2和n3组成的四面体面的表面
   calctotstrain.f90 #根据位移梯度计算总应变
   calculated.f90 #确定实际网格中所有边的长度
   calculateh.f90 #计算原始网格所有节点中h的期望大小
   calculatehmid.f90 #计算所有中间节点中h的期望大小
   CalculiX.h #所有单元的头文件
   calcview.f90 #辐射计算使用
   calcvol.f90 #计算具有节点n1、n2、n3和n4的四面体单元的体积
   calinput.f90 #处理inp文件，为每个关键字单独调用程序处理
   calinput_rfn.f90 #同上
   call_external_umat.c #调用外部umat
   call_external_umat_user.c #同上
   carbon_seal.f90 #碳密封单元，会在flux中调用
   cascade.c #检测MPC，然后拆解它们
   catedges_crackprop.f90 #对网格四面体单元的边进行编目，crackpropagation会调用
   catedges_refine.f90 #同上，refinemesh会调用
   catnodes.f90 #根据节点所属的未细化网格中的锐边数量对节点进行编目，refinemesh会调用
   catsmpcslavno.f90 #为mortar接触所需的主节点和从节点编目SPC和MPC
   cattet.f90 #对网格的四面体单元进行编目，refinemesh会调用
   cattri.f90 #同上
   cavityext_refine.f90 #refinemesh会调用
   cavity_refine.f90 #同上
   ccx_2.20.c #主程序，main函数所在地
   cd_bleedtapping.f90 #航空发动机二次空气系统的仿真，orifice中调用
   cd_bragg.f90 #同上
   cd_chamfer.f90 #同上
   cd_lab_1spike.f90 #在labyrinth中调用
   cd_lab_correction.f90 #同上
   cd_lab_honeycomb.f90 #同上
   cd_lab_radius.f90 #同上
   cd_lab_straight.f90 #同上
   cd_lichtarowicz.f90 #孔口相关
   cd_Mcgreehan_Schotsch.f90 #在labyrinth中调用
   cd_ms_ms.f90 #同上
   cd_own_albers.f90 #同上
   cd_pk_albers.f90 #同上
   cd_pk_ms.f90 #同上
   cd_preswirlnozzle.f90 #同上
   cfdconv.f90 #计算解的变化，CFD应用。
   cfds.f90 #读取关键字*CFD
   cflux.f90 #用户子程序cflux
   cfluxs.f90 #读取关键字*CFLUX
   changedepterm.f90 #更改MPC中的依赖项
   changefrictions.f90 #读取关键字*CHANGE FRICTION
   changekon.f90 #对于复合材料，必须改变连接方式，以允许复合材料元件的多次扩展
   changematerials.f90 #读取关键字*CHANGE MATERIAL
   changeplastics.f90 #读取关键字*CHANGE PLASTIC
   changesolidsections.f90 #读取关键字*CHANGE SOLID SECTION
   changesurfacebehaviors.f90 #读取关键字*CHANGE SURFACE BEHAVIOR
   characteristic.f90 # CFD计算使用
   characteristiclength.f90 #裂缝开展相关
   checkconstraint.f90 #根据约束的函数值检查哪些约束处于活动状态
   checkconvergence.c #检查收敛
   checkconvnet.c #辐射计算相关，和radflowload相关
   checkdivergence.c #检查radflowload.c中是否发出发散信号
   checkexiedge.f90 #检查由节点n1和n2（n1<n2）组成的边是否仍然存在
   checkforhomnet.f90 #检查（简单与否）连接的网络是否不均匀，network elements使用
   checkimpacts.f90 #包含在接触条件下规则增量大小的逻辑实现的例程
   checkinclength.c #检查动态分析的增量大小
   checkinputvaluesnet.f90 #CFD相关
   checkintegrity.f90 #目前没有任何函数调用
   checkjac.f90 #检查所有单元的所有积分点中的雅可比矩阵
   checkprojectgrad.f90 #检查拉格朗日乘子，如果可能的话减少活动约束的数量，并更新线性约束的响应函数值
   checksharp.f90 #refinemesh相关
   checkspcmpc.f90 #检查从属节点中的SPC和MPC是否与mortar接触兼容
   checktemp.f90 #检查对于具有温度条件的力学计算，是否为属于某个元素的每个节点分配了初始和最终温度
   checktime.f90 #检查tmin是否不超过第一个时间点，以防时间点振幅处于活动状态
   checktruecontact.f90 #检查face-to-face罚接触的表面行为定义是否定义了真正的接触，而不仅仅是tie
   checkvol.f90 #如果node的坐标从cotet(1..3,node)更改为pnew(1..3)，则检查属于“node”所有元素的体积
   chksurf.f90 #检查面，在zienzhu中调用，逐点误差估计器。
   cident.f90 #标识px在有序整数数组x中的位置id
   cident80.f90 #同上，x为字符串(长度80)数组
   cident81.f90 #同上，x为字符串(长度81)数组
   clearances.f90 #读取关键字*CLEARANCE
   cloaddistributing.f90 #在属于分布面的节点之间分配分布负载
   cload.f90 #用户子程序cload
   cloads.f90 #读取关键字*CLOADS
   clonesensitivities.f90 #敏感性分析使用
   closefile.f90 #计算结束时关闭文件
   closefilefluid.f90 #关闭流体相关的文件
   cmatrix.f90 #计算C矩阵的值
   combilcfhcf.f90 #疲劳组合，裂纹扩展中使用
   compare.c #比较字符串
   compdt.f90 #确定每个节点的时间步长，CFD使用
   compfluidfem.c #CFD计算的主程序
   complexfreq.c #从实本征模合成复本征模
   complexfrequencys.f90 #读取关键字*COMPLEX FREQUENCY
   con2phys.f90 #根据守恒变量计算物理变量
   condrandomfield.f90 #随机场计算用到
   conductivitys.f90 #读取关键字*CONDUCTIVITY
   constraints.f90 #读取关键字*CONSTRAINT
   contact.c #接触计算
   contactdampings.f90 #读取关键字*CONTACT DAMPING
   contactmortar.c #在变换后的系统中包括双motar接触法的接触条件
   contactpairs.f90 #读取关键字*CONTACT PAIR
   contactprints.f90 #读取关键字*CONTACT PRINT
   contingentsurf.f90 #确定由于偶然自由面附近引起的K因子的增加，裂缝相关
   contraction.f90 #处理通道单元
   controlss.f90 #读取关键字*CONTROLS
   convert2rowbyrow.c #矩阵操作，CFD使用
   coriolissolve.f90 #求解科里奥利力引起的复本征频率
   correctem.f90 #校正谐波电流电场的实部和虚部，电磁分析
   correlationlengths.f90 #读取关键字*CORRELATION LENGTH
   couplings.f90 #读取关键字*COUPLING，配合*KINEMATIC 或 *DISTRIBUTING
   couptempdisps.f90 #读取关键字*COUPLED TEMPERATURE-DISPLACEMENT
   cp_corrected.f90 #计算校正的cp，传热计算需要
   cpypardou.c #并行拷贝浮点数组
   cpyparitg.c #并行拷贝整数数组
   crackfrd.c #将裂缝信息存储为frd格式
   cracklength.f90 #裂缝计算相关
   cracklength_smoothing.f90 #平滑裂缝长度
   crackpropagation.c #同上
   crackpropagations.f90 #同上
   crackpropdata.c #读取裂缝扩展数据
   crackprop.f90 #裂缝计算相关
   crackrate.f90 #计算裂纹扩展速率和该增量的循环次数
   crackshape.f90 #确定每个裂纹前缘节点的形状系数
   createbd.f90 #创建耦合矩阵，接触相关
   createblock_struct.f90 #创建块结构，gmres相关
   create_contactdofs.f90 #无质量动态接触
   createelemneigh.f90 #确定节点i的相邻单元的目标节点所属的所有单元，目标优化相关
   createfint.f90 #所有主动自由度内力矢量的计算
   createialnk.f90 #确定属于节点i的单元。
   createinterfacempcs.f90 #电磁分析相关
   createinum.f90 #在inp中不需要外推的情况下确定inum
   createlocalsys.f90 #在裂纹前缘创建局部坐标系
   createmddof.f90 #创建一组imddof，其中包含用户为模态动态计算选择的自由度
   createmdelem.f90 #存储请求结果的单元，节点等
   createnodeneigh.f90 #确定所有目标节点
   createtele.f90 #为quad-quad mortar生成局部坐标变换矩阵
   createteleinv.f90 #逆
   createtele_lin.f90 #quad-lin mortar method
   createteleinv_lin.f90 #逆
   createtet.f90 #remesh相关
   createtiedsurfs.f90 #为电磁计算域之间的曲面创建联系
   creep.f90 #用户子程序 蠕动
   creeps.f90 #读取关键字*CREEP
   cross_split.f90 #十字型单元，CFD相关
   cubic.f90 #三次方程公式解
   cubtri.f90 #三角形上的自适应求积
   cyclichardenings.f90 #读取关键字*CYCLIC HARDENING
   cyclicsymmetrymodels.f90 #读取关键字*CYCLIC SYMMETRY MODEL
   dam1parll.c #阻尼力计算的并行化
   dam2parll.c #同上
   dampings.f90 #读取关键字*DAMPING
   dashdamp.f90 #计算阻尼器的阻尼系数
   dashpots.f90 #读取关键字*DASHPOT
   dattime.f90 #在Fortran中获取日期和时间
   ddeabm.f90 #用adams-bashforth方法求解常微分方程的初值问题
   ddebdf.f90 #用逆微分公式求解常微分方程的初值问题
   dealloc_cal.c #释放内存计算
   decascade_mortar.c #解耦生成的变换MPC
   deformationplasticitys.f90 #读取关键字*DEFORMATION PLASTICITY
   defplas.f90 #为变形塑性材料计算刚度和应力
   delaun.f90 #delauny三角剖分
   deltri.f90 #三角化
   densitys.f90 #读取关键字*DENSITY
   depvars.f90 #读取关键字*DEPVAR
   designresponses.f90 #读取关键字*DESIGN RESPONSE
   designvariabless.f90 #读取关键字*DESIGN VARIABLES
   desiperelem.f90 #存储每个单元的设计变量
   detectactivecont.f90 #接触相关
   determineextern.f90 #确定哪些面、边和节点是外部的
   dfdbj.c #目前没有被调用
   dflux.f90 #用户子程序dflux
   dfluxs.f90 #读取关键字*DFLUX
   dgesv.f90 #求解一般实矩阵的线性方程组
   dgmres.f90 #预处理GMRES迭代稀疏Ax=b求解器
   dgmres1.f90 #同上
   dgmresmain.c #dgmres的主函数，处理多线程
   disp_sen_dv.f90 #计算节点set位移的平方和及其相对于网格坐标的导数
   distattach_1d.f90 #计算两个节点的距离，一个节点给定全局坐标，另一个节点是由曲线上的局部坐标来确定。
   distattach_2d.f90 #计算两个节点的距离，一个节点给定全局坐标，另一个节点是由曲面上的局部坐标来确定。
   distattach_3d.f90 #同上
   distattachline.f90 #计算直线和曲面上的某个节点的距离
   distributesens.f90 #面部分布与对应节点值之间关系的计算——将节点灵敏度转化为面部分布灵敏度
   distributingcouplings.f90 #读取关键字*DISTRIBUTING COUPLING
   distributions.f90 #读取关键字*DISTRIBUTION
   divparll.c #一个数组除以另一个数组的并行化，每个元素对应一个元素
   dKdm.f90 #孔口相关
   dKdp.f90 #同上
   dKdt.f90 #同上
   dKdX.f90 #同上
   dload.f90 #用户子程序dload
   dloads.f90 #读取关键字*DLOAD
   dlz.f90 #将复矩阵A简化为上海森堡形式，将复矩阵B简化为三角形形式
   dmatrix.f90 #计算D矩阵的值
   dqag.f90 #定积分计算
   drfftf.f90 #快速傅里叶变换
   dsort.f90 #排序
   dsptrf.f90 #实对称矩阵分解，A = U*D*U**T  or  A = L*D*L**T
   dsptri.f90 #实对称矩阵不定分解
   dualshape3tri.f90 #三节点线性等参三角形单元的形状函数及其导数
   dualshape4q.f90 #形函数计算
   dualshape6tritilde.f90 #同上
   dualshape6tritilde_lin.f90 #同上
   dualshape8qtilde.f90 #同上
   dualshape8qtilde_lin.f90 #同上
   dudsmain.c #没有被任何函数调用
   dyna.c #动态分析
   dynamics.f90 #读取关键字*DYNAMIC
   dynboun.c #动态分析边界
   dynresults.f90 #在模态动力学计算中计算位移或温度
   e_c3d_cs_se.f90 #敏感性
   e_c3d_duds.f90 #同上
   e_c3d_em.f90 #
   e_c3d.f90 #为konl中具有拓扑结构的单元计算单元矩阵和rhs
   e_c3d_plhs.f90 #压力单元矩阵
   e_c3d_prhs.f90 #同上
   e_c3d_rhs.f90 #计算rhs
   e_c3d_rhs_th.f90 #同上
   e_c3d_se.f90 #敏感性
   e_c3d_th.f90 #
   e_c3d_u1.f90 #用户自定义单元u1
   e_c3d_u.f90 #同上
   e_c3d_us3.f90 #同上
   e_c3d_us45.f90 #同上
   e_c3d_v1rhs.f90 #单元速度矩阵
   e_c3d_v2rhs.f90 #同上
   e_c3d_vlhs.f90 #同上
   e_corio.f90 #同上
   e_damp.f90 #同上
   edgedivide.f90 #基于h场确定要分割的边以及每个这样的边的子间隔数量
   edg.f90 #目前没有被调用
   effectivemodalmass.f90 #计算频率计算的有效模态质量
   elastics.f90 #读取关键字ELASTIC
   electricalconductivitys.f90 #读取关键字*ELECTRICAL CONDUCTIVITY
   electromagnetics.c #电磁分析主程序
   electromagneticss.f90 #读取关键字*ELECTROMAGNETICS
   elemChecker.c #目前没有被调用
   elementcpuload.c #将单元划分为具有相等数量的活动单元的范围（单元编号可能有间隙），以便在不同cpu上并行处理
   elementpernode.f90 #确定属于单元节点的单元
   elementpernodef.f90 #同上
   elements.f90 #读取关键字*ELEMENT
   elemperdesi.f90 #确定属于给定设计变量i且包含多于nopedesi个设计变量的单元
   elemperorien.f90 #确定属于单元节点的单元
   elprints.f90 #读取*ELEMENT PRINT
   envtemp.f90 #确定气体温度和辐射温度的数量
   eplane.f90 #平面方程
   eqspacednodes.f90 #裂缝计算
   equationcheck.f90 #辐射计算
   equationfs.f90 #读取关键字*EQUATIONF
   equations.f90 #读取关键字*EQUATION
   errorestimator.f90 #误差估计，frd中调用
   evalshapefunc.f90 #计算形函数的值
   expand_auw.f90 #重新排列Wb矩阵中的行
   expand.c #调用Arnoldi包（ARPACK）进行循环对称性计算
   expansions.f90 #读取关键字*EXPANSION
   extendmesh.f90 #计算网格的扩展
   external.c #条件编译宏未定义
   extern_crackprop.f90 #确定外部边和外部节点，裂缝计算
   extfacepernode.f90 #列出与给定节点i对应的外部面
   extract_matrices.f90 #从刚度矩阵中提取矩阵bb，bi，ib
   extrapol2dto3d.f90 #对于二维模型，将中点的结果外推到2个对称平面
   extrapolatecontact.f90 #将积分点处的接触值外推到节点（用于face-to-face的罚接触）
   extrapolate.f90 #将积分点处的字段值外推到节点
   extrapolatefem.f90 #同上，处理内部变量
   extrapolate_se.f90 #
   extrapolateshell.f90 #
   extrapolateshell_us3.f90 #同上，自定义壳单元
   extrapolateshell_us45.f90 #同上，自定义壳单元
   extrapolate_u1.f90 #同上，自定义单元
   extrapolate_u.f90 #同上，自定义单元
   extrapolate_us3.f90 #同上，自定义单元
   extrapolate_us45.f90 #同上，自定义单元
   faceinfo.f90 #基于当前单元编号nelem和面编号jface为单元和曲面找到正确节点
   fcrit.f90 # 临界阻尼
   feasibledirection.c #基于灵敏度信息寻找可行方向
   feasibledirections.f90 #读取关键字*FEASIBLE DIRECTION
   fillknotmpc.f90 #更新非线性MPC中的系数
   film.f90 #用户子程序film
   films.f90 #读取关键字*FILM
   filter.f90 #灵敏度过滤
   filtermain.c #同上
   filters.f90 #读取关键字*FILTER
   findextsurface.f90 #对结构的外表面进行编目
   findslavcfd.f90 #在循环对称约束下寻找CFD计算的从属节点
   findsurface.f90 #确定网格的外表面并将其存储在ipoface和nodface字段中
   fixnode.f90 #灵敏度分析中固定节点的确定
   flowbc.f90 #流动边界，辐射计算
   flowoutput.f90 #辐射计算
   fluidconstantss.f90 #读取关键字*FLUID CONSTANTS
   fluidsections.f90 #读取关键字*FLUID SECTION
   flux.f90 #气体单元程序
   fminsirefine.f90 #用多面体方法最小化N个变量的函数，仅使用函数值
   forcadd.f90 #将cload条件添加到数据库中
   forcesolve.f90 #求解科里奥利力引起的复本征频率
   forparll.c #resultsforc.c中力计算的并行化
   frd.c #将结果保存为frd格式
   frdcyc.c #静态循环对称计算的重复字段
   frdfluidfem.f90 #将结果保存为frd格式，CFD
   frdgeneralvector.c #向量操作
   frdheader.c #处理header
   frditeration.f90 #将结果保存为frd格式
   frdselect.c #无需额外转换即可存储标量、向量分量和张量
   frd_sen.c #将结果保存为frd格式
   frdset.c #处理set
   frdvector.c #矢量数据
   frecord.c #将记录读取到“\n”；返回读取的字符数
   free_convection.f90 #自由对流
   free_disc_pumping.f90 #自由盘式泵流量
   frequencys.f90 #读取关键字*FREQUENCY
   fricheat.f90 #用户子程序fricheat
   friction_coefficient.f90 #计算包括过渡区域在内的层流和湍流管道流的摩擦系数
   frictionheating.f90 #决定摩擦加热的效果
   frictions.f90 #读取关键字*FRICTION
   fsub.f90 #亚临界阻尼
   fsuper.f90 #超临界阻尼
   fumid.f90 #节点周围二次四面体单元壳质量的确定
   fuvertex.f90 #节点周围线性四面体单元球质量的确定
   gapconductances.f90 #读取关键字*GAP CONDUCTANCE
   gapcon.f90 # 用户子程序gapcon
   gapheatgenerations.f90 #读取关键字*GAP HEAT GENERATION
   gaps.f90 #读取关键字*GAP
   gasmechbc.f90 #在热计算后的力计算中更新边界条件
   gaspipe_fanno.f90 #具有摩擦损失的管道
   gaspipe_rot.f90 #具有摩擦和可变横截面的旋转管
   gauss.f90 #高斯积分点和权重
   gen3dboun.f90 #将定义了SPC的1-D和2-D单元的节点连接到其扩展对应节点
   gen3dconnect.f90 #将扩展的1-D和2-D单元与真正的3D元素或弹簧单元或质量单元连接起来
   gen3delem.f90 #生成3D单元
   gen3dforc.f90 #处理集中力
   gen3dfrom1d.f90 #将1d单元i扩展为3d单元
   gen3dfrom2d.f90 #2d
   gen3dmembrane.f90 #SPC
   gen3dmpc.f90 #MPC
   gen3dnor.f90 #计算1d,2d单元的法向
   gen3dsurf.f90 #处理surface
   gen3dtemp.f90 #映射温度和温度梯度
   gen3dtruss.f90 #处理桁架
   genadvecelem.f90 #生成模拟网络单元和结构面之间平流的单元
   gencontelem_f2f.f90 #为从属接触节点生成接触单元
   gencontelem_n2f.f90 #同上
   gendualcoeffs.f90 #确定slave曲面上对偶形函数的系数
   generatecycmpcs.f90 #生成循环mpc
   generateeminterfaces.f90 #确定phi域和任何其他域之间的接口，电磁计算
   generatetet_refine.f90 #生成新的tet
   generatetet_refine2.f90 #生成新的tet并更新数据库
   genfirstactif.f90 #生成第一个活动集并计算从属面上所有面的面积
   genislavactdof.f90 #MORTAR接触
   genislavelinv.f90 #计算islavelinv，MORTAR接触
   genmidnodes.f90 #在相邻顶点节点之间的中间生成中间节点
   genmodes.f90 #为不兼容的模式生成节点
   genmpc.f90 #生成MPC，将旧tet网格中的节点连接起来，其中SPC或点力被定义为与改进tet网格的节点连接
   gennactdofinv.f90 #对域nactdof求逆
   genrandmain.c #生成随机数
   genratio.f90 #创建MPC，将细化tet网格中的节点连接到初始tet网格的节点；这是新网格中温度边界条件所必需的
   gentiedmpc.f90 #为从属tied 接触节点生成MPC
   geometricconstraints.f90 #读取关键字*GEOMETRIC CONSTRAINT
   geometrictolerances.f90 #读取关键字*GEOMETRIC TOLERANCE
   geomview.f90 #辐射计算
   getcontactparams.f90 #提取接触常数的函数
   getdesiinfo2d.f90 #在nodedesi中存储设计变量，在nodedesiinv中标记哪些节点是设计变量
   getdesiinfo3d.f90 #同上
   getdesiinfo3d_robust.f90 #同上
   getdesiinfobou.f90 #同上
   getglobalresults.c #获取全局结果
   getlocalresults.c #获取局部结果
   getlocno.f90 #在单元内查找局部节点编号
   getnewline.f90 #处理inp文件，获取一个新行
   getnodel.f90 #基于面号jface和节点号ii为不同单元类型找到正确节点
   getnodesinitetmesh.f90 #读取将被细化的初始tet网格
   getnumberofnodes.f90 #获取单元的节点数量
   getSystemCPUs.c #一种统一的方法来获取*NIX和Windows系统的可用CPU核数
   getuncrackedresults.c #从文件中读取所有温度、位移、应力和力数据
   getversion.f90 #获取软件版本
   globalcrackresults.f90 #计算沿裂纹前缘的应力强度因子
   greens.f90 #读取关键字*GREEN
   hcfs.f90 #读取关键字*HCF
   hcrit.f90 #确定梯形渠道交叉口的临界深度
   headings.f90 #读取关键字*HEADING
   heattransfers.f90 #读取关键字*HEAT TRANSFER
   henergy.f90 #确定与特定能量和质量流量的给定值相对应的深度，流体计算
   hgforce.f90 #8节点实体平均应变单元的沙漏形控制力
   hgstiffness.f90 #8节点实体平均应变单元的沙漏形控制刚度
   hnorm.f90 #确定梯形渠道交叉口的正常深度
   hns.f90 #同上
   hybsvd.f90 #奇异值分解
   hyperelastics.f90 #读取关键字*HYPERELASTIC
   hyperfoams.f90 #读取关键字*HYPERFOAM
   ident.f90 #标识px在实数有序数组x中的位置id
   ident2.f90 #同上
   identamta.f90 #同上
   identifytiedface.f90 #识别tie从属面中的从属节点
   identifytransform.f90 #检查是否对给定的面应用了变换，如果是，则检查是哪一个（仅适用于CFD）
   includefilename.f90 #确定一个include文件的名称
   incplas.f90 #增量塑性材料法计算刚度和应力
   incplas_lin.f90 #同上
   ini_cal.c #在初始化和重初始化时会调用此函数
   inicont.c #初始化
   inimortar.c #在nonlingeo.c开始时初始化mortar接触
   iniparll.c #resultsini.c中的并行部分
   initialcfdfem.f90 #CFD计算初始化
   initialchannel.f90 #CFD
   initialconditionss.f90 #读取关键字*INITIAL CONDITIONS
   initialnet.f90 #为gas计算初始条件
   initialstrainincreases.f90 #读取关键字*INITIAL STRAIN INCREASE
   init_submodel.f90 #初始化ipofa和inodfa
   inputerror.f90 #输出读取错误,并设置ier=1
   inputinfo.f90 #输出读取错误
   inputwarning.f90 #警告
   insert.c #在数据结构中插入一个新的非零矩阵位置，下三角矩阵的例程，不包括对角线
   insert_cmatrix.c #同上
   insertas.c #稀疏矩阵
   insertas_ws.c #同上
   insertcbs.c #同上
   insertrad.c #同上
   insertfreq.c #计算边界刚度系数
   insertsortd.f90 #对于小的n的简单插入排序，浮点数
   insertsorti.f90 #对于小的n的简单插入排序，整数
   interpol_alfa2.f90 #插值alfa2
   interpolateinface.f90 #对face进行三角剖分，并根据这些平面的平面方程插值xstate变量
   interpolatestate.f90 #在新增量开始时对新积分点的xstate值进行插值
   interpolatestatemain.c #插值，在nonlingeo中调用
   interpolextnodes.f90 #主文件应力结果到裂纹形状边界节点的插值，裂缝计算
   interpolextnodesf.f90 #模态“mode”的hcf主文件应力结果到裂纹形状边界节点的插值，裂缝计算
   interpolsubmodel.f90 #对于坐标为coo的节点，在存储在integerglob和doubleglob中的全局网格内，用相对位置为“iselect”的“nselect”值进行插值
   interpoltet.f90 #同上
   interpoltetmain.c #目前未被调用
   intersectionpoint.f90 #计算交点，在sutherland_hodgman中调用。
   inversewavspd.f90 #波速导数，在anisomaxwavspd调用
   inviscidpre.f90 #inviscidpre，目前没有调用
   islavactive.f90 #对于具有相反主面的节点，将值1设置为字段islavact。
   isortic.f90 #整型数组排序
   isortiddc.f90 #同上
   isortid.f90 #同上
   isorti.f90 #同上
   isortiiddc.f90 #同上
   isortiid.f90 #同上
   isortii.f90 #同上
   isortiii.f90 #同上
   jouleheating.f90 #决定焦耳加热的效果
   keystart.f90 #用来构造inp域中的链
   knotmpc.f90 #为节点node生成关于参考（平移）节点irefnode和旋转节点irotnode的三个结MPC
   lab_straight_ppkrit.f90 #labyrinth使用
   labyrinth.f90 #迷宫密封
   limit_case_calc.f90 #限制器，CFD
   linel.f90 #计算线弹性材料的应力
   linkdissimilar.f90 #连接不同网格以实现循环对称
   linscal.f90 #计算C3D20单元中温度的二次插值的三线性近似值（全积分）
   linscal10.f90 #C3D10
   linstatic.c #线性静力计算
   lintemp.f90 #计算C3D20单元中温度的二次插值的三线性近似值（全积分）
   lintemp_th0.f90 #同上
   lintemp_th1.f90 #同上
   lintemp_th.f90 #同上
   linvec10.f90 #同上
   linvec.f90 #同上
   liquidpipe.f90 #不可压缩介质管元
   liquidpump.f90 #不可压缩介质泵
   loadadd.f90 #将面分布加载条件添加到数据库中
   loadaddp.f90 #同上
   loadaddt.f90 #热
   localaxescs.f90 #根据CYCLIC SYMMETRY MODEL关键字上定义的旋转轴确定局部轴系
   localaxes.f90 #根据CENTRIF关键字上定义的旋转轴确定局部轴系
   lump.f90 #将adb、aub中存储的矩阵进行汇总，并将结果存储在adl中
   machpi.f90 #计算输入的压力比PI的马赫数
   mafillcorio.f90 #以稀疏矩阵格式填充阻尼矩阵
   mafilldm.f90 #同上
   mafilldmss.f90 #以稀疏矩阵格式填充刚度矩阵，稳态动力学
   mafilldmssmain.c #同上
   mafillem.f90 #电磁
   mafillfreq_em.f90 #同上
   mafillnet.f90 #gas
   mafillpbc.f90 #压力
   mafillplhs.f90 #同上
   mafillprhs.f90 #同上
   mafillsm.f90 #以稀疏矩阵格式填充刚度矩阵
   mafillsmas.f90 #反对称贡献
   mafillsmasmain.c #多线程处理
   mafillsmcs.f90 #
   mafillsmcsas.f90 #
   mafillsmcsse.f90 #
   mafillsmduds.f90 #
   mafillsmforc.f90 #
   mafillsmmain.c #
   mafillsmmain_se.c #
   mafillsmse.f90 #
   mafillv1rhs.f90 #
   mafillv2rhs.f90 #
   mafillvlhs.f90 #
   magneticpermeabilitys.f90 #读取关键字*MAGNETIC PERMEABILITY
   map3dto1d2d.f90 #将三维场节点值插值到1d/2d节点位置
   map3dto1d2d_v.f90 #
   map3dtolayer.f90 #
   massflow_percent.f90 #部分质量流单元
   massflows.f90 #读取关键字*MASS FLOW
   massless.c #确定无质量接触全局系统的RHS
   masss.f90 #读取关键字*MASS
   mastruct.c #确定热力矩阵的结构
   mastructcmatrix.c #确定包含边界节点协方差信息的C-Matrix的结构
   mastructcs.c #确定具有循环对称性的热力矩阵的结构
   mastructdmatrix.c #确定包含边界节点协方差信息的D-Matrix的结构
   mastructem.c #确定热电磁矩阵的结构
   mastructffem.c #
   mastructnmatrix.c #决定（N^T*N）矩阵的结构
   mastructrad.c #确定视因子和辐射矩阵的结构
   mastructrand.c #确定协方差矩阵的结构
   mastructse.c #确定灵敏度矩阵的结构
   materialdata_cond.f90 #决定导热系数
   materialdata_cp.f90 #确定比热
   materialdata_cp_sec.f90 #确定恒压下的割线比热
   materialdata_crack.f90 #计算裂纹扩展增量
   materialdata_dvi.f90 #确定动态粘度
   materialdata_dvifem.f90 #同上
   materialdata_em.f90 #确定温度t1l下的电导率和磁导率
   materialdata_me.f90 #确定单元iel的材料数据
   materialdata_rho.f90 #确定密度
   materialdata_sp.f90 #确定单元iel的材料数据
   materialdata_tg.f90 #确定气体材料数据
   materialdata_th.f90 #同上
   materials.f90 #读取关键字*MATERIAL
   matrixsort.c #稀疏矩阵排序
   matrixstorage.c #矩阵存储
   matvec.f90 #实稀疏矩阵（压缩行格式）和向量乘法
   matvec_struct.f90 #同上
   mechmodel.f90 #力学材料模型
   membranesections.f90 #读取关键字*MEMBRANE SECTION
   merge_ikactmech1.f90 #从不同的线程合并数据
   meshquality.f90 #计算单元质量。所用的度量与最长边除以内切球半径的比值成正比
   meshqualitycavity.f90 #同上
   midexternaledges.f90 #存储属于未细化网格外部边缘的节点
   midexternalfaces.f90 #存储属于未细化网格外表面的节点
   modaldampings.f90 #读取关键字*MODAL DAMPING
   modaldynamics.f90 #读取关键字*MODAL DYNAMIC
   modelchanges.f90 #读取关键字*MODEL CHANGE
   modf.f90 #取模
   modifympc.f90 #生成MPC，将旧tet网格中的节点连接起来，其中SPC或点力被定义为与改进tet网格的节点连接
   moehring.f90 #CFD
   mortar.h #mortar接触所需的函数
   mortar_postfrd.c #在frd文件中mortar输出的取消准备
   mortar_prefrd.c #在frd文件中mortar输出的准备
   mpcadd.f90 #生成一个等式MPC
   mpcrem.f90 #删除编号为i的MPC
   mpcs.f90 #读取关键字*MPC
   msolve.f90 #矩阵预条件
   msolve_struct.f90 #同上
   mulmatvec_asym.f90 #非对称稀疏矩阵和向量的乘法
   mult.f90 #3阶矩阵乘法
   multimortar.c #将接触条件嵌入矩阵系统并压缩拉格朗日乘子
   multi_rect.c #稀疏矩阵乘法
   multi_rectv.c #稀疏矩阵-向量乘法
   multi_scal.c #两个矩阵的两个列的标量积
   multistages.f90 #创建多级MPC：连接不同的循环对称段
   multvec.f90 #矢量内积
   near2d.f90 #确定n个坐标为(xo，yo)的节点中距离坐标为(xp，yp的点最近的k个节点；
   near3d.f90 #3d
   near3d_se.f90 #球
   neartriangle.f90 #检查是否存在一个三角形，使得穿过p且方向为xn的直线切割该三角形
   negativepressure.f90 #计算面对面接触时最小压力与最大压力的比值。如果压力为负，则该比率为负
   networkelementpernode.f90 #确定属于单元节点的单元
   networkextrapolate.f90 #在流体单元中外插节点值
   networkforc.f90 #计算一般网络单元的集中通量
   networkinum.f90 #为与网络节点对应的inum值分配负号
   networkmpc_lhs.f90 #用户定义网络MPC
   networkmpc_rhs.f90 #同上
   networkmpcs.f90 #读取关键字*NETWORK MPC
   networkneighbor.f90 #网络相关
   networkstiff.f90 #网络相关
   newnodes.f90 #基于h场确定要分割的边以及每个这样的边的子间隔数量
   newton.f90 #通过使用场ipobody将体力分配给元素
   nident.f90 #在有序整数数组x中查找满足条件的id
   nident2.f90 #同上
   nidentk.f90 #x有2个下标(k,n)，第一个下标是有序的。
   nidentll.f90 #同上，不过x是64位整数
   nmatrix.f90 #计算表达式的值：N^（T）N
   noanalysiss.f90 #读取关键字*NO ANALYSIS
   nodalthicknesss.f90 #读取关键字*NODAL THICKNESS
   nodeprints.f90 #读取关键字*NODE PRINT
   nodes.f90 #读取关键字*NODE
   nodestiedface.f90 #识别绑定从属面中的从属节点
   noelfiles.f90 #读取关键字*NODE FILE, *EL FILE and *CONTACT FILE
   noelsets.f90 #读取*NSET和*ELSET
   nonlingeo.c #几何非线性
   nonlinmpc.f90 #更新非线性MPC中的系数
   normals.f90 #读取关键字*NORMAL
   normalsforequ_se.f90 #在优化循环中计算曲面上的法线以进行网格修改
   normalsoninterface.f90 #电磁分析
   normalsonsurface_robust.f90 #计算外表面上的法线方向；设计变量沿此方向移动
   normalsonsurface_se.f90 #同上
   normmpc.f90 #对流体应用（CFD）的MPC系数进行归一化
   norshell3.f90 #计算具有局部坐标xi和et的点中的二次壳单元上的法线
   norshell4.f90 #同上
   norshell6.f90 #同上
   norshell8.f90 #同上
   nortanslav.f90 #计算从属曲面（slavnor、slavtan）节点中的法线和切线矢量
   objective_disp.f90 #计算节点set位移的平方和
   objective_disp_tot.f90 #
   objective_freq_cs.f90 #
   objective_freq.f90 #
   objectivemain_se.c #
   objective_mass_dx.f90 #计算质量及其相对于网格坐标的导数
   objective_modalstress.f90 #模态应力灵敏度的计算
   objective_peeq.f90 #计算节点set的von Mises应力的平方和
   objective_peeq_se.f90 #
   objectives.f90 #读取关键字*OBJECTIVE
   objective_shapeener_dx.f90 #计算网格坐标的内能及其导数
   objective_shapeener_tot.f90 #
   objective_stress_dx_dy.f90 #
   objective_stress.f90 #计算（von Mises）应力的Kreisselmeier-Steinhauser函数，优化设计使用
   objective_stress_se.f90 #
   objective_stress_tot.f90 #
   onedint.f90 #逐点定义函数的插值
   op.f90 #稀疏对称矩阵乘法
   opas.f90 #稀疏对称矩阵乘法
   op_corio.f90 #反对称
   openfile.f90 #创建必须的文件，并打开输入和输出文件
   openfilefluidfem.f90 #打开流体计算的文件
   opnonsym.f90 #非对称矩阵-向量乘法
   opnonsymt.f90 #同上
   orientations.f90 #读取关键字*ORIENTATION
   orifice.f90 #孔口单元
   orthonl.f90 #正交各向异性，替换e_c3d.f中部分
   orthotropic.f90 #将9个正交各向异性弹性常数展开为3x3x3x3矩阵
   outputs.f90 #读取关键字*OUTPUT
   pardiso.c #未定义宏，因此未使用
   pardiso_cp.c #同上
   pastix.c #同上
   patch.f90 #计算单元面片的平滑节点应力
   pcgsolver.c #预处理共轭梯度求解器
   peeq_sen_dv.c #敏感性分析用到
   peeq_sen_dx.c #同上
   phys2con.f90 #根据物理变量计算保守变量
   physicalconstantss.f90 #读取关键字*PHYSICAL CONSTANTS
   pk_cdc_cl1.f90 #孔口相关
   pk_cdc_cl3a.f90 #
   pk_cdc_cl3b.f90 #
   pk_cdc_cl3d.f90 #
   pk_cdc_cl3.f90 #
   pk_cdi_noz.f90 #
   pk_cdi_r.f90 #
   pk_cdi_rl.f90 #
   pk_cdi_se.f90 #同上
   pk_y0_yg.f90 #测量的绝热膨胀系数y0
   plane3.f90 #根据三个节点计算平面方程
   plane4.f90 #同上，不过要先排除一个点
   plane_eq.f90 #同上
   planeeq.f90 #
   planempc.f90 #为位于由两个节点a和b定义的直线上的节点生成MPC。
   plastics.f90 #读取关键字*PLASTIC
   plcopy.f90 #从imat材料种复制硬化数据，从plcon中复制温度itemp，生成plconloc，如果数据点不超过200个
   plinterpol.f90 #对各向同性或随动强化的数据插值
   plmix.f90 #插值材料imat和温度j和j-1的硬化数据，以获得温度数据
   pop.f90 #栈操作
   postinitialnet.f90 #可压缩网络
   postprojectgrad.f90 #计算投影梯度
   postview.f90 #辐射计算
   precfdcyc.f90 #cfd应用的循环更新
   preconditioning.f90 #矩阵的对角预处理
   precondrandomfield.f90 #右侧装配
   precontact.c #接触相关
   predgmres_struct.f90 #为dgmres构造
   predgmres_struct_mt.c #多线程
   prediction.c #预测
   prediction_em.c #电磁相关
   prefilter.f90 #敏感性过滤
   preinitialnet.f90 #基于边界条件和用户通过网络传播给出的初始值来确定初始值
   preiter.c #预迭代
   premortar.c #在求解器转换SPC/MPC、矩阵和二次单元的右侧之前调用的函数
   preparll.c #prediction.c的并行部分
   preprojectgrad.f90 #计算投影梯度
   presgradient.f90 #确定压力梯度的测量值
   pretensionsections.f90 #*PRE-TENSION SECTION
   prethickness.f90 #厚度计算，优化使用
   pretransition.f90 #敏感性分析
   printoutcontact.f90 #接触力的计算和打印
   printoutebhe.f90 #将结果存储在.dat文件中
   printoutelem.f90 #将nelem单元的整个单元结果存储在.dat文件中
   printout.f90 #将结果存储在.dat文件中
   printoutface.f90 #表面上的热通量、力和/或力矩的计算和打印输出
   printoutfacefem.f90 #升力和阻力的计算和打印
   printoutfluidfem.f90 #将结果存储在.dat文件中
   printoutint.f90 #将nelem单元的积分点的结果存储在.dat文件中
   printoutintfluidfem.f90 #同上
   printoutnode.f90 #节点
   printoutnodefluid.f90 #同上
   printoutnodefluidfem.f90 #同上
   projectgrad.f90 #计算非线性约束下的投影梯度、拉格朗日乘子和校正项
   projectmidnodes.f90 #中间节点投影
   projectvertexnodes.f90 #同上
   propertynet.f90 #用户子程序propertynet
   pt2_lim_calc.f90 #限制器计算
   pt2zpt1_crit.f90 #计算最大容许压力比pt2/pt1，管道流动
   pt2zpt1_rot.f90 #同上
   push.f90 #入栈
   qsorti.f90 #快速排序
   quadmeshquality.f90 #计算单元的质量
   quadraticsens.f90 #敏感性分析
   radcyc.c #循环辐射条件下的复制三角形面
   radflowload.c #辐射计算
   radiate.f90 #用户子程序radiate
   radiates.f90 #读取关键字*RADIATE
   radmatrix.f90 #辐射
   radresult.f90 #同上
   randomfieldmain.c #生成用于鲁棒性评估的随机场
   randomfields.f90 #读取关键字*RANDOM FIELD
   randomval.f90 #使用Box-Muller变换创建正态分布单位方差高斯随机变量
   ranstarefine.f90 #随机搜索以确定一个函数值与起点X不同的点
   ranuwh.f90 #使用Wichmann和Hill方法的便携式均匀随机数生成器
   rcavi.f90 #旋转空腔单元，孔口
   rcavi2.f90 #同上
   rcavi_cp_lt.f90 #同上
   rcavi_cp_nt.f90 #同上
   readforce.f90 #读取复杂的力（例如，流体对谐波结构激励的响应）
   readfrd.c #读取frd文件
   readinput.c #读取.inp文件,根据关键字对文件进行分块, 确定set的数量：
   readnewmesh.c #读取新网格
   readsen.f90 #敏感性分析
   readview.f90 #读取辐射因子
   rearrangecfd.f90 #对流体的节点和单元重新编号，以确保没有间隙
   rearrange.f90 #修改Ernst Rank迭代求解器（pcgsolver）的稀疏存储模式
   rectcylexp.f90 #循环对称相关
   rectcyl.f90 #同上
   rectcylvi.f90 #同上
   rectcylvold.f90 #同上
   reducematrix.f90 #无质量动态接触
   refinemesh.c #作为场变量函数的四面体网格细化
   refinemeshs.f90 #读取关键字*REFINE MESH
   regularization_gn_c.f90 #法向mortar接触的正则化函数
   regularization_gt_c.f90 #切向
   regularization_slip_iwan.f90 #同上
   regularization_slip_lin.f90 #同上
   reinit_refine.f90 #refinemesh相关
   relaxval_al.f90 #接触相关
   remastruct.c #在MPC发生变化后，重建刚度和质量矩阵中的非零位置
   remastructar.c #同上，由arpack调用
   remastructem.c #同上
   removesliver.f90 #移除四面体网格表面的碎片
   removetet_refine.f90 #删除tet并更新数据库
   removetet_sliver.f90 #同上
   reorderampl.f90 #按字母顺序重新排序amname
   res1parll.c #calcresidual.c的并行化
   res2parll.c #
   res3parll.c #
   res4parll.c #同上
   reservoir.f90 #求解非侵蚀性底部河道中湍流静止流的Bresse方程：水库
   resforccont.f90 #接触使用
   restartread.f90 #重启动读取
   restarts.f90 #读取关键字*RESTART
   restartshort.f90 #重启动相关
   restartwrite.f90 #将重启动所需的所有信息写入到文件中
   restrictor.f90 #具有部分总水头损失的压力损失单元
   resultnet.f90 #辐射计算
   results.c #计算积分点上的各种变量的值，将节点或积分点的值存储在.dat文件中
   resultsem.f90 #计算积分点处的热通量和材料切线，以及节点处的内部集中通量
   resultsforc.c #减去mpc力
   resultsforc_em.f90 #方程组内力矢量的计算
   resultsforc_se.f90 #同上
   resultsinduction.c #多线程处理
   resultsini.c #后处理
   resultsini_em.f90 #同上
   resultsini_mortar.f90 #mortar与mpc
   resultsk.f90 #计算节点中的湍流校正（步骤5）
   resultsmech.f90 #计算积分点处的应力和材料切线以及节点处的内力
   resultsmech_se.f90 #同上
   resultsmech_u1.f90 #
   resultsmech_u.f90 #
   resultsmech_us3.f90 #
   resultsmech_us45.f90 #同上
   resultsnoddir.f90 #将自由度值复制为（idir，node）格式
   resultsp.f90 #计算节点中的压力校正（步骤2）
   resultsprint.f90 #打印结果
   results_se.c #敏感性计算
   resultsstr.c #计算积分点的应力值
   resultst.f90 #计算节点中的能量校正（步骤4）
   resultstherm.f90 #计算积分点处的热通量和材料切线，以及节点处的内部集中通量
   resultsv1.f90 #计算节点中的速度校正（步骤1）
   resultsv2.f90 #计算节点中的速度校正（步骤3）
   retainednodaldofss.f90 #读取关键字*RETAINED NODAL DOFS
   rhs.f90 #填充右侧载荷向量b
   rhsmain.c #多线程处理
   rhsnodef.f90 #同上
   rigidbodys.f90 #读取关键字*RIGID BODY
   rigidmpc.f90 #生成关于参考（平移）节点irefnode和旋转节点irotnode的节点“node”的三个刚体MPC
   rimseal_calc.f90 #rimseal单元
   rimseal.f90 #rimseal单元
   robustdesign.c #鲁棒性设计
   robustdesigns.f90 #读取关键字*ROBUST DESIGN
   rotationvector.f90 #根据旋转矩阵a计算旋转向量v
   rotationvectorinv.f90 #根据旋转向量计算旋转矩阵
   rs.f90 #特征值求解
   rubber.f90 #计算橡胶和弹性泡沫材料的刚度和应力
   scalesen.f90 #敏感性计算
   scavenge_pump.f90 #扫气泵单元
   sdvini.f90 #用户子程序sdvini
   searchmidneigh.f90 #查找中间节点的邻居
   sectionprints.f90 #读取关键字*NODE PRINT
   selectcyclicsymmetrymodess.f90 #读取关键字*SELECT CYCLIC SYMMETRY MODES
   sensi_coor.c #敏感性分析
   sensi_orien.c #
   sensitivity_out.c #读取关键字*SENSITIVITY
   sensitivitys.f90 #
   setpardou.c #并行化给一个域赋予浮点数值
   setparitg.c #并行化给一个域赋予整数数值
   sgi.c #SGI
   shape10tet.f90 #形函数和导数
   shape15w.f90 #
   shape20h_ax.f90 #
   shape20h.f90 #
   shape20h_pl.f90 #
   shape2l.f90 #
   shape3l.f90 #
   shape3tri.f90 #
   shape4q.f90 #
   shape4tet.f90 #
   shape6tri.f90 #
   shape6tritilde.f90 #
   shape6tritilde_lin.f90 #
   shape6w.f90 #
   shape7tri.f90 #
   shape8h.f90 #
   shape8hr.f90 #
   shape8hu.f90 #
   shape8humass.f90 #
   shape8q.f90 #
   shape8qtilde.f90 #
   shape8qtilde_lin.f90 #
   shape9q.f90 #
   shellsections.f90 #读取关键字*SHELL SECTION
   sigini.f90 #用户子程序sigini
   skip.f90 #
   slavintmortar.f90 #计算从属主三角测量
   slavintpoints.f90 #确定从属曲面中积分点的位置
   sluicegate.f90 #管道相关
   smalldist.f90 #敏感度使用
   smoothbadmid.f90 #refine使用
   smoothbadvertex.f90 #同上
   smoothingmidnodes.f90 #通过移动中点平滑二次四面体网格
   smoothingvertexnodes.f90 #平滑网格
   smoothshock.f90 #平滑有限元结果
   solidsections.f90 #读取关键字*SOLID SECTION
   solveeq.c #通过迭代求解集总形式求解方程组
   sortev.f90 #对复频率的特征值和特征向量进行排序
   spcmatch.f90 #将一步的SPC边界条件与前一步的边界条件相匹配
   specificgasconstants.f90 #读取关键字*SPECIFIC GAS CONSTANT
   specificheats.f90 #读取关键字*SPECIFIC HEAT
   splitline.f90 #将text按照逗号分割,结果存储在textpart中
   spooles.c #线性方程组求解器
   spooles_read.f90 #
   spooles_write.f90 #
   springdamp_f2f.f90 #计算接触阻尼矩阵（face-to-face惩罚）
   springdamp_n2f.f90 #node-to-face
   springforc_f2f.f90 #计算弹簧的力（face-to-face惩罚）
   springforc_f2f_th.f90 #计算接触区域的热通量
   springforc_n2f.f90 #计算弹簧的力（node-to-face惩罚）
   springforc_n2f_th.f90 #计算接触区域的热通量
   springs.f90 #读取关键字*SPRING
   springstiff_f2f.f90 #计算弹簧的刚度（face-to-face惩罚）
   springstiff_f2f_th.f90 #
   springstiff_n2f.f90 #计算弹簧的刚度（node-to-face惩罚）
   springstiff_n2f_th.f90 #
   statics.f90 #读取关键字*STATIC
   steadystate.c #稳态动力学计算
   steadystatedynamicss.f90 #读取关键字*STEADY STATE DYNAMICS
   steps.f90 #读取关键字*STEP
   stiff2mat.f90 #刚度矩阵从空间坐标到材料坐标的转换，变形塑性会用到
   stof.c #从字符串位置a到b返回double
   stoi.c #从字符串位置a到b返回int
   stop.f90 #关闭所有文件，并调用exit(201)
   stopwithout201.f90 #关闭所有文件，但不调用exit(201)
   storecontactdof.c #接触自由度，目前没有被调用
   storecontactprop.f90 #!计算接触单元的固有振荡周期
   storeresidual.f90 #保存残差
   stos.c #从位置a到b返回字符串缓冲区
   str2mat.f90 #将空间坐标中的应力转换为材料坐标，或将材料坐标中的应变转换为空间坐标。
   straightchannel.f90 #渠道流动
   straighteq2d.f90 #计算三角形边的方程。
   straighteq3d.f90 #计算穿过三角形边并垂直于三角形的平面与三角形本身的平面的方程
   straighteq3dpen.f90 #计算穿过三角形边并垂直于每个三角形边的代表法线的平面以及三角形本身的平面的方程
   straightmpc.f90 #为位于由两个节点a和b定义的直线上的节点生成MPC
   strcmp1.c #判断s1和s2是否一方是另一方的连续首子串
   strcmp2.c #
   strcpy1.c #从s2复制length个字符到s1中
   stressintensity.f90 #计算沿裂纹前缘的应力强度因子
   stressintensity_smoothing.f90 #使裂纹长度平滑
   stressmortar.c #mortar接触
   stress_sen_dv.c #敏感性
   stress_sen_dx.c #
   strsplt.c #字符串分解
   submodels.f90 #读取关键字*SUBMODEL
   subspace.f90 #求解映射在特征向量子空间上的线性动力学方程（仅当模型中有缓冲器时）
   substructuregenerates.f90 #读取关键字*SUBSTRUCTURE GENERATE
   substructurematrixoutputs.f90 #读取关键字*SUBSTRUCTURE MATRIX OUTPUT
   subtracthmatrix.f90 #可压缩流体的H-矩阵对rhs的传递效应
   surfacebehaviors.f90 #读取关键字*SURFACE BEHAVIOR
   surfaceinteractions.f90 #读取关键字*SURFACE INTERACTION
   surfaces.f90 #读取关键字*SURFACE
   sutherland_hodgman.f90 #多边形裁剪与主动线搜索相结合
   swap.f90 #
   tau.c #TAUCS
   tee.f90 # 十字型单元
   temperatures.f90 #读取关键字*TEMPERATURE
   temploaddiff.f90 #计算给定时间的负载和上次调用temploaddiff的差距
   tempload_em.f90 #电磁
   tempload.f90 #计算给定时间的负载
   temploadfem.f90 #计算给定时间的负载
   temploadmodal.f90 #计算给定时间下模态动力学过程的SPC边界条件
   thermmodel.f90 #热分析
   thickness.f90 #实际壁厚的计算
   thicknessmain.c #多线程
   tiedcontact.c #tied约束
   tiefaccont.f90 #对slave face进行编目
   ties.f90 #读取关键字*TIE
   timepointss.f90 #读取关键字*AMPLITUDE
   topocfdfem.f90 #cfd应用的初步计算
   totalcontact.f90 #为从属接触节点生成接触单元
   trafontmortar2.c #
   trafontspcmpc.c #由于SPC/MPC修正n和t
   transformatrix.f90 #确定笛卡尔坐标系或柱面坐标系的点p中的变换矩阵a
   transformfs.f90 #读取关键字*TRANSFORMF
   transforms.f90 #读取关键字*TRANSFORM
   transformspcsmpcs_quad.c #将SPC/MPC转换为双mortar接触所需的二次从属单元
   transition.f90 #设计空间与非设计空间之间的灵敏度缩放
   transitionmain.c #多线程
   transpose.c #系数矩阵转置
   treatmasterface.f90 #用从属曲面切割主曲面的三角形
   treatmasterface_mortar.f90 #
   trianeighbor.f90 #对给定主三角形的相邻三角形进行编目
   triangucont.f90 #生成接触主曲面的三角剖分
   triangulate.f90 #生成独立侧（=右侧）的三角剖分，识别独立侧的单元面并进行三角剖分
   triloc.f90 #delauny用到
   ts_calc.f90 #根据总温度Tt、总压力Pt和质量流量xflow计算静态温度Ts。通用气体方程的使用
   tt_calc.f90 #同上
   turningdirection.f90 #根据CENTRIF关键字上定义的旋转轴确定局部轴系
   twodint.f90 #逐点定义的二维函数插值
   two_phase_flow.f90 #两相流
   uamplitude.f90 #用户子程序uamplitude
   uboun.f90 #用户子程序
   u_calloc.c #内存分配
   ufaceload.f90 #用户子程序，面荷载
   u_free.c #内存释放
   uhardening.f90 #用户子程序，强化
   u_malloc.c #内存分配
   umat_abaqus.f90 #
   umat_abaqusnl.f90 #
   umat_aniso_creep.f90 #
   umat_aniso_plas.f90 #
   umat_ciarlet_el.f90 #
   umat_compression_only.f90 #
   umat_elastic_fiber.f90 #
   umat.f90 #umat统一入口
   umatht.f90 #
   umat_ideal_gas.f90 #
   umat_lin_el_corot.f90 #
   umat_lin_iso_el.f90 #
   umat_main.f90 #
   umat_single_crystal_creep.f90 #
   umat_single_crystal.f90 #
   umat_tension_only.f90 #
   umat_undo_nlgeom_lin_el.f90 #
   umat_undo_nlgeom_lin_iso_el.f90 #
   umat_user.f90 #
   umpc_dist.f90 #更新dist-mpc中的系数
   umpc_mean_rot.f90 #更新平均旋转mpc中的系数
   umpc_user.f90 #用户自定义MPC
   uncouptempdisps.f90 #读取关键字*UNCOUPLED TEMPERATURE-DISPLACEMENT
   updatecon.f90 #更新守恒变量
   updatecont2d.f90 #
   updatecont.f90 #更新接触主曲面三角剖分的几何数据
   updatecontpen.f90 #同上
   updategeodata.f90 #计算实际网格所有节点中h的期望大小
   u_realloc.c #重新分配内存
   us3_sub.f90 #用户自定义单元的材料
   us4_sub.f90 #同上
   userelements.f90 #读取关键字*USER ELEMENT
   usermaterials.f90 #读取关键字*USER MATERIAL
   usermpc.f90 #为用户mpc初始化mpc字段
   user_network_element.f90 #
   user_network_element_p0.f90 #
   user_network_element_p1.f90 #
   usersections.f90 #读取关键字*USER SECTION
   utemp.f90 #用户子程序utemp
   utemp_ccxlib.f90 #同上
   utempread.c #读取数据
   valuesatinfinitys.f90 #读取关键字*VALUES AT INFINITY
   varsmooth.f90 #有限元解的变量平滑
   v_betrag.c #向量a的长度
   velinireltoabs.f90 #通过使用场ipobody将体力分配给单元
   viewfactors.f90 #读取关键字*VIEWFACTOR
   viscos.f90 #读取关键字*VISCO
   vortex.f90 #涡单元
   v_prod.c #矢量乘法
   v_result.c #矢量减法
   wcoef.f90 #二阶单元刚度矩阵推导中w系数的计算
   worparll.c #并行计算外力功
   wpi.f90 #计算输入的压力比PI的流速
   writeboun.f90 #将MPC写入标准输出
   writebv.f90 #将屈曲力系数写入5号
   writecvg.f90 #在.cvg文件中写入收敛信息
   writedeigdx.f90 #将本征频率相对于方向的导数写入.dat文件中
   writedesi.f90 #将方向设计变量写入.dat文件
   writeelem.f90 #如果发现单元计数与frd文件中存储的单元数量不一致，则调用此例程
   writeevcomplex.f90 #将特征值写入.dat文件
   writeevcscomplex.f90 #将复特征值写入.dat文件
   writeevcs.f90 #将特征值写入3号
   writeev.f90 #将特征值写入.dat文件，并用其平方根=频率（单位为rad/时间）替换特征值
   writeheading.c #在frd文件的开头写入.inp文件的*HEADING的内容
   writehe.f90 #在.dat文件中为每个本征频率写入一个header
   writeim.f90 #同上
   writeinput.f90 #将inpc,ipoinp,inp,ipoinpc写入到文件中，debug时可用
   writelm.f90 # 计算投影梯度
   writemaccs.f90 #将MAC计算结果写入*_MAC.dat
   writemac.f90 #将MAC计算结果写入*_MAC.dat
   writematrix.f90 #将矩阵写入文件
   writemeshinp.f90 #网格
   writempc.f90 #将MPC写入标准输出
   writenewmesh.c #在网格细化计算中写入新网格
   writeobj.f90 #将目标函数的结果写入.dat文件
   writeoldmesh.c #网格细化计算中写入旧网格
   writepf.f90 #将参与系数写入5号
   writerandomfield.f90 #将randomfield的误差度量写入.dat文件中
   writere.f90 #在.dat文件中为每个本征频率写入一个标头
   writerefinemesh.f90 #
   writesen.f90 #将“原始”敏感性写入jobname.sen文件
   writestadiv.f90 #在.sta文件中写入增量统计信息
   writesta.f90 #在.sta文件中写入增量统计信息
   writesubmatrix.f90 #将子结构的矩阵写入.mtx文件
   writetetmesh.f90 #
   writetrilinos.f90 #
   writeturdircs.f90 #
   writeturdir.f90 #将特征值写入.dat文件
   writevector.f90 #将向量写入文件（用于调试目的）
   writevfa.f90 #写入face值
   writeview.f90 #将视角因子写入文件
   wye.f90 #Y型单元
   xlocal.f90 #单元面内的三维局部高斯点
   zeta_calc.f90 #计算不同部分总水头损失限制器的不同ζ指数
   zienzhu.f90 #修正的zienkiewicz-zhu逐点误差估计器
   ```
