# 基础部分

1. Python诞生于1990年，完成同一功能所需要的代码量一般为C语言的10%不到，有庞大的第三方库，C和Python可以互相调用。2009年发布了python3.0版本。

2. Python的名称来源于巨蟒剧团 Monty Python，python作为英文单词，意思是蟒蛇。

3. Python Package Index（PyPI）是Python的官方软件仓库。现在已经有6万多个库了。

4. 标准库包含了多个内置模块 (以C编写)，Python必须依靠它们来实现系统级功能，例如文件I/O，此外还有大量以Python编写的模块，提供了日常编程中许多问题的标准解决方案，它们将特定平台功能都抽象化为平台中立的API来增强Python程序的可移植性。

5. Windows版本的Python安装包通常包含整个标准库，往往还包含许多额外组件。对于类Unix操作系统，Python通常会被分成一系列的软件包，因此可能需要使用包管理工具来获取部分或全部可选组件。

6. 计算机只能解决一个问题的可计算部分。

7. 有两种编程方式，交互式（例如IPython和Jupyter）和文件式，和matlab类似。交互式控制台提供REPL（read-eval-print-loop），即读取，求值，输出的循环。

8. 缩进是Python语法的一部分，缩进不正确可能导致运行错误，是表达代码包含和层次关系的唯一手段。一般为四个空格或一个tab。

9. #后面是单行注释   '''开头和结尾是多行注释，三个单引号或双引号。

   ```python
   #单行注释
   
   '''
   多行注释
   多行注释
   '''
   ```

10. 命名是将标识符和对象关联的过程，标识符区分大小写，可以有汉字。

11. 一共有33个保留字，也称为关键字，区分大小写。

    ```python
    and      elif    import raise  global
    as       else    in     return nonlocal
    assert   execpt  is     try    True
    break    finally lambda while  False
    class    for     not    with   None
    continue from    or     yield
    def      if      pass   del
    ```

12. 语句结尾不用加分号。如果要将几行代码写到一行，可以用分号分隔。

13. type(x) 可以返回对象x的类型，type不是关键字。

14. 如果某行代码太长，可以使用\来续行。要求\之后立刻就是换行，不能有别的空格。相当于\把enter转义了。

15. python会忽略`(),[],{}`内的换行符，因此他们内部的换行符可以不用\来续行。

    ```python
    a = [1, 2, 3,
         4, 5]
    #等价于
    a = [1, 2, 3,\
         4, 5]
    ```

16. PEP是Python Enhancement Proposals的缩写，一般包含以下几种：

    1. 跟踪Python中的新特性

    2. 说明Python中的某一个设计问题

    3. 关于Python的提案，但不针对Python语言本身

17. python2中True是一个变量，可以对它赋予其他的值，但是不建议这么做，会造成混乱，因此while True就不会被python2优化掉，因为用户可能会修改True的值。在python3中，True作为一个关键字存在，不允许赋值，因此while True会被优化。


# 字符串

## 字符串类

1. 字符串可以由单引号或双引号括起来，普通字符串为\_\_builtin\_\_模块的str类型。Python没有专门用于表示字符的类型，字符可以看做只有一个元素的字符串。三个单(双)引号括起来长字符串，可以跨越多行。其实Python没有多行注释，三个引号可以充当多行注释。

   ```python
   #以下四种写法等价：
   name = "jack"
   name = 'jack'
   name = '''jack'''
   name = """jack"""
   
   "\n" == '''
   '''     #这两个字符串是完全相等的,都只有一个字符\n。单行字符串和多行字符串都可以互相替换，只需要把多行字符串的换行符都替换为\n即可。
   ```

2. 字符串类str的许多方法，在Python2中都是在string模块中，现在不推荐使用string模块。但是string模块中仍然包含一些str类没有的常量：

   ```python
   import string
   string.digits         #数字  '0123456789'
   string.ascii_letters  #大小写字母'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   string.ascii_lowercase #小写字母 'abcdefghijklmnopqrstuvwxyz'
   string.ascii_uppercase #大写字母 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   string.printable #所有可打印的ASCII字符,一共100个
   '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
   string.punctuation #标点符号  '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
   ```

3. 所有针对序列的操作都可以对字符串实施，但是字符串的内容是不可变immutable的，即不能对元素或切片赋值。

   ```python
   s = "abc"
   s[1] = "d"  #会报错，TypeError: 'str' object does not support item assignment
   ```

4. 如果希望字符串内出现引号，则应在字符串外使用另一种引号，或者使用\进行转义。

   ```python
   "ah'hh'ha"    #字符串内有引号，需要单双引号交替使用。
   'ah\'hh\'ha'  #和上面的字符串完全一样。
   "ah'hh'ha" == 'ah"hh"ha' #结果为False，因为最外部的单双引号可以替换，内部的不可以
   ```

5. 字符串中元素的下标从0开始编号。0表示首个，-1表示最后一个。可以用[ ]进行切片操作来获取字符串的子串。

   ```python
   str1 = "abcde"
   str1[1:3]   #获得的为"bc",取出下标为1,2的子串,切片是左闭右开
   str1[-1]    #获得的为"e"
   str[:3]     #获得的为"abc",相当于[0:3]
   str[2:]     #获得的为"cde",相当于[2:0],包含最后一个元素
   str[1:4:2]  #获得的为"bd",从1到4，步长为2。即str[1],str[1+2]组合起来
   str[::-1]   #获得的为"edcba",将原来的字符串逆序。步长可以是负数
   ```

6. 字符串处理函数：

   ```python
   len("12哈哈")  #4，返回字符串的长度，即字符个数。
   
   str(1.23)      #"1.23",将任意类型转化为字符串形式，调用str的构造函数，自定义类型的对象需要该类型自己定义 .__str__(self) 保留方法。
   str([1,2,3])   #"[1,2,3]",并非"123"
   
   hex(425)       #"0x1a9",转化为16进制形式的字符串，只能接受整数。
   oct(425)       #"0o651",转化为8进制形式的字符串，只接受整数。
   
   chr(21704)     #"哈"，根据Unicode码点值(范围在0到0x10ffff之间)，获得对应的字符。
   ord("哈")      #21704,将字符转化为Unicode码点值,结果为int类型,只能处理单个字符。
   ```

7. 字符串操作符：

   ```python
   "abc" + "def"  #结果为"abcdef",字符串拼接。
   3*"abc"        #结果为"abcabcabc"。
   "a" in "abc"   #结果为True。判定是否是连续子串。早期的Python中，字符串的in只能用来确定单个字符是否∈某个字符串，和普通容器相同。
   "ab" in "abc"  #结果为True。
   "ac" in "abc"  #结果为False。
   ```

8. 字符串可以使用+运算符拼接，也可以直接连写，不过后者仅限于字符串字面值常量使用：

   ```python
   x = "hello"
   y = "world"
   x+y            #结果为"helloworld"
   "hello"  "world" #中间可以有0或任意多个空格，都会被忽略。相当于"helloworld"
   x y            #会报错
   ```

9. python提供两种机制将对象转化为字符串，str类和repr函数：

   ```python
   #待处理的字符串为 "abc\ndef" ,一共有7个字符
   len("abc\ndef")  #结果为7,\n看做一个字符
   str("abc\ndef")  #结果还是"abc\ndef",长度为7,这种字符串方便打印识别
   repr("abc\ndef") #结果为"'abc\\ndef'",长度为10,\\看做一个字符。在处理字符串时，不识别转义，将\n看作2个字符
   #二者的一个重要区别是repr的结果可以用eval函数将字符串还原：
   a = eval(str("abc\ndef"))   #会报错，这里相当于将abc\ndef赋值给a。
   b = eval(repr("abc\ndef"))  #运行正确，此时b为一个字符串,等于"abc\ndef"。
   #使用print打印时，会将解析最外层的转义字符，例如会将\n作为真实的换行输出，\\则会变为\。
   print(str("abc\ndef"))
   abc
   def
   print(repr("abc\ndef"))
   'abc\ndef'
   ```

10. 常用方法：

    1. 对齐 justify

       ```python
       "1111".center(10,"*") #在字符串两边填充指定字符，默认为空格。 '***1111***'
       "1111".ljust(10,"*")  #左对齐   '1111******'
       "1111".rjust(10,"*")  #右对齐   '******1111'
       "1111".zfill(10)      #用0填充  '0000001111'
       ```

       2. 查找

          ```python
          'With a moo-moo here, and a moo-moo there'.find('moo',10,20)  #结果为11。在字符串中寻找连续子串,如果找到就返回子串的第一个字符的索引(基于整个串，而非搜索范围),否则返回0。后两个参数为指定搜索的范围,区间为左闭右开,可以省略。
          ```

       3. 合并，分割

          ```python
          s = list("12345")  #  ['1', '2', '3', '4', '5'] 将一个字符串转换为字符串列表
          "*".join(s)  #用特定字符(串)将字符串列表连接起来。结果为:  '1*2*3*4*5'
          '1*2*3*4*5'.split("*")  #用特定字符(串)分割字符串,将分割后的结果存储在列表中。和join是相反的操作
          ['1', '2', '3', '4', '5']
          "*".join([1,2,3,4,5])   #会报错,只能合并字符串列表
          #如果要将列表[1,2,3,4,5]转换为"12345"，推荐使用如下步骤
          [str(i) for i in [1,2,3,4,5] ]  #使用列表推导式，对列表的每个元素都执行str函数，构成新列表  ['1', '2', '3', '4', '5']
          "".join(['1', '2', '3', '4', '5']) #使用空字符串将字符列表拼接起来，得到"12345"
          #还可以使用map函数和str函数结合的方法
          "".join(map(str, [1,2,3,4,5]))  #map的结果为迭代器，join的参数就需要一个可迭代
          r"G:\Python file\data".split(r"\")  #结果为 ['G:', 'Python file', 'data']
          '/usr/bin/env'.split("/")  #结果为   ['', 'usr', 'bin', 'env'],如果不指定分割字符，默认会使用单个或多个连续的空白字符(空格,制表符,换行符)来分割。如果分隔符出现在第一个字符，则会产生一个空字符串
          ```

       4. 查找并替换
       
          ```python
          'This is a test'.replace('is', 'eez')  #查找子串"is",将所有的匹配向都替换为"eez",结果为'Theez eez a test'
          #根据转换表来替换,实际上是不同的Unicode码点之间转换关系。和replace不同的是,该函数只能进行单个字符的查找替换，不过可以同时进行多对。
          table = str.maketrans('cs', 'kz')  #table为一个Unicode码点映射的元组 {99: 107, 115: 122}
          'this is an incredible test'.translate(table) #对字符串应用转换表,结果为 'thiz iz an inkredible tezt'
          ```

       5. 掐头去尾
       
          ```python
          "  a  bc  ".strip()  #将字符串两端的空白剔除掉,中间的空白除外。 结果为'a  bc'
          "  abc  ".lstrip()   #去掉左侧空白，结果为"abc  "，也可以使用rstrip去掉右侧空白。
          '*** SPAM * for * everyone!!! ***'.strip(' *!')   #也可以指定删除其他多种字符,结果为'SPAM * for * everyone'
          ```

       6. 判断字符串的开头或结尾是否匹配另一个字符串
       
          ```python
          "Hello, Python".startswith("He")  #是否以"He"开头,结果为True
          "Hello, Python".endswith("on")    #是否以"on"结尾,结果为True
          ```

       7. 判断字符串是否满足特定条件
       
          ```python
          "1a".isidentifier() #结果为False。判断字符串是否可以作为Python的标示符，关键字也可以作为标识符的，但是不建议，因为会覆盖原有的关键字的含义
          isspace      #是否都是空白字符(空格,制表符,换行符)
          isnumeric isdigit #二者对于字节数组的表现不同
          #Unicode定义了一些属性，满足特定属性的字符会被归类到一个集合中，例如Numeric_Type属性，有三种取值，分别为：
          Decimal #在位置十进制(罗马计数法就不属于位置值)中使用的字符，0-9
          Digit   #位置十进制系统中字符的变种，例如①(圆圈包起来的位1)，₀(下标的0)，⑩(圆圈包起来的数字10)
          Numeric #除了上述两种以外的具有数值含义的字符，例如⅐，Ⅰ(罗马数字1)，〡(苏州码字的1，古代商业上用)
          #从Decimal到Digit再到Numeric越来越宽泛
          print("1".isdigit())     #True
          print("1".isdecimal())   #True
          print("1".isnumeric())   #True
          print("①".isdigit())     #True
          print("①".isdecimal())   #False
          print("①".isnumeric())   #True
          print("⅐".isdigit())    #False
          print("⅐".isdecimal())  #False
          print("⅐".isnumeric())  #True
          ```


## 字符串编码

1. python3中所有的字符串都是Unicode字符串。

2. 原生字符串并不是一种新的类型，在送交解释器执行前会转换为普通字符串，出现的目的是为了让程序员在将现实中的字符串（例如windows路径或正则表达式）嵌入到程序时，不用去考虑复杂的转义。

3. 原生字符串要求r后面是一个普通字符串，而普通字符串的末尾不能为奇数个\，否则会出现\"，那么字符串末尾的标记就没了。实际上原生字符串就是将其后的普通字符串中的每个\都替换为两个\，当然这个替换是无法用replace完成的，因为他会把\n识别成一个字符。

   ```python
   a = r"abc\ndef"   #在普通字符串前加上r(R)就可以的到原生字符串，相当于"abc\\ndef"
   r"sd\"            #错误写法，可以将\单独写出来然后拼接,例如r"sd"+"\\"
   r"sd\\"           #有效，等价于"sd\\\\"
   ```

