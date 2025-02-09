# 基础

1. TEX是斯坦福大学的Knuth（高德纳）教授开发的，是一个电子排版系统，非常适用于生成高印刷质量的科技类和数学类文档。

2. 1977年，正在编写《计算机程序设计艺术》的高德纳意识到每况愈下的排版质量将影响其著作的发行，为扭转这种状况，他着手开发TEX。

3. TEX的哲学是使版面样式设置和文档的具体内容尽可能分离，让写文档的人更加专注于文档的撰写，而少花些心思在排版上。TeX排版的结果是DVI(Device Independent)，文件与输出设备无关。可以打印，显示，照排等，可以输出到任何设备上。

4. 现在使用TeX引擎发布于1982年，1989年稍加改进。TeX的版本号不断逼近π，当前为3.141592653。TeX的拼写来自希腊语τεχνική (technique，技术)的开头的几个字母。

5. 由于TEX是很低阶的排版语言，所以基于其开发的宏集（集成了大量二次开发的命令，更方便使用）有很多，LaTeX就是其中之一，由Leslie Lamport编写的，LaTex就是“Lamport TEX”的简称。还有比较著名的AMSTeX，美国数学学会推荐数学家使用的。

6. LaTeX是一种使用TEX程序作为排版引擎的格式（format），可以粗略地将它理解成是对TEX 的一层封装。当前的版本为LaTeX2e，意思是超出了第2版，接近但还远没有到第3版。e是希腊字母ε的意思，也就是无穷小量。

7. 和Word相比，TEX排版系统的缺点：不如所见即所得软件显而易见，需要不断地编译查看，且其使用的宏语言比一般的编程语言更难排错，且无法调试。word是所见即所得，LaTeX是所想即所得。二者的设计目标不一致，也各自有自己的适用范围。

8. TEX的发行版一般包含编译引擎，宏包，文档。常见的发行版与TEXLive、CTEX、MiKTEX、MacTEX。

   1. TEXLive每年发行一版，当发布新版本后，旧版本就会被冻结，update只能更新到当前版本的最新。它是跨平台的。推荐使用这个。
   2. MacTEX 是macOS（OS X）系统下的一个定制化的TEX Live 版本，与TEX Live 同步更新。
   3. CTEX是中科院吴凌云基于MiKTEX的基础上开发的，2012年之后疏于维护，长久不更新。CTEX是利用TEX排版系统的CTEX中文套装的简称。它集成了编辑器 、WinEdt和 PostScript处理软件 Ghostscript 和 GSview 等主要工具。 CTeX中文套装在 MiKTeX的基础上增加了对中文的完整支持。CTeX中文套装支持 CCT 和 CJK 两种中文 TeX处理方式。 
   4. 以上2者都集成了一个简单的LaTeX 源代码编辑器TeXworks。不过不推荐安装，推荐单独安装TexStudio。

9. Linux 发行版的软件源也提供TEX Live 的安装，不过不够完整，更新也不是很及时。建议直接从镜像安装。

10. 两种发行版都提供了用来安装，删除，更新宏包的工具。TEX Live 默认安装所有宏包，而MiKTEX 的安装程序只包含了LaTeX的一些基本宏包。除非万不得已，尽量不要手动安装宏包，应该使用发行版带的工具安装。

11. 由于历史原因，LaTeX是学术圈子里面写论文的事实标准（国内除外）。八十年代末，Tex就已经发布出来了，而MS Office在1990年才发布第一版。在Office还没有机会渗透到学术圈子里面之前，LaTeX已经大面积应用上了。

12. 命令以\开头，对大小写敏感，有一下两种形式：

    1. \后面跟一串字母，例如`\LaTeX`，以任意非字母符号（空格、数字、标点）作为分隔符。
    2. \后面是单个非字母符号，例如`\[`，其后无需分隔符。

13. 一般来说，命令后紧接着的空格都会被忽略，如果要体现出空格，可以使用以下方法：

    ```latex
    中文\heiti 字体     %并不会出现空格
    
    中文\songti{} 字体 %使用{}来显示终结命令
    
    中文\fangsong~字体 %使用~
    
    中文\heiti\ 字体  %使用\对空格转义
    ```

14. <img src="LaTeX.assets/image-20240105011944208.png" alt="image-20240105011944208" />

15. 一些命令可以接收参数，参数会影响命令的效果，必选参数用`{}`包含，可选参数用`[]`包含，还有一些命令可以带一个\*，带\*和不带\*的命令不一样，可以将其当作一个可选参数。

16. 以单个字符作为命令的参数时，可以不加括号。例如，在数学环境下，\frac12和\frac{1}{2}的效果是一样的。

17. LaTeX中还包含环境，引入环境的目的是使某些效果在局部生效，或者生成特殊的文档元素。部分环境允许嵌套使用：

    ```latex
    \begin{⟨environment name⟩}[⟨optional arguments⟩]{⟨mandatory arguments⟩}
    
    \end{⟨environment name⟩} %begin和end中填写的环境名必须一致，环境也可以有可选和必选参数
    ```

18. 有些命令会对其后的所有内容产生作用，可以使用分组（一对大括号`{}`）来限制其适用范围，在分组中使用的命令被限制在分组内，不会影响到分组外的内容。环境也是一个隐含的分组，在环境中的命令被包裹在分组内。不过个别命令在分组内仍然会产生全局作用，例如\setcounter等命令。

    ```latex
    {
    \bfseries
    }
    ```

19. 一个LaTeX文档包含导言区（进行全局设置）和正文区（有且只有一个document环境）。

20. 在`\documentclass`和`\begin{document}`之间的区域称为导言区，除了使用`\usepackage`调用宏包之外，一些对文档的全局设置命令也在这里使用。当然也可以什么都不写，一个宏包都不调用。一切视自己需求。

    ```latex
    \documentclass{...} % ... 为某文档类
    % 导言区
    \begin{document}
    % 正文内容
    \end{document}
    % 此后内容会被忽略
    ```

21. 排版引擎：读入源代码并编译生成文档的程序，如pdfTeX,XeTeX，也称为编译器。

22. 格式：定义了一组命令的代码集，LaTeX就是一个应用最广泛的格式。规定了如何识别LaTeX源码中的标记。高德纳本人还编写了一个简单的plain TEX格式，没有定义诸如\documentclass 和\section等等命令。

23. 命令：实际调用的，结合了引擎和格式的命令，如`pdfLaTeX`就是将pdfTeX引擎和LaTeX格式结合起来。

    ```shell
    D:\texlive\2023\bin\windows>LaTeX.exe
    This is pdfTeX, Version 3.141592653-2.6-1.40.25 (TeX Live 2023) (preloaded format=LaTeX)
     restricted \write18 enabled.
    ```

24. 一般来说LaTeX代表格式，latex代表命令，命令都是全小写的。可见pdflatex和xelatex都是使用LaTeX的格式，只不过是引擎（编译器）不同。

    ```
               文档格式   plain TEX格式    LaTeX格式
    TEX引擎      DVI         tex           N/A
    pdfTEX引擎   DVI        etex          latex
                 PDF       pdftex       pdflatex
    XETEX引擎    PDF        xetex        xelatex
    ```

25. 常用命令：

    ```shell
    LaTeX helloworld.tex      #编译，生成helloworld.dvi文件。
    dvipdfmx helloworld.dvi   #将dvi文件转化为pdf文件。
    pdfLaTeX helloworld.tex   #可以直接生成pdf。
    xeLaTeX heloworld.tex     #可以直接生成pdf。
    ```

26. xelatex支持UTF-8编码和对TrueType/OpenType字体的调用。当前较为方便的中文排版解决方案基于xelatex。

27. 文档类（documentclass）规定了要生成的文档的性质，源代码（.tex文件）必须以`\documentclass[⟨options⟩]{⟨class-name⟩}`开头指定文档类，类似于word的模板。LaTeX提供的基础文档类，前三个称为标准文档类：

    ```
    article 文章格式的文档类，广泛用于科技论文，报告，说明文档
    report  长篇报告格式的文档，具有章节结构，用于综述，长篇论文，简单的书籍等
    book    书籍文档类，包含章节结构，前言，正文，后记等结构
    -------------------------
    proc    基于article的一个简单学术文档模板
    slides  幻灯片格式，使用无衬线字体
    minimal 一个极其精简的文档类，只设定了纸张大小和基本字号，用于代码测试的最小工作实例
    ```

28. `\documentclass`命令的可选参数会全局地影响文档的布局，类似于word的页面设置。

    ```latex
    \documentclass[11pt,twoside,a4paper]{article}  %指定纸张为A4大小，基本字号为11pt，双面排版。
    %三个标准文档类可指定的选项包括：
    10pt, 11pt, 12pt %指定文档的基本字号。默认为10pt。LaTeX会根据这个选择对应的标题，上下标的字号。
    a4paper, letterpaper, … %指定纸张大小。默认为美式信纸letterpaper（8.5inch×11inch，大约相当于21.6cm×28.0cm）。可指定选项还包括a5paper，b5paper，executivepaper 和legalpaper。
    twoside, oneside %指定单面/双面排版。双面排版时，奇偶页的页眉页脚、页边距不同。article和report默认为oneside，book默认为twoside。
    onecolumn, twocolumn %指定单栏/双栏排版。默认为onecolumn。
    openright, openany %指定新的一章\chapter是在奇数页（右侧）开始，还是直接紧跟着上一页开始。report默认为openany，book默认为openright。该选项对article无效。
    landscape %指定横向排版。默认为纵向。
    titlepage, notitlepage %指定命令\maketitle是否生成单独的标题页。article默认为notitlepage，report和book默认为titlepage。
    fleqn %令行间公式左对齐。默认为居中对齐。
    leqno %将公式编号放在左边。默认为右边。
    draft, final %指定草稿或终稿模式。草稿模式下，断行不良（溢出）的地方会在行尾添加一个黑色方块；插图、超链接等功能也会受这一组选项影响，将图片显示为方框，加快编译速度。默认为final。
    ```

29. LaTeX依赖一些扩展来增强或补充其功能，例如排版复杂的表格、插入图片、增加颜色甚至超链接等高级功能，这些扩展称为宏包 。使用方法类似于调用文档类，`\usepackage[⟨options⟩]{⟨package-name⟩}`。

30. `\usepackage{A,B,C}`，可以一次性载入多个宏包。使用前要确认是否安装该宏包。使用多个宏包时指定选项，相当于给每个宏包指定同样的选项，如果有某个宏包不能识别指定的选项，则会出错。

31. 宏包（包括前面所说的文档类）可能定义了许多命令和环境，或者修改了LaTeX已有的命令和环境。使用texdoc命令查询相关的信息。

32. LaTeX常用文件格式：

    ```latex
    .sty  %宏包文件
    .cls  %文档类文件
    .bib  %BiBTeX参考文献数据库文件，按条存储参考文献数据
    .bst  %BiBTeX参考文献格式模板
    %辅助文件如下
    .log  %排版引擎生成的日志文件，供排查错误使用。
    .aux  %LaTeX 生成的主辅助文件，记录交叉引用、目录、参考文献的引用等。
    .toc  %LaTeX 生成的目录记录文件。
    .lof  %LaTeX 生成的图片目录记录文件。
    .lot  %LaTeX 生成的表格目录记录文件。
    .bbl  %BIBTEX 生成的参考文献记录文件。
    .blg  %BIBTEX 生成的日志文件。
    .idx  %LaTeX 生成的供makeindex处理的索引记录文件。
    .ind  %makeindex 处理.idx生成的用于排版的格式化索引文件。
    .ilg  %makeindex 生成的日志文件。
    .out  %hyperref 宏包生成的PDF书签记录文件。
    ```

33. LaTeX的辅助功能，如交叉引用，参考文献，目录等需要先编译生成辅助文件，再次编译时才会读入辅助文件。所以复杂的源代码可能需要编译多次，一般以不再出现warning为止，之所以设计成这样，是因为当时的电脑内存容量有限。

34. 多文档编译，一般用于编写书籍或毕业论文，将内容分章节组织成多个tex文件，会大大简化修改和校对
    的工作。两种方法：

    1. 可以使用命令`\include{⟨filename⟩}`在源代码里插入文件（文件名不能带.tex扩展，2020-10-1的LaTeX版本后允许带后缀名）。
    2. 可以在导言区使用`\includeonly{文档列表}`，这样生成PDF时会只会载入文档列表中的文件，正文中不在该范围的`\include`命令不会起效，一般用于调试，最终生成时应注释掉这句话。
    3. \include命令会在插入前另起一页。有的时候我们并不需要这样，而是使用`\input{b.tex}`进行原样插入，它纯粹是把文件里的内容插入。

35. 当导言区内容较多时，常常将其单独放置在一个.tex 文件中，再用\input 命令插入。复杂的图、表、代码等也会用类似的手段处理。

36. 2020版本之前的LaTeX，对于include和input的文件名最好不要有空格或特殊字符，尽量壁面使用中文，现在只要是操作系统允许的，都可以作为文件名。

37. syntonly宏包是用来排查错误的，使用这个宏包和在导言区加入\syntaxonly命令后，编译不产生pdf，dvi文档。排错方便，速度提升。如果想生成文档则使用%注释掉该行命令即可。

    ```latex
    \usepackage{syntonly}
    \syntaxonly
    ```

38. ISO的纸张：A系列常用于公文；B系列常用于海报和护照(B7, 88mm x 125mm)；C系列常用于信封，因为它恰好比A系列大一点，比如A4纸可以装在C4信封里，对折一下就可以装进C5信封，再对折一次装进C6信封。



# 中文支持

1. 最早的TeX只支持7-bit的ASCII编码，如Möbius必须通过输入`M\"obius`得到。3.0版本后支持8-bit，能够处理0x80-0xFF之间的字符，使用latex或pdflatex命令时，对源代码的编码处理由inputenc宏包支持。比如将源代码保存为Latin-1编码，并在导言区调用inputenc宏包并指定latin1选项后，Möbius这样的词语就可以直接通过（用适当输入法）输入`Möbius`得到了。

2. 将使用拉丁字母的文档保存为UTF-8编码后，可以用pdflatex直接编译，但是非拉丁字母仍然无法直接在LaTeX中使用。

3. 用LaTeX 排版中文需要解决两方面问题：对中文字体的支持，对中文排版中的一些细节的处理，例如汉字之间控制断行、标点符号的禁则（如句号、逗号不允许出现在行首）、中英文之间插入间距等。

4. xeCJK 及luatexja宏包封装了对汉字排版细节的处理功能。ctex宏包和文档类进一步封装了CJK、xeCJK、luatexja等宏包，使得用户在排版中文时不用再考虑排版引擎等细节。

5. ctex 宏包本身用于配合各种文档类排版中文，而ctex 文档类对LaTeX 的标准文档类进行了封装，对一些排版根据中文排版习惯做了调整，包括ctexart、ctexrep、ctexbook等。ctex 宏包和文档类能够识别操作系统和TEX 发行版中安装的中文字体，因此基本无需额外配置即可排版中文文档。

6. xelatex和lualatex命令配合ctex宏包/文档类的方式成为当前的主流中文排版支持方式，旧方式（CCT、CJK等）日渐退出舞台。

7. 虽然ctex宏包和文档类保留了对GBK编码以及latex和pdflatex编译命令的兼容，但是不推荐使用。

8. ctex还用来指代一个TEX的过时的发行版，注意区分。xelatex又称为“邪恶LaTeX”。

9. 在LaTeX的2018-04-01版本之前，需要调用inputenc宏包并指定utf8选项才能使用UTF-8编码，现在默认就是UTF-8编码。

10. 使用XeLaTeX编译时，强制开启UTF8选项，而使用pdfLaTeX或LaTeX编译时，为ANSI编码。

11. ctex的两种使用方法：

    1. XeLaTeX编译+使用ctex宏包   CJK环境仅仅是支持了中文的输入，这个ctex则是将营造了中文的环境，例如二者对日期的支持不同，CJK输出英文，ctex输出中文。
    2. XeLaTeX编译+使用ctexart文档类，之后不用再声明使用ctex宏包。
    3. 上述两种方法不完全一样，例如对于\section的内容，ctex宏包会左对齐， ctexart文档类会居中。使用\ctexset{ }命令来设置全局的样式。这些都可以在导言区通过\ctexset命令来进行修改。

12. 使用%来产生注释，其后一直到行尾的字符都会被注释，行末的换行符也不会产生空格。对于大段文字的注释，百分号就显得比较繁琐。这时我们可以使用verbatim 宏包的comment环境。

13. 以下字符需要转义才可以正常输入：

    ```latex
    # $ % & { } _ ^ ~ \
    %其中\^和\~需要{}，因为他们也可以为字符添加重音。当{}内为空时，就直接输入该字符
    \# \$ \% \& \{ \} \_
    \^{} \~{} \textbackslash
    %不能使用\\来输出\，因为它被直接定义成了手动换行的命令，没有使用\n，应该是因为TeX的源码使用Pascal编写的
    ```

14. 西文排版中经常会出现连字（ligatures），常见的有`ff   fi   fl   ffi   ffl`。可以在连字中间加入{}来取消。

15. <img src="LaTeX.assets/fb89aba2-499c-4b04-ab86-6c028d545381.png" alt="img" style="zoom:33%;" />

16. 点号分为两类，①句内点号：顿号、逗号、分号、冒号②句末点号：句号、问号、叹号。这些点号主要表示语言中种种停顿。标号包括破折号、括号、省略号、书名号、引号、连接号、间隔号、着重号、专名号等，主要标明词语或句子的性质和作用。需要注意的是，问号和叹号也兼属标号：就其表示句末停顿而言，是点号；就其表示句子语气而言，是标号。

17. 从键盘上一共可以输入6种引号，分别是英文输入法下的单双引号，和中文输入法下的左右单双引号。中文的引号是分左右的，不过都是通过一个键来输入，输入法会自动选择左右引号。

    ```latex
    '   "
    %上面两个是英文输入法下的单双引号，编码分别为0x27和0x22，为半角的
    ‘   ’
    %上面两个是中文输入法下的单双引号，编码分别为0xE28098和0xE28099，为全角的
    “   ”
    %上面两个是中文输入法下的单双引号，编码分别为0xE2809C和0xE2809D，为全角的
    ```

