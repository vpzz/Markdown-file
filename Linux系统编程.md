# 基础知识

1. 操作系统内核的接口被称作系统调用，system call。公用函数库建立在系统调用上，两者可以被应用程序使用。

2. Bash是GNU Shell，所有的linux都支持该shell，设计遵循POSIX标准，兼容Bsh，支持Csh和Ksh的特色功能。

3. 目录是一个包含目录项的文件，每条目录项包含该目录下的文件名，及其iNode。之所以不在目录项中存放文件的属性是因为一个文件可能有多个硬链接副本，很难在多个副本之间保持属性的一致。

4. /和空格不能作为文件名，因为/表示路径的分隔，空格表示文件名的终止。如果文件名中包含空格，在shell中需要使用双引号包括起来使用。

5. 文件名(filename)指的是某个文件的名称，路径名(pathname)分为绝对路径和相对路径。从路径名不能分辨出，指向的是文件还是目录。

6. 早期的Unix将8个部分都集中在《Unix程序员手册》，现在已经分开了，方便用户，程序员，系统管理员的使用。

7. 按照惯例，函数的返回值为0，表示正常结束。一般用-1表示出错。

8. 如果要对返回值进行校验，有宏名的用宏名，不要用宏值，因为宏值有可能会改变。

9. 每个进程都有一个工作目录，可以用chdir函数更改，所有的相对路径都以此开始解释。

10. 每当运行一个新的程序时，shell都会为其打开三个文件描述符，stdin，stdout，stderr。默认这三个文件描述符都链接向终端。

11. 系统I/O对应的三个标准文件描述符，STDIN_FILENO，STDOUT_FILENO和STDERR_FILENO，定义再unistd.h文件中。

12. 标准I/O对应的三个标准流，stdin，stdout，stderr，定义在stdio.h文件中。

13. ```shell
    ./a.out < in.txt > out.txt     #将a.out程序的标准输入重定向为in.txt，标准输出重定向为out.txt。
    ```

14. 系统I/O不带缓冲，标准I/O会自动选定合适的缓冲大小。

15. 程序（program）是指存储在硬盘上的某个可执行文件，使用exec函数将程序读入内存执行。

16. 进程（process）是程序执行的实例。

17. 使用函数的时候，应该将man提到的头文件原封不动的都包含进来。有时不包含对应的头文件也可以编译通过，但是会报警。例如：

    ```c
    int *p = malloc(sizeof(int));  //如果没有include stdlib.h的话,会报warning,提示说类型不匹配。其实并不是malloc的返回值void*和int*不匹配，而是当没有头文件时，编译器默认malloc的返回值为int，因此时int和int*的类型不匹配。
    ```

18. 进程在执行过程中会收到各种各样的信号，可以忽略（不推荐），或按照系统默认的方式（大多是结束该进程）处理，也可以捕捉信号，自己编写函数处理。键盘可以产生信号，例如Ctrl+C或Ctrl+\键。在一个进程中调用kill函数可以向另一个进程发送信号，此时需要是该进程的所有者或root。

19. Unix中的两类时间：

    1. 日历时间：早期的Unix使用格林尼治时间，后来使用了更精确的世界协调时UTC。表示从1970年1月1日00:00以来经过的秒数。使用time_t类型保存。
    2. 进程时间：也被称作CPU时间，用来度量进程使用的CPU资源。以时钟滴答计算，每秒钟曾经取过50,60，100个时钟滴答。使用sysconf(_SC_CLK_TCK)查询。

20. Unix为一个进程维护了3个时间值，使用time命令查看，其中real又称为墙上时钟时间。

21. linux3.2大约定义了320个系统调用。在man 2中说明，用C语言书写成。早期的系统使用汇编语言定义内核入口点。

22. 系统调用本质上是设置一下寄存器，然后调用软中断int 0x80，原则上任何编程语言只要内部用汇编指令实现这样的操作，就可以为该语言提供系统调用接口。不过大部分的操作系统的系统调用都是用C语言编写的。

23. 一个库函数可能使用多个系统调用，也可能不使用，例如atoi或strcpy。

24. 内存分配函数malloc，内部就使用到了sbrk系统调用。不过该函数只是增加或进程的地址空间，如何管理改地址空间，取决于进程本身，malloc内部实现了分配。如果对库函数不满意，可以使用系统调用封装自己的库函数。

25. 系统调用只做最基础的操作，例如关于时间只有一个系统调用，返回一个整数秒数，具体的时间日期解析，交给库函数。系统调用通常提供的是最小接口，库函数通常提供比较复杂的功能。

26. 内核中有大量的宏定义（应用到了极致），因为宏只占用编译时间，不占用调用时间，这个和函数相反。

27. char型是无符号还是有符号的这件事，是未定义的，标准C中没有该数据类型。

28. 如果使用到了命令行传参，那么就该在main函数的开头就检查参数的个数和类型是否正确，不正确的话应该像标准错误中输出正确的用法，可以使用fprintf()。

29. 如果申请两个资源，要求第一个成功再申请第二个，那么就应该考虑在第二个申请失败时，释放第一个资源。

30. 

31. 

32. 

33. 

# Unix标准及实现

1. 1989年，ANSI开发的C标准X3.159-1989被采纳为国际标准ISO/IEC9899-1990。ANSI（美国国家标准协会）是在ISO中代表美国的组织，IEC是国际电子技术委员会。
2. ISO C的目标是提高C语言程序的移植性，使其能够使用于大量操作系统，不仅是Unix。该标准定义了语法和语义，还定义了标准库。大部分的操作系统都提供了C标准中的库函数。
3. 1999年，ISO C更新为ISO/IEC9899-1999。自1999年以来，已经公布了3个技术勘误，分别在2001,2004,2007年。后续的标准有ISO/IEC9899-2011和2018。分别被称为
4. 不同的编译器支持的C标准不同。
5. C标准：
   1. ==ANSI C==
   2. ISO C
6. 
36. 

# I/O

1. 系统调用I/O（sysio）是和系统实现相关的，尽量使用标准I/O（stdio），标准I/O也是基于系统调用I/O的。标准的出现是为了兼容不同的系统的，一般来说标准只提供与一个函数的定义，规定了输入和输出应该是什么，具体的实现，在不同的操作系统上都是不一样的。
2. 标准I/O移植性好，标准I/O也是合并了系统调用，提供buffer和cache，为读写提供加速。
3. 例如C标准中，打开文件的函数fopen，在linux下依赖于open函数，在Windows下依赖于openfile函数。
4. I/O非常重要，设备，管道，套接字的读写都要依赖它。而且I/O非常有可能出错。一切皆文件，因此文件的读写非常重要。

## 标准I/O

1. 标准I/O中的函数

   1. 文件打开关闭：fopen()，fclose()。
   2. 字符读写：fgetc()，fputc()。
   3. 字符串读写：fgets()，fputs()。
   4. 二进制数据块的操作：fread()，fwrite()。
   5. 输入输出：printf()，scanf()。
   6. 文件位置指针操作：fseek()，ftell()，rewind()。
   7. buffer和cache的操作：fflush()。

2. 标准I/O中设计到一个核心的结构体，FILE。

3. man手册的第三章是标准库函数，也就是C标准的实现。第二章是系统调用。第一章是系统命令，第七章是机制讲解，例如socket，TCP。如果有重名的话，可以加上章号，例如：man 3 fopen。如果发现找不到对应的条目，可以更新man手册，yum install man-pages

4. 一个进程的空间中能打开的文件数量是有上限的（ulimit -a 可以查看或修改）。在不更改默认环境的情况下，进程创建时，默认打开3个流，标准输入stdin（指向键盘），标准输出stdout（指向屏幕），标准错误stderr（指向屏幕）。因此若ulimit -a中显示为1024，则只能再打开1021个文件。在当前shell中如果修改ulimit后，其子进程会继承这个上限，因此也会生效。如果新开一个shell，则是默认的ulimit。

   ```c
   #include <stdio.h>
   extern FILE *stdin;
   extern FILE *stdout;
   extern FILE *stderr;
   ```

5. 使用fopen创建文件时，文件的权限都是用户的默认权限（0666 & ~umask），不同的用户执行该程序，创建出来的文件权限不同。0666的0表示八进制数，因此这是三个八进制数，如果umask为0002时，取反为0775，再和0666按位与上，结果为066。相当于在rw-rw-rw-的基础上减去umask对应的权限，例如0002表示-------w-，所以结果为rw-rw-r--。文件的所有者和所属组默认是执行该程序的用户和它的默认组。

### fopen

1. fopen，fdopen，freopen都是流打开函数：

   ```c
   #include <stdio.h>
   FILE *fopen(const char *path, const char *mode);   //指定文件路径(相对和绝对都行)和打开权限。返回代表该文件的结构体的指针。如果失败，则返回NULL（空指针），并设置errno。
   FILE *fdopen(int fd, const char *mode); //将一个系统I/O的文件描述符封装为一个标准I/O的流。例如打开套接字会返回一个描述符，如果想要用标准I/O操作，就可以用这个函数。
   FILE *freopen(const char *pathname, const char *mode, FILE *stream);
   ```

2. 参数里的const声明是让用户放心，该函数内部不会对指针指向的内容进行修改。如果自定义的函数中的参数要接受的是字符串，但是形参不是const的，此时编译器会报warning。

3. 推荐应用尽用const还有一个原因，就是有时某些编译器会不将字符串字面常量放到常量区域。

   ```c
   char * ptr = "abc";
   ptr[0] = 'x';  //是有可能得到 "xbc"的
   ```

### errno

1. 大部分函数在出错时，会返回-1或者NULL，并且设置errno，记录出错的相关信息。在多线程环境中，每个线程都有自己的局部errno。

2. errno可以理解为全局变量（早期是一个整型变量，导致它容易被更新的错误覆盖，现在变成了一个宏定义），这样做的原因是为了方便调试，因为返回值的NULL并不能告诉调用者错误原因。errno会被其他的报错程序不断地刷新，因此出错后应该立即打印。errno会被替换为，这样就变成了一个线程私有化的了：

   ```c
   (*__errno_location ())   //一个函数调用的返回值，然后再解引用，
   ```

3. errno中关于错误的定义写在了/usr/include/asm-generic/errno-base.h和errno.h（后者include了前者）中，以宏定义的方式。当然打印出errno再去查找对应的头文件中的注释是比较麻烦的事情，可以用如下两个函数来简化：

   ```c
   void perror(const char *s);  //该函数会接受一个参数，并将该参数放在前面，后面加上当前的errno对应的信息一起打印，然后换行。该函数会自动关联全局变量errno
   char *strerror(int errnum);  //接受一个errnum，返回对应errnum的信息字符串。
   ```

4. ![image-20230430195623986](assets/image-20230430195623986.png)

5. 在遇到错误时，可以将errno和这些常量比较，来区别地处理错误。但这比较麻烦，因此C标准中定义了2个函数用来打印出错信息：

   ```c
   #include <string.h>
   char *strerror(int errnum); //errnum为errno，返回出错的信息字符串。
   #include <stdio.h>
   void perror(const char *msg);  //先在标准错误上输出msg指向的字符串，然后是冒号和空格，最后是errno对应的出错信息，最后是一个换行符。这个函数不用手动指定errno，他会自动关联errno。
   ```

6. 一般来说出错信息中，应该包含程序名，这样当程序作为管道的一部分执行时，可以区分出来错误是来自于那个程序。

### 文件打开 mode

1. 文件的打开权限mode是以如下6种字符中的一种开头的，且只从开头开始比对（即r123等价于r，r+456等价于r+）：
   1. r，只读方式，位置指针定位在文件的开始处。
   2. r+，读写方式，其余同上。
   3. w，有则清空，无则创建，以只写形式打开，位置指针定位在文件的开始处。
   4. w+，读写方式，其余同上。
   5. a，追加只写，如果文件不存在，则创建，位置指针定位在文件的末尾的下一个位置。
   6. a+，追加读写，如果文件不存在，则创建，如果第一个操作是读，则位置指针在文件的开头，如果第一个操作是写，则位置指针在末尾的下一个位置。
2. 文件的读写都是发生在位置指针所指的那个字符。这个位置指针是悬在字符的正上方的，读的话就是读取该字符，写的话，会覆盖该字符。因此以追加模式打开的话，位置指针指向文件最后一个字符的下一个位置。位置指针是从0开始计数的，存储在一个long整型中。例如文件有5个字节，以非追加模式打开，位置指针为0，否则为5。
3. r+模式比较特殊，如果一打开就获取位置指针的话，结果也是0，此时读从头开始，但是此时写入会却追加到末尾。因此r+模式，一开始读写是分离的，容易弄乱，所以建议以r+打开，然后手动来seek位置指针进行读写。r+模式在经历过一次写后或fseek之后，会将位置指针移动到对应的位置。但是即使seek到其他位置，无论何时再写入，仍然会写入到最后，也就是说写入的时候不会看当前位置指针，而是始终在末尾写入。
4. 可以发现6个权限中，除了r和r+以外，其余的权限在文件不存在是都会创建文件，而r和r+则会返回NULL。
5. fopen和open中文件打开权限的对应。可见，r+并不等于w+，因为w+可以在打开不存在的文件时会创建，r+会返回NULL，同时w+在打开存在的文件时会截断到0，r+不会。所以一般读写已存在的文件，应使用r+。
6. <img src="assets/image-20230430201356662.png" alt="image-20230430201356662" style="zoom:80%;" />
7. 打开文件的权限，够用就好，不要过多地申请，防止意外出错。慎用w和w+，可能会不慎截断已有的文件。
8. 在Windows下编程时，文件有两种类型：二进制流，文本流。而在POSIX系统中"b"选项会被忽略掉（即权限中可以加上b，也可以不加，这是兼容C89的作法），因为POSIX下只有一个流（stream）的概念。按照字符来读取就是字符流，按照字节来读取就是二进制流。
9. fopen内部用到了malloc，而fclose内部是free，二者是成对出现的。因此返回的FILE结构体本身存在于标准库所管理的堆中。
10. 一般来说，如果函数返回的是指针，同时又有逆操作，那么该指针指向内容是放在堆上的。也有些函数返回指针，但是指针所指的内容放在静态区。

### fclose

1. fclose关闭一个流：

   ```c
   int fclose(FILE *fp);  //成功返回0，失败返回宏值EOF。
   ```

2. 一般不回去校验fclose的返回值，因为很少失败。

### 字符读写函数

1. 字符读入函数：

   ```c
   #include <stdio.h>
   int fgetc(FILE *stream);  //读取到一个unsigned char，但是方便用户使用，同时也为了包含出错输出中的-1，替换为int类型。如果失败或读到文件末尾，则返回EOF。
   int getc(FILE *stream);  //等价于fgetc，最早被定义为宏来使用。返回值同上。
   int getchar(void);   //从标准输入读入，等价于getc(stdin)，返回值同上。
   ```

2. 字符输出函数：

   ```c
   int fputc(int c, FILE *stream);  //将指定的字符输出到指定的流上，可以是标准输出，标准错误，或打开的文件。
   int putc(int c, FILE *stream);  //同上面的fputc。
   int putchar(int c);  //输出到标准输出，等价于putc(c,stdout);
   ```

3. 推荐使用fgetc和fputc函数。

4. 虽然读到文件的末尾和发生错误都会返回EOF，但是此时errno是不一样的，前者的errno为0，表示没有错误。

### 字符串读写函数

1. 字符串读入函数（行缓冲模式）：

   ```c
   char *fgets(char *s, int size, FILE *stream);   //从流stream中读取size长度的字符串，放到s指向的空间，返回的指针就是参数s。
   char *gets(char *s);   //从标准输入读入一行数据到buffer，末尾的换行会被替换为"\0"。尽量不要使用该函数，因为它不检查缓冲区的溢出，尽量使用fgets来替代。
   ```

2. 上面的缓冲区溢出指的是用于接收字符串的s所指向的空间，可能会剩余的空间不够，进而覆盖掉别的有用的信息。

3. fgets正常结束有两种情况：

   1. 读取到size-1个字符，还没遇到EOF（文件结尾）或\n（行尾），此时停止读取，在缓冲区的末尾添加上一个'\0'，并写入到指针s对应的空间去。文件的位置指针向后移动size-1个字符。

      ```c
      //加入文件的内容如下，且size = 5：
      abcdef
      //写入的字符串如下，此时位置指针指向e：
      abcd'\0'
      ```
      
   2. 还没读到size-1个字符，就遇到文件末尾或者中间行尾了，位置指针会指向到下一行的开头。

      ```c
      //流的内容如下，且size = 5，这一行有3个字符：
      ab
      //写入的字符串如下，如果这是最后一行，也是'\n'。
      ab'\n''\0'
      ```

4. 文件的最后一行和中间行的区别在于，中间行包含一个换行符，而最后一行不包含。

   ```c
   //用vscode生成如下文件，一共3行，每行的字符个数为4，5，2个，一共有11个字符。
   abc
   absd
   as
   ```

5. 人工编辑的文件末尾有没有换行，取决于编辑器，vim会给末尾也添加一个换行符，这样每一行都是一样的。而vscode则不会自动给末尾添加换行符，因此尾行和其他行不一样。在Windows下，行尾的换行是以两个字符来代替的，CR和LF，分别表示回车（\r 光标回到本行开头），换行（\n光标下移一行）的意思。ASCII码分别为0xD 0xA，（如下图所示）。Unix/Linux仅使用LF(\n)作为行尾的换行。

6. ![image-20230501003508267](assets/image-20230501003508267.png)

7. 特殊情况如下，需要两次才能读完如下一个4个字符文件：

   ```c
   //流的内容如下,且size = 5：
   abcd
   //第一次读取abcd 4个字符，写入的字符串如下：
   abcd'\0'
   //第二次读取一个\n就停止了，会写入如下：
   '\n' '\0'
   ```

8. 字符串输出函数：

   ```c
   int fputs(const char *s, FILE *stream);  //从s所指的位置开始输出字符串到流stream，直到遇到'\0'，'\0'本身是不会被输出的。
   int puts(const char *s);  //和fputs(s,stdout)不完全一样，因为该函数还会输出一个换行符。
   ```

### EOF

1. 最后一行的结尾什么也没有，他和中间行的末尾不同，没有\n。
2. 其实EOF和\n不同，它不是一个字符，而是定义在stdio.h中的一个常量，值为-1。
3. 在文件的结尾处并不存在一个EOF的字符。而是当系统读取到文件的末尾时，会返回一个信号值，为EOF。至于是否到了文件末尾，可以通过文件大小和位置指针的位置来判断。
4. 普通字符的ASCII范围为32-127，EOF定义为了-1，不会发生混淆。
5. 由于读取文件内容出错时，也会返回EOF，那么此时就需要一个函数来判断是出错了，还是真的到达了文件的末尾。
6. int feof (FILE *stream)是C语言标准库函数，定义在stdio.h中，其功能是检测流上的文件结束符，如果文件结束，则返回非0值，否则返回0。
7. EOF实际上是表示流的末尾，包含了文件的末尾，因此在标准输入中也可以有。从标准输入读取内容时，由于无法事先知道流长度，因此必须手动输入一个EOF。
8. Linux中，在新的一行的开头，按下Ctrl+D，就代表EOF（如果在一行的中间按下Ctrl+D，则表示输出"标准输入"的缓存区，所以这时必须按两次Ctrl+D）；Windows中，Ctrl+Z表示EOF。（顺便提一句，Linux中按下Ctrl+Z，表示将该进程中断，在后台挂起，用fg命令可以重新切回到前台；按下Ctrl+C表示终止该进程。）
9. 字符读取和字符串读取系列函数，遇到出错或读到文件末尾时的输出是不同的，前者返回EOF，后者返回NULL。因为这两个函数的返回值不同，字符读取的返回值是读取到的字符，而字符串读取的返回值是一个指针。因此EOF表示无效的字符，而NULL表示无效的指针。
10. 在每次读取之前会进行判断，当前的位置指针是否指向文件的结尾处，如果是的话，就不进行读取，直接返回对应的报错值，EOF或NULL。

### 二进制读写函数

1. 二进制读写函数，按照字节来读写：

   ```c
   size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream); //从stream中读取nmemb个对象，每个对象size个字节，写入到ptr指向的空间。ptr指向的空间应该至少有size*nmemb剩余的空间。
   size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);  //将ptr指向的空间中，size*nmemb个字节的数据写入到流stream中。   ptr的const表示该函数不会修改ptr所指向的空间。
   ```

2. 以上两个函数的返回值表示成功读写的对象的个数，而不是字节数。每个对象为size个字节。如果剩余的内容不够一个对象的大小，则不会进行读写，返回0。

3. size_t是sizeof操作符的返回值类型，在32位环境下表示unsigned int，在64位环境下表示unsigned __int64。后缀t表示type。

4. 这个函数用在数据持久化（序列化和反序列化）上比较好，适合操作成块的数据。例如需要将10个结构体存储到文件中，就可以将size设置为1个结构体的大小，nmemb设置为10。不过需要这些结构体空间连续保存（例如为结构体数组），因为以上的读写都要求连续空间。

5. 进行成块的数据读写时，位置指针不能有一点偏差。

6. 使用二进制读写函数对文件进行读写时，不会考虑'\n'等因素，也不会再末尾加入'\0'，文件不是按照行来组织的，而是可以看成一个特别长的字符数组。

7. 如果文件的内容还剩很多，如下两个函数都能顺利读到10个字节，但是返回值分别为10和1。如果文件只剩5个字节了，那么第一个函数可以读到5个字节，返回值为5。第二个函数什么都读不到，返回值为0。

   ```c
   fread(buf, 1, 10, fp); //每个对象1个字节
   fread(buf, 10, 1, fp); //每个对象10个字节
   ```

8. 因此如果用这两个函数来做字符串的输入输出，一般都将第二个参数设为1。

9. 对于使用fread和fwrite进行文件复制（每个对象为1B）时，仅当fread的返回值>0时，才需要fwrite使用fread的返回值作为其写入的参数。因为最后一次的fread不一定恰好读够想要的对象个数。

### 格式化输入输出

1. 格式化输出：

   ```c
   //可变参数版本
   int printf(const char *format, ...);  //将待输出项以format的格式输出到标准输出中。
   int fprintf(FILE *stream, const char *format, ...);  //将待输出项以format的格式输出到流stream中。
   int sprintf(char *str, const char *format, ...);  //将待输出项以format的格式输出到指针str指向的空间。该函数可能会发生缓冲区溢出，应该使用下面的snprintf。最后会默认加上'\0'
   int snprintf(char *str, size_t size, const char *format, ...);  //将待输出项以format的格式输出到指针str指向的空间，最多输出size-1个字符。最后会默认加上'\0'
   
   //固定参数版本
   #include <stdarg.h>
   int vprintf(const char *format, va_list ap);//对应于printf
   int vfprintf(FILE *stream, const char *format, va_list ap); //对应于fprintf
   int vdprintf(int fd, const char *format, va_list ap);//类似于fprintf，不过输出到文件描述符。
   int vsprintf(char *str, const char *format, va_list ap);//对应于sprintf
   int vsnprintf(char *str, size_t size, const char *format, va_list ap);//对应于snprintf
   ```

2. 好的程序应该多使用fprintf，而不是printf，因为正常的输出和错误的输出应该分别输出到stdout和stderr，虽然默认情况下这俩都输出到屏幕，但是可以通过重定向来分离他们。无人值守的程序，推荐使用输出重定向到文件，这样方便之后查看运行过程。

3. 实际上snprintf()只是解决了sprintf可能会遇到的缓冲区溢出的问题，但是如果要写入的字符个数就是比size-1大，snprintf也只能丢弃多余的数据。只能通过动态内存分配来自适应输出的长度。

4. 字符串->数字如下，并没有itoa这样的函数，因为可以用sprintf来进行数字->字符串的操作：

   ```c
   #include <stdlib.h>
   int atoi(const char *nptr);   //将nptr所指向的字符串转化为整数，例如"123"->123，"12a3"->12
   long atol(const char *nptr);  //转化为long类型
   long long atoll(const char *nptr); //转化为long long类型
   double atof(const char *nptr);  //转化为double类型
   ```

5. 格式化读取：

   ```c
   int scanf(const char *format, ...);  //从标准输入中以format的格式读取数据，放到后续的参数中。
   int fscanf(FILE *stream, const char *format, ...);  //从流stream中以format的格式读取数据，放到后续的参数中。
   int sscanf(char *str, const char *format, ...);  //从指针str指向的空间中以format的格式读取数据，放到后续的参数中。
   ```

6. scanf在使用上最大的缺陷是由于终端输入的不确定性，有可能造成接受数据的缓冲区溢出。尤其是存在%s参数时。因为字符串参数的可用空间对于输入者来说是未知的。

### fseek

1. 文件位置指针操作函数：

   ```c
   int fseek(FILE *stream, long offset, int whence);  //将流stream的位置指针移动到，从whence偏移offset个字节的位置。whence有三种情况，SEEK_SET SEEK_CUR SEEK_END分别表示文件首，当前位置，文件尾。操作成功返回0，失败返回-1，并设置errno。
   long ftell(FILE *stream);  //返回流stream的位置指针的位置。先fseek到末尾，然后ftell可以获取文件的大小。
   void rewind(FILE *stream);  //把位置指针移动到文件首。相当于(void) fseek(stream, 0L, SEEK_SET);使用0L是严格用法，有些编译器会校验这个操作。
   ```

2. 上面说的SEEK_END，这里的文件尾指的是最后一个字节的下一个位置。这是和append操作相协调的，即读写都是操作的当前的位置。

3. 文件的位置指针默认是指向第0个字符的，读取一个字符完成后会移动该指针到下一个位置。写入一个字符完成后会移动该指针到下一个位置。以上指针的移动都是自动完成的。

4. long类型在C标准中没有规定字节数，但是说至少和int一样长。一般的编译器把他当做4字节的和int一样。

5. long默认为有符号的，范围是$[-2^{31}\to 2^{31}-1]$，在fseek中可以发现offset的取值范围为-2G~2G-1。因此文件最大可以有4G的范围。但是又因为ftell的返回值也是long，这里的文件位置指针又不能取负数。因此文件的位置指针只能是从0到2G-1的范围。

