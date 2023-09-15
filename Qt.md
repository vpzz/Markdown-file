# 安装 msvc版本

1. Qt5.12.9 使用msvc2017套件需要注意以下几项：
   1. 这里使用的是vs2022 IDE，不过下载了vs2017的平台工具集。
   2. ![image-20221022000406117](Qt.assets/image-20221022000406117.png)
   3. 按照如下顺序 Kits→Compilers→Add→MSVC→C/C++ 手动添加编译器。
   4. 然后找到vs的配置脚本路径：D:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build。进入Qt Creator配置编译器，需要加上一个选项为-vcvars_ver=14.16。因为vcvarsall.bat默认会使用Microsoft.VCToolsVersion.default.txt文件中的版本。就是14.33，也就是vs2022的平台工具集。
   5. ![image-20221022000739716](Qt.assets/image-20221022000739716.png)
   6. 按照上面的步骤，分别设置C和C++编译器。
   7. 虽然vs2022也会下载对应的sdk，由于vs使用的是C:\Windows\System32\vsjitdebugger.exe调试器，而qt只能使用gdb或cdb。因此需要去https://developer.microsoft.com/en-us/windows/downloads/sdk-archive/下载Windows sdk。点击右侧的sdk，用管理员权限打开，然后选择Debugging Tools for Windows安装即可。
   8. 使用winver命令查看操作系统的内部版本。
   9. ![image-20221112122905525](Qt.assets/image-20221112122905525.png)
   10. 下载对应的winsdksetup.exe文件，打开应该是如下情况。
   11. ![image-20221112122838782](Qt.assets/image-20221112122838782.png)
   12. ![image-20221022001732573](Qt.assets/image-20221022001732573.png)
   13. 实际上也可以修改vs2022安装的那个Windows sdk。
   14. 重启Qt Creator，即可自动识别到cdb。
2. 如果编译时遇到找不到shell32.lib的错误，可以先到C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\um\x64目录下观察一下是否存在该文件。如果不存在的话，用管理员权限打开Visual Studio Installer，修改，勾选上Windows 通用 C 运行时和Windows通用 CRT SDK。然后安装即可。
3. 在安装VS的时候也可以导入一下配置，保存到.config文件中：

   ```json
   {
     "version": "1.0",
     "components": [
       "Microsoft.VisualStudio.Component.CoreEditor",
       "Microsoft.VisualStudio.Workload.CoreEditor",
       "Microsoft.VisualStudio.Component.Roslyn.Compiler",
       "Microsoft.Component.MSBuild",
       "Microsoft.VisualStudio.Component.TextTemplating",
       "Microsoft.VisualStudio.Component.Debugger.JustInTime",
       "Microsoft.VisualStudio.Component.IntelliCode",
       "Microsoft.VisualStudio.Component.VC.CoreIde",
       "Microsoft.VisualStudio.Component.Windows10SDK",
       "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
       "Microsoft.VisualStudio.Component.Graphics.Tools",
       "Microsoft.VisualStudio.Component.VC.DiagnosticTools",
       "Microsoft.VisualStudio.Component.Windows10SDK.19041",
       "Microsoft.VisualStudio.Component.VC.Redist.14.Latest",
       "Microsoft.VisualStudio.ComponentGroup.NativeDesktop.Core",
       "Microsoft.VisualStudio.ComponentGroup.WebToolsExtensions.CMake",
       "Microsoft.VisualStudio.Component.VC.CMake.Project",
       "Microsoft.VisualStudio.Component.VC.ASAN",
       "Microsoft.VisualStudio.Component.VC.v141.x86.x64",
       "Microsoft.Component.VC.Runtime.UCRTSDK",
       "Microsoft.VisualStudio.Workload.NativeDesktop"
     ]
   }
   ```

# jom

1. nmake 可以理解成微软家的make，随着vs安装。
2. jom是qt的定制nmake。jom是nmake的克隆，可支持并行执行多个独立命令。它基本上增加了-j命令行开关，类似于GNU make。原始博客文章仍可以在Qt博客上找到。 https://wiki.qt.io/Jom。一般make可以加一个参数-j 表示使用多少个线程来编译，-j4就表示使用4个线程编译。linux下使用make，而在windows上面使用nmake，是vs提供的一个东西，但是有很个坑的事，就是nmake不支持-j这个参数，也是就是说它是单线程编译，Qt为了解决这样子的一个问题，弄出一个jom.exe，这和make的功能基本是一样的，但是他比nmake多出来的就是，-j这个参数.也就是说它支持多线程编译。

# qmake

