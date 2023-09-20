# 基础

1. make 是linux下的一个工程管理器。make的提出，主要是linux下IDE的缺乏。最初用来管理C程序文件。对于维护一些具有相互依赖关系的文件特别有用。例如程序库依赖.h文件，.c文件，可执行文件依赖库文件等。会根据目标文件和依赖文件的存在与否和时间戳，来决定命令是否执行。确保修改的文件会反映到所有依赖他的目标文件中。

2. Cmake和make不同，它是用来产生各种Makefile或Project（例如vs的.sln工程文件）文件的。

4. 使用make的好处是，可以有序地编译链接工程。修改部分文件后再编译时，只需要编译所有依赖于修改过的文件的文件即可。

5. make工具不仅可以用于编译C，还可以编译任何语言的代码。还可以处理一些自动化任务。

6. C程序编译链接的原则如下，好的Makefile应该做到这一点：

   1. 如果程序从来没被编译过，则所有.c文件都要被编译并链接。
   2. 如果某些.c文件被修改了，则只编译这些被修改的.c文件并链接。
   3. 如果某些.h文件被修改了，则需要编译链接所有include了这些.h文件的.c文件。

7. 一个Makefile开头一般是变量定义，然后就是显式规则，第一个规则的目标约定俗成为all。

8. Makefile文件中主要包含5个部分：

   1. 显示规则：最主要的部分，说明了如何生成一个或多个目标文件

   2. 隐晦规则：make的自动推导功能依赖该规则，由make程序提供，不同的make，隐晦规则可能不同。

   3. 变量定义：变量都是字符串，像C语言的宏，当Makefile被执行时，变量才会扩展为值。

   4. 文件指示：包含了3部分
      1. 在一个Makefile中引用另一个Makefile，像C语言的#include

      2. 根据某些条件，指定某一范围的内容是否有效，像C语言的#ifdef条件编译指令

      3. 定义一个多行的命令

   5. 注释：只有行注释，和shell脚本一样，用#。如果要实际使用#字符，可以用\转义。

9. Makefile中有2种注释，一种是Makefile本身的，会被make识别，它出现在规则的命令部分以外；另一种出现在规则的命令部分中，它会被make直接传递给shell，会被shell识别。

   ```makefile
   #正常注释
   test: #正常注释
   	#shell识别的注释，仍然会回显，可以在前面加上@，取消回显
   	echo 3#由于3和#之间没分开，因此shell不会识别为注释
   	echo 3 #shell会自动舍弃掉echo的第二个参数，等价于echo 3
   	ls #这个注释会被当作注释
   ```

10. 不推荐在命令的同行后面包含注释（此时会被当作命令行参数，例如echo命令同行的注释会被直接当作内容输出），可以单独占一行，并在行首添加@，取消注释的输出，这样更美观。

11. 注释推荐单独占一行，如果要和变量定义赋值放在同一行，则#前不应有额外的空格，否则空格会被当作变量值的一部分，可以利用这种特点来定义值为一个或多个空白字符的变量：

    ```makefile
    #下式=后只有一个空格，因此$(a)为空字符串
    a= 
    #下式)后有一个空格，因此$(b)为空格。如果)后有多个空格，$(b)也会一并接收的
    b= $(a) 
    test:
    	@#下式中$(a)为空字符串，命令为echo xx
    	echo x$(a)x
    	@#下式中$(b)为" "，命令为echo x x
    	echo x$(b)x
    ```

12. 被include引用的Makefile会原样复制到对应位置，这种行为会递归进行，直到不再有include出现：

    ```makefile
    include Makefile.inc b.inc *.in #文件名可以带有shell支持的通配符，include前可以有空格，但是不能以tab开头，include后可以有一个或多个空格，多个被包含的文件用空格分隔
    #当没有指定绝对路径或相对路径时，include 的寻找顺序：
    1.当前目录
    2.make的命令行参数 -I或--include-dir选项的参数
    3./usr/include或/usr/local/include等
    ```

13. 如果有文件没有找到，则会生成一条警告，但是不会立刻报错，会继续载入其他文件，当完成Makefile的读取后，再试图寻找刚才没找到的文件，如果还没找到，则报错。可以在include前加一个-，这样就不会因此报错了。

14. 如果当前shell环境中定义了环境变量MAKEFILES，那么这个变量中的文件名也会被include，这对当前shell下执行的所有make都生效，因此建议不要使用这个环境变量，可能产生意想不到的行为。

    ```shell
    MAKEFILES=a.inc b.inc
    #会被转化为
    include a.inc b.inc
    ```

14. 规则的语法要求如下：

    ```makefile
    targets:prerequisites
    	command #任意shell命令，必须要以tab开头，不能缺少，也不能将tab替换为空格。否则会提示 Makefile:2: *** missing separator.  Stop.
    	... #命令可以有空行，空行上只能包含空白字符
    #或者是
    targets:prerequisites;command #如果命令较短可以和目标写在同一行，不过要用分号分隔。
    	command#这一行仍然有效，但是是一个新的shell
    ```

19. 在shell下输入make，会在shell的当前目录查找makefile文件，顺序依次为：GNUmakefile，makefile，Makefile。因此建议先cd到对应目录，再make。

20. 最好使用Makefile，因为第一个字母大写比较醒目，同时在需要的时候，也可以用户自己编写一个优先级更高的makefile替代。最好不要用GNUmakefile，这个文件只有GNU的make识别。

21. 也有一些带后缀的Makefile，例如Makefile.Linux或Makefile.Solaris用于特定平台，不过他们不会被make自动识别。带后缀的保存有特定于平台的内容，由平台探测脚本探测完平台类型之后，然后由主控Makefile调用对应的文件。

22. 如果没有手动指定目标（make 目标名），则会将文件中的第一个规则的第一个目标作为默认的目标。 

23. 无论是否在make命令行中指定目标，make都会先将make读入的文件名作为目标。如果默认的3个文件名，也没有手动指定文件，则会依次make那三个文件，这里会触发隐式规则，首先寻找GNUmakefile.o。

24. 一般来说，发布的源码包中都是Makefile，这样用户可以手动写一个makefile来替代当前的默认编译设置。

25. 当本次make的最终目标是最新的时，会提示：`make: 'test1' is up to date.`。

26. make程序的选项：

    ```shell
    -f filename #显式指定Makefile的文件
    -C dirname  #指定make程序的当前工作目录
    -e #不允许在Makefile中替换环境变量的赋值
    -k #执行命令出错时，放弃当前目标，继续维护其他目标
    -n #将计划执行的命令(包括用@开头的命令)打印出来，而不真正执行
    -p #显示Make file中所有的变量和内部规则
    -r #忽略内部规则
    -s #执行，但不显示命令，常用来检查Makefile的正确性
    -S #如果执行命令错误就退出
    -t #修改每个目标文件的创建日期
    -I #忽略执行命令时的错误
    -V #显示make的版本号
    ```