6. 因此后续给出了更为完善的关于文件位置指针的函数，不过这两个函数只有POSIX标准支持，C89,C99等都不支持，这意味着不能移植到Windows平台上：

   ```c
   int fseeko(FILE *stream, off_t offset, int whence);   //off_t是一个宏定义，默认情况下它和long都是32位的，如果编译时加入#define _FILE_OFFSET_BITS 64        则表示off_t为64位的。如果没有定义该宏，在某些平台上off_t的行为是未定义的。
   //gcc编译时加入 -D_FILE_OFFSET_BITS=64 即可。makefile写法：CFLAGS += -D_FILE_OFFSET_BITS=64
   off_t ftello(FILE *stream);
   ```

7. fseek可以用来创建空洞文件。只要seek到文件末尾以后的地方即可。这样文件的大小就会变化，增加的空间用'\0'填充。有的下载工具会在一开始创建一个空洞文件，然后多线程下载，从不同的地址写入，从而实现真正的多线程下载。

### fflush

1. 刷新缓存：

   ```c
   int fflush(FILE *stream);   //刷新流stream的缓冲区，如果stream为NULL，将会刷新所有打开的流。
   ```

2. 标准输出这样的流都是行缓冲模式的，直到遇到'\n'，才会将缓冲区的内容输出。

3. 如下情况，不会看到"Before while()"的输出，因为该缓冲区没有被刷新，因此要么加入'\n'，要么手动刷新fflush(stdout)。

   ```c
   printf("Before while()");
   while(1);
   printf("After while()");
   ```

4. 缓冲区的作用是合并系统调用，缓冲模式有：

   1. 行缓冲：遇到'\n'或缓冲区满的时候会自动刷新。也可以用fflush手动刷新。终端设备默认是行缓冲。
   2. 全缓冲：缓冲区满的时候才会刷新。fflush可以手动刷新。文件默认是全缓冲，应该及时地flush。'\n'只是换行的作用。
   3. 无缓冲：不进行缓冲，例如stderr，不能等待，需要立即输出。

5. 只要输出不是终端设备，默认都是全缓冲的。不过也可以修改流的缓冲模式，但是一般不会修改：

   ```c
   int setvbuf(FILE *stream, char *buf, int mode, size_t size);  //设置流stream的缓冲模式为mode，mode取值须为_IONBF(No Buffer)，_IOLBF(Line Buffer)，_IOFBF(Full Buffer)之一。
   ```

### 行输入和输出

1. 之前的所有函数都无法保证不丢失地读入一行的内容，因为不知道一行究竟有多长，因此需要使用动态内存分配。getline的内部就是封装了动态内存分配。malloc+realloc的结合。

2. 行读入和输出，getline函数时GNU C扩展支持的，不是C标准规定的，libc 4.6之后才支持：

   ```c
   #define _GNU_SOURCE    //可以在makefile 的CFLAGS中附加上。  CFLAGS += -D_GNU_SOURCE 不过在Ubuntu22.04中不定义这个宏，也可以使用。
   ssize_t getline(char **lineptr, size_t *n, FILE *stream);   //从流stream中读取一行，存放到一个地方，一级指针*lineptr指向该地方的首地址。*n是为了存储该行而在堆上开辟的内存空间大小。函数返回值表示读取到的字符数量，包含'\n'，但是不包含'\0'。失败时返回-1。
   //意思就是用户提供一个二级指针和一个一级指针。读完之后，该行的内容存储在\*linptr的地方，长度为\*n。
   ```

3. getline会逐个字符读取，直到遇到'\n'字符。才会停止，如果遇到'\0'也不会停止，但是此时*lineptr就得配合返回值来使用了，因为该行的中间有一个'\0'。如果读到行尾时，行尾没有'\n'，也不会自动加上的。

4. 如果在调用getline前，\*linebuf为NULL，且\*n为0，则getline会自己申请一块内存。否则会getline会优先使用提供的这块大小为\*n的内存\*linebuf，如果不够的话，会realloc，并更新这两个参数。因此，推荐在首次调用前，一定初始化两个参数。

5. 例子：

   ```c
   FILE *fp;
   char *linebuf = NULL;
   size_t linesize = 0;   //必须要在使用前赋值，否则容易产生bug。
   
   getline(&linebuf, &linesize, fp);  //这里之所以使用指针传参，是因为需要在getline函数内修改定义在它外面的linesize的值，如果传入的参数是linesize，那么修改的就只是getline函数内的形参，最终在函数外定义的linesize是无法被修改的。
   printf("该行的长度为：%zu。该行的内容为：%s", linesize, linebuf);
   ```

6. getline 会从流中开始读取，直到读到一个\n为止，会将读到的内容都放到一个malloc出来的区域中，并将用户传入的一级指针的地址修改为malloc的头地址，将读入的字节数赋值给第二个参数指针指向的空间。在这期间，如果分配的空间不够，则会realloc。

7. 第一次malloc的大小默认为120字节。读完一行后，会继续从头使用当前malloc的内存读取下一行，只有空间不够容纳新的一行时，才会realloc。可以看到，该函数没有对malloc的内存进行free，会产生一个可控的内存泄露。因为它不像守护进程一样，会长期运行而不终止，因此不会不断地产生泄露。I/O函数的泄露非常有限。实际上也不建议开发者自己free，因为该函数内部申请内存的函数可能不是malloc。

8. 例子：

   ```c
   //使用getline读取如下两行内容：
   abc
   aaa'\0'bb
   //第一次读取返回值为4，linebuffer指向的空间为 'a','b','c','\n','\0'...第二次读取返回值为6，linebuffer指向的空间为'a','a','a','\0','b','b','\0'...
   ```


### 临时文件

1. 临时文件，由于临时文件一般放在/tmp目录下（任何用户都可以访问），多用户环境下，可能冲突。临时文件用完要及时销毁，否则造成冲突的几率也会上升。

2. ```c
   char *tmpnam(char *s);     //返回一个可用的临时文件名称,如果参数s为NULL,字符串存在于标准库管理的堆内存中，可能会被下一次的tmpnam调用而覆盖掉。如果参数s不为NULL,则会将该字符串复制到s指向的字符数组中，此时s的空间应至少有L_tmpnam(定义在stdio.h中的一个宏，等于20)长度。文件名的前缀默认为P_tmpdir(stdio.h中被定义为/tmp/)。例如会创建一个文件名为 /tmp/fileDNhq93
   FILE *tmpfile(void);      //会打开一个独一无二的临时文件，以w+b的模式打开。关闭流或程序终止时会自动删除该文件。
   ```

3. 不太推荐使用tmpnam函数，因为创建一个临时文件需要两步，首先申请一个临时文件名，然后fopen。这期间可能被并发的其他进程打断，如果这个进程碰巧，也要申请一个文件，那么tmpnam可能会把之前分配的临时文件名分配给它，造成冲突。

4. 推荐使用tmpfile，实际上使用临时文件时，并不关心文件名，只是要有一个流可以进行读写就行了。这个文件在使用中是匿名的，ls -a也查看不到。系统统一管理，匿名文件，没有名字因此不会重名，但是会占用一个文件描述符资源，和ulimit的值有关。

## 系统I/O

1. 系统调用I/O也称为文件I/O。文件描述符fd是贯穿系统I/O的类型。
2. 标准I/O是依赖于系统调用I/O来实现的。常见的系统调用I/O函数有：open，close，read，write，lseek。

### 文件描述符

1. 文件描述符是整型数，本质是一个数组下标，数组中该位置存储了一个结构体的指针。该数组的长度为ulimit得到的值。结构体指针数组，每个元素都是结构体指针，该数组属于单个进程的。
2. fopen是依赖于open的，因此FILE结构体内部也有open得到的文件描述符fd。
3. 进程默认打开的三个FILE流stdin stdout stderr和默认的三个文件描述符0，1，2相互对应。

    ```c
    // unistd.h中定义的
    #define	STDIN_FILENO	0
    #define	STDOUT_FILENO	1
    #define	STDERR_FILENO	2
    ```
4. 实际上进程默认打开的文件描述符是从父进程继承来的，如果父进程关闭了2，则子进程打开一个文件会获得2这个文件描述符。
5. 文件描述符优先使用可用的最小的一个，可以插空。例如：0 1 3 4 5，再打开一个就会使用2。
6. 不同的进程打开同一个文件，会产生不同的结构体，存储在不同的数组中，fd之间没关系。在一个进程中打开同一个文件多次，则会创建多个结构体，存储在该数组中，互不影响，fd之间不能重复。每一个fd都有自己的位置指针。
7. close一个文件描述符，就是回收一个fd，然后将结构体指针数组的对应元素置为NULL，但不一定会释放结构体内存，因为有时有两个fd指向同一个结构体，这可以通过复制文件描述符dup的方式得到。只有结构体的引用计数归零，才会释放该结构体。
8. 一共有三级结构，数组↔结构体↔iNode。多个结构体可以同时指向一个iNode，这个一般出现在多次open同一个文件。一个结构体可以被数组中的多个元素同时指向，这个一般出现在复制数组的元素到其他位置。
9. 文件位置指针和文件状态标识存储在文件描述符关联的结构体中，dup的两个文件描述符共享这些状态。

### open

1. open打开一个文件：

   ```c
   #include <sys/types.h>
   #include <sys/stat.h>
   #include <fcntl.h>
   int open(const char *pathname, int flags);  //pathname为文件路径，flags为权限信息，作用和fopen的mode相同。成功时返回文件描述符，失败返回-1。
   int open(const char *pathname, int flags, mode_t mode); //这两个open不是重载，因为C语言中没有重载，而是变参函数实现的。只有flags中存在O_CREAT或O_TMPFILE，才不会忽略指定文件权限位的mode参数。同理如果flags包含O_CREAT或O_TMPFILE，也必须指定mode参数，否则会用栈上的其他内容作为该参数的值。mode会和进程的umask取反再相与，结果才是文件的真正权限位。和fopen不同的是，fopen只能使用默认的mode，这里可以手动指定mode。
   int creat(const char *pathname, mode_t mode); //等价于使用O_CREAT|O_WRONLY|O_TRUNC来调用open
   int openat(int dirfd, const char *pathname, int flags);  //和open类似，如果pathname参数是一个相对路径(不以/开头)，则被认为是相对于dirfd所指的路径而不是进程的当前工作目录。如果pathname参数为相对路径，且dirfd为AT_FDCWD则在进程的当前工作目录打开文件，这和open一样。如果pathname参数是绝对路径，则忽略dirfd，功能和open完全相同。
   int openat(int dirfd, const char *pathname, int flags, mode_t mode);
   ```

2. open函数的flags支持读写，创建，截断，阻塞，信号驱动等等模式。比fopen要复杂和强大的多。多个选项使用按位或 | 来组合，不过必须存在如下三个中的一个 O_RDONLY，O_WRONLY，O_RDWR，且不能用O_RDONLY | O_WRONLY来代替O_RDWR。后续可以跟零个或多个文件创建标识和文件状态标识来组合使用。

   1. 文件的创建标识，影响文件打开操作：

      ```c
      O_CLOEXEC  //
      O_CREAT    //如果文件不存在，则创建一个普通文件，新文件的所有者ID为进程的有效用户ID，新文件的所属组ID为进程的有效组ID(System V语法)或父目录的组ID(BSD语法)。Linux上如果设置了set-group-ID模式位,则使用System V语法，否则使用BSD语法。
      O_DIRECTORY//如果打开的路径不是一个目录，则会报错。一般打开目录可以跟openat结合使用。
      O_EXCL     //
      O_NOCTTY   //
      O_NOFOLLOW //如果路径名的末尾部分是一个符号链接，则打开失败。末尾之前的部分如果包含符号链接还是会被跟踪的，不会失败。
      O_TMP‐FILE //
      O_TRUNC    //如果文件存在，是一个普通文件，且访问模式允许写入(使用了O_RDWR或O_WONLY)时，文件长度会被截断到0，如果文件是一个FIFO或终端设备文件，则忽略这个标识。
      ```

   2. 文件状态标识，影响后续的I/O操作，后续可以通过fcntl获取和修改：

      ```c
      O_APPEND   //
      O_ASYNC    //
      O_DIRECT   //
      O_DSYNC    //
      O_LARGEFILE//如果打开大小不能用off_t表示(但可以用off64_t表示)的文件，需要定义_LARGEFILE64_SOURCE宏才可以使用。不过在32位系统上更推荐使用定义宏_FILE_OFFSET_BITS=64，结合ftello和fseeko使用。
      O_NOATIME  //当read文件时，不更新最近访问时间(存储在inode的st_time)，只有当进程的有效用户ID和文件的所有者ID相同时，才可以设置此标识。
      O_NONBLOCK 和 O_NDELAY //非阻塞
      O_PATH     //
      O_SYNC     //不进行缓冲，调用write时，直接写入数据。write函数返回时，表明输出的数据和响应的元数据修改已经完成。相当于每次write后都调用fsync。
      ```

3. open函数中mode参数的取值：

   ```c
   S_IRUSR S_IWUSR S_IXUSR //分别表示所有者的读写执行权限，也可以用S_IRWXU来代替这三个的或，三个宏的取值分别为00400,00200,00100，综合宏的取值为00700
   S_IRGRP S_IWGRP S_IXGRP //分别表示所属组的读写执行权限，也可以用S_IRWXG来代替这三个的或，三个宏的取值分别为00040,00020,00010，综合宏的取值为00070
   S_IROTH S_IWOTH S_IXOTH //分别表示其他人的读写执行权限，也可以用S_IRWXO来代替这三个的或，三个宏的取值分别为00004,00002,00001，综合宏的取值为00007
   S_ISUID //set-user-ID，取值为0004000
   S_ISGID //set-group-ID，取值为0002000。会影响O_CREAT创建文件时，文件的所属组ID的取值。
   S_ISVTX //sticky bit，取值为0001000。粘滞位。
   ```

4. 从程序设计的角度来理解cache和buffer：cache看作是读的缓冲区，一般称为缓存，实际上是缓取，例如cpu的多级缓存，DNS缓存，CDN等，可以提高重复读取的效率。buffer是写的缓冲区，例如标准I/O会先将每次的写入存到缓冲区内，然后再统一调用一次系统I/O，效率高。

### read write lseek

1. read和write

   ```c
   #include <unistd.h>
   ssize_t read(int fd, void *buf, size_t count); //从fd中读取count个字节，存储到buf指向的地址中。如果成功，返回读取到的字节数，为0表示读到了文件末尾，也视为一次成功的读取。失败(任何内容都没读到)返回-1，并设置errno。
   ssize_t write(int fd, const void *buf, size_t count); //将buf指向的地址中count个字节的内容写入到fd中。如果成功，返回写入的字节数，为0表示。失败(任何内容都没写入)返回-1，并设置errno。
   //可以写入0个字节，例如被信号打断时。应对函数的返回值进行判断，如果>=0时，是否等于count，如果不等于则表明没有完全写完，那就继续从中断的位置写，即第二个参数应为buf+write返回值，同时写入的字节数也应减去之前分次写入的和。一次写入可能会被中断多次，因此需要while(1)，直到分片的write的返回值的和等于初次的count才可以。
   //例如要从buf向fd中写入10个字节，如果第一次写入了3个字节就中断了，则第二次应该从buf+3处开始向fd中写入10-3=7个字节，如果第二次写入5个字节又中断了，则第三次应该从(buf+3)+5处开始向fd中写入7-5=2个字节。中间还可能中断，直到某一次write的返回值等于该次调用的count参数，则表明10个字节已经完全写入。
   ```

2. 一次成功的读写，返回值可能小于count，例如：

   1. 当read被信号中断或剩余的字节不够count时，返回值会 < count。

   2. 当write被信号中断或磁盘空间不够时，返回值会 < count。

3. 一次失败的读写意味着任何内容都没读写到，此时返回值为-1，并设置errno。例如：

   1. 当errno为EINTR时，表示因为被信号打断，才导致任何内容都没被读到或写入。

4. 因此综上，信号可能会在没有读到或写入任何内容时就打断阻塞的read和write。也有可能在读写了一部分后，再打断。通过返回值来标识是哪种情况。

5. lseek，综合fseek和ftell的功能

   ```c
   #include <sys/types.h>
   #include <unistd.h>
   off_t lseek(int fd, off_t offset, int whence); //移动fd的文件位置指针，定位到whence偏移offset的位置。whence的取值和fseek中whence一样。返回值为移动后的文件位置指针的位置，类似于ftell的功能。lseek(fd,0,SEEK_CUR)的结果就是当前位置。
   ```

### 标准I/O和系统I/O的区别

1. 标准I/O具有缓冲机制，吞吐量大，系统调用I/O没有缓冲，实时性高，响应速度快，每次调用都进入内核态。缓冲的作用就是合并系统调用。实际上更推荐使用标准I/O。标准I/O和文件I/O不应混用，容易出错。

2. ```c
   int fileno(FILE *stream);  //返回流对应的文件描述符
   FILE *fdopen(int fd, const char *mode);  //将已经打开的文件描述符的fd封装为一个流，以供使用。要求mode参数和创建fd时的mode参数兼容。文件位置指针也会关联，mode中的w和w+参数不会导致文件被截断，当fclose该流时，fd也会被close。
   ```

3. 标准I/O和系统I/O中结构体的部分成员（例如文件位置指针）的值不一定相同。因为标准I/O有缓冲机制，在标准I/O中写入后，流的位置指针会变动，但是fd对应的位置指针并不跟着变动，因为没有刷新缓冲区。读取也存在这种情况，当标准I/O读取少量内容时，系统I/O可能会按块一口气读取较多的内容，放到缓存中，此时二者的文件位置指针也不相同。如下例子表明了标准I/O的系统I/O互不影响，各自工作。

   ```c
   putchar('a')    //顺序执行这六个函数，输出的结果为bbbaaa。
   write(1,"b",1)
   putchar('a')
   write(1,"b",1)
   putchar('a')
   write(1,"b",1)
   ```

4. 使用strace命令来跟踪系统调用，从第8行可以看出，标准I/O会合并系统调用。

   ```shell
   [zj@ZJ test]$ strace ./sysio
   execve("./sysio", ["./sysio"], 0x7fff5e2e6280 /* 26 vars */) = 0
   brk(NULL)                               = 0xbe6000
   ...
   write(1, "b", 1b)                        = 1
   write(1, "b", 1b)                        = 1
   write(1, "b", 1b)                        = 1
   write(1, "aaa", 3aaa)                      = 3 #合并为了一个系统调用
   exit_group(0)                           = ?
   +++ exited with 0 +++
   ```

5. time命令可以计算后面的命令执行消耗的时间：

   ```shell
   [zj@ZJ test]$ time cp /etc/services aa
   real    0m0.003s  #实际运行的时间=user+sys+调度消耗，也称为墙上时间
   user    0m0.000s  #在用户态运行的时间
   sys     0m0.003s  #在内核态运行的时间
   ```

6. 随着buffersize的值变大，性能存在一个拐点，大约是4k。读写太频繁，每次读写非常少的内容和读写太不频繁，每次读写非常大的内容，这两种方案都是效率低下的。当buffersize增大到一定程度后，会产生栈溢出错误，ulimit -a中可以查看到，一般为8M。

### 文件共享

1. 文件共享：一个文件被多次打开，产生多个文件描述符，每个文件描述符都存在自己的文件位置指针。例如：要删除一个文件的第10行，此时可以将改文件以r和r+打开两次，一个用来读取11行，另一个用来将读到的内容写入第10行，然后依次向后移动。最后将文件大小截断，减去第10行的大小。

2. ```C
   #include <unistd.h>
   #include <sys/types.h>
   int truncate(const char *path, off_t length);  //将一个未打开的文件截断到length长度。
   int ftruncate(int fd, off_t length);  //将一个打开的文件截断到length长度。
   ```

### dup dup2

1. 原子操作：不可分割的操作。作用是为了解决竞争和冲突。例如：进程1使用tmpnam获取临时文件名A后，时间片耗尽，切换到另一个进程2，恰好进程2也要调用tmpnam申请临时文件名，由于此时进程1还未使用文件名A，tmpnam可能会将文件名A分配给进程2。此时就发生了关于临时文件名A的竞争。出现竞争的原因是因为创建文件名和创建文件是分成两步进行的，不是一个原子操作。多进程/线程并发时，会使用到原子操作。

2. 重定向 dup dup2：

   ```c
   #include <unistd.h>
   int dup(int oldfd);   //复制一个文件描述符，新的文件描述符为当前可用的最小序号。如果成功返回新的文件描述符，失败返回-1。
   int dup2(int oldfd, int newfd);  //和dup的工作类似，但是不使用最小的可用文件描述符，而是使用newfd参数。将数组oldfd的指针复制一份到newfd中去，如果newfd已经被打开，则会先关闭。等价于close(newfd);dup(oldfd)。如果oldfd无效，则报错，也不会关闭newfd。成功的话，返回新的文件描述符。
   ```

3. dup操作并不会复制结构体，而是在数组中新增了一个结构体指针，指向oldfd描述符对应的结构体。两个文件描述符关联了同一个结构体。

4. 例子：将printf输出的内容重定向到文件a中。

   ```c
   oldfd = open("a",O_WRONLY | O_CREAT | O_TRUNC, 0600); //打开文件a，获得文件描述符oldfd。
   close(1); //关闭标准输出
   int newfd = dup(oldfd); //此时新的描述符会是1,和oldfd关联同一个结构体。
   puts("abcd"); //此时向标准输出中写入内容，例如printf，就相当于write(1,buf,count);会写入到1和oldfd共同对应的文件了，从而实现了将标准输出输出重定向到文件。
   ```

5. 上述操作如果在第二步和第三步中间被中断，有可能出现bug。例如关闭了1号文件描述符，但是切换到另一个线程，如果该线程碰巧正要打开一个文件，则该文件就会占用1号文件描述符，这样等到第三步再执行时，就newfd就不是1了，就不能实现将标准输出重定向到文件了。出现这种情况的原因是close和dup这两个函数不是原子操作，因此推荐使用dup2函数。上述代码还存在一个问题，如果该进程默认关闭了1号文件描述符，那么第二步会关闭掉第一步打开的文件。

6. 原子操作dup2比非原子的close+dup好处：

   1. 如果newfd=oldfd，dup2什么也不做，不会报错。因为close(newfd)后，此时如果再dup(oldfd)，就会发现oldfd的位置已经没有指向结构体了。
   2. dup2函数可以手动指定新的文件描述符，而close+dup只能依次使用可用的最小文件描述符。

   ```c
   dup2(oldfd,1);    //如果oldfd=5,那么会使得1号文件描述符和5号指向相同的结构体。关闭的时候需要关闭1和5。
   if (oldfd != 1); //如果oldfd=1,那么dup2不会做任何动作，此时只需要关闭一次1或者oldfd即可。
       close(oldfd);
   close(1);
   ```

7. 可以重定向的原因是printf之类的函数都是指定文件描述符，他不认识文件描述符后面是不是标准输出。

8. 实际用的时候，如果中途需要改变进行重定向，使用完成后，需要及时恢复过来。尽量不改变其他部分运行的环境。

### sync fcntl ioctl

1. 同步sync，将该进程内核层面的buffer，cache（例如待写入的数据或待更新的属性）同步到磁盘中。一般在卸载设备前，需要将buffer和cache中的数据及时地写入到设备中。

   ```c
   #include <unistd.h>
   void sync(void);    //同步所有的文件描述符
   int syncfs(int fd); //只同步fd。
   
   int fsync(int fd); //同步一个文件fd。
   int fdatasync(int fd); //只同步fd的数据，不同步元数据metadata。metadata是指文件的属性，修改时间等等信息。
   ```

2. fcntl操作文件描述符，管家函数。

   ```c
   #include <unistd.h>
   #include <fcntl.h>
   int fcntl(int fd, int cmd, ... /* arg */ );  //几乎之前讲的所有文件描述符相关的操作都可以用该函数实现。cmd是命令，后续的变参列表为cmd的参数
   ```

3. ioctl()是设备相关的管家函数。硬件工程师经常使用。一切皆文件的思想方便了系统及以上的程序员，但是对硬件程序员不友好，因为一些硬件不仅仅只有文件的5个常用操作。

   ```c
   #include <sys/ioctl.h>
   int ioctl(int fd, unsigned long request, ...); //request是设备相关的请求码，
   ```

4. /dev/fd目录是一个虚目录，显示当前进程的文件描述符信息。

   ```shell
   [zj@ZJ test]$ ls /dev/fd #此处看到的是ls进程的文件描述符。
   0  1  2  3
   [zj@ZJ test]$ ll /dev/fd
   lrwxrwxrwx. 1 root root 13 5月   3 08:33 /dev/fd -> /proc/self/fd
   [zj@ZJ test]$ ll /proc/self/fd
   总用量 0
   lrwx------. 1 zj zj 64 5月   3 20:39 0 -> /dev/pts/0
   lrwx------. 1 zj zj 64 5月   3 20:39 1 -> /dev/pts/0
   lrwx------. 1 zj zj 64 5月   3 20:39 2 -> /dev/pts/0
   lr-x------. 1 zj zj 64 5月   3 20:39 3 -> /var/lib/sss/mc/passwd
   lrwx------. 1 zj zj 64 5月   3 20:39 4 -> 'socket:[41112]'
   lr-x------. 1 zj zj 64 5月   3 20:39 5 -> /var/lib/sss/mc/group
   lr-x------. 1 zj zj 64 5月   3 20:39 6 -> /proc/3403/fd
   ```

# 文件系统

## 文件属性

1. 获取文件的属性：

   ```c
   #include <sys/types.h>
   #include <sys/stat.h>
   #include <unistd.h>
   //使用之前，要先创建一个struct stat类型的结构体。然后将结构体的地址传给第二个参数。以下函数成功返回0，失败返回-1。
   int stat(const char *pathname, struct stat *statbuf); //根据文件路径，获取文件的信息，存储到statbuf指向的位置。对待符号链接时，获取的是被链接文件的属性。
   int fstat(int fd, struct stat *statbuf); //接受文件描述符，功能和stat一样。
   int lstat(const char *pathname, struct stat *statbuf); //对待符号链接时，获取的是符号链接本身的属性，即不跟踪符号链接。
   ```

