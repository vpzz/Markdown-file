# 基础

1. make 是linux下的一个==工程管理器==。会根据目标文件和依赖文件的存在与否和时间戳，来决定命令是否执行。确保修改的文件会反映到所有依赖他的目标文件中。

2. Cmake和make不同，它是用来产生各种Makefile或Project（例如vs的.sln工程文件）文件的。

3. make的提出，主要是linux下IDE的缺乏。最初用来管理C程序文件。对于维护一些具有相互依赖关系的文件特别有用。例如程序库依赖.h文件，.c文件，可执行文件依赖库文件等。

4. 使用make的好处是，可以有序地编译链接工程。修改部分文件后再编译时，只需要编译所有依赖于修改过的文件的文件即可。

5. make工具不仅可以用于编译C，还可以编译任何语言的代码。还可以处理一些自动化任务。

6. C程序编译链接的原则如下，好的Makefile应该做到这一点：

   1. 如果程序从来没被编译过，则所有.c文件都要被编译并链接。
   2. 如果某些.c文件被修改了，则只编译这些被修改的.c文件并链接。
   3. 如果某些.h文件被修改了，则需要编译链接所有include了这些.h文件的.c文件。

7. 规则的语法要求如下：

   ```makefile
   targets:prerequisites
   	command #任意shell命令，必须要以tab开头，不能缺少，也不能将tab替换为空格。否则会提示 Makefile:2: *** missing separator.  Stop.
   	... #命令可以有空行，空行上只能包含空白字符
   #或者是
   targets:prerequisites;command #如果命令较短可以和目标写在同一行，不过要用分号分隔。
   	command
   ```

8. 在shell下输入make，会自动查找makefile文件，顺序依次为：GNUmakefile，makefile，Makefile。

9. 如果没有手动指定目标（make 目标名），则会将文件中的第一个目标作为默认的目标。 

10. 无论是否在make命令行中指定目标，make都会先将make读入的文件名作为目标。如果默认的3个文件名，也没有手动指定文件，则会依次make那三个文件，这里会触发隐式规则，首先寻找GNUmakefile.o。

11. 一般来说，发布的源码包中都是Makefile，这样用户可以手动写一个makefile来替代当前的默认编译设置。

12. 当本次make的最终目标是最新的时，会提示：`make: 'test1' is up to date.`。

13. make程序的选项：

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

14. 使用-d选项来输出更多的细节：

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

15. 

16. 


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

10. 规则中的目标可以有多个，用空格分开。可以使用通配符来构成模式规则，这种规则可以匹配多个目标名。一条命令一行写不完可以加\换行。命令可以有多条。

11. 如果要生成多个可执行文件，则可以这样写：

    ```makefile
    all : main1 main2
    main1 : main.c
    	command
    main2 :main2.c
    	command
    ```

12. make默认使用默认的shell执行命令。

13. makefile支持三种通配符：

    ```makefile
    *  #≥0个任意字符
    ?  #任意单个字符
    [] #[]内的任意一个字符，例如[a-z]表示任意小写字母
    ```

14. 如果想在文件名中包含实际的通配符符号，则使用\转义。

15. 可以将通配符给变量赋值：

    ```makefile
    objects = *.o       #这里的.o并不会就地展开。类似于C语言中的宏。
    objects = $(wildcard *.o)    #此时会强行让*.o就地展开为当前目录下以.o结尾的文件，只有实际存在的文件才有用。
    ```


# 伪目标

1. 约定俗成，all为最终目标，且写在最开始。。

2. clean目标没有依赖的文件。约定俗成为删除编译生成的各种文件，将目录还原为编译前的状态。一般放在Makefile的最后。

3. clean就是一个伪目标。他并不是一个文件，而只是一个标签。因为并不会生成这个文件。make首先寻找是否存在同名文件，然后和依赖文件的时间戳比较，而这里没有依赖文件，同时，伪目标clean文件也不存在，因此会运行命令以生成该文件。（这样会导致只要每次make clean，都会无条件的执行下面的命令）