27. 使用-d选项来输出更多的细节：

    ```makefile
    test1:test2 test3
    	echo 1
    test2:
    	echo 2
    test3:
    	echo 3
    ####################### 执行make test1 -d后的输出如下
    Reading makefiles...
    Reading makefile 'Makefile'... #读取Makefile文件作为主控文件
    Updating makefiles....
     Considering target file 'Makefile'.  #会首先将主控文件名作为第一个目标，由于不存在一个规则的目标可以匹配该文件名，所以会依次触发所有的隐式规则，每个隐式规则又会作为中间文件，再一次触发隐式规则。
    ...
      No implicit rule found for 'Makefile'. #找不到一个隐式规则可以匹配Makefile
      Finished prerequisites of target file 'Makefile'.
     No need to remake target 'Makefile'.
    Updating goal targets....
    Considering target file 'test1'. #用户的第一个目标
     File 'test1' does not exist. #存在一个显式规则可匹配test1，且test1文件不存在。
      Considering target file 'test2'. #make test1的依赖test2
       File 'test2' does not exist.#存在一个显式规则可匹配test1，且test1文件不存在。
       Finished prerequisites of target file 'test2'.#因为匹配test的规则不存在依赖，所以结束不再调用新的make
      Must remake target 'test2'. #在匹配的test2的规则中，目标不存在，因此要执行命令
    echo 2 #默认会回显将要执行的命令
    Putting child 0x55755bf70b70 (test2) PID 3184 on the chain. #创建一个子进程shell来执行命令
    Live child 0x55755bf70b70 (test2) PID 3184 
    2 #shell命令执行的结果
    Reaping winning child 0x55755bf70b70 PID 3184 #父进程wait子进程结束
    Removing child 0x55755bf70b70 PID 3184 from chain.
      Successfully remade target file 'test2'.
     Finished prerequisites of target file 'test1'.#test目标的依赖处理完成
    Must remake target 'test1'. #test1不存在，因此会执行命令
    echo 1
    Putting child 0x55755bf71300 (test1) PID 3185 on the chain.#创建一个新的子进程shell执行命令
    Live child 0x55755bf71300 (test1) PID 3185 
    1
    Reaping winning child 0x55755bf71300 PID 3185 
    Removing child 0x55755bf71300 PID 3185 from chain.
    Successfully remade target file 'test1'.
    ```

28. 一般都会有个clean目标，用来清除编译产生的中间文件和最终文件，将源代码目录恢复到原来的最开始的情况，一般放在Makefile的末尾。

    ```makefile
    clean:
    	rm -f *.o main  #加上-f选项，使得文件不存在时也不会报错。或者在命令开头加上-，这种方法针对所有的命令都有效
    ```

29. VPATH是一个特殊的变量，如果定义了它，make会当前目录下找不到想要的文件时，会去这个变量的路径列表中按顺序寻找，它的格式和环境变量PATH一样。

    ```makefile
    VPATH = src:../include #包含2个目录 src和../include
    ```

30. 另一个设置寻找目录的方式是，使用vpath关键字，类似于include一样，它比VPATH变量更为灵活。

    ```makefile
    vpath <pattern> <directories> #为符合模式的目标指定搜索目录
    vpath <pattern> #清除为该模式设置的搜索目录，即对该模式文件的搜索只会使用默认的目录
    vpath #清除所有设置的搜索目录
    ```

31. 模式pattern是用来匹配目标的，可以包含%，用来代指任意多个任意字符，可以匹配一类目标，也可以不包含（此时只会匹配一个目标）。例如当前在make abc.o，那么这个目标就会匹配模式%.o。注意和用于搜索文件的*通配符进行区分。

    ```makefile
    vpath test3 include:../include #只为test3目标指定2个搜索目录
    VPATH = include
    ####################
    make test3 #假设include目录下存在test3,同时Makefile中有没有test3匹配的规则，如果不设置vpath，则会报错，说找不到适用于test3的规则，如果设置了vpath，则会提示include/test3不需要更新。
    ```

32. vpath语句可以多次出现，可以重复：

    ```makefile
    #一个目标会按照定义的顺序依次跟所有vpath的模式匹配，直到匹配后，在对应的目录找到了文件。
    vpath %.c foo
    vpath %   blish #所有文件都会去blish中寻找，类似于 VPATH += blish
    vpath %.c bar
    #如果当前寻找a.c目标，则会依次去foo,blish,bar目录中寻找a.c文件。
    ```

33. 可以利用编译器对源代码进行分析，来自动生成依赖性，这样可以再修改源代码后，自动维护依赖性关系：

    ```shell
    gcc -MM main.c #如果main.c中include了defs.h，那么输出如下，如果使用-M，则会将标准库的头文件也包含过来
    main.o : main.c defs.h
    #这个功能还需要处理一下才可以和Makefile结合起来。GNU推荐将编译器为每个源文件生成的依赖关系放到一个同名的.d文件中。这个.d文件也不用用户手动逐个执行gcc -M命令生成，而是构建一个Makefile的规则，自动调用。
    ```

34. 由.c自动生成.d的示例规则：

    ```makefile
    %.d: %.c
    	@set -e; rm -f $@; \
    	$(CC) -MM $(CPPFLAGS) $< > $@.$$$$; \
    	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
    	rm -f $@.$$$$
    #第1个命令前的@表示该命令不会回显到屏幕上，set用于开关shell的某些特性，-e选项表示当如果后续的命令有一个返回值不是0，则退出shell，默认是+e，不退出。
    #第2个命令中$@是自动化变量，表示规则的逐个目标，这一步会删除当前.c文件对应的.d文件。
    #第3个命令用编译器处理.c文件，输出重定向到文件一个中间文件，$<表示规则的逐个依赖。中间文件名为目标文件名再加上一个后缀，$$$$表示4位随机数字。
    #第4个命令是使用sed对上一步输出的中间文件内容进行处理，输出到.d文件中，这里的$$$$会和上一步的保持一致。
    #第5个命令删除中间文件。
    
    #这样就把原来的依赖关系 main.o : main.c defs.h 转化为：
    main.o main.d : main.c defs.h # 这就是main.d文件的内容，这里的规则只有依赖，没有命令
    #然后需要在主控Makefile中加入以下语句：
    sources = foo.c bar.c
    include $(sources:.c=.d)#将字符串source中的.c替换为.d
    ```

35. 整套例子：

    ```makefile
    sources = main.c add.c    #main.c包含add.h，add.c包含add.h 。也可以换成sources=*.o
    main:$(sources:.c=.o) #需要放在include语句之前，这样才会成为make的默认目标
    	gcc -o $@ $^
    include $(sources:.c=.d) #会include main.d和add.d
    %.d: %.c #每次make命令行运行时都会执行include语句，因此会对.d这个目标进行make。
    	@set -e; rm -f $@; \
    	$(CC) -MM $(CPPFLAGS) $< > $@.$$$$; \
    	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
    	rm -f $@.$$$$
    #%.d:%.c规则保证了%.d依赖于%.c，同时include语句将多个.d文件内的规则引入，此时%.d还会依赖.c中#include的头文件。
    ```

36. 某些shell环境下，输入make后，按下tab键，此时就会寻找Makefile中的目标用来命令行不全，此时就会执行include命令，进而生成.d文件。按2下tab键，会以字母顺序显示出本Makefile中所有的目标。

37. 上面的sed例子：

    ```shell
    #引号内的内容用逗号分为5个部分，s表示查找替换，
    sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' #默认从标准输入读取，输出到屏幕。
    #当输入为
    main.o : main.c defs.h
    #输出为
    main.o main.d : main.c defs.h
    ```

38. 条件表达式，关键字和括号之间应有空格分隔，都应和endif配套使用：

    ```makefile
    ifeq ($(a),3)
    ifneq ($(a),3)
    ifdef a#这里只是测试$(a)是否为空，而不是测试$(origin a)是否为undefined
    ifndef a
    #等价的写法，推荐使用括号
    ifeq (<arg1>, <arg2>)
    ifeq '<arg1>' '<arg2>'
    ifeq "<arg1>" "<arg2>"
    ifeq "<arg1>" '<arg2>'
    ifeq '<arg1>' "<arg2>"
    ```

39. 条件判断还有语句，可以用在变量赋值或规则中的命令选择中：

    ```makefile
    a = 3
    test:
    ifeq ($(a),3)
    	echo $(a)#行首的tab不能省略
    else
    	echo $(a)
    endif
    ```


# 命令行参数

1. make执行有3种退出码：

   ```makefile
   0 #表示成功
   1 #表示遇到了错误
   2 #如果指定了-q选项，并且使得某些目标不需要更新，则会返回2。GNU make好像不会输出2
   ```