1. qmake是qt专用的构建工具，可以根据.pro文件来生成对应的makefile。不过在Qt6开始使用cmake作为构建工具。

# vcvarsall.bat

1. 该文件是接受多个参数，平台，kit版本，msvc平台工具集版本。例如：

   ```
   vcvarsall.bat x64 -vcvars_ver=14.16
   ```
2. 需要注意的是，这个脚本需要在cmd中执行，power shell不行。执行上述命令后，可以运行C/C++编译器cl，观察输出：

   ```
   D:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build>cl
   用于 x64 的 Microsoft (R) C/C++ 优化编译器 19.16.27048 版
   版权所有(C) Microsoft Corporation。保留所有权利。
   
   用法: cl [ 选项... ] 文件名... [ /link 链接选项... ]
   ```
3. 

# 错误

1. QT中如果出现： warning: 'nullptr' is incompatible with C++98等类似警告，可以修改设置→C++→Code Model→Clang Code Model→built-in即可。
1. 如果编译器报错warning: C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失。当文件中出现中文，且用UTF-8编码（不含BOM头）保存时就可能出现问题。可以用notepad++转化成UTF-8 BOM 即可。或者在QtCreator中右键，Add UTF-8 BOM on save，修改一下文件，保存即可。
1. BOM头是用来让文本编辑器识别文件编码的方式，用文件开头的三个不可见的字节（EF BB BF）表示。Unix下的文本文件默认都是uft-8编码，因此默认不含有BOM头。windows下的默认含有。
1. 因为msvc默认使用的是系统编码，即GB18030，QT的源文件默认是以utf-8存储的。更推荐在.pro文件中添加如下内容，这样有没有BOM头都是可以的：

   ```
   msvc{
       QMAKE_CFLAGS += -utf-8
       QMAKE_CXXFLAGS += -utf-8
   }
   ```
1. 使用RC_ICONS = AppIcon.ico设置完程序图标后，需要重新执行qmake才会生效。可以先clean，再build。
1. 如果使用shadow构建，就要检查一下源码目录是否有.ui文件对应的.h文件。如果有的话，会优先include这个，而不是通过.ui文件在构建文件夹中生成的.h文件。
1. ![image-20221119014509132](Qt.assets/image-20221119014509132.png)

# 编码

1. 下面第一行为手动编写的，即使文件的编码为utf-8也会出现乱码。其中\351是八进制，三个字节表示一个汉字。

   ```c++
   btnClose=new QPushButton(tr("退出"));
   btnClose->setText(QApplication::translate("Dialog", "\351\200\200\345\207\272", Q_NULLPTR)); //.ui文件生成的
   //        \351\200\200\345\207\272
   //         e9  80  80  e5  87  ba  
   ```

2. 在Qt中，使用QString输出中文，有两种方法：

   1. utf-8编码的源文件

      ```c++
      //使用如下形式来创建中文的QString。推荐使用第三种，最简单。当直接书写非ASCII字符时，需要保证编码为utf-8。
      QString::fromUtf8("中文")
      QString::fromUtf8("\xE4\xB8\xAD\xE6\x96\x87") //中文两个字符的utf-8编码就是E4B8ADE69687.
      QString("中文")
      QString("\xE4\xB8\xAD\xE6\x96\x87")//这个构造函数使用上面的函数来创建，第二种方式对于utf-8或者ANSI编码的文件都适用，但第一种方式更直观。
      
      //可以在.pro文件中添加如下设置，使msvc编译器将源码当做utf-8编码，这只是为了让msvc编译器不报警告。不过有的时候是警告，有的时候是错误。因此建议都加上。
      msvc{
          QMAKE_CFLAGS += -utf-8
          QMAKE_CXXFLAGS += -utf-8
      }
      ```

   2. ANSI编码的源文件

      ```c++
      QString::fromLocal8Bit("中文");  //这种比较方便。这里的local指的是系统的默认编码，Windows下是ANSI。
      QString::fromLocal8Bit("\xD6\xD0\xCE\xC4");//不太方便，中文这两个字符的GB18030编码就是D6D0CEC4。这种方式对于utf-8编码的源文件也适用。
      //此时应该取消上一小节中msvc编译器的utf-8设置，否则会报大量的警告
      ```

3. 例子：

   ```c++
   "\345\256\213\344\275\223" //在C++语言看来，这个就是一个字符串字面常量，有6个字符，占7个字节（包括末尾的\0）。
   QString::fromUtf8("\345\256\213\344\275\223");  //8进制，6个字节。被解析为Utf-8编码。\345=0xE5，在三字节的范围内，因为后面两个字节会和第一个字节联合起来构成一个Unicode字符的utf-8编码。即0xE5AE8B。
   //第二个字符的第一个字节为E4，也是3字节，因此第二个字符的utf-8编码为0xE4BD93
   ```