18. 在使用ctex宏包或文档类的情况下，中文引号可以通过输入法直接输入。

19. 示例，下面的所有引号从pdf中复制出去，结果都是中文的引号，都不是ASCII字符。：

    ```latex
    A'and"B
    
    A''and"B  %两个单引号可以等价于一个双引号，两者编译后都只会生成同一个符号
    
    A`and'B   %`和'构成左右单引号
    
    A‘and’B   %这行在没有开启ctex时，和上一行一样，如果开启了ctex后，则和上面显示不同，从pdf中观察可以发现，这是因为这里的引号使用的字体是中文字体，因此比较宽，将其修改为英文字体后，结果和上面一样。
    
    A``and''B %``和''构成左右双引号
    
    A“and”B   %同上2行的结果
    ```

20. <img src="LaTeX.assets/image-20240105125946526-1704516157720-1-1704516183761-59.png" alt="image-20240105125946526" />

21. 有三种长度的“横线”可用：

    1. 连字号（hyphen），用来组成复合词。

    2. 短破折号（en-dash），用来连接数字表示范围。中文排版中一般使用`$\sim$`来连接数字表示范围。不能直接使用`~`，因为他表示一个空格。

    3. 长破折号（em-dash），用来连接单词，语义上类似中文的破折号。

    4. ```latex
       daughter-in-law, X-rated
       
       pages 13--67 页码80$\sim$88
       
       yes---or no?
       ```

    5. <img src="LaTeX.assets/image-20240105131444483-1704516157720-2-1704516183762-61.png" alt="image-20240105131444483" />

22. TeX中几个短划线是相连的，XeTeX中它们之间是有空隙的。可以用Mapping参数指示改回TeX的方式，即去掉短划线之间的空隙。

    ```latex
    \usepackage{fontspec}
    \setmainfont[Mapping=tex-text]{Times New Roman}
    \setsansfont[Mapping=tex-text]{Tahoma}
    \setmonofont{Courier New}
    ```

23. 可以使用\ldots命令表示省略号，相对于直接输入三个点的方式更为合理，因为前者会被编译成一个字符，后者是三个。\dots与\ldots命令等效。

    ```latex
    one, two, three, \ldots{} one hundred.%加入{}的目的是为了使得和one之间的空格生效
    
    abc...def\ldots
    ```

24. <img src="LaTeX.assets/image-20240105132141058-1704516157720-3-1704516183762-60.png" alt="image-20240105132141058" />

25. 支持用命令输入西欧语言中使用的各种拉丁文扩展字符，主要为带重音的字母，注意和数学符号的重音区分开：

    ```latex
    H\^otel, na\"\i ve, \'el\`eve,%\^o等价于\^{o}
    
    sm\o rrebr\o d, !`Se\ norita!,
    
    Sch\"onbrunner Schlo\ss
    
    Stra\ss e
    ```

26. <img src="LaTeX.assets/image-20240105132743531-1704516157721-4-1704516183762-62.png" alt="image-20240105132743531" />

27. 预定义的其它一些文本模式的符号，更多的符号多由特定的宏包支持：

    ```latex
    \P{} \S{} \dag{} \ddag{}
    
    \copyright{} \pounds{}
    
    \textasteriskcentered A*%注意区分，高度不同
    
    \textperiodcentered A.
    
    \textbullet A·
    
    \textregistered{} \texttrademark
    ```

28. <img src="LaTeX.assets/image-20240105133200094-1704516157721-5-1704516183762-63.png" alt="image-20240105133200094" />

29. 错落有致的LaTeX标志：

    ```latex
    \TeX
    
    \LaTeX
    
    \LaTeXe
    ```

30. <img src="LaTeX.assets/image-20240105133348061-1704516157721-6-1704516183762-64.png" alt="image-20240105133348061" />

31. 在西文排版实践中，断行的位置优先选取在两个单词之间，也就是在源代码中输入的“空格”。“空格”本身通常生成一个间距，它会根据行宽和上下文自动调整，文字密一些的地方单词间距就略窄，反之略宽。当文字在单词间的“空格”处断行时，“空格”生成的间距随之舍去。可以使用`~`来生成一个不会断行的空格，一般用在英文人名，图标名称等情况，因为不希望他们出现在两行上，此时引擎会寻找其他可以断行的位置。

    ```latex
    Fig.~2a
    
    Donald~E. Knuth
    ```

32. 一般来说不需要手动进行断行或断页，只需要进行分段即可。

    ```latex
    \\[<length>]  %参数length用于在断行处向下增加垂直间距。\\也在表格，公式等地方用于换行。它只是换行，并不会产生新的段落，所以并不会缩进。
    \\*[<length>] %比\\多了个功能，禁止在断行处分页
    \newline      %只用于文本段落中
    ```

33. 源码行尾的换行符被视为1个空格；源码中连续2个换行符，才被编译为1个换行符，会将文字分段。

34. 空格键和Tab键输入的空白字符视为“空格”。连续的若干个空白字符视为一个空格。源码中一行开头的空格会被忽略。

35. 通常为了保持源文件的清晰，通过插入空行或使用`\par`命令来实现分段，类似于word的回车。多个空行视为一个。

36. 换行（`\\`强制断行）≠分段（空一行或`\par`）

37. 手动断页的命令有2个：

    ```latex
    \newpage
    \clearpage
    %在双栏排版模式中\newpage起到另起一栏的作用，\clearpage则能够另起一页。
    %二者在涉及浮动体的排版上行为不同。
    ```

38. 有时候我们不满足于默认的断行和断页位置，需要进行微调，可以用以下命令告诉引擎哪些地方适合断行或断页，哪些地方不适合：

    ```latex
    \linebreak[⟨n⟩] \nolinebreak[⟨n⟩]
    \pagebreak[⟨n⟩] \nopagebreak[⟨n⟩]
    %以上命令都带一个可选的参数n，表示是适合或不适合的程度，取值范围为0-4，默认为4.
    %\linebreak[4]表示此处需要强行断行
    %\nolinebreak[4]表示禁止在此处断行
    ```

39. 不过不推荐使用break系列命令，更推荐使用new系列命令，因为使用这些命令强行断行/断页可能会制造出糟糕的排版效果，并导致引擎报Underfull \hbox 等警告：

    ```latex
    使用\verb|\newline| 断行的效果
    \newline
    与使用\verb|\linebreak| 断行的效果
    \linebreak
    进行对比。
    ```

40. <img src="LaTeX.assets/image-20240105135106405-1704516157721-7-1704516183762-65.png" alt="image-20240105135106405" />

41. 当遇到非常长的单词时，仅在单词之间断行无法形成宽度均匀的行时，会进行断字。手动断字使用\-

42. 当遇到了很长的英文单词时，如果仅靠在单词之间的“空格”处断行无法生成疏密程度匀称的段落时，就会考虑从单词中间断开。对于绝大多数单词，引擎能够找到合适的断词位置，在断开的行尾加上连字符-。如果一些单词没能自动断词，我们可以在单词内手动使用`\-`命令指定断词的位置：

    ```latex
    I think this is I think this is I think this is I think this is: su\-per\-cal\-i\-frag\-i\-lis\-tic\-ex\-pi\-al\-i\-do\-cious.
    ```

43. <img src="LaTeX.assets/image-20240105135556029-1704516157721-8-1704516183762-66.png" alt="image-20240105135556029" />

# 文档元素

1. 一个结构化的文档所依赖的各种元素有：章节、目录、列表、图表、交叉引用、脚注等。

2. 标准文档类或继承自该类的文档类都有以下命令，这些命令生成章节标题，并能够自动编号，还向目录中添加条目，并影响页眉页脚的内容：

   ```latex
   \chapter{第一章}           %章标题，只在report和book文档类有定义
   \section{第一节}           %节标题，对于article，最高的就是section了
   \subsection{第一小节}      %小节标题
   \subsubsection{第一小小节} %小小节标题
   ```

3. <img src="LaTeX.assets/image-20240105140723605-1704516157721-9-1704516183762-67.png" alt="image-20240105140723605" />

4. 每个命令有两种变体：

   ```latex
   \section[⟨short title⟩]{⟨title⟩} %带可选参数，标题使用⟨title⟩参数，在目录和页眉页脚中使用⟨short title⟩参数；
   \section*{⟨title⟩} %带星号，此时标题不带编号，也不生成目录项和页眉页脚。
   ```

5. `\paragraph{}`和`\subparagraph{}`是章节标题命令，不是分段。它是在`\subsubsection{}`在下一层，即使不用带星号的变体，生成的标题默认也不带编号。

6. article 文档类带编号的层级为\section、\subsection、\subsubsection三级。

7. report 和book 文档类带编号的层级为\chapter、\section、\subsection三级。

8. 除此之外LaTeX 还提供了\part 命令，用来将整个文档分割为大的分块，但不影响\chapter或\section等的编号。应该类似于word的分节。

9. LaTeX及标准文档类并未提供为\section等章节命令定制格式的功能，这一功能由titlesec宏包提供。

10. 生成目录的方法，只需在合适的地方使用命令：`\tableofcontents`。这个命令会生成单独的一个chapter（report/book）或一个section（article），不过该章节默认不写入目录。标题默认为“Contents”，可以使用`\contentsname`定制标题。若使用ctex包，标题为“目录”。

11. 有时我们使用了`\chapter*`或`\section*`这样不生成目录项的章节标题命令，而又想手动生成该章节的目录项，可以在标题命令后面使用：

    ```latex
    \addcontentsline{toc}{⟨level⟩}{⟨title⟩} %其中⟨level⟩为章节层次chapter或section等，⟨title⟩为出现于目录项的章节标题。
    ```

12. 自定义目录样式  使用tocloft宏包，进行简单修改，复杂修改使用titletoc宏包。

13. 使用tocbibind宏包来为目录项中增加参考文献，目录项本身，索引，图列表，表列表等项目，默认全部增加。可以指定可选参数，不添加某一项。

14. 为了正确生成目录项，一般需要编译两次源代码，有时可能要编译3次。

15. 所有标准文档类都提供了一个\appendix命令将正文和附录分开2，使用\appendix后，最高一级章节改为使用拉丁字母编号，从A开始。

16. book文档类还提供了前言、正文、后记结构的划分命令：

    ```latex
    \frontmatter %前言部分，页码使用小写罗马数字；其后的\chapter不编号。直到遇到\mainmatter都是前言部分。
    \mainmatter  %正文部分，页码使用阿拉伯数字，从1开始计数；其后的章节编号正常。
    \backmatter  %后记部分，页码格式不变，继续正常计数；其后的\chapter不编号。
    %以上三个命令还可和\appendix命令结合，生成有前言、正文、附录、后记四部分的文档。
    ```

17. 摘要环境abstract默认只在标准文档类中的article和report文档类可用。一般紧跟在\maketitle之后。

18. LaTeX支持生成简单的标题页。首先需要给定标题和作者等信息：`\title{⟨title⟩} \author{⟨author⟩} \date{⟨date⟩}`，其中前两个命令是必须的（不用\title会报错；不用\author会警告），\date命令可选。给定信息的指令可以放在导言区或正文区，但是\maketitle必须放在正文区。且其之前会分页。

19. LaTeX还提供了一个\today命令自动生成当前日期，\date默认使用\today。在\title、\author等命令内可以使用\thanks命令生成标题页的脚注，用\and隔开多个人名。

20. 在信息给定后，就可以使用\maketitle 命令生成一个简单的标题页了。

21. article文档类的标题默认不单独成页，而report和book默认单独成页。

22. LaTeX 标准类还提供了一个简单的titlepage环境，生成不带页眉页脚的一页。用户可以在这个环境中使用各种排版元素自由发挥，生成自定义的标题页以替代\maketitle命令。甚至可以利用titlepage环境重新定义\maketitle：

    ```latex
    \renewcommand{\maketitle}{\begin{titlepage}
    ... % 用户自定义命令
    \end{titlepage}}
    ```

23. 实际上为标准文档类指定了titlepage选项以后，使用\maketitle命令生成的标题页就是一个titlepage环境。

24. 使用titlepage参数的标题是垂直居中的，而在maketitle之后使用\newpage，并不是居中的，而是在较靠上的地方。

25. 一个ctexbook文档类的示例：

    ```latex
    \documentclass{ctexbook}
    % 导言区，加载宏包和各项设置，包括参考文献、索引等
    \usepackage{makeidx} % 调用makeidx 宏包，用来处理索引
    \makeindex % 开启索引的收集
    \bibliographystyle{plain} % 指定参考文献样式为plain
    \begin{document}
    	\frontmatter % 前言部分
    	\title{Test title}
    	\author{ Mary\thanks{E-mail:*****@***.com}\and Ted\thanks{Corresponding author}\and Louis}
    	\date{\today}
    	\maketitle % 标题页
    	\include{preface} % 前言章节preface.tex
    	\tableofcontents
    	\mainmatter % 正文部分
    	\include{chapter1} % 第一章chapter1.tex
    	\include{chapter2} % 第二章chapter2.tex
    	...
    	\appendix % 附录
    	\include{appendixA} % 附录A appendixA.tex
    	...
    	\backmatter % 后记部分
    	\include{epilogue} % 后记epilogue.tex
    	\bibliography{books} % 利用BibTeX 工具从数据库文件books.bib 生成参考文献
    	\printindex % 利用makeindex 工具生成索引
    \end{document}
    ```


## 交叉引用

1. 在能够被交叉引用的地方，如章节、公式、图表、定理等位置使用\label命令做标记。之后可以在别处使用\ref或\pageref命令，分别生成该标记的编号和页码：

   ```latex
   \chapter{测试}\label{sec:this}
   A reference to this subsection looks like:
   ``see section~\ref{sec:this} on page~\pageref{sec:this}.''
   ```

2. <img src="LaTeX.assets/image-20240105163454711-1704516157721-10-1704516183762-68.png" alt="image-20240105163454711" />

3. 为了生成正确的交叉引用，一般也需要多次编译源代码。文档中新增标签后后，第一次编译时会得到类似下面的警告信息。因为第一次编译只会扫描出有标签的地方，第二次编译才能得到正确结果。

   ```shell
   LaTeX Warning: There were undefined references.
   LaTeX Warning: Label(s) may have changed. Rerun to get
   cross-references right.
   ```

4. \label命令可用于记录各种类型的交叉引用，使用位置分别为：

   ```latex
   章节标题 %在章节标题命令\section等之后紧接着使用。
   行间公式 %单行公式在公式内任意位置使用；多行公式在每一行公式的任意位置使用。
   有序列表 %在enumerate环境的每个\item命令之后、下一个\item命令之前任意位置使用。
   图表标题 %在图表标题命令\caption之后紧接着使用。
   定理环境 %在定理环境内部任意位置使用。
   %如果对象是由一条命令产生的，如\section，直接在其后输入\label{...}即可，如果是由环境产生，则需要在环境内部任意处声明label，如equation。 
   %在使用不记编号的命令形式（\section*、\caption*3、带可选参数的\item 命令等）时不要使用\label 命令，否则生成的引用编号不正确。
   ```


## 脚注，边注

1. 使用\footnote命令可以在页面底部生成一个脚注，脚注内也可以包含公式、图片等：

   ```latex
   “天地玄黄，宇宙洪荒。日月盈昃，辰宿列张。”\footnote{出自《千字文》。}
   ```

2. 在正文和脚注的显示分别为：

3. <img src="LaTeX.assets/image-20240105164024452-1704516157721-11-1704516183762-69.png" alt="image-20240105164024452" />

4. <img src="LaTeX.assets/image-20240105164032650-1704516157721-13-1704516183762-70.png" alt="image-20240105164032650" />

5. 有些情况下（比如在表格环境、各种盒子内，用于对某个单元格进行注释）使用\footnote并不能正确生成脚注。我们可以分两步进行，先使用\footnotemark为脚注计数，再在合适的位置用\footnotetext生成脚注。对整个表格的注释就放在环境外，直接使用\footnote即可。

6. 边注可以使用\marginpar命令。单面排版时，边注缺省排在页面右边空白处；双面排版时，边注在外侧；双栏页面的边注排在最近的页边。如要切换边注的方向，可以使用\reversemarginpar和\normalmarginpar命令。

7. \marginpar命令使用浮动体(float)来生成边注，所以不能在其他浮动体或脚注内嵌套。marginnote宏包的\marginnote命令不使用浮动体，因而没有这个缺陷。


## 列表