4. 伪目标的名称不能和已有的文件重名（这样的话，就会认为目标存在，且足够新，就不会运行命令了）。当然也可以使用.PHONY关键字显式地指定当前目标为伪目标。一旦被显式指定为伪目标，make该目标时，一定会运行它下面的命令。例如：

5. ```makefile
   .PHONY:clean
   clean:
   	rm -f *.o
   ```

6. 伪目标一般没有依赖文件。不过也可以添加依赖文件，伪目标的修改时间可以看做是任意早的，即任何时候都需要进行更新的。

7. Makefile支持依赖于相同文件的多目标。等价于多个单目标的结果。

   ```makefile
   bigoutput littleoutput:text.g
   	generate text.g -$(subst output,,$@)>;$@
   #等价于
   bigoutput:text.g
   	generate text.g -big >;bigoutput
   littleoutput:text.g
   	generate text.g -little >;littleoutput
   ```

8. 

# 命令执行

1. $()表示执行一个Makefile的函数。 \$@表示目标集合的迭代类型。
2. make会一条一条地执行命令，忽略空行。但是如果是以tab开头的空行，则认为是一个空命令（啥也不做）
3. 默认每条命令都是独立的环境，如果需要上一条命令的结果作用于下一条命令，则应把这两个命令写在同一行上，使用分号分隔这两个命令。
4. <img src="Make.assets/image-20200604012451718.png" alt="image-20200604012451718"  />
5. 每次命令执行完毕后，make都会检测它的返回码，如果出现错误，则终止当前规则。不过有时候命令报错不重要，还希望继续执行后面的命令。可以在命令最前面加上一个-减号，忽略该行命令的错误。

   ```makefile
   exec:
   	- cd /home/zj  #进入/home/zj目录，并忽略错误
   	pwd            #打印当前目录
   ```
6. 命令中若要使用shell的\$符号，要用\$\$来转义。

# 变量

1. Makefile中的变量和C中的宏一样，代表了一个字符串。在Makefile执行的时候，会自动展开。变量可以使用在目标，依赖，命令等地方。

   ```makefile
   #定义一个变量，内容为"a.o b.o"
   objects = a.o b.o
   #使用变量,会在执行命令前将变量展开
   test:
   	echo $(objects)#这里的注释被当作命令的注释，而不是makefile的，虽然makefile的注释也是以#开头
   ```

2. 变量名是大小写敏感的，可以以数字开头，不应包含:#=和空格等。在声明时要赋予予初值。使用$在变量名前引用变量。不过最好加上()或{}。如果要使用真正的\$，则输入\$\$。

3. ![image-20200604013440833](Make.assets/image-20200604013440833.png)

4. 给变量赋值可以使用=或：=。：=表示只使用它之前定义过的变量。例如：

5. ```makefile
   y:=$(x) bar       因为这之前没有定义x变量，所以y的值为bar，而不是foo bar
   x:=foo
   
   y=$(x) bar       y的值为foo bar
   x=foo
   ```

6. 变量定义还有一个有用的操作符   ?=   含义是如果先前没有定义过该变量，则定义并赋值，如果定义了则不做任何事情。类似于C语言的ifdef。

7. ```makefile
   FOO ?= bar
   等价于如下代码：
   ifeq($(origin FOO),undefined)
   	FOO = bar
   endif
   ```

8. ifeq 为条件判断语句，origin函数返回FOO的出处。

9. 可以使用+=为变量追加值。

10. ```makefile
    objects = main.o foo.o bar.o
    objects += another.o
    		$(objects) = main.o foo.o bar.o another.o
    ```

11. 上述命令等价于：

    ```makefile
    objects = main.o foo.o bar.o
    objects :=$(objects) another.o
    ```

12. +=根据前一次的赋值操作符来区分=和：=

    ```makefile
    variable := value
    variable += more
    #等价于:
    variable := value
    variable = $(variable) more
    ```

13. 

# 内置函数

1. 使用\$()或\${}来调用函数，返回值可以当做变量来使用。先是函数名，后面为参数。参数之间用逗号分隔，函数名和参数之间用空格分隔。

