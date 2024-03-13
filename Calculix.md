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

1. 在ccx_2.20.c中包含了，主要是定义了有些简短的宏，用来简化函数调用，：

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

3. 可以在.bashrc中添加export CCX_LOG_ALLOC=1，来输出内存释放分配的日志，它会混合原来的求解器输出到屏幕上。

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

4. 


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
   流号  文件名
   1    jobname.inp #输入文件
   5    jobname.dat #输出的结果
   7    jobname.frd #结果数据库文件，类似于abaqus的.odb文件
   8    jobname.sta #
   11   jobname.cvg #收敛状态文件
   12   jobname.fcv #
   15   jobname.rout#重启动相关
   27   jobname.cel #接触单元
   ```

2. Fortran使用//拼接字符串，这句代码会被翻译成多个函数调用：

   ```fortran
   fndat=jobname(1:i)//'.dat' !如果再调试时，需要跳过过程
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

3. 安装Ctags Companion扩展。然后执行终端→运行任务→显示所有任务→Ctags Companion: rebuild ctags即可生成tags文件。之后可以使用F12，CTRL+单击来进行跳转。

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

9. 也可以将多个文件夹添加到同一个工作区, 此时, 工作区需要单独保存为一个 code-workspace 文件。

10. 如果在VSCode remote中使用ranger，右键打开文件时，报错：`xdg-open unexpected option: '--'`。此时可以进行如下操作：

    ```shell
    ranger --copy-config=all #命令行执行如下命令，生成ranger的配置文件，在~/.config/ranger目录下。
    #在~/.config/ranger/rifle.conf文件中找到下面的内容。将下面的 xdg-open -- "$@"改为${VISUAL:-$EDITOR} -- "$@"。这样就会使用select-editor选中的编辑器打开了。
    label open, has xdg-open = ${VISUAL:-$EDITOR} -- "$@"
    label open, has open     = open -- "$@"
    ```