2. struct stat类型：

   ```c
   struct stat {
       dev_t     st_dev;         /* ID of device containing file */ 当前文件所在的设备ID号
       ino_t     st_ino;         /* Inode number */ iNode号。
       mode_t    st_mode;        /* File type and mode */ 文件类型和权限信息
       nlink_t   st_nlink;       /* Number of hard links */ 硬链接计数
       uid_t     st_uid;         /* User ID of owner */ 所有者ID
       gid_t     st_gid;         /* Group ID of owner */ 所属组ID
       dev_t     st_rdev;        /* Device ID (if special file) */ 如果当前文件是一个设备的话，此处表示设备的ID
       off_t     st_size;        /* Total size, in bytes */文件大小，单位为字节
       blksize_t st_blksize;     /* Block size for filesystem I/O */ 最佳I/O块的大小，默认4096B，一般是读写缓冲区的拐点。
       blkcnt_t  st_blocks;      /* Number of 512B blocks allocated */ 当前文件所占512B块的数量，不包含空洞产生的无效数据，因此比st_size/512B小。
       /* Since Linux 2.6, the kernel supports nanosecond precision for the following timestamp fields. For the details before Linux 2.6, see NOTES. */
       struct timespec st_atim;  /* Time of last access */  最后一次读的时间
       struct timespec st_mtim;  /* Time of last modification */ 最后一次写的时间，数据修改
       struct timespec st_ctim;  /* Time of last status change */ 最后一次元数据修改的时间
       #define st_atime st_atim.tv_sec      /* Backward compatibility */
       #define st_mtime st_mtim.tv_sec
       #define st_ctime st_ctim.tv_sec
   };
   ```

3. 文件实际所占的用的空间大小为st_blocks\*512B，因为操作系统是按照block来分配存储空间的，即使文件没有用完一个block，该block的剩余空间也不能给别的文件使用。而st_size指的是文件的内容所占的大小，st_size只是一个属性，并不表示实际占用的空间。对于非空洞文件来说，块数量的分配也不都是按照字节数量/512来分配的，例如一个1个字节的文件，会被分配8个block。

4. 需要注意的是st_blocks所指的块并非是st_blksize这么大。两者一个是用来描述所占存储空间的，一个是描述最佳I/O行为的块大小。即使刚touch的一个空文件，st_blksize也不为0，而其st_size和st_blocks均为0。

5. 产生一个5G大小的空洞文件：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <sys/types.h>
   #include <sys/stat.h>
   #include <fcntl.h>
   #include <unistd.h>
   int main(int argc, char** argv) {
       int fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0600);
       if (fd < 0) {
           perror("open()");
           exit(1);
       }
       lseek(fd, 5LL * 1024LL * 1024LL * 1024LL - 1LL, SEEK_SET); //需要对每个常量用LL修饰，否则会溢出，因为结果为5G-1，而int的范围最大为2G-1。
       write(fd, "", 1);  //如果不执行这一步，文件的size和blocks都是0
       close(fd);
       exit(0);
   }
   //源文件的blocks是8，如果此时用cp命令拷贝这个文件，则新文件的blocks为0，因为cp会检查文件的字节，结果发现都是'\0'。
   ```

6. 除了使用这些系统调用之外，stat命令也可以获取文件的相关信息：

   ```shell
   [zj@ZJ test]$ ll test
   -rwxrwxr-x. 1 zj zj 13K 5月   3 09:18 test #1为硬链接计数
   [zj@ZJ test]$ stat test
     文件：test
     大小：13152           块：32         IO 块：4096   普通文件
   设备：fd00h/64768d      Inode：134295685   硬链接：1
   权限：(0775/-rwxrwxr-x)  Uid：( 1000/      zj)   Gid：( 1000/      zj)
   环境：unconfined_u:object_r:user_home_t:s0
   最近访问：2021-05-03 09:18:10.706737642 +0800
   最近更改：2021-05-03 09:18:07.583666022 +0800  #ls默认显示的时间
   最近改动：2021-05-03 09:18:07.583666022 +0800
   ```

7. st_mode权限信息有两部分组成，一个是文件的类型，一共有7种，分别为：d c b - l s p，分别表示目录，字符设备，块设备，常规文件，符号链接，套接字，管道文件（FIFO，特指命名管道，因为匿名管道在文件系统中看不到）。系统提供了一系列的宏来测试st_mode中的字段来获取文件类型，例如S_ISREG(st_mode)如果为true，则表示文件是常规文件，否则不是。或者用S_ISDIR(st_mode)判断路径名是否是目录。目录是一种特殊的文件。

8. st_mode是一个16位的整型数，例如0170000，0开头表示8进制。

9. 3位二进制，组合起来有8种情况，可以用来表示7种文件类型。9位二进制分别标识所有者，所属组，其他人的RWX权限是否存在。最后是3位，分别标识Set-User-ID，Set-Group-ID，Sticky Bit。一共3+9+3=15，因此一般使用16位数据来存储st_mode。

10. 

## 文件权限

1. 一个新文件的默认权限为0666&~umask。umask命令是显示或更改创建文件的进程的掩码。umask的存在是为了限制创建文件的权限过松。默认的umask为0002。文件权限为4位8进制数，第一位表示特殊权限。umask函数可以更该进程的掩码，这样后续创建的所有文件都会受影响。umask命令和函数都不能更改Set-User-ID，Set-Group-ID，Sticky Bit。

2. ```c
   #include <sys/types.h>
   #include <sys/stat.h>
   mode_t umask(mode_t mask);  //功能和使用umask命令相同。返回之前的umask值
   ```

3. 更改文件的权限位：

   ```c
   #include <sys/stat.h>
   int chmod(const char *pathname, mode_t mode);  //根据路径索引，修改文件的权限位为mode，不会受umask影响，因为umask只在创建文件时起作用。
   int fchmod(int fd, mode_t mode);  //根据文件描述符索引
   ```

4. 粘滞位，也称为t位，原本是给可执行文件设置，使得其能够在内存中驻留，使得下次装在此模块时较快，由于现在内存已经使用了page cache，此功能用处不大。更多是为目录设置，例如/tmp。

## 文件系统

1. FAT和UFS系统。UFS是Unix早期的文件系统，和ext2较为接近。

2. 一个FAT（File Allocation table）文件的本质是一个静态存储的单链表。静态指的是使用数组存储。比较轻量级，现在多用在U盘等设备中。有两种思路：

   1. 用一个结构体数组来存储多个文件，每个元素都是一个结构体，结构体中至少存在两个字段，next：指向下一个结构体在数组中的下标；data[size]：数据字段，存储size个字节。这样一来，从一个文件的头结构体，可以依次找到后续的所有结构体，将这些所有的结构体的data字段拼接到一起，就得到整个文件的内容。

   2. 用一个整型数组来记录文件的下一个块的下标值。用另一个结构体数组来记录每个块的数据。通过在下标数组中查找下标，同时可以在结构体数组中查找下一个块的数据。

3. 分完区之后还要格式化mkfs，才能挂载，因为格式化后才会有文件系统。

4. 早期linux系统使用的是Minix系统的文件系统，后来才发展出了ext2。

5. ```
   Filesystem OS type:          Linux
   Inode count:                 103424
   Block count:                 25856
   Reserved block count:        1292
   Free blocks:                 21508
   Free inodes:                 103413
   First block:                 0
   Block size:                  4096
   Fragment size:               4096
   Reserved GDT blocks:         24
   Blocks per group:            8320
   Fragments per group:         8320
   Inodes per group:            25856
   Inode blocks per group:      808
   ```

6. 超级块之后是一个一个的块组groups，块组内部依次为超级块（文件系统超级块的备份，只在前几个块组内有），块组描述符，GDT，block位图（用0和1记录block区域的使用情况），iNode位图（用0和1记录iNode区域的使用情况），iNode区域，block区域。

7. <img src="Linux系统编程.assets/image-20210504112913720.png" alt="image-20210504112913720" style="zoom:50%;" />

8. ![image-20210504110109409](Linux系统编程.assets/image-20210504110109409.png)

9. 文件系统屏蔽了设备的底层细节。linux在文件系统上还有一个VFS，统一了各个文件系统之间的操作，使得用户可以用同样的操作对不同文件系统的分区进行操作。

10. <img src="Linux系统编程.assets/image-20210504111017447.png" alt="image-20210504111017447" style="zoom: 67%;" />

11. mkfs：

    ```shell
    mkfs -t ext2 -b 4096 -i 1024 /dev/sdb1     #可以用mkfs.ext2替代。block大小为4k,iNode大小为1k。
    ```

12. 每个iNode块是一个结构体（通常为128B），其中stat函数获取的信息就是在这里取得的。例如有文件权限，时间戳，所有者，所属组，文件大小等，还有数据块指针（直接+1级+2级+3级），该指针指向block区域的数据块。但是不包括文件名，文件名存在于dentry结构中，文件的文件名是其所在目录的文件信息。block中有的是数据，有的是指针信息。

13. <img src="Linux系统编程.assets/image-20210504113611065.png" alt="image-20210504113611065" style="zoom:50%;" />

14. 块设备是以块为单位收发数据的，支持缓冲和随机访问。包括硬盘，CD和RAM盘等。字符设备是相对于块设备来说的，不可以寻址，只能逐字符地读写数据，包括串行端口和磁带等。

15. 由于硬盘扇区的单位是512B，较小，因此计算机读写数据是按照逻辑块block来进行的，这样可以提高I/O的效率。逻辑块的大小一般为扇区的2^n倍。文件的st_blocksize。一般设定为4KB大小。如果都是大容量的文件，例如视频，可以将block设置大一点。

16. 如果分区中的小文件太多，可能会把iNode消耗尽，但是还剩余很多的block。一个文件对应于1个iNode，最少占用1个block，即只使用了一个直接块指针。

17. 一个文件的大小指的是它所占用的data块。但是要在文件系统中存储一个文件还需要inode块，可能有间接块。

18. boot block是在分区的最开始的，存储着启动信息，文件系统不能使用。

19. ext2系统没有日志，速度特别快，CDN服务器是适合，文件丢了不怕，再从原始数据获取一份就可以了。

20. 目录也是一个文件，目录文件的block中存储着目录项，每个目录项包含iNode，目录或文件名。因此修改和删除文件名都是在操作文件所属目录的block。

21. linux文件的读取都是从根目录开始的，先找根的iNode，再从根的block找到子目录，再找子目录的iNode等等。

22. 每个文件的iNode中都存在一个属性，记录链接计数。

    1. 创建一个文件的硬链接，会新增一条目录项，iNode号为源文件的iNode，两个iNode中的硬链接计数+1，并不会创建新的iNode。由于iNode是一样的，因此硬链接是不分主从的，地位相等，权限，时间戳都一模一样。不能跨分区（iNode容易重复）或给目录建立硬链接。符号链接可以跨分区，可以给目录建立。

       ```shell
       [zj@ZJ ~]$ stat hha
         文件：hha
         大小：0               块：0          IO 块：4096   普通空文件
       设备：fd00h/64768d      Inode：201729670   硬链接：1
       权限：(0664/-rw-rw-r--)  Uid：( 1000/      zj)   Gid：( 1000/      zj)
       环境：unconfined_u:object_r:user_home_t:s0
       最近访问：2021-05-04 13:28:57.879173871 +0800
       最近更改：2021-05-04 13:28:57.879173871 +0800
       最近改动：2021-05-04 13:28:57.879173871 +0800
       创建时间：-
       [zj@ZJ ~]$ ln hha hha_hard   #创建硬链接
       [zj@ZJ ~]$ stat hha
         文件：hha
         大小：0               块：0          IO 块：4096   普通空文件
       设备：fd00h/64768d      Inode：201729670   硬链接：2
       权限：(0664/-rw-rw-r--)  Uid：( 1000/      zj)   Gid：( 1000/      zj)
       环境：unconfined_u:object_r:user_home_t:s0
       最近访问：2021-05-04 13:28:57.879173871 +0800
       最近更改：2021-05-04 13:28:57.879173871 +0800
       最近改动：2021-05-04 13:29:28.380924642 +0800
       创建时间：-
       [zj@ZJ ~]$ stat hha_hard
         文件：hha_hard
         大小：0               块：0          IO 块：4096   普通空文件
       设备：fd00h/64768d      Inode：201729670   硬链接：2
       权限：(0664/-rw-rw-r--)  Uid：( 1000/      zj)   Gid：( 1000/      zj)
       环境：unconfined_u:object_r:user_home_t:s0
       最近访问：2021-05-04 13:28:57.879173871 +0800
       最近更改：2021-05-04 13:28:57.879173871 +0800
       最近改动：2021-05-04 13:29:28.380924642 +0800
       创建时间：-
       [zj@ZJ ~]$ ln -s hha hha_sym    #创建符号链接
       [zj@ZJ ~]$ stat hha_sym
         文件：hha_sym -> hha
         大小：3               块：0          IO 块：4096   符号链接
       设备：fd00h/64768d      Inode：201873610   硬链接：1
       权限：(0777/lrwxrwxrwx)  Uid：( 1000/      zj)   Gid：( 1000/      zj)
       环境：unconfined_u:object_r:user_home_t:s0
       最近访问：2021-05-04 13:34:00.394965636 +0800
       最近更改：2021-05-04 13:33:56.925887595 +0800
       最近改动：2021-05-04 13:33:56.925887595 +0800
       创建时间：-
       ```

    2. 软连接相当于新建了一个文件，iNode号为新的，该文件的block中存放的是被连接文件的路径（因此该文件的size就是被链接文件的文件名大小，也是因为它存储的数据非常少，就不给他分配block了，而是把数据存储到iNode中了）。符号链接文件的权限，时间戳和被链接文件没有任何关系。


## 链接与重命名

1. 硬链接相关的函数：

   ```c
    #include <unistd.h>
   int link(const char *oldpath, const char *newpath);  //源文件为oldpath，新文件为newpath。如果newpath文件存在，那么不会覆盖，会返回-1，设置errno。相当于ln命令。
   int unlink(const char *pathname); //从文件系统中删除一个名称，当且仅当该名称对应的文件链接计数为0且没有进程正在打开它时，名称对应的文件才会被从硬盘上删除以腾出空间。该函数不会跟踪符号链接，而是删除符号链接本身。
   #include <stdio.h>  //标准库函数，相当于rm命令
   int remove(const char *pathname); //对于文件，会调用unlink,对于目录会调用rmdir。只能删除空目录。
   ```

2. 修改文件名或路径：

   ```c
   #include <stdio.h>  //标准库函数，相当于mv命令
   int rename(const char *oldpath, const char *newpath); //如果新旧路径名中仅文件名不同，则表示改名，否则表示移动位置并改名。打开的文件描述符不会受影响。如果newpath路径名存在，则会被原子性地替换。该函数不会跟踪符号链接。
   ```


## utime

1. ls看到的时间默认是mtime，即数据内容被修改的时间，Unix文件系统不记录文件的创建时间。

2. 修改文件的atime和mtime

   ```c
   #include <sys/types.h>
   #include <utime.h>
   int utime(const char *filename, const struct utimbuf *times);  //接受一个结构体指针
   struct utimbuf {
       time_t actime;       /* access time */
       time_t modtime;      /* modification time */
   };
   ```


## 工作目录

1. 目录的创建和销毁，切换当前路径。

   ```c
   #include <sys/stat.h>
   #include <sys/types.h>
   int mkdir(const char *pathname, mode_t mode);
   #include <unistd.h>
   int rmdir(const char *pathname);   //只能删除空目录。由于目录没有硬链接，删除目录就是从磁盘删除了。非空目录只能递归删除，先删除目录中的所有文件，再删除目录本身。
   ```

2. 获取和更改当前的工作路径：

   ```c
   #include <unistd.h>
   int chdir(const char *path);  //改变当前进程的工作路径。该函数能够突破chroot的假根，称为chroot穿越。和cd命令的功能相同。
   int fchdir(int fd);
   #include <unistd.h>
   char *getcwd(char *buf, size_t size);  //获取当前的工作路径，和pwd命令的功能相同。
   ```

3. chroot可以修改进程的根目录，可以起到保护其他目录的作用，是一种安全机制。

## 目录解析

1. 目录的解析可以用glob函数，也可以用一系列的函数opendir closedir readdir rewinddir seekdir telldir。

2. glob函数可以找到满足pattern的多个文件名，pattern是一个带通配符的字符串，*表示任意多个字符，?表示一个字符，shell的通配符用的也是这种。该函数的模式不会去递归子目录，这点也和shell一样。

   ```c
   #include <glob.h>
   int glob(const char *pattern, int flags, int (*errfunc)(const char *epath, int errno), glob_t *pglob);  //第一个参数为一个模式字符串，第二个参数一些可以相或的选项,0表示无选项。第三个参数为一个函数指针，在解析的过程中，每次出错都会调用该函数，以保存出错的路径和原因，可以在该函数内进行错误处理，如果不需要处理，可以传入NULL。第四个参数为解析的结果。
   void globfree(glob_t *pglob);  //使用完毕后，要用该函数释放内存空间，即gl_pathv指向的空间。
   typedef struct{
       size_t gl_pathc;  //匹配pattern的路径数量
       char **gl_pathv;  //匹配的路径字符串数组，类似于main函数的输入参数管理方式。这里会申请2累内存，一个是字符指针数组，一共有gl_pathc个元素，然后是每个字符指针所指字符串的内容。这里的路径都是绝对路径。
       size_t gl_offs;   //偏移，在gl_pathv的开头中保留gl_offs个位置，用NULL填充。
   } glob_t  //gl_pathc, gl_pathv和argc, argv一样。
   //常用的flags选项：
   GLOB_DOOFFS  //根据gl_offs的值，进行偏移。
   GLOB_NOCHECK //如果pattern没有匹配到任何内容，返回pattern，即将pattern存入glob_t数据中。默认情况下，会返回GLOB_NOMATCH。
   GLOB_APPEND  //追加到现有的参数glob_t数据中，只能用于第二次或以后。可以将多次的查找合并。默认是覆盖。
   GLOB_NOSORT  //不对文件名进行排序，可以节省运行时间。默认情况下会进行排序。ls命令默认的结果就是排过序的。
   ```

3. 例子：获取所有匹配/etc/a*.conf的路径：文件和目录都会被找到。/etc/\*只能找到非隐藏的文件和目录，相当于ls /etc/\*的结果。如果要查看隐藏文件或目录，模式为/etc/.\*     可以为glob函数指定一个选项GLOB_APPEND，把两次（一次非隐藏，一次隐藏）匹配到的路径追加到一起。

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <glob.h>
   #include <string.h>
   int errfunc1(const char *epath, int errno){
       print("%s\n",epath);
       fprintf(stderr,"%s\n",strerror(errno));
   }
   int main(int argc, char** argv){
       glob_t globres;
       if (glob(argv[1],0,errfunc1,&globres) != 0) 
           fprintf(stderr,"Error");
       for(int i=0;i<globres.gl_pathc;i++){
           printf("%s\n",globres.gl_pathv[i]);
       }
       globfree(&globres);
   }
   ```

4. main的命令行参数，在shell下如果使用通配符，会被shell自动展开(不是所有的shell都会自动展开)，例如：

   ```shell
   ./main *.c    # *.c会被替换，argc不止两个。
   ```

5. 可以使用glob函数将一段命令行字符串解析为argv的样式，利用它的自动分配字符串内存的功能：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <glob.h>
   #include <string.h>
   int main() {
       char* linebuffer = NULL;
       size_t linebuf_size = 0;
       char* tok = NULL;
       glob_t globres;
       int times = 0;
       if (getline(&linebuffer, &linebuf_size, stdin) < 0) {
           perror("getline()");
           exit(1);
       }
       while (1) {
           tok = strsep(&linebuffer, " \t\n");
           if (tok == NULL)//空指针，表示到了字符串的结尾了，此时应该退出循环。
               break;
           if (tok[0] == '\0')  //空字符串。这个和上面的并不一样。上面是判断tok是否为0，这个是判断*tok是否为0。只不过指针的0一般用NULL，字符的0一般用'\0'。
               continue;
           glob(tok, GLOB_NOCHECK | GLOB_APPEND * times, NULL, &globres); //这里需要循环第一个次不能使用GLOB_APPEND，之后才需要。GLOB_NOCHECK表示如果找不到对应的匹配，则返回pattern本身。
           times = 1; //times初始为0，后续都为1。
       }
       for (int i = 0;i < globres.gl_pathc;i++) {
           printf("[%d]:[%s]\n", i, globres.gl_pathv[i]);
       }
       globfree(&globres);
       exit(0);
   }
   ```

6. 上述函数实验：

   ```shell
   ls -l    /etc
   [0]:[ls]
   [1]:[-l]
   [2]:[/etc]
   ```

7. 目录操作函数：

   ```c
   #include <sys/types.h>
   #include <dirent.h>
   DIR *opendir(const char *name); //通过目录文件名打开一个目录
   DIR *fdopendir(int fd); //将一个open过的目录的文件描述符转化为目录流
   int closedir(DIR *dirp);  //关闭一个目录流
   struct dirent *readdir(DIR *dirp); //从一个目录流dirp中读取一条数据，每次读取都会移动目录项位置指针。类似于文件的read。
   struct dirent{   //directory entry 目录项
       ino_t             d_ino;       //inode号
       off_t             d_off;       //下一个dirent的偏移
       unsigned short    d_reclen;    //本条记录的长度    
       unsigned char     d_type;      //当前文件的类型
       char              d_name[256];  //当前文件的文件名
   }
   void rewinddir(DIR *dirp); //将目录流dirp的当前位置指针恢复到开头
   void seekdir(DIR *dirp, long loc);  //调整目录流当前位置指针的位置，下一次readdir时，就会读取这个目录项。
   long telldir(DIR *dirp);  //返回目录流dirp的目录项位置指针的当前位置。
   int scandir(const char *dirp, struct dirent ***namelist, int (*filter)(const struct dirent *), int (*compar)(const struct dirent **, const struct dirent **)); //扫描目录dirp(不包含子目录)，对每个目录项调用过滤器filter函数，如果filter为NULL，则所有目录项都被选择。filter函数有一个参数，为目录项的指针，返回值为int类型。对满足条件(返回值非0)的目录项使用compar函数进行排序，然后结果存储到目录项指针数组namelist中。namelist数组和该数组的每个指针所指的每个dirent的结构体都是由I/O库使用malloc分配管理的，使用完都应先逐个释放结构体，再释放数组。如果调用成功，函数的返回值为namelist数组的元素个数。失败返回-1，并设置errno。
   int alphasort(const struct dirent **a, const struct dirent **b); //这两个函数是glibc自带的两个函数，可以作为scandir函数的compar参数，比较的内容都是文件名，这个函数按照strcoll函数的规则比较。完全按照字母顺序来比较，例如abc就在abd之前。
   int versionsort(const struct dirent **a, const struct dirent **b); //按照strverscmp函数的规则比较。例如他会将2放在10前面，而不是按照一位一位地比较。
   ```

8. 例子，逆序打印当前目录中的文件名：

   ```c
   #define _DEFAULT_SOURCE
   #include <dirent.h>
   #include <stdio.h>
   #include <stdlib.h>
   int main(void){
       struct dirent **namelist;
       int n;
       n = scandir(".", &namelist, NULL, alphasort); //不过滤，只排序。因为要修改二级指针的值，所以用了三级指针。
       if (n == -1) {
           perror("scandir");
           exit(EXIT_FAILURE);
       }
       while (n--) {
           printf("%s\n", namelist[n]->d_name);
           free(namelist[n]);  //namelist数组的每个元素都是一个struct dirent结构体的指针。结构体的空间也是有scandir申请的，用完应该由使用者释放。
       }
       free(namelist);  //由使用者释放，最后释放数组本身的空间。
       exit(EXIT_SUCCESS);
   }
   ```

9. 例子：解析/etc下有多少文件

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <dirent.h>
   int main(){
   	DIR *dp;
       struct dirent *cur;
       if((dp = opendir("/etc")) == NULL){
           perror("opendir()");
           exit(1);
       }
       
       while((cur = readdir(dp)) != NULL){
           printf("%s\n",cur->d_name);
       }
   }
   ```

