# 编译记录

1. 下载Calculix.tar.gz文件，解压后会出现CCX目录，内部含有SPOOLES2.2，ARAPCK和Calculix三个文件夹。
2. 先构建SPOOLES2.2和ARAPCK，最后构建Calculix。三个文件夹放在同一级目录中，但不要求都放在用户家目录中，因为makefile中大多数为相对路径。
3. SPOOLES2.2的Tree/src/makeGlobalLib文件中包含了一个错误的引用应该将 file drawTree.c 改成file draw.c，因为drawTree.c不存在。
4. 进入SPOOLES.2.2中执行 make CC=gcc lib。如果不加CC=gcc会报错:/usr/lang-4.0/bin/cc: No such file or directory。
5. 进入ARPACK文件夹，先根据README修改ARmake.inc文件。
   1. 修改home为ARPACK文件夹路径
   2. 修改PLAT = INTEL
   3. 修改FFLAGS = -O -fallow-argument-mismatch。这里去除了-cg89的选项，增加了-fallow-argument-mismatch
   4. 修改UTIL/second.f，在EXTERNAL ETIME的最开头添加*注释
   5. 最后运行make lib即可
6. 在Calculix/ccx_2.20/src中执行make。如果遇到 Interface mismatch in dummy procedure ‘f’ at (1): ‘fun’ is not a function的错误。单独编译该文件，应该加上 --std=legacy的选项。
7. 执行 ./ccx_2.20 ../test/beamp，检查是否出现beamp.dat文件，可以beamp.dat.ref校对检验软件是否成功编译。
8. 也可以调用test/compare脚本来检验软件是否成功编译。这一步会计算test中的所有inp文件并比较。

# 文件结构

1. 注意CalculiX.h的X是大写，书写Makefile的依赖和包含头文件时不要写错。

2. 程序内有Bug，如果修改SFREE的宏，使得其每次释放内存后，都将指针置为NULL，则运行时会报错，卡住在extraploate.f90，ielorien指针在这里已经是NULL了，结果这里还使用了它。当然也不排除是因为修改了太多的源代码导致的。

3. dyna.c文件中出现如下笔误：

   ```c
   SFREE(xboundiff), SFREE(xbodydiff); //如果SFREE不包含将指针置为NULL的动作，则不会有问题，反之则会报错。
   ```

4. 源文件目录中

   1. 一共有942个.f90文件，但是gauss.f90和xlocal.f90只是被include到其他文件中，并不会单独编译，因此Makifile.inc中SCCXF一共包含940个.f90文件。
   2. 一共有176个.c源文件，而主文件ccx_2.20.c需要单独编译，因此Makefile.inc中SCCXC只包含175个.c文件

5. 使用代码统计工具cloc统计文件数，空白行，注释行，代码行的总数：

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

6. 经过统计，代码行比较多的文件如下：

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

7. Makefile的实际执行顺序为：

   ```shell
   #1.编译ccx_2.20.c主文件
   gcc -O2  -I ../../../SPOOLES.2.2 -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT -g   -c -o ccx_2.20.o ccx_2.20.c
   #2.编译SCCXF中的940个.f90文件
   gfortran -O2 --std=legacy  -c str2mat.f90
   #3.编译SCCXC中的175个.c文件
   gcc -O2  -I ../../../SPOOLES.2.2 -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT -g   -c -o writeoldmesh.o writeoldmesh.c
   #4.打包所有的目标文件到静态库文件
   ar vr ccx_2.20.a absolute_relative.o ...
   #5.修改三个重要文件中的时间标志
   ./date.pl;
   #6.重新编译ccx_2.20.c，不过前面修改了三个文件，这里只重新编译了一个。
   gcc -O2  -I ../../../SPOOLES.2.2 -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT -g -c ccx_2.20.c;
   #使用gfortran链接所有的文件，生成可执行文件ccx_2.20
   gfortran  -Wall -O2 -o ccx_2.20 ccx_2.20.o ccx_2.20.a ../../../SPOOLES.2.2/spooles.a ../../../ARPACK/libarpack_INTEL.a -lpthread -lm -lc -fopenmp
   ```

8. Makefile：

   ```makefile
   CFLAGS =  -Wall -O2  -I ../../../SPOOLES.2.2 -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT -g #指定SPOOLES头文件的目录，定义宏SPOOLES和ARPACK表示使用这两个库，-g调试
   FFLAGS =  -Wall -O2 --std=legacy #设置--std=legacy会使得gfortran8及以上的编译器在编译老代码中不再被支持的特性时，不会报错
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
   	./date.pl; #修改三个重要文件中的时间标志
   	$(CC) $(CFLAGS) -c ccx_2.20.c; #单独编译主文件
   	$(FC) $(FFLAGS) -o $@ $(OCCXMAIN) ccx_2.20.a $(LIBS) -fopenmp #使用gfortran进行链接。
   #打包所有的目标文件到静态库文件
   ccx_2.20.a: $(OCCXF) $(OCCXC)
   	ar vr $@ $?
   clean:
   	rm -f *.o *.a
   ```