1. LaTeX提供了基本的有序和无序列表环境enumerate和itemize，两者的用法很类似，都用\item标明每个列表项。enumerate环境会自动对列表项编号。其中\item可带一个可选参数，将有序列表的计数或者无序列表的符号替换成自定义的符号。列表可以嵌套使用，最多嵌套四层。

   ```latex
   \begin{enumerate}
   	\item An item.
   	\begin{enumerate}
   		\item A nested item.\label{itref}
   		\item[*] A starred item.
   	\end{enumerate}
   	\item Reference(\ref{itref}).
   \end{enumerate}
   %各级无序列表的符号由命令\labelitemi 到\labelitemiv定义，可以简单地重新定义它们。有序列表使用\labelenumi到\labelenumiv。
   \renewcommand{\labelitemi}{\ddag} %i表示第一级,ii表示第二级
   \renewcommand{\labelitemii}{\dag}
   \begin{itemize}
   	\item An item.
   	\begin{itemize}
   		\item A nested item.
   		\item[+] A `plus' item.
   		\item Another item.
   	\end{itemize}
   	\item Go back to upper level.
   \end{itemize}
   ```

2. <img src="LaTeX.assets/image-20240105170001764-1704516157721-12-1704516183762-71.png" alt="image-20240105170001764" />

3. 默认的列表间距比较宽，LaTeX本身也未提供方便的定制功能，可用enumitem宏包定制各种列表间距。enumitem宏包还提供了对列表标签、引用等的定制。

4. 还有一种描述列表：

   ```latex
   \begin{description}
   	\item[C++] 编程语言
   	\item[Java] 编程语言
   	\item[HTML] 标记语言
   \end{description}
   ```

5. <img src="LaTeX.assets/image-20240115010001003.png" alt="image-20240115010001003" />

6. 上述列表的缺省行间距较大，如要节省空间，可以使用paralist宏包，它提供了一系列压缩列表和行间列表环境。compactitem，compactenum，compactdesc。


## 对齐

1. center、flushleft 和flushright 环境分别用于生成居中、左对齐和右对齐的文本环境。

   ```latex
   \begin{center}
       Centered text using a
       \verb|center| environment.
   \end{center}
   \begin{flushleft}
       Left-aligned text using a
       \verb|flushleft| environment.
   \end{flushleft}
   \begin{flushright}
       Right-aligned text using a
       \verb|flushright| environment.
   \end{flushright}
   ```

2. <img src="LaTeX.assets/image-20240105181322555-1704516157721-14-1704516183762-74.png" alt="image-20240105181322555" />

3. 还可以用以下命令直接改变文字的对齐方式：

   ```latex
   %段落缺省两端对齐(fully justified)
   \centering
   Centered text paragraph.
   
   \raggedright
   Left-aligned text paragraph.
   
   \raggedleft
   Right-aligned text paragraph.
   ```

4. <img src="LaTeX.assets/image-20240105181743608-1704516157721-15-1704516183762-72.png" alt="image-20240105181743608" />

5. 三个命令和对应的环境经常被误用，命令是对其后的所有都生效，直到遇到同类的其他命令。命令和环境的区别是：

6. center等环境会在上下文中产生一个额外间距，而\centering等命令不产生，只是改变对齐方式。比如在浮动体环境table或figure内实现居中对齐，应使用\centering命令，没必要再用center环境。


## 引用，代码输出

1. LaTeX提供了两种引用的环境：quote用于引用较短的文字，首行不缩进；quotation用于引用若干段文字，首行缩进。引用环境较一般文字有额外的左右缩进。

2. 有时我们需要将一段代码原样转义输出，这就要用到代码环境verbatim，它以等宽字体排版代码，回车和空格也分别起到应有的换行和空格的作用；带星号的版本会将空格显示成`␣`。会在代码前后插入空行。

   ```latex
   \begin{verbatim*}
   #include <iostream>
   int main(){
   	std::cout << "Hello, world!"
   	<< std::endl;
   	return 0;
   }
   \end{verbatim*}
   ```

3. <img src="LaTeX.assets/image-20240105192426917-1704516157721-16-1704516183762-73.png" alt="image-20240105192426917" />

4. 正文间插入少量等宽文字，或排版简短的代码或关键字，可使用\verb命令：

   ```latex
   \verb⟨delim⟩⟨code⟩⟨delim⟩ %⟨delim⟩符号用来标明代码的分界位置，前后必须一致，除字母、空格或星号外，可任意选择使得不与代码本身冲突，习惯上使用|符号。
   %同verbatim 环境，\verb 后也可以带一个星号，以显示空格
   \verb|\LaTeX|
   
   \verb+(a || b)+ \verb*+(a || b)+
   ```

5. <img src="LaTeX.assets/image-20240105192813874-1704516157721-17-1704516183762-76.png" alt="image-20240105192813874" />

6. \verb命令对符号的处理比较复杂，一般不能用在其它命令的参数里，否则多半会出错。verbatim 宏包优化了verbatim环境的内部命令，并提供了\verbatiminput命令用来直接读入文件生成代码环境。fancyvrb 宏包提供了可定制格式的Verbatim环境；listings宏包更进一步，可生成关键字高亮的代码环境，支持各种程序设计语言的语法和关键字和关键词加粗。

   ```latex
   \usepackage{listings}
   \begin{document}
   \begin{lstlisting}[language=Python]
   #注释
   import requests
   htmlurl = "https://www.acfun.cn/v/ac13355779_1"
   f = open("xx.txt", "w+")
   f.write(responsehtml)
   f.close()
   \end{lstlisting}
   \end{document}
   ```

7. <img src="LaTeX.assets/image-20240106024811696-1704516157721-18-1704516183762-75.png" alt="image-20240106024811696" />

## 表格

1. 排版表格最基本的是tabular环境，直接使用tabular环境的话，会和周围的文字混排。但是通常情况下tabular环境很少与文字直接混排，而是会放在table浮动体环境中，并用\caption命令加标题。

   ```latex
   \begin{tabular}{|c|} % |c|是列格式标记
   	center-\\ aligned
   \end{tabular},
   \begin{tabular}[t]{|c|}
   	top-\\ aligned
   \end{tabular},
   \begin{tabular}[b]{|c|}
   	bottom-\\ aligned
   \end{tabular} tabulars.
   %有一个可选参数可以控制垂直对齐：t和b分别表示按表格顶部、底部对齐，其他参数或省略时（默认）表示居中对齐。
   ```

2. <img src="LaTeX.assets/image-20240105193648370-1704516157721-19-1704516183762-77.png" alt="image-20240105193648370" />

3. http://www.tablesgenerator.com   在线生成LaTeX表格。

4. 表格环境中使用&来分隔单元格，`\\`来换行，\hline来在行与行之间绘制横线。

5. 列格式，指定表格的列数以及每列的格式：

   ```latex
   \begin{tabular}{lcr|p{6em}}
   	\hline
   	left & center & right & par box with fixed width\\ %第一个&前没有任何内容则表示空
   	L & C & R & P \\
   	\hline
   \end{tabular}
   %lcr 表示单元格内容左对齐/居中/右对齐，不折行
   %p{6em} 单元格宽度固定为6em，如果超出可自动折行
   %| 会在左右的列之间绘制竖线
   ```

6. <img src="LaTeX.assets/image-20240105194948173-1704516157721-20-1704516183762-78.png" alt="image-20240105194948173" />

7. 表格中每行的单元格数目不能多（可以少）于列格式里`l/c/r/p`的总数，否则出错。

8. @格式可在单元格前后插入任意的文本，但同时它也消除了单元格前后额外添加的间距。可以适当使用以充当“竖线”。

   ```latex
   \begin{tabular}{@{}r@{:}lr@{}}  %rlr一共3列，在r和l之间有一个:
   	\hline
   	1 & 1 & one \\
   	11 & 3 & eleven \\
   	\hline
   \end{tabular}
   ```

9. <img src="LaTeX.assets/image-20240105200209634-1704516157721-21-1704516183762-79.png" alt="image-20240105200209634" />

10. 还提供了简便的将格式参数重复的写法：

    ```latex
    \begin{tabular}{|c|c|c|c|c|p{4em}|p{4em}|}
    \begin{tabular}{|*{5}{c|}*{2}{p{4em}|}} %同上
    % *{5}{c|}  等价于c|c|c|c|c|
    ```

11. 有时需要为整列修饰格式，如果对该列的每个单元格逐个施加，则比较麻烦，可以使用array宏包提供了辅助格式>和<，用于给列格式前后加上修饰命令：

    ```latex
    \usepackage{array}
    \begin{document}
    \begin{tabular}{>{\itshape}r<{*}l}
    	\hline
    	italic & normal \\
    	column & column \\
    	\hline
    \end{tabular}
    \end{document}
    ```

12. <img src="LaTeX.assets/image-20240105201305824-1704516157721-22-1704516183762-80.png" alt="image-20240105201305824" />

13. array宏包还提供了类似p格式的m格式和b格式，三者分别在垂直方向上靠顶端对齐、居中以及底端对齐。

14. 在控制列宽方面，LaTeX表格有着明显的不足：l/c/r格式的列宽是由文字内容的自然宽度决定的，而p格式给定了列宽却不好控制对齐（可用array宏包的辅助格式），更何况列与列之间通常还有间距，所以直接生成给定总宽度的表格并不容易。

15. tabularx宏包为我们提供了方便的解决方案。它引入了一个X列格式，类似p列格式，不过会根据表格宽度自动计算列宽，多个X列格式平均分配列宽。X列格式也可以用array里的辅助格式修饰对齐方式：

    ```latex
    \usepackage{array,tabularx}
    \begin{document}
    \begin{tabularx}{14em}
    	{|*{4}{>{\centering\arraybackslash}X|}}
    	\hline
    	A & B & C & D \\
    	\hline
    	a & b & c & d \\
    	\hline
    \end{tabularx}
    \end{document}
    ```

16. <img src="LaTeX.assets/image-20240105202050423-1704516157721-23-1704516183762-81.png" alt="image-20240105202050423" />

17. \hline命令可以绘制贯穿所有单元格的横线。另外`\cline{⟨i⟩-⟨j⟩}`用来绘制跨越部分单元格的横线：

    ```latex
    \begin{tabular}{|c|c|c|}
    	\hline
    	4 & 9 & 2 \\
    	\cline{2-3}
    	3 & 5 & 7 \\
    	\cline{1-1}
    	8 & 1 & 6 \\
    	\hline
    \end{tabular}
    ```

18. <img src="LaTeX.assets/image-20240105202407972-1704516157721-24-1704516183762-82.png" alt="image-20240105202407972" />

19. 三线表由booktabs 宏包支持，它提供了\toprule、\midrule 和\bottomrule命令用以排版三线表的三条线，以及和\cline 对应的\cmidrule。除此之外，最好不要用其它横线以及竖线：

    ```latex
    \usepackage{booktabs}
    \begin{document}
    \begin{tabular}{cccc}
    	\toprule
    	& \multicolumn{3}{c}{Numbers} \\
    	\cmidrule{2-4}
    	& 1 & 2 & 3 \\
    	\midrule
    	Alphabet & A & B & C \\
    	Roman & I & II& III \\
    	\bottomrule
    \end{tabular}
    \end{document}
    ```

20. <img src="LaTeX.assets/image-20240105202728473-1704516157721-25-1704516183762-83.png" alt="image-20240105202728473" />

21. LaTeX是一行一行排版表格的，横向合并单元格较为容易，由\multicolumn命令实现。

22. LaTeX生成的表格看起来通常比较紧凑。修改参数\arraystretch可以得到行距更加宽松的表格。另一种增加间距的办法是给换行命令`\\`添加可选参数。

    ```latex
    \renewcommand\arraystretch{1.8}
    
    \\[6pt] %在这一行下面加额外的间距，适合用于在行间不加横线的表格
    ```


## 图片

1. LaTeX本身不支持插图功能，需要由graphicx宏包辅助支持。

2. 使用latex + dvipdfmx 编译命令时，调用graphicx 宏包时要指定dvipdfmx 选项；而使用pdflatex 或xelatex 命令编译时不需要。事实上不同编译命令支持的图片格式种类也不同：

   ```latex
   格式                    矢量图         位图
   latex + dvipdfmx        .eps          N/A
      （调用bmpsize 宏包）  .eps .pdf    .jpg .png .bmp
   pdflatex                .pdf         .jpg .png
      （调用epstopdf 宏包） .pdf .eps    .jpg .png
   xelatex                 .pdf .eps    .jpg .png .bmp
   ```

3. 在调用了graphicx 宏包以后，就可以使用\includegraphics命令加载图片。

   ```latex
   \includegraphics[⟨options⟩]{⟨filename⟩} %图片文件的扩展名一般可不写。文件名里既不要有空格（类似\include），也不要有多余的英文点号。
   %可选参数可以使用⟨key⟩=⟨value⟩的形式给出
   width=⟨width⟩   %将图片缩放到宽度为⟨width⟩
   height=⟨height⟩ %将图片缩放到高度为⟨height⟩
   scale=⟨scale⟩   %将图片相对于原尺寸缩放⟨scale⟩倍
   angle=⟨angle⟩   %将图片逆时针旋转⟨angle⟩度
   ```

4. 另外graphicx宏包还提供了\graphicspath命令，用于声明一个或多个图片文件存放的目录，使用这些目录里的图片时可不用写路径：

   ```latex
   \graphicspath{{figures/}{logo/}}
   ```

5. graphicx 宏包也支持draft/final 选项。当graphicx 宏包或文档类指定draft 选项时，图片将不会被实际插入，取而代之的是一个包含文件名的与原图片等大的方框。


## 盒子

1. 盒子是LaTeX排版的基础单元，每一行是一个盒子，里面的文字从左到右依次排列；每一页也是一个盒子，各行文字从上到下依次排布。在HTML和CSS中也可以见到类似的模型。分为四种：

2. 水平盒子

   ```latex
   \mbox{…} %基本的水平盒子，内容只有一行，不允许分段（除非嵌套其它盒子，比如后文的垂直盒子）。外表看上去，\mbox 的内容与正常的文本无二，不过断行时文字不会从盒子里断开。
   \makebox[⟨width⟩][⟨align⟩]{…} %可选参数用于控制盒子的宽度⟨width⟩，以及内容的对齐方式⟨align⟩，可选居中c（默认值）、左对齐l、右对齐r和分散对齐s。
   %例子
   |\mbox{Test some words.}|\\
   |\makebox[10em]{Test some words.}|\\
   |\makebox[10em][l]{Test some words.}|\\
   |\makebox[10em][r]{Test some words.}|\\
   |\makebox[10em][s]{Test some words.}|
   ```

3. <img src="LaTeX.assets/image-20240113164517072.png" alt="image-20240113164517072" />

4. 带框的水平盒子，\fbox和\framebox让我们可以为水平盒子添加边框。使用的语法同上：

   ```latex
   \fbox{Test some words.}\\ %和mbox对应
   \framebox[10em][r]{Test some words.} %和makebox对应
   %可以通过\setlength命令调节边框的宽度\fboxrule和内边距\fboxsep
   ```

5. <img src="LaTeX.assets/image-20240113164548091.png" alt="image-20240113164548091" />

6. 垂直盒子，有宽度、高度、外部对齐、内部对齐等选项：

   ```latex
   \parbox[⟨align⟩][⟨height⟩][⟨inner-align⟩]{⟨width⟩}{…} %⟨align⟩为盒子和周围文字的对齐情况(类似tabular环境，其中t表示盒子的顶部和周围文字的顶部对齐)；⟨height⟩和⟨inner-align⟩设置盒子的高度和内容的对齐方式，类似水平盒子\makebox的设置，不过⟨inner-align⟩接受的参数是顶部t、底部b、居中c 和分散对齐s。
   \begin{minipage}[⟨align⟩][⟨height⟩][⟨inner-align⟩]{⟨width⟩}
   …
   \end{minipage}
   %例子
   三字经：\parbox[t]{3em}{人之初性本善性相近习相远}\quad{}千字文：
   \begin{minipage}[b][8ex][t]{4em}
   	天地玄黄宇宙洪荒
   \end{minipage}
   ```

7. <img src="LaTeX.assets/image-20240113165847365.png" alt="image-20240113165847365" />

8. 如果在minipage里使用\footnote命令，生成的脚注会出现在盒子底部，编号是独立的，并且使用小写字母编号。这也是minipage 环境之被称为“迷你页”（Mini-page）的原因。而在\parbox 里无法正常使用\footnote命令，只能在盒子里使用\footnotemark，在盒子外使用\footnotetext。

   ```latex
   %在带框的水平盒子里嵌套一个垂直盒子
   \fbox{\begin{minipage}{15em}这是一个垂直盒子的测试。\footnote{脚注来自minipage。}\end{minipage}}
   ```

9. <img src="LaTeX.assets/image-20240113170119866.png" alt="image-20240113170119866" />


## 浮动体

1. 内容丰富的文章或者书籍往往包含许多图片和表格等内容。这些内容的尺寸往往太大，导致分页困难。LaTeX为此引入了浮动体的机制，令大块的内容可以脱离上下文，放置在合适的位置。

2. LaTeX预定义了两类浮动体环境figure 和table。习惯上figure里放图片，table里放表格，但并没有严格限制，可以在任何一个浮动体里放置文字、公式、表格、图片等等任意内容，也允许在一个浮动体里面放置多张图。

   ```latex
   \usepackage{graphicx}
   \begin{document}
   \begin{figure}[htbp!] %htbp!表示浮动体允许排版的位置，分别表示当前位置，顶部，底部，单独成页，在决定位置时忽视限制。排版位置的选取与参数里符号的顺序无关，因为latex总是按照h-t-b-p的顺序决定的。
   	\centering
   	\includegraphics[width=...]{...}
   	\qquad
   	\includegraphics[width=...]{...} \\[...pt]
   	\includegraphics[width=...]{...}
   	\caption{...}
   \end{figure}
   \end{document}
   ```

3. <img src="LaTeX.assets/image-20240105212608227-1704516157721-26-1704516183762-84.png" alt="image-20240105212608227" />

4. 限制包括浮动体个数（除单独成页外，默认每页不超过3 个浮动体，其中顶部不超过2 个，底部不超过1 个）以及浮动体空间占页面的百分比（默认顶部不超过70%，底部不超过30%）。

5. 双栏排版环境下，LaTeX 提供了table* 和figure* 环境用来排版跨栏的浮动体。它们的用法与table和figure一样，不同之处为双栏的⟨placement⟩ 参数只能用tp两个位置。

6. 浮动体的位置选取受到先后顺序的限制。如果某个浮动体由于参数限制、空间限制等原因在当前页无法放置，就要推迟到之后处理，并使得之后的同类浮动体一并推迟。\clearpage 命令会在另起一页之前，先将所有推迟处理的浮动体排版成页，此时htbp等位置限制被完全忽略。

7. float 宏包为浮动体提供了H位置参数，不与htbp 及! 混用。使用H位置参数时，会取消浮动机制，将浮动体视为一般的盒子插入当前位置。这在一些特殊情况下很有用（如使用multicol宏包排版分栏内容的时候），但尺寸过大的浮动体可能使得分页比较困难。

8. 图表等浮动体提供了\caption命令加标题，并且自动给浮动体编号。可以用带星号的命令\caption*9 生成不带编号的标题，不过要使用caption宏包。

9. 由于标题是横跨一行的，用\caption命令为每个图片单独生成标题就需要借助\parbox或者minipage环境，将标题限制在盒子内。

   ```latex
   \begin{figure}[htbp]
   \centering
       \begin{minipage}{...}
           \centering
           \includegraphics[width=...]{...}
           \caption{...}
       \end{minipage}
   \qquad
       \begin{minipage}{...}
           \centering
           \includegraphics[width=...]{...}
           \caption{...}
       \end{minipage}
   \end{figure}
   ```

10. <img src="LaTeX.assets/image-20240105213751384-1704516157721-27-1704516183762-85.png" alt="image-20240105213751384" />

11. 如果要给每个图片定义小标题，就要用到subcaption宏包。subcaption 依赖上文提到过的caption 宏包，因此也支持子图表标题样式的定制。并排子图表的功能也可通过subfig 宏包的\subfloat 命令实现

# 公式

1. AMS宏集合是美国数学学会(American Mathematical Society) 提供的对LaTeX原生的数学公式排版的扩展，其核心是amsmath宏包，对多行公式的排版提供了有力的支持。此外，amsfonts宏包以及基于它的amssymb宏包提供了丰富的数学符号，amsthm宏包扩展了LaTeX 定理证明格式。

2. 数学公式有两种排版方式：与文字混排的行内公式；单独列为一行的行间公式。

3. 行内公式由一对$ 符号包裹：

   ```latex
   The Pythagorean theorem is $a^2 + b^2 = c^2$.
   ```

4. <img src="LaTeX.assets/image-20240105215132102-1704516157721-28-1704516183762-86.png" alt="image-20240105215132102" />

5. 行间公式在由equation环境包裹。equation环境为公式自动生成一个编号，这个编号可以用\label和\ref生成交叉引用，amsmath宏包的\eqref命令甚至为引用自动加上圆括号；还可以用\tag 命令手动修改公式的编号，或者用\notag 命令取消为公式编号（与之基本等效的命令是\nonumber）。

   ```latex
   \usepackage{amsmath}
   \begin{document}
   The Pythagorean theorem is:
   \begin{equation}
   	a^2 + b^2 = c^2 \label{pythagorean}
   \end{equation}
   Equation \eqref{pythagorean} is called `Gougu theorem' in Chinese.
   \end{document}
   ```