4. 在https://www.qqxiuzi.cn/bianma/utf-8.htm用字节流解码"E5AE8BE4BD93"，得到"宋体"

5. 使用QTextCodec来将其他编码的字符串转化为QString。

   ```c++
   QTextCodec* codec = QTextCodec::codecForName("GB18030");  //创建一个中文的编解码器。
   QString s1 = codec->toUnicode("\xC2\xD2\xC2\xEB");  //将参数字符串转化为Unicode编码。
   ```

6. 同一个字符可以有两种方式：

   ```c++
   strcmp("乱码","\xE4\xB9\xB1\xE7\xA0\x81")  //当源码是utf-8编码时，结果为0，即两个字符串完全相同。前者每个汉字占用3个字节，一共占用6个字节，后者一共有6*4=24个字节。
   //当源码不是utf-8，但是是其他兼容ASCII的编码时，第一个参数的字节表示就不一样了，而第二个还是一样的。
   ```

7. QtDesigner生成的.h文件，对中文都是使用第二中表示方式，不过是8进制。如果msvc编译器没有开启utf-8编译选项时，会默认将源码当做系统编码，即GB18030，这样"乱码"两个汉字就会被解析错误，而"\xE4\xB9\xB1\xE7\xA0\x81"并不会被解析错误。不过还是推荐使用直接书写中文的方式，这样修改更容易。

   ```c++
   QString::fromUtf8("乱码")
   QString::fromUtf8("\xE4\xB9\xB1\xE7\xA0\x81")
   ```

8. 可以在main函数中使用如下代码来修改执行字符集，也就是可以将程序中的默认编码方案从gb18030改为utf-8。

   ```c++
   QTextCodec *codec = QTextCodec::codecForName("UTF-8"); //不区分大小写
   QTextCodec::setCodecForLocale(codec);
   //此时  QString::fromLocal8Bit()  等价于  QString::fromUtf8()
   ```

9. Qt5中QString内部采用Unicode字符集，utf-16编码。构造函数QString::QString(const char *str)默认使用fromUtf8()，将str所指的执行字符集从utf-8转码成utf-16。

10. 如果确认文件是utf-8编码，也是正确使用了QString那么应该打开每个文件，取消BOM头，然后在.pro文件中添加utf-8的编译器选项。


# 大小

1. 设定程序窗口为固定大小：

   ```c++
   setFixedSize(this->geometry().size());  //在窗口类的ui->setupUi(this)之后。
   ```

2. 

3. 


# Qt Creator 格式化

1. 推荐使用Artistic style来格式化。

   1. 首先勾选Help→About Plugins→C++→Beautiful，以开启格式化功能。

   2. 然后下载Artistic style软件，在tool→option→Beautifier→General中选中Artistic style。

   3. 勾选Enable auto format on file save。保存时自动格式化。在Artistic style标签页中指定可执行程序的地址。然后在最下面勾选Use Customized style，右边add，name随便，在value中粘贴下面的内容即可。


   ```
   --style=stroustrup  #GNU 风格格式和缩进
   --indent=spaces=4  # 缩进4个空格
   --indent-preproc-block  # 条件编译预处理缩进
   --indent-preproc-define   # -w  设置宏定义模块缩进
   --indent-namespaces       # -N  设置 namespace 整体缩进
   #--indent-col1-comments   # 注释也缩进
   --pad-oper  #操作符两端插入一个空格
   --pad-header
   --unpad-paren  # 刪除括号外多余的空格
   --max-continuation-indent=80 #最大行长度80
   --indent-col1-comments  # 注释和代码一起缩进
   --suffix=none
   --align-pointer=name  # 指针符号等附在变量上 如 char *foo1;
   --lineend=linux  # 以linux话的格式显示
   --indent=tab=4  # TAB 转4个空格
   --convert-tabs  #TAB转换为空格
   --indent-switches  #switch case 缩进-S
   #--indent-cases 	    # -K  设置 cases 整体缩进
   --break-one-line-headers  #if 语句一行分两行写
   --add-braces  # 在'if', 'for', 'while'等句块中只有一行也加入大括号
   --attach-return-type-decl # 函数返回类型和函数名搞成一行
   --unpad-paren #移除括号两端多余空格
   --delete-empty-lines      # -xe 删除多余空行
   --break-blocks            # if while等前增加一空行
   --verbose
   ```

2. 

3. 

4. 

5. 