2. 任何目标都可以指定为命令行参数的终极目标，不在Makefile中的目标都可以被指定，只要能够通过隐式规则推导出来。但是除了以-开头或是包含呢了=的目标，因为前者会被认为是命令行参数，后者会被认为是变量。

3. 变量MAKECMDGOALS会存储make命令行显式指定的目标，如果没有指定则为空字符串。

   ```makefile
   ifdef MAKECMDGOALS
   a = 3
   else
   a = 4
   endif
   test:
   	echo $(a)#如果执行make，则命令为echo 4，如果执行make test，则命令为echo 3
   ```

4. GNU软件自带的Makefile中一般都会有以下伪目标：

   ```makefile
   all #一般是第一个目标，编译所有的代码
   clean #一般是最后一个目标，删除编译产生的任何文件，回复目录到最初状态
   install #安装已编译好的程序，一般是将可执行文件和共享库拷贝到系统的执行目录下
   print #列出修改过的文件
   tar #将当前目录打包，得到.tar文件
   check和test #一般用来测试当前Makefile的流程
   ```

5. 参数：

   ```makefile
   "-n","--just-print","--dry-run","--recon" #只是打印命令，不管目标是否更新，把规则和其下的命令打印出来，但不执行
   "-t","--touch" #把目标的时间更新为当前，但不更改其内容，相当于touch目标文件，假装编译目标。当只是修改了文件的格式时，可以这么做来避免大量重复工作。
   "-q","--question" #不运行命令，也不输出。仅检查所指定的目标是否需要更新。如果是0则说明要更新，如果是2则说明有错误发生。
   "-B","--always-make" #认为所有的目标都需要更新，相当于make clean后在make all
   "-C <dir>","--directory=<dir>" #指定去<dir>目录下寻找Makefile，如果有多个-C参数，则后面路径以前面路径为相对路径，例如make –C ~hchen/test –C prog等价于make –C ~hchen/test/prog
   "--debug[=<options>" #设置调试信息输出的级别，可以是b(basic，最基本的，默认选项), v(verbose，输出依赖相关信息),-i(implicit 输出所有的隐含规则),j(jobs，输出命令的详细信息，包括PID和返回值),m(makefile，输出读取更新执行makefile的信息),a(all，输出所有的信息)
   "-d" #等价于 --debug=a
   "-e","--environment-overrides" #指明环境变量的值将覆盖Makefile中定义的变量的值。
   "-f=<file>","--file=<file>","--makefile=<file>" #指定需要执行的makefile。如果不止一次使用了-f选项，那么多个Makefile都会被make使用
   "-i","--ignore-errors" #执行时忽略所有错误
   "-I <dir>","--include-dir=<dir>" #指定一个include语句的搜索目录。可以多次出现
   "-j [<jobsnum>]","--jobs[=<jobsnum>]" #指定多线程数量。如果没有<jobsnum>，make运行命令时能运行多少就运行多少。一个4核8线程的CPU，最多指定为8。
   "-p","--print-data-base" #输出makefile中的所有数据，包括所有的规则和变量。这个参数会让一个简单的makefile都会输出1200多行。如果指向输出信息，而不执行makefile，可以使用make -qp。如果指向查看make本身的数据，而不是Makefile的，可以使用make -p -f /dev/null，即输入一个空文件。
   "-r","--no-builtin-rules" #禁止使用任何隐含规则。
   "-s","--silent","--quiet" #在命令运行时不输出命令的输出。
   "-w","--print-directory" #输出运行makefile之前和之后的信息。这个参数对于跟踪嵌套式调用make 时很有用。
   "--no-print-directory" #禁止-w选项。
   "--warn-undefined-variables" #只要发现有未定义的变量，那么就输出警告信息。
   ```


# Makefile语法规则

1. make会递归地解析依赖关系（生成一个依赖的树）。例如make xxx这个目标：

   1. 首先在所有的规则中寻找该目标和xxx字符串匹配的规则，如果找到，则会逐个make它的每一个依赖，这一步构成了递归。如果找不到规则时会再检查xxx文件存在与否，如果存在则直接返回，提示`make: Nothing to be done for 'xxx'.`。如果文件仍不存在则报错：`make: *** No rule to make target 'test3', needed by 'test1'.  Stop.`。

   2. 当一个规则的所有依赖的子make调用都正确返回后（此时并不代表依赖的文件都存在了，因为有的规则的命令并不会产生文件），此时要决定该规则的命令是否会执行。
      1. 只要目标或依赖中有一个文件不存在，就会执行规则的命令。

      2. 如果目标和依赖文件都存在，则会比较目标和所有依赖文件的最后修改时间，然后决定是否执行规则的命令。

   3. 这种递归不是尾递归，因为递归调用返回后，还要判定文件的时间。

2. 可以将一条规则看作一个树型结构，根节点是目标（携带有一个数据，就是该规则的命令），然后所有的依赖都是它的子节点，按顺序排列。make根节点时，会依次make子节点，最后再执行根节点的命令。当make子节点时，会在所有的树（也就是规则）中寻找最匹配的根，然后根据该树进行make。

3. 如果检查到一个目标本身不存在时，仍然会检查其依赖，不过无论如何，该规则的命令都会执行，因为不存在的目标的最后修改时间回比任何依赖的最后修改时间都早。

4. make一个目标时，存在以下几种情况，该目标对应的文件是否存在，该目标对应的显式规则是否存在，一共分为4种情况：

   1. 文件和显式规则都没有：错误提示，没有找到匹配目标的规则。

   2. 文件存在，显式规则不存在：正确提示，该目标不需要更新。

   3. 文件不存在，显式规则存在：按照规则进行处理依赖，如果没有遇到错误，最终一定会执行命令。

   4. 文件和显式规则都存在：按照规则进行处理依赖，不一定会执行命令。

5. 如果一个目标没有依赖时，当目标文件存在时（总认为它是最新的），不执行命令，否则会执行命令。

6. 因此，如果修改了kbd.c文件，make all的时候，会检查到kbd.o这个目标的依赖kbd.c比目标更新。会先执行kbd.o的命令，再执行all的命令。

   ```makefile
   #源文件包括8个.c和3个.h
   all:main.o kbd.o command.o display.o insert.o search.o files.o utils.o
   	gcc -o all main.o kbd.o command.o display.o insert.o search.o files.o utils.o
   main.o:main.c defs.h
   	gcc -c main.c
   kbd.o:kbd.c defs.h command.h
   	gcc -c kbd.c
   command.o:command.c defs.h command.h
   	gcc -c command.c
   display.o:display.c defs.h buffer.h
   	gcc -c display.c
   insert.o:insert.c defs.h buffer.h
   	gcc -c insert.c
   search.o:search.c defs.h buffer.h
   	gcc -c search.c
   files.o:files.c defs.h buffer.h command.h
   	gcc -c files.c
   utils.o:utils.c defs.h
   	gcc -c utils.c
   clean:
   	rm all main.o kbd.o command.o display.o insert.o search.o files.o utils.o
   ```

7. 最终目标依赖于各种中间文件，中间文件依赖于源文件和头文件。C语言中，分为编译和链接，编译的时候，只需要源文件和头文件（include在源文件中的）。链接时候要寻找各种函数的中间文件和库。一般有多少个.c文件就有多少个.o的目标。最后需要将这些个.o用ar打包成为一个静态库.a、用链接器打包成动态库.so或用链接器产生最终可执行程序。

8. 一般情况下，每一个.c文件都是有.h对应的，来记录它里边函数的声明，这个头文件会包含在自己的.c和所有使用到该.c中函数的.c中。例如a.c使用到了于b.c中的函数，b.c的声明在b.h中，因此a.c会包含 b.h。如果要修改b模块中函数的接口，那么b.c和b.h都要修改。由于b.c默认会包含b.h，所以推荐a.c依赖b.h，而非b.c。