6. <img src="LaTeX.assets/image-20240105220308953-1704516157721-29-1704516183762-87.png" alt="image-20240105220308953" />

7. 如果需要直接使用不带编号的行间公式，则将公式用命令`\[`和`\]`包裹，与之等效的是displaymath环境。也可以使用equation*环境。TEX原生排版的行间公式是用一对$$符号（即左右各2各）包裹，不过无法通过指定fleqn选项控制左对齐，与上下文之间的间距也不好调整，故不太推荐使用。

   ```latex
   \begin{equation*}
   	a^2 + b^2 = c^2
   \end{equation*}
   For short:
   	\[ a^2 + b^2 = c^2 \]
   Or if you like the long one:
   \begin{displaymath}
   	a^2 + b^2 = c^2
   \end{displaymath}
   ```

8. <img src="LaTeX.assets/image-20240106124701106.png" alt="image-20240106124701106" />

9. 为了与文字相适应，行内公式在排版大的公式元素（分式、巨算符等）时显得很“局促”：

   ```latex
   $\lim_{n \to \infty}\sum_{k=1}^n \frac{1}{k^2}= \frac{\pi^2}{6}$.
   
   In display:
   \[ \lim_{n \to \infty}\sum_{k=1}^n\frac{1}{k^2}= \frac{\pi^2}{6} \]
   ```

10. <img src="LaTeX.assets/image-20240106124929469.png" alt="image-20240106124929469" />

11. 行间公式的对齐、编号位置等性质由文档类选项控制，文档类的fleqn选项令行间公式左对齐；leqno选项令编号放在公式左边。

12. 输入公式时，会进入数学模式，有如下特点：

    1. 输入的空格被忽略。数学符号的间距默认由符号的性质（关系符号、运算符等）决定。需要人为引入间距时，使用\quad和\qquad等命令。

    2. 不允许有空行（分段），行间公式中也无法用`\\`命令手动换行。排版多行公式需要用特殊的环境。

    3. 所有的字母被当作数学公式中的变量处理，字母间距与文本模式不一致，也无法生成单词之间的空格。如果想在数学公式中输入正体的文本，简单情况下可用\mathrm命令。或者用amsmath提供的\text命令。该命令仅适合在公式中穿插少量文字。如果需要在许多文字中穿插使用公式，则应该使用行内公式，而不是滥用\text命令。

    4. ```latex
       \usepackage{amsmath}
       \usepackage{amssymb}
       \begin{document}
       $x^{2} \geq 0 \qquad \text{for \textbf{all} }x\in\mathbb{R}$ %文本都添加在公式中
       \end{document}
       ```

       <img src="LaTeX.assets/image-20240106125809479.png" alt="image-20240106125809479" />

    5. ```latex
       \usepackage{amsmath}
       \usepackage{amssymb}
       \begin{document}
       $x^{2} \geq 0$\qquad for \textbf{all} $x\in\mathbb{R}$ %尽可能少的在公式中添加文本
       \end{document}
       ```

       <img src="LaTeX.assets/image-20240106130111557.png" alt="image-20240106130111557" />


## 符号

1. LaTeX默认提供了常用的数学符号，amssymb宏包提供了一些次常用的符号。

2. 希腊字母符号的名称就是其英文名称，例如$\alpha$用`\alpha`表示。大写的希腊字母为首字母大写的命令，例如$\Delta$用`\Delta`表示。

3. 省略号有`\dots`和`\cdots`两种形式，有各自的用途：

   ```latex
   $a_1, a_2, \dots, a_n$ %这里使用cdots时，点就会比逗号的点高出一部分，不好看。
   
   $a_1 + a_2 + \cdots + a_n$ %这里使用cdots和dots结果一样，都会和+的水平线对齐。
   ```

4. <img src="LaTeX.assets/image-20240106130643731.png" alt="image-20240106130643731" />

5. `\ldots`和`\dots`是完全等效的，它们既能用在公式中，也用来在文本里作为省略号。在矩阵中可能会用到竖排的`\vdots`和斜排的`\ddots`。

   ```latex
   $a\vdots b\ddots c$
   ```

6. <img src="LaTeX.assets/image-20240106131000277.png" alt="image-20240106131000277" />

7. 导数符号`'`是一类特殊的上标，可以适当连用表示多阶导数，也可以在其后连用上标：

   ```latex
   $f(x) = x^2 \quad f'(x) = 2x \quad f''^{2}(x) = 4$
   ```

8. <img src="LaTeX.assets/image-20240106131407462.png" alt="image-20240106131407462" />

9. 分式的大小在行间公式中是正常大小，而在行内被极度压缩。amsmath提供了方便的命令\dfrac和\tfrac，令用户能够在行内使用正常大小的分式，或者在行间使用缩小的公式。

   ```latex
   In display style:
   \[
   3/8 \qquad \frac{3}{8} \qquad \tfrac{3}{8}
   \]
   In text style:
   $1\frac{1}{2}$ hours \qquad $1\dfrac{1}{2}$ hours
   ```

10. <img src="LaTeX.assets/image-20240106131727591.png" alt="image-20240106131727591" />

11. 根式命令`\sqrt[n]{}`有一个可选参数，用于表示开方的次数：

    ```latex
    $\sqrt[3]{2}$
    ```

12. <img src="LaTeX.assets/image-20240106132450210.png" alt="image-20240106132450210" />

13. 特殊的分式形式，如二项式结构，由amsmath宏包的\binom命令生成：

    ```latex
    \[ \binom{n}{k} =\binom{n-1}{k} + \binom{n-1}{k-1} \]
    ```

14. <img src="LaTeX.assets/image-20240106132525160.png" alt="image-20240106132525160" />

15. 常见的关系符号除了可以直接输入的=，>，<，其它符号用命令输入。大于等于或小于等于有两种样式，倾斜的关系符号由amssymb提供。

    ```latex
    $a\ge b$ $a \geqslant b$
    ```

16. <img src="LaTeX.assets/image-20240106133217648.png" alt="image-20240106133217648" />

17. LaTeX还提供了自定义二元关系符的命令\stackrel，用于将一个符号叠加在原有的二元关系符之上：

    ```latex
    \[ f_n(x) \stackrel{*}{\approx} 1 \]
    ```

18. <img src="LaTeX.assets/image-20240106132914033.png" alt="image-20240106132914033" />

19. LaTeX将数学函数的名称作为一个算符排版，字体为直立字体。其中有一部分符号在上下位置可以书写一些内容作为条件，类似于后文所叙述的巨算符。作为算符的函数名称汇总如下：

    ```latex
    %     不带上下限的算符
    \sin \arcsin \sinh \exp \dim
    \cos \arccos \cosh \log \ker
    \tan \arctan \tanh \lg \hom
    \cot \arg \coth \ln \deg
    \sec \csc
    %     带上下限的算符
    \lim \limsup \liminf \sup \inf
    \min \max \det \Pr \gcd
    %例子
    \[
    \lim_{x \rightarrow 0} \frac{\sin x}{x}=1
    \]
    ```

20. <img src="LaTeX.assets/image-20240106133540022.png" alt="image-20240106133540022" />

21. 如果LaTeX自带的算符不够用的话，amsmath允许用户在导言区用\DeclareMathOperator定义自己的算符，其中带星号的命令定义带上下限的算符：

    ```latex
    \usepackage{amsmath}
    \DeclareMathOperator{\argh}{argh}
    \DeclareMathOperator*{\nut}{Nut}
    \begin{document}
    \[\argh 3 = \nut_{x=1} 4x\]
    \end{document}
    ```

22. <img src="LaTeX.assets/image-20240106133742697.png" alt="image-20240106133742697" />

23. 积分号，求和号等符号被称为巨算符。他们在行内公式和行间公式的大小和形状有区别。

    ```latex
    $ \sum_{i=1}^n \quad\int_0^{\frac{\pi}{2}} \quad\oint_0^{\frac{\pi}{2}} \quad\prod_\epsilon $
    
    In display:
    \[ \sum_{i=1}^n \quad\int_0^{\frac{\pi}{2}} \quad\oint_0^{\frac{\pi}{2}} \quad\prod_\epsilon \]
    ```

24. <img src="LaTeX.assets/image-20240106134133801.png" alt="image-20240106134133801" />

25. 巨算符的上下标位置可由\limits和\nolimits调整，前者令巨算符的上下标位于正上下方，后者令巨算符的上下标位于右上方和右下方，类似于积分符号的。

    ```latex
    $\sum\limits_{i=1}^n \quad\int\limits_0^{\frac{\pi}{2}} \quad\prod\limits_\epsilon $
    
    In display:
    \[ \sum\nolimits_{i=1}^n \quad\int\limits_0^{\frac{\pi}{2}} \quad\prod\nolimits_\epsilon \]
    ```

26. <img src="LaTeX.assets/image-20240106134511109.png" alt="image-20240106134511109" />

27. amsmath宏包还提供了\substack，能够在下限位置书写多行表达式；subarray 环境更进一步，令多行表达式可选择居中(c) 或左对齐(l)：

    ```latex
    \[
    \sum_{\substack{0\le i\le n \\ j\in \mathbb{R}}}P(i,j) = Q(n)
    \]
    
    \[
    \sum_{
    	\begin{subarray}{l}
    		0\le i\le n \\
    		j\in \mathbb{R}
    	\end{subarray}}
    P(i,j) = Q(n)
    \]
    ```

28. <img src="LaTeX.assets/image-20240106134657226.png" alt="image-20240106134657226" />

29. 数学符号可以像文字一样加重音，使用时要注意重音符号的作用区域，一般应当对某个符号而不是“符号加下标”使用重音。

    ```latex
    $\bar{x_0} \quad \bar{x}_0$
    
    $\vec{x_0} \quad \vec{x}_0$
    
    $\hat{\mathbf{e}_x}\quad\hat{\mathbf{e}}_x$
    ```

30. <img src="LaTeX.assets/image-20240106134913077.png" alt="image-20240106134913077" />

31. LaTeX也能为多个字符加重音，

    ```latex
    $0.\overline{3} =\underline{\underline{1/3}}$
    
    $\hat{XY} \qquad \widehat{XY}$
    
    $\vec{AB} \qquad \overrightarrow{AB}$
    ```

32. <img src="LaTeX.assets/image-20240106135145752.png" alt="image-20240106135145752" />

33. LaTeX 提供了多种括号和定界符表示公式块的边界，如小括号`()`、中括号`[]`、大括号`{}`、尖括号`⟨⟩`（\langle，\rangle)等。使用\left和\right命令可令括号（定界符）的大小可变，在行间公式中常用。LaTeX会自动根据括号内的公式大小决定定界符大小。二者必须成对使用。需要使用单个定界符时，另一个定界符写成`\left.`或`\right.`。

    ```latex
    \[
    1 + \left( \frac{1}{1-x^{2}} \right)^3 \qquad \left. \frac{\partial f}{\partial t} \right|_{t=0}
    \]
    ```

34. <img src="LaTeX.assets/image-20240106203414230.png" alt="image-20240106203414230" />

35. 还可以用\big、\bigg等命令生成固定大小的定界符，这些不必成对出现，这使得它可以被断行，这是比`\left`和`\right`好的点。

    ```latex
    $\Bigl((x+1)(x-1)\Bigr)^{2}$
    
    $\bigl( \Bigl( \biggl( \Biggl( \quad
    \bigr\} \Bigr\} \biggr\} \Biggr\} \quad
    \big\| \Big\| \bigg\| \Bigg\| \quad    %||得到的结果不是一样长的竖线
    \big\Downarrow \Big\Downarrow \bigg\Downarrow \Bigg\Downarrow$
    ```

36. <img src="LaTeX.assets/image-20240106204003183.png" alt="image-20240106204003183" />


## 折行

1. 通常来讲应当避免写出超过一行而需要折行的长公式。如果一定要折行的话，优先在等号前折行，其次在加号、减号之前，再次在乘号、除号之前。其它位置应当避免折行。

2. amsmath宏包的multline环境提供了书写折行长公式的方便环境。它允许用`\\`折行，公式编号在最后一行。多行公式的首行左对齐，末行右对齐，其余行居中。

   ```latex
   \begin{multline}
   a + b + c + d + e + f + g + h + i \\
   	= j + k + l + m + n\\
   	= o + p + q + r + s\\
   	= t + u + v + x + z
   \end{multline}
   ```

3. <img src="LaTeX.assets/image-20240106205252434.png" alt="image-20240106205252434" />

4. 与表格不同的是，公式的最后一行不应写`\\`，如果写了，反倒会产生一个多余的空行。类似equation\*，multline\* 环境排版不带编号的折行长公式。


## 多个公式

1. 更多的情况是，我们需要罗列一系列公式，并令其按照等号对齐：

2. LaTeX 提供了eqnarray 环境。它按照等号左边——等号——等号右边呈三列对齐，但等号周围的空隙过大，加上公式编号等一些bug，目前已不推荐使用。

3. 目前最常用的是align环境，它将公式用&隔为两部分并对齐。分隔符通常放在等号左边：

   ```latex
   \begin{align}
   	a & = b + c \\
   	& = d + e
   \end{align}
   ```

4. <img src="LaTeX.assets/image-20240106210002728.png" alt="image-20240106210002728" />

5. align环境会给每行公式都编号。我们仍然可以用\notag去掉某行的编号。为了对齐等号，将分隔符放在右侧，并且此时需要在等号后添加一对括号{}以产生正常的间距：

   ```latex
   \begin{align}
   	a ={} & b + c \\
   	={} & d + e + f + g + h + i + j + k + l \notag \\
   	={} & p + q + r + s
   \end{align}
   ```

6. <img src="LaTeX.assets/image-20240106211057402.png" alt="image-20240106211057402" />

7. 将多个公式组在一起公用一个编号，编号位于公式的居中位置。amsmath宏包提供了诸如aligned、gathered等环境，与equation环境套用。aligned环境可以用定界符包裹。

   ```latex
   \begin{equation}
   	\begin{aligned}
   		a &= b + c \\
   		d &= e + f + g \\
   		h + i &= j + k \\
   		l + m &= n
   	\end{aligned}
   \end{equation}
   ```

8. <img src="LaTeX.assets/image-20240106210414383.png" alt="image-20240106210414383" />


## 矩阵

1. 为了排版矩阵，LaTeX提供了array环境，用法与tabular环境极为类似，也需要定义列格式，并用`\\`换行。矩阵可作为一个公式块，在外套用`\left`、`\right`等定界符：

   ```latex
   \[
   \mathbf{X} = \left(
   \begin{array}{cccc}
   	x_{11} & x_{12} & \ldots & x_{1n}\\
   	x_{21} & x_{22} & \ldots & x_{2n}\\
   	\vdots & \vdots & \ddots & \vdots\\
   	x_{n1} & x_{n2} & \ldots & x_{nn}\\
   \end{array} \right)
   \]
   ```

2. <img src="LaTeX.assets/image-20240106211453943.png" alt="image-20240106211453943" />

3. 分段函数排版：

   ```latex
   \[
   |x| = \left\{
   \begin{array}{rl}
   	-x & \text{if } x < 0,\\
   	0 & \text{if } x = 0,\\
   	x & \text{if } x > 0.
   \end{array} \right.
   \]
   ```

4. <img src="LaTeX.assets/image-20240106211841026.png" alt="image-20240106211841026" />

5. 可以用array环境排版各种矩阵。amsmath宏包还直接提供了多种排版矩阵的环境，包括不带定界符的matrix，以及带各种定界符的矩阵pmatrix，bmatrix，Bmatrix，vmatrix，Vmatrix。使用这些环境时，无需给定列格式，事实上这些矩阵内部也是用array环境生成的，列格式默认为*{⟨n⟩}{c}，⟨n⟩ 默认为10：

   ```latex
   matrix  %没有定界符
   pmatrix %小括号
   bmatrix %中括号
   Bmatrix %大括号
   vmatrix %单竖线
   Vmatrix %双竖线
   ```