10. 如果要想获取一个目录的大小，即du命令的结果，需要进行递归解析该目录下/*和/.\*的目录和文件大小，如果遇到目录，要递归进行处理。递归的时候要注意，linux的文件系统不是树状结构，每个目录下必定有2个隐藏文件，.和.. 递归的时候需要排除掉这两个目录。排除完就可以认为是树状的了，不过还要排除硬链接和符号链接。

    ```shell
    du flen.c  #查看flen.c文件所占用的磁盘空间
    4  #结果为4，单位是KB。通过stat也可以看到该文件占用了8个block。即使该文件的内容只有432B大小。
    # 当du一个目录时，会将该目录下的所有文件和目录（包含隐藏的），除了..意外，都执行一遍du命令。例如一个目录下有1个文件test.txt和2个目录std,sys，两个目录的du结果分别为56KB和128KB。test.txt文件和.目录都占用8个block，即4KB。所以该目录的du结果为56+128+4+4=192KB。
    du #没有参数时，表示对当前目录执行du命令。
    ```

11. 例子，自定义的du命令：

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/types.h>
    #include <sys/stat.h>
    #include <unistd.h>
    #include <glob.h>
    #include <string.h>
    #include <libgen.h>
    #include <fcntl.h>
    
    #define PATHSIZE 256
    static long long mydu(const char* pathname) {
        static struct stat statres; //仅在递归点之前使用，所以可以放在静态区。
        static char strippath[PATHSIZE] = { 0 }; //去除完末尾/的路径
        static char conpath[PATHSIZE] = { 0 };
        glob_t globres;
        static int globret = 0;
        long long sum = 0;
        char* filename;
        strncpy(strippath, pathname, PATHSIZE);//复制一份，不直接在argv上修改
        if (strippath[strlen(strippath) - 1] == '/') {
            strippath[strlen(strippath) - 1] = '\0';  //删除路径名末尾的/
        }
        if (lstat(pathname, &statres) < 0) {
            perror("lstat");
            exit(-1);
        }
        if (!S_ISDIR(statres.st_mode)) {
            return statres.st_blocks / 2;
        } else {
            strncpy(conpath, strippath, PATHSIZE);
            strncat(conpath, "/*", 3); //非隐藏文件和目录，要求第三个参数比第二个参数的长度大，且比第一个参数的空间小。
            globret = glob(conpath, 0, NULL, &globres);
            if (globret != 0 && globret != GLOB_NOMATCH) { //无法在空目录中寻找到非隐藏文件
                perror("glob");
                exit(-1);
            }
            strncpy(conpath, strippath, PATHSIZE);
            strncat(conpath, "/.*", 4); //隐藏文件和目录
            globret = glob(conpath, GLOB_APPEND, NULL, &globres);
            if (globret != 0 && globret != GLOB_NOMATCH) {  //追加到上一次的结果中
                perror("glob()");
                exit(-1);
            }
            sum += statres.st_blocks / 2;
            for (int i = 0; i < globres.gl_pathc; i++) {
                filename = basename(globres.gl_pathv[i]);
                if (!strcmp(filename, ".") || !strcmp(filename, ".."))
                    continue;
                sum += mydu(globres.gl_pathv[i]);
            }
        }
        globfree(&globres);
        return sum;
    }
    int main(int argc, char* argv[]) {
        if (argc != 2) {
            fprintf(stderr, "%s", "Ussage:...\n");
            exit(-1);
        }
        printf("%lldK\t%s\n", mydu(argv[1]), argv[1]);
    }
    ```

12. 由于每一次递归都要将局部变量压入栈中，因此将变量尽量存储在静态区是一种比较好的节省栈的方法，这样可以使得递归的次数增加。只在递归点前使用的局部变量是可以优化为static存储的，即递归返回的时候，该变量不会被使用到。

13. 将路径名拆分为目录名和文件名，路径名使用绝对或相对路径都可以：

    ```c
    #include <libgen.h>
    char *dirname(char *path); //两个函数可能会修改path，返回值存储在函数的静态区，可能会被后续的调用覆盖掉。也有可能指向path的一部分，如果要修改返回值，应strcpy到其他地方修改。
    char *basename(char *path);
    //通常情况下用最后一个/分割。二者都不包含/。path结果如果有/，会先被去掉。
    //如果path不包含/(即只有一个文件或目录名),则dirname为.，basename为路径名本身。
    
    //特殊情况：
     1 如果path就是/，那么dirname和basename都是"/"
     2 如果path是空指针或指向一个空字符串(含有空白字符)，则dirname和basename都是"."
    //除特殊情况外，都可以将dirname和"/"还有basename拼接起来，得到path。
    ```

14. ![image-20230504023001398](assets/image-20230504023001398.png)

# 用户信息操作

1. 用户信息文件和操作函数：/etc/passwd /etc/group /etc/shadow这三个文件，存储着UID，GID和用户名，组名，密码的关系。不建议直接查询文件来获得相关信息，因为不是所有的Unix系统都是使用这些文件。FreeBSD上使用一个数据库BDB来存放这些信息。HP-Unix利用文件系统来存储这些信息。

   ```shell
   # /etc/passwd文件
   zj:x:1000:1000:Jian:/home/zj:/bin/bash #登录用的用户名:具有密码:用户ID:初始组ID:注释字段，安装Ubuntu时输入的:家目录:登录shell路径
   # /etc/group
   root:x:0: #组名:组密码:组ID:除了同ID的用户以外，组内成员ID
   adm:x:4:syslog,zj  #adm组除了还有两个成员用户syslog和zj
   # /etc/shadow
   zj:$6$SFRinE5OA7YV.tJY$kmMwKLTaGsm7Q9NkU.nms/nT2nTzfozsU0goIjwD66ll0LaP33R3Rf8i5f0KUIkIl7Wp9wLZOCJOUnaLnFkk80:19477:0:99999:7::: #用户名:加密后的密码:后续的字段都是关于密码时间的记录或设置。
   #第二个字段表示Hash后的结果，分为三段，用$分割。第一段的6表示加密方式为sha512，第二段表示做hash运算之前使用的随机盐值。每个用户都不一样，这样可以保证即使密码相同，由于盐值不同，得出的hash值也不同。第三段是Hash值。
   ```

2. 用户信息操作函数：

   ```c
   #include <sys/types.h>
   #include <pwd.h>
   struct passwd *getpwnam(const char *name); //通过用户名查询
   struct passwd *getpwuid(uid_t uid); //通过用户ID查询
   struct passwd {   //和passwd文件的顺序相同。
        char   *pw_name;       /* username */
        char   *pw_passwd;     /* user password */
        uid_t   pw_uid;        /* user ID */
        gid_t   pw_gid;        /* group ID */
        char   *pw_gecos;      /* user information */
        char   *pw_dir;        /* home directory */
        char   *pw_shell;      /* shell program */
   };
   ```

3. 组信息操作函数：

   ```c
   #include <sys/types.h>
   #include <grp.h>
   struct group *getgrnam(const char *name);
   struct group *getgrgid(gid_t gid);
   struct group { //和/etc/group文件中的顺序相同
       char   *gr_name;        /* group name */
       char   *gr_passwd;      /* group password */
       gid_t   gr_gid;         /* group ID */
       char  **gr_mem;         /* NULL-terminated array of pointers to names of group members 存储组成员名的字符串数组*/
   };
   ```

4. 为了防止穷举对密码进行爆破，有时会进行口令随机校验，即使用户输对了密码，也要提示错误，让其重新输入。较为重要的操作，可能会进行随机校验。

5. shadow文件的权限为000，所有者和所属组都是root，但是这并不妨碍root用户读写它，这样的权限主要是提醒root用户，尽量不要去修改它。

6. 密码信息操作函数：

   ```c
   #include <shadow.h>
   struct spwd *getspnam(const char *name);
   struct spwd {
        char *sp_namp;     /* Login name */
        char *sp_pwdp;     /* Encrypted password */
        long  sp_lstchg;   /* Date of last change(measured in days since 1970-01-01 00:00:00 +0000 (UTC)) */
        long  sp_min;      /* Min # of days between changes */
        long  sp_max;      /* Max # of days between changes */
        long  sp_warn;     /* # of days before password expires to warn user to change it */
        long  sp_inact;    /* # of days after password expires until account is disabled */
        long  sp_expire;   /* Date when account (measured in days since 1970-01-01 00:00:00 +0000 (UTC)) */
        unsigned long sp_flag;  /* Reserved */
   };
   #include <crypt.h> //crypt函数只推荐用来对用户的密码进行加密，不建议用于一般的加密。注意，使用crypt.h头文件中的函数，需要显式链接上libcrypt库，gcc参数为 -lcrypt；makefile写法为：LDFLAGS += -lcrypt
   char* crypt(const char *phrase, const char *setting); //phrase是待加密的明文，setting参数是由加密方法和盐值构成的字符串。也就是/etc/shadow文件中第二个字段中第三个$及之前的字符。
   ```

7. 例子，验证用户的密码，需要root执行权限：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <unistd.h>
   #include <shadow.h>
   #include <string.h>
   #include <crypt.h>
   int main(int argc, char* argv[]) {
       if (argc < 2) {
           fprintf(stderr, "Usage:...\n");
           exit(1);
       }
       char* input_pass;
       struct spwd* shadowline;
       char* crypted_pass;
       input_pass = getpass("input you passwd\n"); //从终端获取内容，但是不回显输入，不包含末尾的换行符。目前已经不推荐使用该函数了，可以使用termios来关闭终端的回显功能。
       shadowline = getspnam(argv[1]); //这一步会查询/etc/shadow文件，如果进程没有root权限，会失败。
       crypted_pass = crypt(input_pass, shadowline->sp_pwdp); //该函数的第二个参数只会读取前几个字符。
       if (strcmp(crypted_pass, shadowline->sp_pwdp)) {
           puts("Error");
       } else {
           puts("Ok");
       }
   }
   ```

# 时间操作相关函数

1. 时间操作的流程：使用time函数获取time_t的整数时间戳，然后使用localtime或gmtime构建struct tm结构体。mktime可以将结构体转化为时间戳。使用strftime将tm结构体转化为格式化的字符串。

2. <img src="assets/image-20230504200250203.png" alt="image-20230504200250203" style="zoom: 80%;" />

3. 使用stat函数获取文件的时间属性时，得到的也是time_t类型。

4. 时间操作函数：

   ```c
   #include <time.h>
   time_t time(time_t *tloc); //从内核中获取时间，以秒为单位的计数，从eopch开始，也就是1970年1月1日00:00。如果参数不是NULL，时间戳会同时存储在参数和返回值中。
   
   struct tm *gmtime(const time_t *timep);   //根据时间戳构建tm结构体，格林威治时间
   struct tm *localtime(const time_t *timep); //根据时间戳构建tm结构体，本地时间
   time_t mktime(struct tm *tm);    //将tm结构体转化为时间戳。可能会修改结构体。因为结构体中存在冗余，例如tm_wday和tm_yday都可以通过之前的字段推导出。还有就是某些字段超出取值范围的话，会被用于修改其他字段，例如1月33日，会被当作2月2日。
   struct tm {
       int tm_sec;    /* Seconds (0-60) 范围不是0-59，是因为有闰秒的存在*/
       int tm_min;    /* Minutes (0-59) */
       int tm_hour;   /* Hours (0-23) */
       int tm_mday;   /* Day of the month (1-31) */
       int tm_mon;    /* Month (0-11) 比平时说的少1*/
       int tm_year;   /* Year - 从1900开始算 */
       int tm_wday;   /* Day of the week (0-6, Sunday = 0) 周日是一周的第一天*/
       int tm_yday;   /* Day in the year (0-365, 1 Jan = 0) */
       int tm_isdst;  /* Daylight saving time 是否开启夏令时调整*/
       //夏令时调整，是一种为了节约能源而人为规定的地方时间调整，因为夏天天亮的早，所以一般将时钟调快一个小时，使得人可以早起早睡，充分利用太阳光，例如1986-1991年中国规定：每年从四月中旬第一个星期日的凌晨2时整（北京时间），将时钟拨快一小时，即将表针由2时拨至3时，夏令时开始；到九月中旬第一个星期日的凌晨2时整（北京夏令时），再将时钟拨回一小时，即将表针由2时拨至1时，夏令时结束。中国的时区跨度太大，不适合，现在能源供应比较充足，也不必这么做。另一种提高白天利用率的方法是，调整工作时间，例如可以将一天的工作时间都向前调整1个小时。
   };
   size_t strftime(char *s, size_t max, const char *format, const struct tm *tm);//将tm结构体按照format格式,输出到一个字符串s中(最多输出max的字符)。返回值为成功输出的字符串的长度。format例子："%Y-%m-%d" 可能会输出"2021-05-05"。
   ```

5. 通过tm结构体来引用具体的年月，会发现年是从1900年开始计算的，例如2010年时，tm.tm_year为110。而通过strftime格式化输出的时候就没有这种问题。

6. 比较诡异的是，time获取的时间戳是从1970年开始算的，而struct tm中的tm_year字段却是从1900年开始计算的。

7. 一般来说，返回值为指针的库函数，如果有_r版本的函数，那么普通版本的指针指向的空间都是放在静态区的，\_r版本的函数是修改后的线程安全的版本。静态区的好处是不用提供回收内存的配对函数，因为始终就只有那么一点内存被使用，而如果放在堆上，那么每次调用都会产生一块内存泄漏。静态区的缺点是，调用完该函数后，应该立即使用，再一次调用该函数，就会冲掉原来的数据。

8. 求当前时间100天以后的日期：

   ```c
   time _t t1 = time(NULL);
   struct tm *tm=localtime(&t1);
   tm->tm_mday += 100;  //tm_day合理的取值范围为1-31。
   mktime(tm);   //mktime会先判断tm结构体是否合法，如果不合法会将其纠正为合法的结构体。会自动进位。返回值没用。
   ```

# 进程环境

1. C程序总是从main函数开始执行，其原型如下。

    ```c
    int main(int argc, char* argv[]); //argc是命令行参数的个数，argv是指向各个参数的指针构成的数组。
    ```

2. 内核通过exec函数替换程序镜像来执行C程序。在调用main函数前，会先调用一个特殊的启动例程，这是因为链接器将该启动例程放置在了程序的起始地址处。启动例程从内核获得main函数的命令行参数和环境变量，然后按照main函数的定义来调用它。

    ```c
    exit(main(argc, argv)); //启动例程调用main函数的可能方式。实际上该例程通常用汇编语言编写。
    ```

3. main函数作为程序的入口是人为规定的，该函数由C启动例程来调用。可以通过设置链接器来将其他函数来代替main函数。

## 进程终止方式

1. 进程有8种终止的情况，其中5种为正常，3种为异常。
2. 进程的正常终止方式：
   1. 从main函数return返回。因为从main函数返回后，启动例程也会立即调用exit函数，本质上和方式2类似。
   2. 主动调用exit函数。
   3. 主动调用\_exit或\_Exit函数。
   4. 最后一个线程从其启动例程中返回。启动例程就是线程的执行序列。类似于方式1。但是该线程的返回值不用作进程的返回值。进程此时以0作为终止状态返回。
   5. 最后一个线程调用了pthread_exit函数。类似于2。和4类似，此时进程的终止状态总是0。
3. 进程的异常终止：

   1. 调用abort函数。该函数会发送一个sigabort信号给当前进程，响应时会产生一个coredump文件。它是方式2的一个特例。
   2. 被动接收到一个信号并终止，例如Ctrl+C发出的SIGINTR信号的默认行为就是终止进程。或者kill命令。信号可由自身，其他进程，内核产生。例如进程内存访问越界或除以0时，内核会发送响应的信号。
   3. 最后一个线程对取消请求并作出响应。默认情况下，“取消”以延迟方式发生：一个线程要求取消另一个线程，若干时间后，目标线程终止。
4. 不论进程如何终止，最后都会执行内核中的同一段代码。这段代码为进程关闭所有打开的文件描述符，释放它所使用的内存。
5. 正常终止时，子进程通过返回值来通知父进程其终止状态。异常终止时，内核产生一个指示其异常终止原因的终止状态。这两种情况下，父进程都可以用wait或waitpid来获得子进程的终止状态。

## exit, _exit, _Exit

1. 三个函数都用于正常终止一个程序，不同的是\_exit和\_Exit会立即进入内核，而exit会先执行一些清理处理，然后再进入内核。

2. exit()函数会执行标准I/O库的清理关闭操作。为所有打开的流调用fclose，这会导致输出缓冲区的数据被fflush。将它的子进程过继给init进程，发送SIGCHILD信号通知它的父进程。

3. return的返回值是给父进程看的，父进程可以通过wait函数来收集该返回值。shell可以通过读取$?变量来获得程序的返回值。

4. 发生以下任意一种情况，进程的终止状态是未定义的：

    1. 调用三个exit时，不带终止状态。

    2. main函数中执行了不带参数的return语句。

    3. main函数的定义中，没有声明返回值类型为整型。例如为void或没有任何类型。

5. 但是若main函数定义了返回类型为整型，并且main执行到最后一条语句时隐式返回（不出现return语句），那么进程的终止状态为0。这是C99中规定的，在以前若main函数终止时没有显式使用return语句或exit函数，则进程的终止状态是未定义的。例如：

    ```c
    #include <stdio.h>
    main(){
        printf("hello,world\n");
    } //该程序的终止码在某些平台上是随机的。具体的返回值取决于返回时栈和寄存器的内容。
    //gcc returncode.c -o returncode -std=c89   这个程序的终止状态为12，即printf输出的字符个数，因为printf的返回值会存放在eax寄存器中，其后直接从栈中返回，则相当于return 12。
    //如果修改-std=c99选项或者不指定std(因为较新的gcc默认使用的标准已经覆盖C99了)，终止码就变成了0。但是编译的时候会提示如下，也就是main函数没有显式声明返回值类型：
    returncode.c:2:1: warning: return type defaults to ‘int’ [-Wimplicit-int]
        2 | main() {
          | ^~~~
    ```

6. main函数return 一个整型值，等价于调用exit(该整型值)。为了统一管理，在main函数中推荐使用exit而不是return。普通函数的结尾可以使用return。这样通过grep命令可以统计到整个工程中所有的退出点。

    ```c
    return a; //等价于 exit(a);  但是某些编译器并不了解这种等价关系，可能会报warning，gcc不会。
    ```

7. ```c
   #include <stdlib.h>
   void exit(int status); //将status&0377的结果返回给父进程。即保留status的低8位，即从-128到127。C标准提供了两个宏可以作为status的值，EXIT_SUCCESS和EXIT_FAILURE。
   void _Exit(int status); //立刻终止调用进程
   #include <unistd.h>
   void _exit(int status); //完全等价于_Exit(),不过此函数是系统调用(POSIX.1定义)而非库函数。
   
   #include <unistd.h>
   void _exit(int status);  //exit函数所依赖的下层的系统调用。不过这两个函数不会执行钩子函数和I/O清理。
   void _Exit(int status);  //功能同上。这两个函数用在意外的分支。例如switch-case中的default分支，只有它之前的程序出错才会执行到这一步，因此一旦执行到这一步就应该尽快退出。
   ```

8. 终止处理程序，最早由C89引入，因此早于C89的系统例如SVR3、4.3BSD都不支持这一机制：

    ```c
    int atexit(void (*function)(void)); //向一个进程注册它正常终止前会调用的函数(即钩子函数，又称为终止处理函数)。返回0表示成功挂上钩子。钩子函数没有参数，没有返回值。注册过的钩子函数，只有在进程正常终止时才会被逆序调用(类似于栈)，可以认为钩子函数的入口地址被放在一个栈中。一个函数可以被注册多次，因此也会被调用多次。
    int on_exit(void (*function)(int , void *), void *arg); //被注册的函数又两个参数，第一个为exit的参数或return的返回值。第二个为注册时给on_exit提供的第二个参数arg。
    ```

9. ISO C要求，系统应该至少支持32个终止处理程序，可以更多，实际也是如此。使用sysconf函数来确定当前平台最多支持的终止处理程序上限。

    ```c
    #include <stdio.h>
    #include <unistd.h>
    #include <stdlib.h>
    int main() {
        printf("_SC_ATEXIT_MAX: %ld\n", sysconf(_SC_ATEXIT_MAX)); //Ubuntu22.04上结果为2147483647，也就是2^31个。
        exit(0);
    }
    ```

10. 从下图中可以看到C启动程序调用main函数，main函数会再调用用户自己写的程序。正常情况下，他们可以依次return。不过在任意位置都可以调用exit函数，exit函数内部会调用之前注册过的所有钩子函数最后调用标准I/O清理程序。然后自己再调用\_exit或\_Exit进入内核。当然main和用户函数也可以直接调用\_exit或\_Exit来直接进入内核，不过这样就无法调用钩子函数了。从C启动例程指向exit函数的箭头，这次调用并非用户主动调用，而是C启动例程自动调用的。

11. 下图展示了一个C程序是如何产生和消亡的。内核使得程序执行的唯一方法就是调用exec函数。进程自愿终止的唯一方法就是显式或隐式地调用\_exit或\_Exit函数。进程也可以非自愿地通过收到一个信号而终止。

12. <img src="assets/image-20230505103736237.png" alt="image-20230505103736237" style="zoom: 80%;" />

13. 从上图中可以看出exit函数会执行标准I/O清理，但是ISO C并不处理文件描述符，多进程以及作业控制，因此这一定义对Unix系统是不完整的。

14. ISO C定义了\_Exit函数，是为了给进程提供一种无需执行终止处理程序或信号处理程序而终止的方法。对于标准I/O流是否冲洗，取决于实现，在Unix系统中，\_Exit和\_exit是同义的，都不冲洗标准I/O流。\_exit由exit调用。

15. 通过fork创建子进程时，子进程会继承注册记录。但是通过exec函数后，会清除注册记录。

16. 例子，测试钩子函数：

       ```c
       #include <stdio.h>
       #include <stdlib.h>
       #include <unistd.h>
       static void my_exit1(void) {
           printf("my_exit1 is done\n");
       }
       static void my_exit2(void) {
           printf("my_exit2 is done\n");
       }
       int main(void) {
           if (atexit(my_exit2) != 0) {
               perror("can’t register my_exit2");
               exit(2);
           }
           if (atexit(my_exit1) != 0) {
               perror("can’t register my_exit1");
               exit(11);
           }
           if (atexit(my_exit1) != 0) {
               perror("can’t register my_exit1");
               exit(12);
           }
           printf("main is done\n");
           return 0; //return 0和exit(0)都会导致钩子函数被调用，会依次调用my_exit1,my_exit1,my_exit2三个函数；_exit(0)和_Exit(0)都不会。
       }
       ```

17. 钩子函数的典型用法：在打开多个文件时，如果后面的文件打开失败，为了防止内存泄露，需要关闭之前打开的所有文件，再调用exit，可以使用钩子函数来完成这一操作。类似于C++中的析构函数。

      ```c
      void closefd1(void){
          close(fd1);
      }
      fd1 = open();
      if(fd1<0){
          perror();
          exit(1); //exit只会关闭标准I/O，不会管系统I/O。
      }
      atexit(closefd1);   //当fd1成功打开后，立刻注册钩子函数，这样一旦后续的文件打开失败，exit时会自动释放掉fd1的内存。
      ```

18. 如果发生了意外的不可控的错误，就应该调用\_exit或\_Exit直接退出或者调用abort()得到一个coredump，而不是调用exit()。因为后者会刷新各种流，调用钩子函数，进而会扩大错误的影响范围。


## 命令行参数分析

1. 当通过shell执行一个新的程序时，shell会收集命令行参数，然后在exec时传递过去。POSIX.1和ISO C都要求argv[argc]为NULL，这样可以不通过argc也可以获得命令行参数的个数。

   ```c
   for (int i = 0; i < argc; i++) //可以遍历命令行参数
   for (int i = 0; argv[i] != NULL; i++) //也可以
   ```

2. 可以使用echo命令来观察展开的命令行参数，但是echo不回显第0个参数（即echo本身）：

   ```shell
   zj@hit:~/linux_c/process$ echo ls *.c #这句话的输出会展示当去掉echo直接输出时，shell得到的命令行参数的样子。
   ls -l exec.c fork.c mydaemon.c mysu.c shell.c test.c uid.c wait.c
   zj@hit:~/linux_c/process$ `echo ls -l *.c`   #可以用` `或$( )将命令括起来，这样可以将一个命令的输出作为另一个命令的一部分来执行。
   -rw-rw-r-- 1 zj zj    0 May  8 00:47 exec.c
   ...
   ```

3. 命令行参数的使用方法非常灵活，需要专门的函数分析，几乎所有的程序都是使用这两个函数来解析的：

   ```c
   //常见的命令行参数的用法，有时顺序可以随意安排：
   //纯选项 -v(短) --version(长)
   //多个短选项可以连用 -abc(等价于 -a -b -c)
   //带参数的选项 -a xx
   //纯参数 xx
   
   #include <unistd.h>
   int getopt(int argc, char * const argv[], const char *optstring); //前两个参数是命令行参数，将main函数获取到的对应变量传过来即可，optstring是要分析的选项，不包括-。如果成功找到了一个选项，则返回该字符。如果没有则返回-1。
   //argv中以-开头的每个字符串("-"和"--"除外)都会被认为是一个选项。除了开头的-以外的另一个字符(因为getopt只能处理短选项)被认为是该选项的特征字符，可以放到optstring中。getopt也可以处理短选项连用的情况，-abc会自动当作三个选项 -a -b -c。
   //关联的全局变量
   extern char *optarg;
   extern int optind, opterr, optopt;
   #include <getopt.h>
   int getopt_long(int argc, char * const argv[], const char *optstring, const struct option *longopts, int *longindex);
   ```

4. 带参数的选项连写需要注意：  -my 4相当于 -m -y 4。如果要用touch创建一个名为-a的文件，不能用touch -a，因为此时-a会被认为是选项，应该用touch ./-a。或者用touch -- -a，其中--表示选项传参结束。

5. 在optstring开头加一个 - ，可以获取非选项的传参，每个非选项的传参都被认为是选项为-1的传参，例如 ls -l /etc中的/etc，其中l后面没有 : ，即表示它没有对应的选项参数，即/etc是非选项参数，此时相当于ls -l -1 /etc。

6. 全局变量optind记录着当前getopt要获取argv的下一个字符串的下标(index)，初始为1，即argv[optind - 1]为当前选项的命令行字符串。如果还想再处理一套命令行参数或者一个参数向量，可以将optind设置为1，然后执行getopt函数。

7. ```c
   int c = getopt(argc,argv,"HMSy:md"); //函数会逐个从argv中取出字符串，来比对是否等于"-H","-M"等。如果成功就返回匹配到的字符串,但不包含-。如果也需要接受选项后面的参数，可以在对应的字符后面加:。当匹配到有选项的参数时，全局变量optarg就指向该选项的参数。
   //例如:   ./myls -H -d -y abc -s   会跳过./myls这个非选项传参，当处理到-c时，optarg会指向abc字符串。
   //有些情况下参数并非是和选项相关联的，例如 ls -l /etc 其中/etc就不是-l的参数。
   ```

8. 正常的处理流程：

   ```c
   while(1){
       int c = getopt(argc,argv,"-HMSy:md");
       if (c<0)
           break;  //找不到匹配的选项
       switch(c){
           case 1:  //非选项的传参
               break;
           case H:
               break;
           case y:
               break; //待选项的传参，可以使用optarg来获取该选项对应的参数。
           ...
           default:
               exit();
       }
   }
   ```


## 环境变量

1. 较早时候，大多数的Unix系统支持main函数带三个参数的，第三个参数就是环境变量，但是ISO C规定main函数只有两个参数，因此POSIX.1也规定使用environ来代替第三个参数。

    ```c
    int main(int argc, char* argv[], char* envp[]);
    ```

2. Unix内核并不关心环境变量。它的解释完全取决于各个应用程序。例如shell使用了大量的环境变量，例如USER和PATH等，程序也使用，例如LS_COLORS。通常在一个shell的启动文件中设置环境变量，以控制shell的行为。POSIX.1定义了一些环境变量，例如LC_ALL，PATH等，而ISO C并没有定义任何环境变量。

3. 进程的环境变量是以键值对的方式存储，key="value"。等号两侧不能空格。

4. 每个程序都有一个环境表，和参数表一样，都是字符指针数组。在程序内使用全局变量environ来获取：

    ```c
    extern char **environ;  //也称为环境指针,使用方法和argv一样，不过没有argc来计数，而是用来NULL来标记字符指针数组的结束。
    for (int i =0; environ[i] != NULL;i++){
        printf("%s\n",environ[i]);
    }
    ```