9. date.pl，功能是在ccx_2.20.c，ccx_2.20step.c，frd.c中插入当前编译的时间，方便编译调试：

   ```perl
   #!/usr/bin/env perl
   chomp($date=`date`); #执行shell命令date，获取日期时间，存储到date变量中，chomp表示去掉结尾的换行符
   # inserting the date into ccx_2.20.c
   @ARGV="ccx_2.20.c";
   $^I=".old"; #先将ccx_2.20.c打开，并另存为ccx_2.20.c.old，然后再ccx_2.20.c上修改
   while(<>){ #<>表示从@ARGV中读取内容
       s/You are using an executable made on.*/You are using an executable made on $date\\n");/g; #正则表达式，搜索然后替换
       print;
   }
   # inserting the date into ccx_2.20step.c
   @ARGV="ccx_2.20step.c";
   $^I=".old";
   while(<>){
       s/You are using an executable made on.*/You are using an executable made on $date\\n");/g;
       print;
   }
   # inserting the date into frd.c
   @ARGV="frd.c";
   $^I=".old";
   while(<>){
       s/COMPILETIME.*/COMPILETIME       $date                    \\n\",p1);/g;
       print;
   }
   system "rm -f ccx_2.20.c.old"; #删除掉备份的旧文件，保留修改后的文件
   system "rm -f ccx_2.20step.c.old";
   system "rm -f frd.c.old";
   ```

10. cleanupcode，功能是清理编译产生的中间文件和可执行文件，不过这个功能已经被集成到makefile中了，使用make clean即可：

    ```shell
    #!/bin/sh
    for x in *.f *.c  #遍历所有的.f和.c文件文件
    do
        if [ "$x" = "CalculiX.c" ]; then
    	echo $x "is kept"
    	continue
        fi
        if [ "$x" = "gauss.f" ]; then
    	echo $x "is kept"
    	continue
        fi
        if [ "$x" = "xlocal.f" ]; then
    	echo $x "is kept"
    	continue
        fi
        if grep -q $x Makefile.inc #观察文件是否是Makefile.inc记录的
        then
    	echo $x "is kept"
        else
    	echo $x "is deleted"
    	rm -f $x
        fi
    done
    ```

11. hwloc可以显示CPU拓扑，比较方面地查看CPU各级缓存以及各个核、物理CPU之间，可以共享哪一级别的CPU cache。

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

12. task.json，用于生成可执行文件，点击菜单栏的终端→运行生成任务，可以执行默认任务，需要打开该项目的一个文件，否则会提示无法解析fileDirname变量：

    ```json
    {
        "tasks": [
            {
                "type": "cppbuild",
                "label": "构建ccx_2.20",
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
            }
        ],
        "version": "2.0.0"
    }
    ```

13. launch.json，用于启动调试：

    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "(gdb) 启动",
                "type": "cppdbg",
                "request": "launch",
                "program": "${workspaceFolder}/ccx_2.20", //设置可执行文件的完整路径，${workspaceFolder}为当前工作空间的位置，是/home/zj/CCX/CalculiX/ccx_2.20/src。
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

14. settings.json，这里保存工作区的设置：

    ```json
    {
        "files.associations": {
            "*.py": "python",
            "*.oth": "xml",
            "*.f": "FortranFixedForm",
            "calculix.h": "c",
            "string.h": "c"
        }
    }
    ```

15. c_cpp_properties.json，用于控制IntelliSense的高亮：

    ```json
    {
        "configurations": [
            {
                "name": "Linux", // 系统名称
                "includePath": [ // 头文件路径
                    "../../../SPOOLES.2.2"
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
   tar -czvf CalculiX-`date +%F`.tar.gz CCX #会生成一个类似CalculiX-2024-03-05.tar.gz的文件。
   ```

3. 执行如下命令解压缩：

   ```shell
   tar -xzvf CalculiX*.tar.gz #或者使用x命令。
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

1. 官方提供的例子，也可以用于校验编译结果是否正确：

   ```shell
   #!/bin/sh
   export OMP_NUM_THREADS=1
   rm -f error.*      #删除掉之前生成的错误文件
   tempfile=temp.$$   #$$表示当前进程的PID，一般用于生成唯一的文件名
   errorfile=error.$$
   #逐个对每个.inp文件进行处理
   for i in *.inp; do
           echo " "
           echo "example ${i%.inp}"
           echo " "
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
   # 删除掉之前运行产生的对应的.dat和.frd文件
   	rm -f ${i%.inp}.dat  #${i%.inp}表示从i的末尾去掉.inp
   	rm -f ${i%.inp}.frd
   # 执行Calculix，生成.dat和.frd文件，将命令行输出保存到tempfile文件。需要的话可以修改可执行文件的路径
           ~/CalculiX/CalculiX  ${i%.inp} >> $tempfile 2>&1
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
   echo "check the existence of file $errorfile" #检查是否存在errorfile，如果不存在，则表明计算结果和参考结果的误差可忽略不计
   echo "if this file does not exist, the present results"
   echo "agree with the reference results"
   echo " "
   ```

2. 


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

3. 

4. 

5. 

6. 