6. 如果矩阵中的元素包含分式时，要用到\dfrac等命令，行与行之间有可能紧贴着，因此需要使用

   ```latex
   \[
   \mathbf{H}=
   \begin{bmatrix}
   	\dfrac{\partial^2 f}{\partial x^2} &
   	\dfrac{\partial^2 f}{\partial x \partial y} \\[8pt]
   	\dfrac{\partial^2 f}{\partial x \partial y} &
   	\dfrac{\partial^2 f}{\partial y^2}
   \end{bmatrix}
   \]
   ```

7. <img src="LaTeX.assets/image-20240106214407804.png" alt="image-20240106214407804" />


## 间距

1. 绝大部分时候，数学公式中各元素的间距是根据符号类型自动生成的，需要手动调整的情况极少。一般用命令\quad和\qquad生成间距。还可以使用\,、\:、\; 以及负间距\!。文本中的\␣ 也能使用在数学公式中。

   ```latex
   aa   %无额外间距
   
   a\,a %1个空格
   
   a\:a %1个空格
   
   a\;a %1个空格
   
   a\quad{}a  %4个空格
   
   a\qquad{}a %8个空格
   
   a\!a   %负1个空格
   ```

2. <img src="LaTeX.assets/image-20240106221522052.png" alt="image-20240106221522052" />

3. 常见的用途是在被积函数f(x)和dx之间增加一个微小的距离。注意微元里的d用的是直立体。

   ```latex
   \[
   \int_a^b f(x)\mathrm{d}x
   \qquad
   \int_a^b f(x)\,\mathrm{d}x
   \]
   ```

4. <img src="LaTeX.assets/image-20240106220746345.png" alt="image-20240106220746345" />

5. 另一个用途是生成多重积分号。如果我们直接连写两个\int，之间的间距将会过宽，此时可以使用负间距`\!`对其修正。不过amsmath提供了更方便的多重积分号，如二重积分\iint、三重积分\iiint等。

   ```latex
   \begin{gather*}
   	\int\int f(x)g(y)\diff x \diff y \\
   	\int\!\!\!\int f(x)g(y) \diff x \diff y \\
   	\iint f(x)g(y) \diff x \diff y \\
   	\iint \quad \iiint \quad \idotsint
   \end{gather*}
   ```


## 字体

1. LaTeX允许一部分数学符号切换字体，主要是拉丁字母、数字、大写希腊字母以及重音符号等。

2. 不同的数学字体往往带有不同的语义，如矩阵、向量等常会使用粗体或粗斜体，而数集常会使用\mathbb 表示。出于内容与格式分离以及方便书写的考虑，可以为它们定义新的命令：

   ```latex
   $\mathcal{R} \quad \mathfrak{R} \quad \mathbb{R}$
   \[
   \mathcal{L}= -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}
   \]
   $\mathfrak{su}(2)$ and $\mathfrak{so}(3)$ Lie algebra
   ```

3. <img src="LaTeX.assets/image-20240107155640483.png" alt="image-20240107155640483" />

4. 如果需要为所有的数学符号切换字体，则需要直接调用数学字体宏包。在xelatex或者lualatex编译命令下，还可以使用基于fontspec宏包的unicode-math宏包配置Unicode数学字体。

   ```latex
   \begin{align}
       \mathnormal{ABab12}\\
       \mathrm{ABab12}\\
       \mathit{ABab12}\\
       \mathbf{ABab12}\\
       \mathsf{ABab12}\\
       \mathtt{ABab12}\\
       \mathcal{AB}\\      %仅提供大写字母
       \mathcal{AB}\\      %eucal宏包，仅提供大写字母。这个命令和上一条一样，如果不使用eucal宏包，也不会报错。
       \mathscr{AB}\\      %mathrsfs宏包 仅提供大写字母
       \mathfrak{ABab12}\\ %amssymb或eufrak宏包
       \mathbb{AB}\\       %amssymb宏包，仅提供大写字母
   \end{align}
   ```

5. <img src="LaTeX.assets/image-20240107161015811.png" alt="image-20240107161015811" />

6. \mathbf命令只能获得直立、加粗的字母，对希腊字母没有效果。如果想得到粗斜体（一般用来表示矢量），可以使用amsmath宏包提供的\boldsymbol命令，也可以使用bm宏包提供的\bm命令：

   ```latex
   $\mu, M \qquad \boldsymbol{\mu}, \boldsymbol{M}$
   
   $\mu, M \qquad \bm{\mu}, \bm{M}$
   ```

7. <img src="LaTeX.assets/image-20240107161425393.png" alt="image-20240107161425393" />

8. 在LaTeX默认的数学字体中，一些符号本身并没有粗体版本，使用\boldsymbol也得不到粗体。此时\bm命令会生成“伪粗体”，尽管效果比较粗糙，但在某些时候也不失为一种解决方案。

9. 数学符号按照符号排版的位置规定尺寸，从大到小包括行间公式尺寸`\displaystyle`、行内公式尺寸`\textstyle`、上下标尺寸`\scriptstyle`、次级上下标尺寸`\scriptscriptstyle`。除了字号有别之外，行间和行内公式尺寸下的巨算符也使用不一样的大小。在分式中，分子分母默认为行内公式尺寸，下面代码将分母切换到行间公式尺寸，分子还是使用默认的行内公式尺寸：

   ```latex
   \[
   r = \frac{\sum_{i=1}^n (x_i- x)(y_i- y)}
   {\displaystyle \left[\sum_{i=1}^n (x_i-x)^2 \sum_{i=1}^n (y_i-y)^2 \right]^{1/2}}
   \]
   ```

10. <img src="LaTeX.assets/image-20240107162022794.png" alt="image-20240107162022794" />

11. \Alpha，\Beta等希腊字母符号不存在，因为它们和拉丁字母A，B等一模一样；小写希腊字母里也不存在
    \omicron，直接用拉丁字母o代替。

12. 所有的二元关系符都可以加\not前缀得到相反意义的关系符：

    ```latex
    $\not=\qquad\not\subset$
    ```

13. <img src="LaTeX.assets/image-20240107162915294.png" alt="image-20240107162915294" />


# 排版样式设定

## 字体

1. 英文中的typeface 和font一般都被翻译为字体，传统印刷业通常使用typeface，电脑字体通常使用font。

2. 电脑字体的诸多相关概念可以划分为三个层次：

   1. 编码层，字符(包括字母、数字、符号、控制码等) 的索引和编码，也就是字符集(character set) 和字符编码(character encoding) 。如何使用一个或多个字节表示一个字符，纯文本的形式。

   2. 格式层，字形(glyph) 的定义描述方法，以及字体的文件存储格式。

   3. 显示层，字体的外在表现形式，比如字体的样式，或具体的字体。

3. TeX使用字体比较复杂，这是因为Knuth当初设计TEX时，既没有Unicode字符集和UTF‐8编码，也没有TrueType和OpenType字体格式。

4. 最先是由ANSI发布了ASCII编码，7位。然后又扩展到了8位，这个被ISO标准化成了ISO-8859。由于欧洲国家的字符仅靠剩余的128个位置也不够存放，因此8859分为15个部分，每个部分只有0xA0-0xFF之间不同（后96个字符），前面部分都和ASCII相同。例如ISO 8859-1是西欧语言，也成为Latin-1。

5. 在ISO标准完全定型之前，IBM 就有一系列自己的字符编码，也就是代码页(code page) ，比如437 (扩展ASCII) 、850 (西欧语言) 、852 (东欧语言) 。IBM代码页通常被用于控制台(console) 环境，也就是MS‐DOS 或Unix Shell那样的命令行环境。

6. 微软将IBM 代码页称为OEM 代码页，自己定义的称为ANSI代码页，比如1252 (西欧语言)，1250 (东欧语言)，936 (GBK 简体中文)，950 (Big5 繁体中文)，932 (SJIS 日文)，949 (EUC‐KR 韩文) 等。

7. 电脑字体的数据格式可以分为三大类：点阵(bitmap) 字体、轮廓(outline)字体和笔画(stroke‐based) 字体。

   1. 点阵字体通过点阵来描述字形。早期的电脑受到容量和绘图速度的限制，多采用点阵字体。点阵字体后来渐渐被轮廓字体所取代，但是很多小字号字体仍然使用它，因为这种情况下轮廓字体缩放太多会导致笔画不清晰。

   2. 轮廓字体又称作矢量字体，它通过一组直线段和曲线来描述字形。轮廓字体易于通过数学函数进行缩放等变换，形成平滑的轮廓。轮廓字体的主要缺陷在于它所采用的贝塞尔曲线(Bézier curves) 在光栅设备(比如显示器和打印机) 上不能精确渲染，因而需要额外的补偿处理比如字体微调(font hinting) 。但是随着电脑硬件的发展，人们一般不在意它比点阵字体多出的处理时间。

   3. 笔画字体其实也是轮廓字体，不过它描述的不是完整的字形，而是笔画。它多用于东亚文字。

8. 当前常见的轮廓字体格式有：Type 1，TrueType，OpenType。也成为封装格式

   1. 1984年Adobe推出PostScript，同时支持两种字体格式：Type 1和Type 3，它们都采用三次贝塞尔曲线。

   2. 1991年苹果发布TrueType，它采用二次贝塞尔曲线。二次曲线处理起来比三次曲线快，但是需要更多的点来描述。从TrueType到Type 1的转换是无损的，反之是有损的。

   3. 1996 年微软和Adobe 联合发布了OpenType，它可以被认为是Type 1和TrueType的超集，既可使用二次曲线，也可使用三次曲线。平台独立、开放、易于开发，并且支持更多的语言比如阿拉伯语。

   4. 1984年Knuth发布了METAFONT，它与TrueType和OpenType的区别是，不直接描述字形轮廓，而描述生成轮廓的笔的轨迹。笔的形状可以是椭圆形或多边形，尺寸缩放自如，字形边缘也柔和一些。不过设计一款这样的字体需要的工作量太大，参数太多。

9. Type 1和Type 3把字体的尺寸(metrics)信息和字形(glyph)信息分别存储。

10. TrueType 和OpenType则将字体数据都存在一个文件里，它们的文件后缀分别是是.ttf 和.otf。

11. METAFONT虽然用矢量图形来定义字形，实际输出的却是一种点阵格式：PK (packed raster)。

12. 这些字体格式按照技术先进性，从高到低依次为：OpenType，TrueType，Type 1，Type 3，PK，所以要优先选用OpenType和TrueType。

13. PostScript文件可以包含Type 1和Type 3字体，而PDF除了这两种还支持TrueType和OpenType字体。

14. TeX的缺省字体是Knuth用METAFONT生成的Computer Modern；XeTeX的缺省字体是1997年AMS发布的Latin Modern，它基于Computer Modern，但是扩展了其字符集，其封装格式有Type 1和OpenType。

15. 各种字体样式及其常见字体：

    1. Windows
       1. 衬线字体：Times New Roman，Georgia，Palatino Linotype

       2. 无衬线字体：Tahoma，Verdana，Arial

       3. 等宽字体：Courier New，Lucida Console，Consolas

    2. macOS
       1. 衬线字体：Times，Georgia，Times New Roman

       2. 无衬线字体：Helvetica，Lucida Grande，Geneva

       3. 等宽字体：Monaco，Courier，Courier New

16. 早期的TeX只能使用METAFONT生成的字体。直到LaTeX2ε时代NFSS的出现后，Type 1和Type 3才在LaTeX中得到广泛应用。后起之秀XeTeX则极大程度地简化了TrueType和OpenType的配置，而且它还支持Unicode。

17. XeTeX可以直接使用电脑系统字体，不再需要TFM文件。首先需要知道电脑上有哪些字体，XeTeX用一个XML文件记录系统字体路径，MikTeX用的是localfonts.conf，TeXlive 用的是fonts.conf。

18. 设置字体时需要字体的引用名，它和字体的文件名是不同的概念。fc-list程序可以用来获取字体引用名。

    ```shell
    D:/texlive/2023/texmf-dist/fonts/opentype/public/fonts-tlwg/Norasi-Italic.otf: Norasi:style=Italic
    
    ```

19. 带XeTeX的发行包首次安装时会自动扫描这些字体目录，生成字体的缓存(cache) 。每次系统安装了新字体时，我们需要手工运行字体缓存命令`fc-cache -r`，生成新的缓存。

20. XeTeX提供的字体命令比较原始、繁琐。fontspec宏包提供了较好的封装。

32. LaTeX根据文档的逻辑结构（章节、脚注等）来选择默认的字体样式以及字号。

33. LaTeX2e相比于较早的LaTeX版本（2.09 版或更早）在字体样式和字号的设定上有很大改进，令字体的各种属性相互独立，用户可以改变字体的大小，而仍然保留字体原有的粗体或者斜体的特性。

34. 拉丁文字体主要有三大类：衬线字体(roman, serif) 、无衬线字体(sans serif)和等宽字体(monospace, typewriter) 。衬线字体笔画的边缘部分有些修饰，类似于中文的宋体、仿宋、楷体、魏体等。无衬线字体的笔画则是平滑的，类似于中文的黑体。

35. Sans这个词来源于法语，就是“没有”的意思。

36. 字体还可以有粗体(bold) 、斜体(italic) 、伪斜体(oblique, slanted) 、小型大写字母(small caps) 等修饰效果。TeX提供了介于正常字体和粗体之间的半粗体(medium weight)。

37. 斜体通常对原字体进行了重新设计，它修饰精细，多用于衬线字体；伪斜体基本上是把原字体倾斜，多用于无衬线字体，一般伪斜体看起来比斜体要宽一些。小型大写字母的形状和大写字母相同但尺寸较小，一般高度和小写字母相似。

38. 每种字体样式包含很多种具体的字体。

39. LaTeX 提供了两组等效的修改字体的命令。

    1. 类似`\textbf{<sometext>}`只改变`{}`内部的字体，较为常用。

    2. 类似`\bfseries`形式的命令，将会影响之后所有的字符，如果想要让它在局部生效，需要使用分组，也就是`{\bfseries ⟨sometext⟩}`的形式；

       ```latex
       \textrm{roman} %衬线字体（罗马体）  \rmfamily
       
       \textsf{sans serif} %无衬线字体    \sffamily
       
       \texttt{typewriter} %等宽字体      \ttfamily
       
       \textmd{medium} %正常粗细（中等）   \mdseries
       
       \textbf{bold face} %粗体           \bfseries
       
       \textup{upright} %直立体           \upshape
       
       \textit{italic} %意大利斜体        \itshape
       
       \textsl{slanted} %倾斜体           \slshape
       
       \textsc{SMALL CAPS} %小型大写字母   \scshape
       
       \emph{emphasized} %强调，默认是斜体   \em
       
       \textnormal{normal font} %默认字体  \normalfont
       ```

    3. ![image-20240107164253672](LaTeX.assets/image-20240107164253672.png)

40. 在公式中，直接使用\textbf等命令不会起效，甚至报错。LaTeX 提供了修改数学字母样式的命令，如\mathbf等。

41. 字号命令实际大小依赖于所使用的文档类及其选项。下面是它们在标准文档类中的绝对大小，单位为pt。使用字号命令的时候，通常也需要用花括号进行分组，如同\rmfamily那样。

   ```latex
   字号              10pt      11pt      12pt
                  (文档类默认)
   \tiny             5pt       6pt       6pt
   \scriptsize       7pt       8pt       8pt
   \footnotesize     8pt       9pt       10pt
   \small            9pt       10pt      10.95pt
   \normalsize       10pt      10.95pt   12pt
   \large            12pt      12pt      14.4pt
   \Large            14.4pt    14.4pt    17.28pt
   \LARGE            17.28pt   17.28pt   20.74pt
   \huge             20.74pt   20.74pt   24.88pt
   \Huge             24.88pt   24.88pt   24.88pt
   %例子
   He likes {\LARGE large and {\small small} letters}.
   ```

11. ![image-20240107164530728](LaTeX.assets/image-20240107164530728.png)

12. LaTeX还提供了一个基础的命令`\fontsize`用于设定任意大小的字号和对应的行距：

    ```latex
    \fontsize{⟨size⟩}{⟨base line-skip⟩}  %size为字号，base line-skip为基础行距
    ```

13. 上面的10个命令在设置字号的同时，也设定了与字号对应的基础行距，大小为字号的1.2倍。

14. 如果不是在导言区，\fontsize的设定需要\selectfont命令才能立即生效，而上面的10个命令都是立即生效的。

15. LaTeX默认的字体是由高德纳设计制作的Computer Modern字体。可以使用字体宏包来完成整套配置，在调用宏包之后，照常使用\bfseries或\ttfamily等我们熟悉的命令。

16. xelatex和lualatex命令能够支持直接调用系统和TEX发行版中的.ttf或.otf格式字体。相比于上面的字体宏包，这种方式更自由。需要使用fontspec宏包。提供了几个设置全局字体的命令，设置\rmfamily等对应命令的默认字体。

    ```latex
    %旧版本fontspec宏包的命令把必选参数⟨font name⟩放在可选参数⟨font features⟩的后面。新版本目前兼容旧版本的用法，但推荐使用新版本的用法。
    \setmainfont{⟨font name⟩}[⟨font features⟩] %font name为字体的文件名（带扩展名）或者字体的英文名称。font feature用来手动配置粗体或斜体。通常情况下会自动检测并配置，无需手动指定。
    \setsansfont{⟨font name⟩}[⟨font features⟩]
    \setmonofont{⟨font name⟩}[⟨font features⟩]
    %下面的例子设置无衬线字体为Arial，同时配置其对应的粗体和斜体。
    \setsansfont{Arial}[BoldFont={Arial Bold}, ItalicFont={Arial Italic}]
    ```

17. fontspec宏包会覆盖数学字体设置。需要调用表5.4 中列出的一些数学字体宏包时，应当在调用fontspec宏包时指定no-math选项。fontspec宏包可能被其它宏包或文档类（如ctex文档类）自动调用时，则可以在文档开头的\documentclass命令里指定no-math选项。

18. ctex宏包或文档类提供了和fontspec宏包非常类似的语法设置中文字体：

    ```latex
    \setCJKmainfont{⟨font name⟩}[⟨font features⟩] %使用xelatex编译时，这几个命令实际上由xeCJK宏包提供
    \setCJKsansfont{⟨font name⟩}[⟨font features⟩]
    \setCJKmonofont{⟨font name⟩}[⟨font features⟩]
    %由于中文字体少有对应的粗体或斜体，⟨font features⟩里多用其他字体来配置，比如下面例子就是设定基本字体为宋体，并设定对应的BoldFont为黑体，ItalicFont为楷体：
    \setCJKmainfont{SimSun}[BoldFont=SimHei, ItalicFont=KaiTi]
    ```