5. 可以使用env命令查看当前shell的环境变量，export命令用来设置环境变量，如果不加参数表示显示当前的环境变量，它会比env少一个变量   _=/usr/bin/env   。

   ```shell
   SHELL=/bin/bash                   # env命令的输出,大多数预定义环境变量的名称为全大写字母。
   declare -x SHELL="/bin/bash"      # export命令的输出，指明了创建的方式和类型。
   ```

6. 通常通过以下环境变量相关的操作函数来使用环境变量，而不是直接使用environ变量，但若要查看整个环境变量，则必须使用environ指针：

   ```c
   #include <stdlib.h>  //getenv是ISO C定义的，其余都是POSIX.1额外定义的。
   char *getenv(const char *name);   //根据键名获取对应的值。如果不存在对应的环境变量，则返回NULL。
   int setenv(const char *name, const char *value, int overwrite); //如果name不存在，则创建；如果name存在，且overwrite非0，则先删除现有的定义，再创建一个新的，值为value。如果name存在，且overwrite为0，则什么也不做。
   int unsetenv(const char *name);   //删除一个环境变量的定义，即使name不存在也不会报错。等价于unset命令。
   int putenv(char *string);  //string的形式为"name=value"。如果name存在，则会先删除旧的，再添加新的，string没有const修饰，也无法控制覆盖与否，不推荐使用。
   ```

7. putenv和setenv的差异：很多实现中，putenv直接将string放入到环境表中，而string一般作为局部变量，期待putenv自己分配空间，否则函数返回后，栈上的空间就被释放了。setenv会自己分配空间来用name和value来构造环境字符串，不会出现上述情况。

8. 只能修改当前进程和子进程的环境变量，不能修改父进程的。

9. 可以看到环境表和所有环境字符串最初是存储在栈的上面。几种可能的修改：

    1. 如果删除一个环境变量，则只需在环境表中找到该指针，将后续指针都向前移动一个位置，然后将最后空出来的位置的指针置为NULL即可。

    2. 如果要增加或者修改一个环境变量，要复杂的多，因为在进程空间中，它上面是内核区域，下面是栈区域，夹在二者中间，使得环境表和环境字符串都不能原地扩展。

    3. 如果setenv修改已存在的环境变量，字符串变短的话，可以直接就地修改，如果是变长的话，则需要用malloc堆上申请一块空间用于存放新的字符串，然后将新字符串复制过去，并修改环境表中对应的指针指向新分配的内存地址。

    4. 如果新添加环境变量，首先应该malloc一个空间用来存储新的环境字符串。
        1. 如果是第一次增加环境变量，则需要malloc一块空间用来存储新的环境表。然后将旧的环境表复制过来，并将新增的环境变量地址添加到新环境表的末尾，然后在环境表的末尾添加一个NULL。最后将environ指向新的环境表。虽然新的环境表移动到了堆中，但是大多数的环境字符串还是存储在原来的栈顶以上。

        2. 如果不是第一次增加环境变量，则只需realloc原先malloc的地址块，增加一个指针的空间即可。将新的环境字符串地址添加到环境表的尾部，然后添加一个NULL。



## 内存空间分配

1. 一个C程序在内存中通常由以下几部分构成：

    1. 代码段，也称为正文段，存储着可执行的指令，通常是共享，只读的。

    2. 初始化数据段，也称为数据段，包含了程序中需明确赋予初值的变量，例如函数之外的声明：int a = 9。需要在可执行文件中占据同样大小的空间，因此载入可执行文件时，直接复制过去即可。

    3. 未初始化数据段，也成为bss段，名称来源于早期汇编程序的一个操作符，意思是由符号开始的块(block started by symbol)。在程序开始执行前，内核将此段中的数据初始化为0或空指针。例如函数外的声明：int sum[3]。不在可执行文件中占据同样大小的空间，只需一个标记即可，因为它的值都是0。

    4. 栈，自动变量以及每次函数调用时所需要保存的信息（返回地址，要保存的某些寄存器的值，要传递的参数）都存放在此段中，递归函数在栈上会产生多个栈帧，这样他们之间互不影响。

    5. 堆，动态内存分配的区域。位于未初始化数据段和栈之间。

2. 一个C程序可执行文件中，不包含栈和堆这2个段，但是还包含符号表的段，调试信息段，共享库信息段等。不过后面这些段都不会载入内存。size命令可以查看一个可执行文件中各个段的大小：

    ```shell
    zj@hit:~/linux_c/process$ size test #
       text    data     bss     dec     hex filename
       1579     616       8    2203     89b test
    ```

3. Intel x86处理器下的Linux内存布局如下图，进程的虚拟空间是4G，0x08048000到0xc0000000(3G)是给用户使用的，3G-4G的部分是给内核使用的。64位环境下，进程的虚拟空间是128T。正文段从0x08048000开始。栈底则在0xc0000000之下开始。这种结构中，栈由高地址向低地址增长。

4. <img src="Linux系统编程.assets/image-20210506184423249.png" alt="image-20210506184423249" style="zoom:80%;" />

5. 栈不一定要向低地址生长，某些硬件并没有对栈提供特殊的支持，此时C实现可能要用链表来实现栈帧。

6. 使用pmap命令查看进程的地址空间：

   ```shell
   [zj@ZJ test]$ pmap 1550   #查看进程号为1550的进程地址空间
   1550:   -bash
   0000559894e73000   1056K r-x-- bash
   000055989517a000     16K r---- bash
   000055989517e000     36K rw--- bash
   0000559895187000     40K rw---   [ anon ]  #动态分配的空间
   ...
   00007ffe3412e000    132K rw---   [ stack ] #栈
   00007ffe34183000     12K r----   [ anon ]
   00007ffe34186000      8K r-x--   [ anon ]
   ffffffffff600000      4K r-x--   [ anon ]
    total           235468K
   ```
   
7. 例子，各种变量的存储空间占用：

   ```c
   #include <stdio.h>
   static int g1;
   static int g2 = 0;
   static int g3 = 3;
   int g4;
   int g5 = 0;
   int g6 = 8;
   int main() {
       static int s1;
       static int s2 = 0;
       static int s3 = 3;
       int s4;
       int s5 = 0;
       int s6 = 8;
       printf("g1: %p,g2: %p,g3: %p,g4: %p,g5: %p,g6: %p\n", &g1, &g2, &g3, &g4, &g5, &g6);
       printf("s1: %p,s2: %p,s3: %p,s4: %p,s5: %p,s6: %p\n", &s1, &s2, &s3, &s4, &s5, &s6);
       getchar();
   }
   //gcc test.c -o test -m32 。输出结果为：
   zj@hit:~/linux_c/process$ ./test 
   g1: 0x565a3020,g2: 0x565a3024,g3: 0x565a3008,g4: 0x565a3018,g5: 0x565a301c,g6: 0x565a300c
   s1: 0x565a3028,s2: 0x565a302c,s3: 0x565a3010,s4: 0xffec9810,s5: 0xffec9814,s6: 0xffec9818
   
   //pmap的结果为：
   zj@hit:~/linux_c$ pmap 4658
   4658:   ./test
   000000005659f000      4K r---- test  //由于是32位程序，所以高32位地址全部为0。
   00000000565a0000      4K r-x-- test
   00000000565a1000      4K r---- test
   00000000565a2000      4K r---- test
   00000000565a3000      4K rw--- test  //g1-g6,s1-s3都在这里。因为4K=0x1000=2^12，这段的末尾地址为565a4000。这些变量有的位于初始化数据段，有的位于未初始化数据段中，但是他们都被映射到了同一个内存页中。
   00000000565cd000    136K rw---   [ anon ]
   00000000f7ce4000    128K r---- libc.so.6
   00000000f7d04000   1528K r-x-- libc.so.6
   00000000f7e82000    532K r---- libc.so.6
   00000000f7f07000      4K ----- libc.so.6
   00000000f7f08000      8K r---- libc.so.6
   00000000f7f0a000      4K rw--- libc.so.6
   00000000f7f0b000     40K rw---   [ anon ]
   00000000f7f1c000      8K rw---   [ anon ]
   00000000f7f1e000     16K r----   [ anon ]
   00000000f7f22000      8K r-x--   [ anon ]
   00000000f7f24000      4K r---- ld-linux.so.2
   00000000f7f25000    148K r-x-- ld-linux.so.2
   00000000f7f4a000     60K r---- ld-linux.so.2
   00000000f7f59000      8K r---- ld-linux.so.2
   00000000f7f5b000      4K rw--- ld-linux.so.2
   00000000ffeab000    132K rw---   [ stack ]  // s4,s5,s6都在这里
    total             2788K
   //size的结果：
   zj@hit:~/linux_c$ size process/test
      text    data     bss     dec     hex filename
      1693     324      28    2045     7fd process/test
   ```

8. ISO C提供了3个用于动态内存分配的函数，都应使用free来释放。这三个函数返回的指针一定是适当对齐，使其可以用于存储任何数据对象。例如某些系统中要求double型变量的内存地址必须为8的倍数，此时这三个函数的返回值一定也是8的倍数。

   ```c
   #include <stdlib.h>
   void *malloc(size_t size); //分配无符号数size个字节的内存空间，其中的初始值不确定。
   void *calloc(size_t nmemb, size_t size); //为size个长度为nmemb的对象分配空间，总大小为size*nmemb个字节。其中的每个字节都被初始化为0。
   void *realloc(void *ptr, size_t size);//增加或减少以前分配的内存区域ptr的长度，使之新长度为size。当增加长度时，有可能原有的位置不够，会重新分配一块更大的内存，然后将原来的内容复制过来，并释放ptr所指的空间，新增的部分的初始值不确定。应该总是使用返回值，而不是ptr的值作为新的区域的指针。如果某些指针的值正好落在该区域内，可能在realloc后，该指针就会变为无效。
   //realloc(NULL, size); 等价于 malloc(size);
   ```

9. 这三个函数底层通过sbrk系统调用来实现。该系统调用用来扩充或缩小进程的堆。大多数free的实现中，释放的空间并不会用sbrk归还给内核，而是保留在malloc内存池中以便下一次分配时更加快速，不用调用sbrk。大多数实现中，malloc分配一块内存，实际占用的大小要不参数大，因为还要存储一些管理信息，例如分配块的长度，下一个分配块的指针。这样free的时候就只用给出地址块的起始地址即可。

   ```c
   #include <unistd.h>
   int brk(void *addr); //
   void *sbrk(intptr_t increment); //
   ```

10. 在动态分配的空间中写越界，可能会修改掉块大小记录，或其他块的内容。

11. 内存泄漏越多，可用的内存空间就越少，换页行为就越频繁，性能下降越大。

12. 一些系统中支持程序使用自定义的动态内存分配和释放函数（链接时指定即可），进行附加检错。替代的库有：libmalloc，alloca(在栈上分配，这样在函数返回时，就会自动释放)，TCMalloc，jemalloc（FreeBSD8.0中默认的）等。

## 装载库

1. 动态库和静态库都是在编译时确定库的名称的，而装载库时运行时才知道要库的名称。

2. 一些无关紧要的库或插件在程序启动时如果装载失败，会先跳过，可以后续让用户手动启动。

3. 手工装载库依赖的函数：

   ```c
   #include <dlfcn.h>        //使用的时候要加上链接选项 -ldl
   void *dlopen(const char *filename, int flags);  //打开filename这个库，flags为打开方式。返回的是一个handle。filename可以是绝对或相对路径，也可以在默认路径(例如/usr/lib等)下搜寻的文件。
   int dlclose(void *handle);  //关闭这个库
   void *dlsym(void *handle, const char *symbol);   //在一个成功打开的库handle中寻找某个symbol的地址。
   char *dlerror(void); //当dlopen族的函数出错时，通过该函数可以获取到一个出错信息。如果没出错，则返回NULL。
   ```