9. 还有一些是公共的头文件，即找不到对应的.c，例如上例子中的def.h。其中可能定义一些枚举量，或者是第三方库（以.so的方式给出）的头文件。

10. 规则中的目标可以有多个，用空格分开。可以使用通配符来构成模式规则，这种规则可以匹配多个目标名。一条命令一行写不完可以加\换行，make对一行的长度没有限制。一个规则的命令可以有多条。

11. 如果要生成多个可执行文件，则可以这样写：

    ```makefile
    all : main1 main2
    main1 : main.c
    	command
    main2 :main2.c
    	command
    ```

12. Windows下的用户没有宿主目录，~根据环境变量HMOE确定。

13. Makefile支持三种通配符（功能和shell的一样），他们代表了一群满足条件的文件（也会尝试.和..），可以用在变量定义，命令和依赖中：

    ```makefile
    *  #≥0个任意字符
    ?  #任意单个字符
    [...] #[]内的任意一个字符，例如[a-z]表示任意小写字母
    
    objects = *.o #变量为当前目录中所有.o文件的集合
    clean:
    	rm -f *.o #删除当前目录下所有.o文件
    print:*.c #print依赖于当前目录下所有的.c文件
    	lpr -p $?
    	touch print
    ```

14. 通配符出现的位置，并不会立即展开，搜索满足条件的文件进行替换，而是等到实际要使用通配符时，才会展开，也可以手动强制立即展开：

    ```makefile
    objects := *.o       #这里的.o并不会就地展开。类似于C语言中的宏。
    objects = $(wildcard *.o)    #此时会强行让*.o就地展开为当前目录下以.o结尾的文件，只有实际存在的文件才有用。
    objects := $(wildcard *.o) #如果在此后其他命令产生了新的.o文件，则不会包含进来
    ```

15. 如果想在文件名中包含实际的通配符符号，则使用\转义。

16. 后缀规则和模式规则的功能类似，都可以表示该规则适用于一类目标或需要一类依赖。使用"模式规则"会更智能，清除，但"后缀规则"可以用来保证Makefile的兼容性。

    ```makefile
    .c.o : #和%o:%c相同
    	command
    ```

17. 后缀规则有两种，单后缀和双后缀。后缀规则不允许有任何依赖，否则不是后缀规则。后缀规则的后缀应该是make所识别的：

    ```makefile
    .c.o: #双后缀，相当于%o:%c
    	command
    .c: #单后缀，相当于%:%.c
    	command
    .c.o: foo.h #表示.c.o文件依赖于foo.h文件，而不是%.c:%.o foo.h。
    	command
    ```

18. 后缀规则如果没有命令，则毫无意义，因为它不会去移除内建的隐含规则。

19. 可以使用.SUFFIXES目标来定义make所识别的后缀，可以用“.SUFFIXES”来改变后缀列表，但不要改变变量“SUFFIXE”的值。

    ```makefile
    .SUFFIXES: .hack .win #把后缀.hack 和.win 加入后缀列表中的末尾
    .SUFFIXES: # 删除默认的后缀
    .SUFFIXES: .c .o .h # 定义自己的后缀
    ```

20. 所有的后缀规则在Makefile 被载入内存时，会被转换成模式规则。

21. 静态模式可以更容易地定义多目标的规则，语法为：

    ```makefile
    <targets ...> : <target-pattern> : <prereq-patterns ...>
        <commands>
    #第一部分定义了一系列目标，第二部分指明了这些目标的模式，第三部分指明了依赖的模式。例如
    objects = foo.o bar.o #变量定义
    $(objects): %.o: %.c #依赖的集合为foo.c bar.c
    	$(CC) -c $(CFLAGS) $< -o $@
    #上面的规则会被拆分为2个单一目标，单一依赖的规则
    foo.o : foo.c
    	$(CC) -c $(CFLAGS) foo.c -o foo.o
    bar.o : bar.c
    	$(CC) -c $(CFLAGS) bar.c -o bar.o
    ```

22. 如果同时又很多的.c都要编译成.o文件，使用静态模式会大大提高效率。

23. 一般来说，一个模式可能有一个前缀或后缀是%，或者没有前后缀，就一个%。%所匹配的内容成为茎stem，目标和依赖同时存在%时，茎会传递。当目标存在/时，目录的部分会首先移动开，进行匹配，成功后，再将目录部分添加上：

    ```makefile
    ab.o #可以匹配 %.o，其中%为ab
    ab.o #可以匹配ab.%，其中%为o
    src/eat #可以匹配e%t，%为src/a，如果依赖模式为x%y，则依赖为src/xay
    ```


# 伪目标

1. 根据规则中目标对应的命令是否会真正生成该目标，将目标分为普通目标和标签目标。一般来说标签目标都表示一件具体的事情，例如install表示安装，clean表示删除。

2. 推荐将所有的标签目标设置为伪目标。原因：当make这些标签目标时，就是想最终执行命令。然而可能会有文件和该目标重名，导致make认为该目标不需要更新，因而不执行命令。

3. 当一个目标被定义为伪目标后，make它时，不会检查文件是否存在，总是认为目标文件不存在，因此命令总会被执行。

4. 和普通目标相同的时，伪目标也可以有依赖，make它时，仍然会依次make它的依赖。但是不会再检查目标和依赖的时间了，因为始终认为目标不存在。

5. 使用.PHONY关键字显式地指定当前目标为伪目标，大部分的伪目标都没有依赖，all目标有时例外：

   ```makefile
   .PHONY:clean all #本行的位置无所谓
   all:program1 program2#这条规则不需要命令
   clean:
   	rm -f *.o
   ```

6. Makefile支持依赖于相同文件的多目标。会被拆分为多个单目标的规则，注意不会将多个依赖也一并拆分。

   ```makefile
   bigoutput littleoutput:text.g
   	generate text.g -$(subst output,,$@)>;$@ #这里可以使用自动化变量来分离出来每个目标和每个依赖
   #等价于
   bigoutput:text.g
   	generate text.g -big >;bigoutput
   littleoutput:text.g
   	generate text.g -little >;littleoutput
   ```

# 命令

1. $()表示执行一个Makefile的函数。 \$@表示目标集合的迭代类型。

2. make会一条一条地执行命令，忽略空行。但是如果是以tab开头的空行，则认为是一个空命令（啥也不做）

3. make通常会把要执行的命令回显到屏幕上，然后再执行，可以在命令开头处加上@来取消回显。echo语句一般都会加上@。

4. 默认每条命令都是独立的环境（会使用SHELL变量，该变量可以在make使用命令行参数传入，也可以在Makefile中用SHELL=修改），如果需要上一条命令的结果作用于下一条命令，则应把这两个命令写在同一行上，使用分号分隔这两个命令。

   ```makefile
   test1:
   	cd /root #逐条执行命令，分别产生shell子进程
   	pwd
   test2:
   	cd /root;pwd #输出为/root。通过命令行参数-d可以看到，这两条命令被一起提交给shell的
   ```
   
5. 每条命令执行完毕后，make都会检测它的返回码，如果出现错误，则终止当前规则，否则执行吓一跳命令，如果整个规则的所有命令都不出错，则该规则成功运行。一个规则出错，会直接退出，其后续的规则也不会执行。

6. 不过有时候命令报错不重要或不代表真实出错，还希望继续执行后面的命令。可以在命令最前面加上一个-减号，忽略该行命令的错误。还可以为make命令加上-i或--ignore-errors参数，这样相当于所有命令前都有一个-。还有一个命令行参数-k或--keep-going，这个参数表明遇到错误时，仅终止该规则的后续命令执行，但是不影响其他规则。

   ```makefile
   exec:
   	- cd /home/zj  #进入/home/zj目录，并忽略错误
   	pwd            #打印当前目录
   ```
   