19. 使用\setxxxfont和\setCJKxxxfont可以分别设置英文和中文的字体。

20. 英文的字体对应的斜体是需要另外开发绘制的，不是计算的来的。不是所有的字体都有对应开发的粗体，例如EB Garamond。此时可以使用伪粗体代替。

21. 在xelatex或者lualatex命令下，使用unicode-math宏包可以调用Unicode数学字体配置数学公式的字体风格。Unicode 数学字体相比于正文字体的选择余地不多。

    ```latex
    \setmathfont{⟨font name⟩}[⟨font features⟩] %绝大多数时候，只需要给定字体名称⟨font name⟩ 即可
    %常见的Unicode数学字体
    数学字体名称            配套正文字体名称     备注
                         %开源字体，发布于CTAN
    Latin Modern Math       Latin Modern       基于Computer Modern 风格
    STIX Math                  STIX            Times 风格
    XITS Math                  XITS            基于STIX，Times 风格，有粗体XITS Math Bold可用
    TeX Gyre Pagella Math   TeX Gyre Pagella   Palatino 风格
    TeX Gyre Termes Math    TeX Gyre Termes    Times 风格
    TeX Gyre DejaVu Math     DejaVu Serif      DejaVu 风格
    Libertinus Math          Libertinus        Linux Libertine 风格
    Garamond Math            EB Garamond       Garamond 风格
    Fira Math                  Fira            Sans 无衬线数学字体
                             %商业字体
    Cambria Math              Cambria          微软Office 预装的数学字体
    Lucida Bright Math OT   Lucida Bright OT   须购买商业授权
    Minion Math              Minion Pro        须购买商业授权
    ```

22. unicode-math宏包与传统数学字体、符号包并不兼容，但其本身已经提供了大量的符号和字体样式。实际上，`\mathrm`系列命令和加粗命令均已被unicode-math所涵盖，无需调用其他宏包就可以获得覆盖完整、风格较为统一的字体样式。


## 下划线

1. 使用\underline命令用来为文字添加下划线，此方法无法断行，且不同的单词可能生成高低各异的下划线，不够美观。可以使用ulem宏包中的\uline来解决问题。

   ```latex
   An example of \uline{some long and underlined words.}
   
   An example of \underline{some long and underlined words.}
   ```

2. ![image-20240108192109757](LaTeX.assets/image-20240108192109757.png)

3. 可以使用\emph命令将文字变成斜体以示强调，如果在已强调的文字中嵌套使用\emph，则会还原成直立体。

   ```latex
   Some \emph{emphasized words, including \emph{double-emphasized} words}, are shown here.
   ```

4. ![image-20240108192450344](LaTeX.assets/image-20240108192450344.png)

5. 如果使用了ulem宏包，\emph命令会变为下划线，嵌套使用，则表示双下划线。

   ```latex
   %我们可以在引用宏包时可以加个选项改回去
   \usepackage[normalem]{ulem} %不修改\emph的含义
   ```

6. 中文下划线：

   ```latex
   \usepackage{ulem}
   \usepackage{CJKfntef}
   \begin{document}
   \uline{中文 ABC 123}  \CJKunderline{中文 ABC 123}
   
   \uuline{中文 ABC 123} \CJKunderdot{中文 ABC 123}
   
   \uwave{中文 ABC 123}  \CJKunderwave{中文 ABC 123}
   
   \sout{中文 ABC 123}   \CJKsout{中文 ABC 123}
   \end{document}
   ```

7. ![image-20240108193004906](LaTeX.assets/image-20240108193004906.png)


## 长度

1. 长度和长度变量，长度的数值⟨length⟩由数字和单位组成。常见的单位有：

   ```latex
   pt %点(point，也译作“磅”)，1pt = 1/72.27 in
      %point是个传统印刷业采用的单位，而big point是Adobe推出PostScript时定义的新单位
   bp %大点(big point)，1bp = 1/72 in
   in %英寸，1in = 2.54cm
   cm %厘米
   mm %毫米
   em %大致相当于当前字号下大写字母M的宽度，常用于设定水平距离。相对单位，比如当前字体是11pt时，1em就是11pt
   ex %大致相当于当前字号下小写字母x的高度，常用于设定垂直距离
   mu %数学单位(math unit)，1mu = 1/18 em
   ```

2. 在一些情况下还会用到可伸缩的“弹性长度”，如12pt plus 2pt minus 3pt 表示基础长度为12pt，可以伸展到14pt，也可以收缩到9pt。也可只定义plus 或者minus 的部分，如0pt plus 5pt。

3. 长度的数值还可以用长度变量本身或其倍数来表达，如`2.5\parindent`等。LaTeX预定义了大量的长度变量用于控制版面格式。如页面宽度和高度、首行缩进、段落间距等。如果需要自定义长度变量，需使用如下命令：

   ```latex
   \newlength{\⟨length command⟩} %创建一个新的长度变量，可以用在需要长度的地方。
   ```

4. 长度变量可以用\setlength赋值，或用\addtolength增加长度：

   ```latex
   \setlength{\⟨length command⟩}{⟨length⟩} %修改长度变量的具体数值，例如\setlength{\leftskip}{5em} 设置左缩进为5em
   \addtolength{\⟨length command⟩}{⟨length⟩}
   ```


## 行距，缩进

1. 之前提到可以使用`\fontsize`命令修改字号及行距，但是很少这么做，更常用的方法是在导言区用\linespread命令设置行距系数，这样会全局修改。

   ```latex
   \linespread{⟨factor⟩}  %<factor>表示实际行距是基础行距的倍数，默认的基础行距为字号大小的1.2倍。因此当factor=1.5时，则最终行距为1.5*1.2=1.8倍字号大小。<factor>默认为1，及1.2倍行距
   ```

2. \linespread命令不仅会改变正文行距，同时也把目录、脚注、图表标题等的行距给改了。如果只想改正文行距，可以使用setspace宏包的行距命令。

   ```latex
   \usepackage{setspace}
   ...
   \singlespacing %单倍行距
   \onehalfspacing %一倍半行距
   \doublespacing %双倍行距
   \setstretch{1.25} %任意行距
   ```

3. 上述行距命令对全文的行距都会产生影响，setspace宏包还提供了singlespacing，onehalfspacing，doublespacing等环境，可以用来设置局部文字的行距。

   ```latex
   \begin{doublespacing}
   double\\spacing
   \end{doublespacing}
   
   \begin{spacing}{1.25}
   any\\spacing
   \end{spacing}
   ```

4. 如果只想要局部地改变某个段落的行距，需要用\selectfont命令使\linespread命令的改动立即生效。可以使用分组来使之局部生效。字号的改变是即时生效的，而行距的改变直到文字分段时才生效。不过需要注意下面分段的细节：

   ```latex
   %这样会分为两段，各自行距不一样。
   {\linespread{2.0}\selectfont{}The baseline skip is set to be twice the normal baseline skip. Pay attention to the \verb|\par| command at the end.\par}
   In comparison, after the curly brace has been closed, everything is back to normal.
   %这样会分为2段，但是行距都是默认的。这种写法和将第一段的\par放在{}外效果是等价的。
   {\linespread{2.0}\selectfont{}The baseline skip is set to be twice the normal baseline skip. Pay attention to the \verb|\par| command at the end.}
   
   In comparison, after the curly brace has been closed, everything is back to normal.
   ```

5. 以下长度分别为段落的左缩进、右缩进和首行缩进，它们和设置行距的命令一样，在分段时生效：

   ```latex
   \setlength{\leftskip}{⟨length⟩}  %length可以直接给定长度，也可以给定长度变量
   \setlength{\rightskip}{⟨length⟩}
   \setlength{\parindent}{⟨length⟩}
   ```

6. LaTeX默认在段落开始时缩进，长度为`\parindent`。如果需要在某一段不缩进，可在段落开头使用\noindent命令。相反地，\indent命令强制开启一段首行缩进的段落。在段落开头使用多个\indent命令可以累加缩进量。

7. 控制段落缩进的命令为：

   ```latex
   \indent
   \noindent
   ```

8. LaTeX还默认在\chapter、\section等章节标题命令之后的第一段不缩进。如果不习惯这种设定，可以调用indentfirst宏包，令第一段的首行缩进照常。不过ctex宏包和文档类默认按照中文习惯保持标题后第一段的首行缩进，不用修改。

# 垂直，水平间距

1. 段落间的垂直间距为`\parskip`长度变量，也就是段前段后的间距：

   ```latex
   \setlength{\parskip}{1ex plus 0.5ex minus 0.2ex} %设置段落间距在0.8ex到1.5ex 间变动。
   ```

2. LaTeX默认为将单词之间的“空格”字符转化为水平间距。如果需要在文中手动插入额外的水平间距，可使用\hspace命令：

   ```latex
   This\hspace{1.5cm}is a space of 1.5 cm.
   ```

3. ![image-20240109163220981](LaTeX.assets/image-20240109163220981.png)

4. 使用\hspace命令生成的水平间距如果位于一行的开头或末尾，则有可能因为断行而被舍弃。可使用`\hspace*`命令代替以得到不会因断行而消失的水平间距。

5. 命令`\stretch{⟨n⟩}`可以生成一个特殊弹性长度，n为权重。它的基础长度为0pt，但可以无限延伸，直到占满可用的空间。如果同一行内出现多个弹性长度，这一行的所有可用空间将按他们权重⟨n⟩进行分配。

   ```latex
   x\hspace{\stretch{1}}x\hspace{\stretch{3}}x\hspace{\fill}x  %这里嵌套使用了长度变量，因为\stretch的结果是一个长度变量。
   %命令\fill相当于\stretch{1}。
   ```

6. ![image-20240109163725762](LaTeX.assets/image-20240109163725762.png)

7. 在正文中用`\hspace`命令生成水平间距时，往往使用em作为单位，这样生成的间距随字号大小而变。

8. 我们在数学公式中使用过的\quad和\qquad命令，也可以用于文本中，分别相当于\hspace{1em} 和\hspace{2em}。

9. 在页面中，段落、章节标题、行间公式、列表、浮动体等元素之间的间距是LaTeX预设的。比如\parskip，默认设置为0pt plus 1pt。如果想要人为地增加段落之间的垂直间距，可以在两个段落之间的位置使用\vspace命令：

   ```latex
   A paragraph.
   
   Another paragraph.
   
   \vspace{2ex}
   Another another paragraph.
   ```

10. ![image-20240109164541717](LaTeX.assets/image-20240109164541717.png)

11. \vspace命令生成的垂直间距在一页的顶端或底端可能被“吞掉”，这和\hspace一样。因此也有\vspace* 命令产生不会因断页而消失的垂直间距。\vspace也可使用\stretch设置无限延伸的垂直长度。

12. 在同一段落内的两行之间增加垂直间距，可以使用`\\[6pt]`或`\\*[6pt]`。\vspace也可以在段落内使用，区别在于\vspace只引入垂直间距而不断行。

    ```latex
    Use command \verb|\vspace{12pt}| to add \vspace{12pt} some spaces between lines in a paragraph. But the next line will be the old space. This is different with Word. As you can see.
    
    Or you can use \verb|\\[12pt]| to \\[12pt] add vertical space, but it also breaks the line.
    ```

13. ![image-20240109165806928](LaTeX.assets/image-20240109165806928.png)

14. word不支持同一段内的指定两行增加间距，只能统一调整该段内所有行的间距。word内一般不会手动断行。


## 页边距

1. 控制页边距的参数由下图里给出的各种长度变量控制。可以用\setlength命令修改这些长度变量，以达到调节页面尺寸和边距的作用。反之也可以利用这些长度变量来决定排版内容的尺寸，如在tabularx环境或\includegraphics命令的参数里，设置图片或表格的宽度为0.8\textwidth。

   ```latex
   \textwidth %正文宽度
   \textheight %正文高度
   \paperwidth %纸张宽度=左边距+正文宽度+右边距
   \paperheight %纸张高度=上边距+正文高度+下边距
   ```

2. 不过不推荐直接设置这些长度变量。可以geometry宏包来简易设置页边距。用其提供的\geometry命令设置页面参数：

   ```latex
   \usepackage{geometry}
   \geometry{⟨geometry-settings⟩}  %⟨geometry-settings⟩以⟨key⟩=⟨value⟩的形式组织
   %也可以直接在宏包选项中设置：
   \usepackage[⟨geometry-settings⟩]{geometry}
   %例如Word默认的页面设定是A4纸张，上下边距1英寸，左右边距1.25英寸。
   \geometry{a4paper,left=1.25in,right=1.25in,top=1in,bottom=1in}
   \geometry{a4paper,hmargin=1.25in,vmargin=1in} %效果同上，h为horizontal，v为vertical
   \geometry{margin=1.25in} %上下左右的边距都是1.25in
   ```

3. 对于书籍等双面文档，习惯上奇数页在右手边、偶数页在左手边，一般外侧的页边距较大，而靠近书脊的页边距较小。我们可以这样设定：

   ```latex
   \geometry{inner=1in,outer=1.25in}
   ```

4. 通过geometry 宏包设置的纸张大小是输出PDF文件的真实大小，而在文档类选项中设置的参数实际上只影响输出区域。

5. LaTeX默认将页面内容在垂直方向分散对齐。对于有大量图表的文档，许多时候想要做到排版匀称的页面很困难，垂直分散对齐会造成某些页面的垂直间距过宽，还可能报大量的Underfull \vbox警告。LaTeX还提供了另一种策略：将页面内容向顶部对齐，给底部留出高度不一的空白。

   ```latex
   \raggedbottom %页面在垂直方向上向顶部对齐
   \flushbottom  %页面在垂直方向分散对齐
   ```


## 双栏

1. LaTeX支持简单的单栏或双栏排版。标准文档类的全局选项onecolumn、twocolumn可控制全文分单栏或双栏排版。LaTeX也提供了切换单/双栏排版的命令：

   ```latex
   \onecolumn
   \twocolumn[⟨one-column top material⟩] %可选参数是用于排版双栏之上的一部分单栏内容。
   ```

2. 切换单/双栏排版时总是会另起一页（\clearpage）。在双栏模式下使用\newpage会换栏而不是换页；\clearpage才能够换页。

3. 双栏排版时每一栏的宽度为\columnwidth，它由\textwidth减去\columnsep的差除以2得到。两栏之间还有一道竖线，宽度为\columnseprule，默认为零，也就是看不到竖线。

4. 一个比较好用的分栏解决方案是multicol，它提供了简单的multicols环境（注意不要写成multicol环境）自动产生分栏，如以下环境将内容分为3栏：

   ```latex
   \begin{multicols}{3}
   	...
   \end{multicols}
   ```

5. multicol宏包能够在一页之中切换单栏/多栏，也能处理跨页的分栏，且各栏的高度分布平衡。但代价是在multicols环境中无法正常使用table和figure等浮动体环境，它会直接让浮动体丢失。multicols环境中只能用跨栏的table* 和figure* 环境，或者用float宏包提供的H参数固定浮动体的位置。


## 页眉页脚

1. LaTeX中提供了如下命令来修改页眉页脚的样式：

   ```latex
   \pagestyle{⟨page-style⟩} %所有页面
   \thispagestyle{⟨page-style⟩} %只影响当页的页眉页脚样式。参数为样式的名称，在LaTeX里预定义了四类样式：
   empty %页眉页脚为空
   plain %页眉为空，页脚为页码。(article和report文档类默认；book文档类的每章第一页也为plain格式)
   headings %页眉为章节标题和页码，页脚为空。(book文档类默认)
   myheadings %页眉为页码及\markboth和\markright命令手动指定的内容，页脚为空。
   ```

2. 常用文档类及选项的样式：

   1. article文档类，twoside选项：偶数页为页码和节标题，奇数页为小节标题和页码；

   2. article文档类，oneside：选项页眉为节标题和页码；

   3. report和book文档类，twoside选项：偶数页为页码和章标题，奇数页为节标题和页码；

   4. report和book文档类，oneside选项：页眉为章标题和页码。

3. 改变页眉页脚中的页码样式：

   ```latex
   \pagenumbering{⟨style⟩} %⟨style⟩为页码样式，默认为arabic(阿拉伯数字)，还可修改为roman(小写罗马数字)、Roman(大写罗马数字)等。
   ```

4. 注意使用`\pagenumbering`命令后会将页码重置为1。book文档类的`\frontmatter`和`\mainmatter`内部就使用了`\pagenumbering`命令切换页码样式。

5. 对于headings或者myheadings样式，LaTeX允许用户使用命令手动修改页眉上面的内容，特别是因为使用了`\chapter*`等命令而无法自动生成页眉页脚的情况：

   ```latex
   \markright{⟨right-mark⟩}
   \markboth{⟨left-mark⟩}{⟨right-mark⟩}
   ```

6. 在双面排版、headings或myheadings页眉页脚样式下，⟨left-mark⟩和⟨right-mark⟩的内容分别预期出现在左页（偶数页）和右页（奇数页）上。

7. 事实上\chapter和\section等章节命令内部也使用\markboth或者\markright生成页眉。LaTeX默认将页眉的内容都转为大写字母。如果需要保持字母的大小写，可以使用如下代码：

   ```latex
   \renewcommand\chaptermark[1]{\markboth{Chapter \thechapter\quad #1}{}}
   \renewcommand\sectionmark[1]{\markright{\thesection\quad #1}}
   %其中\thechapter、\thesection等命令为章节计数器的数值
   %注意以上代码适用于report和book文档类；对于article文档类，与两个页眉相关的命令分别为\sectionmark和\subsectionmark。
   ```

8. fancyhdr宏包改善了页眉页脚样式的定义方式，允许我们将内容自由安置在页眉和页脚的左、中、右三个位置，还为页眉和页脚各加了一条横线。