4. 例子，手工装载math库，执行cos函数：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <dlfcn.h>
   #include <gnu/lib-names.h>  /* Defines LIBM_SO (which will be a string such as "libm.so.6") */
   int main(void){
       void *handle;
       double (*cosine)(double); //定义一个函数指针
       char *error;
   
       handle = dlopen(LIBM_SO, RTLD_LAZY);   //RTLD_LAZY,延迟绑定，即等到使用时再装载。
       if (!handle) {
           fprintf(stderr, "%s\n", dlerror());
           exit(EXIT_FAILURE);
       }
       dlerror();    /* Clear any existing error */
       cosine = (double (*)(double)) dlsym(handle, "cos");
       // *(void **) (&cosine) = dlsym(handle, "cos"); 强转换换完就成void*赋值给void*了。由于C99标准唯独没有对void*转化为函数指针的情况进行定义，所以不能直接赋值，早期就使用这种方法，而POSIX.1-2013中对这一情况进行统一规定，因此可以使用上面的简化写法，进行强制转化了。
       error = dlerror();
       if (error != NULL) {
           fprintf(stderr, "%s\n", error);
           exit(EXIT_FAILURE);
       }
       printf("%f\n", (*cosine)(2.0));   //使用函数指针来调用对应的函数时，要加上*。
       dlclose(handle);
       exit(EXIT_SUCCESS);
   }
   ```


## setjmp longjmp

1. C语言中goto关键字不能够跨函数跳转，看上去执行路径跳转过去了，但是没有对栈进行恢复。当出现函数的嵌套调用时，例如main→A→B→C，此时如果C函数中出现了非致命错误，需要重新开始新一轮的A→B→C的调用。此时最快的方法就是从C函数直接跳转到main函数，就需要setjmp和longjmp这两个函数，否则就需要在B和A函数中进行返回值判断，决定上一次调用是否正确，特别麻烦。

   ```c
   C(){
       
   }
   B(){
       C();
   }
   A(){
   	B();
   }
   int main(){
       char line[1024];
       while(fgets(line,1024,stdin)){ //不断地从中断获取输入，然后调用A来处理。如果在调用链A→B→C中的某一个出问题时，最好直接返回到这里，报错，然后开始下一次的循环。
           A();
       }
   }
   ```

2. 这两个函数对于处理发生在深层嵌套调用中的出错情况非常有用。他们被称为非局部goto，会在栈上跳过若干调用帧，返回到当前调用路径上的某个函数中。相当于这些栈帧被丢弃了。

3. 例如在进行递归查找的时候，如果查找到了某个内容，就可以通过跨函数跳转立刻返回到最高层。还有就是在内层函数中抛出异常，则也会用到跨函数跳转到异常处理程序。

   ```c
   #include <setjmp.h>
   int setjmp(jmp_buf env);   //设置跳转点，env存放着用来恢复栈状态的所有信息，同时也标识该跳转点的，longjmp的第一个参数要用到，因此一般定义为（静态）全局变量。直接执行来设置跳转点时，返回0; 从longjmp跳转回来时，返回值为longjmp的第二个参数。这种行为类似于fork，一次调用，两次返回，不过还是单一进程。
   void longjmp(jmp_buf env, int val);  //进行长跳转，跳转到使用setjmp设置env的地方，并带回非零值val。如果val被设置为了0，则会被修改为1。之所以有val，是因为一个setjmp可以对应于多个longjmp，val用来区分它们。该函数永远不会返回。
   ```

4. 一般来说，env中存放着栈指针，指令指针，一些其他寄存器的值和信号屏蔽字。

5. 例子：执行到C函数时，立刻返回到A函数的setjmp中继续执行，跳过从C函数返回到B函数和从B函数返回到A函数的过程。然后因为在第5行中ret不等于0，所以程序会执行else分支，然后从A正常结束。

   ```c
   #include <stdio.h>
   #include <unistd.h>
   #include <stdlib.h>
   #include <setjmp.h>
   static jmp_buf jmp_save;  //使用静态全局变量在不同函数共享变量。
   void C() {
       printf("C() Begin\n");
       if (1) {
           longjmp(jmp_save, 3);  //直接回到第32行的位置，返回值为3。
       }
       printf("C() End\n"); //不会被调用
   }
   void B() {
       printf("B() Begin\n");
       if (0) {
           longjmp(jmp_save, 2);
       }
       C();
       printf("B() End\n"); //不会被调用
   }
   void A() {
       printf("A() Begin\n");
       if (0) {
           longjmp(jmp_save, 1);
       }
       B();
       printf("A() End\n"); //不会被调用
   }
   int main() {
       char line[1024];
       int ret;
       ret = setjmp(jmp_save); //第一次为主动调用ret=0，后续为longjmp调用。
       if (ret == 0) {
           while (fgets(line, 1024, stdin)) { //不断地从中断获取输入，然后调用A来处理。如果在调用链A→B→C中的某一个出问题时，最好直接返回到这里，报错，然后开始下一次的循环。
               A();
           }
       } else {
           switch (ret) {  //出错分类
           case 1:
               printf("longjmp back from A()\n");
               break;
           case 2:
               printf("longjmp back from B()\n");
               break;
           case 3:
               printf("longjmp back from C()\n");
               break;
           default:
               printf("Error!");
               break;
           }
       }
   }
   //运行程序，输出为：
   zj@hit:~/linux_c/process$ ./test 
   A() Begin
   B() Begin
   C() Begin
   longjmp back from C()
   ```

6. 之所以可以进行长跳转或goto这些操作，是因为C语言可以通过内嵌汇编来打破自己构建的栈帧，直接操作栈内存结构。

7. longjmp会丢弃部分栈帧，将执行序列回到setjmp的位置。但是对于自动变量和寄存器变量并不保证恢复到第一次调用setjmp时的状态。

8. 例子：自动变量，寄存器变量，易失变量，局部静态变量，（静态）全局变量在longjmp后的变化。 

    ```c
    #include <stdio.h>
    #include <unistd.h>
    #include <stdlib.h>
    #include <setjmp.h>
    static jmp_buf jmpbuffer;
    static int globval;  //全局变量
    static void f2(void){
        longjmp(jmpbuffer,1);
    }
    static void f1(int i, int j, int k, int l){
        printf("in f1():\n");
        printf("globval = %d, autoval = %d, regival = %d, vloaval = %d, statval = %d\n", globval, i, j, k, l);
        f2();
    }
    int main(){
        globval = 1;
        int autoval = 2;
        register int regival = 3;
        volatile int volaval = 4;
        static int statval = 5;
        if(setjmp(jmpbuffer)!=0){ //longjmp之后
            printf("after longjmp:\n");
            printf("globval = %d, autoval = %d, regival = %d, vloaval = %d, statval = %d\n",globval,autoval,regival,vloaval,statval);
            exit(0);
        }
        //setjmp之后，longjmp之前
        globval = 95;
        autoval = 96;
        regival = 97;
        volaval = 98;
        statval = 99;
        f1(globval,autoval,regival,vloaval,statval);
    	exit(0);
    }
    //如果不进行优化的编译gcc test.c -o test，执行结果为：
    in f1():
    globval = 95, autoval = 96, regival = 97, vloaval = 98, statval = 99
    after longjmp:
    globval = 95, autoval = 96, regival = 3, vloaval = 98, statval = 99
    //如果进行优化的编译gcc test.c -O -o test，执行结果为：
    in f1():
    globval = 95, autoval = 96, regival = 97, vloaval = 98, statval = 99
    after longjmp:
    globval = 95, autoval = 2, regival = 3, vloaval = 98, statval = 99
    ```

9. setjmp规定了存储在存储器上的变量将具有longjmp时的值，即不会恢复。而CPU寄存器中的变量将会恢复为setjmp时的值。一般来说全局变量，静态变量，易失变量总是放在存储器上。有些编译器不优化的话，寄存器变量会存储在寄存器上，而自动变量存储在内存中，优化时，自动变量会存储在寄存器中。

## 资源获取和控制

1. 每个进程都有一组资源限制，资源获取和控制函数如下：

   ```c
   #include <sys/time.h>
   #include <sys/resource.h>
   int getrlimit(int resource, struct rlimit *rlim); //获取resource资源限制，将结果存储到rlim中。resource是众多宏中的一个，例如RLIMIT_STACK，和ulimit中显示的对应。
   int setrlimit(int resource, const struct rlimit *rlim); //使用rlim设置当前resource的limit。
   struct rlimit {
       rlim_t rlim_cur;  //软限制，必须要小于等于硬限制。rlim_t是对unsigned long的封装。
       rlim_t rlim_max;  //硬限制。用RLIM_INFINITY来表示unlimited。
   };
   ```

2. 进程的资源限制通常在系统初始化时，由0号进程建立，然后由后续进程继承或修改。

3. 子进程会继承其父进程的资源限制。为了影响一个用户的所有后续进程，需要将资源限制的设置构造在shell中，例如ulimit。类似的umask，chdir也必须是shell内置的。因为修改的是当前进程，而非新产生的子进程。

4. 更改资源限制需要满足三点：

   1. 任何进程都可以将软限制修改为<或等于硬限制。
   2. 任何进程都可以降低硬限制，但必须>或=其软限制。这种降低对于普通用户是不可逆的。
   3. 只有超级用户进程可以提高硬限制。

5. 常见的资源：

   ```shell
   RLIMIT_AS     #进程总的可用存储空间的最大长度(字节)，这影响sbrk和mmap函数。
   RLIMIT_CORE   #core文件的最大字节数，若为0，则组织创建core文件。
   RLIMIT_CPU    #进程可用CPU时间的最大值，若超过此限制，该进程会收到SIGXCPU信号
   RLIMIT_DATA   #数据段的最大长度(字节)。进程的内存空间中初始化数据段，未初始化的数据段，堆的总和。
   RLIMIT_FSIZE  #可以创建的文件的最大长度(字节)，若超过此限制，该进程会收到SIGXFSZ信号。
   RLIMIT_MEMLOCK #使用mlock能够锁定在内存中的最大长度(字节)。
   RLIMIT_MSGQUEUE #进程为POSIX消息队列可分配的最大存储字节数。
   RLIMIT_NICE  #进程的调度优先级(友好值)，可以设置的最大值。
   RLIMIT_NOFILE  #进程能打开的文件数量上限，更改此限制将影响sysconf(_SC_OPEN_MAX)返回的值。
   RLIMIT_NPROC   #每个实际用户ID可拥有的最大子进程数量，更改此限制将影响sysconf(_SC_CHILD_MAX)返回的值。
   RLIMIT_NPTS   #用户可同时打开的伪终端数。
   RLIMIT_RSS    #进程最大驻留内存集长度(字节)，如果可用的内存非常少，则内核将从进程回收超过RSS的部分，发生内存交换。
   RLIMIT_SBSIZE #任意时刻，用户可以占用的套接字缓冲区(socket buffer)的最大长度(字节)
   RLIMIT_SIGPENDING #一个进程可以排队的信号最大数量。具体由sigqueue来实现这个限制。
   RLIMIT_STACK  #栈的最大长度(字节)
   RLIMIT_SWAP   #用户可使用的交换空间的最大长度(字节)
   RLIMIT_VMEM   #和RLIMIT_AS相同。
   ```

# 进程

1. 每个进程都有一个非负整数表示的唯一进程ID。它在整个系统中不重复。有些程序使用进程ID作为名字的一部分来创建一个唯一的文件。例如coredump文件。进程ID是可以被复用的。当进程终止后，它的ID会被回收，其他进程可以用。大多数Unix采用的是延迟分配的算法，并不会刚回收的进程ID分配出去。这样是为了防止被认错为同ID的旧进程。

2. ID为0的进程通常是调度进程，也被称为交换进程(swapper)，它是内核的一部分，但是并不执行磁盘上的任何程序。

3. ID为1的进程为init进程。在自举结束后，由内核调用，文件为/sbin/init。该进程会读取系统初始化文件，例如/etc/rc*，/etc/inittab以及/etc/init.d中的文件，并将系统引导到一个适合用户使用的状态。init进程不会终止，它不是内核的一部分，只是一个普通的用户进程，但是以超级用户特权运行。

4. few代指fork，exec，wait三个函数。

5. 进程标识符的类型为pid_t，一般为有符号的16位整型数，因此，最多同时运行32767个进程（从1开始计数）。ulimit中没有规定进程的最多个数。进程号的使用顺次循环使用，不会插空。

   ```c
   #include <sys/types.h>
   #include <unistd.h>
   pid_t getpid(void);    //获取当前进程的PID
   pid_t getppid(void);   //获取父进程的PID
   ```


## fork

1. 进程的产生：

   ```c
   #include <sys/types.h>
   #include <unistd.h>
   pid_t fork(void);  //通过复制当前进程的方式来创建一个新的子进程，该函数和setjmp类似，都是执行一次，返回两次，区别是setjmp是从同一个进程的不同函数返回，fork是从不同进程的同名函数返回。如果执行成功，父进程中返回子进程的PID，子进程返回0。如果失败，父进程返回-1。
   //失败的情况一般为该RUID的进程总数超过了资源限制。
   ```

2. 将子进程的ID通过fork返回给父进程的原因是一个进程的子进程可以有多个，并且没有一个函数可以使一个进程获得它所有子进程的ID。之所以给子进程返回0，是因为子进程只有一个父进程，总可以用getppid获得其父进程的ID。

3. 创建子进程一般有两个目的：

   1. 复制一个自己，例如网络服务程序，每当接收到一个请求时，就会复制一个自己去响应请求，而自己继续监听请求。

   2. 执行新的程序，例如shell。

4. 通过fork出来的进程和当前进程一模一样（相当于memcpy），都是执行到fork这一行。区别只有以下几点：

   1. 父子进程fork函数的返回值不同，由此可以进行父子进程的区分。
   2. 父子进程的PID和PPID都不同，子进程的PPID就是父进程的PID。
   3. 子进程不继承父进程的内存锁。
   4. 子进程的未决（还未来得及响应的）信号集被初始化为空。
   5. 子进程不继承父进程设置的文件锁。
   6. 子进程不继承父进程的信号量调整。
   7. 子进程不继承父进程的计时器（闹钟）。
   8. 子进程不继承父进程的的资源利用量。
   9. CPU计时器清零。tms_utime（进程的用户态执行时间），tms_stime（进程的内核态执行时间），tms_cutime（子进程的用户态执行时间），tms_cstime（子进程的内核态执行时间）的值设置为0，这四个字段为struct tms的成员，通过times函数获取。

5. 父子进程共享的内容：

    1. EUID（有效用户ID），EGID（有效组ID），RUID（真实用户ID），RGID（真实组ID）。

    2. 附属组ID

    3. PGID（进程组ID）

    4. SID（会话ID）

    5. 控制终端

    6. SUID（设置用户ID）和SGID（设置组ID）标志

    7. 当前工作目录

    8. 根目录

    9. 文件模式创建屏蔽字，即umask

    10. 信号屏蔽字

    11. 对任一打开文件描述符的close-on-exec（exec时关闭）标志。

    12. 环境变量

    13. 连接的共享存储段

    14. 内存空间

    15. 资源限制

6. 早期的fork会完全复制一份内存，费时又占用内存，因此有了vfork来使得子进程和父进程共享内存。但是现在新版的fork使用了写时复制（copy-on-write）技术，即fork后的进程的内存并不会完全复制一份，而是和父进程共用，如果某个进程要修改对应的内存空间，才会自己复制出来一份（要修改的内容所在的页）用于修改。谁修改，谁来拷贝。这个功能需要虚拟内存的支持。

7. 因为某些情况下，fork后会很快调用exec，这将导致fork中复制的内容被扔掉，造成时间的浪费，因此产生了vfork，它用于创建一个新的进程，而该进程的目的就是为了执行一个新程序。shell就是典型。vfork并不将父进程的地址空间完全复制到子进程中。不过在调用exec之前，子进程会在父进程的地址空间运行，即此时子进程对变量的修改会影响到父进程。vfork的另一个特点是，它保证子进程先运行，在它调用exec或exit之后，父进程才可能会被调度。

8. Linux支持一种新的进程创建函数clone，它是fork的增强版，允许调用者控制父进程的哪部分和子进程共享。

9. 某些系统为fork+exec提供了一个合并系统调用spawn，分开的好处是可以在fork后，exec前进行一些I/O重定向，用户ID，信号安排的工作。

10. init进程是所有进程的祖先进程，PID=1。

11. 产生子进程后，由调度器决定哪个进程先运行，不一定哪个先运行。

12. 例子：

     ```c
     #include <stdio.h>
     #include <stdlib.h>
     #include <unistd.h>
     int main(){
         pid_t pid1;
         printf("[%d]:Begin\n",getpid());
     //  fflush(NULL);    //刷新所有的流，清空缓冲区。
         if((pid1 = fork()) < 0){
             perror("fork()");
             exit(1);
         }
         if(pid1 == 0 ){
             printf("[%d]:Child Process\n",getpid());  //子进程中会执行该句
         }else{
             printf("[%d]:Parent Process\n",getpid()); //父进程中会执行该句
         }
         printf("[%d]:End\n",getpid());                //父子进程都会执行该句
     }
     ```

13. 上述代码运行结果如下：

     ```shell
     [zj@ZJ test]$ ./test   #终端是行缓冲设备，上面的每行后面都有一个\n，所以会无延迟地输出。
     [1841]:Begin
     [1841]:Parent Process
     [1841]:End
     [1842]:Child Process
     [1842]:End
     #有时候会出现程序结束时，命令行的提示符看不到了，实际上是命令行的提示符提前输出了，即shell在父进程结束后就立即输出了提示符，而后续子进程又输出了一些内容，所以就把设立了的命令提示符挡住了。shell只会等待自己的子进程，但是不会等待子进程的子进程。
     [zj@ZJ test]$ ./test >/tmp/out   #文件是全缓冲设备，遇到\n不刷新，必须手动fflush。否则会到进程结束时刷新。因此在fork的时候，父进程输出缓冲区内的begin字符串也被复制过来了。因此在fork之前要加上fflush(NULL)，刷新所有的流。
     [zj@ZJ test]$ cat a
     [1843]:Begin
     [1843]:Parent Process
     [1843]:End
     [1843]:Begin  #还是父进程填入的自己的PID
     [1844]:Child Process
     [1844]:End
     ```

14. 子进程会复制父进程的所有打开的文件描述符，好像执行了dup函数。子进程和父进程的每个相同的文件描述符共享同一个文件表项。因此共享同一个文件的偏移量，这样二者对同一个文件的读写同步。

15. <img src="assets/image-20230515221900109.png" alt="image-20230515221900109" style="zoom: 67%;" />

16. 如果父进程在创建子进程后什么也不做，只是等待子进程完成。则fork前后无需对文件描述符做任何特殊操作。因为父子进程对文件的操作不会交叉。不会发生竞争的现象。

17. 如果父子进程在fork后各自执行不同的代码段，那么fork之前，父子进程都应该关闭他们不需要的文件描述符，这样不会互相干扰。

18. pstree -p 查看进程树关系。

19. ![image-20210507111305440](Linux系统编程.assets/image-20210507111305440.png)

20. 循环创建子进程需要注意的问题：

     ```c
     #include <stdio.h>
     #include <stdlib.h>
     #include <unistd.h>
     int main(){
         pid_t pid;
         for (int i=0;i<3;i++){
             fflush(NULL);
             pid = fork();
             if (pid<0){
                 perror("fork()");
                 exit(1);
             }
             if(pid ==0){  //子进程分支
                 printf("child:[%d]\n",getpid());
                 //sleep(1000);
                 exit(0); //在循环内部fork时，子进程必须要有exit，否则子进程也会继续循环，进而fork孙子进程。1→1+2→ 1+3 2+4→ 1+5 3+6 2+7 4+8
             }
         }
         //sleep(1000);
         exit(0);
     }
     ```

21. 上面程序中的两处sleep分别起作用时会出现如下状况：

     1. 仅15行起作用时，每个子进程都休眠1000s，因此父进程很快创建完所有的子进程后会先结束。此时子进程的状态都为S，可中断的睡眠态。且他们的父进程都会变成init。因为父进程消亡后，子进程并不会被爷爷进程接管，而是直接被init接管。init也要等到这些由它接管的进程sleep都结束了才可以为其收尸，因为无法为正在运行的程序收尸。
     2. 仅19行起作用时，父进程休眠1000s，因此子进程会先结束。此时子进程的状态都为Z，僵尸态。等待父进程给他们收尸。而本程序中，父进程也没有为子进程收尸的语句，因此子进程会先变成孤儿，然后再被init收尸。

22. 僵尸进程偶尔出现，一闪即过，可能是他的父进程正在忙，暂时没有时间收尸。一个僵尸进程只占用一个结构体，其中包含了它的退出状态，且最宝贵的资源是PID。

23. 通过fork产生的子进程共享父进程的终端信息，因此也会将其标准输入，输出和错误关联到同一个终端上。父进程可以先打开一个文件，然后fork，这样子进程也可以通过读写这个文件来和父进程交互。

24. 任何一个进程终止时，内核会逐个检查所有活动进程，以判断它是否是正要终止进程的子进程，如果是则该进程的父进程会被修改为1，这样确保了每个进程都有父进程。

25. 内核为每个终止的进程保留了一定量的信息，因此其父进程调用wait或waitpid时，可以得到子进程的终止状态。这些信息至少包括：子进程的进程ID，终止状态，使用的CPU时间统计。

26. 内核可以释放终止进程所使用的内存，关闭其打开的文件。

27. 如果一个要长期运行的进程，fork了很多子进程，但是都没为子进程收尸，就会产生很多僵尸进程。

28. init进程被设计为负责任的，他会在它的每个子进程终止后，调用wait获得其终止状态，这样就可以防止系统中产生大量的僵尸进程。


## wait

1. 当一个进程正常或异常终止，内核就向其父进程发送SIGCHILD信号，像子进程终止这种异步事件使用信号非常方便。对于这个信号，父进程可以选择忽略（默认），也可以为其注册一个信号处理程序。

2. 当一个父进程调用wait时：

    1. 如果其所有子进程都还在运行，则父进程阻塞。

    2. 如果一个子进程已经终止，正在等待父进程获取终止状态，则父进程取得该子进程的终止状态后立即返回。

    3. 如果它没有任何子进程，则立即出错返回。因为任何时刻，wait系列函数都只能为其子进程收尸。

3. wait的调用可以是在任意时间点调用（此时可能会阻塞），也可以是在SIGCHILD的信号处理函数中调用（此时会立即返回）。

4. wait系列函数是等待子进程的状态发生改变（正常终止，被信号终止，被信号恢复），对于正常终止的进程，wait程序会释放和它相关的资源，否则进程会变为僵尸态。

5. wait无法指定为哪个子进程收尸，哪个先结束就先为哪个收尸。对于wait来说，父进程会阻塞，等待一个信号通知它子进程的状态改变了。但是如果子进程出问题了，父进程可能永远无法被唤醒。waitpid除了可以指定为哪个子进程收尸之外，还支持一些选项，例如NOHANG(非阻塞)，如果没有子进程处于待收尸状态，父进程不会等待，而是立即返回0，如果有子进程处于待收尸状态，父进程会为其收尸，并立即返回。

6. 在shell中运行程序，有时候shell提示符会先跳出来，后面还会打印别的内容，这种情况一般为，运行的程序比它的子进程先结束了，同时没有wait子进程。如果在父进程的结束前加上wait函数，父进程就会阻塞，直到所有的子进程都结束，父进程为子进程收尸。然后父进程结束，shell为父进程收尸，最后shell显示出命令提示符。

7. ```c
   #include <sys/types.h>
   #include <sys/wait.h>
   pid_t wait(int *wstatus);  //等待进程状态发生变化，将进程的终止状态(不是exit的退出码)保存在参数wstatus中（如果不关心，可以用NULL）。如果成功，返回终止的子进程的PID。失败返回-1。 该函数时一直等待，直到进程状态变化，阻塞式的。
   pid_t waitpid(pid_t pid, int *wstatus, int options);//可以指定要为其收尸的pid，option如果为WNOHANG，则将该阻塞操作变为非阻塞的。
   //wstatus是可以看做是一个位图，可以用以下宏来检测对应的位：
   WIFEXITED(wstatus);    //该宏是用来检测进程的退出状态是否是正常退出(调用exit(), _exit()或从main函数return)。正常退出时可以执行WEXITSTATUS(wstatus);来获取退出码(exit的参数或return的值)。
   WIFSIGNALED(wstatus);  //检查进程是否是由信号终止的。如果为真则可以通过WTERMSIG(wstatus);来获取信号值。如果为真有些实现还可以用WCOREDUMP(wstatus);来检查是否产生coredump文件。
   //当一个进程被停止或由停止继续执行时，也会发生状态变化，此时也可以由wait获取到：
   
   ```

8. waitpid中的第一个参数可以有以下几种情况：

   1. = -1，等待任何一个子进程，此时和wait等价。
   2. < -1，子进程.PGID == |参数|
   3. ==  0，子进程.PGID == 调用进程.PGID。
   4. \>  0，PID等于该值的子进程才会被等待。

9. wait函数在进程没有子进程或者被信号打断时，都会出错。waitpid中如果指定的PID或PGID都不存在，或pid指定的进程不是调用进程的子进程，也会出错。

10. 进程也可以分组，便于统一管理，默认子进程是和创建它的父进程一组的。wait等价于waitpid(-1,&status,0)。

11. ```c
     #include <stdio.h>
     #include <stdlib.h>
     #include <unistd.h>
     #include <sys/types.h>
     #include <sys/wait.h>
     int main() {
         pid_t pid;
         int status;
         for (int i = 0;i < 3;i++) {
             fflush(NULL);
             pid = fork();
             if (pid < 0) {  //只有父进程有可能到达这里
                 perror("fork()");
                 for (int j = 0; j < i; j++) { //这里没有直接exit,是考虑到前2个进程创建成功，但第3个不成功的情况，这个循环wait给前两个子进程收尸。如果不写循环，直接exit父进程的话，子进程会变成孤儿进程，然后被init接管，不推荐这样做。
                     wait(NULL);
                 }
             }
             if (pid == 0) { //子进程
                 printf("child:[%d]\n", getpid());
                 exit(i);
             }
         }
         for (int i = 0;i < 3;i++) {
             pid = wait(&status);
             printf("child-terminated,pid:[%d],status:[%d],returncode:[%d]\n", \
                 pid, status, WEXITSTATUS(status));
         }
         exit(0);
     }
    ```

12. 上述程序执行的结果可能为：

     ```shell
     [zj@ZJ test]$ ./test
     child:[1896]
     child:[1898]     #子进程之间，子进程和父进程之间谁会先执行，完全取决于调度器。
     child:[1897]
     child-terminated,pid:[1897],status:[256],returncode:[1]
     child-terminated,pid:[1898],status:[512],returncode:[2]
     child-terminated,pid:[1896],status:[0],returncode:[0]
     #另一种执行情况
     child:[1945]
     child-terminated,pid:[1945],status:[0],returncode:[0]
     child:[1947]
     child-terminated,pid:[1947],status:[512],returncode:[2]
     child:[1946]
     child-terminated,pid:[1946],status:[256],returncode:[1]
     ```

13. 如果有一个父进程不想wait其子进程，也不想让子进程变成僵尸一直等待父进程终止，然后被init接管并收尸。这个目的可以用两次fork实现：

     ```c
     #include <stdio.h>
     #include <stdlib.h>
     #include <sys/wait.h>
     #include <unistd.h>
     int main() {
         pid_t pid;
         if ((pid = fork()) < 0) { //主进程首先fork了一次，然后就去21行wait自己的子进程了。
             perror("first fork()");
             exit(1);
         } else if (pid == 0) { 
             if ((pid = fork()) < 0) {//子进程又fork了一次
                 perror("second fork()");
                 exit(1);
             } else if (pid > 0) { //主进程的子进程推出了，这样21行就能返回。
                 exit(0);
             }
             sleep(2);//这里是主进程的孙子进程，它的父进程消亡了，因此它被init接管。
             printf("second child, parent pid = %ld\n", (long)getppid());//上面之所以要让孙子进程睡眠2秒，是为了让printf执行时，其父进程结束，这样此时getppid的结果就一定是1。
             exit(0);
         }
         if (waitpid(pid, NULL, 0) != pid) {
             perror("waitpid");
             exit(1);
         }
         exit(0);
     }
     //这里进程A fork一次，产生了进程A和B，然后进程B再fork一次，产生了B和C，此时进程B exit了，进程A也wait进程B，这样进程B就完美退出了，此时就只剩进程C了，他被init接管了。
     //这个方法可以最终产生一个被init接管的进程，对进程A来说，不用阻塞很久，好像啥也没发生一样，进程C跟它始终没啥关系。
     ```

14. 如果有一系列类似任务要分配给多个进程，不推荐一个任务分配给一个进程，

     1. 有些任务适合于均匀分配给多个进程；有分块和交叉分配两种算法，例如1-100分给三个进程：
        1. 分块，1-33分给1，34-67分给2，67-100分给3。
        2. 交叉分配，1，4，...分给1，2，5，...分给2，3，6，...分给3。一般情况下优先选择交叉分配，也有例外，例如查找质数的任务，交叉分配可能导致某个进程始终分配到的数都是某个很小的数的倍数，因而该进程很快就完成了任务。
     2. 有些任务需要非均匀的分配，各个进程才能一样忙。例如查找质数的任务，由于质数的分布密度不均匀，在较小的数附近分布较密。
     3. 池类算法：可以创建一个任务池，进程逐个从池中取任务，如果先结束，就先取任务，能者多劳。上游将任务投递到任务池内，下游从任务池内取任务。类似于生产者和消费者，会产生竞争和冲突。


## exec

1. 如果没有exec函数族，那就无法通过shell运行程序。因为fork只能复制一个shell。

2. exec函数族用来执行一个文件，会用一个新的进程镜像(来自新的可执行文件)替换掉当前进程的镜像，但是PID不会变化，其中有汇编级别的操作来操作内存和IP。替换的内容有：正文段，数据段，堆段，栈段：

   ```c
   #include <unistd.h>
   extern char **environ;  //环境变量
   int execl(const char *path, const char *arg, .../* (char  *) NULL */); //path为文件名，可以有多个命令行参数，最后以NULL结尾。
   int execlp(const char *file, const char *arg, .../* (char  *) NULL */); //和上一个不同的是，file为文件名，如果文件名中含有/，就将其视为路径名;否则就按path环境变量，在各个目录中寻找可执行文件。
   int execle(const char *path, const char *arg, .../*, (char *) NULL, char * const envp[] */);//和第一个比，允许使用自定义的环境变量envp。命令行参数和环境变量中间需要间隔一个NULL的参数。
   int execv(const char *path, char *const argv[]);  //命令行参数由一个字符指针数组当做一个参数传入。一般用于函数之间相互调用的情况，因为无法实现确定有多少个参数，因而无法使用execl函数。
   int execvp(const char *file, char *const argv[]); //类似于execlp
   int execvpe(const char *file, char *const argv[], char *const envp[]); //类似于execle
   ```

3. PATH环境变量包含了一个目录列表（路径前缀），目录之间用冒号分割，例如：

    ```shell
    PATH=/bin:/usr/bin:/usr/local/bin:.      #最后的.表示当前路径。一个零长度的前缀也表示当前目录，例如开头的单个: 中间的两个连续的:: 和末尾的:。
    #不过处于安全考虑，不推荐将.加入到PATH中。
    ```

4. exec函数族中的命令行参数是从argv[0]开始传入的。argv[0]对可执行程序本身没用，但是在该程序内部可能会使用到，该名称也被称作进程名，ps命令中会从argv[0]开始显示整个argv。

5. 如果此类函数产生返回，说明exec失败，因为原来的进程执行环境已经被破坏了，正常情况下该函数是不会返回的。

   ```c
   //exec前也应fflush刷新所有的流。和fork不同的是，fork会复制到子进程中一份。而如果不刷新，缓冲区内的内容会丢失。
   execl("\bin\date","date","+%s",NULL);  //如果该函数执行成功，其后的代码就被替换，因而不会再被执行了。
   perror("execl()");  //此处不用再判断返回值，因为只要该函数返回，就表示执行失败。直接打印错误信息，然后退出进程即可。
   exit(1);
   ```

6. 例子fork+exec+wait操作：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <sys/types.h>
   #include <unistd.h>
   int main(){
       pid_t pid;
       printf("Begin!\n");
       fflush(NULL);
       pid = fork();
       if(pid <0){
           perror("fork()");
           exit(1);
       }
       if(pid == 0){ //子进程
           execl("/bin/date","date","+%s",NULL);
           perror("execl()");
           exit(1);
       }
       wait(NULL); //父进程等待子进程
       printf("End!\n");
       exit(0);
   }
   ```

7. 在Shell环境下执行命令的过程：shell先fork一个子进程（和shell一样），然后在子进程中exec对应的命令，父进程中wait对应的子进程，子进程执行完毕后，shell为其收尸，最后显示命令提示符。

8. 自定义shell，还有很多地方待完善，可以将此shell作为某个用户的登录shell：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <glob.h>
   #include <string.h>
   #include <unistd.h>
   #include <sys/types.h>
   #include <sys/wait.h>
   #define DELIMS " \t\n"
   
   static void parse(char* linebuffer, glob_t* globres);
   
   int main() {
       char* linebuffer = NULL;
       size_t linebuf_size = 0;
       char* tok = NULL;
       glob_t globres;
       int times = 0;
       pid_t pid;
       while (1) {
           printf("zj@hit:$ ");
           fflush(stdout);
           if (getline(&linebuffer, &linebuf_size, stdin) < 0) {
               perror("getline()");
               exit(1);
           }
           parse(linebuffer, &globres);
           if (!strcmp(globres.gl_pathv[0], "-1"))
               exit(0);
           pid = fork();
           if (pid < 0) {
               perror("fork()");
               exit(1);
           }
           if (pid == 0) {
               execvp(globres.gl_pathv[0], globres.gl_pathv);
               perror("execvp()");
               exit(1);
           }
           wait(NULL);
           globfree(&globres);
       }
       exit(0);
   }
   static void parse(char* linebuffer, glob_t* globres) {
       char* tok = NULL;
       int times = 0;
       while (1) {
           tok = strsep(&linebuffer, DELIMS);
           if (tok == NULL)
               break;
           if (tok[0] == '\0')
               continue;
           glob(tok, GLOB_NOCHECK | GLOB_APPEND * times, NULL, globres);
           times = 1;
       }
   }
   ```


## u+s，g+s

1. 普通用户对/etc/shadow文件是没有读写权限的，但是却可以通过passwd命令来修改密码，其实就是修改该文件。用shell执行任何命令，都会附带着一个用户ID的信息，这样才可以执行文件的权限检查和资源利用限制。

2. 进程的PCB中除了存储着运行该进程的用户的UID和GID(也称为real)，还存储着effective，save的UID和GID，一共6个。suid，sgid不一定有，而real和effective是必须有的。

   ```c
   struct task_struct{
       ...
       uid_t uid,euid,suid,fsuid;
       gid_t gid,egid,sgid,fsgid;
       int ngroups;                  //记录进程在多少个用户组中
       gid_t groups[NGROUPS];      //记录进程所在的组
       ...
   }
   ```

3. 有些可执行文件还具有特殊权限，即所有者或所属组的执行权限变为s，s是包含x的。u+s的操作是other在执行该程序时，会暂时将EUID转变为文件的所有者的ID。这样可以将root的权限下放，给与普通用户一些暂时提权的固定行为。 在没有u+s权限的时代，普通用户都不可以修改自己的密码。例如：

   ```shell
   [zj@ZJ ~]$ ll /bin/passwd 
   -rwsr-xr-x. 1 root root 33K 4月   7 2020 /bin/passwd
   [zj@ZJ ~]$ ll /usr/bin/su
   -rwsr-xr-x. 1 root root 50K 7月  22 2020 /usr/bin/su
   [zj@ZJ ~]$ ll /usr/bin/sudo
   ---s--x--x. 1 root root 162K 1月  27 05:58 /usr/bin/sudo
   ```

4. 获取和修改real和effective ID：

   ```c
   #include <unistd.h>
   #include <sys/types.h>
   uid_t getuid(void);   //返回当前进程的real UID。uid_t在64位Ubuntu上为unsigned int
   uid_t geteuid(void);  //返回当前进程的effective UID。
   gid_t getgid(void);   //返回当前进程的real GID。gid_t在64位Ubuntu上为unsigned int
   gid_t getegid(void);  //返回当前进程的effective GID。
   
   int setuid(uid_t uid); //设置当前进程的effective UID。如果当前进程是有特权的(例如EUID为root或者是一个u+s的程序)，那么RUID和SUID也会被设置。
   int setgid(gid_t gid); //设置当前进程的effective GID。同上
   int seteuid(uid_t euid); //设置当前进程的effective UID。非特权进程只能将EUID设置为RUID,EUID或SUID。
   int setegid(gid_t egid); //设置当前进程的effective GID。同上
   
   int setreuid(uid_t ruid, uid_t euid);  //同时设置当前进程的real和effective UID，原子化的操作，有一个设置失败，则整个操作不会执行。如果有一个不想修改，可以用-1来代替。非特权进程只能将EUID设置为RUID,EUID,SUID中的一个。非特权进程只能将RUID设置为RUID或EUID。这个函数可以用来互换当前进程的EUID和RUID。
   int setregid(gid_t rgid, gid_t egid);  //同时设置当前进程的real和effective GID，原子化的操作。
   ```

5. u+s权限和setuid的例子：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <unistd.h>
   #include <sys/types.h>
   void getID() {
       printf("UID: %d\t", getuid());
       printf("EUID: %d\t", geteuid());
       printf("GID: %d\t", getgid());
       printf("EGID: %d\n", getegid());
   }
   int main(int argc, char* argv[]) {
       pid_t pid;
       printf("Before\n");
       if (argc != 2) {
           fprintf(stderr, "Usage:...\n");
           exit(1);
       }
       getID();
       if (setuid(atoi(argv[1])) < 0) {
           perror("setuid");
           exit(1);
       }
       printf("After\n");
       getID();
       exit(0);
   }
   //由root用户运行时，结果如下：
   root@hit:/home/zj/linux_c/process# ./uid 1000 //setuid的参数为1000
   Before
   UID: 0  EUID: 0 GID: 0  EGID: 0
   After
   UID: 1000       EUID: 1000      GID: 0  EGID: 0
   //如果通过chmod赋予该程序u+s权限，但是不修改所有者和所属组，由root执行同样的命令，结果如下：
   root@hit:/home/zj/linux_c/process# ./uid 0
   Before
   UID: 0  EUID: 1000      GID: 0  EGID: 0  //可以看到执行u+s权限的程序只会改变EUID
   After
   UID: 0  EUID: 0 GID: 0  EGID: 0  //而调用setuid函数后，会改变UID和EUID
   //如果EUID为0的进程通过setuid函数修改了自己的UID和EUID为1000后，此时它无法再通过setuid将EUID修改回0。
   
   ```