11. task.json，用于生成可执行文件：

    ```
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

12. launch.json，用于启动调试：

    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "(gdb) 启动",
                "type": "cppdbg",
                "request": "launch",
                "program": "${workspaceFolder}/ccx_2.20", //设置可执行文件的完整路径
                "args": [ //命令行参数
                    "-input",
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

13. settings.json，这里保存工作区的设置：

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

14. c_cpp_properties.json，用于控制IntelliSense的高亮：

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

2. 执行如下命令打包并压缩：

   ```shell
   tar -czvf CalculiX-`date +%F`.tar.gz CCX #会生成一个类似CalculiX-2024-03-05.tar.gz的文件。
   ```

3. 执行如下命令解包并解压缩：

   ```shell
   tar -xzvf CalculiX*.tar.gz #或者使用x命令。
   ```

# 所有文件的作用

1. ```shell
   absolute_relative.f90 #孔口单元
   acctube.f90 # ACC(空冷式凝汽器)管单元
   acctube_one.f90 #同上
   actideacti.f90 # activate或deactivate某个set
   actideactistr.f90 #停用与应力目标函数集内的节点不相邻的单元
   add_bo_st.f90 #向稀疏矩阵格式中的刚度矩阵中存储边界刚度系数
   addimd.f90 #将node添加到imd域中，imd包含了用户指定的那些要在模态动力学中计算结果的实体
   addimdnodecload.f90 # adds the dof in which a user-defined point force was applied to imdnode，用户自定义集中力
   addimdnodedload.f90 # adds the nodes belonging to a user-defined facial load to imdnode，用户自定义面力
   addimdnodedof.f90 #模态动力学计算相关
   addizdofcload.f90 #
   addizdofdload.f90 #
   add_sm_ei.f90 #存储刚度系数相关
   add_sm_fl.f90 # fl表示流体
   add_sm_st_as.f90 #
   add_sm_st_corio.f90 #科里奥利修正
   add_sm_st.f90 #
   adjacentbounodes.f90 #根据邻接性对裂纹边界节点进行排序
   adjustcontactnodes.f90 #根据用户的要求调整接触节点
   addshell.f90 # 更新真实壳体的平移和旋转自由度
   advecforc.f90 #计算平流单元的刚度 advection是平流，convection是对流。
   advecstiff.f90 #同上
   air_valve.f90 # 空气阀，专有代码，具体实现代码已经被删除
   allocation.f90 #计算要分配的域大小的保守估计
   allocation_rfn.f90 #
   allocont.f90 #计算三角化接触主表面所需的三角形数量
   amplitudes.f90 #读取*AMPLITUDE关键字
   angsum.f90 #计算与节点相邻的单元边的所有空间角之和
   anisomaxwavspd.f90 #计算各向异性材料中的传播波速度，最大为21常数
   anisonl.f90 #
   anisotropic.f90 #将21个各向异性弹性常数扩展为3x3x3矩阵
   applybounfem.f90 #应用温度和速度SPC
   applybounp.f90 #应用速度边界条件
   approxplane.f90 #计算通过四边形边缘并平行于矢量xn的平面的方程
   assigndomtonodes.f90 # 电磁学中使用
   attach_1d.f90 #将节点附着到线上
   attach_2d.f90 #
   attach_3d.f90 #
   attachline.f90 #返回由节点坐标描述的面的局部坐标
   auglag_inclusion.f90 #接触相关
   autocovmatrix.f90 #计算自协方差矩阵的值
   basemotions.f90 #读取*BASE MOTION关键字
   basis.f90 #将主网格中的场插值到任意位置p处的新节点上
   beamextscheme.f90 #为横截面不是矩形也不是椭圆形的梁提供了外插方案
   beamgeneralsections.f90 #读取*BEAM SECTION关键字，为PIPE, BOX and GENERAL三种类型
   beamintscheme.f90 #为横截面不是矩形也不是椭圆形的梁提供了积分方案
   beammpc.f90 #为彼此保持恒定距离的两个节点生成MPC
   beamsections.f90 #读取*BEAM SECTION关键字
   biotsavart.f90 # 计算电流引起的磁场强度，毕奥萨伐尔定律
   bodyadd.f90 #将体积化的dload条件添加到数据库
   bodyforce.f90 #通过使用field ipobody将体积力指定给单元
   bounadd.f90 #将一个边界条件添加到数据库
   bounaddf.f90 #将一个面边界条件添加到数据库
   boundaryfs.f90 #读取*BOUNDARYF关键字
   boundarys.f90 #读取*BOUNDARY关键字
   bsort.f90 #二分插入排序
   buckles.f90 #读取*BUCKLE关键字
   calcdatarget.f90 #计算裂纹扩展增量
   calcdev.f90 #计算解的改变
   calcdhds.f90 #计算流体在光滑和粗糙管道中的摩擦系数
   calceigenvalues.f90 #计算对称3x3矩阵的特征值，特征值按递增顺序排序
   calcenergy.f90 #计算*DYNAMIC计算中的能量
   calcexternalwork.f90 #升力和阻力的计算和打印
   calcgeomelemnet.f90 #计算柔性网络单元和用户定义网络单元的横截面积
   calch0interface.f90 #mpc相关
   calcheatnet.f90 #用户子程序film
   calc_ider_cross_split.f90 #
   calc_ider_tee.f90 #
   calc_ider_wye.f90 #
   calcmac.f90 #计算模态置信矩阵，也就是振型相关系数
   calcmach.f90 #计算比热比和马赫数
   calcmass.f90 #计算单元质量
   calcmechstrain.f90 #根据位移梯度和热拉伸计算力学应变
   calcnormal.f90 #确定单元某个面的局部法线方向
   calc_residual_cross_split.f90 #
   calc_residual_tee.f90 #
   calc_residual_wye.f90 #
   calcspringforc.f90 #计算弹簧力和弹簧能量，对应于node-surface罚函数
   calcstabletimeinccont.f90 #
   calcstabletimeincvol.f90 #
   calcstressheatfluxfem.f90 #
   calcsurf.f90 #
   calctotstrain.f90 #
   calculated.f90 #
   calculateh.f90 #
   calculatehmid.f90 #
   calcview.f90 #
   calcvol.f90 #
   calinput.f90 #
   calinput_rfn.f90 #
   carbon_seal.f90 #
   catedges_crackprop.f90 #
   catedges_refine.f90 #
   catnodes.f90 #
   catsmpcslavno.f90 #
   cattet.f90 #
   cattri.f90 #
   cavity_refine.f90 #
   cavityext_refine.f90 #
   cd_bleedtapping.f90 #
   cd_bragg.f90 #
   cd_chamfer.f90 #
   cd_lab_1spike.f90 #
   cd_lab_correction.f90 #
   cd_lab_honeycomb.f90 #
   cd_lab_radius.f90 #
   cd_lab_straight.f90 #
   cd_lichtarowicz.f90 #
   cd_Mcgreehan_Schotsch.f90 #
   cd_ms_ms.f90 #
   cd_own_albers.f90 #
   cd_pk_albers.f90 #
   cd_pk_ms.f90 #
   cd_preswirlnozzle.f90 #
   cfdconv.f90 #
   cfds.f90 #
   cflux.f90 #
   cfluxs.f90 #
   changedepterm.f90 #
   changefrictions.f90 #
   changekon.f90 #
   changematerials.f90 #
   changeplastics.f90 #
   changesolidsections.f90 #
   changesurfacebehaviors.f90 #
   characteristic.f90 #
   characteristiclength.f90 #
   checkconstraint.f90 #
   checkexiedge.f90 #
   checkforhomnet.f90 #
   checkimpacts.f90 #
   checkinputvaluesnet.f90 #
   checkintegrity.f90 #
   checkjac.f90 #
   checkprojectgrad.f90 #
   checksharp.f90 #
   checkspcmpc.f90 #
   checktemp.f90 #
   checktime.f90 #
   checktruecontact.f90 #
   checkvol.f90 #
   chksurf.f90 #
   cident80.f90 #
   cident81.f90 #
   cident.f90 #
   clearances.f90 #
   cload.f90 #
   cloaddistributing.f90 #
   cloads.f90 #
   clonesensitivities.f90 #
   closefile.f90 #
   closefilefluid.f90 #
   cmatrix.f90 #
   combilcfhcf.f90 #
   compdt.f90 #
   complexfrequencys.f90 #
   con2phys.f90 #
   condrandomfield.f90 #
   conductivitys.f90 #
   constraints.f90 #
   contactdampings.f90 #
   contactpairs.f90 #
   contactprints.f90 #
   contingentsurf.f90 #
   contraction.f90 #
   controlss.f90 #
   coriolissolve.f90 #
   correctem.f90 #
   correlationlengths.f90 #
   couplings.f90 #
   couptempdisps.f90 #
   cp_corrected.f90 #
   cracklength.f90 #
   cracklength_smoothing.f90 #
   crackprop.f90 #
   crackpropagations.f90 #
   crackrate.f90 #
   crackshape.f90 #
   create_contactdofs.f90 #
   createbd.f90 #
   createblock_struct.f90 #
   createelemneigh.f90 #
   createfint.f90 #
   createialnk.f90 #
   createinterfacempcs.f90 #
   createinum.f90 #
   createlocalsys.f90 #
   createmddof.f90 #
   createmdelem.f90 #
   createnodeneigh.f90 #
   createtele.f90 #
   createteleinv.f90 #
   createteleinv_lin.f90 #
   createtele_lin.f90 #
   createtet.f90 #
   createtiedsurfs.f90 #
   creep.f90 #
   creeps.f90 #
   cross_split.f90 #
   cubic.f90 #
   cubtri.f90 #
   cyclichardenings.f90 #
   cyclicsymmetrymodels.f90 #
   dampings.f90 #
   dashdamp.f90 #
   dashpots.f90 #
   dattime.f90 #
   ddeabm.f90 #
   ddebdf.f90 #
   deformationplasticitys.f90 #
   defplas.f90 #
   delaun.f90 #
   deltri.f90 #
   densitys.f90 #
   depvars.f90 #
   designresponses.f90 #
   designvariabless.f90 #
   desiperelem.f90 #
   resforccont.f90 #
   detectactivecont.f90 #
   determineextern.f90 #
   dflux.f90 #
   dfluxs.f90 #
   dgesv.f90 #
   dgmres1.f90 #
   dgmres.f90 #
   disp_sen_dv.f90 #
   distattach_1d.f90 #
   distattach_2d.f90 #
   distattach_3d.f90 #
   distattachline.f90 #
   distributesens.f90 #
   distributingcouplings.f90 #
   distributions.f90 #
   dKdm.f90 #
   dKdp.f90 #
   dKdt.f90 #
   dKdX.f90 #
   dload.f90 #
   dloads.f90 #
   dlz.f90 #
   dmatrix.f90 #
   dqag.f90 #
   drfftf.f90 #
   dsort.f90 #
   dsptrf.f90 #
   dsptri.f90 #
   dualshape3tri.f90 #
   dualshape4q.f90 #
   dualshape6tritilde.f90 #
   dualshape6tritilde_lin.f90 #
   dualshape8qtilde.f90 #
   dualshape8qtilde_lin.f90 #
   dynamics.f90 #
   dynresults.f90 #
   e_c3d_cs_se.f90 #
   e_c3d_duds.f90 #
   e_c3d_em.f90 #
   e_c3d.f90 #
   e_c3d_plhs.f90 #
   e_c3d_prhs.f90 #
   e_c3d_rhs.f90 #
   e_c3d_rhs_th.f90 #
   e_c3d_se.f90 #
   e_c3d_th.f90 #
   e_c3d_u1.f90 #
   e_c3d_us3.f90 #
   e_c3d_us45.f90 #
   e_c3d_u.f90 #
   e_c3d_vlhs.f90 #
   e_c3d_v1rhs.f90 #
   e_c3d_v2rhs.f90 #
   e_corio.f90 #
   e_damp.f90 #
   edgedivide.f90 #
   edg.f90 #
   effectivemodalmass.f90 #
   elastics.f90 #
   electricalconductivitys.f90 #
   electromagneticss.f90 #
   elementpernode.f90 #
   elementpernodef.f90 #
   elements.f90 #
   elemperdesi.f90 #
   elemperorien.f90 #
   elprints.f90 #
   envtemp.f90 #
   eplane.f90 #
   eqspacednodes.f90 #
   equationcheck.f90 #
   equationfs.f90 #
   equations.f90 #
   errorestimator.f90 #
   evalshapefunc.f90 #
   expand_auw.f90 #
   expansions.f90 #
   extendmesh.f90 #
   extern_crackprop.f90 #
   extfacepernode.f90 #
   extract_matrices.f90 #
   extrapol2dto3d.f90 #
   extrapolatecontact.f90 #
   extrapolate.f90 #
   extrapolatefem.f90 #
   extrapolateshell.f90 #
   extrapolateshell_us3.f90 #
   extrapolateshell_us45.f90 #
   extrapolate_se.f90 #
   extrapolate_u.f90 #
   extrapolate_u1.f90 #
   extrapolate_us3.f90 #
   extrapolate_us45.f90 #
   faceinfo.f90 #
   fcrit.f90 #
   feasibledirections.f90 #
   fillknotmpc.f90 #
   film.f90 #
   films.f90 #
   filter.f90 #
   filters.f90 #
   findextsurface.f90 #
   findslavcfd.f90 #
   findsurface.f90 #
   fixnode.f90 #
   flowbc.f90 #
   flowoutput.f90 #
   fluidconstantss.f90 #
   fluidsections.f90 #
   flux.f90 #
   fminsirefine.f90 #
   forcadd.f90 #
   forcesolve.f90 #
   frdfluidfem.f90 #
   frditeration.f90 #
   free_convection.f90 #
   free_disc_pumping.f90 #
   frequencys.f90 #
   fricheat.f90 #
   friction_coefficient.f90 #
   frictionheating.f90 #
   frictions.f90 #
   fsub.f90 #
   fsuper.f90 #
   fumid.f90 #
   fuvertex.f90 #
   gapconductances.f90 #
   gapcon.f90 #
   gapheatgenerations.f90 #
   gaps.f90 #
   gasmechbc.f90 #
   gaspipe_fanno.f90 #
   gaspipe_rot.f90 #
   gen3dboun.f90 #
   gen3dconnect.f90 #
   gen3delem.f90 #
   gen3dforc.f90 #
   gen3dfrom1d.f90 #
   gen3dfrom2d.f90 #
   gen3dmembrane.f90 #
   gen3dmpc.f90 #
   gen3dnor.f90 #
   gen3dsurf.f90 #
   gen3dtemp.f90 #
   gen3dtruss.f90 #
   genadvecelem.f90 #
   gencontelem_f2f.f90 #
   gencontelem_n2f.f90 #
   gendualcoeffs.f90 #
   generatecycmpcs.f90 #
   generateeminterfaces.f90 #
   generatetet_refine2.f90 #
   generatetet_refine.f90 #
   genfirstactif.f90 #
   genislavactdof.f90 #
   genislavelinv.f90 #
   genmidnodes.f90 #
   genmodes.f90 #
   genmpc.f90 #
   gennactdofinv.f90 #
   genratio.f90 #
   gentiedmpc.f90 #
   geometricconstraints.f90 #
   geometrictolerances.f90 #
   geomview.f90 #
   getcontactparams.f90 #
   getdesiinfo2d.f90 #
   getdesiinfo3d.f90 #
   getdesiinfo3d_robust.f90 #
   getdesiinfobou.f90 #
   getlocno.f90 #
   getnewline.f90 #
   getnodel.f90 #
   getnodesinitetmesh.f90 #
   getnumberofnodes.f90 #
   getversion.f90 #
   globalcrackresults.f90 #
   greens.f90 #
   hcfs.f90 #
   hcrit.f90 #
   headings.f90 #
   heattransfers.f90 #
   henergy.f90 #
   hgforce.f90 #
   hgstiffness.f90 #
   hnorm.f90 #
   hns.f90 #
   hybsvd.f90 #
   hyperelastics.f90 #
   hyperfoams.f90 #
   ident2.f90 #
   identamta.f90 #
   ident.f90 #
   identifytiedface.f90 #
   identifytransform.f90 #
   includefilename.f90 #
   incplas.f90 #
   incplas_lin.f90 #
   init_submodel.f90 #
   initialcfdfem.f90 #
   initialchannel.f90 #
   initialconditionss.f90 #
   initialnet.f90 #
   initialstrainincreases.f90 #
   inputerror.f90 #
   inputinfo.f90 #
   inputwarning.f90 #
   insertsortd.f90 #
   insertsorti.f90 #
   interpol_alfa2.f90 #
   interpolateinface.f90 #
   interpolatestate.f90 #
   interpolextnodes.f90 #
   interpolextnodesf.f90 #
   interpolsubmodel.f90 #
   interpoltet.f90 #
   intersectionpoint.f90 #
   inversewavspd.f90 #
   inviscidpre.f90 #
   islavactive.f90 #
   isortic.f90 #
   isortiddc.f90 #
   isortid.f90 #
   isorti.f90 #
   isortii.f90 #
   isortiiddc.f90 #
   isortiid.f90 #
   isortiii.f90 #
   jouleheating.f90 #
   keystart.f90 #
   knotmpc.f90 #
   lab_straight_ppkrit.f90 #
   labyrinth.f90 #
   limit_case_calc.f90 #
   linel.f90 #
   linkdissimilar.f90 #
   linscal10.f90 #
   linscal.f90 #
   lintemp.f90 #
   lintemp_th0.f90 #
   lintemp_th1.f90 #
   lintemp_th.f90 #
   linvec10.f90 #
   linvec.f90 #
   liquidpipe.f90 #
   liquidpump.f90 #
   loadadd.f90 #
   loadaddp.f90 #
   loadaddt.f90 #
   localaxescs.f90 #
   localaxes.f90 #
   lump.f90 #
   machpi.f90 #
   mafillcorio.f90 #
   mafilldm.f90 #
   mafilldmss.f90 #
   mafillem.f90 #
   mafillfreq_em.f90 #
   mafillnet.f90 #
   mafillpbc.f90 #
   mafillplhs.f90 #
   mafillprhs.f90 #
   mafillsm.f90 #
   mafillsmas.f90 #
   mafillsmcsas.f90 #
   mafillsmcs.f90 #
   mafillsmcsse.f90 #
   mafillsmduds.f90 #
   mafillsmforc.f90 #
   mafillsmse.f90 #
   mafillv1rhs.f90 #
   mafillv2rhs.f90 #
   mafillvlhs.f90 #
   magneticpermeabilitys.f90 #
   map3dto1d2d.f90 #
   map3dto1d2d_v.f90 #
   map3dtolayer.f90 #
   massflow_percent.f90 #
   massflows.f90 #
   masss.f90 #
   materialdata_cond.f90 #
   materialdata_cp.f90 #
   materialdata_cp_sec.f90 #
   materialdata_crack.f90 #
   materialdata_dvi.f90 #
   materialdata_dvifem.f90 #
   materialdata_em.f90 #
   materialdata_me.f90 #
   materialdata_rho.f90 #
   materialdata_sp.f90 #
   materialdata_tg.f90 #
   materialdata_th.f90 #
   materials.f90 #
   matvec.f90 #
   matvec_struct.f90 #
   mechmodel.f90 #
   membranesections.f90 #
   merge_ikactmech1.f90 #
   meshquality.f90 #
   meshqualitycavity.f90 #
   midexternaledges.f90 #
   midexternalfaces.f90 #
   modaldampings.f90 #
   modaldynamics.f90 #
   modelchanges.f90 #
   modf.f90 #
   modifympc.f90 #
   moehring.f90 #
   mpcadd.f90 #
   mpcrem.f90 #
   mpcs.f90 #
   msolve.f90 #
   msolve_struct.f90 #
   mulmatvec_asym.f90 #
   mult.f90 #
   multistages.f90 #
   multvec.f90 #
   near2d.f90 #
   near3d.f90 #
   near3d_se.f90 #
   neartriangle.f90 #
   negativepressure.f90 #
   networkelementpernode.f90 #
   networkextrapolate.f90 #
   networkforc.f90 #
   networkinum.f90 #
   networkmpc_lhs.f90 #
   networkmpc_rhs.f90 #
   networkmpcs.f90 #
   networkneighbor.f90 #
   networkstiff.f90 #
   newnodes.f90 #
   newton.f90 #
   nident2.f90 #
   nident.f90 #
   nidentk.f90 #
   nidentll.f90 #
   nmatrix.f90 #
   noanalysiss.f90 #
   nodalthicknesss.f90 #
   nodeprints.f90 #
   nodes.f90 #
   nodestiedface.f90 #
   noelfiles.f90 #
   noelsets.f90 #
   nonlinmpc.f90 #
   normals.f90 #
   normalsforequ_se.f90 #
   normalsoninterface.f90 #
   normalsonsurface_robust.f90 #
   normalsonsurface_se.f90 #
   normmpc.f90 #
   norshell3.f90 #
   norshell4.f90 #
   norshell6.f90 #
   norshell8.f90 #
   nortanslav.f90 #
   objective_disp.f90 #
   objective_disp_tot.f90 #
   objective_freq_cs.f90 #
   objective_freq.f90 #
   objective_mass_dx.f90 #
   objective_modalstress.f90 #
   objective_peeq.f90 #
   objective_peeq_se.f90 #
   objective_shapeener_dx.f90 #
   objective_shapeener_tot.f90 #
   objective_stress_dx_dy.f90 #
   objective_stress.f90 #
   objective_stress_se.f90 #
   objective_stress_tot.f90 #
   objectives.f90 #
   onedint.f90 #
   opas.f90 #
   op_corio.f90 #
   openfile.f90 #
   openfilefluidfem.f90 #
   op.f90 #
   opnonsym.f90 #
   opnonsymt.f90 #
   orientations.f90 #
   orifice.f90 #
   orthonl.f90 #
   orthotropic.f90 #
   outputs.f90 #
   patch.f90 #
   phys2con.f90 #
   physicalconstantss.f90 #
   pk_cdc_cl1.f90 #
   pk_cdc_cl3a.f90 #
   pk_cdc_cl3b.f90 #
   pk_cdc_cl3d.f90 #
   pk_cdc_cl3.f90 #
   pk_cdi_noz.f90 #
   pk_cdi_r.f90 #
   pk_cdi_rl.f90 #
   pk_cdi_se.f90 #
   pk_y0_yg.f90 #
   plane3.f90 #
   plane4.f90 #
   plane_eq.f90 #
   planeeq.f90 #
   planempc.f90 #
   plastics.f90 #
   plcopy.f90 #
   plinterpol.f90 #
   plmix.f90 #
   pop.f90 #
   postinitialnet.f90 #
   postprojectgrad.f90 #
   postview.f90 #
   precfdcyc.f90 #
   preconditioning.f90 #
   precondrandomfield.f90 #
   predgmres_struct.f90 #
   prefilter.f90 #
   preinitialnet.f90 #
   preprojectgrad.f90 #
   presgradient.f90 #
   pretensionsections.f90 #
   prethickness.f90 #
   pretransition.f90 #
   printoutcontact.f90 #
   printoutebhe.f90 #
   printoutelem.f90 #
   printout.f90 #
   printoutface.f90 #
   printoutfacefem.f90 #
   printoutfluidfem.f90 #
   printoutint.f90 #
   printoutintfluidfem.f90 #
   printoutnode.f90 #
   printoutnodefluid.f90 #
   printoutnodefluidfem.f90 #
   projectgrad.f90 #
   projectmidnodes.f90 #
   projectvertexnodes.f90 #
   propertynet.f90 #
   pt2_lim_calc.f90 #
   pt2zpt1_crit.f90 #
   pt2zpt1_rot.f90 #
   push.f90 #
   qsorti.f90 #
   quadmeshquality.f90 #
   quadraticsens.f90 #
   radiate.f90 #
   radiates.f90 #
   radmatrix.f90 #
   radresult.f90 #
   randomfields.f90 #
   randomval.f90 #
   ranstarefine.f90 #
   ranuwh.f90 #
   rcavi2.f90 #
   rcavi_cp_lt.f90 #
   rcavi_cp_nt.f90 #
   rcavi.f90 #
   readforce.f90 #
   readsen.f90 #
   readview.f90 #
   rearrange.f90 #
   rearrangecfd.f90 #
   rectcylexp.f90 #
   rectcyl.f90 #
   rectcylvi.f90 #
   rectcylvold.f90 #
   reducematrix.f90 #
   refinemeshs.f90 #
   regularization_gn_c.f90 #
   regularization_gt_c.f90 #
   regularization_slip_iwan.f90 #
   regularization_slip_lin.f90 #
   reinit_refine.f90 #
   relaxval_al.f90 #
   removesliver.f90 #
   removetet_refine.f90 #
   removetet_sliver.f90 #
   reorderampl.f90 #
   reservoir.f90 #
   restartread.f90 #
   restarts.f90 #
   restartshort.f90 #
   restartwrite.f90 #
   restrictor.f90 #
   resultnet.f90 #
   resultsem.f90 #
   resultsforc_em.f90 #
   resultsforc_se.f90 #
   resultsini_em.f90 #
   resultsini_mortar.f90 #
   resultsk.f90 #
   resultsmech.f90 #
   resultsmech_se.f90 #
   resultsmech_u1.f90 #
   resultsmech_us3.f90 #
   resultsmech_us45.f90 #
   resultsmech_u.f90 #
   resultsnoddir.f90 #
   resultsp.f90 #
   resultsprint.f90 #
   resultst.f90 #
   resultstherm.f90 #
   resultsv1.f90 #
   resultsv2.f90 #
   retainednodaldofss.f90 #
   rhs.f90 #
   rhsnodef.f90 #
   rigidbodys.f90 #
   rigidmpc.f90 #
   rimseal_calc.f90 #
   rimseal.f90 #
   robustdesigns.f90 #
   rotationvector.f90 #
   rotationvectorinv.f90 #
   rs.f90 #
   rubber.f90 #
   scalesen.f90 #
   scavenge_pump.f90 #
   sdvini.f90 #
   searchmidneigh.f90 #
   sectionprints.f90 #
   selectcyclicsymmetrymodess.f90 #
   sensitivitys.f90 #
   shape10tet.f90 #
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
   shellsections.f90 #
   sigini.f90 #
   skip.f90 #
   slavintmortar.f90 #
   slavintpoints.f90 #
   sluicegate.f90 #
   smalldist.f90 #
   smoothbadmid.f90 #
   smoothbadvertex.f90 #
   smoothingmidnodes.f90 #
   smoothingvertexnodes.f90 #
   smoothshock.f90 #
   solidsections.f90 #
   sortev.f90 #
   spcmatch.f90 #
   specificgasconstants.f90 #
   specificheats.f90 #
   splitline.f90 #
   spooles_read.f90 #
   spooles_write.f90 #
   springdamp_f2f.f90 #
   springdamp_n2f.f90 #
   springforc_f2f.f90 #
   springforc_f2f_th.f90 #
   springforc_n2f.f90 #
   springforc_n2f_th.f90 #
   springs.f90 #
   springstiff_f2f.f90 #
   springstiff_f2f_th.f90 #
   springstiff_n2f.f90 #
   springstiff_n2f_th.f90 #
   statics.f90 #
   steadystatedynamicss.f90 #
   steps.f90 #
   stiff2mat.f90 #
   stop.f90 #
   stopwithout201.f90 #
   storecontactprop.f90 #
   storeresidual.f90 #
   str2mat.f90 #
   straightchannel.f90 #
   straighteq2d.f90 #
   straighteq3d.f90 #
   straighteq3dpen.f90 #
   straightmpc.f90 #
   stressintensity.f90 #
   stressintensity_smoothing.f90 #
   submodels.f90 #
   subspace.f90 #
   substructuregenerates.f90 #
   substructurematrixoutputs.f90 #
   subtracthmatrix.f90 #
   surfacebehaviors.f90 #
   surfaceinteractions.f90 #
   surfaces.f90 #
   sutherland_hodgman.f90 #
   swap.f90 #
   tee.f90 #
   temperatures.f90 #
   temploaddiff.f90 #
   tempload_em.f90 #
   tempload.f90 #
   temploadfem.f90 #
   temploadmodal.f90 #
   thermmodel.f90 #
   thickness.f90 #
   tiefaccont.f90 #
   ties.f90 #
   timepointss.f90 #
   topocfdfem.f90 #
   totalcontact.f90 #
   transformatrix.f90 #
   transformfs.f90 #
   transforms.f90 #
   transition.f90 #
   treatmasterface.f90 #
   treatmasterface_mortar.f90 #
   trianeighbor.f90 #
   triangucont.f90 #
   triangulate.f90 #
   triloc.f90 #
   ts_calc.f90 #
   tt_calc.f90 #
   turningdirection.f90 #
   twodint.f90 #
   two_phase_flow.f90 #
   uamplitude.f90 #
   uboun.f90 #
   ufaceload.f90 #
   uhardening.f90 #
   umat_abaqus.f90 #
   umat_abaqusnl.f90 #
   umat_aniso_creep.f90 #
   umat_aniso_plas.f90 #
   umat_ciarlet_el.f90 #
   umat_compression_only.f90 #
   umat_elastic_fiber.f90 #
   umat.f90 #
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
   umpc_dist.f90 #
   umpc_mean_rot.f90 #
   umpc_user.f90 #
   uncouptempdisps.f90 #
   updatecon.f90 #
   updatecont2d.f90 #
   updatecont.f90 #
   updatecontpen.f90 #
   updategeodata.f90 #
   us3_sub.f90 #
   us4_sub.f90 #
   userelements.f90 #
   usermaterials.f90 #
   usermpc.f90 #
   usersections.f90 #
   user_network_element.f90 #
   user_network_element_p0.f90 #
   user_network_element_p1.f90 #
   utemp_ccxlib.f90 #
   utemp.f90 #
   valuesatinfinitys.f90 #
   varsmooth.f90 #
   velinireltoabs.f90 #
   viewfactors.f90 #
   viscos.f90 #
   vortex.f90 #
   wcoef.f90 #
   wpi.f90 #
   writeboun.f90 #
   writebv.f90 #
   writecvg.f90 #
   writedeigdx.f90 #
   writedesi.f90 #
   writeelem.f90 #
   writeevcomplex.f90 #
   writeevcscomplex.f90 #
   writeevcs.f90 #
   writeev.f90 #
   writehe.f90 #
   writeim.f90 #
   writeinput.f90 #
   writelm.f90 #
   writemaccs.f90 #
   writemac.f90 #
   writematrix.f90 #
   writemeshinp.f90 #
   writempc.f90 #
   writeobj.f90 #
   writepf.f90 #
   writerandomfield.f90 #
   writere.f90 #
   writerefinemesh.f90 #
   writesen.f90 #
   writestadiv.f90 #
   writesta.f90 #
   writesubmatrix.f90 #
   writetetmesh.f90 #
   writetrilinos.f90 #
   writeturdircs.f90 #
   writeturdir.f90 #
   writevector.f90 #
   writevfa.f90 #
   writeview.f90 #
   wye.f90 #
   zeta_calc.f90 #
   zienzhu.f90#
   
   
   add_rect.c #计算两个系数矩阵的和
   arpack.c # arpack相关
   arpackbu.c #
   arpackcs.c #
   bdfill.c #计算耦合矩阵，插入到数据结构中
   biosav.c #计算磁感应强度，毕奥萨伐尔定律
   buildtquad.c #计算转换矩阵
   calcresidual.c #计算残差
   calcresidual_em.c #
   calcshapef.c #确定流体网格的形函数和导数
   ccx_2.20step.c #
   call_external_umat.c #调用外部的umat
   call_external_umat_user.c #
   cascade.c #检测级联的mpc并将其拆分
   checkconvergence.c #检查是否收敛
   checkconvnet.c #检查动态收敛
   checkdivergence.c #检查radflowload.c中是否有发散信号
   checkinclength.c #检查新的增量大小是否不太大
   compare.c #比较字符串
   compfluidfem.c #主要CFD程序
   complexfreq.c #
   contact.c #接触
   contactmortar.c #在转换系统中使用双砂浆方法包含接触条件的函数
   convert2rowbyrow.c #矩阵操作
   cpypardou.c #并行版数组拷贝
   cpyparitg.c #
   crackfrd.c #将结果存储为frd格式
   crackpropagation.c #裂缝扩展
   crackpropdata.c #读取裂缝扩展数据的用户程序
   dam1parll.c #计算阻尼力的并行化
   dam2parll.c #
   dealloc_cal.c #释放所有的域，除了*inp外
   decascade_mortar.c #生成转换MPC的函数
   dfdbj.c #计算接触力相对于模态变量的导数
   dgmresmain.c #求解稀疏方程组
   divparll.c #数组除法的并行
   dudsmain.c #计算duds矩阵
   dyna.c #
   dynboun.c #
   electromagnetics.c #电磁学
   elemChecker.c #纠正未对齐的元素
   elementcpuload.c #为多个cpu并行，将单元分范围
   expand.c #调用Arnoldi包（ARPACK）进行循环对称性计算
   external.c #外部行为支持
   feasibledirection.c #基于灵敏度信息寻找可行方向
   filtermain.c #过滤灵敏度
   forparll.c #并行化计算resultsforc.c中的力
   frd.c #将结果存储为frd格式
   frdcyc.c #用于静态循环对称计算的重复域
   frdgeneralvector.c #
   frdheader.c #
   frdselect.c #
   frd_sen.c #
   frdset.c #
   frdvector.c #
   frecord.c #
   genrandmain.c #伪随机数发生器
   getglobalresults.c #
   getlocalresults.c # 按顺序编目所有四面体单元
   getSystemCPUs.c #确定可用核数
   getuncrackedresults.c #从文件中读取所有温度、位移、应力和力数据
   ini_cal.c #初始化和重新初始化
   inicont.c #确定主三角形和从实体的数量
   inimortar.c #初始化mortar接触
   iniparll.c #resultsini.c的并行部分
   insert_cmatrix.c #下三角矩阵，插入矩阵相关
   insertas.c # 在稀疏矩阵中插入新的非零矩阵位置
   insertas_ws.c # 在有序稀疏矩阵中插入新的非零矩阵位置
   insert.c #在数据结构中插入新的非零矩阵位置
   insertcbs.c #
   insertfreq.c #用于边界刚度系数
   insertrad.c #
   interpolatestatemain.c #
   interpoltetmain.c #
   linstatic.c #
   mafilldmssmain.c #
   mafillsmasmain.c #
   mafillsmmain.c #
   mafillsmmain_se.c #
   massless.c #确定无质量接触全局系统的RHS
   mastruct.c #
   mastructcmatrix.c #
   mastructcs.c #
   mastructdmatrix.c #
   mastructem.c #
   mastructffem.c #
   mastructnmatrix.c #
   mastructrad.c #
   mastructrand.c #
   mastructse.c #
   matrixsort.c #
   matrixstorage.c #
   mortar_postfrd.c #
   mortar_prefrd.c #
   multimortar.c #
   multi_rect.c #
   multi_rectv.c #
   multi_scal.c #
   nonlingeo.c #
   objectivemain_se.c #
   pardiso.c #
   pardiso_cp.c #
   pastix.c #
   pcgsolver.c #
   peeq_sen_dv.c #
   peeq_sen_dx.c #
   precontact.c #
   premortar.c #
   predgmres_struct_mt.c #
   prediction.c #
   prediction_em.c #
   preiter.c #
   preparll.c #
   radcyc.c #
   radflowload.c #
   randomfieldmain.c #
   readfrd.c #
   readinput.c #
   readnewmesh.c #
   refinemesh.c #
   remastructar.c #
   remastruct.c #
   remastructem.c #
   res1parll.c #
   res2parll.c #
   res3parll.c #
   res4parll.c #
   results.c #
   resultsforc.c #
   resultsinduction.c #
   resultsini.c #
   results_se.c #
   resultsstr.c #
   rhsmain.c #
   robustdesign.c #
   sensi_coor.c #
   sensi_orien.c #
   sensitivity_out.c #
   setpardou.c #
   setparitg.c #
   sgi.c #
   solveeq.c #
   spooles.c #
   steadystate.c #
   stof.c #
   stoi.c #
   storecontactdof.c #
   stos.c #
   strcmp1.c #
   strcmp2.c #
   strcpy1.c #
   stress_sen_dv.c #
   stress_sen_dx.c #
   stressmortar.c #
   strsplt.c #
   tau.c #
   thicknessmain.c #
   tiedcontact.c #
   trafontmortar2.c #
   trafontspcmpc.c #
   transformspcsmpcs_quad.c #
   transitionmain.c #
   transpose.c #
   u_calloc.c #
   u_free.c #
   u_malloc.c #
   u_realloc.c #
   utempread.c #
   v_betrag.c #
   v_prod.c #
   v_result.c #
   worparll.c #
   writeheading.c #
   writenewmesh.c #
   writeoldmesh. #
   
   umat_dl.cpp #
   ```