9. fancyhdr宏包自定义了样式名称fancy。通常先用\pagestyle{fancy}调用这个样式。在fancyhdr中定义页眉页脚的命令为：

   ```latex
   \fancyhf[⟨position⟩]{…} %⟨position⟩为L(左)/C(中)/R(右)以及与O(奇数页)/E(偶数页)字母的组合
   \fancyhead[⟨position⟩]{…} %单独设定页眉
   \fancyfoot[⟨position⟩]{…} %单独设定页脚
   ```

10. 例子：

    ```latex
    % 在导言区使用此代码
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \renewcommand{\chaptermark}[1]{\markboth{#1}{}}
    \renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}
    \fancyhf{}
    \fancyfoot[C]{\bfseries\thepage}%设置页脚，居中加粗显示页码
    \fancyhead[LO]{\bfseries\rightmark}
    \fancyhead[RE]{\bfseries\leftmark}
    \renewcommand{\headrulewidth}{0.4pt} % 设置页眉横线的宽度，注意不用\setlength
    \renewcommand{\footrulewidth}{0pt} %“去掉”页脚的横线
    %效果为将章节标题放在和headings一致的位置，但使用加粗格式；
    
    \fancyhead[L,C]{}
    \fancyhead[R]{\textbf{The performance of new graduates}}
    \fancyfoot[L]{From: K. Grant}
    \fancyfoot[C]{To: Dean A. Smith}
    \fancyfoot[R]{\thepage}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{2pt}
    ```

11. ![image-20240110210228077](LaTeX.assets/image-20240110210228077.png)

12. fancyhdr宏包还支持用\fancypagestyle为自定义的页眉页脚样式命名，或者重新定义已有的样式如plain等：

    ```latex
    % 自定义myfancy样式
    \fancypagestyle{myfancy}{
        \fancyhf{}
        \fancyhead{...}
        \fancyfoot{...}
    }
    % 使用样式
    \pagestyle{myfancy}
    ```

# 参考文献

1. LaTeX提供的参考文献和引用方式比较原始，需要用户自行书写参考文献列表（包括格式），因此较难直接使用。最基本的\cite命令用于在正文中引用参考文献：

   ```latex
   \cite{⟨citation⟩} %⟨citation⟩为引用的参考文献的标签，类似\ref里的参数；
   %可以有一个可选参数，为正文中引用的编号后加上额外的内容，如\cite[page 22]{Paper2013}可能得到形如[13, page 22]这样的引用。
   ```

2. 参考文献由thebibliography环境包裹。每条参考文献由\bibitem 开头，其后是参考文献本身的内容：

   ```latex
   \begin{thebibliography}{⟨widest label⟩}
       \bibitem[⟨item number⟩]{⟨citation⟩} ...
   \end{thebibliography}
   %⟨citation⟩ 是\cite所使用的文献标签。
   %⟨item number⟩ 自定义参考文献的序号，如果省略，则按自然排序给定序号。
   %⟨widest label⟩ 用以限制参考文献序号的宽度，如99意味着不超过两位数字。通常设定为与参考文献的数目一致。
   ```

3. 在article文档类，thebibliography环境会自动生成不带编号的一节，标题默认为“References”；而在report或book文档类中，则会生成不带编号的一章，标题默认为“Bibliography”。

4. 例子：

   ```latex
   \documentclass{article}
   \begin{document}
   \section{Introduction}
   Partl~\cite{germenTeX} has proposed that \ldots
   \begin{thebibliography}{99}
   	\bibitem{germenTeX} H.~Partl: \emph{German \TeX},TUGboat Volume~9, Issue~1 (1988)
   \end{thebibliography}
   \end{document}
   ```

5. ![image-20240110224028374](LaTeX.assets/image-20240110224028374.png)

6. BIBTEX是最为流行的参考文献数据组织格式之一。它的出现让我们摆脱手写参考文献条目的麻烦。我们还可以通过参考文献样式的支持，让同一份BIBTEX数据库生成不同样式的参考文献列表。BIBTEX数据库以.bib作为扩展名，其内容是若干个文献条目，每个条目的格式为：

   ```latex
   @⟨type⟩{⟨citation⟩, %⟨type⟩为文献的类别，如article为学术论文，book为书籍，incollection为论文集中的某一篇。⟨citation⟩为\cite命令所使用的文献标签。
   ⟨key1⟩ = {⟨value1⟩}, %键值对的形式，记录本条文献的属性。
   …
   }
   %例子
   @article{Alice13,
   title = {Demostration of bibliography items},
   author = {Alice Axford and Bob Birkin and Charlie Copper and Danny Dannford},
   year = {2013},
   month = {Mar},
   journal = {Journal of \TeX perts},
   volume = {36},
   number = {7},
   pages = {114-120}}
   ```

7. 常用的文献类别：

   ```latex
   article %学术论文，必需字段有author,title,journal,year;可选字段包括volume,number,pages,doi等；
   book %书籍，必需字段有author/editor,title,publisher,year;可选字段包括volume/number, series,address等；
   incollection %论文集中的一篇，必需字段有author,title,booktitle,publisher,year;可选字段包括editor,volume/number,chapter,pages,address等；
   inbook %书中的一章，必需字段有author/editor,title,chapter/pages,publisher,year;可选字段包括volume/number,series,address等。
   ```

8. 多数时候，我们无需自己手写BIBTEX文献条目。从Google Scholar或者期刊/数据库的网站上都能够导出BIBTEX文献条目，老牌的文献管理软件EndNote 也支持生成BIBTEX 格式的数据库。开源软件JabRef甚至支持BIBTEX文献条目的导入、导出和管理。

9. BIBTEX用样式（style）来管理参考文献的写法。BIBTEX预定义的样式，如plain，unsrt，alpha等。也可以使用期刊提供的样式，样式文件以.bst为扩展名。一些文档类也提供自带的样式。

10. 使用样式文件：在源代码内（一般在导言区）使用如下命令：

    ```latex
    \bibliographystyle{⟨bst-name⟩} %参数为样式文件名，不带.bst后缀。
    ```

11. BIBTEX程序在生成参考文献列表时，通常只列出用了\cite命令引用的那些。如果需要列出某个未被引用的文献，则需要`\nocite{⟨citation⟩}`命令；而`\nocite{*}`则列出所有未被引用的文献。

12. 在需要列出参考文献的位置，使用\bibliography命令代替thebibliography环境：

    ```latex
    \bibliography{⟨bib-name⟩} %bib-name是数据库的文件名，不带.bib后缀。
    ```

13. 注意\bibliographystyle和\bibliography命令缺一不可，否则使用BIBTEX生成参考文献列表的时候会报错。

14. 编译步骤，如果使用TexStudio，则需要手动指定命令运行：

    ```shell
    #首先使用pdflatex或xelatex等命令编译LaTeX源代码demo.tex；
    xelatex demo
    #接下来用bibtex命令处理demo.aux辅助文件记录的参考文献格式、引用条目等信息。bibtex命令处理完毕后会生成demo.bbl文件，内容就是一个thebibliography环境；
    bibtex demo
    #再使用pdflatex或xelatex等命令把源代码demo.tex编译两遍，读入参考文献并正确生成引用。
    xelatex demo
    xelatex demo
    ```

15. 一些学术期刊比较喜欢使用人名—年份的引用方式，形如`(Axford et al., 2013)`。natbib宏包提供了对这种“自然”引用方式的处理。除了\cite之外，natbib宏包在正文中支持两种引用方式：

    ```latex
    \citep{⟨citation⟩} %结果样式为：(Axford et al., 2013)
    \citet{⟨citation⟩} %结果样式为：Axford et al. (2013)
    ```

16. 正确排版人名—年份引用还依赖于特定的BIBTEX样式。natbib提供了与LaTeX预定义样式相对应的几个样式，包括plainnat、abbrvnat和unsrtnat。学术论文模板是否支持natbib，需要参考其帮助文档。

17. natbib宏包同样也支持数字引用，并且支持将引用的序号压缩：

    ```latex
    \usepackage[numbers,sort&compress]{natbib} %指定左侧选项后，连续引用多篇文献时，会生成形如(3–7)的引用而不是(3,4, 5, 6, 7)。
    ```

18. natbib默认的引用是用小括号包裹的，可指定square选项改为中括号；\citep命令支持可选参数，为引用前后都添加额外内容。

19. biblatex 宏包是一套基于LaTeX宏命令的参考文献解决方案，提供了便捷的格式控制和强大的排序、分类、筛选、多文献表等功能。因其对UTF-8和中文参考文献的良好支持，被国内较多LaTeX模板采用。

# 索引

1. 书籍和大文档通常用索引来归纳关键词，方便用户查阅。LaTeX借助配套的makeindex程序完成对索引的排版。

2. 使用索引的步骤：

   1. 在LaTeX源代码的导言区调用makeidx宏包，并使用\makeindex命令开启索引的收集

      ```latex
      \usepackage{makeidx}
      \makeindex
      ```

   2. 在正文中需要索引的地方使用\index命令。

   3. 最后在需要输出索引的地方(如所有章节之后)使用\printindex命令。

   4. 编译过程：

      1. 首先用xelatex等命令编译源代码demo.tex。编译过程中产生索引记录文件demo.idx；
      2. 用makeindex程序处理demo.idx，生成用于排版的索引列表文件demo.ind；
      3. 再次编译源代码demo.tex，正确生成索引列表。

3. 添加索引项的命令为：

   ```latex
   \index{⟨index entry⟩} %index entry为索引项
   %其中!@|为特殊符号，如果要向索引项直接输出这些符号，需要加前缀"；而"需要输入两个引号""才能输出到索引项。
   ```

# 颜色

1. 原始的LaTeX不支持使用各种颜色。color宏包或者xcolor宏包提供了对颜色的支持，给PDF输出生成颜色的特殊指令。

2. 调用color或xcolor宏包后，我们就可以用如下命令切换颜色，颜色的表达方式有两种：

   ```latex
   %一是使用色彩模型和色彩代码，代码用0到1的小数代表成分的比例。color宏包支持rgb、cmyk和gray模型，xcolor支持更多的模型如hsb等。
   \color[⟨color-mode⟩]{⟨code⟩}
   %二是直接使用名称代表颜色，前提是已经定义了颜色名称（没定义的话会报错）。
   \color{⟨color-name⟩}
   %例子
   \large
   {\color[gray]{0.6}60\%灰色}
   {\color[rgb]{0,1,1}青色}
   
   \large
   {\color{red} 红色}
   {\color{blue} 蓝色}
   ```

3. ![image-20240110235213018](LaTeX.assets/image-20240110235213018.png)

4. color宏包仅定义了8 种颜色名称，xcolor补充了一些，总共有19种：

5. ![image-20240111002421167](LaTeX.assets/image-20240111002421167.png)

6. 还可以通过命令自定义颜色名称：

   ```latex
   \definecolor{⟨color-name⟩}{⟨color-mode⟩}{⟨code⟩} %这里的⟨color-mode⟩ 是必选参数
   ```

7. 原始的\color命令类似于字体命令\bfseries，它使之后排版的内容全部变成指定的颜色，所以直接使用时通常要加花括号分组。color 和xcolor宏包都定义了一些方便用户使用的带颜色元素。

   ```latex
   \textcolor[⟨color-mode⟩]{⟨code⟩}{⟨text⟩} %输入带颜色的文本
   \textcolor{⟨color-name⟩}{⟨text⟩}
   
   \colorbox[⟨color-mode⟩]{⟨code⟩}{⟨material⟩} %构造一个带背景色的盒子
   \colorbox{⟨color-name⟩}{⟨material⟩}
   
   \fcolorbox[⟨color-mode⟩]{⟨fcode⟩}{⟨code⟩}{⟨material⟩} %构造一个带背景色和有色边框的盒子，⟨fcode⟩或⟨fcolor-name⟩用于设置边框颜色。
   \fcolorbox{⟨fcolor-name⟩}{⟨color-name⟩}{⟨material⟩}
   ```

8. 例子：

   ```latex
   文字用\textcolor{red}{红色}强调
   
   \colorbox[gray]{0.95}{浅灰色背景}
   
   \fcolorbox{blue}{yellow}{\textcolor{blue}{蓝色边框+文字，黄色背景}
   ```

9. ![image-20240110235108980](LaTeX.assets/image-20240110235108980.png)


# 超链接

1. 电子文档最实用的需求之一就是超链接功能。LaTeX中实现这一功能的是hyperref宏包。

2. hyperref 宏包涉及的链接遍布LaTeX的每一个角落—目录、引用、脚注、索引、参考文献等等都被封装成超链接。但这也使得它与其它宏包发生冲突的可能性大大增加，虽然宏包已经尽力解决各方面的兼容性，但仍不能面面俱到。为减少可能的冲突，习惯上将hyperref宏包放在其它宏包之后调用。

3. hyperref 宏包提供了命令\hypersetup来配置各种参数。参数也可以作为宏包选项，在调用宏包时指定：

   ```latex
   \hypersetup{⟨option1⟩,⟨option2⟩=⟨value⟩,…} %当选项值为true时，可以省略=true不写。
   \usepackage[⟨option1⟩,⟨option2⟩=⟨value⟩,…]{hyperref}
   ```

4. 选项：

   ```latex
   参数                   默认值   含义 
   draft=⟨true|false⟩      false   %是否关闭所有超链接、书签等功能（也可以通过文档类选项指定）
   final=⟨true|false⟩      true    %开启所有超链接、书签等功能（也可以通过文档类选项指定）
   
   colorlinks=⟨true|false⟩ false   %设置为true为链接文字带颜色，反之加上带颜色的边框
   hidelinks                      %取消链接的颜色和边框
   pdfborder={⟨n⟩ ⟨n⟩ ⟨n⟩}  0 0 1   %超链接边框设置，设为0 0 0 可取消边框
   
   bookmarks=⟨true|false⟩  true    %是否生成书签，只能用作宏包选项
   bookmarksopen=⟨true|false⟩ false %是否展开书签
   bookmarksnumbered=⟨true|false⟩ false %书签是否带章节编号
   
   pdftitle=⟨string⟩        空     %标题
   pdfauthor=⟨string⟩       空     %作者
   pdfsubject=⟨string⟩      空     %主题
   pdfkeywords=⟨string⟩     空     %关键词
   pdfstartview=⟨Fit|FitH|FitV⟩ Fit %设置PDF页面以适合页面/适合宽度/适合高度等方式显示，默认为适合页面
   ```

5. hyperref宏包提供了直接书写超链接的命令，用于在PDF中生成URL：

   ```latex
   \url{⟨url⟩} %都像抄录命令\verb一样输出一个URL，区别是前者还为URL加上了超链接，后者没有。
   \nolinkurl{⟨url⟩} %url参数中可以直接输入如%、& 这样的特殊符号
   ```

6. 一些PDF阅读器会为URL文本自动加上超链接，这些超链接不是LaTeX生成的。

7. 也可以像HTML中的超链接一样，把一段文字作为超链接：

   ```latex
   \href{⟨url⟩}{⟨text⟩}
   ```

8. 使用hyperref宏包后，文档中所有的引用、参考文献、索引等等都转换为超链接。用户也可对某个\label命令定义的标签⟨label⟩作超链接：

   ```latex
   \hyperref[⟨label⟩]{⟨text⟩}
   %注意这里的⟨label⟩ 虽然是可选参数的形式，但通常是必填的
   ```

9. 默认的超链接在文字外边加上一个带颜色的边框（在打印PDF时边框不会打印），可指定colorlinks参数修改为将文字本身加上颜色，或修改pdfborder参数调整边框宽度以“去掉”边框；hidelinks参数则令超链接既不变色也不加边框。

   ```latex
   \hypersetup{hidelinks}
   \hypersetup{pdfborder={0 0 0}} %效果同上
   ```

10. hyperref 宏包另一个强大的功能是为PDF生成书签。对于章节命令\chapter、\section等，默认情况下会为PDF自动生成书签。和交叉引用、索引等类似，生成书签也需要多次编译源代码，第一次编译将书签记录写入.out文件，第二次编译才正确生成书签。

11. 使用ctex宏包和文档类，且使用xelatex或lualatex编译的情况下，无需用户额外干预，即可正确生成中文书签。

12. hyperref还提供了手动生成书签的命令：

    ```latex
    \pdfbookmark[⟨level⟩]{⟨bookmark⟩}{⟨anchor⟩} %⟨bookmark⟩为书签名称，⟨anchor⟩为书签项使用的锚点(类似交叉引用的标签)。可选参数⟨level⟩为书签的层级，默认为0。
    ```

13. 在章节命令里可以有LaTeX命令甚至数学公式，而PDF书签只能是纯文本，对命令和公式的处理很困难，有出错的风险。hyperref宏包已经为我们处理了许多常见命令，如\LaTeX和字体命令\textbf等，对于未被处理的命令或数学公式，就要在章节标题中使用如下命令，分别提供LaTeX代码和PDF书签可用的纯文本：

    ```latex
    \texorpdfstring{⟨LaTeX code⟩}{⟨PDF bookmark text⟩}
    
    \section{质能公式\texorpdfstring{$E=mc^2$}{E=mc\textasciicircum 2}} %在章节名称里使用公式E=mc2，而书签则使用纯文本形式的E=mc^2
    ```

# 自定义命令和功能

## 命令

1. 编写可重复利用的模块-宏包和文档类，并在其中自己定义命令和环境。使用自定义环境和命令，在后续的修改中，比较方便，不用挨个修改所有用到他们的情况，只需要修改命令和环境的定义即可。

   ```latex
   \newcommand{\⟨name⟩}[⟨num⟩]{⟨definition⟩} %两个必选参数，name是新的命令的名称，必须带\。definition是命令的具体定义。num是可选参数，指定命令所需要的参数个数，最多9个，默认是0。
   %例子
   \newcommand{\tnss}{The not so Short Introduction to \LaTeXe} %将一段话定义为一个命令。
   This is ``\tnss'' \ldots{} ``\tnss''
   ```