6. 例子，root用户修改自己的EUID，然后又修改回来：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <unistd.h>
   #include <sys/types.h>
   void getID() {
       printf("UID: %d\t", getuid());
       printf("EUID: %d\t", geteuid());
       printf("GID: %d\t", getgid());
       printf("EGID: %d\n", getegid());
   }
   int main(int argc, char* argv[]) {
       pid_t pid;
       if (argc != 2) {
           fprintf(stderr, "Usage:...\n");
           exit(1);
       }
       if (setreuid(-1, atoi(argv[1])) < 0) {
           perror("setuid");
           exit(1);
       }
       printf("Before\n");
       getID();
       if (setreuid(atoi(argv[1]), 0) < 0) {
           perror("setuid");
           exit(1);
       }
       printf("After\n");
       getID();
       printf("Back\n");
       if (setuid(0) < 0) {
           perror("setuid");
           exit(1);
       }
       getID();
       exit(0);
   }
   //由root用户来执行命令 ./uid 1000 结果为:
   root@hit:/home/zj/linux_c/process# ./uid 1000
   Before
   UID: 0  EUID: 1000      GID: 0  EGID: 0 //首先仅设置了自己的EUID
   After
   UID: 1000       EUID: 0 GID: 0  EGID: 0//然后将EUID修改为了RUID
   Back
   UID: 0  EUID: 0 GID: 0  EGID: 0 //最后将EUID和RUID还原为一开始的0
   ```

7. u+s，g+s被称为setuid或setgid。

   ```shell
   chmod u+s a.out    #为可执行文件设置u+s权限。只有该文件的所有者和root可以执行此命令
   ```

8. exec函数会检查可执行文件是否具备u+s或g+s权限，如果具备，则会将当前子进程的EUID修改为可执行文件的所有者的UID或GID。而RUID和RGID不变，内核总是通过有效UID和GID来判断权限的。RUID和RGID一般是用来做资源利用统计的。

9. exec切换EUID或EGID后，一般不需要再切换回去，因为可执行文件结束后，就被父进程或init收尸了。

10. u+s或g+s的权限设置要慎重，因为这样会使得一个普通用户没有输入root的密码也以root的身份来运行一个程序。


## sudo

1. 用户执行sudo命令时，因为sudo命令设置了是u+s权限的，因此exec函数会将子进程的EUID更改为root。sudo命令内部会再根据第一个参数再exec一次（此时EUID已经是root了，一般并不会修改EUID），传入后续对应的参数。这样sudo后面的命令就可以用root用户的身份执行了。

2. sudo命令中并没有设置有效UID的操作，因为它被设置了u+s权限，fork出的shell子进程在exec时就会修改EUID。

3. sudo并不要求其后的命令具有u+s或g+s权限。而sudo程序本身具有u+s权限。

4. 一般来说others用户执行u+s的程序并不需要任何验证信息。而sudo程序比较特殊，因为它的所有者是root，还有就是它再提权后，会再执行用户指示的程序。因而需要验证当前用户是否有资格来执行sudo提权。

5. 利用sudo来提升权限需要满足以下要求：当前用户符合在sudoers文件中某一项的设置（推荐使用visudo命令来修改该文件，因为修改该文件需要root权限，如果修改不当，可能导致当前用户没有了root权限，无法再次修改）。

   ```shell
   #/etc/sudoers文件
   # User privilege specification
   root    ALL=(ALL:ALL) ALL
   # Members of the admin group may gain root privileges
   %admin ALL=(ALL) ALL
   # Allow members of group sudo to execute any command
   %sudo   ALL=(ALL:ALL) ALL  #表明允许sudo组的所有用户执行任何命令。第二部分是扩展巴科斯范式EBNF。格式为  本条规则使用的用户或组 限制用户从哪些主机登录时才可以使用=(允许变身为的身份，冒号分割用户或组，ALL:ALL则表示任意组内的任意用户) 可执行命令的列表。
   #例子A B=(C:D) E     对于用户A来说，当他从主机B登录时允许它变身为用户C或用户组D的成员来执行命令E。
   
   #/etc/groups
   sudo:x:27:zj  #zj用户是在sudo组内的，因此它具备执行任何命令
   ```

6. 例子，写一个自定义的扩展功能的sudo，可以以指定de 任意用户来执行某个命令：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <unistd.h>
   int main(int argc, char* argv[]){
       pit_t pid;
       if(argc < 3){
           fprintf(stderr, "Usage:...\n");
           exit(1);
       }
       pid = fork();
       if(pid < 0){
           perror("fork()");
           exit(1);
       }
       if (pid == 0){
           if (setuid(aoti(argv[1])) < 0){
               perror("setuid");
               exit(1);
           }
           execvp(argv[2],argv+2);
           perror("exec()");
           exit(1);
       }
       wait(NULL);
       exit(0);
   }
   //执行命令   ./mysu 0 cat /etc/shadow      希望该程序会使用root用户的权限来执行cat /etc/shadow文件。但是setuid函数会报错，Operation not permitted。因为普通用户无法修改自己的EUID为root。
   //还需要root用户执行以下两步才可以达到目标：
   sudo chown root mysu
   sudo chmod u+s mysu
   ```

7. 可以用id命令来获取某个用户的RUID，RGID，EUID，EGID，还可以列出属于的所有组：

   ```shell
   zj@hit:~/linux_c/process$ id -un   #-u表示列出当前用户的有效用户ID。配合-r使用可以获得真实用户ID。whoami等价于id -un
   zj
   zj@hit:~/linux_c/process$ id -Gn   #-G表示列出当前用户所在的组,-n表示列出名称,而不是ID。
   zj adm cdrom sudo dip plugdev lxd
   zj@hit:~/linux_c/process$ id -gn   #-g表示列出当前用户有效组ID。配合-r使用可以获得真实组ID
   zj
   
   ./mysu 0 id -un  #结果为root
   ./mysu 0 id -run  #结果为root，可见setuid把RUID也改了。实际上u+s的程序在exec时并不会修改RUID，但是此时
   ./mysu 0 id -gn  #结果为zj
   ./mysu 0 id -rgn  #结果为zj
   ./mysu 0 id -Gn  #结果为zj adm cdrom sudo dip plugdev lxd
   ```

   

## 登录过程

1. 登录和用户身份切换过程：

   1. init进程（此时还是root用户）产生（fork + exec）一个getty进程，提示输入用户名，保存用户名。
   2. 然后getty进程再exec(login)，变身为login进程，提示输入密码，保存密码。
   3. 将输入的密码和shadow文件中对应的行的盐值组合，计算摘要是否等于之前设置的。到此，都是root用户的身份。
   4. 如果相等，则认证成功。fork+exec一个用户对应的shell程序。开始变成对应的用户身份。root用户可以设置当前进程的所有用户和组ID。但是设置完成后，就无法再修改回来了。
   5. 如果不相等，则exec一个getty进程。
2. 和一般的用法不同的是，可以不fork，直接exec。

## 解释器

1. 解释器文件就是脚本文件。

   ```shell
   #!/bin/bash
   ls
   cat /etc/shadow #一行一行地执行，中间的某一行出错，不会影响下一行。
   ps
   ```

2. exec函数会先判断文件的前两个字符是否是#!，如果是则为脚本文件，则不会直接将当前进程镜像替换为脚本文件，需要特殊处理：exec载入对应的解释器（路径存储在第一行的#!后面），其中包含一个命令行参数为脚本文件名。这样解释器就回解释执行整个当前文件（相当于执行命令bash a.sh或python a.py），包括第一行。由于exec根据开头的两个字符是否是#!来判断是不是脚本文件。所以一般解释器(bash，python)也顺便将#作为脚本文件的注释行，这样解释器就会跳过第一行。

3. 实际上#!后面可以不是解释器文件，任意的可执行文件都行，例如脚本文件abc为：

   ```shell
   #!/usr/bin/cat
   hah
   hoho
   ```

4. chmod a+x abc，然后执行./abc结果如下：

   ```shell
   [zj@manjaro linux]$ ./abc  #相当于/bin/cat ./abc,由于cat命令不会将#当做注释,因而会输出该解释器文件的每一行。
   #!/usr/bin/cat
   hah
   hoho
   ```

5. 有时候需要限制某些用户的操作，可以为其定制shell，需要修改/etc/passwd文件中的该用户的登录shell。

6. system函数执行shell命令：

   ```c
   #include <stdlib.h>
   int system(const char *command);//相当于调用/bin/sh -c command 可以看做是fork+exec+wait的简单封装。
   ```

## 竞争条件

1. 当多个进程都试图对共享数据进行处理，且最后的结果又取决于进程运行的顺序时，认为发生了竞争条件。
2. 如果fork之后，某种逻辑显式或隐式地依赖于父进程或子进程的先后执行顺序，那么认为fork处发生了竞争，因为无法保证fork后子进程和父进程哪个先执行。
3. 竞争导致的错误很难调试，因为它时而出现，时而不出现。

## 计时

1. clock_t在linux 64位下就是long类型，在C标准头文件time.h中定义。该头文件中还定义了CLOCKS_PER_SEC宏，表示一秒内的时钟滴答数，一般是100万。

2. C标准的时间函数clock：

   ```c
   #include <time.h>
   clock_t t = clock();
   printf ("Calculating...\n");
   ...
   t = clock() - t; //结果是时间差对应的滴答数
   printf ("It took me %d clicks (%f seconds).\n",t,((float)t)/CLOCKS_PER_SEC);
   ```

3. 进程时间，time命令的基础：

   ```c
   #include <sys/times.h>
   clock_t times(struct tms *buf);   //buf是该函数存储时间的结构体指针。返回值为墙上时钟的滴答数。这个函数和C标准库的time函数要区分开，time是获取从1970年到现在的时间戳。如果不想要详细的时间，参数可以传入NULL。
   struct tms {
       clock_t tms_utime;  /* user time */
       clock_t tms_stime;  /* system time */
       clock_t tms_cutime; /* user time of children */
       clock_t tms_cstime; /* system time of children */
   };    //用户时间+子进程的用户时间=最终的用户时间。
   
   //通过系统的times函数获取到的clock_t类型的滴答数，和时间的对应关系为1秒钟=sysconf(_SC_CLK_TCK)个滴答。一般是1秒钟=100滴答。而通过C标准头文件clock获取到的，1秒钟=100万滴答。因此clock函数更容易溢出，大约半个小时就会溢出。
   ```

4. 常见的计时方式有：

   1. 通过时钟中断进行间隔计时，每隔一定时间（一般为10ms），时钟中断就会传入CPU中，CPU会执行中断服务程序，减少当前进程的时间片，将当前进程PCB中的时间属性加1，如果中断时在用户态就增加用户时间，反之增加系统时间。这种方法不太精确，只有当程序运行时间在秒级别才有意义。
   
5. 使用time命令为进程计时，其中父进程会等待子进程，因此进程的时间会包含父进程自己的时间和子进程的运行时间，还有父进程等待子进程的时间，当然这三个时间有可能重叠。

6. sysconf函数可以在运行时获取系统的信息，通过一系列枚举量来指定，可以通过man sysconf查询：

   ```c
   #include <unistd.h>
   long sysconf(int name);
   //获得一个内存页面的大小。
   printf("Size of a page in bytes:%ld\n",sysconf(_SC_PAGESIZE));
   ```


## 会话和进程组

1. 真正的终端是在早期，多人共同使用一台计算机的情况，只有基本的输入输出，类似于网吧的无盘系统。现在使用的都是终端模拟器。

2. 一个终端的登录就产生一个会话session，当然也可以主动产生会话(创建守护进程时需要)。一个session可以容纳多个进程组，一个进程组内可以有多个进程。进程组分为前后台，任何时刻有且只有一个前台进程组，其余的都是后台进程组。之所以要区分前后台，主要是为了确定终端的输入分配给哪个进程组。

3. 进程组也有ID，称为PGID，进程组的leader，满足PID=PGID。父进程是它和他的子进程所在组的leader。

4. 会话也有ID，称为SID，会话的leader，满足PID=SID。

5. 刚登录时，只有一个进程组，该进程组内只有一个进程，就是该用户的登录shell。如果此时执行top命令则会创建一个新的进程组，组内只有一个进程top，该进程组为前台进程组，占据着终端。如果从top退出，则shell进程组又回到了前台。

6. 设计session和进程组的目的是为了支持shell的job管理。一个进程组通常称为一个job。使用管道符链接起来的多个进程属于同一个进程组，例如ls | wc。同一个进程组的所有进程隶属于一个session，同一个session共享一个控制终端。

7. 使用ps命令可以查看，PPID为父进程的ID，PGID为所属进程组的ID，SID为会话ID，TTY为关联的终端，？表示没有关联控制终端：

   ```shell
   [zj@manjaro ~]$ ps ajx
      PPID     PID    PGID     SID TTY        TPGID STAT   UID   TIME COMMAND
         0       1       1       1 ?             -1 Ss       0   0:01 /sbin/init
         1     372     372     372 ?             -1 Ss      81   0:00 /usr/bin/dbus-daemon 
   ```

8. 进程组中leader退出并不会终止该进程组中的其他进程。只有进程组的所有进程都退出后，进程组才会消亡。

9. 一个进程的PID不会变，PPID一般也不会变（如果父进程提前结束，子进程的PPID会变为父进程的父进程，有可能是1号的init进程），而PGID和SID是可以改变的。通过fork创建子进程时，子进程会继承父进程的PGID和SID。

10. 设置或获取进程相关的ID：

   ```c
   #include <unistd.h>
   pid_t getpid(void);  //获取当前进程的PID,没有对应的setpid，因为进程的pid是在fork时由内核从可用的pid中找出来的。
   pid_t getppid(void);  //获取当前进程父进程的PID，即PPID。同样也没有对应的setppid函数。
   
   pid_t getpgrp(void);  //获取当前进程所在的进程组ID，即PGID。
   pid_t getpgid(pid_t pid);  //获取参数pid进程的PGID，如果pid=0,那么表示获取当前进程的PGID,等价于getpgrp()。
   
   pid_t setpgrp(void);  //如果当前进程不是session的leader，会将当前进程的组ID修改为和当前进程的ID相同，也就是将当前进程单独成组。否则什么也不做。
   int setpgid(pid_t pid, pid_t pgid);  //修改pid进程的PGID为pgid。一个进程只能修改自己和它的同一个session中的子进程的组ID，否则会报错。如果pid=0,则表示修改当前进程的组ID。
   
   pid_t getsid(pid_t pid);  //获取进程pid所在的session ID。如果pid为0，表示获取当前进程所在的session ID。
   pid_t setsid(void); //如果当前进程不是一个进程组的leader，则会创建一个session，并且在新会话中创建一个新的进程组，然后把该进程放到新的进程组中。当前进程会变为新session和新group的leader，且新的session默认没有控制终端。新的PGID和SID都和该进程的PID相同。如果调用成功，返回新的session ID，否则返回-1。如果当前进程是组leader，则什么也不做。
   ```

11. 一般来说父进程fork出子进程，父进程是进程组的leader，而子进程不是，子进程可以通过调用这个函数，来变成一个新的进程组和session的leader，并且脱离控制终端，这也会将该子进程变为守护进程。

12. 例子：

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    int main() {
        pid_t pid;
        if ((pid=fork())<0) {
            fprintf(stderr, "fork error!\n");
            exit(1);
        }else if (pid==0) {   //进入子进程
            printf("The child process PID is %d.\n",getpid());
            printf("The Group ID is %d.\n",getpgrp());
            printf("The Group ID is %d.\n",getpgid(0));
            printf("The Group ID is %d.\n",getpgid(getpid()));
            printf("The Session ID is %d.\n",getsid(0));
            printf("The Session ID is %d.\n",getsid(getpid()));
            exit(0);
        }
        wait(NULL);
        printf("The parent process PID is %d.\n",getpid());
        printf("The PPID of parent process %d.\n",getppid());
        printf("The Group ID is %d.\n",getpgrp());
        printf("The Session ID is %d.\n",getsid(0));
        return 0;
    }
    //程序的输出：
    The child process PID is 1529.
    The Group ID is 1528.
    The Group ID is 1528.
    The Group ID is 1528.
    The Session ID is 1159.
    The Session ID is 1159.
    The parent process PID is 1528.
    The PPID of parent process 1159.
    The Group ID is 1528.
    The Session ID is 1159.
    //ps命令的结果
       PPID     PID    PGID     SID TTY        TPGID STAT   UID   TIME COMMAND
       1156    1158    1156    1156 ?             -1 R     1000   0:01 sshd: zj@pts/0
       1158    1159    1159    1159 pts/0       1538 Ss    1000   0:00 -bash
    ```

13. 可以发现bash进程(PPID=1158)是sshd进程(PID=1158)的子进程，但是两个进程不属于同一个session，是bash进程通过调用setsid实现的。bash进程是他所在的session和进程组的leader。他创建了程序中的父进程1528，后者又创建了它的子进程1529，这两个进程和bash同属于一个session 1159，但是这两个进程单独属于一个进程组1528，可见bash运行程序时会单独为其创建一个进程组，该程序就是该进程组的leader。


## 守护进程

1. 守护进程daemon（又称为精灵进程，因为daemon为古希腊神话中的半神半人精灵），类似于Windows上的服务，一般会开机自动在后台运行。
2. 守护进程的特点，前两条正好可以用setsid来实现：

   1. 守护进程一般是会话和进程组的leader。

   2. 守护进程一般都是脱离控制终端的，所以控制终端的输入输出会对他有影响，且会通过终端发送信号来影响守护进程。

   3. PPID=1，因为在创建守护进程时，他的父进程一般会直接退出，而不是等待为其收尸，因为守护进程可能要运行很久都不会退出。这样守护进程的父进程就变为init进程。
3. 一般会对守护进程的标准输入，标准输出和标准错误进行重定向，否则会报错。其父进程在fork前就先修改自己的标准输入，标准输出和标准错误，fork完再修改回来。
4. 创建守护进程的步骤：

   1. 父进程fork()创建子进程，然后父进程执行exit()，使得子进程被init接管。
   2. 子进程setsid()创建新会话，chdir("/")修改工作目录，这样可以防止占用某个挂载的设备，使得该设备无法卸载。
   3. umask(0)重新设置umask
   4. close() 关闭所有打开的文件描述符，因为子进程会继承父进程的所有打开的文件描述符。

      ```c
      for(i=0;i<getdtablesize();i++)  //getdtablesize返回当前进程文件描述符表的项数
          close(i);
      ```
   5. 执行守护进程的任务，顺便打开一个日志文件，记录日志。

5. 守护进程一般要求是单实例的，即重复启动会失败。一般通过在/var/run目录下的*.pid锁文件来实现。每次启动时，都会去检验该目录下是否存在同名的.pid文件，如果有则表示已经存在一个实例了，启动失败。锁文件内保存着该守护进程的PID。

6. 

## 日志

1. 守护进程脱离了控制终端，因此需要通过写日志来反应自己的运行状况。实际上所有的程序都应该写日志来记录自己的运行状况。可以写入到系统日志中，也可以写入到程序自己的日志中。系统日志需要通过系统的服务来写入。

2. 系统日志，在/var/log目录下。其下的messages文件为主日志文件。不能允许所有的程序任意修改日志，因此出现了syslogd服务，进程将要写的日志交给该服务，由该服务写日志，属于权限分离。日志文件的所有者和用户组一般都是root。

3. ```c
   #include <syslog.h>
   void openlog(const char *ident, int option, int facility); //关联日志服务。
   //indent为标识，例如进程名，会添加到每条日志的开头，如果为NULL，则使用程序名
   //option控制日志打开和后续写入的行为，常用的为LOG_PID，即在每条日志中包含进程的PID
   //facility用来指明写日志的程序的类型，常用的又LOG_FTP,LOG_MAIL,LOG_LPR,LOG_CRON等
   void syslog(int priority, const char *format, ...);  //priority是由openlog中的facility参数和level参数按位或得到的。其中level确定了日志的等级，常用的为LOG_ERR, LOG_WARNING, LOG_INFO, LOG_DEBUG。format及后面的参数可以当作和printf一样使用，syslog会自动为每一条日志换行。
   void closelog(void);  //关闭日志
   #include <stdarg.h>
   void vsyslog(int priority, const char *format, va_list ap);
   ```
   
4. 守护进程和系统日志综合例子：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   #include <unistd.h>
   #include <sys/types.h>
   #include <sys/stat.h>
   #include <fcntl.h>
   #include <syslog.h>
   #include <errno.h>
   #include <string.h>
   #define FNAME "/tmp/out1"
   int main() {
       FILE* fp = NULL;
       pid_t pid = 0;
       int fd = 0;
       int i = 0; //打印计数器
       openlog("mydaemon", LOG_PID, LOG_DAEMON);
       pid = fork();
       if (pid < 0) {
           syslog(LOG_ERR, "fork() failed %s", strerror(errno)); //不能使用perror报错。
           exit(1);
       }
       if (pid > 0) {
           exit(0);
       }
       //子进程代码
       fd = open("/dev/null", O_RDWR); //打开一个设备
       if (fd < 0) {
           syslog(LOG_ERR, "open(\"/dev/null\") failed %s", strerror(errno));
           exit(1);
       }
       dup2(fd, 0);
       dup2(fd, 1);
       dup2(fd, 2);
       if (fd > 2) {
           close(fd);
       }
       chdir("/");
       umask(0);
       if (setsid() < 0) {
           syslog(LOG_ERR, "setsid() failed %s", strerror(errno));
           exit(1);
       } else {
           syslog(LOG_INFO, "setsid() success");
       }
       fp = fopen(FNAME, "w"); //打开一个文件
       if (fp == NULL) {
           syslog(LOG_ERR, "fopen(%s) failed %s", FNAME, strerror(errno));
           exit(1);
       }
       syslog(LOG_INFO, "%s was opend", FNAME);
       while (1) {
           fprintf(fp, "%d\n", i);
           fflush(fp);
           sleep(1);
           i++;
       }
       fclose(fp);
       closelog();
       exit(0);
   }
   //实测Ubuntu22.04会将日志写入到/var/log/syslog文件中。
   ```

# 信号

1. 信号和多线程是实现并发的两大类方法。


## 同步和异步

1. 事件可以分为同步和异步。异步的意思是事件何时到来不确定。钓鱼中的鱼上钩，俄罗斯方块中按键的到来，网络编程中监听外部连接的到来就可以看做是一个异步事件。

2. 异步事件的处理方法：
   1. 查询法：适用于事件发生频率较高的情况。主动。
   2. 通知法：适用于事件发生频率较低的情况。被动。本质上也是查询，可以看做间接查询。让别人主动查询，然后通知自己。

3. 信号属于初步异步，线程属于强烈异步。混合使用的比较少。


## 信号

1. 信号是软件层面的中断，和系统调用中的int 0x80还不一样。信号的响应依赖于中断机制。信号是进程层面的。

2. 信号是经典的异步实例，进程不能通过测试某个变量来判断是否发生了信号，只能告诉内核，当某个信号发生时，应该如何响应。

3. ```shell
   [zj@manjaro ~]$ kill -l
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
   ```

4. 信号1-31称为标准信号，34-64称为实时信号，RT为RealTime。信号的名字都是以SIG开头的。

5. 标准信号会丢失，而实时信号不会。

6. 信号的不可靠指的是信号的行为不可靠，而不是标准信号会丢失。因为程序中没有显式书写调用信号处理程序的语句，信号处理程序的执行现场是内核布置的。在处理一个信号的同时，如果又来了一个相同的信号，第二次的执行现场就可能把第一次的覆盖掉。早期的Unix为了规避这种问题，就规定信号处理程序在被响应一次后，信号的行为变成默认的。

7. 产生信号的方法：

   1. 用户在终端上的按键，例如Ctrl+C会产生一个SIGINT信号，发送给前台进程组。Ctrl+\会产生一个SIGQUIT信号。
   2. 硬件异常产生信号，例如除数为0，无效的内存引用，这些异常由硬件产生，通知内核，内核为进程产生一个信号。例如访问0地址会受到SIGSEGV。
   3. kill函数或命令可以发送任意信号给一个进程或进程组。有权限要求，普通用户的进程只能发送给自己的其他进程，root用户的进程可以发送给任意用户的进程。
   4. 当检测到某些条件满足，会发送信号，这里的条件是软件层面的，例如定时器到时，会发送SIGALRM信号。

8. 对于信号的处理：

   1. 忽略此信号，大多数信号都可以这样处理，SIGKILL和SIGSTOP除外，否则进程不能被内核或root终止。如果忽略某些硬件产生的信号，例如除0，进程的行为将是不确定，因此不推荐忽略这些信号。
   2. 捕捉信号，对信号进行处理。不能捕捉SIGKILL和SIGSTOP信号。
   3. 执行系统的默认动作，大多数信号的默认动作都是终止该进程或终止+产生core文件。

9. 大部分的系统都支持31个信号，Solaris支持40个信号。标准C中规定的信号特别少。

10. ![image-20210620105646237](Linux系统编程.assets/image-20210620105646237.png)

11. signal函数，为一个信号注册处理函数：

    ```c
     #include <signal.h>
    typedef void (*sighandle_t)(int);  //定义了一个函数指针类型。多个信号可以共用一个信号处理函数，因此信号处理函数的参数int为此次触发该函数的信号编号。
    sighandle_t signal(int signum, sighandle_t handler); //返回值为信号之前的处理函数指针
    //展开如下：
    void (*signal(int sig, void (*func)(int)))(int);  //建议使用这种，因为可以少定义一个类型，避免命名冲突。
    ```

12. signal函数的第二个参数可以是SIG_IGN(忽略信号)，SIG_DFL(系统默认行为，这样做相当于恢复默认)或用户自定义的函数。