2. 为了风格的统一，()和{}的使用，应该统一。

3. 字符串替换函数subst

   ```makefile
   $(subst <from>,<to>,<text>)
   #功能:把字符串<text>中的<from>字串，替换成<to>字符串。
   #返回：函数返回被替换过后的字符串
   ```

4. 模式字符串替换：查找text中的单词，然后将符合模式的单词进行替换。%传递通配内容。

   ```makefile
   $(subst bar,bax,bar.c bar.h)
   ```

5. ![image-20200604103802735](Make.assets/image-20200604103802735.png)

6. ```makefile
   $(patsubst %.c,%.o,x.c.c bar.c)
   目标字符串可以分为两个单词，x.c.c和bar.c，二者都匹配%.c的规则(默认贪婪匹配)，因此替换为:
   x.c.o bar.o
   ```

7. ![image-20200604104231759](Make.assets/image-20200604104231759.png)

8. ```makefile
   $(findstring a,a b c)     返回"a"
   $(findstring a,b c)       返回空字符串""
   ```

9. ![image-20200604104532804](Make.assets/image-20200604104532804.png)

10. ```makefile
    $(filter %c %s,foo.c bar.c baz.s ugh.h)
    text中有4个单词，pattern中有2个模式，依次匹配。fooc. bar.c baz.s符合，其余的都去掉。按顺序输出即可。
    fooc. bar.c baz.s
    ```

11. ![image-20200604104858048](Make.assets/image-20200604104858048.png)

12. ```makefile
    $(filter %c %s,foo.c bar.c baz.s ugh.h)  只有ugh.g该单词不符合模式。
    ugh.h
    ```

13. ![image-20200604105042799](Make.assets/image-20200604105042799.png)

14. ```makefile
    $(sort lose foo bar lost)
    bar foo lose lost
    ```

15. ![image-20200604105226285](Make.assets/image-20200604105226285.png)

16. ```makefile
    $(word 2,programing linux c)
    linux
    ```

17. ![image-20200604105346707](Make.assets/image-20200604105346707.png)

18. ```makefile
    $(wordlist 2,4,I like linux c programming)
    like linux c
    ```

19. ![image-20200604105514129](Make.assets/image-20200604105514129.png)

20. ```makefile
    $(words I like linux c programming)
    5
    ```

21. ![image-20200604105658722](Make.assets/image-20200604105658722.png)

22. ```makefile
    $(firstword I like linux c programming)
    I
    ```

23. ![image-20200604105909857](Make.assets/image-20200604105909857.png)

24. ```makefile
    $(dir usr/src/linux-2.4/Makefile hello.c)
    usr/src/linux-2.4 ./
    ```

25. ![image-20200604110028221](Make.assets/image-20200604110028221.png)

26. ```makefile
    $(notdir usr/src/linux-2.4/Makefile hello.c)
    Makefile hello.c
    ```

27. ![image-20200604110210852](Make.assets/image-20200604110210852.png)

28. ```makefile
    $(suffix usr/src/linux-2.4/Makefile hello.c foo.s)
    " .c .s"
    ```

29. ![image-20200604110406919](Make.assets/image-20200604110406919.png)

30. ```makefile
    $(basename usr/src/linux-2.4/kernel/exit.c hello.o home/hacks)
    usr/src/linux-2.4/kernel/exit hello home/hacks
    ```

31. ![image-20200604110546563](Make.assets/image-20200604110546563.png)

32. ```makefile
    $(addsuffix .c,foo bar hello)
    foo.c bar.c hello.c
    ```

33. ![image-20200604110653953](Make.assets/image-20200604110653953.png)

34. ```makefile
    $(addprefix usr/src/linux-2.4/kernel/,exit.c time.c)
    usr/src/linux-2.4/kernel/exit.c usr/src/linux-2.4/kernel/time.c
    ```

# 循环，判断

1. makefile中将循环当做一个函数：将list中的单词逐一取出，放到参数var中，执行text中的表达式。最终返回一个包含各循环结果的字符串，空格分隔。list也可以是个表达式。text中使用$(var)引用循环变量的值。