2. ![image-20240111160716660](LaTeX.assets/image-20240111160716660.png)
3. 带参数的命令：

   ```latex
   %在命令的定义中，标记#n代表第n个参数，n从1开始计数。
   \newcommand{\txsit}[1]{This is the \emph{#1} Short Introduction to \LaTeXe}
   \begin{itemize}
   	\item \txsit{not so} %用not so替换#1
   	\item \txsit{very}
   \end{itemize}
   ```
4. ![image-20240111161019578](LaTeX.assets/image-20240111161019578.png)
5. LaTeX不允许使用\newcommand定义一个与现有命令重名的命令。如果需要修改命令定义的话，应使用\renewcommand命令。它使用与命令\newcommand相同的语法。
6. 在某些情况之下，使用\providecommand命令是一种比较理想的方案：即在命令未定义时，它相当于\newcommand；在命令已定义时，什么也不做。

## 环境

1. 定义新的环境：

   ```latex
   %用\newenvironment定义新的环境
   \newenvironment{⟨name⟩}[⟨num⟩]{⟨before⟩}{⟨after⟩} %3个必选参数，name为环境名，before，after分别为环境前后的内容，用于替换\begin{name}和\end{name}。可选参数num表示环境的参数个数，用法同上。
   %例子
   \newenvironment{king}{\rule{1ex}{1ex}\hspace{\stretch{1}}}{\hspace{\stretch{1}}\rule{1ex}{1ex}}
   
   \begin{king}
   	My humble subjects \ldots
   \end{king}
   %相当于
   {\rule{1ex}{1ex}\hspace{\stretch{1}}}
   	My humble subjects \ldots
   {\hspace{\stretch{1}}\rule{1ex}{1ex}}
   ```
2. 同样存在renewenvironment命令可以重定义一个环境。
3. 通过\newcommand和\newenvironment定义的命令或环境格式比较固定。如果需要定义带有多个可选参数、或者带星号的命令或环境，可以使用xparse宏包。它提供了\NewDocument-Command和\NewDocumentEnvironment 等命令。

   ```latex
   %在LaTeX2020-10-01版本后，xparse宏包已经集成在格式中了，不用显式调用。
   \NewDocumentCommand\⟨name⟩{⟨arg spec⟩}{⟨definition⟩} %xparse使用{⟨arg spec⟩}来指定参数的个数和格式，{⟨arg spec⟩}中的空格可以忽略。
   \NewDocumentEnvironment{⟨name⟩}{⟨arg spec⟩}{⟨before⟩}{⟨after⟩}
   ```
4. 参数格式：

   ```latex
   参数格式     说明
     m         %指定必选参数，由{...} 给出
     o         %指定可选参数，由[...] 给出；未给出时返回-NoValue-标记
   O{⟨default⟩} %指定可选参数，但在未给出时则返回默认值⟨default⟩
     s         %可选的星号*
     +         %修饰其后的m、o等，表示允许在参数中分段
   ```
5. 例子：

   ```latex
   参数格式           输入值           #1        #2      #3
   m m             {foo}{bar}        foo       bar
   o m               {foo}        -NoValue-    foo
   o o m           [foo]{bar}        foo    -NoValue-  bar
   m O{default}      {foo}           foo     default
   m O{default}    [bar]{foo}        foo       bar
   m O{default}      [bar]          报错
   s o m          *[foo]{bar}    \BooleanTrue  foo    bar
   s m O{default}    {foo}       \BooleanFalse foo  default
   ```
6. -NoValue-标记可以用如下命令来判断：

   ```latex
   \IfNoValueTF{⟨argument⟩}{⟨true code⟩}{⟨false code⟩} %同时设置真/假时的操作
   \IfNoValueT{⟨argument⟩}{⟨true code⟩} %只设置真时的操作
   \IfNoValueF{⟨argument⟩}{⟨false code⟩}
   %例子，行尾的百分号用于注释掉不必要的空格和换行符，或者将他们写在一行。
   \NewDocumentCommand\hello{om}{% 接收1个可选参数和1个必选参数
   \IfNoValueTF{#1}%
   {Hello, #2!}%
   {Hello, #1 and #2!}%
   }
   \hello{Alice} %没有可选参数，因此#1为-NoValue-
   \hello[Bob]{Alice}%
   ```
7. ![image-20240111172617519](LaTeX.assets/image-20240111172617519.png)
8. \BooleanTrue和\BooleanFalse可以用`\IfBooleanTF`等命令来判断，用法和上面的类似。

   ```latex
   \NewDocumentCommand\hereis{sm}{Here is \IfBooleanTF{#1}{an}{a} #2.}
   \hereis{banana} %没有*，因此#1为\BooleanFalse
   \hereis*{apple}
   ```
9. ![image-20240111172825518](LaTeX.assets/image-20240111172825518.png)
10. 与命令不同，环境在定义时名字里面可以包含`*`，不过这个`*`不表示环境接收带`*`的格式，而只是一个符号而已：

    ```latex
    \NewDocumentEnvironment{envstar}{s}{\IfBooleanTF{#1}{star}{no star}}{}  %通过在arg spec中指定s来表明环境支持*格式。
    \begin{envstar}*  %使用*格式的环境时，*放在\begin{}的后面
    \end{envstar}
    \begin{envstar}
    \end{envstar}
    ```
11. ![image-20240111173751329](LaTeX.assets/image-20240111173751329.png)
12. xparse宏包也允许在命令或环境已有定义时做出相应的处理：

    ```
    定义命令                   定义环境                      已定义        未定义
    \NewDocumentCommand       \NewDocumentEnvironment      报错         新增定义
    \RenewDocumentCommand     \RenewDocumentEnvironment    重新定义       报错
    \ProvideDocumentCommand   \ProvideDocumentEnvironment  什么也不做    新增定义
    \DeclareDocumentCommand   \DeclareDocumentEnvironment  重新定义      新增定义
    ```

## 宏包

1. 如果定义了很多新的环境和命令，将使得文档的导言区变得很长，此时，可以建立一个新的LaTeX宏包来存放所有自定义的命令和环境，然后在文档中使用\usepackage命令来调用这个宏包。
2. 创建宏包的步骤：创建一个.sty的文件，在文件开头添加一行`\ProvidesPackage{...}`，将自定义的环境和命令拷贝进去，然后就可以使用它了。

   ```latex
   % 可以添加一个宏包的注释
   \ProvidesPackage{demopack}  %指定宏包名称，需要和文件名一致。这一句的功能是让LaTeX记录宏包的名称，从而在\usepackage命令再次调用同一个宏包的时候忽略之。但如果以不同的选项多次引入宏包，则有可能会引起错误。
   \newcommand{\tnss}{The not so Short Introduction to \LaTeXe}
   \newcommand{\txsit}[1]{The \emph{#1} Short Introduction to \LaTeXe}
   \newenvironment{king}{\begin{quote}}{\end{quote}}
   ```
3. 在自己编写的宏包中调用其它宏包：

   ```latex
   \RequirePackage[⟨options⟩]{⟨package name⟩} %用法和\usepackage一致
   ```

## 文档类

1. 如果要制作模板，就需要编写自己的文档类。创建文档类的步骤：创建一个.cls的文件，在文件开头添加`\ProvidesClass{...}`一行，将自定义的环境和命令拷贝进去。不过此时并不能直接使用，因为诸如\chapter，\section的命令还没有定义。
2. 在你的文档类中调用其它文档类的命令是\LoadClass：

   ```latex
   \LoadClass[⟨options⟩]{⟨package name⟩} %用法和\documentclass十分相像
   ```

## 计数器

1. LaTeX会对大部分文档元素进行自动计数，例如章节符号、列表、图表等。用户也可以自定义计数器。

   ```latex
   \newcounter{⟨counter name⟩}[⟨parent counter name⟩] %⟨counter name⟩为计数器的名称。计数器可以有上下级的关系，可选参数⟨parent countername⟩定义为⟨counter name⟩的上级计数器。
   %以下命令修改计数器的数值
   \setcounter{⟨counter name⟩}{⟨number⟩} %将计数器的值设定为number
   \addtocounter{⟨counter name⟩}{⟨number⟩} %将计数器的值加上number
   \stepcounter{⟨counter name⟩} %将计数器的值+1，并将下级计数器的值归零。
   ```
2. 计数器⟨counter⟩的输出格式由\the⟨counter⟩表示，例如\thechapter。这个值默认以阿拉伯数字形式输出，如果想改成其它形式，需要重定义\the⟨counter⟩命令：

   ```latex
   \renewcommand\theequation{\Alph{equation}} %将equation计数器的格式定义为大写字母
   ```
3. 所有可用于修改计数器格式的命令，这些命令只能用于计数器，不能直接用于数字：

   ```latex
   命令        样式                                  范围
   \arabic   阿拉伯数字(默认)
   \alph     小写字母                              限0–26
   \Alph     大写字母                              限0–26
   \roman    小写罗马数字                          限非负整数
   \Roman    大写罗马数字                          限非负整数
   \fnsymbol 一系列符号，用于\thanks命令生成的脚注   限0–9
   %\fnsymbol使用的符号顺次为：∗ † ‡ § ¶ ‖ ∗∗ †† ‡‡
   ```
4. 计数器的输出格式还可以利用其它字符，甚至其它计数器的输出格式与之组合。如标准文档类里对\subsection相关的计数器的输出格式的定义相当于：

   ```latex
   \renewcommand\thesubsection{\thesection.\arabic{subsection}} %相当于在\section后加上.数字
   ```
5. LaTeX中的计数器：

   1. 所有章节命令\chapter、\section 等分别对应计数器chapter、section 等等，而且有上
      下级的关系，形成一个链。而计数器part是独立的。
   2. 有序列表enumerate的各级计数器为enumi，enumii，enumiii，enumiv，也有上下级的关系。
   3. 图表浮动体的计数器就是table和figure；公式的计数器为equation。这些计数器在article文档类中是独立的，而在report和book中以chapter为上级计数器。
   4. 页码、脚注的计数器分别是page和footnote。

6. 修改计数器的样式以达到想要的效果：

   ```latex
   \renewcommand\thepage{--~\Roman{page}~--} %把页码修改成大写罗马数字，左右加横线和空格
   \renewcommand\thefootnote{[\arabic{footnote}]} %给脚注编号加上方括号
   ```
7. 命令\pagenumbering的内部机制就是修改page计数器的格式\thepage，并将计数器的值重置为1。
8. LaTeX标准文档类对章节划分了层级：

   1. 在article文档类里part 为0，section为1，依此类推；
   2. 在report和book文档类里part 为-1，chapter 为0，section为1，依此类推。

9. secnumdepth计数器控制章节编号的深度，如果章节的层级大于secnumdepth，那么章节的标题、在目录和页眉页脚的标题都不编号（照常生成目录和页眉页脚），章节计数器也不计数。

10. 可以用\setcounter命令设置secnumdepth为较大的数使得层级比较深的章节也编号，如设置为4令\paragraph也编号；或者设置一个较小的数以取消编号，如设置为-1令\chapter不编号。

11. 后者是生成不编号的章节的一个妙招，免去了手动使用\addcontentsline和\markboth的麻烦。

12. 它在article文档类里默认为3（subsubsection一级）；在report和book文档类里默认为2（subsection一级）。

13. tocdepth计数器控制目录的深度，如果章节的层级大于tocdepth，那么章节将不会自动写入目录项。默认值同secnumdepth。


## 定制文字

1. 对于用户来讲，容易定制的是：标题名称/前后缀和长度。

   ```latex
   %表中所有的LaTeX 命令都可以用\renewcommand 来修改
   命令               默认值             含义
   \partname          Part               \part 命令生成的标题前缀
   \chaptername       Chapter            \chapter 命令生成的标题前缀
   \appendixname      Appendix           使用\appendix 命令生成的附录部分的章标题前缀
   \abstractname      Abstract           摘要环境abstract 的标题名称
   \contentsname      Contents           \tableofcontents 命令生成的目录标题
   \listfigurename    List of Figures    \listoffigures 命令生成的插图目录标题
   \listtablename     List of Tables     \listoftables 命令生成的表格目录标题
   \tablename         Table              table 浮动体中\caption 命令生成的标题前缀
   \figurename        Figure             figure 浮动体中\caption 命令生成的标题前缀
   \refname           References         thebibliography 环境或\bibliography 命令生成的参考文献标题(article 文档类)
   \bibname           Bibliography       thebibliography 环境或\bibliography 命令生成的参考文献标题(report 和book 文档类)
   \indexname         Index              \printindex 命令生成的索引标题
   %表中所有的长度命令可用\setlength来修改。
   \fboxrule          0.4pt   \fbox 或\framebox 等带框盒子的线宽
   \fboxsep           3pt     \fbox 或\framebox 等带框盒子的内边距
   \arraycolsep       5pt     array 环境的表格项前后的间距注1
   \tabcolsep         6pt     tabular 环境的表格项前后的间距注1
   \arrayrulewidth    0.4pt   表格线宽
   \doublerulesep     2pt     连续两根表格线之间的间距
   \abovecaptionskip  10pt    \caption 命令上方的间距注
   \belowcaptionskip  0pt     \caption 命令下方的间距注
   \columnsep         10pt    双栏排版下两栏的间距
   \columnseprule     0pt     双栏排版下两栏之间竖线的宽度
   ```

2. 形如“第X 章”和“第X 部分”的中文章节标题不能直接由修改上表的命令得到，需要使用titlesec等宏包定制。如果使用ctex宏包或文档类，上表的所有标题都会修改为中文标题。

3. \arraycolsep和\tabcolsep是每个表格项本身前后的间距（表格线前后无间距；使用@列格式会消除与前后表格项的间距）。两个表格项之间的间距相当于2\arraycolsep或2\tabcolsep。

4. 在默认设置下，\caption命令和位于它下方的图表之间无间距。如果使用了caption宏包则间距不为0。


## 其他功能

1. Option clash是指：以不同选项重复调用宏包造成冲突。有可能是因为其它宏包内部事先调用了这个宏包，用户再次带选项调用而导致冲突。解决问题的办法是去掉重复调用的宏包。如果宏包允许的话，尽量使用其定义的命令改变设置，而减少使用选项来设置。

2. 相比于“Option clash”，隐性宏包冲突是更难以解决的问题，对各种宏包不熟悉的用户，尤其是使用模板的用户而言，往往难以下手。用户可尝试查找引起冲突的宏包的帮助文档。详尽的手册里通常会告知用户这个宏包应当在某个宏包的前面/后面调用，或者不能与某个宏包一起调用。如果是模板调用了大量宏包导致冲突，可联系模板的作者解决。

3. Tex的常见发行版都提供了一个texdoc的命令，用于快速查找到对应的帮助文档：

   ```shell
   texdoc fancyhdr  #会使用默认的pdf阅读器打开fancyhdr宏包的帮助文档
   texdoc latex2e   #latex的非官方文档，系统地介绍了latex的所有功能
   ```

4. 除了宏包的帮助文档外，TEX 发行版还包括了各类有用的文档。如果不熟悉命令行工具的话，TEX Live 提供了一个图形界面的程序TeXdoc GUI。


## 矢量绘图

1. 与LATEX配套使用的矢量绘图工具有四种：METAPOST，PSTricks，PGF，Asymptote。
2. PSTricks 有PostScript 作后盾，功能最强；METAPOST 擅长处理数学内容；PGF 的流程图有独到之处。后起之秀Asymptote颇有独到之处。


# Error汇总

1. 忘记为矩阵添加数学环境，加上equation环境或者$ $都可以。

   ```latex
   ! Missing $ inserted.
   <inserted text> 
                   $
   l.25 \begin{smallmatrix}
   
   ? 
   ```

2. 忘记添加对应的包了，\usepackage{amssymb}即可。

   ```latex
   ! Undefined control sequence.
   <argument> ...\sin ^2 x \\ &=2\cos ^2 x-1 \mathbb 
                                                     {R} \end {split}
   l.23       \end{split}
   
   ? 
   ```

3. 命令后没有空格。

   ```latex
   ! Undefined control sequence.
   l.14     中文字体中文字体中文字体中文字\LaTeX体中文字体中文字体中文字体中文字体
   
   ?
   ```

4. CJK字体的声明只能在导言区，而\setmainfont就可以在正文区，声明的同时就应用。

   ```latex
   ! LaTeX Error: Can be used only in preamble.
   See the LaTeX manual or LaTeX Companion for explanation.
   Type  H <return>  for immediate help.
    ...                                              
   
   l.22     {\setCJKmainfont
                            {FZQingKeBenYueSongS} 锦瑟}
   ?
   ```

5. \vskip {1em} 应该为 \vskip 1em。

   ```latex
   ! Missing number, treated as zero.
   <to be read again> 
                      {
   l.28     \vskip{
                   1em}
   ?
   ```

6. Hithesis中如果没有引用任何参考文献，需要关闭bibliography的两条命令。否则会报以下错误。

   ```latex
   ! LaTeX Error: Something’s wrong--perhaps a missing \item.
   ```

7. 此错误出现的原因是因为在编译时，在外部（adobe reader）打开了pdf文件。

   ```latex
   xdvipdfmx:fatal: Unable to open "main.pdf". Output file removed.
   
   fwrite: Invalid argument
   
   xelatex.exe:
   
   出现错误
   ```

8. bib数据库中的标识中间不能有空格。

   ```latex
   I was expecting a `,' or a `}'---line 545 of file reference.bib
    : @article{璋㈣悕 
    :                 2018寮€鏀剧┖闂村ぇ灏哄害鍙噧姘斾簯鐖嗙偢娴嬭瘯鎶€鏈帰璁
   I'm skipping whatever remains of this entry
   Warning--Require journal: Berg1996GAME
   (There was 1 error message)
   ```

9. 有时出错是因为前一次编译中断导致.aux等辅助文件不完整，再次编译读入不完整的文件产生错误。解决办法是删除辅助文件并重新编译。

10. 字面上是缺少\begin{document}，实际上往往是由于在\begin{document} 之前（导言区）输入了文字或某些命令。

    ```latex
    ! LaTeX Error: Missing \begin{document}.
    ```

11. 与上一条相反，由于将必须用于导言区的命令在\begin{document} 之后使用而产生。

    ```latex
    ! LaTeX Error: Can be used only in preamble.
    ```