4. Unicode标准为每一个字符都分配了一个码点，即一个数字(https://unicode-table.com/ 可以查询，Unicode官方使用U+十六进制的码点值来表示对应的字符)。可以使用16或32位的16进制字面量(需要分别加上\u或\U的前缀)来表示Unicode字符。或者使用Unicode字符的名称  \N{name} 来使用对应字符。

   ```python
   "\u00d6"     #结果为 'Ö' 字符。其中00不能省略，如果码点值小于256，可以用"\xd6"表示，它和"\u00d6"相等
   "\U000000d6" #结果为 'Ö' 字符。将U换成小写u就变成了5个字符，第一个是"\u0000"，后续是"00d6"
   "\N{cat}"    #结果为 '🐈' 字符,也可以是ship dog flower等。"\N{asterisk}"就是"*"
   ```

5. 需要注意的是，"\x00"不等于0，也不得能与空字符串""，更不等于空格" "，它的长度为1，是Unicode和ASCII的首个字符。C语言中无法创造出只包含一个空字符的字符串，因为C语言使用空字符来作为字符串的结尾标志。chr(0)的结果就是"\x00"

6. 为了与C语言交互或者将文本写入文件或通过网络套接字发送出去，需要将字符串转化为字节序列，也就是编码。

7. .py源文件中如果包含了中文字符(字符串或注释中)，推荐使用utf-8编码，因为python3解释器默认支持utf-8编码。

   ```python
   #utf-8编码的.py文件,正常执行,输出也正确
   print("中")  #中文注释
   
   #GBK编码的.py文件,会报unicode error,提示utf-8编解码器无法解码编号为0的字节0xd6。在.py文件开头添加上 # -*- coding: gbk -*- 后，则输出正常。这句注释是提示解释器文件的编码为gbk
   print("中")  #中文注释
   
   #如果只是在注释中存在中文，那么源代码保存为何种编码都不影响解释器执行
   ```

8. 源代码.py文件如果使用的是utf-8的编码，那么不用操心编码和解码的问题，因为Python3的解释器也是使用utf-8解码器进行解码的。python2默认使用ANSI编码，对于中文就是gbk，那么如果源代码是utf-8的那就需要加上下面的一行，gbk编码的则可以省略。

   ```python
   # -*- coding: utf-8 -*-
   ```

9. 所有的表示编码方案的字符串不区分大小写，也可以省略-，例如utf-8，utf8，UTF-8等。

10. 

11. 有不可变的bytes和可变的bytearray。encode函数是将Unicode字符串转化为特定的字节序列。

    ```python
    x = b"abc"  #x的类型为bytes,而不是str类型,长度为3。
    #bytes字面量只支持128个ASCII字符，余下的128个字符需要使用转义序列表示，例如\xf0表示0xf0,在扩展ASCII中。
    y = b'\xf0abc' #该字符序列有4个字符，第一个为0xf0，后面为abc。
    "ab".encode("utf-32")     #占据12个字节。
    b'\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00'   #最开头的4个字节为BOM头，fffe0000表示为小端。后面a\x00\x00\x00为字符a的UTF-32表示。b\x00\x00\x00为字符b的UTF-32表示。
    "ab".encode("utf-8")  #长度为2,此时就没有BOM头了
    b'ab'
    ```

12. 可以用bytes对象构造bytearray对象，它是为在幕后使用设计的：

    ```python
    x = bytearray(b"Hello")
    x[0]                    #结果为72
    #如果要修改需要使用字符的序数，即0-255,使用ord函数获取。
    x[1] = ord("s")         #此时x为bytearray(b'Hsllo')
    ```

13. Unicode码点和UTF-32BE是对应的：

    ```python
    x = "\N{cat}"  #Unicode码点为\U0001f408
    x.encode("utf-32")
    b'\xff\xfe\x00\x00\x08\xf4\x01\x00' #该字符的UTF-32BE编码为0001f408,
    "\U0001f408"
    '🐈'
    ```

14. 如果字符串中有些字符不在ASCII码表0-127内，则不能使用ASCII编码：

    ```python
    "æ".encode("ASCII")  #会报错
    "æ".encode("utf-8")   #
    b'\xc3\xa6'
    "æ".encode("utf-32")  #
    b'\xff\xfe\x00\x00\xe6\x00\x00\x00'
    ```

15. 上面的这个字符的Unicode编码查询：

16. <img src="Python.assets/image-20210923155046255.png" alt="image-20210923155046255" />

17. 也可以使用decode将bytes解码为字符串：

    ```python
    "æ".encode("utf-32").decode("utf-32")   #编码必须一致，因为bytes并不知道它存储的字节序列是什么编码。
    'æ'
    ```

18. encode和decode也可以用bytes和str类的构造函数替代：

    ```python
    bytes("æ",encoding = "utf-8")   #等价于 "æ".encode("utf-8")
    str(b'\xc3\xa6',encoding = "utf-8")  #等价于b'\xc3\xa6'.decode("utf-8")
    ```

## 字符串格式化

1. Python有多种字符串格式化的方法：

   1. 以前，主要的方法是使用%来进行替换，类似于C语言中的printf。

      ```python
      format = "Hello, %s. %s enough for ya?"     #%s为转换说明符,s表示将对象视为字符串如果给定的值不是字符串，则会自动用str将其转化为字符串。其他说明符也将导致形式的转换,例如%.3f也会将值转化为3位小数的浮点数。
      values = ('world', 'Hot')
      format % values   #结果为   'Hello, world. Hot enough for ya?'
      ```

   2. 模板字符串，类似于Unix shell的语法，并不好用。

      ```python
      from string import Template
      tmpl = Template("Hello, $who! $what enough for ya?") #模板中有两个参数who和what。$会读取一个单词
      tmpl.substitute(who="Mars", what="Dusty") # 使用关键字参数进行替换。
      'Hello, Mars! Dusty enough for ya?'
      ```

   3. 编写新代码时，推荐使用字符串对象的format方法，在2.6版本引入，目前最推荐使用。

      ```python
      name = "Jack"
      age = 18
      "我的名字是:{}, 今年 {} 岁".format(name, age) #结果为 '我的名字是:Jack, 今年 18 岁'
      ```
      
   4. 使用f-string方法，在字符串前加上f，来将{}替换为变量。3.6版本引入

      ```python
      name = "老王"
      f"你好，我是{name}"  # '你好，我是老王'
      ```

2. format方法中每个替换字段都用{}括起来，表示槽，{}内可以包含：

   1. 字段名，默认从0开始编序号，可以省略，也可以手动指定。可以是数字或标识符，在format函数中使用关键词参数来指定：

      ```python
      "{}cd{}gh{}".format("ab","ef",12)  #有两个槽，从左往右编号分别为0,1,2。format有三个参数，依次填入三个槽内，相当于字符串拼接。结果为"abcdefgh12"
      "{1}cd{0}gh{2}".format("ab","ef",12)  #手动指定槽的编号,结果为"efcdabgh12"
      "{1}cd{0}gh{1}".format("ab","ef",12)  #不同的槽可以用同一个编号，但是一个槽只能指定一个编号,结果为"efcdabghef"
      "{name} is approximately {value}.".format(value=3.141592653, name="π") # 结果为 'π is approximately 3.141592653.'
      fullname = ["Alfred", "Smoketoomuch"]
      "Mr {name[1]}".format(name=fullname) #结果为 'Mr Smoketoomuch'
      ```
      
   2. 转换标志，跟在感叹号后面的单个字符，可以有r（表示repr），s（表示str），a（表示ascii）。如果制定了转换标志，则将不使用对象本身的格式，而是使用指定的函数（str，repr，ascii）将对象转化为字符串。

      ```python
      "{pi!s}".format(pi = "π")   # 'π',长度为1,等价于str("π")
      "{pi!r}".format(pi = "π")   # "'π'",长度为3,等价于repr("π")
      "{pi!a}".format(pi = "π")   # "'\\u03c0'",长度为8,等价于ascii("π"),因为字符"π"的等价于"\u03c0"
      ```

   3. 格式说明符。跟在冒号后面的表达式，包含格式类型，字段宽度，数的精度，各种对齐和填充方式。

3. 要在最终的字符串中包含{或}，用两个代替：

   ```python
   "{{ }}".format()      #结果为 '{ }'
   ```

4. 槽的内部除了书写编号外，还可以进行单独的格式控制，格式控制标记需要按照顺序书写。

   ```
   :<填充><对齐><宽度><，千分位分隔符><.精度><整数和浮点数类型>
   ```

5. 默认情况下空格填充， 左对齐，宽度正好够输出。中英文混排时，默认填充的是英文的空格，而一个汉字字符的宽度却比一个英文字母大得多。可以使用全角空格 chr(0x3000)来做填充。

   ```python
   #字符串的格式输出
   "{:s}".format("sda") #保持字符串的格式不变，这也是字符串的默认说明符。
   #数字的格式输出
   "{:d}".format(421)   #将整数视为十进制数处理，这也是整数默认的说明符
   "{:b}".format(4)     #将整数表示为二进制数,结果为"100",不会添加0b前缀
   "{:o}".format(421)   #8进制表示,结果为'645'
   "{:x}".format(421)   #16进制表示,结果为'1a5'
   "{:X}".format(421)   #16进制表示,结果为'1A5'
   
   "{:e}".format(421)   #使用科学计数法表示,结果为"4.210000e+02"
   "{:E}".format(421)   #同上,只不过用E来替换e.结果为"4.210000E+02"
   "{:c}".format(960)   #将整数解读为Unicode码点，结果为"π"。可以用16进制0x03c0替换960。
   "{:f}".format(34)    #将数字解读为浮点数，结果为'34.000000'。默认显示小数点后6位小数。
   "{:%}".format(421)   #表示为百分比值 '42100.000000%'
   ```
   
6. 宽度和精度：

   ```python
   "{num:5}".format(num=32)       #使用整数来指定输出的宽度,结果为 '   32'。数字默认是右对齐。
   "{name:5}".format(name="Bob")  #也可以对字符串设置宽度,'Bob  '。字符串默认是左对齐。
   #精度也是使用整数指定的，但需要在它前面加上一个表示小数点的句点。这里的精度是进行四舍五入后的，不是简单地截断。
   "Pi day is {pi:.4f}".format(pi=pi)    #结果为   'Pi day is 3.1416'。保留到小数点后4位
   f"Pi day is {pi:10.4f}"  #宽度10和精度4结合使用,结果为'Pi day is     3.1416'。
   #添加千分位分隔符,可以和宽度精度联合使用，应该放到宽度和表示精度的小数点之间。
   f"Pi day is {1111.1111111:15,.4f}"  #结果为  'Pi day is      1,111.1111'
   ```

7. 符号对齐与填充，在指定宽度的整数前面添加填充和对齐的标志：

   ```python
   "{:10}".format("PYTHON")    #结果为"PYTHON    "   默认空格填充，左对齐，总宽度为10
   "{:=^20}".format("PYTHON")   #结果为"=======PYTHON======="  =填充,^表示居中对齐,总宽度为20
   "{:*>12}".format("PYTHON")   #结果为"******PYTHON"    *填充,右对齐,总宽度为12
   #  =除了可以用来当作填充字符,还可以表示将指定的填充字符放在符号和数字之间,这里不能和对齐符号联合使用。在对齐说明符后面加上+,可以在整数前添加+符号。
   print ('{0:=+10.2f}\n{1:=10.2f}'.format(pi, -pi))  #结果为:
   +     3.14
   -     3.14
   ```

# 分支，循环

1. 使用if else elif关键字来书写分支语句。

   ```python
   a = 1
   b = 2
   if a < b:   #冒号不可省略，冒号范围内的的语句要缩进。
       print("a<b")
   elif a > b:
       print("a>b")
   else:
       print("a=b")
   ```

2. 二分支结构的紧凑形式，类似于其他语言的三元运算符。并没有赋值过程。根据条件来决定执行哪个表达式。

   ```python
   1+2 if 1>2 else 1+3  #结果为4
   ```

3. 使用for来书写循环语句：

   ```python
   for i in range(5):   #此处i依次为0，1，2，3，4
       print(i)
   ```

4. range类型和list，tuple构成python三大基本序列类型。由于range存在严格的模式，因此它不支持序列的拼接和重复操作。range相比于list的优点是，占用内存小，因为它是实时计算对应下标的值，而非去内存中读取。因此如果要使用list存储大量有规律的数值，可以使用range替代。range例子：

   ```python
   list(range(10))
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   list(range(1, 11))
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   list(range(0, 30, 5))
   [0, 5, 10, 15, 20, 25]
   ```

5. while循环：

   ```python
   while <条件>:
   	<语句块>    #当条件为真时进入循环，执行语句块，直到条件为假时退出循环。
   ```

6. 带索引的循环：

   ```python
   data = ["a","b","c"]
   for index,data in enumerate(data): #enumerate的返回值是一个enumerate对象，它也是迭代器，从中可以依次取出由data构造的元组, (0,data[0]),(1,data[1]),(2,data[2])。该函数还可以指定下标的起始值start，默认为0
       print(index,"  ",data)
   ```

7. 范围for循环：

   ```python
   for c in "abc":        #依次取出字符串中的每个字符。
   for item in [1,2,3,4]  #依次取出列表中的每个元素。也可以是元组，字典类型
   for line in file:      #依次取出文件中的每一行，从文件当前位置指针开始。
   ```

8. break 跳出并结束最内层的整个循环，执行改循环后的语句。

9. continue 结束本次循环，执行下一轮循环，不过也要进行循环条件判定。

10. for，while循环可以和else搭配，和break互动，和continue无关。

   ```python
   for <循环变量> in <遍历结构>  #while也可以
   	<语句块1>
   else: #如果循环没有因为break而退出，即正常退出，则会执行else语句块，类似于异常处理中的else。
       <语句块2>
   ```


# 变量，表达式，语句

1. python的变量没有默认值，使用前必须进行赋值，赋值的同时会开辟内存空间。如果没有赋值就直接使用，会抛出NameError的异常，提示名字未定义。

   ```python
   age = 18
   a = b = c = 2  #此时a,b,c都会被赋值为2
   a,b,c = 1,2,3  #1,2,3被当作是元组(1,2,3)，因此会将元组的3个元素逐个赋值给a,b,c
   ```
   
2. python中一切都是对象，变量是对对象的引用。使用id()来查看变量指向的对象的地址。

   ```python
   a = 3    #在内存中创建一个整型对象，值为3，然后将变量a指向它
   id(a)    #2270013423920
   a = 4    #将变量a指向一个值为4的整型对象
   id(a)    #2270013423952
   b = 4    #不会重复创建对象(节省内存空间)，只是将b和a指向同一个对象。等价于b=a
   id(b)    #2270013423952
   ```

3. 通常用全部大写的变量名表示常量，只是一个约定。

4. 表达式是一些东西，语句是做一些事情。例如2*2是表达式，x = 3 就是语句。在交互式解释器中，解释器总是会将表达式的结果打印出来（实际上是print出来repr的结果）。而在脚本中执行时，则表达式不会打印任何内容。由于==赋值是语句而非表达式==，因此x=3在交互式解释器中不会打印任何内容。

   ```python
   #交互式
   3+3     #会输出6
   x = 3   #什么也不输出
   #而在脚本执行中，只有print语句会产生输出
   ```

5. 在python2中，print是一条语句，可以这样使用 print 3    。而在python3中，print变成了一个函数。

6. 无论在什么编程语言中，赋值语句都是最强大的，因为他可以让你无需知道变量存储的值就可以进行修改。所有的语句都有一个根本的特征就是执行修改操作。

7. 一个纯粹的表达式，例如2*2，也会被解释执行，但是其结果立刻就会被丢弃掉。

8. 布尔类型只有两个值，True和False，首字母小写是错误的。和"True"，"False"不同，这两个是字符串

   ```python
   #为True的值：
   非零数字    非空字符串，字典，列表，元组      非None的对象
   #为False的值：
   0   0.0   -0.0  0j   []   ()   {}   ""   None   
   #可以使用内置的bool函数来测试对象的bool值
   bool(None)  #结果为False
   ```

9. bool类型除了可以进行逻辑运算外，可以进行算术运算，比较运算，此时True被当作整数1，False被当作整数0。

10. 空值None不是布尔类型，而是NoneType类型。None不等于0

    ```python
    type(None)   #结果为NoneType类型。
    None == 0    #结果为False
    ```

# 运算符

1. 比较运算符：

   ```python
   <   <=   >   >=   ==   !=
   
   bmi = 22
   18.5 < bmi < 25  #Python支持这样的判断：18.5 <= bmi < 25。它的意思和数学意思一样。>=18.5且<25。
   18 < bmi < 25   #结果为 True
   25 > bmi > 18   #结果为 True
   (25 > bmi) > 18 #结果为 False，因为会将括号内的结果和18比较大小，无论结果是True或False，都是比18小的
   (18 < bmi) < 25 #结果为 True
   ```

3. 逻辑运算符，对布尔类型进行运算：

   ```python
   x and y  #两个条件的逻辑与
   x or y   #两个条件的逻辑或
   not x    #条件的逻辑非
   ```

4. 位运算符：

   ```python
   a = 0b110010 #二进制
   b = 0b101001
   a&b  #按位与，结果为0b100000
   a|b  #按位或，结果为0b111011
   a^b  #按位异或，结果为0b011011 相异时为1
   ~a   #按位取反，可以认为a是8位二进制数(实际上多少位，结果都一样)，即0b00110010，取反之后位0b11001101 当作8位有符号数即为-51。一个数的相反数=该数取反+1
   a<<2 #左移2位，相当于乘以4，结果为200。左移产生的数会越来越大，范围也会随之变大
   a>>2 #右移2位，结果为0b001100，即12。
   ```

5. 成员运算符：

   ```python
   1 in [1,2,3] #测试元素是否在序列中，结果为True
   4 not in [1,2,3] #结果为True
   ```

6. 身份运算符：

   ```python
   a,b = 10,10
   a is b #判断两个标识符是否引用自同一个对象，实际上是判断id是否相同。结果为True
   a is not b  #结果为False
   ```

# 标准输入

1. input函数可以从控制台获得输入，函数的参数为提示字符串。

   ```python
   str1 = input("请输入内容\n")  #获取到输入末尾的换行会被自动去掉,返回值为str类型。
   ```

2. 可以通过eval函数来动态执行命令，参数为字符串，将执行结果作为返回值返回，相当于把内容输入到解释器，类似于交互式环境：

   ```python
   a  = eval("1+3")  # 会计算1+3的值，并赋值给a。
   b = eval('"1+2"') # b为"1+2"，字符串类型。
   eval("print('hha')") #会执行print函数。
   ```

3. 可以将input和eval结合同时获取多个输入变量：

   ```python
   height, weight = eval(input('请输入身高(m)和体重(kg)[逗号隔开]:')) #这里eval将字符串"1.8,80"转化为了元组类型。
   ```

4. 如果输入的是单个数字，也可以进行类型转换：

   ```python
   int("1")       #结果为int类型 1
   float("3.14")  #结果为float类型 3.14
   ```

5. 获取用户的多次输入：

   ```python
   nums = []
   while True:
       iNumStr = input("请输入数字,(回车确认): ")
       if (iNumStr == ""):
           break
       nums.append(eval(iNumStr))
   print(nums)
   ```

# 标准输出

1. print函数可以向控制台输出，该函数没有返回值。

2. print可以接受end参数，默认为换行符，即输出完内容后再输出一个换行符。可以指定end='，'，这样在输出完内容后，输出一个逗号来替代之前的换行符。

   ```python
   print(self, *args, sep=' ', end='\n', file=None) #函数原型
   
   print(1)
   print(2)   #print默认带有换行符。这两句会在两行出现。
   
   print(1,end="|")
   print(2,end="")    #取消默认的换行符，用空字符串代替
   print(3,end="@")   #输出结果为    1|23@
   #可以设置sep参数来修改用于分隔多个输出变量的符号，默认是空格
   print(1,2,3)     #输出为"1 2 3"
   print(1,2,3,sep="")    #输出为 "123"
   ```

# 库，包，模块

1. 库是一种通俗说法，指特定功能集合，python标准术语中没有“库”的概念，标准术语有模块和包。

   ```python
   import turtle   #然后就可以使用库名.函数名()来调用库内的函数。
   import turtle as tt  #tt就是库别名。
   from turtle import setup  或者   from turtle import *  #这样就可以不用加库名而直接使用setup或所有名称了，不过可能会出现重名。
   from turtle import setup as ttsu  #将turtle.setup导入，并给他添加别名，原名setup是无法使用的，只能使用别名
   # import turtle 和from turtle import *的区别在于后者不会引入库中以_开头的名称
   ```

2. 标准库随python解释器一同安装，第三方库需要利用pip等包管理器额外安装。

3. 模块：以单个文件为独立命名空间的代码片段，模块名就是.py文件的名字。模块中可以import其他模块。

4. 包：目录集合，由多个模块（.py文件）有组织地构成。模块的组织方式构成了命名空间的层次结构。包中还可以包括子包。

5. Python库的核心是模块和模块的组织方式。模块和包分别类似于文件系统中的文件和文件夹

6. 一个模块就是一个命名空间，其中包含类，函数，语句，变量等元素。

7. 使用import 模块会加载模块文件，其中模块内的顶层可执行语句会被执行。使用模块名.名称的方式访问模块内顶层命名空间内的变量，类，函数等。

8. Python包区别于普通目录的主要特征就是包含\_\_init\_\_.py文件。

9. 每个包都需要包含一个\_\_init\_\_.py文件来表达包的组织。可以是空文件，只要存在即可。

   ```python
   #pkg包有2个子包pkg1和pkg2, pkg1有2个模块m1和m2, pkg2有1个模块m1
   pkg -- __init__.py
       \_ pkg1 --  __init__.py
       	    \_ m1.py
       	    \_ m2.py
       \_ pkg2 -- __init__.py
               \_ m1.py
   ```

10. python源文件的名称不能和已有的库冲突，否则在import时，会导入该文件。这样调用库中的功能时，会报属性不存在的错误。

11. 

# 数学计算

1. Python的整数没有限制。以0B或0b开头表示2进制，0O或0o开头表示8进制，0X或0x开头表示16进制。

   ```python
   #a,b,c均等于6689
   a = 0b0001101000100001
   b = 0o15041
   c = 0x1a21  #字母大小写都可以
   ```

2. Python的浮点数取值有精度和范围限制，使用53位二进制表示小数部分，15-16位有效数字，取值范围从$\pm (10^{-308}\to10^{308})$。浮点数的默认类型为<class 'float'>，实际上是C语言的double的精度和范围。

3. 浮点数间的运算存在不确定的尾数，不是bug，是因为用有限位来表示无限小数的问题，还有二进制除不尽的问题。

   ```python
   0.1+0.3      # 0.4
   0.1+0.2      # 0.30000000000000004
   ```

4. 浮点数在计算机中是以2进制的小数来表示的，不幸的是，大多数的十进制小数都无法精确地由有限位的二进制小数表示

   ```python
   十进制小数0.125 = 1/10 + 2/100 + 5/1000
   二进制小数0.001 = 0/2 + 0/4 + 1/8  #二者的值完全相同
   十进制小数0.1 = 0.0001100...   #(其中1100无限循环, 二进制)
   #对于python中的浮点数，仅取53位有效二进制位，因此0.1被近似为  
   11001100110011001100 11001100110011001100 1100110011001/2**56
   结果实际是等于0.09999999999999999167332731531133...
   ```

5. IEEE754中规定了浮点数的存储方法，大部分的计算机语言都采用该标准。==上一段需要修改==

6. Python可以使用科学计数法输入浮点数，可以直接处理复数。

   ```python
   a = 2.13e5  #科学计数法  2.13x10^5
   
   a = 2+3j    #虚数单位使用j,而不是i。
   b = 3+2j
   b.imag      #b的虚部2.0, 复数的实部和虚部都是浮点数，即使定义是使用的整数。b.real表示实部。
   a*b         #结果为13j
   ```

7. Python的除法，python3和2关于/的定义不同。

   ```python
   10 % 3   #除法求余 =1
   10//3    #除法求整数商 =3
   10/3     #浮点数除法 =3.3333333333333335 在python2中，结果为3
   #在python2程序中可以使用如下方法来使用python3的特性
   from __future__ import division
   #取余运算可以对负数或浮点数进行，这要配合整除来计算。
   10//-3  #结果为-4，相当于10/-3的结果向下取整。
   -10//-3 #结果为3，
   #因此
   10%-3  #结果为-2，相当于10-(10//-3)*(-3)
   -10%-3 #结果为-1，相当于(-10)-(-10//-3)*(-3)
   ```

8. 幂次计算：

   ```python
   2**3   #表示2的3次方，这里不可以用^，^在python中表示按位异或。
   2**0.5 #表示根号2。
   -3**2  #结果为-9，而不是(-3)**2，因为乘方运算的优先级高于取相反数运算。
   ```

9. 二元操作符有对应的增强赋值版本，计算结果赋值为第一个操作数。

   ```python
   x += y     x -= y      x *= y    x /= y
   x //= y    x %= y      x **= y
   ```

10. 数字类型之间运算会生成“最宽”的类型，整数→浮点数→复数

11. Python还提供了一系列数值运算的内置函数

    ```python
    abs(-10)     #10
    divmod(10,3) #(3,1)  同时计算商和余数，存储在一个元组内。
    
    pow(2,3)     #8
    pow(2,3,5)   #3,还可以有第三个参数，会除以第三个参数取余数。
    
    #将浮点数圆整为最接近的整数。当两个整数一样接近时，圆整到偶数。
    round(1.5)   #结果为 2。
    round(2.5)   #结果为 2。
    #并不是完全的四舍五入，这并不是bug，因为大多数的小数无法精确地由浮点数表示。
    round(2.15,1) #2.1
    round(2.25,1) #2.2
    round(1.236,2) #保留2位小数,结果为1.24。
    round(1.236) #第二个参数默认为0,保留0位小数,即保留整数,结果为1
    
    max(1,3,2)   #3 参数数量不限。
    min(1,3,2)   #2
    ```

12. 而向下取整的floor函数，并不是内置函数，而是math库提供的。

    ```python
    #返回<=给定数的最大整数。
    import math
    math.floor(2.3)  #结果为2
    math.floor(2)    #结果为2
    #返回>=给定数的最小整数。
    math.ceil(2.3)   #结果为3 天花板函数，向上取整
    ```

13. 字符串转化为数值，数值截断函数：

    ```python
    int(123.45)  #123
    int("123")   #123,只能处理整数字符串。
    
    float(12)    #12.0
    float("1.23")#1.23,可以接受整数字符串。
    
    complex(4)   #4+0j
    ```

14. math模块的sqrt是无法计算负数的平方根的，因为它限定结果为实数，可以使用cmath模块来实现对复数的支持。python中没有纯虚数类型，可以看做是实部为0的复数，python天然支持复数的运算，虚数单位为j或J：

    ```python
    from math import sqrt
    sqrt(-1)       #会报错 ValueError: math domain error
    import cmath
    cmath.sqrt(-1) #结果为1j
    (1+2j)*(2+3J)  #结果为(-4+7j)
    ```

# 标准库

## os库

1. os库是Python标准库，可以处理路径操作（os.path子库），进程管理，环境参数等问题。

2. 路径处理的函数：

   ```python
   os.path.abspath(path)      #返回path在当前系统中的绝对路径
   os.path.abspath(".")       #结果为 'C:\\Users\\zj' 当前工作路径
   os.path.abspath("xxx.txt") #结果为 'C:\\Users\\zj\\xxx.txt'
   
   os.path.normpath(path)     #将path的表示形式归一化，统一使用\\来分隔路径。Unix使用/，Windows使用\
   os.path.normpath("C:/Users/zj/xxx.txt") #结果为 'C:\\Users\\zj\\xxx.txt'
   
   os.path.relpath(path)     #返回在当前工作目录下找到path所需要的相对路径
   os.path.relpath("c:/pye") #结果为 '..\\..\\pye'   其中当前工作目录为 'C:\\Users\\zj'。Windows操作系统中需要path和当前工作目录在同一个磁盘
   
   #以下两个函数不涉及文件系统操作，可以看作是纯字符串的操作。不过会自动识别/和\\路径分隔符
   os.path.dirname(path)     #返回路径path中的目录名称。
   os.path.dirname("C:\\Users\\zj\\xxx.txt")  #结果为  'C:\\Users\\zj'
   os.path.basename(path)                     #返回path中最后一段，可能是文件，也可能是目录。
   os.path.basename("C:\\Users\\zj\\xxx.txt") #结果为 'xxx.txt' 等 "C:\\Users\\zj\\xxx.txt".split("\\")[-1]
   os.path.basename("C:/Users/zj")      #结果为 'zj' 等价于  "C:/Users/zj".split("/")[-1]
   
   os.path.join(path,*paths)  #组合path和paths，返回一个路径字符串。一般将dirname和basename的结果用join连接起来。
   os.path.join(os.path.dirname("C:\\Users\\zj\\xxx.txt"),os.path.basename("C:\\Users\\zj\\xxx.txt"))   #结果为   "C:\\Users\\zj\\xxx.txt"
   os.path.join("C:/","User/zj","xxx.txt")    #结果为 'C:/User/zj\\xxx.txt'  也可以连接多段路径，推荐将最终的结果都进行normpath过程，这样结果中不会混杂/和\
   os.path.join("C:/","User/zj/","xxx.txt")   #结果为 'C:/User/zj/xxx.txt'   每段路径的末尾如果不加/，则会用默认的\\
   ```
   
4. 文件和目录处理的函数：

   ```python
   import os
   import glob
   base_dir = "E:/Code/wiznote"
   files = glob.glob(base_dir + "/*") # 获取base_dir目录下所有文件，完整路径名。使用"*"参数可以获取文件名。
   files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)] #使用目录名+文件名拼接。不拼接即可获得文件名。
   
   os.path.exists(path) #判断path对应的文件或目录是否存在，返回True或False
   os.path.exists("c:/Users")   #结果为 True
   
   os.path.isfile(path) #判断path所对应的是否是文件，且该文件存在。返回True或False
   os.path.isfile("C:/Users/zj/.viminfo")   #结果为 True
   
   os.path.isdir(path)  #判断path是否是目录，且该目录存在。返回True或False
   os.path.isdir("C:/Users/zj")  #结果为 True
   
   os.path.getsize(path) #返回path对应的文件或目录的大小的，以字节为单位。
   os.path.getsize("C:/Users/zj/.viminfo") #结果为 556
   os.path.getsize("C:/Users") #结果为 4096   如果path为目录，结果并非是递归计算期内所有文件的大小之和，而是目录文件的大小。目录文件中存储的是其内的文件名。
   ```
   
5. 文件时间的函数：

   ```python
   os.path.getatime(path)  #返回path对应的文件或目录最近一次访问的时间 access time，结果为浮点数，表示从1970年1月1日0点以来的秒数。可以使用time模块转化为常用的日期+时间
   os.path.getatime("C:/Users") #结果为 1657628862.8915646  若path无效，则会报错
   
   os.path.getmtime(path) #返回path对应的文件或目录最近一次修改的时间 modify time
   os.path.getmtime("C:/Users") #结果为 1645407479.886614
   
   os.path.getctime(path) #返回path对应的文件或目录的创建时间 create time
   os.path.getctime("C:/Users") #结果为 1575709424.5394998
   ```

6. ```python
   os.system(command)  #command为命令字符串，调用shell或cmd来执行该命令。返回值为command的返回值。
   os.chdir(path)     #改变程序的当前工作目录
   os.getcwd()        #获取程序的当前工作目录
   os.getlogin()      #获取当前系统登录的用户名称
   os.cpu_count       #获取当前系统的cpu核心数量，包括超线程
   ```

7. 其他功能：

   ```python
   os.urandom(n)   #获得由n个随机字符组成的字节序列, bytes类型。通常用于加解密运算。
   os.urandom(5)   #b'\xa2l\xcf\\5'   字节序列，不能被打印出来的字符使用\x后面的2位16进制数表示。5个字符用list表示为  ['\xa2',l,'\xcf','\\',5]
   ```

## time库

1. time库是处理时间的标准库，提供系统级的精确时间：

   ```python
   #时间获取：
   time.time()   #获取当前的时间戳，浮点数，从1970年1月1日0点开始计算的秒数。例如：1657630829.0910866
   time.ctime()  #获取当前时间并以易读的方式表示，返回字符串 'Tue Jul 12 21:00:25 2022'
   time.gmtime() #获取当前时间，返回一个struct_time类型的对象 time.struct_time(tm_year=2022, tm_mon=7, tm_mday=12, tm_hour=13, tm_min=1, tm_sec=27, tm_wday=1, tm_yday=193, tm_isdst=0)   分别为年月日，时分秒，周几，一年的第几天，是否是夏令时
   
   time.strftime(tpl,ts)  #将struct_time类型的对象ts时间以tpl的格式输出。
   time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())  #结果为 '2022-07-12 14:47:44'  其中M为分钟，m为月。
   
   time.strftime("%A %a %H %I %p",time.gmtime()) #结果为 'Tuesday Tue 15 03 PM'  %A和%a分别表示星期的全拼和缩写。%H和%I分别表示24时制和12时制下的小时。%p为上下午。
   
   #用第二个参数的形式来解析第一个日期时间字符串参数，构造struct_time对象并返回。
   time.strptime('2022-07-12 14:47:44',"%Y-%m-%d %H:%M:%S")  #结果为 time.struct_time(tm_year=2022, tm_mon=7, tm_mday=12, tm_hour=14, tm_min=47, tm_sec=44, tm_wday=1, tm_yday=193, tm_isdst=-1)
   
   time.sleep(3)  #程序计时和休眠，单位是秒。
   
   time.perf_counter()  #返回一个CPU级别的精确时间浮点计数值，单位为秒。具体值没有意义，计算两次调用的时间差才可以。
   start=time.perf_counter()
   end=time.perf_counter()
   end-start #结果为 2.0499923266470432e-05
   ```
   
2. 一个进度条程序：

   ```python
   import time
   scale = 30
   print('执行开始'.center(scale+9,'-'))
   start = time.perf_counter()
   for i in range(scale+1):
       a = '*'*i
       b = '.'*(scale-i)
       c = i/scale*100
       dur = time.perf_counter()-start
       print("\r{:>3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')  #\r 只回车，不换行，这样新的输出会覆盖掉原来的
       time.sleep(0.1)  #避免输出过快
   #print('')
   print('\n'+'执行结束'.center(scale+9,'-'))
   ```


## Random库

1. random库是标准库，计算机不能产生真正的随机数，只能产生伪随机数，在统计意义上满足某种概率分布。也就是用梅森旋转算法生成的伪随机序列中的元素。伪随机数对于需要一定随机性，但又要保证能够复现过去的情况时，非常有用，但是由于是完全确定的，不适合用在加密领域。

2. 根据种子来产生随机序列，只要种子相同，随机序列也就一样。每次调用random.random()，都会从随机序列中依次取出随机数。除非用random.seed()刷新随机数种子。

   ```python
   random.seed(1)  #设置随机数序列的种子，默认为当前系统时间，如果不显式调用该函数，也会设置种子，为第一次使用random的时间。
   random.random() # 0.13436424411240122   随机数的取值范围为 [0,1)均匀分布的浮点数
   random.random() # 0.8474337369372327
   random.seed(1) #重新设置种子，从生成的序列开头取值。
   random.random() # 0.13436424411240122
   random.random() # 0.8474337369372327
   ```

3. 所有的random库的随机函数共享一个seed，几乎都是基于random函数来构造的：

   ```python
   #randint函数可以生成边界上的数。
   random.randint(10,100)  #生成一个[10,100]之间的整数  结果为37
   random.randrange(10,100,10) #生成一个[10,100]之间以10位步长的随机整数，第三个参数可以省略，默认为1。  结果为 20
   random.getrandbits(5)  #具有k个随机2进制位的非负Python整数, 也就是0b10111。结果为 23
   random.uniform(10,15)  #生成一个[10,15]之间的随机小数，结果为11.108458331365176
   random.choice([2,6,8,1,22,45])  #从序列中随机选择一个元素 结果为 45
   a =[1,2,3,4,5,6]
   random.shuffle(a) # 将序列的元素打乱，会修改参数，并不会返回修改后的序列。此时a=[3, 1, 5, 4, 6, 2]
   random.randbytes(5)  #结果为 b'\xd4T\x9ep+' 功能和os.urandom(5)一样
   random.gauss(mu=0.0, sigma=1.0) #正态分布，mu为平均值，sigma为标准差
   ```

# 异常处理

1. 异常处理。

   ```python
   try:
       <语句块1>
   except:   #任何异常发生时都会捕获，并执行语句块2
       <语句块2>
   
   try:
       <语句块1>
   except <异常类型> as exceptobj:  #只会捕获对应的异常类型，并用exceptobj名称保存异常对象，此时语句块2才会执行。
       <语句块2>
   ```
   
2. 异常处理的高级使用，无异常时，执行逻辑为1→3→4。发生异常时，执行逻辑为：1→2→4。

   ```python
   try:
       <语句块1>
   except:
       <语句块2>
   else:     #不发生异常时，才会执行
       <语句块3>
   finally:  #无论如何都会执行，释放资源的操作会放在这里
       <语句块4>
   ```

# 函数

## 定义与调用

1. 函数是基本的代码抽象。方法和函数不同，前者是面向对象中的专有名词，方法本身也是函数，不过要使用对象.函数名()的方法来使用。

2. 函数定义中的参数是占位符。实参会赋值给形参。定义时没有参数也要保留括号。可以为某些参数指定默认值，成为可选参数，需要放在非可选参数的后面。函数的用法说明中，如果某个参数是可以省略的，则在它的两侧加上方括号。

   ```python
   def <函数名>(<任意多个参数>):
       <函数体>
   	return <返回值>   #return也是函数体内一条普通的语句, 因此也应该缩进
   ```

3. 从定义角度来看，函数的参数分为必选参数和可选参数（默认参数），后者在定义时有=给出默认值。必选参数一定要在可选参数前面，否则会报错 SyntaxError: non-default argument follows default argument

4. 从调用角度来看，函数的参数分为位置参数和关键字参数。位置参数会按照定义的顺序来传递，关键字参数可以不按照该顺序，位置参数必须要在关键字参数前，否则会报错 SyntaxError: positional argument follows keyword argument

   ```python
   def f(x, y=1, z=3):
       print("x={}, y={}, z={}".format(x,y,z))
   
   f(1, y=2, z= 3)  #正确，x=1,y=2,z=3
   f(x=1, 2)        #错误，位置参数应该放到关键字参数前
   f(x=1, y=2, z=3) #正确，x=1,y=2,z=3
   f(1, x=2, z=3)   #错误，x被赋值了两次
   f(1,,3)          #错误，语法不允许，如果想要只给z赋值，而绕过y，可以使用关键字参数f(1,z=3)
   ```

5. 定义和调用中的参数类型没有任何关系。

6. 调用函数时参数的传递可以默认的按照位置传递，也可以按照名称以关键字参数方式传递。

   ```python
   def f(a,b):
       pass
   f(1,2)  #等价于f(a=1,b=2)
   f(b=2,a=1) #可以不按照参数顺序调用
   ```

7. 函数定义中还可以存在可变参数：参数的数量不确定，0或任意多个。例如系统自定义的max和min函数。

   ```python
   #  *args,可变位置参数，接受剩下的所有按照位置传入的参数，元组类型。即使只有一个可变的位置参数，也会构成一个元组。
   #  **kw,可变关键字参数,接受剩下的所有按照关键字传入的参数，字典类型。
   # 以上标识符args和kw可以是任意的，只要*的个数正确就行。定义是，*args一定要在**kw之前。
   def func(a,b,*args, **kw):
       print(args)
       print(kw)
   func(10, 20, 30, c=20, d=40) #args=(30,)  kw={"c":20,"d":40}
   ```

8. 函数定义中，可变位置参数可以放在必选参数前，但是在调用时，必选参数必须要用关键字参数的形式传入，否则无法区分该参数时要给args还是b：

   ```python
   def demo_func(*args, b):  #定义没问题
   	print(args)
   	print(b)
   demo_func(1, 2, 100)   #会出错，因为args会拦截1,2,100，导致没有参数传给b
   demo_func(1, 2, b=100) #正常运行
   ```

9. 从Python3.8开始，函数的定义中，参数位置允许出现/和*。

   ```python
   def f1(a, b, /): # /之前的参数必须使用位置传参，不能使用关键字传参
       return a + b
   def f1(a, *, b, c): # *之后的参数必须使用关键字传参，不能使用位置传参
       return a + b + c
   #标准库中的一些用法
   sorted(iterable, /, *, key=None, reverse=False) #第一个参数只能使用位置传参，key和reverse只能使用关键字传参。
   ```

10. 函数定义中可以有return，也可以没有，没有的话默认返回None。return可以返回多个返回值，用逗号分隔。

   ```python
   def f():
       return 1,2  #可以一次返回多个值，实际上是将1和2构成了一个元组(1,2)
   a,b = f()     #用多个变量来分别接受返回值。
   ```

11. 函数的参数传递实际上是对象的地址，如果实参是引用数据类型（列表，字典等），则在函数内部修改后，会影响到外部。


## 递归

1. 递归：在函数定义中调用函数自身的方式，例如阶乘计算，斐波那契数计算。

2. 递归中存在一个调用链条，还有基例，基例是一个或多个不需要递归的东西。二者缺一不可。一层一层深入，再一层一层跳出。

3. 递归的定义需要通过函数和分支语句(判断输入参数)来实现。

4. ```python
   def fact(n):  #计算n的阶乘
       if n==0:
           return 1
       else:
           return n*fact(n-1)
   def rvs(s):  #将字符串逆序
       if s == "" :
           return s
       else:
           return rvs(s[1:])+s[0]
   ```

5. 汉诺塔问题：

   ```python
   count = 0
   def hanoi(n,src,dst,mid): #先将前n-1层从src搬到mid，然后将第n层从src搬到dst，最后将前n-1层从mid搬到dst
       global count
       if n == 1:
           print("{}:{}->{}".format(1,src,dst))
           count +=1
       else:
           hanoi(n-1,src,mid,dst)
           print("{}:{}->{}".format(n,src,dst))
           count +=1
           hanoi(n-1,mid,dst,src)
   hanoi(4,"A","C","B")
   print(count)
   ```

## 匿名函数

1. 匿名函数就是没有标识符的函数，使用lambda表达式来定义，一般用于简单的能在一行实现的函数。

2. lambda表达式返回函数名，参数不用加括号，也可以没有参数，表达式的结果将会作为调用该函数的返回值输出。

   ```python
   # <函数名> = lambda <参数>: <表达式>
   f = lambda x,y:x+y      #f(2,5)结果为7。
   #也可以直接在定义的时候调用
   (lambda x,y:x+y)(2,5)  #结果为7
   #带if else的
   lambda x, y: x if x < y else y  #输出较小的那个参数，这里用到了二分支结构的紧凑形式
   func = lambda n:1 if n == 0 else n * func(n-1)  #也可以递归定义
   ```

3. 谨慎使用lambda函数，还是应该使用def，它的存在主要是用于一些特定函数或方法的参数。复杂功能的lambda表达式写法比较怪异，可读性相对较差。

## 高级函数 map filter reduce

1. map函数的第一个参数是函数，可以是lambda表达式，第二个参数是可迭代对象，将第二个参数中的每一个元素作为参数依次传入第一个参数中。python2中返回列表，python3中返回迭代器。

   ```python
   mapiter = map(lambda x:x*2,[1,2,3,4,5])
   from collections.abc import Iterable
   isinstance(mapiter,Iterable)  #结果为True，证明返回值为迭代器
   list(mapiter)  #使用list将迭代器转化为列表[2, 4, 6, 8, 10]
   
   list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])) #后续的参数可以有多个，不过要和lambda表达式的参数匹配。[3, 7, 11, 15, 19]
   ```

2. filter函数和map类似，也是接受一个函数和一个可迭代对象。当函数返回True时，则元素会被保留下来存入到待返回的列表中，反之，舍去。python2中返回列表，python3中返回迭代器。

   ```python
   filteriter = filter(lambda x: x < 0,[-2,-1,1,2,3]) #过滤出<0的元素
   list (filteriter)  #结果为 [-2, -1]
   ```

3. reduce函数也是类似的，先对序列的前几个元素调用函数，然后将得到的结果和后续元素再传入函数调用，直到没有后续元素为止。

   ```python
   from functools import reduce  #需要先import
   func = lambda x,y: x+y
   reduce(func, [1,2,3,4,5])  #相当于func(1,2)，在调用func(func(1,2),2)，持续调用下去。结果为15。
   # 第一步之后变为 reduce(func, [func(1,2),3,4,5])  类似于减而知之 reduce and conquer
   ```

## 反射 自省

1. 自省instrospection，表示自我检查的能力。告诉别人我是谁，我可以做什么。python是一门动态语言，支持自省，能够让程序在运行时动态获取对象的类型和属性，方法等，像C语言这样的静态语言，需要调用何种函数，必须要在编译前就写明。

   ```python
   #dir函数: 它返回参数的属性名称经过排序的列表。如果不指定对象，则返回当前作用域中的名称。
   dir(json)
   ['JSONDecodeError',
    ...
    'scanner']
   #hasattr函数: 测试一个对象是否包含某个属性
   hasattr(json,"decoder") #结果为 True
   #getattr函数: 获取对象的某个属性
   getattr(json,"__path__")  #等价于json.__path__。结果为['D:\\Python310\\lib\\json']
   #id函数: 返回对象的唯一标识符，整数
   id(1)  #结果为 2929349165296
   #isinstance: 判断一个对象是否是某个类型的实例
   isinstance("sds",str)  #结果为 True
   #callable: 判断一个对象是否是可以被调用的，即可以执行 对象()操作。
   callable("sd") #结果为 False
   callable(str)  #结果为 True
   ```

2. type是一个python的内建类，构造函数参数可以是任意类型的对象，返回参数对象的类型，可以使用盖type对象构建新的同类型的对象

   ```python
   type([]) == list  #结果为True, 并不等于"list"
   type([])(map(str, [1,2,3,4]))  #相当于list(map(str, [1,2,3,4]))
   ['1', '2', '3', '4']
   ```

3. 对于库特有的方法：

   ```python
   json.__doc__  #返回库的文档字符串，输出内容和help(json)一样。
   json.__name__ #返回库定义时的名称，即使使用import ... as ...为它取了别名。结果为 'json'
   json.__file__ #返回库的文件路径，内建库没有这个属性。结果为 'D:\\Python310\\lib\\json\\__init__.py'
   json.__dict__ #将模块内可用的属性名-属性以字典的形式返回。
   ```

4. 对于类除了上述方法外，还有：

   ```python
   class class1:
   	pass
   
   print(class1.__module__ ) #查看定义该类的模块名称，用户自定义的类在__main__模块中
   '__main__'
   #如果将上述代码放入module1.py，然后在module2.py中from module1 import class1，此时结果为module1。
   class People: pass
   class Teenager(People): pass
   class Man: pass
   class Student(Teenager, Man): pass  #python支持多继承
   Student.__bases__  #获得直接父类构成的元组，不包括父类的父类。结果为 (__main__.Teenager, __main__.Man)
   ```

## 偏函数

1. 如果一个函数定义了多个位置参数，每次调用时都需要把这些参数一个一个传递进去，比较麻烦。而其中只有少部分参数是经常变化的，如果能够将不变的参数省略则可以方便很多。

   ```python
   from functools import partial
   
   def func(a,b,c):
       pass
   f1 = partial(func,b=2,c=3)  #构造了一个偏函数，只有1个参数，调用f1时，会将参数和定义偏函数时给的参数结合起来，转而调用func
   f1(1)  #相当于func(1,b=2,c=3)
   ```

## 泛型函数

1. 根据传入参数的类型不同，来调用不同的函数，称为泛型。python中称为singledispatch。只要是被singledispatch装饰的函数，就是一个泛型函数：

   ```python
   from functools import singledispatch
   
   @singledispatch
   def age(obj):  #如果没有匹配的类型，则调用这个函数
       print('请传入合法类型的参数！')
   
   @age.register(int)
   def _(age):
       print('我已经{}岁了。'.format(age))
   
   @age.register(str)
   def _(age):
       print('I am {} years old.'.format(age))
   
   age(23)  # 会调用第8行的函数
   age('twenty three')  # 会调用第12行的话桉树
   age(['23'])  # 会调用第4行的函数
   ```

## 装饰器

1. 有时候需要在现有的代码上增加功能，例如需要在func函数每次调用前后都做一些动作，一种选择是，找到所有的func调用，在每次调用前后都增加相同的内容，另一种选择就是使用装饰器，只需要定义一个装饰器，然后将装饰器安装到函数定义的地方即可。

2. 装饰器本质上是一个函数，可以让被装饰的函数在不需要任何代码变动的前提下改变其功能，装饰器函数的返回值是一个函数对象。

3. 函数还可以返回函数，利用这点可以实现装饰器：

   ```python
   def logger(func):  #定义装饰器,参数 func 是被装饰的函数
       def wrapper(*args, **kw):  #在函数内定义新函数，使用可变参数可以简化装饰器的编程
           print('准备开始执行：{} 函数:'.format(func.__name__))
           func(*args, **kw)  # 真正执行的是这行。
           print('执行完了。')  #wrapper函数的返回值为None
       return wrapper  #logger函数的返回值
   
   @logger  # 定义业务函数并进行装饰
   def add(x, y):
       print('{} + {} = {}'.format(x, y, x+y))
   add(200,50)  #执行被装饰函数，会转换为 logger(add)(200,50) 相当于wrapper(200,50)，此时wrapper的实参args为(200,50)，kw为None。因此最终会先执行第3行，再执行add(200,50)，最后执行第5行
   ```

4. 带参数的装饰器：

   ```python
   def say_hello(country): #定义装饰器
       def wrapper(func):
           def deco(*args, **kw):
               if country == "china":
                   print("你好!")
               elif country == "america":
                   print('hello.')
               else:
                   return
               func(*args, **kw) #真正执行函数的地方
           return deco
       return wrapper
   
   @say_hello("china") #安装带参数的装饰器
   def xiaoming(x):
       print(x)
       
   @say_hello("america") #安装带参数的装饰器
   def john(x):
       print(x)
       
   xiaoming(3)  # 调用被装饰函数,等价于  say_hello("china")(xiaoming)(3) 相当于 wrapper(xiaoming)(3) 相当于deco(3),会执行第5，10，16行
   john(3)  #也会调用deco(3)，但是会执行第7，10，16行
   ```


## 上下文管理器

1. Python在2.5版本时，引入了with语法，它是一种上下文管理协议，目的在于把try，except和finally 关键字和资源分配释放相关代码通通去掉，简化try….except….finlally的处理流程。

2. 只需要在类中实现上下文管理协议，这个类的实例就可以看作是一个上下文管理器。

3. with通过\_\_enter\_\_方法初始化，然后在\_\_exit\_\_中做善后以及处理异常。所以使用with处理的对象必须有\_\_enter\_\_和\_\_exit\_\_这两个方法。其中\__enter\_\_()方法在语句体（with语句包裹起来的代码块）执行之前运行，__exit\_\_()方法在语句体执行完毕后运行。

4. with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。

5. ```python
   with expression [as target]:    #expression：是一个需要执行的表达式，要求表达式的结果是一个上下文管理器。target：存储的是上下文管理器的__enter__函数的返回值，可以省略。
   
   class opened(object): #继承自object类
       def __init__(self,filename):  #构造函数
           self.handle=open(filename,encoding='utf-8')
           print("Resource init:{}".format(filename))
       def __enter__(self):
           print("[enter]: Allocate resource.")
           return self.handle  #这里返回的是open的返回值，是一个上下文管理器
       def __exit__(self,exc_type,exc_value,exc_trackback): #如果没有异常发生，则后三个参数都会是None。
           print("[Exit]: Free resource.")
           if exc_trackback is None:
               print("[Exit]:Exited without exception.")
               self.handle.close()
           else:
               print("[Exit]: Exited with exception raised.")
           return False # 可以省略return，缺省时返回None也是被看做是False。这个返回值如果为True，则解释器会认为异常已经被成功处理了，不需要再向上传递了。
   
   with opened('file0.log') as fp:
       for line in fp.readlines():
           print(line)
   ```

6. 程序的运行流程：

   1. 计算with后面的表达式，创建opened对象，此时会执行构造函数。
   2. 调用表达式返回对象的\_\_enter\_\_()方法。
   3. 将上一步返回值赋值给as后面的变量fp。fp=opend("file0.log").\_\_enter\_\_()。
   4. 执行with环境内的代码。
   5. 执行表达式返回对象的\_\_exit\_\_()方法。

7. with语句的等价变换：

   ```python
   with EXPRESSION as TARGET:
       SUITE
   #等价于以下操作
   manager = (EXPRESSION)  #先计算EXPRESSION的值
   enter = type(manager).__enter__  #获取上下文管理器的进入函数的地址
   exit = type(manager).__exit__    #获取上下文管理器的推出函数的地址
   value = enter(manager)  #调用进入函数
   hit_except = False #标记是否产生了异常的flag
   
   try:
       TARGET = value  #将进入函数的返回值赋值给TARGET
       SUITE           #执行with内部的语句块
   except:  #只有出现异常才会到这一步
       hit_except = True  #打标记
       if not exit(manager, *sys.exc_info()):  #调用退出函数，传递异常，sys.exec_info()会返回一个元组(type(e), e, e.__traceback__)，元组外边加上*可以展开为多个参数
           raise  #如果退出函数没有正确处理完成异常，则抛出异常，交由更高层处理
   finally:
       if not hit_except:  #如果没产生异常，则调用不带异常的退出函数，如果产生了异常不做任何动作，因为已经在第15行调用了带异常的退出函数
           exit(manager, None, None, None)
   
   ```

8. with可以有多个项：

   ```python
   with A() as a, B() as b:
       SUITE
   #等价于
   with A() as a:
       with B() as b:
           SUITE
   ```

9. python使用上下文管理器的原因是python崇尚简洁优雅的风格，使用with可以将异常处理从主代码中分离出来，增强代码的可读性。

10. 要使用上下文管理器，除了自定义类外，还可以使用contextlib，简化使用流程。

   ```python
   import contextlib
   ```

# 变量作用域

1. 一共有4种作用域，从上到下，依次查找标识符

   1. Local 局部
   2. Enclosing 闭包，函数外的函数中，也就是局部外的局部作用域
   3. Global 全局，不包含在任何局部作用域内的名称都属于全局
   4. Built-in 内建

2. 会影响变量作用域的有：

   ```python
   #函数,def lambda
   #类,class
   #关键字,global nolocal
   #库或模块,*.py
   #推导式,[],(),{}   #仅限python3，python2中会发生变量泄露
   ```

3. 闭包 Closure：函数式编程的一个重要概念，是指引用了自由变量的函数，这个被引用的自由变量将和这个函数一同存在，即使已经离开了创建它的环境。

4. 在外函数中定义了一个内函数，且内函数内部使用了外函数中的局部变量，并且外函数的返回值是内函数的函数名，这样就构成了一个闭包。一般情况下，函数结束时，会销毁所有内部定义的局部变量，但是闭包是一种特殊情况，因为外函数在结束时发现自己的某个局部变量还被一个内函数引用着，未来将会被使用到，此时就会将该局部变量绑定给内函数，而不释放掉，这样外函数就不用再关注这个局部变量了。

   ```python
   def deco():  #外函数
       name = "MING"
       def wrapper():  #内函数
           print(name) #内函数中使用到了外函数的局部变量
       return wrapper  #这里外函数deco返回内函数的函数名，否则之后将无法调用内函数
   
   deco()()  #结果为 "MING"
   ```

5. 一个闭包是由外部函数和内部函数构成的。闭包的三要素：

   1. 内外函数的嵌套定义

   2. 内函数使用到了外函数的局部变量

   3. 外函数的返回值是内函数对象

6. 局部变量是函数内部定义的，全局变量是位于所有函数外部的。函数的参数也是局部变量。

   ```python
   n,s,t=10,100,1000  #三个都是全局变量
   def f(n,s):   #定义函数
       s=1       #对局部变量形参进行赋值，局部变量将外部的重名变量屏蔽了
       n=2       #对局部变量形参进行赋值
       t=3       #这里是对全局变量赋值
   f(n,s)        #值传递
   print(n,s,t)  #n和s还是10和100，t变成了3
   ```

7. 变量的作用域一般都和定义的位置有关，但是还可以通过关键字修改，使之不符合常规。

8. 全局变量在函数内能被访问到，如果有重名局部变量则访问到的是那个局部变量。若此时还想访问全局变量，可以使用global关键字在函数内声明此处的变量为全局变量，此后，在该函数内，该标识符表示的都是全局变量。

   ```python
   n,s = 10,100
   def func(n):
       global s   #声明这里的s是外部定义的全局变量，而非新定义的局部变量，实际上这里也没法定义局部变量，因为定义局部变量的同时必须要赋值
   	s=3        #修改的是全局变量，从100变成3
       return s
   print(func(n),s)  #结果为3 3，s被修改了。
   ```

9. nonlocal关键字可以在闭包函数中，引用并使用闭包外函数的变量（并非全局的）：

   ```python
   def deco(): #外函数
       age = 10
       def wrapper(): #内函数
           nonlocal age  #如果没有这一句，会报错  UnboundLocalError: local variable 'age' referenced before assignment ，python3.11报错为 UnboundLocalError: cannot access local variable 'age' where it is not associated with a value，总结就是age必须要先赋值再引用
           age += 1  #如果不使用+= 一类的运算，也不用nonlocal关键字。
           age = 3   #如果只修改age，则会认为是在wrapper中新定义了一个变量，没有nonlocal也不会报错
           print(age)#如过只读取age，则会认为是第2行的变量，没有nonlocal也不会报错
       return wrapper
   deco()()
   ```

10. 前面定义的变量，可以在同块内的后面的函数内直接使用。不过不建议这样使用，建议使用参数传递进去。

    ```python
    ls = ["F","f"]    #全局变量
    def func(a):
        ls.append(a)      #此处的ls是上面的全局变量
        return ls
    func("C")     #结果为["F","f","C"]
    print(ls)     #结果为["F","f","C"]
    
    ls = ["F","f"]
    def func(a):
        ls = []           #创建了局部变量，屏蔽了全局变量
        ls.append(a)      #此处的ls是新创建的局部变量
        return ls
    func("C")             #局部变量ls被修改，然后函数退出后，由于被返回给了外部函数，因此引用计数并非为0，内存没有被销毁，结果为["C"]
    print(ls)             #此处打印的是全局变量，并未被修改，仍然是["F","f"]
    ```

11. 变量集合：

    ```python
    #globals函数，以字典的方式存储所有全局变量
    def foo():
        print("I am a func")
    globals().get("foo")()  #获取到foo函数，结果为 "I am a func"
    #locals函数，以字典的方式存储所有局部变量
    other = "test"
    def foo():
        a = 3
        for key,value in locals().items(): #只有一个键值对，不包括other。
            print(key, "=", value)
    foo()  #输出 a=3
    ```

# 序列

1. 标准库用C实现了一系列序列类型，分为两类：
   1. 容器序列：list，tuple，collections.deque。可以存放不同的类型（包括用户自定义类型），实际存放的是指针。
   2. 扁平序列：str，bytes，bytearray，memoryview，array.array。只能存放一种类型，使用连续的内存空间存储数据本身。只能存放字符，字节，数值等基础类型。

2. 序列类型还可以根据能否被修改分类：
   1. 不可变序列：str，tuple，bytes。
   2. 可变序列：list，bytearray，array.array，collections.deque，memoryview。一般比不可变序列多提供一些修改自身的方法，例如insert，append方法。

3. 容器就是包含其他对象引用的对象，python中存在非序列的容器，例如集合，字典等。

4. collections.abc模块列举了一些构造内置序列类型时用到的抽象基类：

   ```python
   Container #类中包含__contains__特殊方法。
   Iterable  #类中包含__iter__特殊方法。
   Sized     #类中包含__len__特殊方法。
   Sequence  #类同时继承了上述3个类，同时还增加或重写了一些方法，__getitem__, __contains__, __iter__, __reversed__, index, count。
   MutableSequence #类继承了Sequence，同时同时还增加了一些方法，__setitem__, __delitem__, insert, append, reverse, extend, pop, remove, __iadd__
   ```

5. python支持一种数据结构的基本概念，容器container，也就是可以包含其他对象的对象。两种主要的容器为==序列和映射==。序列包含列表list，元组tuple，字符串str。映射包含字典dict。二者的主要区别时序列使用编号来索引元素，映射使用键来索引元素。还有一种既不是序列，也不是映射的容器，就是集合set。

6. str和bytes是python3特有的类型。

7. Python使用统一的风格来处理数据，不论是字符串，列表，还是字节序列等，他们共用一套操作：迭代，切片，排序，拼接等。

8. python程序员会默认序列可以进行+和*运算的。二者都不会修改原有的序列，python会构建一个新的序列。

9. 在对序列a进行`a*n`这样操作时，如果a中的元素是对其他可变对象的引用，那么新的序列中会有多个元素是指向同一个对象的引用。

   ```python
   x = [[1, 2]]*3 # 此时x为[[1, 2], [1, 2], [1, 2]]，因为[1, 2]是可变对象，因此[[1, 2]]的第0个元素实际上是一个对[1, 2]的引用，而*3会导致该引用被复制3次。
   x[0][0] = 3 # 此时x为[[3, 2], [3, 2], [3, 2]]
   #要想避免这种情况，可以使用列表推导式
   x = [[1, 2] for i in range(3)]
   #或使用for循环
   x = []
   for i in range(3):
       x.append([1, 2]) #每次添加的都是新构造的对象
   #但是不能使用如下的for循环
   x = []
   a = [1, 2]
   for i in range(3):
       x.append(a) #每次添加的都是同一个对象
   #如果a*n中的a中的元素是不可变对象的引用，
   ??a[0] = 3是修改了第0个元素指向的值，属于引用重新绑定？
   x = [1, 2]*3 #相当于[1, 2]+[1, 2]+[1, 2]，结果为[1, 2, 1, 2, 1, 2]
   x[0] = 5 #此时x为[5, 2, 1, 2, 1, 2]
   ```

10. 序列的增量赋值结果取决于第一个对象：

    ```python
    a += b #会先尝试调用a.__iadd__(b)这个特殊方法，如果该方法不存在，表达式就等价于a = a + b，分两步进行加法和赋值。由于赋值操作的存在，会将a绑定到其他位置，因此id(a)会变化。
    #一般来说，可变序列都会实现.__iadd__和.__add__方法，不可变序列只会实现.__add__方法。
    #观察id(a)的变化
    a = [1,2]     # id(a)为2106087749376
    a += [3,4]    # id(a)为2106087749376，此时a为[1, 2, 3, 4]
    a = a + [5,6] # id(a)为2106088734400，此时a为[1, 2, 3, 4, 5, 6]
    #如果a是不可变序列
    a = (1,2)  # id(a)为2106088792640
    a += (3,4) # id(a)为2106087631152，此时a为(1, 2, 3, 4)
    ```

11. 对不可变序列进行拼接操作，时间和空间效率很低，因为会产生临时对象，将原先的数据复制进去，再复制新的数据。

12. 不可变性对元组来说，意味着它的元素不支持赋值操作，但是可以通过+=来修改元素的值。因此不要把可变对象放到元组中：

    ```python
    t = (1, 2, [30, 40])
    t[2] += [50, 60] # 会报错TypeError: 'tuple' object does not support item assignment，但是也会修改t，此时t为(1, 2, [30, 40, 50, 60])
    #增量赋值不是原子操作，这里+=操作被分解为两个步骤，因此虽然第二步抛出了异常，但是还是完成了第一步的操作：
    t[2].extend([50,60]) # 这一步将[30,40]变成了[30,40,50,60]，可以顺利完成，因为list是可变对象。
    t[2] = t[2] # 这一步会报错，因为t是元组，不支持元素的赋值。
    #可以使用dis模块的的dis函数来对CPython进行反汇编，然后分析具体的操作。
    import dis
    dis.dis("t[2] += [50, 60]") #输出为
    #行号   指令的字节编号 指令的操作码   指令的操作数
    0           0 RESUME                   0
    1           2 LOAD_NAME                0 (t) #将co_names[0](即t)入栈，栈顶为STACK[-1]，栈底为STACK[0]
                4 LOAD_CONST               0 (2) #将co_consts[0](即2)入栈，
                6 COPY                     2 #将STACK[-2]追加到栈顶，但是不从原有的位置删除
                8 COPY                     2
               10 BINARY_SUBSCR #binary表示二元操作，subscr表示下标，这个指令会从栈顶弹出key和container，然后在栈顶追加上container[key]
               20 LOAD_CONST               1 (50)
               22 LOAD_CONST               2 (60)
               24 BUILD_LIST               2 #使用栈顶的2个元素创建一个list，然后将该list入栈
               26 BINARY_OP               13 (+=) #执行二元操作+=，此时栈顶为[50,60]的引用，次栈顶为t[2]的引用
               30 SWAP                     3 #将STACK[-3]和STACK[-1]交换。
               32 SWAP                     2 #将STACK[-2]和STACK[-1]交换。
               34 STORE_SUBSCR #从栈顶依次获取key, container, value，执行container[key] = value。经过上面的交换，栈顶向下依次为2,t,t[2]。因此会执行t[2] = t[2]。等号右侧的t[2]是之前就地追加产生的。这一步会报错，因为t是元组，不知道元素的赋值。
               38 LOAD_CONST               3 (None) #将None入栈
               40 RETURN_VALUE #将栈顶元素作为返回值返回
    ```

## 列表

1. 序列类型：具有先后关系的一组元素，元素类型可以不同，元素可以重复，类似于一维向量。有三个派生类型：列表，元组，字符串。

2. 序列是一个基类，从0开始索引，可以有多维索引，a\[2][1]。

3. 在大多数情况下都可以使用列表来替代元组类型，一种例外情况是：==元组可以用作字典的键，而列表不可以==，因为字典的键是不可以修改的。

4. 列表的创建，可以先创建一个空的列表，然后在append元素。也可以先创建一个具有多个None元素的列表，然后逐个赋值。

   ```python
   [1,2,3,4] == list([1,2,3,4]) #结果为True。可以用[]符号创建,也可以用list类的构造函数。
   a = [i for i in range(1,6)]  #使用列表推导式，结果为a=[1, 2, 3, 4, 5]
   [ ]     #空列表,其内什么也没有,长度为0,list类型。等价于list()。
   [None]  #非空列表，一般用来占位，长度为1,list类型，None是NoneType类型的对象。
   #如果要产生一个10元素的空列表，可以用None来占位
   x = [None]*10 #不能使用[]*10,因为这样还是[],长度还是0。
   ```

5. 序列的操作函数与方法： 

   ```python
   3 in [3,5,"a"]       #True,判断元素3是否为列表的元素,也可以是元组。
   2 not in [3,5,"a"]   #True
   [1,"a"] + [3,5]      #结果为[1, 'a', 3, 5],将两个列表拼接。不能对元组进行该操作。不同类型的序列数据也不能直接相加。
   [1,"a"]*3            #结果为[1, 'a', 1, 'a', 1, 'a'],可以是元组，这么做并不会修改序列。
   [1,"a",4][1]         #索引,结果为str类型。可以对元组进行该操作。
   [1,"a",4][-1]        #索引的编号可以为负数,结果等价于x[-n] == x[len(x)-n],其中n>0。
   [1,"a",4][1:2]       #切片,结果为list类型。
   [1,2,3,4,5,6][1:5:2] #结果为[2, 4],分别取[1],[3]的元素，构成一个新的list。
   ```

6. 内置函数，len计算长度，max和min函数需要序列的元素是可比的。

   ```python
   s = [1,2,3,4,5,6,7,8,9]
   len(s)     #容器的大小,即元素个数9
   max(s)     #结果为9
   min(s)     #结果为1
   s.index(2) #结果为1 在序列中查找第一个值为2的元素,并返回下标。如果找不到对应元素，会报ValueError。
   s.index(5,1,8) #结果为4,在[1,8)范围内寻找元素5,并返回下标(原始的下标)。
   s.count(2) #结果为1,返回序列中出现元素2的次数。
   ```

7. 可以用任何序列来初始化列表对象，即构造函数的参数。

   ```python
   list("Hello") #结果为["H", "e", "l", "l", "o"]将字符串转换为字符列表,这样就可以进行修改了。
   "".join(l1)   #结果为'Hello',可以将字符列表转换为字符串。
   x = [1, 2, 3]
   x[6] = 1     #不能给不存在的元素赋值。
   del x[1]     #x为[1,3],从列表中删除特定元素,该操作会修改x。
   del x        #删除标识符x。
   del x[:]     #删除x中的所有元素，相当于x.clear()。
   ```

8. 列表方法：

   ```python
   x = [1,2,3]
   x.append(4)  #x为[1, 2, 3, 4],将一个对象附加到列表的末尾。方法返回NoneType,而不是修改后的列表。
   x.clear()    #将x清空为空列表[],等价于x[:] = []
   y = x        #默认浅拷贝,此时y和x指向同一块内存,修改会互相影响。
   y = x.copy() #深拷贝,两块内存,修改不影响。等价于y = x[:];y =list(a)，都是深拷贝。
   
   x = [1,2,3,4,5]
   x.extend([7,8]) #拼接列表,x为[1, 2, 3, 4, 5, 7, 8],相当于多次append。
   x+[7,8]         #结果同上，但是不修改x,这个称为常规拼接。
   x.insert(3,"h") #x为[1,2,3,"h",4,5],在x[3]前面插入一个对象。
   #列表可以当做栈来使用
   x.pop()         #删除并返回列表的最后一个元素。pop是唯一一个既修改列表又返回非None值的方法。
   x.append(1)     #在列表末尾添加一个元素1。Python的列表没有push方法,可以用append替代。
   #列表可以当做队列使用
   x.pop(0)        #将x[0]从列表中弹出并删除,相当于出队。
   x.append("w")   #入队操作。
   x.remove("h")   #删除元素"h",如果有多个，只删除最前面的那个元素。返回None。和pop不同的是，它是通过值来删除，pop时通过编号来删除。
   x.reverse()     #逆序当前列表,返回None。还有一种逆序的方法x[::-1]，不过不会修改x。
   reversed(x)     #内置函数，返回一个逆序的迭代器,用于逆序遍历。
   ```


## 元组

1. 元组不仅仅是不可变的列表，还是没有字段名的记录（字段的集合）。

2. 元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置。列表可以进行排序，然而元组不可以，因为元组中各个元素的含义和它们的位置有关系。元组没有sort方法，但是仍可以使用sorted函数排序，结果并非元组，而是一个新的列表。

3. 函数返回多个值时，实际上是返回了一个元组。

4. 元组拆包Unpacking的应用：

   ```python
   #将一个元组同时赋值给多个变量，这被称作平行赋值，因为等号左侧也构成了一个元组
   x = (1,2,3,4)
   a, b, _, d = x  #这里的_是占位符，某个元素不想要的话，可以使用_占位。如果程序是国际化的，那就不推荐使用_来做占位符，因为它常被用来当作gettext.gettext函数的别名。
   a, *args, d = x #使用*来接收拆包剩余的元素,只能出现一次,args为[2,3]，这里借鉴了函数中不定量参数的写法。
   y = (1,2,(3,4))
   a,b,(c,d) = y   #拆包可以嵌套进行，等号两侧的结构需要一一对应。
   a,b = b,a       #不使用中间变量来交换两个变量的值
   #使用*运算符拆包，使之作为函数的实参。所有的可迭代对象都可以这么使用
   def func(a,b,c):
       print(a,b,c)
   x = (1,2,3)
   func(x)  #会报错，需要使用func(*x)
   ```

5. 在python3之前，元组可以作为形参放在函数声明中，例如`def func(a,b,(c,d))`，然而python3中不再支持这种写法，这个改变对函数调用者并没有影响，它改变的是某些函数的声明方式。

6. 如果需要给记录中的字段命名，可以使用具名元组namedtuple函数。

   ```python
   import collections
   Card = collections.namedtuple("Card",["rank","suit"]) #该函数是一个工厂函数，可以用来构建一个带字段名的元组和一个有名字的类。该函数的第二个参数也可以为"rank suit"或("rank","suit")。
   #类名是第一个参数，而不是等号左侧的Card，因为它可以赋值给其他变量。
   CC = Card
   CC("3","Δ") #创建一个对象，Card(rank='3', suit='Δ')
   #使用namedtuple构建的类的对象和元组占用一样的内存，因为对象的字段名都保存在类中。这个类的对象跟普通类的对象比起来也要小一些，因为python不会使用__dict__来存放这些实例的属性。
   card1 = Card("3","Δ") #构造一个元组，可以使用字段名或位置来获取元素的字段值。
   ```

7. 具名元组特有的功能：

   ```python
   Card._fields    #类属性，获得所有字段名，结果为 ('rank', 'suit')
   Card._make(["2","Δ"]) #类方法，参数为一个可迭代对象，用来生成这个类的一个实例，等价于Card(*["2","Δ"])
   card1._asdict() #实例方法，转化为collections.OrderedDict字典，结果为 {'rank': '3', 'suit': 'Δ'}
   ```

8. 除了列表的增减元素的方法（例如就地拼接，就地逆序排列）外，元组支持列表其他所有方法。一个例外是，元组没有返回逆序迭代器的`__reversed__`方法，不过reverse(my_tuple)在没有`__reversed__`时，也可以调用成功，返回一个逆序迭代器。

9. 元组是序列类型的扩展，一旦创建就不能被修改。

   ```python
   () == tuple()  #创建空元组的两种方法
   a = (1,2,3)    #括号可以省略
   return 1,2     #等价于 return (1,2)
   #创建只有一个元素的元组
   a = 2,         #等价于a = (2,),是tuple类型。
   2 == (2)       #结果为True,(2)是int类型。
   ```

10. 元组和列表的相互转化：

    ```python
    atuple = (1,2,3,4)
    b = list(atuple) # b=[1,2,3,4]
    
    b=[1,2,3,4]
    atuple = tuple(b) #atuple = (1,2,3,4)
    ```

## 数组

1. 列表底层存放的是对象，而数组底层存放的是字节表述。

2. 如果列表的所有元素都是数值，那么可以使用内置数组来替代。python内置的数组和C语言数组一样精简，创建数组需要一个类型码，用来指示在C底层如何放置数据，这样可以合理使用内存空间，python不允许在数组中存放指定类型以外的数据。

   ```python
   #类型码     对应的C语言数据类型 占用的最小字节数
   'b'         signed integer     1
   'B'         unsigned integer   1
   'u'         Unicode character  2 (see note)
   'h'         signed integer     2
   'H'         unsigned integer   2
   'i'         signed integer     2
   'I'         unsigned integer   2
   'l'         signed integer     4
   'L'         unsigned integer   4
   'q'         signed integer     8 (see note)
   'Q'         unsigned integer   8 (see note)
   'f'         floating point     4
   'd'         floating point     8
   ```

3. 创建一个有1000万个随机浮点数的数组，将其写入到文件中，然后再从文件中读出：

   ```python
   import array
   import random
   floats = array.array("d",(random.random() for i in range(10**7))) #d表示双精度浮点
   fp = open("floats.bin","wb") #以2进制形式打开文件
   floats.tofile(fp) #将数组写入文件
   fp.close()
   fp = open("floats.bin","rb")
   floats2 = array.array("d") #创建一个空的数组，元素类型为双精度浮点
   floats2.fromfile(fp,10**7) #读如10**7个数据
   fp.close()
   ```

4. 将数组写入文件或从文件读入，都比文本文件的操作要快得多，大概2个数量级，因为文本文件还需要执行floats方法。同时二进制存储文件更节省空间，每个双精度浮点数占用8个字节，而使用文本文件存储，每个数字需要19个字节。

5. 还有一些特殊的数字数组类型，例如bytes和bytearray

6. 数组特有的操作：

   ```python
   s = array.array("l",(1,2,3)) #
   s.fromlist([4,5]) #从列表读入数据，添加到尾部
   s.itemsize  #数组中每个元素的占用的字节数
   s.tobytes() #转化成bytes对象，结果为 b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00'
   s.byteswap() #翻转数组内每个元素的字节序列，多字节元素会受到影响，默认为小端
   s.typecode #类型码，结果为 'l'
   ```

7. 从python3.4开始，数组不再支持类似list.sort的这种就地排序的方法，应该使用sorted函数新建一个数组。

   ```python
   a = array.array(a.typecode, sorted(a)) #sorted函数的返回始终为list，需要再构造成array
   ```


## Memory view

1. memoryview 内存视图是一个内置类，表示一块带解释方式的内存区域，能够让用户在不复制内容的情况下操作同一个数组的不同切片。它的出现受到了numpy的启发。它实际上是泛化的，去数学化的numpy数组。允许在不需要复制内容的前提下，在数据结构之间共享内存。

2. memory.cast和数组模块类似，能够以不同方式读写同一块内存区域，且cast操作不会改变内存字节，类似于C语言的类型转换。它会使用memoryview对象构造另一个memoryview对象。

   ```python
   numbers = array.array("h", [-2, -1, 0, 1, 2]) #双字节带符号整数
   numbers.tobytes() #内存中的字节序列，结果为 b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'
   memv = memoryview(numbers) #构造一个memoryview对象
   len(memv) #memoryview对象中的元素个数，结果为5
   memv.nbytes #内存区域的字节数
   memv.format #解释方式，结果为 'h'
   memv[1]  #第2个元素，结果为-1
   memv_oct = memv.cast("B") #将内存当作多个单字节的无符号整数来解析，产生一个新的memoryview对象，这一步并不会复制数据。
   len(memv_oct) #结果为 10
   l1 = memv_oct.tolist() #构造一个list，结果为[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
   memv_oct[5] = 4 #给对应的字节赋值，会修改numbers本身，结果为array('h', [-2, -1, 1024, 1, 2])，因为此时numbers.tobytes()为b'\xfe\xff\xff\xff\x00\x04\x01\x00\x02\x00'
   ```


## 双端队列

1. 利用append和pop(0)方法可以将list当作或栈队列来使用，但是删除列表的第一个元素或在第一个元素前添加元素比较耗时。

2. collections.deque类是一个线程安全的双向队列（线程之间合作交换数据常常喜欢使用队列），允许快速从两端插入或删除元素。双向队列允许指定大小上限，满了后再添加，会将另一端的元素挤出去。

   ```python
   from collections import deque
   d1 = deque(range(10),maxlen = 10) #构造一个双端队列，大小上线为10，这个属性一旦设定就不能更改了
   d1.rotate(3) #队列的旋转操作，类似于循环移位，n>0表示向右移动，n<0表示向左移动，结果为 deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
   d1.append(-1) #在右侧添加一个元素，结果为 deque([8, 9, 0, 1, 2, 3, 4, 5, 6, -1], maxlen=10)，会把原来的最右侧元素挤出去。d1.appendleft为在左侧插入单个元素
   d1.extend([-2,-3]) #将可迭代对象的元素依次插入到右侧，结果为deque([0, 1, 2, 3, 4, 5, 6, -1, -2, -3], maxlen=10)。d1.extendleft为将可迭代对象的元素依次插入到左侧。
   a = d1.pop() #将最右侧元素删除，并返回，结果为 a =-3，d1 =deque([0, 1, 2, 3, 4, 5, 6, -1, -2], maxlen=10)。d1.popleft为从最左侧删除并返回。
   ```

3. 双向队列也可以从中间删除元素，但是会慢些，因为它只对在头尾的操作进行了优化。

4. append和popleft都是原子操作，因此可以在多线程程序中安全使用，不用考虑资源锁的问题。

5. 除了collections.deque之外，python的如下模块也支持队列：

   1. queue模块，提供了线程安全的Queue，LifoQueue，PriorityQueue三个类。和collections.deque不同的时，他们在达到大小上限后，不会挤出另一端的元素，而是会将该线程锁住，直到有新的线程从队列中移除元素后，才会被解锁。
   2. multiprocessing模块，提供Queue，JoinableQueue类，专门用于进程间通信，可以让任务管理更方便。multiprocessing.Queue和queue.Queue功能相似。
   3. asyncio模块，在python3.4中提供，包含Queue，LifoQueue，PriorityQueue，JoinableQueue四个类，收到了queue和multiprocessing模块的影响，为异步编程的任务管理提供帮助。
   4. heapq模块，没有队列类，而是提供了heappush和heappop方法，让用户可以把可变序列当作堆队列或优先队列使用。

## 切片

1. 列表，字符串，元组都支持切片操作，切片和区间操作都不包含区间范围的最后一个元素，这是python的风格，这个习惯符合python和C语言中下标从0开始的传统，这样做的好处有：

   1. 当只有一个位置信息的时候，也可以快速看出切片的长度，`range(3)`和`my_list[:3]`都有3个元素。
   2. 当起止信息都有的时候，可以快速计算出切片的长度，`my_list[2:5]`中有5-2=3个元素。
   3. 可以使用任意一个下标将序列分为不重合的两部分，`my_list[:3]`和`my_list[3:]`。

2. `a:b:c`这种用法只能出现在`[ ]`内，索引是指`[ ]`内只有一个下标。

3. 切片的实际操作为：

   ```python
   my_list[a:b:c] #等价于my_list[slice(a,b,c)]，下标运算又会被转化为如下特殊方法的调用
   my_list.__getitem__(slice(a,b,c)) #会生成一个临时的切片对象。
   ```

4. `[ ]`内还可以使用逗号分隔的多个索引或切片，numpy.ndarray对象就支持这种写法。python内置的序列类型都是一维的，`[[1,2],[3,4]]`也是一维的，因此不支持numpy的这种写法。

   ```python
   a = numpy.array([1,2,3,4,5,6]).reshape((2,3))
   a[1,0] #要这么使用，需要在numpy.ndarray对象的__getitem__和__setitem__方法中以元组的形式来处理position参数。因为python会将a[i,j]转化为a.__getitem__((i,j))
   ```

5. 切片操作，左闭右开的区间：

   ```python
   x = [1,2,3,4,5,6]
   x[-3:-1] #结果为[4,5]
   x[-3:]   #结果为[4,5,6],第二个索引留空才会包含结尾的元素。不可以使用0来代替。
   x[-3:0]  #结果为[],当第一个索引指定的元素在第二个索引指定的元素后面时，结果就为空。
   x[4:2]   #结果为[]
   x[-2:2]  #结果也为[],因为-2可以当做-2%6=4。   这里的6等于len(x)+1。
   x[:3]    #等价于x[0:3],如果省略第一个索引，相当于该索引时0。
   x[:]     #等价于x本身。
   ```

6. 切片的步长默认为1，也可以为负数，但是不能为0：

   ```python
   x = [1,2,3,4,5,6,7]
   x[::2]   #结果为[1,3,5,7]
   x[:6:2]  #结果为[1,3,5]
   x[::-1]  #结果为[7, 6, 5, 4, 3, 2, 1]
   #如果步长是负数，那么第一个索引省略时默认为len(x)或者是-1,第二个索引省略时默认为0
   x[:3:-2] #结果为[7, 5],相当于x[-1],x[-3],...第二个索引相当于3-7=-4
   x[:1:-2] #结果为[7, 5, 3]
   ```

7. 切片赋值，如果赋值的对象是一个切片，则等号右侧必须是一个可迭代对象：

   ```python
   x = [1,2,3,4,5]
   x[2:] = [2,1]   #结果为[1,2,2,1]。将[2:]子序列替换为[2,1],子序列的替换,二者的长度可以不等。
   x[2:2] = [2,1]  #结果为[1,2,2,1,3,4,5]。将[2,2)子序列替换为[2,1],该子序列为空,实际就是在x[2]前面插入。
   x[1:3] = []     #结果为[1,4,5]。相当于将[1,3)子序列删除。等价于del x[1:3]
   del x[1:3] #结果为 x = [1,4,5]
   x[2:4] = 10 # 会报错，TypeError: can only assign an iterable
   ```

8. 省略的正确写法是三个英文句号`...`。python解释器将其当作Ellipsis对象的别名，Ellipsis对象是ellipsis类的唯一对象，类似于True和False是bool类的唯二对象。

   ```python
   print(...)      #结果为 Ellipsis
   ... == Ellipsis #结果为True
   type(...)       #结果为 ellipsis
   #可以用在类型提示中
   from typing import Tuple
   t2: tuple[int, ...] = (1, 2, 3,) # 声明t2为整数组成的元组
   #可以用在函数内部，相当于pass
   def foo2(): ...
   #可以用在numpy的索引中，相当于:
   arr2 = np.array([1,2,3,4,5,6]).reshape(2,3)
   arr2[1 , ...] #结果为array([4, 5, 6])，等价于arr2[1,:]
   ```

# 字典

1. 模块的命名空间，实例的属性，函数的关键字参数都隐式地使用到了字典，它是python的基石。python实现对字典做了高度的优化，散列表是字典性能出众的重要原因。集合的实现也依赖于散列表。

2. collections.abc模块中含有Mapping和MutableMapping两个抽象基类，它们为dict和其他类似的类型提供接口。在python2.6到3.2期间，这些类还属于collections模块，而不是collections.abc模块。

3. 一般来说，非抽象的映射类型一般不会直接继承自这些抽象基类，它们会直接对dict或collections.UserDict进行扩展，这些抽象基类的主要作用是作为形式化的文档，定义了构建一个映射类型所需要的基本接口，还可以使用isinstance来判定某个对象是否是映射类型。

   ```python
   import collections
   my_dict = {}
   isinstance(my_dict, collections.abc.Mapping) #结果为True，这里没有使用type是因为，映射类型不一定都是dict类型。
   ```

4. 标准库里的映射类型都是利用dict实现的。其他映射类型有：

   1. collections.OrderDict，这个类型在添加键时，会保持顺序，因此对键的迭代次序总是一致的。popitem方法有一个可选参数last，默认为True。此时遵循LIFO弹出，如果last为False，遵循FIFO弹出。

   2. collections.ChainMap，可以容纳数个不同的映射对象，像一个映射链。进行键查找时，会按顺序逐个查找，这个功能在给有嵌套作用域的语言做解释器时很有用。可以使用一个映射对象代表一个作用域的上下文。

   3. collections.Counter，该映射类型中键的值为一个整数，用来标记键出现的次数。该类型可以用来给可散列对象计数，或当作多重集合使用。Counter还实现了+，-操作，用来合并记录。

      ```python
      ct = collections.Counter('abracadabra') #ct为 Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
      ct.update('aaaaazzz') #ct为 Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
      ct["f"] #对于不存在的键，不会报KeyError异常，而是会返回0，表示计数为0
      ct["a"] += 1 #向多重集合ct中添加一个元素"a"
      ct.most_common(2) #结果为 [('a', 10), ('z', 3)] 按照次序返回映射里最常见的2个键和它们的计数。
      ```

   4. colllections.UserDict，其实就是把标准dict用纯Python又实现了一遍，目的就是为了让用户来继承，创建自定义映射类型的。它比dict好的点是：dict类会在某些方法的实现上走一些捷径，导致不得不在子类中重写这些方法。

      ```python
      #collections.UserDict并不是dict的子类，但是它有一个data的属性，该属性是dict的实例，它就是最终存储数据的地方。
      import collections
      class StrKeyDict(collections.UserDict): #继承
          def __missing__(self, key):
              if isinstance(key, str):
                  raise KeyError(key)
              return self[str(key)]
          def __contains__(self, key):
              return str(key) in self.data #这里就不用两次判断了，因为所有已存储的键都是字符串了。
          def __setitem__(self, key, item):
              self.data[str(key)] = item #将所有的键都转化成字符串。
      #UserDict继承自MutableMapping，后者又是从Mapping继承来的
      ```

5. 通过名称来访问值的数据结构称为映射，Python中唯一内置的映射类型是字典dict。除此之外，在collections模块中还有2个映射类型，defaultdict和OrderedDict。常见的方法如下：

6. 字典的键必须是可以hash的，例如字符串，数值等。值可以是任意对象，包括字典。

7. 键值对之间是无序的，这里的无序指的是不保证按照插入的顺序存放，并不是真正的没有顺序。键和值用：分隔，键值对之间用，分隔。

8. 创建字典的3种方法：

   ```python
   {} == dict()  #创建空字典的两种方法
   #使用使用关键字参数来调用dict类的构造函数
   d = dict(a = 1, b = 2, c = 3) #键不需要是加""
   #使用{}
   d = {"a":1,"b":2,"c":3}
   #字典推导式
   adict = {x: x**2 for x in (2, 4, 6)}  #结果为 {2: 4, 4: 16, 6: 36}
   #使用键值对的二维序列
   data = [("a",1),("b",2),("c",3)]  #[["a",1],["b",2],["c",3]]或(("a",1),("b",2),("c",3))也可以
   dict(data) #结果为 {'a': 1, 'b': 2, 'c': 3}。
   ```

9. 使用[]和键来进行索引。

   ```python
   d = {"a":1,"b":2,"c":3}
   d["a"]  #结果为1，会调用__getitem__特殊方法
   d["d"]  #会报KeyError错误
   d["d"] = 4 #向字典中添加新的键值对,如果对应的键已存在,则会修改值。
   #建议使用get方法
   d.get("d")  #结果为None
   d.get("d","default") #当没有对应的键时，返回第二个参数。
   ```

10. 常用的方法：

    ```python
    del d["a"]   #从字典中删除键为"a"的键值对。
    "b" in d     #判断字典中是否存在一个键为"b"的键值对。
    d.keys()     #返回字典中所有键的信息      dict_keys(['b', 'c'])
    d.values()   #返回字典中所有值的信息      dict_values([2, 3])
    d.items()    #返回字典中所有键值对的信息  dict_items([('b', 2), ('c', 3)])
    d.get("b","Not In")  #获取字典中键为"b"的键值对的值，如果不存在则返回None或第二个参数。这个函数比直接使用[]来获取值好点,后者当键不存在是会抛出异常。这一步并不会为字典增加一个键。函数的返回值可能是左值或右值，如果值为基本类型，则为左值，引用类型则为右值。
    d.pop("b","Not In")  #弹出字典中键为"b"的键值对的值，如果不存在则返回第二个参数。这个函数会修改字典本身。
    d.popitem()          #从字典中随机弹出一个键值对，以元组的形式返回。例如('a', 1)，Python3.7后，保证按照LIFO即栈的规则弹出。
    d.clear()            #删除所有键值对，清空字典。
    d.fromkeys(it, [initial]) #将迭代器it里的元素添加为字典的键，其值默认为None，如果有initial参数，将这些值设置为initial。
    d.__iter__() #获取键的迭代器
    d.setdefault(k, [default]) #如果键k存在则返回对应的值，如果不存在，则返回None或default，并增加一个键k。它和get的区别是，如果键不存在，它会增加一个键k，值为None或default，get不会。
    ```

11. 使用setdefault处理找不到键的情况：

    ```python
    #读取对应键的值可以使用d[k]或d.get(k, [default])，前者在找不到键时，会报异常，后者则不会，会返回None或提供的default参数。
    #使用上述两种方法，也可以来更改对应键的值。
    d = {"a":[1],"b":[2],"c":[3]} #例如现在要给特定键的值列表追加一个元素5
    d["a"].append(5) #可以直接更新，因为d[]返回的始终是左值，但是考虑到键可能不存在，一般不会使用d[k]
    d.get("a", []).append(5) #也可以正常完成，如果键不存在时，运行不会报错，但是并不会在d中添加一个键，并设置其值为[5]，而是将5追加到了get返回的一个临时的[]中。
    #可以使用如下形式
    tmp = d.get("f", [])
    tmp.append(5)
    d["f"] = tmp #这里d["f"]不会报错，因为当f不是d的键时，这一步会新增一个键，如果是的话，会修改该键对应的值。
    #也可以使用如下一条语句完成等价的功能
    d.setdefault("f",[]).append(5) #这一条语句只会进行1次键查询，上面要进行2次键查询。
    #如下例子的功能是，扫描一个文件，提取出其中的字母数字串，然后获得其行列号，添加到一个index的字典中，
    import sys
    import re
    WORD_RE = re.compile(r'\w+')
    index = {}
    with open("test.py", encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1): # line_no从1开始
            for match in WORD_RE.finditer(line):
                word = match.group() #获取匹配的结果
                column_no = match.start()+1 #匹配的位置，+1表示从1开始计数
                location = (line_no, column_no) #构造记录此次match位置的元组
                occurrences = index.get(word, []) #查询字典中是否已经存在这个字母数字串的键
                occurrences.append(location) #在[]或原有的列表上追加一个新的元组
                index[word] = occurrences #修改键对应的值
    #index字典中的一个键值对为如下形式："for":[(6, 5), (7, 9), (15, 1)]
    #以上程序的倒数三行完成的是一个查询并更新的工作，可以使用setdefault一条语句完成。
                index.setdefault(word, []).append(location)
    ```

12. d.keys()等方法返回的类型并不是列表，而是返回dict_keys等类型，都是可迭代对象，也可以用来构造list类型。

    ```python
    for key,value in t:   #错误，不能直接对t进行迭代
        pass
    for key in t.keys():  #可以采用这种方式进行迭代。可以省略keys()，直接对t进行迭代，结果一样。
        print(key,"  ",t[key])
    for key,value in t.items():  #每次迭代出来的是一个元组
        print(key,"  ",value)
    
    list(d.items())        #列表中每一项都是元组
    [('a', 1), ('b', 2), ('c', 3)]
    dict(list(d.items())) == d #结果为true,也可以用上面的元组列表来生成字典。每个元组构成一个键值对。
    ```

13. python2中，字典有一个haskey的方法，用来判断给定字典是否含有某个键。但这个方法在python3中取消了，使用 in 或not in代替。

    ```python
    d = {"a":1,"b":2,"c":3}
    d.haskey("c")   #True。仅在python2中有效。
    "c" in d  #True
    ```

14. 弹性键查询，有时为了方便起见，有时希望就算某个键不在映射里，也希望能读取到一个默认值，有两种办法：

    1. 使用defaultdict这个dict的派生类型：

       ```python
       #在创建defaultdict对象的时候，就需要提供一个可调用对象，该对象会在__getitem__找不到键时被调用，让__getitem__返回一个默认值。如果没有提供该可调用对象，default_factory属性为None，键不在时，会报错KeyError。
       #不过该可调用对象只会在__getitem__找不到键时被调用，如果使用dd.get(key)，找不到键时，不会调用该对象。这是因为__getitem__找不到键时，会调用__missing__特殊方法，而__missing__中又会调用default_factory。
       import collections
       dd = collections.defaultdict(list) #list就是提供的可调用对象
       dd.default_factory #结果为list，type类型，可调用对象存放在对象属性default_factory中
       dd["new-key"] #经检查new-key不在dd中，因此会将new-key:list()插入到dd中，并返回新的dd["new-key"]
       #此时dd为defaultdict(list, {'new-key': []})
       ```

    2. 自定义一个继承自dict的子类，实现`__missing__`方法：

       ```python
       #dict虽然没有定义__missing__方法，但是它知道它的存在，如果子类实现了__missing__方法，那么在__getitem__找不到键时就会调用该方法，而不是抛出KeyError异常
       #__missing__方法只会被__getitem__调用，它对get或__contains__没有影响。
       #构造一个映射类型，如果找不到的键是字符串，则抛出KeyError异常，如果不是字符串，则将其转化为字符串，再查找。
       class StrKeyDict0(dict): #继承自dict
           def __missing__(self, key):
               if isinstance(key, str): #这一步不能缺少，因为return语句会产生递归调用。如果没有这句，当key是字符串，且键不存在时，会无限递归调用return行。
                   raise KeyError(key)
               return self[str(key)]
           def get(self, key, default=None): #重写父类的方法
               try:
                   return self[key] #将.get()的工作委托给__getitem__特殊方法。
               except KeyError:
                   return default #如果键不存在，则返回default
           def __contains__(self, key): # in操作会调用这个函数。
               return key in self.keys() or str(key) in self.keys() #只要key或str(key)是字典的键就可以。这里不能使用key in self，因为会导致无限递归。必须采用显式方式查询。
       #像k in my_dict.keys()这样的操作在python3中是很快的，即使映射类型的元素很多也无所谓，因为my_dict.keys()返回的是一个视图，这个视图就像一个集合，查找元素很快。python2中返回的是一个列表，在列表中查找元素需要扫描整个列表。
       ```

15. 标准库里所有的映射类型都是可变的，不过有时会有不可变需求。从python3.3开始，types模块引入了一个封装类，MappingProxyType。如果给这个类一个映射，它会返回一个只读的映射视图。对原映射的修改会反映到这个视图上，不过无法通过视图修改映射。具体使用时，只把视图暴露给用户。

    ```python
    from types import MappingProxyType
    d = {1:'A'}
    d_proxy = MappingProxyType(d) #d为 mappingproxy({1: 'A'})
    d_proxy[2] = 'x' #会报错，TypeError: 'mappingproxy' object does not support item assignment
    d[2] = 'B' #通过原映射进行修改，此时视图中d_proxy[2]耶也变成了"B"
    ```

# 集合

1. Python的集合和数学上的集合类似，无序，不能重复，元素不可更改。在创建或后续添加元素时，会自动去重。集合不是序列，因为它是无序的。

2. set和forzenset在python2.3中首次以模块的形式出现，在python2.6中才升级为内置类型。

3. 集合中的元素必须为可散列的，而集合本身却是不可散列的，而frozenset是不可散列的。因此可以创建一个包含不同forzenset的set。

4. 不可变数据类型：整数，浮点数，复数，字符串，元组。

5. python的集合专门为in操作进行过优化，对于检查一个元素是否在一个范围中，集合的操作最快，得益于背后使用的散列表。

6. 集合的创建：

   ```python
   set()  #创建一个空集合，不能使用{},因为{}默认是生成空字典类型的，而非空集合。
   a = {1,2,"ab"} #使用字面量方式创建集合，效率比使用set方法快，frozenset没有这种方法。
   A = {"python","python",123,("python",123)} #使用{}建立集合，有三个元素，其中一个元素是元组
   {123,("python",123),"python"}    #可以看到顺序和建立集合时的顺序无关，且重复的元素会被删除
   B = set("pypy123")  #结果为{'1', '2', '3', 'p', 'y'} 参数应为可迭代的对象，例如字符串或者列表等
   B=set([1,2,3,4])        #结果为 {1, 2, 3, 4}
   ```

7. 集合之间的运算：

   ```python
   S ^ T  #返回一个新集合，由不同时在S和T中的元素构成。相当于S|T-S&T。等价于symmetric_difference 方法
   S <= T或 S < T #返回True/False，判断S是否是T的子集或真子集
   S >= T或 S > T #返回True/False，判断T是否是S的子集或真子集
   
   A = {"p","y",123}   # A = {123, 'p', 'y'}
   B = set("pypy123")  # B = {'1', '2', '3', 'p', 'y'}
   A - B #结果为 {123}，就一个元素。差集，由在A中，但是不在B中的元素构成，等价于.difference方法
   B - A #结果为 {'1', '2', '3'}
   A & B #结果为 {'p', 'y'}，交集，等价于.intersection方法
   A | B #结果为 {'1', 123, '2', '3', 'p', 'y'}，并集，等价于.union方法
   A ^ B #结果为 {'1', 123, '2', '3'}，对称差集，由不同时在A和B中的元素构成。相当于S|T-S&T。等价于.symmetric_difference方法
   #不同的是，运算符要求两侧都应为集合类型，而对应的方法允许运算符右侧为可迭代类型。
   a = {1,2}
   a | {3,4} #结果为{1, 2, 3, 4}
   a.union([3,4,5]) #结果为{1, 2, 3, 4, 5}
   ```

8. 集合的函数或方法：

   ```python
   S.add(x)     #如果x不在S中，则将x增加到S中.update方法有同样的效果。
   S.remove(x)  #从S中移出x，如果x不在S中，产生KeyError异常
   S.discard(x) #从S中移出x，如果x不在S中，不报错
   S.clear()    #移出S中的所有元素
   S.pop()      #随机弹出S中的一个元素，这会修改S，若S为空，则产生KeyError异常
   S.isdisjoint(Z) #判断两个集合是否不相交
   S.copy()     #返回S的一个副本
   len(S)       #返回S中的元素个数
   x in S       #判断x是否在S中
   x not in S   #判断x是否不在S中
   {1}.issubset({1,2,3})   #判断是否为子集。结果为True
   ```

9. 由于集合没有索引，因此无法查询或修改元素。

10. 集合一旦被定义后，内部是有顺序的，不过外部无法利用，仍看做是无序的。

11. 集合的一个非常重要的作用是包含关系的比较和数据去重。

    ```python
    ls = ["p","p","y","y",123]
    S = set(ls)  #{123, 'p', 'y'}
    lt = list(S) #[123, 'y', 'p']  对ls进行了去重，但是原有的顺序已经被打乱了
    ```

# 散列表原理

1. 对集合或字典使用in运算符来查找，会使用散列表，因此速度快，而list只会从头到尾依次扫描一遍，因此速度慢。

2. 如果程序中存在磁盘的读写，那么字典和集合的查询时间消耗，与之相比，可以忽略不计。

3. 散列表（hash table）其实是一个稀疏数组，大部分元素都是空白，每个元素称之为表元（bucket）。在dict的散列表中，每个键值对都占据一个表元，每个表元有两部分组成，对键的引用和对值的引用。因为所有表元的大小一致，因此可以通过偏移量来读取某个表元。

4. Python会设法保证大概还有1/3的表元是空的，因此快到这个阈值时，原有的散列表会被复制到一个更到的空间中。如果要把一个对象放入散列表中，首先要计算他的散列值。

5. 内置函数hash()可以用于所有内置类型对象，对自定义对象调用hash()，实际是调用其`__hash__`特殊方法。

6. 可散列对象必须满足如下性质：

   1. 支持hash函数，且通过`__hash__()`所得到的散列值在其生命周期内不变。

   2. 支持通过`__eq__`方法来检测对象的相等性。因为散列值相等不一定表示对象真的相等。

   3. 若 `a == b`为真，则`hash(a) == hash(b)`也为真，这个应该由`__hash__`方法保证，否则散列表就无法正常工作了。

      ```python
      1 == 1.0 #结果为True
      hash(1) == hash(1.0) #也必须为True，尽管这两个对象本身并不完全一样
      ```

   4. 应该仅在不可变的自定义类中实现`__hash__`方法。

7. 原子不可变数据类型（str，bytes，数值类型）都是可散列类型，frozenset也是，因为它被定义为只能容纳可散列对象，普通的set不是可散列对象。只有当一个元组包含的所有元素都是可散列对象时，该元组才是可散列的。并非所有的不可变类型都是可散列的，因为元组是不可变的，但有的元组不是可散列的。

   ```python
   tt = (1,2,(30,40))
   hash(tt) #结果为 -3907003130834322577
   tl = (1,2,[3,4])
   hash(tl) #会报错,TypeError: unhashable type: 'list'
   a = frozenset([20,30]) #构造一个集合，内部含有2个元素，
   hash(a) #结果为 255044489464142886
   ```

8. 自定义类的`__eq__`方法不为None，在该方法下，对象只和自己相等。自定义类的`__hash__`方法为None，不可调用。因此hash()该对象时，会报错，提示unhashable type。自定义类的`__hash__`方法一般依赖于`id()`函数的返回值来构建。

   ```python
   class NewInt:
       def __init__(self, x=0):
           self.x = x
       def __repr__(self):
           print("__repr__ 被调用了")
           return str(self.x)
       def __eq__(self, other):
           print("__eq__ 被调用了")
           return self.x == other.x
       def __hash__(self):
           print("__hash__ 被调用了")
           return id(self)
   #测试
   a = NewInt(3) #id为2067242640656
   b = NewInt(4) #id为2067244222608
   d = {a:"value-a", b:"value-b"} #d为{3: 'value-a', 4: 'value-b'}，这一步__hash__被调用了2次，每次的参数分别为a和b。
   d #在交互式控制台的结果为{3: 'value-a', 4: 'value-b'}，这一步__hash__和__repr__都被调用了2次
   d[a] #结果为"value-a"，这一步__hash__被调用了1次。
   ```

9. 散列值应该在索引空间中尽量分散开，这样才能更好作为散列表的索引。也就是说，对于一个好的散列函数，相似对象的散列值应该相差很大。

   ```python
   hash(1.0002) #结果为 461168601842689，二进制表示为0000000000000001101000110110111000101110101100011100010000000001
   hash(1.0003) #结果为 691752902764033，二进制表示为
   0000000000000010011101010010010101000110000010101010011000000001
   #二者有23位不同
   ```

10. 从Python3.3开始，str，bytes，datetime对象的散列值计算过程都增加了随机“加盐”的步骤，这个盐值是Python进程中的一个常量，但是每次启动进程都会生成一个随机新的。这样的目的是为了放置DOS攻击。

11. CPython的实现中，如果整形对象能被存入一个机器字中，则它的散列值就是它本身。

12. 为了获取对应键的值，python首先会计算key的散列值，然后把这个值最低的几位数字（具体几位，需要根据散列表的大小确定）当作偏移量，在散列表里查找表元。如果找不到，则抛出KeyError异常。如果找到，则表元内会有一堆对`found_key:found_value`。此时python会检查`key == found_key`，如果为真，则返回found_value，如果为假，则发生了散列冲突，此时python会再散列值中多取几位，然后用特殊方法处理一下，把新得到的数值再在散列表中作为索引查询，如果仍然发生散列冲突，则重复此步骤。

13. 散列冲突：因为散列函数是将任意对象映射到了有限位的散列值上，而在散列表中查询时，又只是用了散列值的一部分，因此冲突确实有可能发生。

14. 添加和更新键值对的过程和查询键值对几乎一样。

15. 在插入新键值对时，python会根据散列表的拥挤程度来决定是否要重新分配内存为它扩容。扩容后，散列值的位数和用作索引的位数都会增加，这样可以降低散列冲突的概率。

16. 实际使用中，即使dict中有数百万个元素，散列冲突也很少发生。

17. 由于字典使用了稀疏的散列表，因此它的空间利用率比较低。因此当只是要存放大量记录时，推荐使用元组或具名元组构成的列表，最好不要使用由字典组成的列表，因为这样会导致散列表占用大量的空间，且每个字典都会存储一份字段名。

    ```python
    #元组构成的列表
    l = [("lip",18),("deb",12)]
    #具名元组构成的列表
    import collections
    Person = collections.namedtuple("Person","name age")
    l = [Person("lip",18), Person("deb",12)]
    #字典构成的列表
    l = [{"name":"lip", "age":18},{"name":"deb", "age":12}]
    ```

18. dict的实现就是用空间换时间，字典类型有着巨大的内存开销，但是可以提供无视数据量大小的快速访问，只要字典可以被装载到内存中。

19. 内存空间的优化工作可以等到真正需要的时候再进行，因为优化往往是可维护性的对立面。

20. 当往dict中添加新键时发生散列冲突，新建可能会被安排到另一个位置。

# 迭代器

1. 可以用范围for循环的对象，都叫做可迭代对象。列表，元组，字典，字符串都是可迭代对象。

   ```python
   from collections.abc import Iterable  #导入一个类，所有的可迭代对象都是该类的对象
   isinstance([0, 1, 2], Iterable)  #判断第一个参数是否是可迭代对象。结果为True。
   #但是这种方法还不是最准确的，最准确的方法时使用范围for循环。
   ```

2. 可迭代对象：

   1. 如果一个对象内部实现了\_\_iter\_\_()方法，并且该方法返回指向该对象的迭代器，那么该对象就是可迭代对象。

      ```python
      from collections.abc import Iterable
      class Array:
          mylist = [0,1,2]
          # 返回迭代器类的实例
          def __iter__(self):  #实现该方法
              return iter(self.mylist)  #获取一个list的迭代器list_iterator并返回。
      my_list = Array()
      print(isinstance(my_list, Iterable)) # True
      for i in my_list:  #相当于 for i in [0,1,2]
          print(i)
      ```

   2. 假设该对象没有实现\_\_iter\_\_()方法，如果实现了\_\_getitem\_\_()方法，接受一个键，返称为可迭代对象。

      ```python
      from collections.abc import Iterable
      class Array:
          mylist = [0,1,2]
          def __getitem__(self, item):  #接受一个参数，可以看作是键，函数返回值。
              return self.mylist[item]
      my_list = Array()
      print(isinstance(my_list, Iterable)) # False,因为这个方法是检查是否有__iter__方法。
      for i in my_list:  #但是仍然是可迭代对象
          print(i)
      ```

3. 迭代器是指向可迭代对象中某个元素的指针。通过iter函数来获得可迭代对象的迭代器：

   ```python
   a = [1,2,3]
   ita = iter(a)  #<list_iterator at 0x17f4e298a00>  初始化的迭代器指向开始的元素
   next(ita)  #先向后移动一个位置，然后返回迭代器刚才指向的元素。结果为1
   next(ita)  #结果为2
   next(ita)  #结果为3
   next(ita)  #报StopIteration错误
   ```

4. 迭代器相比于可迭代对象就是多了个\_\_next\_\_()函数而已。对迭代器使用next函数时，会调用迭代器对象的\_\_next\_\_()函数函数：

   ```python
   from collections.abc import Iterable
   class Array:
       index = 0
       mylist = [0,1,2]
       def __iter__(self): #变成可迭代对象
           return self  # 因为自己就是迭代器，所以返回self
       def __next__(self): #变成迭代器对象
           if self.index <= len(self.mylist)-1:
               value = self.mylist[self.index]
               self.index += 1
               return value
           raise StopIteration     # 当无元素时，必要抛出 StopIteration
   my_iterator = iter(Array())     #__main__.Array类型
   print(isinstance(my_iterator, Iterable)) # output: True
   print(next(my_iterator))  # output: 0
   print(next(my_iterator))  # output: 1
   print(next(my_iterator))  # output: 2
   print(next(my_iterator))  # StopIteration
   ```

5. 迭代器协议是一套python解释器用来识别那些类是迭代器，从而设置的规则。

6. 不过还是建议将类型和它的迭代器类型分开设置。


# 推导式

1. 推导式（comprehension）又称为解析式，是python独有的一种特性，可以从一个数据序列构建一个新的数据序列。这是一种可读性好，且高效的形式。

2. 一般有两种用法， 构造新的容器数据或从已有的容器数据中筛选出满足条件的，一共有三种：

   1. 列表推导式：

      ```python
      #基本形式: new_list = [expression for_loop_expression if condition]，只会讲使得condition为True的元素筛选下来。其中if condition可以省略。
      [i**2 for i in range(5)]  #构造新的列表，结果为[0, 1, 4, 9, 16]
      old_list = [0,1,2,3,4,5]
      new_list = [item for item in old_list if item % 2 == 0] #筛选出来列表中偶数，组成一个新的列表。结果为 [0, 2, 4]
      ```

   2. 字典推导式：

      ```python
      #基本形式: new_dict ={ key_expr: value_expr for_loop_expression if condition }
      kvinfo = {i:i**2 for i in range(5)} #构造新的字典，结果为{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
      old_info = {
          "Jack": {
              "chinese": 87,
              "math": 92,
              "english": 78
          },
          "Tom": {
              "chinese": 92,
              "math": 100,
              "english": 89
          }
      }
      new_info = {name: scores for name, scores in old_info.items() if scores["math"] == 100} # 筛选出数学为100分的记录，结果为{'Tom': {'chinese': 92, 'math': 100, 'english': 89}}
      ```

   3. 集合推导式：

      ```python
      #基本形式: new_set = { expr for_loop_expression if condition }
      {i for i in [0,0,1,2,3,3]}  #可以用此方法对数据进行去重，结果为{0, 1, 2, 3}
      ```

3. 不存在元组推导式，因为其结果是一个生成器。

   ```python
   a = (i for i in range(1,6))  #<generator object <genexpr> at 0x0000017F4EE73D80>
   ```

4. 推导式可能被滥用，因此建议只使用它来创建新的列表，且尽量保持简短，如果逻辑过于复杂，建议使用for循环重写。列表推导不再会有变量泄露的问题。

   ```python
   #python2中for关键字之后的赋值操作可能会影响上下文中的同名变量
   x = "abc"
   y = [x for x in "def"] #上一行定义的x会在这里经历多次赋值，最终变成"f"。
   #但是这种情况已经在python3中解决了，python3规定了推导式和生成器表达式都使用自己局部的作用域，和函数类似，表达式内部的变量会会暂时屏蔽外部的同名变量。
   x = "abc"
   y = [ord(x) for x in x] #执行完成后x的值不变，y的值为[97, 98, 99]
   ```

5. 推导式可以将一个可迭代对象中的元素过滤或加工，产生一个新的列表，以替代filter+map的工作，而且还不需要构造lambda表达式：

   ```python
   x = "abcdef"
   y = [ord(s) for s in x if ord(s) > 99] #结果为[100,101,102]
   #如果不适用列表推导式
   x = "abcdef"
   y = list(filter(lambda c : c > 99, map(ord, x))) #map对象是一个可迭代的对象，其中每个元素是ord函数逐个作用在x的对应元素上。filter会依次调用lambda表达式，只保留结果为True的对象，结果也是一个可迭代对象，然后用list包装一下。
   ```

6. 用推导式作用在两个可迭代对象上，可以生成笛卡尔积，笛卡尔积是一个元组的列表，其中的元素是从多个可迭代对象中任选的元素组合起来的。

   ```python
   # x = ["a","b"]×[1,2,3]
   x = [(s, str(i)) for s in ["a","b"] for i in [1,2,3]] #结果为[('a', '1'), ('a', '2'), ('a', '3'), ('b', '1'), ('b', '2'), ('b', '3')]，两个for的顺序不能反
   #相当于二层循环
   x = []
   for s in ["a","b"]:
       for i in [1,2,3]:
           x.append((s,str(i)))
   ```

# 生成器表达式

1. 虽然使用推导式也可以初始化除了列表以外的其他序列类型，但是生成器表达式是更好的选择，这是因为生成器背后遵循了迭代器协议，可以逐个地产生元素，也不会保留之前产生的元素，而不是先建立一个完整的列表，然后把列表传递到对应类型的构造函数中，这样会浪费时间，额外占用内存空间。

2. 使用生成器时，内存中不会存在一个由该生成器能生成的所有数据的序列。

3. 

4. 生成器是一个可以像迭代器那样使用for循环来获取元素的的函数。python2.2引入，实现了延迟计算，缓解了在处理大量数据时内存消耗过猛的问题。

5. 

6. 创建生成器的两种方法：

   1. 使用生成器表达式，和列表推导式就相差一对括号

      ```python
      (i for i in range(5)) #结果为 <generator object <genexpr> at 0x000002149B440AD0>
      tuple(i for i in range(5)) #结果为(0, 1, 2, 3, 4)。如果生成器表达式是一个函数的唯一参数，那么外边的括号可以省略。
      ```

   2. 函数：

      ```python
      def generator_factory(top=5):
      	index = 0
      	while index < top:
      		print("index 值为: " + str(index))
      		index = index + 1
      		yield index
      	raise StopIteration
      gen = generator_factory()#<generator object generator_factory at 0x0000017F4B359000>  此时gen就是一个生成器对象。
      ```

7. yield相当于函数中的return，但又不一样：

   1. 函数运行到yield时，会暂停，并且把yield后的值返回回去。
   2. 若yield没有接收到任何值，则返回None。
   3. yield虽然返回了，但是函数并没有结束。

8. 使用方法：

   ```python
   #使用next逐个获取
   gen = (i for i in range(3))
   next(gen) # 结果为0，此时函数停在yield处。
   #使用范围for来遍历
   gen = (i for i in range(3))
   for i in gen:
       print(i)  
   ```

9. 生成器对象在创建后，并不会执行任何代码逻辑，想要从中获取元素，首先要激活它。有两种方法：

   ```python
   #使用next()
   #使用generator.send(None)
   gen = (i for i in range(3))
   gen.send(None)  #结果为0，相当于执行了next()。
   ```

10. 生成器在其生命周期中，有4种状态：

    ```python
    GEN_CREATED  #已经创建，但还未激活
    GEN_RUNNING  #解释器正在执行(只有在多线程应用中才能看到这个状态)
    GEN_SUSPEND  #在yield表达式处暂停
    GEN_CLOSED   #执行结束
    #使用 getgeneratorstate(gen)查看gen的状态。
    gen = (i for i in range(3))
    getgeneratorstate(gen)  #结果为 'GEN_CREATED'
    next(gen)  #结果为 0
    getgeneratorstate(gen)  #结果为 'GEN_SUSPENDED'
    next(gen)  #结果为 1
    next(gen)  #结果为 2
    next(gen)  #迭代结束
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    Input In [100], in <cell line: 1>()
    ----> 1 next(gen)
    
    StopIteration:
    getgeneratorstate(gen)  #结果为 'GEN_CLOSED'
    ```

11. 上面定义生成器时，当没有元素可以返回时，抛出了StopIteration的异常，其实，如果不手动抛出StopIteration的异常，生成器在遇到该函数的return时，会自动抛出StopIteration异常。

    ```python
    def generator_factory(top=2):
    	index = 0
    	while index < top:
    		index = index + 1
    		yield index
    	
    gen = generator_factory()
    next(gen) #结果为1
    next(gen) #结果为2
    next(gen) #此时或报异常
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    ```

# 排序和查找

1. 排序算法，用来排序的列表需要元素两两可以比较大小。数值之间，字符串之间可以比较大小，数值和字符串不可以比较大小：

   ```python
   x.sort()        #对列表x进行就地排序。
   sorted(x)       #内置函数，接收任何形式的可迭代对象包括不可变序列或生成器，返回排序后的列表，不修改x本身。按照数值大小，或ASCII顺序来进行增序排序。
   #以上两个函数都有两个可选参数,key为一个单参数函数,从元素中提取出比较使用的键,默认值为None,即恒等函数,reverse设置是否要进行降序排序,默认值为False。
   x = ["aar","aba","acme","add"]
   x.sort(key = len, reverse = False)#结果为['aar', 'aba', 'add', 'acme']，可以看到python的排序算法是稳定的，也就是值相同的两个元素在排序前后不会改变顺序，不论reverse的取值。对一个序列多次使用稳定的排序算法，没有副作用。
   #如果没有提供key函数，那么会直接对元素使用<进行比较，因此自定义类型需要实现__lt__特殊方法。
   #这里并非用len函数来直接给两个元素比较大小。而是先对每个的元素计算一个新的对应的值，生成一个新的列表，然后根据这个新的列表对原有列表进行排序。min,max函数也会用到这种方法。
   ```

2. 其他语言中需要的key一般是一个2参数的函数，接收两个元素，进行比较，返回-1，0，1。python使用单参数的key，虽然总会需要比较两个参数，但是它被是现在了C语言层面，效率更高。

3. 例子：

   ```python
   class NewInt:
       def __init__(self, x = 0):
           self.x = x
       def __repr__(self):
           return str(self.x)
       def __lt__(self, other):
           return self.x < other.x
   arr = [NewInt(i) for i in [0,5,2,4,5,6,1]]
   sorted(arr) #会调用13次__lt__函数
   sorted(arr, reverse = True) #会调用15次__lt__函数
   ```

4. Python的默认排序算法是Timsort，它借鉴了归并排序和二分插入排序（比普通的插入排序需要更少的比较次数）两种方法，速度特别快。Oracle对Google的侵权起诉中，就提供了一些Timsort算法的细节。

   1. 先将待排序的序列划分为有序（递增或严格递减）的片段（称之为run），逆序的片段会被翻转，过短的片段会使用紧邻的后续元素填充，然后使用二分插入排序使之变成较长的有序片段。
   2. 该算法是自适应的，因为run的下限会根据序列的长度自动确定。会从32到64（包括）选择一个数字，使得序列的长度除以run的下限等于或者略小于2的幂次方。如果序列长度比32还短，则会直接使用插入排序。
   3. 归并run时，如果run的总数等于或略小于2的幂次时，效率最高，如果run的总数略高于2的幂次，效率最差。
   4. 普通的归并算法是，相邻子序列的两两合并，这样子序列数量减少一半，然后再重复相邻子序列两两合并。而这里是从前往后，逐个按需合并。
   5. 该算法使用一个栈来保存每个run，从前往后，依次入栈。每次都考察栈顶的3个run（长度分别为X，Y，Z），如果$Z>Y+X$和$Y>X$有一个不满足，则会触发合并，将Y和X，Z中较短的那个合并成一个新的run，放置在原来的位置。如果这两个条件都满足，则会继续向后处理，寻找新的run。
   6. 之所以规定一个最小run长度是因为，将一个长序列和短序列进行归并排序效率低下。该算法之所以较快，是因为它考虑到了现实世界中的序列，有很多是有序的子序列。

5. 像sort这样的方法，返回值是None，这就表明该方法会就地处理对象，这是python的风格。就地修改有一个缺点，就是无法进行连贯接口（fluent interface）的调用，例如`l1.sort().index(3)`。

6. 已排序的序列可以进行快速搜索，标准库的bisect模块实现了二分查找：

   ```python
   #bisect模块包含两个函数bisect和insort,这俩函数有2个可选参数，lo和hi，分别指定搜索和插入的范围，默认值分别为0和序列长度。要求序列本身是递增（不一定严格递增）的，即前一个元素<=后一个元素。
   import bisect
   bisect.bisect(haystack, needle) #在有序序列haystack中查找needle的位置，使得needle插入这个的位置时，haystack仍然保持有序。也就是<= needle的元素中下标的最大值+1。
   bisect.insort(haystack, needle) #在有序序列haystack中合适的位置插入needle，等价于先用bisect查找到index，然后再用haystack.insert(index,needle)在对应位置插入。
   x = [1,4,5,5,6,8,12,15]
   bisect.bisect(x,0)  #结果为 0，比所有元素都小，就放在第0个前面
   bisect.bisect(x,3)  #结果为 1，<=3的元素中最大下标为0
   bisect.bisect(x,5)  #结果为 4，<=5的元素中最大小标为3
   bisect.bisect(x,17) #结果为 8
   #bisect还有一个函数为bisect_left，他和bisect的区别时，如果序列中存在和needle相等的一个或多个元素，由于bisect是从右往左搜索，则会返回最后一个相等元素的下标+1，而bisect_left是从左往右搜索，会返回第一个相等元素的下标。这个差别对于整数序列没有影响，但是对于那些值相等，但是形式不同的情况会有区别
   x = [1,2,2.0,3]
   bisect.bisect(x,2) #结果为3，插入后x为[1,2,2.0,2,3]
   bisect.bisect_left(x,2) #结果为1，插入后x为[1,2,2,2.0,3]
   ```

7. 对字典进行排序，得到的是一个关于其键的列表：

   ```python
   d = {"b":2,"a":1,"c":3}
   sorted(d) #结果为 ['a', 'b', 'c']
   ```

# 文件操作

## 打开

1. 文件可以认为是存储的数据序列。文本文件和二进制文件本质都是二进制文件，只是展示方式不同。

2. 文本文件：由单一特定的编码组成的文件，也被看做是长的字符串。

3. 二进制文件：直接由0/1比特构成，没有统一的编码。

4. ```python
   #文本形式打开文件
   tf = open("f.txt","rt")  #open函数位于自动导入的io模块中。
   print(tf.readline())     #读取一行，包含末尾的换行符。
   tf.close()
   >>>
   中国是一个伟大的国家
   ```

4. Windows默认的路径分隔符 \ 和编程语言的转义符一样，因此对于此文件D:\aa\c.txt有三种解决方法：

10. ```python
    D:/aa/c.txt		#unix中通用
    D:\\aa\\c.txt
    r"D:\aa\c.txt"  #原生字符串
    ```
    
7. 文件的打开模式，rwxa是一类，bt是一类，

   ```python
   'r'  #只读模式，默认值，如果文件不存在，则报FileNotFoundError异常。
   'w'  #覆盖写模式，若文件不存在则创建，存在则覆盖已有内容。
   'x'  #创建写模式，若文件不存在则创建，存在则报FileExistError异常。
   'a'  #追加写模式，若文件不存在则创建，存在则在文件最后追加内容。
   'b'  #二进制模式。
   't'  #文本模式，默认值，认为文件是按照行组织的。
   '+'  #与r/w/x/a 一同使用，在原有的功能上增加同时读写的功能。
   ```

12. 默认情况下，以只读文本模式（rt）打开，只读模式中不能写入信息。

14. 读和写是独立的两个功能，r+  w+  x+  a+ 是在原有的写的基础上增加读的功能，能同时读写。

10. Python解释器会在程序正常退出后，会关闭没有被close()的文件。不过还是尽量手动关闭。

## 读文件

1. 读取文件：

   ```python
   f.read(size=-1) #默认读入全部内容，如果size给定，则从当前位置读入size个字符。返回读到的字符串。
   f.readline(size=-1) #读取一行的内容，包含最后的\n，如果size给定，则读入该行前size个字符。如果到行尾不够size个字符，那就有多少读取多少。
   f.readlines(hint=-1) #读取文件的所有行，返回一个字符串list，list的每个元素是一行的内容。如果hint给定，则读取前hint行。
   ```

1. 如果文件特别大，不建议一次性读入文件。

4. 文件默认的打开编码为ANSI，系统的编码，简体中文版为gbk，要是用utf-8打开需要使用参数，encoding='utf-8'。

5. 使用Windows记事本保存的utf-8格式的文本文件，会自动添加BOM头（ Byte Order Mark，字节顺序标记，出现在文本文件头部，Unicode编码标准中用于标识文件是采用哪种格式的编码 ），即\ufeff

6. 两种解决办法：①使用'utf-8-sig'编码打开即可②用notepad++等保存为utf-8无BOM头的文件也可以。

7. <img src="Python.assets/1590762870359.png" alt="1590762870359" />

7. 常用操作，按行操作，f为文件描述符：

   ```python
   for line in f.readlines():
   或
   for line in f
   ```

   

## 写文件

1. writelines会将列表拼接，然后写入。

   ```python
   f.write(s)  #向文件中写入一个字符串或字节流
   f.writelines(lines) #将一个字符串列表写入文件，相当于多次调用write。
   ```
   
2. writelines后，文件的指针位于文件的末尾，此时需要seek到开头，才可以遍历输出。

   ```python
   f.seek(offset,whence)  #移动文件操作指针的位置，offset表示偏移量，whence表示基点。whence有三种可以有三种取值：0表示文件开头，1表示当前位置，2表示文件末尾。当whence省略时，默认为0。
   f.seek(0) # f.seek(0,0) 移动指针，指向文件的首个字符
   f.seek(0,2) #移动指针，指向文件的最后一个字符
   f.seek(-1,1) #移动指针，指向上一个字符
   ```

5. map函数是将第一个参数一次作用于第二参数（需要时组合数据类型）。

8. ```python
   f = open('data.txt','r',encoding='utf-8')
   datas = []
   for line in f:
       line = line.replace('\n', '')
       datas.append(list(map(eval,line.split(','))))
   f.close()
   ```

9. 原数据为："300,1,144,0,1,0\n"这样的一个字符串。处理后为列表：[300, 1, 144, 0, 1, 0]

10. 如果要将列表元素存储到文件中，且使用空格或特殊符号分隔，可以使用' '.join(ls)。特殊符号会出现在列表的元素之间，首尾没有。

11. 二维列表，即每个元素都是一个列表。

12. csv文件使用逗号分隔，无空行，一行表示一个数据，可能会有标题行。

13. 如果元素缺失，逗号还应该保留，逗号和数据之间没有空格。

15. 如果数据中出现逗号，一般可以用“ ”将元素括起来。

16. 按照先行后列的索引方法，外层列表的元素一般是一行。

12. 读取数据到列表。

    ```python
    #读取CSV文件到二级列表中，每一行为一个列表
    fo = open(fname)
    ls = []
    for line in fo:
        line = line.replace("\n","") #删除行尾的换行符
        ls.append(line.split(","))   #将字符串用逗号分隔为list。
    fo.close()
    
    #将二级列表写入到csv文件中
    ls = [["abc","def"],["12","34"],["a1","b2"]]
    f = open(fname,"w")
    for item in ls:
        f.write(",".join(item)+"\n")    #用,连接一行内的各个字段，末尾加上换行符，一次写入一行
    f.close()
    ```

18. 自顶向下的设计是“系统”思维的体现。

23. 计算思维是除逻辑思维和实证思维以外的第三种思维。主要特征是抽象和自动化。递归是最杰出的代表。

24. 提高用户体验的方法：增加进度显示，对用户的输入进行检查异常处理，设置日志文件，打印帮助信息。

25. 模块内紧耦合，模块间松耦合，使用配置文件来配置程序的功能。

26. python官方的包发行平台 pypi.org   Python package index。

27. 最基本的数据分析库是numpy表达N维数组最基本的库，内部使用C语言实现，速度快，提供了一些矩阵运算的功能。

28. numpy中数组是基本单元，类似于MATLAB，如果不适用numpy则需要使用循环遍历。

29. pandas是数据分析高层次库，基于numpy开发，通过操作索引来操作数据。

21. scipy提供数学，科学工程计算的功能库，类似于MATLAB，也是基于numpy开发的。分为以下几个模块：优化算法，稀疏图运算，稀疏图压缩，图像处理，线性代数，信号处理，傅里叶变换等。

# 面向对象

1. 构造一个包含一摞有序的纸牌的类：

   ```python
   import collections #首先构建表示单张纸牌的类，然后构建一个类似于序列的类，来存储所有的纸牌
   Card = collections.namedtuple("Card",["rank","suit"]) #不能省略返回值赋值。从python2.6开始，collections模块中加入了一个namedtuple命名元组函数，用来快捷构造一个只有属性，而没有方法的类。
   #相当于定义了一个类，名称为Card，有2个属性，分别为rank和suit。
   beer_card = Card("7","diamonds") #创建一个Card的对象。
   class FrenchDeck:
       ranks = [str(n) for n in range(2,11)]+list("JQKA") #字符列表
       suits = "spades diamonds clubs hearts".split #字符串列表
       def __init__(self):
           self._cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits] #该对象底层是使用list来实现的
       def __len__(self): # len函数作用在该类的对象上时，会调用此函数
           return len(self._cards)
       def __getitem__(self, position): # 下标[]作用在该类的对象上时，会调用此函数，[]内的下标会传递给position参数。
           return self._cards[position]
   #使用该类
   deck = FrenchDeck()
   len(deck) #结果为52
   deck[0] #结果为 Card(rank='2', suit='spades')
   #由于__getitem__方法内部交给了list的__getitem__方法， 因此自动支持列表才支持的切片操作
   deck[3:5] #结果为 [Card(rank='2', suit='hearts'), Card(rank='3', suit='spades')]
   #同时该类也是一个可迭代的类
   for card in deck:
       print(card)
   #该类没有实现__contains__特殊方法，因此in运算符会按顺序进行迭代搜索，所以in也可以作用在该对象上。
   Card("Q","hearts") in deck #结果为True
   Card("M","hearts") in deck #结果为False
   import random
   random.choice(deck) #从序列中随机获得一个元素，结果为Card(rank='8', suit='hearts')
   ```

2. 为自己定义的类实现特殊方法，有两个优点：

   1. 方便用户使用，不必去记住一些函数或属性名称，例如不用去纠结获得元素个数到底是.size还是.length方法。

   2. 方便和标准库进行结合，例如random.choice。

3. 特殊方法（又称为魔术方法）的存在是为了给python解释器调用的，用户一般不应该直接调用，除非代码中有大量的元编程存在。例如应该使用`len(deck)`，而不是`deck.__len__()`。`__init__`方法除外，因为子类中经常要显式调用父类的构造方法。

4. Ruby语言中也有特殊方法概念，不过它的社区称之为魔术方法，他们都使用其来丰富元对象协议，让语言的用户和核心开发者拥有并使用同样的工具。Javascript的元对象支持就不够好，例如在Javascript 1.8.5中，用户的自定义对象不能有只读属性，而不少Javascript的内置对象就可以有该属性。

5. 如果对于内置类型调用特殊方法，CPython可能会抄近路，而不去调用特殊方法，例如对于`len([1,2])`，CPython会直接返回PyVarObject（表示内存中长度可变的内置对象的C语言结构体）的ob_size属性，这样比调用特殊方法快得多。

6. 很多时候，特殊方法的调用是隐式的，例如`for i in x:`，背后是`iter(x)`，而这个函数又会调用`x.__iter__()`特殊方法。

7. 通过内置函数（例如len，iter，str）来使用特殊方法是最好的选择，这样可以方便地像使用内置类一样使用自定义类，内置函数作用在内置类上，速度更快。

8. 用户自定义的方法名称不要写成特殊方法`__xxx__`的形式，因为后续Python标准可能会增加特殊方法，容易碰撞。

9. Python内置的complex类可以当作二维向量使用（不过只能模拟加减，无法模拟内积），如果要用n维向量，就要自定义了。

   ```python
   from math import hypot
   class Vector:
       def __init__(self, x = 0, y = 0):
           self.x = x
           self.y = y
       def __repr__(self):
           return "Vector(%r,%r)" % (self.x, self.y) #%r表示用repr处理对应的参数
       def __abs__(self):
           return hypot(self.x, self.y)
       def __bool__(self):
           return bool(abs(self)) #虽然在类中，也不建议直接调用特殊方法__abs__
           #或者使用 bool(self.x or self.y)，效率更高
       def __add__(self, other):
           x = self.x + other.x
           y = self.y + other.y
           return Vector(x,y)
       def __mul__(self, scalar):
           return Vector(self.x*scalar, self.y*scalar)
   #测试
   v1 = Vector(2,3)
   repr(v1) #结果为 'Vector(2,3)'
   
   ```

10. 内置函数repr，获得对象的字符串表示形式。它会调用参数的`__repr__`方法。如果没有实现该特殊方法，函数会调用object的该方法，结果为`'<__main__.Vector object at 0x000001F27393DC90>'`。交互式控制台和调试程序都会使用repr函数获取变量或对象的字符串表示形式。格式化输出时，可以使用%r来获得对应参数的字符串表示，会隐式调用repr函数。

11. 特殊方法`__repr__`不能随便写，应该反映出如何使用代码构造该对象。例如上面的`repr(v1)`的结果就是`Vector(2,3)`。

12. repr和str的区别：str返回的字符串是对终端和用户友好的，repr返回的字符串是方便调试和记录日志的。二者都有对应的特殊方法。如果只想实现一个特殊方法，推荐实现`__repr__`，因为一个对象如果没有`__str__`方法，则解释器会调用`__repr__`方法。

13. python的任何对象都可以用于需要布尔值的上下文，例如if语句中。

    1. 对于自定义类，此时python会自动调用bool函数，bool(x)的背后会调用`__bool__`特殊方法，该方法只能返回True或False。如果`__bool__`特殊方法不存在，则会尝试调用`__len__`特殊方法，如果返回0，则表示False，否则为True。如果这两个方法都不存在，则认为对象总是为True。

    2. 对于内置类型的对象，标准规定了检验真假的标准，不必执行特殊方法。

14. collections.abc模块内存放了很多抽象基类（Abstract Base Class），可以用他们来快速建立具有某一特性的类来替代标准库自带的类。

22. Python中所有的数据类型都是对象，函数，模块都是对象，所有的对象都继承自object。数据的操作都是类方法的体现。

23. python2中对object类的继承需要显式写出ClassA(object)，而Python3中默认都是继承自object。

24. 对象是对函数的更高级别的抽象。面向对象并非高级的方法，而是为了复用代码。

25. 面向对象的重要的三个特征：

    1. 封装，属性方法的抽象，用数据和操作数据的方法来形成对象逻辑

    2. 继承，代码用的高级抽象，用对象之间的继承关系来形成代码复用

    3. 多态，方法灵活性的抽象，让对象的操作更灵活，更多地复用代码

26. Python使用弱类型，天然支持多态。

    1. 参数类型的多态，一个方法可以处理多种类型的能力

    2. 参数形式的多态，一个方法能够接受多个参数的能力

27. 类中包含属性（变量）和方法（函数）。

28. <img src="Python.assets/1590856005743.png" alt="1590856005743" />

29. 使用class保留字定义类，类的定义不限定位置，只要使用类时定义已经完成即可：

    ```python
    class <类名>:  #类名一般使用大写字母单词的组合
        [类描述 "documentation string"] #类描述的字符串，可以使用类名.\_\_doc\_\_访问，可以使用多行字符串。
        <语句块>
    ```

30. __开头和结尾的是类的保留属性，预定义的。

31. 当成功定义一个类之后，会产生一个Python类基本信息的数据结构（即使还没有实例化对象），只有一个，全局唯一，实例对象可以有很多。类对象是type类型的。

32. 类的定义和类对象的生成使得类内的一些语句被执行，因此不在类的定义中包含可执行语句。

    ```python
    class DemoClass:
        "This is a demo for python class"
        print("Hello Demo Class")   #执行类定义时，会执行该语句。
    print(DemoClass.__doc__) #输出为 "This is a demo for python class"
    print(type(DemoClass)) #<class 'type'>
    ```

33. 实例化对象，可以提供多个参数。实例对象的类型是 \_\_main\_\_.类名 这种类型。

    ```python
    <对象名> = <类名>([<参数>])
    ```

34. 构造函数规定如何生成一个对象，支持参数构造。

35. Python使用预定义的__init\_\_函数作为构造函数。创建对象时提供的参数会传递给init函数的参数列表（self之后的）。

36. self表示类实例自身（在类定义内部使用，就像类名代表类对象本身），构造函数没有返回值，或者返回none使用return会产生typeerror异常，因为它要返回实例化的对象，

    ```python
    class <类名>:
        def __init__(self, <参数列表>)
    	    <语句块>
        ……
    ```

37. 属性分为两种：

    1. 类属性，类对象的属性，由所有实例对象共享

    2. 实例属性：实例对象的属性，由各实例对象所独享

38. 类属性在类的内外都是使用类名.属性名来访问。

    ```python
    class <类名>:
        <类属性名> = <类属性初值>
        def __init__(self,<参数列表>)
        	self.<实例属性名> = <实例属性初值>
        ……
    ```

39. 类内一共可以定义5种方法：

    1. 实例方法，实例对象的方法，由各实例对象独享，最常用的形式，第一个参数必须是self

    2. 类方法，类对象的方法，由所有实例对象共享

    3. 自有方法，类中的一个普通函数，由类所在的命名空间管理，类对象独享

    4. 静态方法，类中的一个普通函数，由类对象和实例对象共享

    5. 保留方法，由双下划线开始和结束，保留使用，例如\_\_len\_\_()

40. 需要在定义方法前加上一个装饰器。类对象和实例对象都可以调用。至少包含一个参数，表示类对象，建议用cls。类方法只能操作类属性和其他类方法，不能操作实例属性和实例方法。

    ```python
    class <类名>:
        @classmethod
        def <方法名>(cls,<参数列表>)
        	...
    ```

41. 自由方法：定义在类命名空间中的普通函数。使用类名.方法名()来调用，不能使用对象名.方法名()来调用。类名表示命名空间。不需要self和cls的参数，只能操作类属性和类方法。完全可以放到类定义之外，不过放在内部可以是程序更加紧凑，合理。

    ```python
    class <类名>:
        def <方法名>(<参数列表>)
        	...
    ```

42. 静态方法，用到装饰器，是定义在类中的普通函数，就是比自由函数多个装饰器，但是能够被所有实例对象和类对象使用。

    ```python
    class <类名>:
        @staticmethod
        def <方法名>(<参数列表>)
        	...
    ```

43. 保留方法统一用__开头和结束。一般都有self参数（因为调用对应操作符时，会自动传参），在使用操作符时，会调用这些方法。

    ```python
    class <类名>:
        def <保留方法名>(<参数列表>)
        	...
    ```

44. 例如定义了__len\_\_方法后，就能使用len(对象)方法了（调用该函数）。

45. 当对象消亡时，可以使用析构函数做一些额外处理，如果不写，Python解释器的垃圾回收机制会处理。

46. 使用预定义的__del\_\_作为析构函数（至少需要定义一个self参数），在真实删除（引用数=0或当前程序退出）实例对象时 会被调用。del 对象名 可以删除对象。

47. 如下代码会输出两次，第一次在地13行，第二次输出在main（）函数返回退出后，会删除掉所有局部变量。此时d2真正被删除，调用析构函数。

48. 一般在构建类的时候，不会写析构函数，而是让Python的垃圾回收机制自己去处理。

49. ```python
    class Demo:
        
        def __init__(self,name):
            self.name = name
        
        def __del__(self):
            print ('再见'+self.name)
    
    def main():
        d1 = Demo('老王')
        d2 = d1
        del d1
        print(d2.name)
    main()
    ```

50. 使用构造函数创建对象时，真正生成对象，=赋值只是生成了一个引用。

51. sys.getrefcount(对象名)，可以获得对象的引用次数+1的值。由于调用该函数要传递引用参数，所以对象的引用次数会加1。函数返回后，又会-1。

52. 封装的目的是形成对外可操作的接口，隔离和保护私有的内容。

53. 一共4种属性，公开/私有  类/实例   属性。默认的属性就是公开的。私有的属性定义要以__开头。

54. 私有的类属性，只能在类定义的内部使用（要用类名.属性名访问），子类也不能访问。不过也可以编写get，set之类的函数，使得在类外也可以访问。如果不在类内访问，则会报错。

55. ```python
    class Demo:
        __count = 0 #私有类属性
        def __init__(self,name):
            self.__name = name  #私有实例属性
            Demo.__count +=1
        @classmethod
        def getCount(cls):
            return cls.__count  #return Demo.__count 也行
        def getName(self):
            return self.__name
    d1 = Demo('老王')
    d2 = Demo('老李')
    print(str(Demo.getCount())+'    '+d1.getName()+'      '+d2.getName())
    print(str(d1._Demo__count)+'    '+d1._Demo__name)      #形式上的私有
    ```

56. 私有实例属性，只能在当前类内访问，子类也不能访问，使用__开头。用self来定义。

57. Python的私有属性，只是将属性改名了，这是一种形式上的私有。改名为_类名__属性名。

58. 默认定义的方法是公开的，在定义时，以__开头，则为私有方法。以后只能在类内部使用。也是形式上保护。

59. 类的保留属性（使用类名.属性名访问），也称为特殊属性，是Python解释器预留的类属性，以__开头和结尾。为理解Python类提供了统一的接口。类定义后就可以直接使用。

    ```python
    __name__        #类的名称
    __qualname__    #以.分割的从模块全局命名空间开始的类名称
    __bases__       #类的基类名称
    <类>.__dict__   #包含类成员信息的字典，key是属性和方法名称，value是地址
    <对象>.__dict__ #包含对象属性信息的字典，key是属性名称，value是值
    __class__       #对象所对应的类信息，即type()的结果
    __doc__         #类的描述，卸载类定义下的首行字符串，不能继承
    __module__      #类所在的模块名称
    ```

60. class，doc ,module使用可以用对象名.属性名或类名.属性名访问。类的class属性为type，对象的class属性为类名

    ```python
    print(DemoClass.__doc__, DemoClass.__module__, DemoClass.__class__)
    A Demo Class __main__ <class 'type'>
    print(dc1.__doc__, dc1.__module__, dc1.__class__)
    A Demo Class __main__ <class '__main__.DemoClass'>
    ```

61. 类的保留方法，也称为特殊方法，一般与操作符有关，类定义需要重载。使用__开头和结尾。Python提供了超过100多个保留方法，对应各种操作。

62. 继承是代码复用的高级抽象，新定义的类能够几乎完全使用原有类的属性和方法。基类（超类）和派生类（子类）

63. Python支持多继承。类名后加括号，引入基类，不是参数，基类名之间用逗号分隔。

    ```python
    class <类名>(<基类名>):   #基类名可以带有路径：ModuleName.BaseClassName
        def __init__(self,<参数列表>)
        	...
    ```

64. 基类的属性等同于直接定义在派生类中。派生类可以使用基类的类属性（使用基类名.属性名调用）和实例属性。

65. 派生类可以直接使用基类的各种方法，可以使用派生类对象调用基类的实例方法。

    ```python
    isinstance(obj, cls)    #判断对象obj是否是类cls的实例或子类实例，is-a判断
    issubclass(cls1, cls2)  #判断类cls1是否是类cls2的子类
    ```

66. 派生类只能继承基类的公开属性和方法。

67. object类是Python最基础的类（但是它的类型是type），所有类定义时，默认继承object类。保留属性和保留方法实际上都是在object类中定义的属性和方法。

    ```python
    object.__name__   #结果为 'object' 表示对象的名称
    object.__doc__    #结果为 'The base class of the class hierarchy.\n\nWhen called, it accepts no arguments and returns a new featureless\ninstance that has no instance attributes and cannot be given any.\n'
    object.__bases__  #结果为()
    object.__class__  #结果为type
    object.__module__ #结果为 'builtins'
    object.__dict__   #结果为如下：
    mappingproxy({'__new__': <function object.__new__(*args, **kwargs)>,    
                  '__repr__': <slot wrapper '__repr__' of 'object' objects>,
      ....
    
                  '__doc__': 'The base class of the class hierarchy.\n\nWhen called, it accepts no arguments and returns a new featureless\ninstance that has no instance attributes and cannot be given any.\n'})
    
    ```

68. 字符串就是不可变的类型。主流的Python的解释器使用C语言编写的，也叫CPython，使用内存地址表示对象的标识。其他的解释器还有JPython（Java写的）IronPython（.Net写的）

69. python对象的三个要素：

    1. 标识，identity，对象一旦构建就不会改变，用id()获得，CPython解释器使用内存地址，x is y 用来判断x和y的标识是否相等，而不判断值。

    2. 类型 type，对象的类型，用type()获得

    3. 值 value，分为可变mutable和不可变immutable两种

70. 重载：派生类对基类的属性或方法的再定义。需要同名。

71. 在索引属性时，使用就近原则，如果派生类内定义了，就是用他自己的，如果没有，就向上找。

72. 最近覆盖原则：重载无需特殊标记

    1. 优先使用派生类重定义的属性和方法

    2. 然后寻找基类的属性和方法

    3. 再寻找超类的属性和方法

73. 方法重载分为完全重载（完全不同的功能，直接同名覆盖即可）和增量重载（包含基类的功能，还增加了一些功能）。使用super（），该函数返回派生类对应的基类。

    ```python
    class <派生类名>(<基类名>):
        def <方法名>(self, <参数列表>)
        	super().<基类方法名>(<参数列表>)
    ```

74. 多继承，采用深度优先，从左到右的的方法。当派生类使用方法时，首先会在本身内查找，然后是第一个基类，第一个基类的基类等等，直到找到object类，再然后是第二个基类。

75. 构造函数也参照上述原则，super()也是。

76. Python的运算体现为运算符的重载（object方法中定义过）。实际是保留方法。

77. 不能重载内置类型的运算符，例如字符串的加法。不能新建运算符，只能重载现有的。is and not or 不能被重载。重载也可以是增量的。

78. ```python
    class NewList(list):
        def __add__(self,other):
            result = []
            for i in range(len(self)):
                try:
                    result.append(self[i]+other[i])
                except:
                    result.append(self[i])
            return result
    l1 = NewList([1,2,3,4,5])
    l2 = NewList([2,6,5])
    print(l1+l2)
    ```

## 特殊方法

1. python定义了83个特殊方法，根据是否和运算符相关可以分为两大类：

   1. 运算符相关的特殊方法：

      ```python
      #一元运算符
      .__pos__(self)    +obj     #取原值
      .__neg__(self)    -obj     #取相反数
      .__abs__(self)    abs(obj) #取绝对值
      #比较运算符
      .__lt__(self, obj2)   obj1 < obj2
      .__le__(self, obj2)   obj1 <= obj2
      .__eq__(self, obj2)   obj1 == obj2
      .__ne__(self, obj2)   obj1 != obj2
      .__gt__(self, obj2)   obj1 > obj2
      .__ge__(self, obj2)   obj1 >= obj2
      #算术运算符
      .__add__(self, other)      obj + other
      .__sub__(self, other)      obj - other
      .__mul__(self, other)      obj * other
      .__truediv__(self, other)  obj / other      #除法
      .__floordiv__(self, other) obj // other     #除法取商
      .__mod__(self, other)      obj % other      #除法取余数
      .__divmod__(self, other)   divmod(obj, other)  #返回由商和余数组成的元组
      .__pow__(self, other)      obj ** other   #幂运算
      .__round__(self, ndigits)  round(number, ndigits)  #四舍五入
      #反向算术运算符，除了.__round__(self, ndigits)外，都有对应的反向算术运算符，例如.__radd__(self, other)。
      #增量赋值算术运算符 += -= *= /= //= %= **=，特殊方法名例如.__iadd__(self,other)，i表示in place就地进行。
      #位运算
      .__invert__(self) ~obj        #按位取反
      .__lshift__(self, other) obj << other  #左移
      .__rshift__(self, other) obj >> other  #右移
      .__and__(self, other)  obj & other     #按位与
      .__or__(self, other)   obj | other     #按位或
      .__xor__(self, other)  obj ^ other     #按位异或
      #除了按位取反外，每个位运算符(例如.__and__(self, other))都有对应的反向位运算符(.__rand__(self, other))和增量位运算符(.__iand__(self, other))
      ```

   2. 运算符无关的特殊方法：

      ```python
      #字符串/字节序列表示形式
      .__repr__(self)     repr(obj)          #将对象转换为可打印字符串
      .__str__(self)      str(obj)           #将对象转换为字符串
      .__bytes__(self)    bytes(obj)         #将对象转化为字节串
      .__format__(self)   obj.format()或format(obj) #将对象格式化输出
      #数值转换
      .__abs__(self)      abs(obj)           #绝对值
      .__bool__(self)     bool(obj)          #布尔运算
      .__int__(self)      int(obj)           #转换为整数
      .__float__(self)    float(obj)          #转换为浮点数
      .__complex__(self)  complex(obj)        #转换为复数
      .__hash__(self)     hash(obj)          #哈希操作
      __index__()        ??
      #集合模拟
      .__len__(self)      len(obj)           #对象长度
      .__getitem__(self, key)     obj[key]       #获取对象中序号为key的元素
      .__setitem__(self, key, v)  obj[key] = v   #将v赋值给对象中序号为key的元素
      .__delitem__(self, key)     del obj[k]     #删除对象中序号为key的元素
      __contains__(self, item)    item in obj    #判断item是否为对象中的一个元素
      #迭代枚举
      .__reversed__(self) obj.reversed()     #对象逆序，一般用于含有多个子元素的对象上
      .__iter__(self) iter(obj) ??
      .__next__(self)  ??
      #可调用模拟
      .__call__(self) ??
      #上下文管理
      .__enter__(self)
      .__exit__(self)
      #实例创建与销毁
      .__init__(self)     obj=ClassName()    #初始化实例对象
      .__del__(self)      del obj            #删除实例对象
      .__new__(self) ??
      #属性管理
      .__getattr__(self) ??
      .__getattribute__(self) ??
      .__setattr__(self) ??
      .__delattr__(self) ??
      .__dir__(self) ??
      #属性描述符
      .__get__()
      .__set__()
      .__delete__()
      #跟类相关的服务
      .__prepare__()
      .__instancecheck__()
      .__subclasscheck__()
      ```

2. 当算术或位运算符左侧的对象没有实现对应的特殊方法（例如`__add__`）时，就会调用右侧对象的反向方法（例如`__radd__`）：

   ```python
   class my_complex:
       def __init__(self, real = 0, imag = 0):
           self.real = real
           self.imag = imag
       def __add__(self, other):
           real = self.real + other
           imag = self.imag
           return my_complex(real, imag)
       def __radd__(self, other):
           real = self.real + other
           imag = self.imag
           return my_complex(real, imag)
       def __repr__(self):
           return "my_complex(%r,%r)" % (self.real, self.imag)
   #测试
   c1 = my_complex(2,3)
   c1+3 #结果为 my_complex(5,3)，会调用c1.__add__(3)
   3+c1 #结果为 my_complex(5,3)，因为没有3.__radd__(c1)，所以会调用c1.__radd__(3)
   ```

3. python的内置函数一般都和类内的保留方法对应，将对象作为该函数的参数来调用时，会调用对应的保留方法。某些保留方法在定义一个新的类时会自动使用默认的，例如str，del，某些则没有默认的可供使用，例如len。

4. Python天生支持多态，仅针对方法，分为参数类型（可以处理多种参数类型）和参数形式（可以接受多个参数）两种。

5. 由于Python的变量没有类型声明，所以天然支持参数类型的多态，Python是通过文档来约束，而非语法。只需在程序内部做参数类型的区分处理即可。而无需写多个函数。如果要使得函数可以处理任意类型，建议另外重载一个Python的内部函数（该函数可以和任意对象打交道，例如id()）。

6. Python你的函数/方法都支持可变参数，可以使用默认值。

7. 引用是对象的指针，对象是在计算机中真实分配空间的区域。

8. 引用在程序中表达为变量名，在系统中表达为内存地址。每个对象至少存在一个引用，否则会被垃圾回收。

9. 传参和赋值时，都是传递的引用。而不是赋值对象。因此不会调用构造函数。

10. Python内部对引用的处理：

    1. 不可变对象：immutable 解释器为相同值维护尽量少的内存区域

    2. 可变对象：mutable 解释器为每个对象维护不同的内存区域

11. Python对不可变对象维护同一个内存。因为他不可能被改变，因此解释器就复用了。

    ```python
    a = 10
    b = a
    c = 10
    #以上三个变量的 id()的结果是相同的。
    ```

12. 运算后产生的对象由解释器重新建立。因为运算的结果不确定，因此没有对此进行优化。

    ```python
    a="Python计算生态"   # id为2086092911568
    b=a                 # id为2086092911568，和a相同。
    c="Python"          # id为2085979969584
    d="计算生态"         # id为2086075113488
    e=c+d               # id为2086075109168，和a不同
    f="Python计算生态"   # id为2086092913696，和a也不同？？？
    ```

13. 可变对象不做优化。不复用内存。

    ```python
    la = []
    lb = la
    lc = []
    print(id(la)) #81732512
    print(id(lb)) #81732512
    print(id(lc)) #81021088
    ```

14. sys.getrefcount(d) 获取对象d的引用计数

15. 导致引用+1的情况：

    1. 对象被创建，d = DemoClass()

    2. 对象被引用，a = b

    3. 对象被作为函数或方法的参数

    4. 对象被作为一个容器中的元素，ls = [d]

16. 导致引用-1的情况：

    1. 对象被删除，del d
    2. 对象的名字被赋予新的对象，d = 123
    3. 对象离开作用域，例如函数的局部变量
    4. 对象所在的容器被删除，del ls，其中ls = [d]，此时d的引用会-1

17. 列表等组合数据类型中存储的也都是引用。

18. Python默认是浅拷贝，只复制最顶层对象。深拷贝会真实的生成对象。以下这几种情况是浅拷贝。

19. ![1590923708272](Python.assets/1590923708272.png)

20. 列表容器被拷贝，而其中的元素并没有被拷贝。

21. 列表内存储的是对应数据的指针或者引用。此处修改其中一个元素的内容，同时指向该元素的其他列表也会被修改。

22. ![1590923879364](Python.assets/1590923879364.png)

23. 深拷贝需要使用copy库的deepcopy()方法。可以迭代拷贝对象的各层次对象，完全创建新的内存。仅针对可变数据类型。如果遇到不可变数据类型，则不会另外复制一份。

24. ![1590924132074](Python.assets/1590924132074.png)

25. 函数名是对函数本身的引用。类的实例方法名也是对其实例方法的一种引用。

26. 使用对象名.方法名来创建方法的引用。

    ```python
    class DemoClass:
        def __init__(self, name):
            self.name = name
        def lucky(self, salt = 0):
            s = 0
            for c in self.name:
                s += (ord(c) + id(salt)) % 100
            return s
    
    dc1 = DemoClass("老李")
    lucky = dc1.lucky
    print(DemoClass.lucky(dc1, 10))
    print(lucky(10))
    ```

27. ![1590924332588](Python.assets/1590924332588.png)

28. 命名空间：从名字到对象的一种映射。

29. 管理作用域的问题，全局变量名在模块命名空间中有用，局部变量名在函数命名空间中有用。属性和方法在类的命名空间中有用。名字的全称是       命名空间.变量名/函数名    

30. 命名空间底层使用字典类型实现的，变量名是键，变量引用的对象是值。

    1. 复数z，z.real和z.imag时对象z命名空间的两个属性

    2. 对象d，d.name和d.printName()是对象d命名空间的属性和方法

    3. global和nonlocal是两个声明命名空间的保留字

31. 命名空间互相嵌套 global声明是模块命名空间（全局命名空间）中的变量，nonlocal声明不是本命名空间中的，而是向上层命名空间寻找，直到找到为止。

    ```python
    count = 0       #模块的命名空间
    def getCounting(a):   #第一层函数的命名空间
        count = 0
        if a != "":
            def doCounting():   #第二层函数的命名空间
                nonlocal count
                count += 1
            doCounting()
        return count
    print(getCounting("1"), count)  #记得测试，然后给出结果
    print(getCounting("2"), count)
    print(getCounting("3"), count)
    ```

32. 类的特性装饰器：使用对象名.属性名来给属性赋值时，是无法进行安全检测的。可以使用@property来做。使用@property把类中的方法变成对外可见的属性，内部表现为方法，外部表现为属性。

    ```python
    class DemoClass:
        def __init__(self, name):
            self.name = name
        @property     #有了@property修饰，会产生一个age方法同名的属性，获取属性时会调用该方法
        def age(self):  #右值
            return self._age
        @age.setter  #方法名.setter用于设定属性的赋值操作，对属性进行复制时会调用该函数，=右侧会赋值给value参数
        def age(self, value):  #左值
            if (value < 0) or (value > 100):
                value = 30
            self._age = value
    
    dc1 = DemoClass("老李")
    dc1.age = -100  #等价于调用dc1.age(-100)
    print(dc1.age)  #等价于调用dc1.age()，结果为30
    ```

33. 获取该属性的值或给属性赋值时，会自动调用对应的方法，并传参。这样做的目的是为了方便用户使用，毕竟属性要比方法更容易使用，同时也能增加对属性获取或写入的控制。

34. 异常也是一种对象，自定义异常需要继承自Exception类。使用raise来主动产生异常。

35. 可以重载异常的构造方法，as e是捕获并引用异常对象。

    ```python
    class DemoException(Exception):          #自定义一个异常类型
        def __init__(self, name, msg = "自定义异常"):
            self.name = name
            self.msg = msg
    
    try:
        raise DemoException("脚本错误")  #抛出对应的异常对象
    except DemoException as e:  #捕获对应的异常对象，标识为e
        print("{}异常的报警是{}".format(e.name, e.msg))  #输出为"脚本错误异常的报警是自定义异常"
    ```

36. Python通过_对名称（属性+方法）进行修饰，来完成预定的功能，一共分为5种情况：

    ```python
    _X  #为类内部使用，PEP8。只是约定，仍然可以通过\<对象名\>.\<属性名\>的方式访问。使用from XX import *时不会导入单下划线开头的属性或方法。
    X_  #为了避免于保留字或已有命名冲突，PEP8只是约定，无任何功能性对应
    __X  #将会被解释器修改名称，避免命名冲突，例如__abc会被修改为_类名__abc
    __X__  #无任何特殊意义，名字不会被修改
    _ #无特殊意义
    ```

37. 约定内部调用，然是仍然可以在外部访问到。

38. __是一种约束，不是约定，因为他已经做了一些修改。

39. 一些保留方法（属性）使用这种前后都有双下划线的做法。

40. 例如for in循环便利时，如果循环变量没有被用到，可以使用_。

41. 定义了一个没有任何内容的类，就是最小空类。类实际上就是命名空间，最小空类可以当命名空间使用。最小空类可以辅助数据存储和使用。动态增加属性是python类的一个特点。

    ```python
    class <类名>:
    	pass
    ```

42. 类支持动态增加属性，当做一个命名空间使用。使用dict来访问所有数据。

    ```python
    class EmptyClass:  #建立一个最小空类
        pass
    a = EmptyClass()
    a.name = "老李"    #通过增加属性实现数据保存
    a.age = 50
    a.family = {"儿子":"小李","女儿":"小李女"}
    print(a.__dict__)  #结果为字典 {'name': '老李', 'age': 50, 'family': {'儿子': '小李', '女儿': '小李女'}}
    ```

# 序列化对象

1. pickle模块可以将对象序列化，方便写入到文件中。
2. pickle.dump处理浮点数组，几乎和array.tofile一样快。不过前者可以处理几乎所有的内置类型和用户自定义的类。

# 正则表达式

1. 完整的正则表达式由2种字符组成，特殊字符（也成为元字符）和文字（也成为普通字符）。另一种很像正则表达式的是文件名匹配格式，例如Shell工具中`*.txt`表示所有以.txt结尾的文件。正则表达式比文件名匹配的功能更强大，因为它提供了更多的元字符。

2. 完整的正则表达式由小的构建模块单元组成，每个单独的构建模块很简单，不过它们可以组合起来构成复杂的正则表达式。

3. 文本检索是正则表达式最简单的应用之一，Linux下的egrep命令就是做这个的，需要指定搜索的正则表达式（第一个参数）和文件（后续所有参数），egrep会尝试用正则表达式去匹配每个文件的每一行，并显示能够匹配的行。

   ```shell
   egrep '^(From|Subject): ' mailbox-file
   #需要将正则表达式使用特定一对字符包裹起来，这是Shell的要求，否则会将其中的*解释为Shell所支持的通配符等，它并不是正则表达式的一部分。
   ```

4. 不同命令所支持的正则表达式的元字符的数量和范围不同。正则表达式可以不包含元字符。

5. 正则表达式的搜索不是基于单词的，因为它不理解英语，只是将其当作字符序列。

6. 用来表示行首的元字符是脱字符^，行尾的元字符为美元符号$。二者的特殊就在于它们匹配的是一个位置，而不是具体的文本。`^$`匹配一个空行，`^`匹配所有行，因为每行都有开头，`$`匹配所有行，因为每行都有结尾。

7. `^cat`应该理解为匹配的是以c作为一行的第一个字符，紧接一个a，然后是一个t的文本。而非匹配以cat开头的行。二者的含义相同，但是前者更符合正则表达式工作的逻辑。

8. 字符组可以匹配若干字符之一，`a`匹配字符a，`b`匹配字符b，`[ab]`能匹配字符a或b。例如`gr[ea]y`可以匹配grey或gray。

9. 在字符组内部可以使用字符组元字符-来表示一个范围，例如`H[1-4]`等价于`H[1234]`。一个字符组内可以有多个范围简写，例如`[1-4a-d]`等价于`[1234abcd]`。

10. 字符组内各字符的顺序可以交换，不影响效果，不过包含-的，需要连带-进行交换。

11. 字符组的内部和外部，关于元字符的范围和含义是不同的。

12. 需要注意，只有在字符组内部，-才是元字符，否则就是普通的连字符。不过当它出现在字符组内的开头时（对于排除型字符组，则是^之后的第一个字符），不表示为元字符，而是普通的连字符。同理，?和.在字符组内就是普通字符。例如正则表达式`[0-9a-z_!.?]`中包含一个字符组，该字符组中包含6类字符，只有-是元字符。

13. 字符组的开头如果是^，则为排除型字符组，及匹配任何未列出的字符，例如`[^1-4]`匹配除了1到4以外的任何字符。如果该字符在字符组内，但是不是第一个字符，则表示一个普通的字符。

14. 排除型字符组中只包含一个字符往往是有意义的，这个和非排除型字符组不同，例如`[a]`等价于`a`，因此几乎都会使用后者。而`[^a]`表示匹配除了a以外的任何字符，因为无法列出所有满足条件的字符，因此有时必须使用排除型字符组。

15. 注意排除型字符组的意思是匹配一个未列出的字符，而非不要匹配列出的字符。也就是说排除型字符组也是需要匹配一个字符的，不能啥也不匹配。

16. 通常来说，每行末尾都有一个换行符，egrep会将这些行符去掉后再进行匹配。因此`q[^u]`无法匹配`Iraq`，因为字符q后面没有一个非u字符了。

17. 点号是一个元字符，表示匹配任意字符的字符组，即任意一个字符，一般用作占位符。

18. 例如需要搜索不同格式的某天，例如`2025/03/05`，`2025-03-05`或`2025.03.05`等形式，可以使用`2025[-./]03[-./]05`，或者简单使用`2025.03.05`。注意，在字符组内，点号不是元字符。不能写作`[.-/]`因为-在这里表示范围，但是这不是一个有效的范围。`[./-]`也不对。

19. 由于点号能匹配任何字符，因此`2025.03.05`也能匹配`2025103205`，所以用户应该在精确和易用方面进行取舍，这取决于用户对要检索的文本的了解和所需要的精确性。例如如果认为文本中不可能出现`2025103205`这样的例外，就可以使用宽泛的正则表达式。

20. 普通字符组表示子集，^表示补集，点号表示全集，没有空集。

21. |是一个元字符，表示或的意思，使用它将不同的表达式组合成一个总表达式，这个总表达式能够匹配任意的子表达式，也成为多选分支。`gr[ea]y`等价于`gray|grey`或`gr(e|a)y`，后者使用括号来划定多选分支的范围，其中的括号不能省略，因为`gre|ay`表示匹配gre或ay。

22. 如果|出现在字符组内，则表示普通字符含义。

23. 多选结构可以包含很多字符，但是不能跨越括号的界限。

24. `First|1st`等价于`(Fir|1)st`。

25. 注意，字符组和多选结构是不一样的，前者只能匹配多个字符中的一个，后者可以匹配多个表达式中的一个，而每个表达式可以是任意丰富的。

26. 在包含多选结构的表达式中使用^和$时需要注意，例如`^From|Subject|Date: `和`^(From|Subject|Date): `不同。后者展开后是`^From: |^Subject: |^Date: `，而前者匹配的是`^From`，`Subject`，`Date: `三个中的任意一个。

27. 正则表达式语法是严格区分大小写的，不过这些支持正则表达式的程序都提供忽略大小写的功能，例如egrep的-i选项，需要放在正则表达式参数之前。

28. 有时希望匹配的内容出现在单词的开头或结尾，或者就是一个完整的单词，此时可以使用单词分界符，某些版本的egrep对此提供了有限的支持，元字符分别为`\<`和`\>`，类似于^和$，它们也只是位置匹配，不对应任何字符。

29. 注意，`<`和`>`本身并不是元字符，只有当它们和`\`结合起来时，整个序列才表示元字符。

30. 有些版本的egrep并不能很好地识别英文单词的边界，软件认为的单词并非是英文单词，而是一个连续的字母数字序列。例如

    ```shell
    That dang-tootin' #@!%* varmint's cost me $192.95!
    ↑  ↓ ↑  ↓ ↑    ↓        ↑     ↓ ↑↓↑  ↓ ↑↓  ↑ ↓ ↑↓
    #注意varmint's会被认为是2个单词，第二个单词就是一个字符s
    #192.95也被认为是2个单词，分别为192和95。
    ```

31. ?表示可选项元字符，表示它前面的字符可有可无。一般将?和它前面的字符一同称为要给元字符序列，类似于`\>`这样的元字符序列。

32. 例如`colou?r`可以匹配color或colour，也可以写成`color|colour`。`u?`可以匹配`ccccsa`，实际上它可以匹配任意内容。

33. ?前面除了是一个字符外，还可以是表达式，此时表示该表达式可有可无，例如`4(th)?`等价于`4|4th`，此时?的作用对象是(th)。

34. 括号内的表达式可以任意复杂， 但是从括号外来看是一个整体，因此可以被?作用。

35. +和*的作用和?类似，统称为量词。

    1. +表示前一个字符出现≥1次。

    2. *表示前一个字符出现≥0次，即任意次。

    3. ?表示前一个字符出现0或1次。

36. 和`u?`一样，`u*`也是永远不会匹配失败。

37. 

38. 

39. 

40. 

41. Python的正则表达式本质上是一种嵌入在Python中的微型、高度专业化的编程语言，可通过re模块使用。它是一种通用的字符串表达框架。可以进行字符串匹配，查找和替换。使用前需要将符合正则表达式语法的字符串编译成正则表达式（一个程序对象）。一次编译，多次使用，效率高。

42. 正则表达式字符串会被编译成一系列字节码，然后由用C编写的匹配引擎执行。对于高级用途，可能需要仔细注意引擎如何执行给定的RE，并以某种方式编写RE以生成运行速度更快的字节码。

43. 正则表达式语言相对较小且受限，并非所有字符串处理任务都可以使用正则表达式完成。有时正则表达式非常复杂，此时最好编写Python代码来进行处理，虽然后者运行速度较慢，但它更容易理解。

44. 正则表达式背后的理论是确定性有限自动机DFA和非确定性有限自动机NFA。

45. 元字符一共包含`. ^ $ * + ? { } [ ] \ | ( )`。

46. 所有的元字符（除了\以外），在字符组中都不起作用。

47. 

48. pattern和string还有repl可以是Unicode字符串str，也可以是8位字符数组bytes，但这三个参数必须都相同。

49. 两种主要的使用模式：

    1. 匹配，测试一下整个字符串和这个正则表达式是否完全匹配，结果为bool值。

    2. 查找，在整个字符串中寻找符合正则表达式的子串。可见匹配是查找的一个特例，相当于加了^和$。

50. 字符串abc不匹配正则表达式ab，但是在该字符串内查找正则表达式对应的字串，是可以找到的。

51. 正则表达式：普通字符+元字符

    ```python
    P(Y|YT|YTH|YTHO)?N   #其中()，|，?都是元字符
    ```

52. 以字符为基本操作单元。

53. ```shell
    操作符  说明                              实例
    .      匹配任何单个字符             a、1等
    []     匹配字符集合中的任意一个      [abc]表示a或b或c；[a-z]表示从a到z的任意一个字符
    [^]    匹配字符集合意外的任意一个    [^abc]表示匹配除了a、b、c以外的任意一个字符。
    *      前一个字符的0或无限次扩展     abc*可以匹配ab、abc、abcc、abccc等
    +      前一个字符的1或无限次扩展     abc+可以匹配abc、abcc等
    ?      前一个字符的0或1次扩展        abc?只可以匹配ab、abc这两个字符串。
    |      匹配左右表达式中的任意一个即可 d(abc|def)g只可以匹配dabcg、ddefg这两个字符串。    
    {m}    前一个字符扩展m次            ab{2}c 只可以匹配abbc
    {m,n}  前一个字符扩展m到n次(含n)    ab{1,2}c 只可以匹配abc、abbc。可以省略任意一个m最小为0，n最大为无穷大
    ^      匹配字符串的开头             ^abc可以匹配abc,abcd、abcf、abcdefsf等。这里说的匹配是可以查找到子串的意思。
    $      匹配字符串的结尾             abc$可以匹配dabc、dsfaabc等
    ()     分组标记，方便后续使用的时候引用，可以和任意模式联动。他后面的*+?对整个编组起作用。
    ```

54. 正则表达式预先定义了一些常用的字符，元字符，大多数以\开头。例如：

    ```python
    \d      [0-9]                #数字字符，如果是Unicode字符的话，除了[0-9]，也包括各种语言中的数字。
    \w      [0-9a-zA-Z_]         #单词字符(英文字母，数字，下划线)
    \s      []                   #空白字符(空格,制表符,换行符)
    
    #以上的元字符的字母大写，表示非对应的字符，例如\D表示出了数字字符以外的任意字符。
    #如果要匹配.*+?这类元字符，需要使用\转义。
    ```

55. 经典的正则实例：

    ```shell
    ^[1-9]\d*$      #正整数，不是^[0-9]*[1-9][0-9]*$ 因为它能匹配010之类的非整数。
    ^[A-Za-z]+$     #由26个字母组成的字符串
    ^[A-Za-z0-9]+$  #由26个字母和数字组成的字符串
    ^-?\d+$         #整数形式的字符串
    ^[0-9]*[1-9][0-9]*$  #正整数形式的字符串
    [1-9]\d{5}      #国内邮政编码,6位
    [\u4e00-\u9fa5] #Unicode中文字符
    \d{3}-\d{8}|\d{4}-\d{7}  #国内电话号码
    ```

56. IP地址的精确匹配。

    ```shell
    0-99       #[1-9]?\d
    100-199    #1\d{2}
    200-249    #2[0-4]\d
    250-255    #25[0-5]
    #因此0-255就是  ([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])
    #ip地址形如 x.x.x.x，正则如下：
    (([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])
    #其中\.是对.的转义。
    ```

57. re库使用原生字符串来表达正则表达式。原生字符串不包含转义符，即它里边的\不被解释为转义符。也可以使用string来表达，不过更复杂。

58. 原生字符串：r"字符串内容"。

    ```python
    print("\n")   #表示包含一个字符的字符串
    
    print(r"\n")  #表示包含了2个字符的字符串
    \n
    ```

59. re库常用方法：

    ```python
    re.search(pattern,string,flags=0)    #在字符串string中搜索匹配正则表达式pattern的第一个位置，返回match对象。其中pattern应为原生字符串。flags为控制标记，有以下几种情况：
    
    #re.I 或re.IGNORECASE  忽略大小写区别
    #re.M 或re.MULTILINE   认为字符串中可以包含多个换行符，此时^将匹配字符串中的换行符，而不是仅仅是整个字符串的开头。使用\n将字符串分割为多行，每一行进行一次匹配
    #re.S re.DOTALL        .操作符能够匹配所有字符，默认情况下.只能匹配除换行符以外的任意字符。
    
    re.search(r"\d{6}",'HIT 150006 BIT 100081')
    <re.Match object; span=(4, 10), match='150006'>  #就是'HIT 150006 BIT 100081'[4:10],span从0开始计数，不包括10
    
    re.search(r"[a-z]","ABCdef",re.I)  #忽略大消息，可以匹配A
    <re.Match object; span=(0, 1), match='A'>
    re.search(r"[a-z]","ABCdef")       #默认区分大小写，第一个匹配d
    <re.Match object; span=(3, 4), match='d'>
    
    re.search(r"^[a-z]","ABC\ndef")  #将整个字符串当作一行，什么也匹配不到
    re.search(r"^[a-z]","ABC\ndef",re.M)  #使用\n将字符串分割为多行，每一行进行一次匹配。因此可以匹配第二行的开头
    <re.Match object; span=(4, 5), match='d'>
    
    re.search(r".","\n")       #.无法匹配换行符
    re.search(r".","\n",re.S)  #此时可以匹配换行符
    <re.Match object; span=(0, 1), match='\n'>
    ```

60. ```python
    re.split(pattern, string, maxsplit, flags=0) #将字符串string按照正则表达式pattern匹配的结果进行分割，返回列表类型，每个元素都是字符串，类似于str的分割操作。其中maxsplit为最大分割数，如果达到了最大分割数，后面的匹配不会再进行分割，而是作为一整个元素存入列表。
    re.split(r"\d{6}",'HIT 150006 BIT 100081')
    ['HIT ', ' BIT ', '']  #如果匹配发生在末尾处，列表最后会有一个空字符串。
    re.split(r"\d{6}",'HIT 150006 BIT 100081',maxsplit=1)
    ['HIT ', ' BIT 100081']#达到最大分隔数之后，就不再匹配了。
    ```

61. ```python
    re.sub(pattern,repl,string,count=0,flags=0) #将字符串string中所有的匹配正则表达式pattern的子串替换为repl，返回替换后的字符串。最多替换count次。repl可以是字符串或函数。如果repl是字符串，那么\1,\2等表示匹配对象的group(1)和group(2)。如果repl是函数，则在每一次匹配成功时，它都会被调用，该函数接受一个match对象作为参数，返回一个用来进行替换的字符串。
    
    re.sub(r"\d{6}","abc",'HIT 150006 BIT 100081')
    'HIT abc BIT abc'
    
    re.sub(r'(d.* )(myfunc)',r"\2",'def myfunc') #\1必须要在原生字符串中，因为str是无法对1进行转义的。
    'myfunc'
    re.sub(r'(d.* )(myfunc)',r"\1",'def myfunc')
    'def '
    
    def repfunc(matchobj):
        if matchobj.group(0).startswith("15"):  #如果匹配的字符串以15开头
        	return "hlj"
        elif matchobj.group(0).startswith("10"):
            return "bj"
        else:
            return ""
    re.sub(r"\d{6}",repfunc,'HIT 150006 BIT 100081')
    'HIT hlj BIT bj'
    ```

62. ```python
    re.match(pattern, string, flags=0) #字符串开头匹配，可以看作是只在开头进行搜索的search
    re.match(r"abc","abcdde")
    <re.Match object; span=(0, 3), match='abc'>
    re.match(r"abc","cabcdde")  #匹配失败
    
    re.fullmatch(pattern, string, flags=0) #字符串完全匹配。
    re.fullmatch(r"abc","abc") 
    <re.Match object; span=(0, 3), match='abc'>
    re.fullmatch(r"abc","abcdde") #匹配失败
    ```

63. ```python
    re.findall(pattern, string, flags=0)  #使用正则表达式pattern不重叠地搜索整个string。将搜索到的结果存入一个列表中。
    re.findall(r"\d{6}",'HIT 150006 BIT 100081') 
    ['150006', '100081']
    re.finditer(pattern, string, flags=0) #使用正则表达式pattern不重叠地搜索字符串string，返回一个迭代器，迭代元素为match对象。
    for match in re.finditer(r'\d{6}','HIT 150006 BIT 100081'):
    	print(match.group(0))
    150006
    100081
    ```

64. re库除了可以使用上面的函数外，还可以先将正则表达式编译成对象，然后使用正则对象来进行查找替换等。正则对象的函数中没有原生字符串的参数，因为他已经被包含入了正则对象中。

    ```python
    rst = re.search(r"[1-9]\d{5}","BIT 100081")
    #等价用法如下
    pat = re.compile(r"[1-9]\d{5}")  #还可以接受两个参数，搜索的起始下标，结束下标。
    rst = pat.search("BIT 100081")
    ```

65. 并非每次match都是从字符串的起始位置开始匹配。

    ```python
    pat = re.compile(r"[1-9]\d{5}")
    rst = pat.search("BIT 100081",2) #下标从2开始搜索
    rst.pos   #结果为2
    ```

66. match对象包含了匹配的相关信息。

    ```python
    rst = re.search(r"[1-9]\d{5}","BIT 100081")
    
    rst.string   #'BIT 100081' 整个字符串
    rst.re       #re.compile(r'[1-9]\d{5}', re.UNICODE)
    rst.pos      #0 正则表达式搜索文本的开始文件，一般就是字符串的开头下标，可以修改
    rst.endpos   #10 正则表达式搜索文本的结束位置，一般就是字符串的结尾下标，可以修改
    rst.group(0) #'100081' 获得匹配后的字符串
    rst.start()  #4  匹配开始的下标
    rst.end()    #10 匹配结束的下标
    rst.span()   #(4, 10)   返回(.start(),.end())
    ```

67. re库默认使用贪婪匹配，当在同一个位置有多个匹配可能时，会选择最长的那个匹配。这种情况一般出现在*，+，？和{m,n}。只需要在原来的这些符号后面加上?即可执行最短匹配。

    ```shell
    re.search(r"PY.*N", "PYANBNCNDN")   #默认，执行贪婪匹配，会匹配到PYANBNCNDN整个字符串
    re.search(r"PY.*?N", "PYANBNCNDN")  #会执行最短匹配，匹配到PYAN。
    ```

# Conda

1. Conda是一个开源的包管理系统，最早是为了Python开发的，不过现在可以为Java，R等语言服务。

2. Conda可以快速的安装，更新包，并解决依赖问题。同时可以创建，并快速切换环境。conda将一切都视为包，包括Python和conda自己。

3. 概念区分

   1. conda是包和环境管理工具，比Python自带的pip更强。
   2. Anaconda是Python+conda+一系列的科学计算所需的包
   3. Miniconda是Python+conda

4. 默认情况下，Conda从https://repo.anaconda.com/下载打包好的包，这些包由Anaconda®负责维护。

6. 查看帮助：

   ```python
   conda --help   查看整个conda的帮助说明
   conda install --help
   ```

7. 默认情况下，Conda会安装最新版本的包，这样可能会导致更新其他依赖的包。可以使用    --freeze-installed      选项来强迫安装旧版本。

8. ```python
   conda install  #包名 
   -n                      #指定环境名，默认在当前环境中安装。
   --update-all, -all      #更新环境内的所有已安装的包。
   -q                      #安静模式，不显示进度条。
   -y                      #不用询问，直接确认。
   -c defaults             #使用默认的通道来下载，这个在.condarc中定义了。
   --channel $URL $PACKAGE_NAME  #从特定的通道来下载
   
   conda install python=x.x      #安装指定版本的Python，而不一定是最新版本的。
   ```

9. ```python
   conda clean     #清除无用的包和缓存
   -a, -all        #清除所有文件
   -i, -index      #清除索引文件
   -t, -tarballs   #清除tarball文件，实际是源码的压缩包。
   -d              #仅显示要进行的操作，而不执行。
   
   conda config --show         #显示conda的内部配置数值。
   conda config --show-sources #显示配置的来源
   
   conda create     #可以根据一系列的包来创建一个conda环境。环境之间是相互独立的。
   -n, --name       #指定环境名
   -p, --prefix     #指定存储环境的目录
   --copy           #通过复制的方式创建环境，而不是建立链接。
   
   conda create -n myenv sqlite  #创建一个名为myenv的环境，里边只有一个sqlite包。
   
   codna update 包名          #更新对应的包，在默认的环境下。
   conda update --all        #更新所有包。
   conda update conda        #更新conda本身
   conda update python       #更新Python到最新，2代不能更新到3代。
   ```
   
13. ```python
    conda info       #显示信息
    -a, --all        #显示所有的信息
    --base           #显示base 环境的路径。
    -e, --envs       #显示本地已有的环境。
    -s               #显示环境变量。
    
    (base) C:\Users\Administrator>conda info -e
    # conda environments:
    #
    base                  *  D:\Anaconda3
    
    conda list         #显示所有的已安装的包
    -n 环境名           #指定环境
    --no-pip           #不包含pip安装的包
    
    conda remove   包名       #删除指定的包     等价于uninstall
    -all                      #删除环境内的所有包
    
    conda search 包名     #在网络上搜索对应的包
    --envs                #在所有环境中搜索
    -i, --info            #显示详细信息
    
    conda search scikit-learn   #搜寻是否存在一个scikit-learn的包。不要求完全匹配
    ```
    
17. Conda的配置文件在用户目录下，C:/users/Administrator/.condarc。默认是不存在，第一次运行conda config时会生成。

18. ```
    show_channel_urls: true
    channel_alias: http://mirrors.tuna.tsinghua.edu.cn/anaconda
    default_channels:
      - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
      - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
      - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
      - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
      - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
    custom_channels:
      conda-forge: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      msys2: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      bioconda: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      menpo: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      pytorch: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      simpleitk: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    ssl_verify: true
    channels:
      - defaults
    ```

19. ```python
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ #添加清华镜像源
    conda config --set show_channel_urls yes         #显示通道地址
    ```

20. 环境相关操作：

    ```python
    conda create --name 环境名    #要包含的一系列包名，空格分隔        默认的环境是空的，任何包都没有，需要先安装Python。
    conda activate  环境名        #切换到对应的环境
    conda deactivate             #关闭退出该环境
    ```

21. conda的环境不仅仅是对Python的包管理，他也和操作系统的shell有关联。例如在R36环境中安装了R语言包，在base环境中用which R 就找不到该命令。

22. 新创建的环境的根目录都在anaconda/envs中，base环境的根目录就在anaconda路径中。

23. 有些包安装完之后会有可执行程序供使用，他们都存放在anaconda/scripts

24. 使用conda安装的软件，需要activate对应的环境，才可以使用，否则会报错，Python也是一样。

25. anaconda自带的Spyder也是安装在base环境中的，要在Spyder中使用别的版本的Python，可以新建一个环境，安装Spyder使用。

# 包管理器

1. 安装第三方库：①pip安装，②集成安装③文件安装。
2. pip install 库名；pip install -U 库名    升级库；pip uninstall 库名 ；pip download 库名   下载但不安装；pip show 库名  列出库的详细信息； pip search 关键词    搜索第三方库（出现在介绍信息或名称中）；pip list 列出所有已安装的库。
3. 利用anaconda可以批量安装，默认自带800多个第三方库。
4. 有些第三方库使用pip可以下载，但是不能安装，因为它提供的是源代码，需要先编译再安装。
5. UCI提供了Windows平台上，需要编译的第三方库的编译后得版本。https://www.lfd.uci.edu/~gohlke/pythonlibs/ 
6. 下载对应版本的whl文件，然后使用 pip install 文件名   即可。
7. Python第三方库的安装：
   1. 全自动安装： `easy_install jieba` 或者 `pip install jieba` / `pip3 install jieba`
   2. 半自动安装：先下载 https://pypi.python.org/pypi/jieba/ ，解压后运行 python setup.py install
   3. 手动安装：将 jieba 目录放置于当前目录或者 site-packages 目录
   4. 通过 `import jieba` 来引用

8. Linux和MAC下pip表示python2，pip3表示python3，Windows下都是pip。
9. 安装了anaconda后有些包如果conda中不存在，需要使用pip进行安装，此时应该先运行activate base，进入base环境后，再执行pip命令，否则会出现连接错误。
10. PEP8是Python的一个代码规范，比较严格。可以使用autopep8插件进行自动格式化。
11. 有时候，安装完python后，在scripts文件夹中找不到pip，可以执行以下命令：

    ```shell
    python -m ensurepip #这一步会产生pip3.exe，如果用的不习惯，可以重命名为pip.exe
    ```

12. 有时更新pip时，会出现ValueError: check_hostname requires server_hostname，此时关掉梯子即可。

# 第三方库

## PyInstaller 

1. PyInstaller 第三方库，将.py源代码生成可执行文件。
2. conda install pyinstaller    安装后在命令行打开使用。程序安装在anaconda/script文件夹下。

3. pyinstaller -F 文件名       在dist目录下会出现一个EXE文件。

   ```python
   -h #查看帮助
   --clean #清理打包过程中的临时文件
   -D, --onedir #默认值，生成dist文件夹
   -F, --onefile #在dist文件夹中只生成独立的打包文件
   -i <图标文件名.ico> #指定打包程序使用的图标文件
   ```

4. 建议用法   pyinstaller -F --clean test.py


## doctest

1. 测试驱动开发（TDD）的精髓就是先写测试。在考虑如何实现一个功能之前，先严格地列出这个功能能做什么，这能帮助我们在编程时把精力花在该花的地方。

2. Doctest是一个轻量级的单元测试框架，它寻找像Python交互式代码的文本，然后执行这些代码来确保它们的确就像展示的那样正确运行。

3. doctest的测试原理：把在Python控制台的输入输出记录保存到函数的文档字符串docstring里，然后一一把这些输入到解释器然后对比输出是否一致，来确定测试结果是否通过。

4. 使用方法：只需要把自己平时在Python交互式控制台上测代码时的输入输出记录，拷贝到docstring里，以后要回归这个函数的时候就可以通过doctest回放测试用例了。

   ```python
   def factorial(n): #定义一个函数，下面是它的文档字符串
       """Return the factorial of n, an exact integer >= 0.
   以>>>开头的行会被识别为测试例子，
       >>> [factorial(n) for n in range(6)]
       [1, 1, 2, 6, 24, 120]
       >>> factorial(30)
       265252859812191058636308480000000
       >>> factorial(-1)
       Traceback (most recent call last):
           ...
       ValueError: n must be >= 0
   
       Factorials of floats are OK, but the float must be an exact integer:
       >>> factorial(30.1)
       Traceback (most recent call last):
           ...
       ValueError: n must be exact integer
       >>> factorial(30.0)
       265252859812191058636308480000000
   
       It must also not be ridiculously large:
       >>> factorial(1e100)
       Traceback (most recent call last):
           ...
       OverflowError: n too large
       """
       import math
       if not n >= 0:
           raise ValueError("n must be >= 0")
       if math.floor(n) != n:
           raise ValueError("n must be exact integer")
       if n+1 == n:  # catch a value like 1e300
           raise OverflowError("n too large")
       result = 1
       factor = 2
       while factor <= n:
           result *= factor
           factor += 1
       return result
   
   if __name__ == "__main__":
       import doctest
       doctest.testmod()
   ```

5. 如果函数功能简单，可以直接在docstring里写测试用例，但是如果函数功能比较复杂，或者测试用例比较多，那么写到docstring里就太长了。Doctest支持把测试代码抽离到另外一个文本文件中，然后通过解析该文件的方式运行测试。


# 元对象协议

1. 元对象协议是对象模型的同义词，也就是构建核心语言的API。元对象是指那些对建构语言本身来说很重要的对象，协议指的是接口。
2. 一套丰富的元对象协议，允许程序员对语言进行扩展，让它支持新的编程范式，
3. 面向方面编程，Aspect Oriented Programing，AOP。


# 脚本

1. 脚本的执行在Unix下有两种方式：

   ```shell
   python a.py  #这种情况下不要求a.py文件具备执行权限。
   ./a.py       #这种情况要求a.py文件具备执行权限，同时还要求在该文件的第一行注明解释器的绝对路径，例如  #!/usr/bin/python3     或者用环境变量 #!/usr/bin/env python3
   ```

# 自动化 pyautogui

1. pyautogui可以执行鼠标和键盘的动作，并进行一些图像识别工作来自动化。

2. 在Windows上，PyAutoGUI通过内置的`types`模块访问Windows API（也称为WinAPI或win32 API）。`nicewin`模块提供了如何通过Python进行Windows API调用的演示。

3. 可以设置`pyautogui.PAUSE = 0.2`来在每个pyautogui调用之间插入一个休眠时间0.2秒。

4. 可以设置`pyautogui.FAILSAFE = True`来开启安全模式，此时在程序运行中若将鼠标移动到左上角，则程序会抛出异常`pyautogui.FailSafeException`然后终止，这样可以防止程序跑飞了。

5. 对于一个1920x1080的屏幕，坐标范围为`[0,1919]x[0,1079]`。

6. 建议为程序分别添加一个开始热键和结束热键，而不是一运行就开始执行任务，因为一般要达到某个初始状态才可以执行动作，按键记得有始有终，结束后应该恢复到默认状态，运行前记得检查输入法的状态是否正确。常用模板如下：

   ```python
   #! python3
   import keyboard
   import pyautogui
   import time
   import sys
   pyautogui.PAUSE = 0.2
   pyautogui.FAILSAFE = True
   
   def dosomething():
       pyautogui.press("esc")
       pyautogui.hotkey("ctrl", "h") #按下组合键
       pyautogui.write(r"^TI (.*\n)*?^\w")
       pyautogui.hotkey("alt","enter")
       pyautogui.hotkey("alt","l")
       pyautogui.hotkey("ctrl","h")
       pyautogui.write(r"\n   ")
       pyautogui.press("tab")
       pyautogui.hotkey("ctrl","a")
       pyautogui.press("delete")
       pyautogui.press("space")
       pyautogui.hotkey("ctrl","alt","enter")
       pyautogui.press("esc")
   
       pyautogui.press("esc")
       print("完成一次")
   
   print("自动化已启动，默认最小化窗口")
   pyautogui.hotkey("win","down")
   keyboard.add_hotkey("f8", dosomething) #每按一次f8，就会调用一次dosomething函数。
   keyboard.wait("f9") #等待f9，按下后就会结束整个程序，也可以手动关闭程序。
   ```

7. 鼠标功能：

   ```python
   import pyautogui
   width, height = pyautogui.size()  # 返回屏幕分辨率
   x, y = pyautogui.position()   # 返回当前鼠标位置，屏幕左上角为原点，向右为x轴正向，向下为y轴正向。
   pyautogui.onScreen(1919, 500) # 判断给定位置是否在屏幕上
   #移动鼠标
   pyautogui.moveTo(900, 900, 1)  # 移动鼠标到绝对位置，第三个参数是整个动作的时长duration，前两个参数如果为None，则表示当前鼠标位置，这样就只会在一个方向上移动鼠标。
   pyautogui.move(0, 60, 1)  # 按照相对当前的位置移动鼠标
   #拖动，按住一个键的情况下移动鼠标
   pyautogui.dragTo(800, 800, 1, button="left")  # 左键拖动，绝对位置
   pyautogui.drag(0, 200, 1, button="right")  # 右键拖动，相对位置
   #点击鼠标,如果没有给定任何参数，则会当前位置左键单击一次。
   pyautogui.click(100, 100, duration=1, clicks=2, interval=0.8, button="right") # 鼠标会先移动到指定位置，用时为1秒，然后右键点击2次，间隔为0.8秒。button可以取值为left,middle,或right。
   #如下函数都是对click的包装
   pyautogui.rightClick()
   pyautogui.middleClick()
   pyautogui.doubleClick()  # 左键双击，比自己设定click的interval更好
   pyautogui.tripleClick()  # 左键三击
   #如下2个是click的拆分，拖动的底层就是按住，移动鼠标，再松开
   pyautogui.mouseDown()  # 保持按下鼠标的状态
   pyautogui.mouseUp()  # 保持松开鼠标
   #
   pyautogui.scroll(1000)  # 滚动鼠标滚轮，并非是按照鼠标滚轮上的一段一段滚动的。正数表示向上滚动滚轮，屏幕一般会向下移动，但是也可以设置向上移动。
   #在OS X和Linux平台上，还可以调用hscroll()函数执行水平滚动。起始scroll是vscroll的包装。
   ```

8. 默认情况下，duration都是0，表示立即完成该动作。如果比`pyautogui.MINIMUM_DURATION`小，则会立即完成，该值默认是0.1秒。

9. 通常情况下，鼠标会沿直线匀速运动。pyautogui还支持定制移动功能，这可以在move的第4个参数tween中设置，该参数接受一个函数，该函数接受一个0到1的参数，返回一个0到1的参数，输入表示时间比例，输出表示位置比例，默认为linear，也就是输入=输出。官方自带了一下几种模式：

   ```python
   #只有在duration参数不为0时才会生效。
   pyautogui.easeInQuad     # start slow, end fast
   pyautogui.easeOutQuad    # start fast, end slow
   pyautogui.easeInOutQuad  # start and end fast, slow in middle
   pyautogui.easeInBounce   # bounce at the end
   pyautogui.easeInElastic  # rubber band at the end，移动到终点后，在终点晃动
   #tween为补间动画的意思，easing为缓动的意思。更复杂的功能可以使用pytweening库实现。
   ```

10. drag和dragRel，move和moveRel，write和typewrite都是一样的，前者是pyautogui 1.0后推荐使用的。

11. 键盘功能，按键会转到函数调用时光标所在的位置：

    ```python
    #适用于输入一串内容
    pyautogui.write('Hello world!\n', interval=0.2) # 依次键入字符串中的每个按键，间隔为0.2秒，最后会添加一个回车键。这里只能输入单字符键，无法使用功能键。
    #适用于键入功能键来控制
    pyautogui.press("enter")  # 按下然后抬起一个按键，一般用于按下功能键而非输入文字，大写字母也有效。
    pyautogui.press(["A", "B"], interval=0.2)  # 可以传入一个可迭代对象，这样会依次按下对应的键，注意这里不是热键方式，抬起前一个后，才会按下下一个键。
    pyautogui.press('left', presses=3, interval=0.2) #连续按3下该键，等价于pyautogui.press(['left', 'left', 'left'], interval=0.2)
    #最基本的按键事件
    pyautogui.keyDown("F1")  # 按下按键并保持
    pyautogui.keyUp("F1")  # 释放按键
    #热键的输入方式
    pyautogui.hotkey("ctrl", "v", interval=0.2)  # 依次按下这些键，然后按照相反的顺序依次释放。相当于2个keyDown和2个keyUp
    ```

12. 可以使用hold上下文管理器来进行组合按键：

    ```python
    with pyautogui.hold('shift'):
            pyautogui.press(['left', 'left', 'left']) #等价于按住shift，然后连按3下left，再松开shift。
    #等价于如下按键组合
    pyautogui.keyDown('shift')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.keyUp('shift')
    ```

13. 所有支持的按键名称可以通过`pyautogui.KEYBOARD_KEYS`获得：

    ```python
    ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', 
    '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 
    'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']
    # apps就是右侧的win键右侧的那个键，相当于鼠标右键
    ```

14. 显示提示框和用户交互：

    ```python
    pyautogui.alert(text='This is text', title='This is title', button='OK') #显示一个提示框，只有一个确定按钮，总是返回button的字符串。
    pyautogui.confirm(text='This is text', title='This is title', buttons=['OK', 'Cancel']) #包含确定和取消2个按钮，关闭对话框相当于按取消，会返回buttons中的一个字符串。
    pyautogui.prompt(text='This is text', title='This is title' , default='默认内容') #包含确定，取消2个按钮和1个输入框，用户输入后按确定，可以返回输入的字符串。按取消时返回None。
    pyautogui.password(text='', title='', default='', mask='*') #功能和prompt类似，不同的是，输入的字符会被mask替换，用于输入密码。
    ```

15. pyautogui使用PyScreeze和Pillow/PIL库来处理图像相关的工作。在Linux上，还需要安装scrot库来进行开启截图功能，OS X使用操作系统自带的`screencapture`命令。

    ```python
    # 截图，区域的左上角为100,100，尺寸为500x500。当未指定区域时，截取整个屏幕。指定路径时，会保存截图文件。
    image1 = pyautogui.screenshot("b.png", region=(100, 100, 500, 500))  # 返回值为一个<PIL.Image.Image image mode=RGB size=1920x1080 at 0x24C3EF0>图像对象，也可以不指定文件地址，来直接使用图像对象。region的格式是(x,y,dx,dy)。
    
    imagebox = pyautogui.locateOnScreen("b.png", region=(100, 100, 500, 500), grayscale=True) # 在屏幕上查找和图片b.png内容相同的区域的第一个，找到时返回(left, top, width, height)。从0.9.41开始，找不到时会报ImageNotFoundException异常，而非返回None。region参数用来设定在屏幕上截取和搜索的范围，开启灰度匹配，这样可以提高比对速度，大约30%，也能一定程度模糊颜色区别或者产生假阳性结果（即将不匹配的认定为匹配）。
    pyautogui.locateAllOnScreen #会在屏幕上找到所有相同的区域，返回一个生成器，能够生成位置大小的4元组。查找顺序是从左上角，逐行查找到右下角。可以用for in迭代，或者适用list()承接。
    centerpoint = pyautogui.center(imagebox)  # 根据box返回其中心点对象，可以使用x，y属性来获取值。也可以使用pyautogui.locateCenterOnScreen来直接返回中心点的坐标。
    pyautogui.locateCenterOnScreen("b.png") #等价于locateOnScreen和center。
    pyautogui.click("a.png")  # 在当前屏幕上搜索图片的像素，然后单击其中心。
    #搜索定位的底层操作
    image1.getpixel((100, 100)) # 获取图像中位置为100,100的像素的颜色，会根据颜色格式mode来返回不同的结果，RGB时返回一个三元组，灰度时返回一个数值。
    pyautogui.pixel(100, 100)  # 直接返回屏幕上位置100,100的像素的RGB三元组。
    pyautogui.pixelMatchesColor(100, 100, (255, 255, 255), tolerance=10) # 对100,100位置的像素进行颜色对比，目标颜色为(255,255,255)，每个通道的容差为10。
    pyautogui.locate(needleImage, haystackImage, grayscale=False) #在一系列图像Pillow图像对象中寻找，返回第一个。
    pyautogui.locateAll(needleImage, haystackImage, grayscale=False) #在一系列Pillow图像对象中找到所有。
    ```

16. 在一个1920x1080的屏幕上，截图大概消耗100ms时间，查找大概消耗1到2秒。建议将识别位置的代码放在循环外，一次识别，多次点击。同时尽量少地对全屏截图，全屏搜索，多使用region参数。

17. 可以为locate系列函数定义`confidence=0.9`来设置置信度。不过这需要安装OpenCV才可以。

18. 对于查找返回的生成器，可以使用for in循环依次读取，也可以使用list构造列表。

# keyboard

1. 可以使用keyboard库来hook全局事件，注册热键和模拟按键，它是纯python实现的，没有任何依赖库。该库利用了Windows钩子函数。事件在单独的线程中自动捕获，不阻塞主程序。

2. 注意，使用pyautogui.press施加的按键，不会触发keyboard登记的热键。

3. 功能如下：

   ```python
   import keyboard #注意不是pykeyboard
   keyboard.press_and_release('shift+s, space') #
   
   keyboard.write('abc') #依次按下abc三个键
   
   keyboard.add_abbreviation('@@', 'my.long.email@example.com') #输入@@然后按空格，就会将其替换为后面的字符串。
   
   keyboard.get_current_time() #返回当前时间戳（以秒为单位）。
   keyboard.get_last_time() #返回上次调用 keyboard.wait() 或 keyboard.wait(timeout) 时的时间戳（以秒为单位）。
   
   keyboard.get_pressed() #返回一个字典，其中键是键盘按键事件的类型，值是对应的按键值。
   keyboard.get_key_modifiers() #返回一个字典，其中键是键盘按键事件的类型，值是对应的按键修饰符（如 Shift、Ctrl、Alt 等）。
   keyboard.get_key_status(event_data) #返回一个布尔值，指示键盘按键事件的状态。
   keyboard.get_key_description(event_data) #返回一个字符串，其中键是键盘按键事件的类型，值是对应的按键描述（如 "Key A"、"Key B" 等）。
   ```

4. 注册一个多次使用的热键：

   ```python
   keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey')) #为该热键注册一个函数，当按下ctrl+alt+a时，会调用print函数，并传递参数args，要求args是一个元组，即使只有一个元素。默认是在按键按下时触发，可以设置trigger_on_release=True来改变为抬起时触发。
   keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar')) #按一次PAGE UP，然后再按依次PAGE DOWN会调用函数，这里使用lambda表达式来代替函数。
   keyboard.wait() #永远阻塞当前线程，因为没有指定任何热键，类似于while True，但是while True会使CPU空转，这个不会。
   keyboard.remove_hotkey(event_data, element_data) #移除一个热键。
   keyboard.get_hotkey_status(event_data) #返回一个布尔值，表示热键事件的状态。
   keyboard.get_hotkey_count() #返回一个整数，表示当前活动的热键数量。
   keyboard.get_all_hotkey_status() #返回一个字典，其中键是键盘按键事件的类型，值是对应的状态。
   ```

5. 注册一个只使用1次的热键：

   ```python
   keyboard.wait('space') #阻塞当前线程，直到按下空格键，才会继续执行下面的代码，也就是退出while循环。
   print('space was pressed, continuing...')
   ```

6. 录制按键动作，保存，执行：

   ```python
   recorded = keyboard.record(until='esc') #录制按键序列，直到按下esc键时停止。
   keyboard.play(recorded, speed_factor=3) #以原来3倍的速度执行之前录制的按键
   ```

7. 热键可以是扫描码（数字57代表空格），单个按键（"space"），多个按键（"enter"），多步按键（"alt+F4, enter"）等。

8. 可以发送一个操作系统事件，来执行热键，相当于用于手动按下或抬起热键：

   ```python
   keyboard.send(hotkey, do_press=True, do_release=True) #do_press和do_release表示是否发送对应的按下或抬起事件。
   #该功能的底层是由按下和抬起两个事件组成的
   keyboard.press(hotkey)
   keyboard.release(hotkey)
   keyboard.is_pressed(hotkey) #判断是否处于按下状态
   ```

9. 修饰键就是功能按键，分为sided_modifiers和all_modifiers：

   ```py
   sided_modifiers = {'ctrl', 'alt', 'shift', 'windows'} #在键盘的左右各有一个
   all_modifiers = {'alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows'} #alt gr是一个特殊的按键，在某些语言的键盘上才有。
   keyboard.is_modifier(key) #判断key是否是修饰键，区分大小写。
   keyboard.key_to_scan_codes("s") #将按键s转成扫描码列表，结果为(31,)
   #对all_modifiers中的结果逐个输出如下：
   right shift (54,)
   left shift (42,)
   right alt (56, 57400)
   windows (57435, 91, 57436, 92)
   right windows (57436, 92)
   ctrl (29, 57629, 57373)
   left alt (56,)
   shift (42, 54) #可以看到shift等于right shift和left shift的组合。如果为shift注册热键，则按下左或右shift都可以的。
   left ctrl (29,)
   alt gr (541,)
   right ctrl (57629, 29, 57373)
   alt (56, 57400)
   left windows (57435, 91)
   ```

10. 延迟调用：

   ```python
   keyboard.call_later(fn, args=(), delay=0.001) #延迟1ms后再在一个新的线程中调用函数fn。这可以让系统有足够的事件来处理之前的事件，同时也不阻塞当前的线程。
   ```

11. 按键钩子函数：

    ```python
    keyboard.hook(callback, suppress=False, on_remove=<lambda>) #注册一个按键监听器，按下或抬起任何键都会调用callback，参数为keyboard.KeyboardEvent类型的一个对象。返回创建的event handler，后续可以使用这个对象来卸载监听器。该对象具有如下属性：
    #  name:字符的Unicode表示或描述，例如%，space。
    #  scan_code:该按键的扫描码
    #  time:事件发生时的时间戳
    #以下两个函数只有在按键按下或抬起时才会调用回调函数
    keyboard.on_press(callback, suppress=False)
    keyboard.on_release(callback, suppress=False)
    
    keyboard.hook_key(key, callback, suppress=False) #将特定按键key的按下然后抬起当作一个事件来处理。返回创建的event handler。此函数与热键共享状态，因此clearall_hotkeys也会影响它。
    #以下两个函数只hook指定的按键key，当对应的键被按下或释放时，会调用回调函数。
    keyboard.on_press_key(key, callback, suppress=False) 
    keyboard.on_release_key(key, callback, suppress=False)
    
    keyboard.unhook(remove) #卸载一个钩子，remove可以是回调函数名，或者hook函数返回的event handler。
    keyboard.unhook_all() #卸载之前注册的所有键盘钩子，例如热键，缩写，单词监听器，记录record和等待wait。
    
    keyboard.block_key(key) #压制按键key的所有事件，不论是否有修饰键。
    keyboard.remap_key(src, dst) #将src键的事件替换为dst键的事件，不论是否有修饰键。
    ```