13. 例子：

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <signal.h>
    static void siginthandler(int){
        write(stdout, "!", 1);
    }
    int main(){
        void (*oldsiginthandler)(int);
        oldsiginthandler = signal(SIGINT, siginthandler);
        for (int i = 0; i < 10; i++){
            write(stdout, "*", 1);
            sleep(1);
        }
        exit(0);
    }
    //执行程序，在中途按下Ctrl+c键，结果如下：
    *****^C!*****      //其中^C是功能键的回显，可以关闭。
    ```

14. 阻塞的系统调用会被信号打断而提前返回，例如sleep（规定的时间走完之前），write（在写入任何数据之前），read（在读到任何数据之前）等，此时会设置errno为EINTR。因此如果上面的程序按住Ctrl+C不松的话，程序会很快执行完。

15. 用信号改写之前的程序，例如文件的打开：

    ```c
    do{
        fd = open("/tmp/out", O_RDWR);
        if(fd < 0 && errno != EINTR){  //如果出错且不是因为中断，那表示是真错误，可以退出。
            perror("open()\n");
            exit(1);
        }
    }while(fd < 0)
    ```

16. 可重入函数是为了解决信号的不可靠而产生的。信号处理函数应该为可重入的。其特点是，上一次调用还没结束，下一次调用就发生了，但是二者不会相互影响。所有的系统调用都是可重入的，一部分库函数也是可重入的，例如memcpy。不可重入的库函数一般都会有\_r版本，例如rand和rand\_r。rand产生的随机值是伪随机序列。每次产生的随机值是在上一次的基础上产生的。不可重入函数大多是包含局部静态变量，用来记录多次调用的上下文。通过将局部静态变量变成函数的参数，也就是将其放在栈上，这样就变成可重入的函数了。

    ```c
    #include <stdlib.h>
    int rand(void);
    int rand_r(unsigned int *seedp); //多了一个参数，seedp用来标识不同的调用状态。
    ```

17. 是否可重入在man手册中有个表格会标识出来：

18. ![image-20230509211103651](assets/image-20230509211103651.png)

19. 标准信号的响应过程：

    1. 内核为每个进程维护了至少2个位图，mask和pending，二者都是32位的，分别对应于32个Unix标准信号。mask是信号屏蔽字。用来标识当前进程的状态，默认为全1。pending用来记录当前进程收到了哪些信号，初始为全0，进程收到信号时，内核会将其pending位图的对应位置为1。

    2. 进程在重新获得CPU使用权，从Kernel态转化到User态时，会先计算下mask & pending 按位与操作来获得自己要处理的信号（可能有多个）。然后将其中一个（先响应哪个是没有严格的顺序）信号的mask和pending位都置为0，再去调用对应信号的处理函数。pending置为0表示处理了这个信号，mask置为0是防止重入现象，即另一个线程也对此信号进行处理。

    3. 从该信号处理函数返回后，再进入内核，将上一次的信号的mask位置为1，pending位不处理，此时已经完成了一个信号的处理。然后从内核态回到用户态，重复第2步的操作，继续做mask & pending 的按位与。

20. 通过将signal的第二个参数即信号处理函数设置为SIG_IGN来忽略一个信号。这个函数实际是将指定信号的mask设置为0，这样在按位与时，即使pending位为1，结果也为0。

21. 信号从受到到响应有不可避免地延迟，因为进程只有在（通过中断）陷入内核，然后重新获得CPU使用权时才会处理信号。如果进程当前正在使用CPU或正在排队等待，是无法对信号立刻响应的，收到的信号只能由内核存储在对应进程的pending位图中。用信号来计时的话可能会带来10ms左右的误差。

22. 之所以要在执行信号处理函数期间将对应的mask置为0，是因为这样会避免该函数被同一个信号重入。

23. 如果在短时间内收到了相同的多个信号，只会当作一次，因为位图只有0和1两种情况。

    1. 一种是进程在运行或排队等待CPU时收到了多个相同信号，内核会重复地将对应的pending位设置为1。
    2. 另一种是进程在执行信号处理函数时，收到了多个相同的信号，内核也会重复地将对应的pending位设置为1。

24. 实时信号不会丢失，会记录下相同信号的数量，依次响应。

25. 常用函数：

    ```c
    #include <sys/types.h>
    #include <signal.h>
    int kill(pid_t pid, int sig); //给进程或进程组发送信号sig，kill并非是用来杀死进程，主要是由于大部分的信号的功能是用来杀死进程的。如果pid>0，则是对应的进程。如果pid=0，则发给和当前进程同组的每个进程，一般称为组内广播。如果pid=-1，给当前进程有权发送信号的每个进程发送，除了1号进程init以外，例如即将解除设备挂载时，init进程可以对所有进程发送信号，要求他们解除对该设备的使用。如果pid<-1，将信号发送给进程组ID为-pid内的每个进程。如果sig=0，则不发送信号，但是会执行判断进程是否存在和是否有权对该进程发送信号的检查，这个功能一般用来检查某个进程或进程组是否存在。成功发送至少一个信号则返回0，否则返回-1，并设置errno。
    #include <signal.h>
    int raise(int sig); //给调用进程或线程发送一个信号。在单线程进程中，等价于kill(getpid(), sig)，在多线程进程中，等价于pthread_kill(pthread_self(), sig)。若成功则返回0。
    #include <unistd.h>
    unsigned int alarm(unsigned int seconds); //在倒计时seconds秒后，给当前进程发送一个SIGALRM信号。如果seconds=0，则不会产生新的倒计时。新的alarm设置会覆盖掉旧的。例如alarm(10);alarm(5)，大约会在5s后收到信号。
    #include <unistd.h>
    int pause(void);  //使得调用进程或线程睡眠，以等待一个信号的到达。当信号到达，且其信号处理函数执行完毕后，pause才会返回。
    ```

26. 某些实现中，sleep是用alarm和pause来封装的。这时不推荐使用sleep，因为其内部的alarm和外部其他的alarm会冲突。考虑到移植的问题，因此不推荐使用sleep。

27. 例子，让程序对一个变量持续累加5s，然后打印结果：

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>
    int main() {
        time_t end;
        long long count = 0;
        end = time(NULL) + 5;
        while (time(NULL) <= end) {
            count++;
        }
        printf("%lld\n", count);
        exit(0);
    }
    //用time命令来对进程进行计时，三次结果如下，可以发现时间相差较大，这取决于进程开始执行的时间是处在一秒钟的开头部分还是结尾部分，因为在一秒内的任意时刻获取time都是相同的，假设开始时间为2.1s，结束时间为8.0s，则一共经历5.9s；若开始时间为2.9s，结束时间相同，则一共经历5.1s：
    zj@hit:~/linux_c/parallel$ time ./5sec 
    2614308708
    real    0m5.392s
    user    0m5.389s
    sys     0m0.000s
    zj@hit:~/linux_c/parallel$ time ./5sec 
    2567372156
    real    0m5.289s
    user    0m5.287s
    sys     0m0.001s
    zj@hit:~/linux_c/parallel$ time ./5sec 
    2489735892
    real    0m5.138s
    user    0m5.136s
    sys     0m0.001s
    ```

28. 使用信号来优化上一个程序：

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>
    #include <signal.h>
    #include <unistd.h>
    static volatile int flag = 1;
    static void alrm_handler(int) {
        flag = 0;
    }
    int main() {
        time_t end;
        long long count = 0;
        signal(SIGALRM, alrm_handler); //要求必须先注册信号处理函数，然后再计时。
        alarm(5);
        while (flag) { //这个程序如果使用gcc -O1优化可能会产生一个bug，就是gcc认为循环体内没有改变flag，因此在每次测试flag时，都是直接从寄存器中读取来提高效率，而非每次从内存中读取。这样会导致及时信号处理函数已经在内存中修改了flag的值，由于while不会从内存中读取，因而程序会进入死循环。因此推荐在flag的定义中加上volatile关键字，使得每次遇到该变量时，都去内存中读取它的值，而非使用寄存器中的值。在嵌入式编程中常用。
            count++;
        }
        printf("%lld\n", count);
        exit(0);
    }
    //用time命令来对进程进行计时，两次结果如下，可以发现时间相差不大，而且虽然修改的程序运行时间断了，但是计数的值却比修改前的大，这是因为修改前的程序每步循环都要取时间戳，会浪费CPU。可以发现alarm的精度比time更高，且更节省CPU。
    zj@hit:~/linux_c/parallel$ time ./5sec_sig
    2723499745
    
    real    0m5.003s
    user    0m4.997s
    sys     0m0.004s
    zj@hit:~/linux_c/parallel$ time ./5sec_sig
    2738516149
    
    real    0m5.003s
    user    0m4.982s
    sys     0m0.012s
    ```

29. 在一些需要定速输出的程序（播放视频，网络发送数据）中，可以使用alarm和pause的组合。例子：每秒从文件中读取10个字符，同时输出到终端。

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <sys/types.h>
    #include <fcntl.h>
    #include <sys/stat.h>
    #include <errno.h>
    #include <signal.h>
    #define CPS 10
    #define BUFFERSIZE CPS
    static volatile int loop = 0;
    void alrm_handler(int) {
        alarm(1); //每次响应alarm信号时，再设置一个alarm信号，这样就可以每秒收到一个alarm信号了
        loop = 1;
    }
    int main(int argc, char* argv[]) {
        int sfd, dfd = 1;  //目标流为标准输出
        char buf[BUFFERSIZE] = { 0 };
        int len, ret, pos;
        if (argc < 2) {
            fprintf(stderr, "Usage:...\n");
            exit(1);
        }
        do {
            sfd = open(argv[1], O_RDONLY);
            if (sfd < 0) {
                if (errno != EINTR) {
                    perror("open");
                    exit(1);
                }
            }
        } while (sfd < 0);
        signal(SIGALRM, alrm_handler);
        alarm(1);
        while (1) {
            while (!loop)
                pause();
            loop = 0; //从pause恢复后，立刻为下一次等待设置条件
            len = read(sfd, buf, BUFFERSIZE);
            if (len < 0) {  //读和写的重要区别，如果read的返回值小于目标读取量，不推荐反复读，因为
                if (errno == EINTR) {
                    continue; //读取失败时，会回到35行，然后又会在37行等待。主要是因为38行中已经将loop设置为0了，有两种方案，第一种是将loop=0移动到46行或62行之后。第二种是为了这个read在添加一层while循环。这样continue才会回到read处。
                }
                perror("read()");
                break;
            }
    /* 第二种方案例子
    		while((len = read(sfd, buf, BUFFSIZE)) < 0){
                if (errno == EINTR) {
                    continue;
                perror("read()");
                break;
            }
    */
            if (len == 0) {
                break;
            }
            pos = 0;
            while (len > 0) {
                ret = write(dfd, buf + pos, len);
                if (ret < 0) {
                    if (errno == EINTR) {
                        continue;
                    }
                    perror("write()");
                    exit(1);
                }
                pos += ret;
                len -= ret;
            }
          //loop = 0;
        }
        close(sfd);
        exit(0);
    }
    //从/etc/services中读取，并每秒输出10个字符
    ./slowcat /etc/services
    ```

30. 假设要读取的内容来自一个慢速的设备，例如打印机，若此时设备上没有数据，程序会阻塞在39行，然后等时钟信号到来后，阻塞被打断，经过42行的跳转，又会阻塞在39行。如果到来的数据量非常大，也无能为力，因为只能一秒读取一次，一次读取10个字符。这是典型的漏桶的实现。

31. 令牌桶是漏桶的改进，当读不到数据时，会积攒读取的权限，下次如果能读取多个，就会尽可能消耗掉权限。这样能应对波动的数据输入。一般数据的到来都是突发的，短时间会到来大量的数据，其他时间都在静默。令牌桶的实现如下，数据突然涌入时，也会突然消耗掉之前积攒的权限，读写多次：

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <sys/types.h>
    #include <fcntl.h>
    #include <sys/stat.h>
    #include <errno.h>
    #include <signal.h>
    #define CPS 10
    #define BUFFERSIZE CPS
    #define BURST 100 //token的上限
    static volatile int token = 0; //用来标记积攒的读取权限
    void alrm_handler(int) {
        alarm(1);
        token++;
        if (token > BURST){
            token = BURST;
        }
    }
    int main(int argc, char* argv[]) {
        int sfd, dfd = 1;
        char buf[BUFFERSIZE] = { 0 };
        int len, ret, pos;
        if (argc < 2) {
            fprintf(stderr, "Usage:...\n");
            exit(1);
        }
        do {
            sfd = open(argv[1], O_RDONLY);
            if (sfd < 0) {
                if (errno != EINTR) {
                    perror("open");
                    exit(1);
                }
            }
        } while (sfd < 0);
        signal(SIGALRM, alrm_handler);
        alarm(1);
        while (1) {
            while (token <= 0) //只要token>0，就会不暂停，直接读写
                pause();
            len = read(sfd, buf, BUFFERSIZE); //如果读取不到任何内容，则会阻塞在此处，等到下一次时钟信号到来被打断，在45行continue，又会等待在42行上，但是此时token已经完成了自增1，积累了一次权限。
            if (len < 0) {
                if (errno == EINTR) {
                    continue;
                }
                perror("read()");
                break;
            }
            if (len == 0) {
                break;
            }
            pos = 0;
            while (len > 0) {
                ret = write(dfd, buf + pos, len);
                if (ret < 0) {
                    if (errno == EINTR) {
                        continue;
                    }
                    perror("write()");
                    exit(1);
                }
                pos += ret;
                len -= ret;
            }
            token--;//完成一次输出，消耗掉一个token。这里存在一个可能出错的问题，就是信号处理函数15行也会对全局变量token进行处理，一般来说这里和15行不大可能时间上冲突。还有就是在某些精简指令集系统中，token--可能会被翻译成多条指令，非原子。可以将token声明为sig_atomic_t类型。这样对于该变量的使用和赋值都会是原子的。
        }
        close(sfd);
        exit(0);
    }
    ```

32. 实际上程序只要求匀速输出，至于读取的频率有多快，每次读取多少并不关心。例如用户只关心视频能否流畅播放，不关心缓冲的速度和进度。这种最好用多线程，生产者消费者模型来实现。

33. 为了方便后续的使用，可以将令牌桶封装成库，供其他程序调用。考虑到程序中可能需要多个令牌桶，该库中也应该维护一个令牌桶的数组或链表。

34. 结构体指针数组中，可以让结构体来自述下标。也就是说如果接收到了一个结构体指针，要释放它，此时不用去数组内循环查找它的位置来将其设置为NULL。可以在结构体的设计中包含一个pos变量，生成该结构体的时候，就存储上它在数组中的位置。这样在释放它时，可以直接通过pos变量来获取它的位置。直接对数组的对应元素赋值NULL。

35. 用单一计时器alarm来实现多任务计时器，效果如下：

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    
    void f1(char* s){
        printf("f1(): %s", s);
    }
    void f2(char* s){
        printf("f2(): %s", s);
    }
    int main(){
        int job1, job2, job3;
        puts("Begin!");
        if ((job1 = anytimer_addjob(5,f1,"aaa")) < 0){ //用一个结构体将等待时间，注册待调用的函数和参数保存起来。
            fprintf(stderr, "anytimer_addjob(): %s\n", strerr(-job1)); //校验返回值，后面调用两个也应该有。
            exit(1);
        }
        anytimer_addjob(2,f2,"bbb"); //用一个结构体指针数组来管理所有的计时器。每过一秒钟，将所有的有效计时器的等待时间都-1。如果在某一秒中，某个计时器的等待时间变为了0。则调用注册的函数，完事释放该结构体，并将对应的数组元素置为NULL。
        anytimer_addjob(7,f1,"ccc");
        puts("End!");
        while(1){ //不能立刻结束，需要等待时钟到来
            write(stdout, "*", 1); //每秒向控制台输出一个*
            sleep(1);
        }
    }
    //程序的预期结果为 先输出2个*，13行的信号到来输出，然后输出3个*，12行的信号到来，然后输出2个*，最后14行的信号到来，然后一直输出*。即**f2(): bbb***f1(): aaa**f1(): ccc*******
    ```

36. anytimer.h：

    ```c
    #ifndef ANYTIMER_H__
    #define ANYTIMER_H__
    
    #define JOB_MAX 1024
    typedef void(*anytimer_jobfunc_t)(void);
    /*
     *返回值  >=0    成功，返回计时任务ID
     *        == -EINVAL    失败，参数非法     //这里用系统自带的errno来返回出错的结果，调用者可以用strerr(返回值)来获取详细的出错信息。
     *        == -ENOSPC    失败，数组满
     *        == -ENOMEM    失败，内存空间不足
     */
    int anytimer_addjob(int sec, anytimer_jobfunc_t job, void* arg); //传给用户一个类似于文件描述符的整数，实际上就是结构体指针所在数组的下标。
    /*
     *返回值 == 0 成功，指定任务已经取消
     *      == -EINVAL 失败，参数非法
     *      == -EBUSY  失败，指定任务已完成
     *      == ECANCELED 失败，指定任务重复cancel
     */
    int anytimer_canceljob(int id);//取消一个job
    
    /*
     *返回值 == 0 成功，指定任务的结构体已经成功释放
     *      == -EINVAL 失败，参数非法
    */
    int anytimer_waitjob(int id);
    
    #endif
    ```

37. setitimer和getitimer，中间的i表示interval，即时间间隔。不同于时刻定时器，后者在某一时刻到达时才会触发。系统为每个进程提供了三种时钟，一个进程每种计时器最多只能有一个。setitimer的好处是，长期运行误差不累计。

    ```c
    //当时间间隔定时器(interval timer)到时后，内核会发送一个信号给调用进程。然后计时器会重置为特定的值，如果时间间隔非零的话。
    #include <sys/time.h>
    int getitimer(int which, struct itimerval *curr_value);//which为要设置的时钟，时钟存储在curr_value中。
    int setitimer(int which, const struct itimerval *new_value,struct itimerval *old_value);//用新的new_value设置，如果要保存旧的，可以提供old_value，否则可以用NULL代替。
    struct itimerval {
        struct timeval it_interval; //周期间隔，每个it_interval时间都会发送一个信号。
        struct timeval it_value;    //初始时间间隔，每次都会递减这个值
    };
    struct timeval {
        time_t      tv_sec;  //秒
        suseconds_t tv_usec; //微秒
    };
    //若成功，返回0，否则返回-1，并设置errno。
    //如果it_value的2个字段都为0，则表示关闭这个定时器。如果it_interval的2个字段都为0，则表示这个定时器仅生效一次，否则为循环定时器。
    ```

38. 三种时钟到时后，发出的信号不同。

    1. ITIMER_REAL 用墙上时间计时，每次到时后发出SIGALRM信号。和alarm函数类似。
    2. ITIMER_VIRTUAL 用进程在用户态消耗的CPU时间来计时，计算该进程下所有线程的和。每次到时后发送SIGVTALRM信号。
    3. ITIMER_PROF 用进程消耗的总CPU时间(用户态和内核态之和)来计时，计算该进程下所有线程的和。每次到时后发出SIGPROF信号。联合ITIMER_VIRTUAL可以用来度量进程的用户和内核态的CPU用时。

39. 通过fork产生的子进程不继承父进程的时间间隔定时器。时间间隔定时器在execve时保留。

40. 

41. 

42. 

43. 用sigprocmask函数block的信号，在被屏蔽期间，终端的按键会回显也会发出信号，设置pending中的位图，但是却无法打断阻塞的系统调用，例如sleep。

44. sigpending的作用不大，它会去内核中获取pending集，即到来的信号的状态。但是该函数从内核中返回时，就会响应一个信号，返回后的pending集就跟原来不同了。

45. 不能从信号处理函数随意跳转到其他位置，例如使用longjmp。因为信号处理函数结束后，还要把之前的设置过的mask位恢复，若longjmp，就没有机会做这件事，会导致该进程永远无法收到该信号了。不同unix的行为不一样，BSD上在setjmp时，就可以设置保存mask。然后再longjmp时，会自动回复。POSIX提供了两个函数用来完成这样的工作：sigsetjmp和siglongjmp，配套使用，这样就可以从信号处理函数往外跳了。

    ```c
    #include <setjmp.h>
    void sigsetjmp(sigjmp_buf env, int savesigs);//savesigs表示是否要保存mask，如果为true，则siglongjmp时，就会自动恢复mask。
    void siglongjmp(sigjmp_buf env, int val);
    ```

46. sigsuspend可以用来实现一个信号驱动程序。

47. 

48. 用signal为多个信号注册同一个处理函数时可能会出现信号处理函数被重入的风险。例如信号A，B都注册了处理函数C，当进程在执行处理函数C来响应信号A期间，可能会进入内核，在从内核返回时，又回去响应刚刚到来的信号B，因此又会去调用C。这样C函数将会被调用两次。另外一种情况就是从内核返回时，也可能。如果使用signal函数，要避免这种情况，就只能在信号处理函数一开始就先屏蔽掉其他注册了此处理函数的其他信号，然后在信号处理函数结束时，再恢复。

49. sigaction可以完整地替换signal函数。并解决上面的问题。

50. signal并不区分信号的来源。

51. 

52. 

53. 


# 库的使用

1. 在程序开发时，通常把公用的自定义功能从主程序中分离开来，函数和类的生命在头文件中，其实现在源文件中，主程序包含头文件，链接包含库文件即可使用该库的功能。

2. 共享库使得可执行文件中不必包含公用的库函数代码。只需要在所有进程都可以引用的内存区域载入一份该共享库即可。共享库的一个优点是：用库函数的新版本替代老版本而无需对使用该库的程序重新编译链接（假定参数的数目和类型都没变）。

3. 使用gcc -static可以阻止gcc使用共享库，也就是都用静态链接，这样程序的各个段和总体积会变大很多。

4. 编译成库文件可以隐藏具体代码实现。动态库文件还可以随时更换，更新方便，动态加载，用完卸载，节省内存。

5. 一般的头文件都有条件编译的宏定义，为了防止重复包含。头文件public.h：

   ```c
   /*
    * 程序名：public.h，公共功能函数声明的头文件，用于测试静态和动态链接
    * 作者：xxxxx 日期：xxxxxx
   */
   #ifndef PUBLIC_H
   #define PUBLIC_H
   void func();     // 自定义函数的声明
   
   #endif
   ```

6. 源文件public.cpp：

   ```c
   /*
    * 程序名：public.cpp，公共功能函数定义的程序文件，用于测试静态和动态链接
    * 作者：xxxxxx 日期：xxxxxxxx
   */
   #include "public.h"  // 包含自定义函数声明的头文件
    
   void func()   // 自定义函数的实现
   {
     printf("我心匪石，不可转也。我心匪席，不可卷也。威仪棣棣，不可选也。\n");
   }
   ```

7. 如果库是以源代码的形式给出的，则可以编译的时候，加上库的源文件即可。例如：

   ```shell
   g++ -o book265 book265.cpp public.cpp
   ```

8. 不包含头文件，编译不通过；不链接库，不能运行成功。

9. 动态库是在程序执行的开始进行判断寻找对应的文件是否存在，在需要的时候才会载入，占用运行时。静态库占用程序体积，但是不会占用运行时。

10. 静态库：一般取名为libxxx.a，其中xxx为库名。

    ```shell
    ar -cr libxxx.a xxx.o yyy.o        //把目标代码打包成一个静态库。
    ```

11. 静态，动态库必须要手动链接才可以，在编译时，都要指明路径和库名（如果不是在默认的位置）。

    ```shell
    gcc -L/usr/local/lib -o main main.o -lxxx     //-L后面表示搜索库的路径，一般默认的路径不用包含。-l参数必须在最后。  从-lxxx看不出要链接动态还是静态库，如果出现重名，优先选择动态库。
    ```

12. 动态库：一般取名为libxxx.so.y    xxx为库名，y为版本号。

    ```shell
    gcc -shared -fPIC -o libxxx.so xxx.c     //-shared表示生成动态库。-fPIC表示位置无关代码，也可以是-fpic，
    ```

13. 一般来说动态库libxxx.so都是一个软连接，指向libxxx.so.y之类的具体版本的库。

14. 如果发布的位置不是在标准的位置，还要在/etc/ld.so.conf配置文件中添加该位置。然后使用/sbin/ldconfig重新读入该配置文件。其实在标准或非标准位置新增库文件，都应该执行该程序一下，它的作用是将文件/etc/ld.so.conf列出的路径下的库文件缓存到/etc/ld.so.cache以供使用。配置文件如下：

    ```shell
    include ld.so.conf.d/*.conf   #会读入该目录下的所有配置文件。
    /x/lib           #用户新添加的路径
    ```

15. 如果一个程序依赖多个库，且这些库之间也存在依赖关系，那么在-l时，被依赖的库要放在后面。

16. 还可以在程序执行的过程中手动装载和卸载，这样可以使程序启动速度加快，节约内存开销。

17. 静态，动态库的发布：

    1. 将头文件xxx.h存放到/usr/local/include中。
    2. 将编译好的静态库libxxx.a或libxxx.so放在/usr/local/lib中。

18. ldd工具，查看当前可执行文件依赖的动态库：

    ```shell
    [zj@ZJ ~] ldd ./llist 
    	linux-vdso.so.1 => (0x00007fff3b35f000)
    	libllist.so => /usr/local/lib/libllist.so (0x00007f1c761b2000)
    	libc.so.6 =>/lib64/libc.so.6 (0x0000003fdfe00000)
    	/lib64/ld-linux-x86-64.so.2 (0x0000003fdf600000)
    ```

## 静态库

1. linux下静态库文件名为libxxx.a      其中xxx为库的名称。lib和.a不可省略。

2. 静态库的生成方法：

   ```shell
   g++ -c -o libpublic.a public.cpp          # -c表示只进行预处理，编译，汇编，不链接，生成.o的目标文件。
   ```

3. 使用方法有两种：

   1. 直接把调用者的源代码和库文件一起编译：

      ```shell
      g++ -o book265 book265.cpp libpublic.a   #实际就是分步编译，这里要使用库的文件名
      ```

   2. 采用L参数指定静态库文件的目录，-l参数指定静态库名。

      ```shell
      g++ -o book265 book265.cpp -L/home/wucz/demo -lpublic   #-l的参数为库名，而不是库的文件名。如果要制定多个库和库的目录，则可以使用多次-L,-l。
      ```

## 动态库

1. 动态库的命名libpublic.so，和静态库相比，就是后缀名不同。动态库是运行时动态加载，因此需要制定动态库的目录。

2. 动态库的生成方法：

   ```shell
   g++ -fPIC -shared -o libpublic.so public.cpp
   ```

3. 文件属性：

4. ![image-20201207101605678](assets/image-20201207101605678.png)

5. 在同一个目录下，如果既有静态库又有动态库，那么优先使用动态库。如果非要使用静态库，则应该使用静态库的第一种编译方法。

6. 动态库的使用方法：

   ```shell
   g++ -o book265 book265.cpp -L/home/wucz/demo -lpublic #方法和静态库的相同。
   ```

7. 如果在运行时出现如下异常，则应该制定动态库的位置。

8. ![image-20201207101850646](assets/image-20201207101850646.png)

9. ```shell
   export LD_LIBRARY_PATH=/home/wucz/demo:.:$LD_LIBRARY_PATH    #添加/home/wucz/demo和当前目录为动态库的搜索路径。
   ```

10. 动态库在编译时，只做语法检查，并没有被编译进程序中。当程序执行到动态库中的函数时，才会动态加载该函数。

## 优缺点

1. 静态库优点：
   1. 静态链接相当于复制一份库文件到可执行程序中，不需要像动态库那样有动态加载和识别函数地址的开销，也就是说采用静态链接编译的可执行程序运行更快。
2. 静态库缺点：
   1. 静态链接生成的可执行程序比动态链接生成的大很多，运行时占用的内存也更多。
   2. 库文件的更新不会反映到可执行程序中，可执行程序需要重新编译。
3. 动态库优点：
   1. 相对于静态库，动态库在时候更新（修复bug，增加新的功能）不需要重新编译。
   2. 全部的可执行程序共享动态库的代码，运行时占用的内存空间更少。
4. 动态库缺点：
   1. 使可执行程序在不同平台上移植变得更复杂，因为它需要为每每个不同的平台提供相应平台的共享库。
   2. 增加可执行程序运行时的时间和空间开销，因为应用程序需要在运行过程中查找依赖的库函数，并加载到内存中。
5. 动态库的不足相对于它带来的好处在现今硬件下简直是微不足道的，所以链接程序在链接时一般是优先链接动态库的