7. 命令中若要使用shell的\$符号，要用$$来转义。

   ```makefile
   SHELL = /bin/zsh
   test:
   	echo $$SHELL #这条语句为echo $SHELL，会由/bin/zsh执行，输出的SHELL环境变量，也是zsh配置文件中定义的
   ```

8. 如果经常要使用到某些命令序列，可以将他们定义为一个命令包，define还可以定义变量，字符串等。

   ```makefile
   define run-command #run-yacc为包名，不应和变量重名。命令序列就以下3行,可以包含自动化变量。
   cd ~;pwd
   pwd
   echo $@
   endef
   #像使用变量一样
   test:
   	$(run-command)
   ```

# 嵌套make

1. 大工程的源码应该按照功能分别存放在不同的文件夹中，因此每个文件夹中都应该有自己的Makefile，子文件夹的Makefile只负责处理本文件夹下的文件。根目录下的Makefile被称为主控文件，负责依次调用子目录下的Makefile。

   ```makefile
   #例如有一个文件夹subdir，模块为subsystem，其中有一个Makefile，指明了该目录下文件的规则，那么在总控Makefile中可以这样写：
   .PHONY : subsystem #定义为一个伪目标
   all : subsystem #由all统一生成
   subsystem:
   	cd subdir && $(MAKE) #当&&前面的命令正确执行后，才会执行其后的命令。使用MAKE变量可以让多个子文件夹的命令行参数统一。
   #subsystem规则也可以写为：
   subsystem:
   	$(MAKE) -C subdir
   ```

2. 总控Makefile的变量可以使用export命令传递到下级的Makefile，但是不会覆盖同名的，除非制定了-e参数。

   ```makefile
   export <variable ...> #也可以使用unexport <variable ...>来阻止某些变量传递到下级
   export variable = value #等价于variable = value和export variable这两句。:=和+=同样。
   ```

3. SHELL和MAKEFLAGS（包含了make的命令行参数）这两个变量比较特殊，不论是否export，都会传递到下级

   ```shell
   make test -j abc=3 # MAKEFLAGS的值为"-j -- abc=3"
   #并非所有的make命令行参数都会记录到MAKEFLAGS中，例如 -C -f -h -o和-W。
   #如果不想往下级传递make的命令行参数，可以将MAKEFLAGS赋值为空
   $(MAKE) MAKEFLAGS=
   ```

4. 嵌套调用时，上层Makefile中变量会以系统环境变量的方式传递到下层的Makefile 中。默认情况下，只有通过命令行设置的变量会被传递。而定义在文件中的变量，如果要向下层Makefile 传递，则需要使用exprot 关键字来声明。

5. SHELL和MAKEFLAGS变量也可以从shell的环境变量继承而来。不过不推荐设置MAKEFLAGS，因为他会对所有的make调用都生效，可能引发意外情况。

6. 还有一个在嵌套make时比较有用的选项，-w或--print-directory，它会使得make在每一次进入或离开子目录时打印提示。当使用-C进入子目录make时，-w是自动打开的。如果打开了-s或--silent或--no-print-directory选项，则不-w总是失效：

   ```shell
   make: Entering directory `/home/hchen/gnu/make'.
   make: Leaving directory `/home/hchen/gnu/make'.
   ```

7. 变量MAKELEVEL在嵌套Makefile时可以用来指示当前Makefile所处的层级。主控Makefile的MAKELEVEL为0。

# 变量

1. 对于变量，make会采用延迟展开，如果变量出现在规则中，只有这条规则被启用了，才会展开为值。

2. Makefile中的变量和C中的宏一样，代表了一个字符串。在Makefile执行的时候，会自动展开。变量可以使用在目标，依赖，命令等地方。

   ```makefile
   #定义一个变量，内容为"a.o b.o"
   objects = a.o b.o
   #使用变量,会在执行命令前将变量展开
   test:
   	echo $(objects)
   ```

3. 变量赋值时，只会把等号右侧的前导空格去掉，末尾的不会：

   ```makefile
   a = b#$(a)的值为"b"
   c = d #$(c)的值为"d "，这里有没有注释都是一样的，字符串的右边界以#或行尾为标记。
   test:
   	echo x$(a)x
   	echo x$(c)x
   ```

4. 变量名是大小写敏感的（这一点和shell一样），可以以数字开头，但不推荐，不应包含:#=和空格等。在声明时要赋予予初值。使用$在变量名前引用变量。不过最好加上()或{}。如果要使用真正的\$，则输入\$\$。shell不支持使用括号，但是支持不加括号或使用大括号。

5. 推荐使用首字母大写的方式来给变量命名，这样不会和系统的环境变量重复，也利于快速识别。

6. 变量值中的通配符不会被识别为本来的字符，如果需要使用本来的字符，可以用\转义

   ```makefile
   abc = *.c #不会立即在当前目录中搜索.c后缀的文件，如果变量用于命令中，则始终不展开，交由执行命令的shell展开，如果用于其他情况，则由make负责在使用到的地方再展开
   test:
   	echo $(abc) #会执行echo *.c
   ```

7. 可以使用其他变量的值来定义一个变量的值：

   ```makefile
   foo = abc
   bar = $(foo)#bar变量的值为字符串"$(foo)字符串"，但不会立即展开为abc
   ugh = $(bar)
   #如果再这里加上一个bar = 123，则第6行执行的命令为echo 123
   test:
   	echo $(ugh)  #在此时ugh变量会一直展开到底，得到它的值abc，因此会执行命令echo abc
   ```

8. 也可以将一个变量的值再当作变量使用：

   ```makefile
   x = y
   y = z
   a := $($(x))#$(x)为y，所以$($(x))为$(y)为z
   #注意这两句的区别
   x = $(y)
   y = z
   a := $(x)#x=z，所以$(x)为z
   ```

9. 甚至可以用变量的值来定义另一个变量的名字：

   ```makefile
   dir = foo
   $(dir)_sources := 123
   test:
   	@# $(foo_sources)为123
   	echo $(foo_sources)
   ```

10. 给变量赋值可以使用=或：=。:=表示只使用它之前定义过的变量，使用=定义的变量和传统的编程语言不一样。因此推荐先定义变量后使用，或者一律使用:=。

11. ```makefile
    x := $(y) bar#因为这之前没有定义y变量，所以此时$(y)为空字符串，因此$(x)为" bar"，而不是"foo bar"。
    y := foo
    
    a = $(b) bar#a的值不会就地展开。
    b = foo
    b = new
    
    test:
        @#执行命令为echo  bar
        echo $(x)
        @#执行命令为echo new bar
        echo $(a)
    ```

12. 变量定义还有一个有用的操作符   ?=   含义是如果先前没有定义过该变量，则定义并赋值，如果定义了则不做任何事情。类似于C语言的ifdef。