2. ```makefile
   $(foreach var,list,text)
   names := a b c d
   files := $(foreach n,$(names),$(n).o)
   结果为  a.o b.o c.o d.o
   ```

3. ![image-20200604151322859](Make.assets/image-20200604151322859.png)

4. 条件判断函数

   ```makefile
   $(if <condition>,<then-part>)
   #或者:
   $(if <condition>,<then-part>,<else-part>)
   ```

5. 如果conditiono非空，则表达式为真。


# 隐式规则和默认变量

1. 根据Linux内核makefile的经验，不建议使用任何隐式规则，最好全部使用显式规则，这样避免make进行错误或意想不到的自动推导。

2. make一个目标时，会自动根据目标名称来自动推导其依赖和命令，推导的原则是根据隐式规则。

3. 隐式规则：make程序预先约定好了的，不用在makefile中写出来的规则。隐式规则会使用一些系统变量，例如系统变量CFLAGS可以控制编译器的参数。例如：

4. ```makefile
   foo:foo.o bar.o
   	cc -o foo foo.o bar.o $(CFLAGS) $(LDFLAGS)
   ################################
   #上一条规则有2个依赖foo.o和bar.o，如果在makefile中找不到和foo.o匹配的规则，则make会根据隐式规则自动推导他们的依赖目标和命令如下：
   foo.o:foo.c
   	$(CC) $(CPPFLAGS) $(CFLAGS) -c foo.c
   bar.o:bar.c
   	$(CC) $(CPPFLAGS) $(CFLAGS) -c bar.c
   ```

5. 事实上，.o文件不仅依赖于.c，还依赖于.h头文件，make的自动推导只会依赖于.c。

6. 特例：

   ```makefile
   #如果仅有下面一行，而main.o的下一行不是以tab开头，则该行不表示一个规则，而是表示一个依赖附加关系，即在自动推导main.o的规则时，会把defs.h当作依赖添加上。
   main.o:defs.h
   #例如当
   
   #如果main.o的下一行是以tab开头的，即使tab后没有命令，也被认为是一个空命令，此时该行被当作一个main.o的规则，此时不会再触发自动推导。
   main.o:defs.h
   	
   #例如当
   ```

7. make的目标和普通规则匹配时，仅需要和规则的目标匹配即可。如果和隐式规则匹配时，还需要保证其依赖的文件也存在才可以正确匹配。例如：

   ```makefile
   test1:test2
   	echo 1
   #make test1时，可以发现上面的规则的目标就是test1，因此可以匹配。而make test2时，找不到显式规则，因此开始寻找隐式规则，有很多条都可以匹配，例如从n.o生成n，从n.c生成n和从n.f生成n等，因此会寻找n.o，n.c，n.f这些文件是否存在，经过一番查找后，如果找不到，那就说明
   ```

8. 隐式规则的命令中基本都使用了预先设置的变量，也可以使用 make -R/--no-builtin-variables来取消预定义变量对隐式规则的作用。

9. 例如第一条隐式规则的为：

10. ```makefile
    $(cc) -c $(CFLAGS) $(CPPFLAGS)
    ```

11. 而CC变量默认为cc。一般都会改为gcc，$(CC)=gcc

12. 隐式规则的中使用的变量可以分为两种：①命令相关，例如CC②参数相关，例如CFLAGS

13. ![image-20200604153356878](Make.assets/image-20200604153356878.png)

14. 可以使用模式规则的来定义隐式规则的，至少要包含%。

15. %表示任意长度的非空字符串，通配符。依赖目标和命令中的%取值对应于目标中的%取值。

16. ```makefile
    %o : %c		#指出了从所有的.o文件依赖于对应的.c文件。
    	command
    .c.o :           #和%o:%c相同，旧格式
    	command 
    ```

17. make会根据%的规则去匹配当前目录下的文件名，一旦找到就会执行对应的命令。

18. 自动化变量一共有21个，实际是7个，然后分别加上D和F，表示目录和文件。

19. ![image-20200604155606978](Make.assets/image-20200604155606978.png)

20. 

21. 