12. ```makefile
    FOO ?= bar
    等价于如下代码：
    ifeq($(origin FOO),undefined)#ifeq 为条件判断语句，origin函数返回FOO的出处。
    	FOO = bar
    endif
    
14. 可以使用+=为变量追加值。

15. ```makefile
    objects = main.o foo.o bar.o
    objects += another.o # $(objects)为"main.o foo.o bar.o another.o"等价于以下语句
    objects :=$(objects) another.o
    ```

16. +=根据前一次的赋值操作符来区分=和：=。没有+:=或:+=符号。

    ```makefile
    variable := value
    variable += more#使用+=就可以避免出现递归赋值。且如果变量之前没有定义过，会自动变成=
    #等价于:
    variable := value
    variable := $(variable) more#但是第二句不能使用=，因为这样会发生关于variable的递归赋值，第一句=和:=没有区别。
    
    variable = value
    variable += more#这里并不会发生递归赋值，make会自动处理好
    ```

17. 没有-=和-运算：

    ```makefile
    objects = a.o b.o
    objects -= b.o#会报错，Makefile:2: *** missing separator.  Stop.
    objects := $(objects) - b.o#$(objects)会变成"a.o b.o - b.o"，4项。
    ```

18. 变量后缀字符串替换：

    ```makefile
    foo := a.o b.o c.o d.f90
    bar := $(foo:.o=.c)#将foo变量的每一项的末尾.o替换为.c，如果某项结尾不匹配，则结果该项不变。结果$(bar)为"a.c b.c c.c d.f90"
    
    x = a ab ba
    y = $(x:a=c)#结果$(y)为"c ab bc"，而不是"c cb bc"。因此不是整体搜索替换
    ```

19. 另一种变量替换的方法是以“静态模式”定义的，效果和上面的后缀替换一样：

    ```makefile
    foo := a.o b.o c.o d.f90
    bar := $(foo:%.o=%.c)#foo中的每一项都会和%.o去匹配，成功的话，替换为%.c，两个%的内容相同。
    ```

20. 包含多项的变量，在替换后会把项中间多余的空白变成一个空格，变得规整。

    ```makefile
    foo = a.o b.o   c.o# $(foo)为"a.o b.o   c.o"
    bar = $(foo:.o=.c)# $(bar)为a.c b.c c.c
    ```

21. 如果通过命令行传递进来了某个变量，那么在Makefile内对该变量的修改不会生效，但是如果想要在Makefile中对其进行修改，可以使用override指示符，override后面可以是=或:=，它也可以和define共同使用：

    ```makefile
    a = 2
    override b = 2
    test:
    	echo $(a) $(b)
    #######若命令行为 make a=3 b=3，那么命令为echo 3 2
    ```

22. 执行make时，还会将shell的环境变量带入，不过他们的优先级比较低，会被Makefile中的同名变量覆盖，如果想要不被覆盖，可以使用make -e：

    ```makefile
    COLORTERM = 3#shell中存在同名的环境变量，env|grep COLORTERM 为 COLORTERM=truecolor
    test:
    	echo $(COLORTERM)#此时直接make，会echo 3，如果make -e，会echo truecolor
    ```

23. 可以通过命令行参数来向Makefile中传递变量，例如

    ```makefile
    test:
    	echo $(abc)
    #执行以下语句
    make abc=3 #会执行echo 3，输出3
    ```

24. 变量定义位置影响其优先级：命令行最高，其次是Makefile中的，最后是程序环境变量中的（一般有shell带来）。make -e和override指示符可以调整优先级。

25. 一般情况下不推荐额外设置make的变量在环境变量中，这会影响所有的make执行。

26. 以上设置的默认都是全局变量，会对所有的使用到该变量的地方生效。还有一种是目标变量，仅会对某个目标将其引发的后续目标生效：

    ```makefile
    CFLAGS = -O2
    test1 : CFLAGS += -g
    test1 : test2
    	echo $(CFLAGS)
    test2 : 
    	echo $(CFLAGS)
    test3 :
    	echo $(CFLAGS)
    #make test1时，会执行2次echo -O2 -g
    #make test2时，会执行1次echo -O2
    #make test3时，会执行1次echo -O2
    ```

27. 模式变量类似于目标变量，不过他是通过模式来指定一堆目标的：

    ```makefile
    %.o : CFLAGS = -O#对所有匹配%.o模式的目标及其引发的后续目标都生效
    ```

# 函数

1. 使用\$( )或\${ }来调用函数，返回值可以当做变量来使用。先是函数名，后面为参数。函数名和参数之间用空格分隔，参数之间用逗号分隔。为了风格的统一，()和{}的使用，应该统一。

2. 循环被当做一个函数foreach：

3. ```makefile
   $(foreach <var>,<list>,<text>)
   #功能：将<list>中的单词逐一取出，放到<var>(临时变量名，作用域只在函数内)中，执行<text>中的表达式。最终返回一个包含各循环中<text>表达式字符串，空格分隔。list也可以是个表达式。text中使用$(var)引用循环变量的值。
   names := a b c d
   files := $(foreach n,$(names),$(n).o)#结果为"a.o b.o c.o d.o"
   ```

4. 条件判断函数if：

   ```makefile
   $(if <condition>,<then-part>)#如果conditiono为非空字符串，则表达式为真。
   #或者:
   $(if <condition>,<then-part>,<else-part>)
   ```

5. 创建一个新的参数化函数，同时直接调用：

   ```makefile
   $(call <expression>,<parm1>,<parm2>,<parm3>...)
   #功能：<param1>等是函数的实参，会依次传递给<expression>中的$(1)等形参，表达式的结果就是函数的返回值。
   #例子：
   reverse = $(2) $(1)
   foo = $(call reverse,a,b)#结果为"b a"。call的第一个参数需要是一个变量名，不能将$(2) $(1)直接填入到call的第一个参数。
   ```

6. 获得变量的来源，有时希望判断命令来自何处，进而做出不同的操作：

   ```makefile
   $(origin <variable>)
   #功能：获得变量<variable>的来源，可能为undefined(从来没被定义过)，default(make自带的，例如CC)，environment(来自进程环境变量，并且make时没有打开-e选项)，file(在Makefile中定义)，override(被override指示符重新定义了)，automatic(命令运行中的自动化变量)
   #例子：
   a = 
   b = 3
   #make时，输出file file undefined，可见值为空字符串和未定义变量的不一样。当make c=4，输出为file file command line
   test:
   	echo $(origin a) $(origin b) $(origin c)
   ```

7. 执行shell命令，不太推荐使用，因为会单独开启一个shell进程执行，性能开销大：

   ```makefile
   $(shell <command>)
   #功能：
   #例子：
   contents = $(shell ls -a)
   test:
   	echo $(contents)#等价于echo . .. add.c add.h main.c Makefile testf.f90 .vscode
   ```

8. 错误和警告函数：

   ```makefile
   $(error <text ...>)
   $(warning <text ...>)
   #产生一个致命错误或警告，<text>是信息。error会让make退出，warning只是输出一段警告信息，然后继续执行。
   ```

9. 字符串操作函数分两大类，有的会将待操作的数据看作多个单词（单词由空格和tab分隔），有的会将其看作1个整体字符串。

10. 字符串替换函数subst，将待替换的字符串当作一个整体，而不是处理其中的单词。

    ```makefile
    $(subst <from>,<to>,<text>)
    #功能:把字符串<text>中的<from>字串，替换成<to>字符串
    #返回：被替换过后的字符串
    
    #例子，将字符串"a b c"中的空格替换为,结果为"a,b,c"
    empty =#$(empty)为空字符串
    space = $(empty) #这里定义$(space)为一个空格
    comma = ,#不能再subst中直接输入逗号作为参数，因为这会和参数的分隔符混淆
    foo := a b c
    bar :=$(subst $(space),$(comma),$(foo))
    ```

11. 模式字符串替换patsubst：

    ```makefile
    $(patsubst <pattern>,<replacement>,<text>)
    #功能：查找text中的单词（以空格，tab分隔），然后将符合模式的单词进行替换。%传递通配内容。
    #返回：被替换过后的字符串
    
    #例子：将字符串"x.c.c bar.c"变为"x.c.o bar.o"
    $(patsubst %.c,%.o,x.c.c bar.c)
    #目标字符串可以分为两个单词，x.c.c和bar.c，二者都匹配%.c的规则，因此替换为:
    x.c.o bar.o
    
    #还有一种后缀写法：
    $(var:<suffix>=<replacement>)#和$(patsubst %<suffix>,%<replacement>,$(var))
    #例子
    objects = a.o b.o
    test:
    	echo $(objects:.o=.c)#等价于echo $(patsubst %.o,%.c,$(objects))
    	#后缀也可以有%，结果相同
    	echo $(objects:%.o=%.c)
    ```

12. 字符串查找函数：

    ```makefile
    $(findstring <find>,<in>)
    #功能：在字符串<in>中查找<find>字符串
    #返回：如果找到，则返回<find>字符串，否则返回空字符串
    
    #例子
    $(findstring a,a b c)     返回"a"
    $(findstring a,b c)       返回空字符串""
    ```

13. 过滤函数：

    ```makefile
    $(filter <pattern...>,<text>)
    #功能：过滤<text>中的单词，保留符合模式<pattern...>的单词,可以有多个模式
    
    #例子：
    $(filter %c %s,foo.c bar.c baz.s ugh.h)
    text中有4个单词，pattern中有2个模式，依次匹配。fooc. bar.c baz.s符合，其余的都去掉。按顺序输出即可。
    fooc. bar.c baz.s
    ```

14. 反过滤函数：

    ```makefile
    $(filter-out <pattern...>,<text>)
    #功能：过滤<text>中的单词，去除符合模式<pattern...>的单词,可以有多个模式
    #例子
    $(filter %c %s,foo.c bar.c baz.s ugh.h)  只有ugh.g该单词不符合模式。
    ugh.h
    ```

15. 排序函数：

    ```makefile
    $(sort <list>)
    #功能：将字符串<list>中的单词按照字母升序排列，会自动去重
    #例子
    $(sort lose foo bar lost)
    bar foo lose lost
    ```

16. 按位置取单词：

    ```makefile
    $(word <n>,<text>)
    #从字符串<text>中取出第<n>个单词，计数从1开始，如果<n>超过了最大单词数量，则返回空字符串
    #例子
    $(word 2,programing linux c)
    linux
    ```

17. 取连续多个单词：

    ```makefile
    $(wordlist <s>,<e>,<text>)
    #功能：从字符串<text>中取出第<s>到第<e>个单词构成的串，两侧都是闭区间，如果<s>超过了最大单词数量，则返回字符串，如果<e>超过了最大单词数量，则取到最后一个单词。
    #例子
    $(wordlist 2,4,I like linux c programming)
    like linux c
    ```

18. 统计单词个数：

    ```makefile
    $(words <text>)
    #功能：统计字符串<text>中的单词个数
    #例子
    $(words I like linux c programming)
    5
    ```

19. 获取首个单词：

    ```makefile
    $(firstword <text>)
    #功能：获取字符串<text>中的首个单词，等价于$(word 1,<text>)
    #例子
    $(firstword I like linux c programming)
    I
    ```

20. 取路径的目录部分：

    ```makefile
    $(dir <names...>)
    #功能：从路径中取出目录部分，即最后一个/之前的部分，包括/。names可以有多个路径
    #例子
    $(dir usr/src/linux-2.4/Makefile hello.c include/bit/)
    usr/src/linux-2.4/ ./ include/bit/
    ```

21. 取路径的文件名部分：

    ```makefile
    $(notdir <names...>)
    #功能：从路径中取出非目录部分，即最后一个/之后的部分，不包括/。names可以有多个路径
    #例子
    $(notdir usr/src/linux-2.4/Makefile hello.c include/bit/)#最后一项被转化为空字符串
    Makefile hello.c
    ```

22. 取后缀部分：

    ```makefile
    $(suffix <names...>)
    #功能：从路径中取出后缀名，即点后的部分
    #例子：
    $(suffix usr/src/linux-2.4/Makefile hello.c foo.s)#第一项被转化为空字符串
    .c .s
    ```

23. 取前缀部分：

    ```makefile
    $(basename <names...>)
    #功能：从路径名取出文件名的前缀部分
    #例子：
    $(basename usr/src/linux-2.4/kernel/exit.c hello.o home/hacks .c)#最后一项被转化为空字符串
    usr/src/linux-2.4/kernel/exit hello home/hacks
    ```

24. 链接前后缀：

    ```makefile
    $(join <list1>,<list2>)
    #功能：将<list1>和<list2>的对应单词连接起来，如果单词数量不一样多，则用空字符串替代。
    #例子：
    $(join a b , 1 2 3)#结果为"a1 b2 3"
    ```

25. 增加后缀：

    ```makefile
    $(addsuffix <suffix>,<names...>)
    #功能：把后缀<suffix>添加到<names...>中的每个单词后面
    #例子：
    $(addsuffix .c,foo bar hello)
    foo.c bar.c hello.c
    ```

26. 增加前缀：

    ```makefile
    $(addprefix <prefix>,<names...>)
    #功能：把后缀<suffix>添加到<names...>中的每个单词的前面，不会将单词当作路径来特殊处理
    #例子
    $(addprefix include/,exit.c time.c bit/stdio.h)#第一个参数如果没有/，结果也不会自动补全/。最后一项也不会变成bit/include/stdio.h
    include/exit.c include/time.c include/bit/stdio.h
    ```

27. 去前后空白：

    ```makefile
    $(strip <string>)
    #功能：去掉<string>字符串前后的空白字符，当作一整个字符串处理
    #例子：
    test:
    	echo $(strip a b c )#一个参数为"a b c "，结果为"a b c"
    ```

# 隐式规则和默认变量

1. 根据Linux内核makefile的经验，不建议使用任何隐式规则，最好全部使用显式规则，这样避免make进行错误或意想不到的自动推导。

2. make一个目标时，会根据隐式规则来自动推导目标名称的依赖和命令。每一条隐含规则都在库中有其顺序，越靠前的则是越被经常使用的，所以，这会导致我们有些时候即使我们显示地指定了目标依赖，make也不会管。

   ```makefile
   foo.o : foo.p #如果该规则没有命令，则表示在隐式规则推导foo.o时，存在这么一条路径。当目录中存在.c文件，那么foo.o:foo.c的规则更靠前，会无视这个规则。
   #因此，如果不希望任何隐含规则的推导，那就不要出现没有命令的规则
   ```

3. 隐式规则：make程序预先约定好了的，不用在makefile中写出来的规则。隐式规则会使用一些系统变量，例如系统变量CFLAGS可以控制编译器的参数。例如：

4. ```makefile
   foo:foo.o bar.o
   	cc -o foo foo.o bar.o $(CFLAGS) $(LDFLAGS)
   ################################
   #上一条规则有2个依赖foo.o和bar.o，如果在makefile中找不到和foo.o匹配的规则，则make会根据隐式规则自动推导他们的依赖目标和命令如下：
   foo.o:foo.c
   	$(CC) $(CFLAGS) -c foo.c
   bar.o:bar.c
   	$(CC) $(CFLAGS) -c bar.c
   ```

5. 事实上，.o文件不仅依赖于.c，还依赖于.h头文件，make的自动推导只会依赖于.c。

6. 不带命令的规则：

   ```makefile
   #如果仅有下面一行，而main.o的下一行不是以tab开头，则该行不表示一个规则，而是表示一个依赖附加关系，即在自动推导main.o的规则时，会把defs.h当作依赖添加上。
   main.o:defs.h
   #如果main.o的下一行是以tab开头的，即使tab后没有命令，也被认为是一个空命令，此时该行被当作一个main.o的规则，此时不会再触发自动推导。
   main.o:defs.h
   	#有一个tab
   ```

7. make的目标和普通规则匹配时，仅需要和规则的目标匹配即可。如果和隐式规则匹配时，还需要保证其依赖的文件也存在才可以正确匹配。例如：

   ```makefile
   test1:test2
   	echo 1
   #make test1时，可以发现上面的规则的目标就是test1，因此可以匹配。而make test2时，找不到显式规则，因此开始寻找隐式规则，有很多条都可以匹配，例如从n.o，n.c或n.f生成n等，因此会寻找n.o，n.c，n.f这些文件是否存在，经过一番查找后，如果找不到，那就报错。
   ```

8. 目标可以被一系列隐含规则构成的链作用，例如.o文件依赖于.c，.c文件依赖于.y文件。如果.c文件存在，则直接调用C编译器编译它，如果.c不存在，而.y文件存在，则会先调用yacc生成.c文件，再调用C编译器生成.o文件。此时.c文件就是中间目标，最后会被自动删除，看起来像是从.y一步生成了.o文件。

9. 在"隐含规则链"中，禁止同一个目标出现两次或两次以上，这样一来，就可防止在make自动推导时出现无限递归的情况。

10. make会优化某些特殊的隐含规则，而不生成中间文件，例如从foo.c生成foo，会选择一步编译链接完成，而不是先生成foo.o，再连接生成foo文件。

11. 通常，一个被makefile 指定成目标或是依赖目标的文件不能被当作中间目标。然而，你可以明显地说明一个文件或是目标是中介目标，你可以使用".INTERMEDIATE ： mid"来强制声明。

12. 也可以阻止 make 自动删除中间目标，要做到这一点，可以使用".SECONDARY : sec"来强制声明。

13. 还可以把你的目标，以模式的方式来指定（如：%.o）成“.PRECIOUS”的依赖目标，以保存被隐含规则所生成的中间文件。

14. 隐式规则的命令中基本都使用了预先设置的变量，也可以使用 make -r或--no-builtin-variables来取消预定义变量对隐式规则的作用。

    ```makefile
    CC = cc
    #CFLAGS，CPPFLAGS，TARGET_ARCH均为未定义
    COMPILE.c = $(CC) $(CFLAGS) $(CPPFLAGS) $(TARGET_ARCH) -c
    OUTPUT_OPTION = -o $@
    %.o: %.c
    	$(COMPILE.c) $(OUTPUT_OPTION) $<
    ###################################
    #LDFLAGS，LOADLIBES，LDLIBS均为未定义
    LINK.o = $(CC) $(LDFLAGS) $(TARGET_ARCH)
    %: %.o
    	$(LINK.o) $^ $(LOADLIBES) $(LDLIBS) -o $@
    ```

15. 实际上，即使制定了-r选项，某些隐含规则还是会生效的，因为许多隐含规则都是使用了后缀规则来定义的。所以只要对应的后缀名在后缀列表（定义在目标.SUFFIXES的依赖中）中存在，那么对应后缀名的隐含规则就会生效。

    ```makefile
    #默认的后缀列表为：
    SUFFIXES := .out .a .ln .o .c .cc .C .cpp .p .f .F .m .r .y .l .ym .yl .s .S .mod .sym .def .h .info .dvi .tex .texinfo .texi .txinfo .w .ch .web .sh .elc .el
    #可以将SUFFIXES变量置为空，来使得后缀规则失效。
    ```

16. 可以取消或者定义一个全新的内建的隐式规则：

    ```makefile
    %.o: %.c
    	$(CC) –c $(CPPFLAGS) $(CFLAGS) -D$(date)#定义一个全新，覆盖默认的隐式规则
    %.o: %.cc
    #取消特定的隐式规则，不写命令即可。
    ```

17. 隐式规则的中使用的变量可以分为两种：

    1. 与命令相关的变量：

       ```makefile
       AR  #函数库打包程序，默认为ar
       AS  #汇编语言编译程序，默认为as
       CC  #C语言编译程序，默认为cc
       CXX #C++语言编译程序，默认为g++
       CPP #C语言预处理器，输出到标准输出，默认为$(CC) -E
       FC  #Fortran编译器和预处理程序，默认为f77
       LEX #Lex词法分析器生成器，将.l文件生成lex.yy.c文件(C语言源文件)，默认为lex
       YACC#Yacc文法分析器生成器，将.y生成y.tab.c文件，默认为yacc
       RM  #删除文件，默认为rm -f
       ```

    2. 与参数相关的变量，很多都是未定义的，不过都推荐使用+=，而不是=追加参数：

       ```makefile
       ARFLAGS  #函数库打包程序AR命令的参数。默认值是"rv"。
       ASFLAGS  #汇编语言编译器参数，当明显地调用“.s”或“.S”文件时。
       CFLAGS   #C语言编译器参数。
       CXXFLAGS #C++语言编译器参数。
       CPPFLAGS #C预处理器参数，C和Fortran编译器也会用到。
       FFLAGS   #Fortran 语言编译器参数。
       LDFLAGS  #链接器参数。
       LFLAGS   #Lex 文法分析器参数。
       YFLAGS   #Yacc 文法分析器参数。
       ```

18. 可以使用模式规则的来定义隐式规则的，至少要包含%。%的展开发生在变量和函数的展开之后（运行时），变量和函数的展开发生在载入Makefile 时。

19. 在模式规则中，目标和依赖文件都是一系例的文件，可以使用自动化变量来书写一个命令完成从不同的依赖文件生成相应的目标。

20. 自动化变量一共有21个，实际是7类，然后分别加上D和F，表示目录和文件。

    ```makefile
    $@  #规则中所有目标文件的集合，如果是模式规则(以%定义的)，则表示匹配与模式定义的集合
    $%  #仅当目标时函数库文件(例如foo.a(bar.o)，Unix下的.a，Windows下的.lib)时，表示规则中的目标成员名，即括号中的bar.o。如果目标不是函数库文件，其值为空。
    $<  #依赖中第一个，如果是模式规则(以%定义的)，则表示匹配与模式定义的集合。
    $?  #所有比目标新的依赖的集合，以空格分隔，一般用在使用ar命令将.o文件打包成.a库
    $^  #所有依赖的集合，以空格分隔，自动去重
    $+  #同$^，只是不去重
    $*  #目标模式中%及之前的部分，如果目标为dir/a.foo.b，模式为a.%.b，那么$*就是dir/a.foo。某些情况会触发GNUMake的特性，应尽量避免使用。
    #以上的每一个都可以由D或F的后缀，例如$(@D)和$(@F)，这俩分别为$@的目录部分和文件部分，相当于dir和notdir函数的返回值。这是GNUMake中老版本的特性，在新版本中，我们使用函dir或notdir就可以做到了。
    #例子：
    %.o : %.c
    	$(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@ #$@表示所有目标的挨个值，$<表示所有依赖的挨个值
    %.o:%.c %.h
    	echo $@ $< $^ #对于目标add.o来说，$@为add.o，$<为add.c，$^为add.c add.h
    foo.a(bar.o):
    	echo $@ $% #$@为foo.a，$%为bar.o
    lib:foo.o bar.o lose.o win.o
    	ar r libxx.a $? #仅将比函数库libxx.a新的目标文件更新，比打包所有的目标文件更有效率。
    ```


# 打包库文件

1. Unix下使用ar命令将.o文件打包成.a函数库文件。

   ```makefile
   libxx.a(add.o minus.o)#指定函数库及其组成，这不是一个命令，而是一个目标和依赖的定义。这种写法就是为了ar服务的。等价于libxx.a(add.o) libxx.a(minus.o)
   foolib(hack.o) : hack.o
   	ar cr foolib hack.o
   ```

2. 如果make的目标是a(m)形式的，则会把目标变成(m)去匹配规则。

3. 可以使用"后缀规则"和"隐含规则"来生成函数库打包文件：

   ```makefile
   .c.a:
       $(CC) $(CFLAGS) $(CPPFLAGS) -c $< -o $*.o
       $(AR) r $@ $*.o
       $(RM) $*.o
   ##等价于
   (%.o) : %.c
       $(CC) $(CFLAGS) $(CPPFLAGS) -c $< -o $*.o
       $(AR) r $@ $*.o
       $(RM) $*.o
   ```

4. 在进行函数库打包文件生成时，请小心使用 make 的并行机制（“-j”参数）。如果多个ar命令在同一时间运行在同一个函数库打包文件上，就很有可以损坏这个函数库文件。所以，在make 未来的版本中，应该提供一种机制来避免并行操作发生在函数打包文件上。目前来看不应该使用-j参数打包。
