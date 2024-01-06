# 基础

1. TEX是斯坦福大学的Knuth（高德纳）教授开发的，是一个电子排版系统，非常适用于生成高印刷质量的科技类和数学类文档。

2. 1977年，正在编写《计算机程序设计艺术》的高德纳意识到每况愈下的排版质量将影响其著作的发行，为扭转这种状况，他着手开发TEX。

3. TEX的哲学是使版面样式设置和文档的具体内容尽可能分离，让写文档的人更加专注于文档的撰写，而少花些心思在排版上。TeX排版的结果是DVI(Device Independent)，文件与输出设备无关。可以打印，显示，照排等，可以输出到任何设备上。

4. 现在使用TeX引擎发布于1982年，1989年稍加改进。TeX的版本号不断逼近π，当前为3.141592653。TeX的拼写来自希腊语τεχνική (technique，技术)的开头的几个字母。

5. 由于TEX是很低阶的排版语言，所以基于其开发的宏集（集成了大量二次开发的命令，更方便使用）有很多，LaTeX就是其中之一，由Leslie Lamport编写的。还有比较著名的AMSTeX，美国数学学会推荐数学家使用的。

6. LaTeX是一种使用TEX程序作为排版引擎的格式（format），可以粗略地将它理解成是对TEX 的一层封装。当前的版本为LaTeX2e，意思是超出了第2版，接近但还远没有到第3版。e是希腊字母ε的意思，也就是无穷小量。

7. 和Word相比，TEX排版系统的缺点：不如所见即所得软件显而易见，需要不断地编译查看，且其使用的宏语言比一般的编程语言更难排错，且无法调试。word是所见即所得，LaTeX是所想即所得。二者的设计目标不一致，也各自有自己的适用范围。

8. TEX的发行版一般包含编译引擎，宏包，文档。常见的发行版与TEXLive、CTEX、MiKTEX、MacTEX。

   1. TEXLive每年发行一版，当发布新版本后，旧版本就会被冻结，update只能更新到当前版本的最新。它是跨平台的。推荐使用这个。
   2. MacTEX 是macOS（OS X）系统下的一个定制化的TEX Live 版本，与TEX Live 同步更新。
   3. CTEX是中科院吴凌云基于MiKTEX的基础上开发的，2012年之后疏于维护，长久不更新。CTEX是利用TEX排版系统的CTEX中文套装的简称。它集成了编辑器 、WinEdt和 PostScript处理软件 Ghostscript 和 GSview 等主要工具。 CTeX中文套装在 MiKTeX的基础上增加了对中文的完整支持。CTeX中文套装支持 CCT 和 CJK 两种中文 TeX处理方式。 
   4. 以上2者都集成了一个简单的LaTeX 源代码编辑器TeXworks。不过不推荐安装，推荐单独安装TexStudio。

9. Linux 发行版的软件源也提供TEX Live 的安装，不过不够完整，更新也不是很及时。建议直接从镜像安装。

10. 两种发行版都提供了用来安装，删除，更新宏包的工具。TEX Live 默认安装所有宏包，而MiKTEX 的安装程序只包含了LaTeX 的一些基本宏包。除非万不得已，尽量不要手动安装宏包，应该使用发行版带的工具安装。

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

14. ![image-20240105011944208](LaTeX.assets/image-20240105011944208.png)

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
    10pt, 11pt, 12pt %指定文档的基本字号。默认为10pt。
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

33. LaTeX的辅助功能，如交叉引用，参考文献，目录等需要先编译生成辅助文件，再次编译时才会读入辅助文件。所以复杂的源代码可能需要编译多次。一般以不再出现warning为止。

34. 多文档编译，一般用于编写书籍或毕业论文，将内容分章节组织成多个tex文件，会大大简化修改和校对
    的工作。两种方法：

    1. 可以使用命令`\include{⟨filename⟩}`在源代码里插入文件（文件名不能带.tex扩展，2020-10-1的LaTeX版本后允许带后缀名）。
    2. 可以在导演去使用`\includeonly{文档列表}`，这样生成PDF时会只会载入文档列表中的文件，正文中不在该范围的`\include`命令不会起效，一般用于调试，最终生成时应注释掉这句话。
    3. 这条命令会在插入前另起一页。有的时候我们并不需要这样，而是使用`\input{b.tex}`进行原样插入，它纯粹是把文件里的内容插入。

35. 当导言区内容较多时，常常将其单独放置在一个.tex 文件中，再用\input 命令插入。复杂的图、表、代码等也会用类似的手段处理。

36. 2020版本之前的LaTeX，对于include和input的文件名最好不要有空格或特殊字符，尽量壁面使用中文，现在只要是操作系统允许的，都可以作为文件名。

37. \input{part/part1}\newpage   引用某一个LaTeX文件的内容。在章末另起一页。也可以使用\include{}。

38. syntonly宏包是用来排查错误的，使用这个宏包和在导言区加入\syntaxonly命令后，编译不产生pdf，dvi文档。排错方便，速度提升。如果想生成文档则使用%注释掉该行命令即可。

    ```latex
    \usepackage{syntonly}
    \syntaxonly
    ```


# 中文支持

1. 最早的TeX只支持7-bit的ASCII编码，如Möbius必须通过输入`M\"obius`得到。3.0版本后支持8-bit，能够处理0x80-0xFF之间的字符，使用latex或pdflatex命令时，对源代码的编码处理由inputenc宏包支持。比如将源代码保存为Latin-1编码，并在导言区调用inputenc宏包并指定latin1选项后，Möbius这样的词语就可以直接通过（用适当输入法）输入`Möbius`得到了。

2. 将使用拉丁字母的文档保存为UTF-8编码后，可以用pdflatex直接编译，但是非拉丁字母仍然无法直接在LaTeX中使用。

3. 用LATEX 排版中文需要解决两方面问题：对中文字体的支持，对中文排版中的一些细节的处理，例如汉字之间控制断行、标点符号的禁则（如句号、逗号不允许出现在行首）、中英文之间插入间距等。

4. xeCJK 及luatexja宏包封装了对汉字排版细节的处理功能。ctex宏包和文档类进一步封装了CJK、xeCJK、luatexja等宏包，使得用户在排版中文时不用再考虑排版引擎等细节。

5. ctex 宏包本身用于配合各种文档类排版中文，而ctex 文档类对LATEX 的标准文档类进行了封装，对一些排版根据中文排版习惯做了调整，包括ctexart、ctexrep、ctexbook等。ctex 宏包和文档类能够识别操作系统和TEX 发行版中安装的中文字体，因此基本无需额外配置即可排版中文文档。

6. xelatex和lualatex命令配合ctex宏包/文档类的方式成为当前的主流中文排版支持方式，旧方式（CCT、CJK等）日渐退出舞台。

7. 虽然ctex宏包和文档类保留了对GBK编码以及latex和pdflatex编译命令的兼容，但是不推荐使用。

8. ctex还用来指代一个TEX的过时的发行版，注意区分。xelatex又称为“邪恶LaTeX”。

9. 在LaTeX的2018-04-01版本之前，需要调用inputenc宏包并指定utf8选项才能使用UTF-8编码，现在默认就是UTF-8编码。

10. 使用XeLaTeX编译时，强制开启UTF8选项，而使用pdfLaTeX或LaTeX编译时，为ANSI编码。

11. ctex的两种使用方法：

    1. XeLaTeX编译+使用ctex宏包   CJK环境仅仅是支持了中文的输入，这个ctex则是将营造了中文的环境，例如二者对日期的支持不同，CJK输出英文，ctex输出中文。
    2. XeLaTeX编译+使用ctexart文档类，之后不用再声明使用ctex宏包。
    3. 上述两种方法不完全一样，例如对于\section的内容，ctex宏包会左对齐， ctexart文档类会居中。使用\ctexset{ }命令来设置全局的样式。这些都可以在导言区通过\ctexset命令来进行修改。

12. 空格键和Tab键输入的空白字符视为“空格”。连续的若干个空白字符视为一个空格。源码中一行开头的空格会被忽略。

13. 使用%来产生注释，其后一直到行尾的字符都会被注释，行末的换行符也不会产生空格。

14. 以下字符需要转义才可以正常输入：

    ```latex
    # $ % & { } _ ^ ~ \
    %其中\^和\~需要{}，因为他们也可以为字符添加重音。当{}内为空时，就直接输入该字符
    \# \$ \% \& \{ \} \_
    \^{} \~{} \textbackslash
    %不能使用\\来输出\，因为它被直接定义成了手动换行的命令
    ```

15. 西文排版中经常会出现连字（ligatures），常见的有`ff   fi   fl   ffi   ffl`。可以在连字中间加入{}来取消。

16. <img src="LaTeX.assets/fb89aba2-499c-4b04-ab86-6c028d545381.png" alt="img" style="zoom:33%;" />

17. 点号分为两类，①句内点号：顿号、逗号、分号、冒号②句末点号：句号、问号、叹号。这些点号主要表示语言中种种停顿。标号包括破折号、括号、省略号、书名号、引号、连接号、间隔号、着重号、专名号等，主要标明词语或句子的性质和作用。需要注意的是，问号和叹号也兼属标号：就其表示句末停顿而言，是点号；就其表示句子语气而言，是标号。

18. 从键盘上一共可以输入6种引号，分别是英文输入法下的单双引号，和中文输入法下的左右单双引号。中文的引号是分左右的，不过都是通过一个键来输入，输入法会自动选择左右引号。

    ```latex
    '   "
    %上面两个是英文输入法下的单双引号，编码分别为0x27和0x22，为半角的
    ‘   ’
    %上面两个是中文输入法下的单双引号，编码分别为0xE28098和0xE28099，为全角的
    “   ”
    %上面两个是中文输入法下的单双引号，编码分别为0xE2809C和0xE2809D，为全角的
    ```

19. 在使用ctex宏包或文档类的情况下，中文引号可以通过输入法直接输入。

20. 示例，下面的所有引号从pdf中复制出去，结果都是中文的引号，都不是ASCII字符。：

    ```latex
    A'and"B
    
    A''and"B  %两个单引号可以等价于一个双引号，两者编译后都只会生成同一个符号
    
    A`and'B   %`和'构成左右单引号
    
    A‘and’B   %这行在没有开启ctex时，和上一行一样，如果开启了ctex后，则和上面显示不同，从pdf中观察可以发现，这是因为这里的引号使用的字体是中文字体，因此比较宽，将其修改为英文字体后，结果和上面一样。
    
    A``and''B %``和''构成左右双引号
    
    A“and”B   %同上2行的结果
    ```

21. ![image-20240105125946526](LaTeX.assets/image-20240105125946526-1704516157720-1-1704516183761-59.png)

22. 有三种长度的“横线”可用：

    1. 连字号（hyphen），用来组成复合词。

    2. 短破折号（en-dash），用来连接数字表示范围。中文排版中一般使用`$\sim$`来连接数字表示范围。不能直接使用`~`，因为他表示一个空格。

    3. 长破折号（em-dash），用来连接单词，语义上类似中文的破折号。

    4. ```latex
       daughter-in-law, X-rated
       
       pages 13--67 页码80$\sim$88
       
       yes---or no?
       ```

    5. ![image-20240105131444483](LaTeX.assets/image-20240105131444483-1704516157720-2-1704516183762-61.png)

23. 可以使用\ldots命令表示省略号，相对于直接输入三个点的方式更为合理，因为前者会被编译成一个字符，后者是三个。\dots与\ldots命令等效。

    ```latex
    one, two, three, \ldots{} one hundred.%加入{}的目的是为了使得和one之间的空格生效
    
    abc...def\ldots
    ```

24. ![image-20240105132141058](LaTeX.assets/image-20240105132141058-1704516157720-3-1704516183762-60.png)

25. 支持用命令输入西欧语言中使用的各种拉丁文扩展字符，主要为带重音的字母，注意和数学符号的重音区分开：

    ```latex
    H\^otel, na\"\i ve, \'el\`eve,%\^o等价于\^{o}
    
    sm\o rrebr\o d, !`Se\ norita!,
    
    Sch\"onbrunner Schlo\ss
    
    Stra\ss e
    ```

26. ![image-20240105132743531](LaTeX.assets/image-20240105132743531-1704516157721-4-1704516183762-62.png)

27. 预定义的其它一些文本模式的符号，更多的符号多由特定的宏包支持：

    ```latex
    \P{} \S{} \dag{} \ddag{}
    
    \copyright{} \pounds{}
    
    \textasteriskcentered A*%注意区分，高度不同
    
    \textperiodcentered A.
    
    \textbullet A·
    
    \textregistered{} \texttrademark
    ```

28. ![image-20240105133200094](LaTeX.assets/image-20240105133200094-1704516157721-5-1704516183762-63.png)

29. 错落有致的LaTeX标志：

    ```latex
    \TeX
    
    \LaTeX
    
    \LaTeXe
    ```

30. ![image-20240105133348061](LaTeX.assets/image-20240105133348061-1704516157721-6-1704516183762-64.png)

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

34. 通常为了保持源文件的清晰，通过插入空行或使用`\par`命令来实现分段，类似于word的回车。多个空行视为一个。

35. 换行（`\\`强制分行）≠分段（空一行或`\par`）

36. 手动段页的命令有2个：

    ```latex
    \newpage
    \clearpage
    %在双栏排版模式中\newpage起到另起一栏的作用，\clearpage则能够另起一页。
    %二者在涉及浮动体的排版上行为不同。
    ```

37. 有时候我们不满足于默认的断行和断页位置，需要进行微调，可以用以下命令告诉引擎哪些地方适合断行或断页，哪些地方不适合：

    ```latex
    \linebreak[⟨n⟩] \nolinebreak[⟨n⟩]
    \pagebreak[⟨n⟩] \nopagebreak[⟨n⟩]
    %以上命令都带一个可选的参数n，表示是适合或不适合的程度，取值范围为0-4，默认为4.
    %\linebreak[4]表示此处需要强行断行
    %\nolinebreak[4]表示禁止在此处断行
    ```

38. 不过不推荐使用break系列命令，更推荐使用new系列命令，因为使用这些命令强行断行/断页可能会制造出糟糕的排版效果，并导致引擎报Underfull \hbox 等警告：

    ```latex
    使用\verb|\newline| 断行的效果
    \newline
    与使用\verb|\linebreak| 断行的效果
    \linebreak
    进行对比。
    ```

39. ![image-20240105135106405](LaTeX.assets/image-20240105135106405-1704516157721-7-1704516183762-65.png)

40. 当遇到非常长的单词时，仅在单词之间断行无法形成宽度均匀的行时，会进行断字。手动断字使用\-

41. 当遇到了很长的英文单词时，如果仅靠在单词之间的“空格”处断行无法生成疏密程度匀称的段落时，就会考虑从单词中间断开。对于绝大多数单词，引擎能够找到合适的断词位置，在断开的行尾加上连字符-。如果一些单词没能自动断词，我们可以在单词内手动使用`\-`命令指定断词的位置：

    ```latex
    I think this is I think this is I think this is I think this is: su\-per\-cal\-i\-frag\-i\-lis\-tic\-ex\-pi\-al\-i\-do\-cious.
    ```

42. ![image-20240105135556029](LaTeX.assets/image-20240105135556029-1704516157721-8-1704516183762-66.png)

# 文档元素

1. 一个结构化的文档所依赖的各种元素有：章节、目录、列表、图表、交叉引用、脚注等。

2. 标准文档类或继承自该类的文档类都有以下命令，这些命令生成章节标题，并能够自动编号，还向目录中添加条目，并影响页眉页脚的内容：

   ```latex
   \chapter{第一章}           %章标题，只在report和book文档类有定义
   \section{第一节}           %节标题，对于article，最高的就是section了
   \subsection{第一小节}      %小节标题
   \subsubsection{第一小小节} %小小节标题
   ```

3. ![image-20240105140723605](LaTeX.assets/image-20240105140723605-1704516157721-9-1704516183762-67.png)

4. 每个命令有两种变体：

   ```latex
   \section[⟨short title⟩]{⟨title⟩} %带可选参数，标题使用⟨title⟩参数，在目录和页眉页脚中使用⟨short title⟩参数；
   \section*{⟨title⟩} %带星号，此时标题不带编号，也不生成目录项和页眉页脚。
   ```

5. `\paragraph{}`和`\subparagraph{}`是章节标题命令，不是分段。它是在`\subsubsection{}`在下一层，即使不用带星号的变体，生成的标题默认也不带编号。

6. article 文档类带编号的层级为\section、\subsection、\subsubsection三级。

7. report 和book 文档类带编号的层级为\chapter、\section、\subsection三级。

8. 除此之外LATEX 还提供了\part 命令，用来将整个文档分割为大的分块，但不影响\chapter或\section等的编号。应该类似于word的分节。

9. LaTeX及标准文档类并未提供为\section等章节命令定制格式的功能，这一功能由titlesec宏包提供。

10. 生成目录的方法，只需在合适的地方使用命令：`\tableofcontents`。这个命令会生成单独的一个chapter（report/book）或一个section（article），不过该章节默认不写入目录。标题默认为“Contents”，可以使用`\contentsname`定制标题。

11. 有时我们使用了`\chapter*`或`\section*`这样不生成目录项的章节标题命令，而又想手动生成该章节的目录项，可以在标题命令后面使用：

    ```latex
    \addcontentsline{toc}{⟨level⟩}{⟨title⟩} %其中⟨level⟩为章节层次chapter或section等，⟨title⟩为出现于目录项的章节标题。
    ```

12. itletoc、tocloft等宏包提供了具体定制目录项格式的功能。

13. 为了正确生成目录项，一般需要编译两次源代码，有时可能要编译3次。

14. 所有标准文档类都提供了一个\appendix 命令将正文和附录分开2，使用\appendix 后，最高一级章节改为使用拉丁字母编号，从A 开始。

15. book文档类还提供了前言、正文、后记结构的划分命令：

    ```latex
    \frontmatter %前言部分，页码使用小写罗马数字；其后的\chapter不编号。直到遇到\mainmatter都是前言部分。
    \mainmatter  %正文部分，页码使用阿拉伯数字，从1开始计数；其后的章节编号正常。
    \backmatter  %后记部分，页码格式不变，继续正常计数；其后的\chapter不编号。
    %以上三个命令还可和\appendix命令结合，生成有前言、正文、附录、后记四部分的文档。
    ```

16. LaTeX支持生成简单的标题页。首先需要给定标题和作者等信息：`\title{⟨title⟩} \author{⟨author⟩} \date{⟨date⟩}`，其中前两个命令是必须的（不用\title会报错；不用\author会警告），\date命令可选。给定信息的指令可以放在导言区或正文区，但是\maketitle必须放在正文区。且其之前会分页。

17. LaTeX还提供了一个\today命令自动生成当前日期，\date默认使用\today。在\title、\author等命令内可以使用\thanks命令生成标题页的脚注，用\and隔开多个人名。

18. 在信息给定后，就可以使用\maketitle 命令生成一个简单的标题页了。

19. article文档类的标题默认不单独成页，而report和book默认单独成页。

20. LATEX 标准类还提供了一个简单的titlepage环境，生成不带页眉页脚的一页。用户可以在这个环境中使用各种排版元素自由发挥，生成自定义的标题页以替代\maketitle 命令。甚至可以利用titlepage环境重新定义\maketitle：

    ```latex
    \renewcommand{\maketitle}{\begin{titlepage}
    ... % 用户自定义命令
    \end{titlepage}}
    ```

21. 实际上为标准文档类指定了titlepage 选项以后，使用\maketitle 命令生成的标题页就是一个titlepage环境。

22. 一个ctexbook文档类的示例：

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

23. 在能够被交叉引用的地方，如章节、公式、图表、定理等位置使用\label命令做标记。之后可以在别处使用\ref或\pageref命令，分别生成该标记的编号和页码：

    ```latex
    \chapter{测试}\label{sec:this}
    A reference to this subsection looks like:
    ``see section~\ref{sec:this} on page~\pageref{sec:this}.''
    ```

24. ![image-20240105163454711](LaTeX.assets/image-20240105163454711-1704516157721-10-1704516183762-68.png)

25. 为了生成正确的交叉引用，一般也需要多次编译源代码。

26. \label命令可用于记录各种类型的交叉引用，使用位置分别为：

    ```latex
    章节标题 %在章节标题命令\section等之后紧接着使用。
    行间公式 %单行公式在公式内任意位置使用；多行公式在每一行公式的任意位置使用。
    有序列表 %在enumerate环境的每个\item命令之后、下一个\item命令之前任意位置使用。
    图表标题 %在图表标题命令\caption之后紧接着使用。
    定理环境 %在定理环境内部任意位置使用。
    %1. 如果对象是由一条命令产生的，如\section，直接在其后输入\label{}即可，如果是由环境产生，则需要在环境内部任意处声明label，如equation。 
    %在使用不记编号的命令形式（\section*、\caption*3、带可选参数的\item 命令等）时不要使用\label 命令，否则生成的引用编号不正确。
    ```

27. 使用\footnote命令可以在页面底部生成一个脚注，脚注内也可以包含公式、图片等：

    ```latex
    “天地玄黄，宇宙洪荒。日月盈昃，辰宿列张。”\footnote{出自《千字文》。}
    ```

28. 在正文和脚注的显示分别为：

29. ![image-20240105164024452](LaTeX.assets/image-20240105164024452-1704516157721-11-1704516183762-69.png)

30. ![image-20240105164032650](LaTeX.assets/image-20240105164032650-1704516157721-13-1704516183762-70.png)

31. 有些情况下（比如在表格环境、各种盒子内，用于对某个单元格进行注释）使用\footnote并不能正确生成脚注。我们可以分两步进行，先使用\footnotemark为脚注计数，再在合适的位置用\footnotetext生成脚注。对整个表格的注释就放在环境外，直接使用\footnote即可。

32. LATEX 提供了基本的有序和无序列表环境enumerate和itemize，两者的用法很类似，都用\item标明每个列表项。enumerate环境会自动对列表项编号。其中\item可带一个可选参数，将有序列表的计数或者无序列表的符号替换成自定义的符号。列表可以嵌套使用，最多嵌套四层。

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

33. ![image-20240105170001764](LaTeX.assets/image-20240105170001764-1704516157721-12-1704516183762-71.png)

34. 默认的列表间距比较宽，LaTeX 本身也未提供方便的定制功能，可用enumitem宏包定制各种列表间距。enumitem宏包还提供了对列表标签、引用等的定制。

35. center、flushleft 和flushright 环境分别用于生成居中、左对齐和右对齐的文本环境。

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

36. ![image-20240105181322555](LaTeX.assets/image-20240105181322555-1704516157721-14-1704516183762-74.png)

37. 还可以用以下命令直接改变文字的对齐方式：

    ```latex
    \centering
    Centered text paragraph.
    
    \raggedright
    Left-aligned text paragraph.
    
    \raggedleft
    Right-aligned text paragraph.
    ```

38. ![image-20240105181743608](LaTeX.assets/image-20240105181743608-1704516157721-15-1704516183762-72.png)

39. 三个命令和对应的环境经常被误用，命令是对其后的所有都生效，直到遇到同类的其他命令。命令和环境的区别是：

40. center等环境会在上下文中产生一个额外间距，而\centering等命令不产生，只是改变对齐方式。比如在浮动体环境table或figure内实现居中对齐，应使用\centering命令，没必要再用center环境。

41. LaTeX提供了两种引用的环境：quote用于引用较短的文字，首行不缩进；quotation用于引用若干段文字，首行缩进。引用环境较一般文字有额外的左右缩进。

42. 有时我们需要将一段代码原样转义输出，这就要用到代码环境verbatim，它以等宽字体排版代码，回车和空格也分别起到应有的换行和空格的作用；带星号的版本会将空格显示成`␣`。会在代码前后插入空行。

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

43. ![image-20240105192426917](LaTeX.assets/image-20240105192426917-1704516157721-16-1704516183762-73.png)

44. 要排版简短的代码或关键字，可使用\verb命令：

    ```latex
    \verb⟨delim⟩⟨code⟩⟨delim⟩ %⟨delim⟩符号用来标明代码的分界位置，前后必须一致，除字母、空格或星号外，可任意选择使得不与代码本身冲突，习惯上使用|符号。
    %同verbatim 环境，\verb 后也可以带一个星号，以显示空格
    \verb|\LaTeX|
    
    \verb+(a || b)+ \verb*+(a || b)+
    ```

45. ![image-20240105192813874](LaTeX.assets/image-20240105192813874-1704516157721-17-1704516183762-76.png)

46. \verb命令对符号的处理比较复杂，一般不能用在其它命令的参数里，否则多半会出错。verbatim 宏包优化了verbatim环境的内部命令，并提供了\verbatiminput命令用来直接读入文件生成代码环境。fancyvrb 宏包提供了可定制格式的Verbatim环境；listings宏包更进一步，可生成关键字高亮的代码环境，支持各种程序设计语言的语法和关键字和关键词加粗。

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

47. ![image-20240106024811696](LaTeX.assets/image-20240106024811696-1704516157721-18-1704516183762-75.png)


# 表格

1. 排版表格最基本的是tabular环境，直接使用tabular环境的话，会和周围的文字混排。但是通常情况下tabular环境很少与文字直接混排，而是会放在table浮动体环境中，并用\caption命令加标题。：

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

2. ![image-20240105193648370](LaTeX.assets/image-20240105193648370-1704516157721-19-1704516183762-77.png)

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

6. ![image-20240105194948173](LaTeX.assets/image-20240105194948173-1704516157721-20-1704516183762-78.png)

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

9. ![image-20240105200209634](LaTeX.assets/image-20240105200209634-1704516157721-21-1704516183762-79.png)

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

12. ![image-20240105201305824](LaTeX.assets/image-20240105201305824-1704516157721-22-1704516183762-80.png)

13. array宏包还提供了类似p格式的m格式和b格式，三者分别在垂直方向上靠顶端对齐、居中以及底端对齐。

14. 在控制列宽方面，LATEX 表格有着明显的不足：l/c/r 格式的列宽是由文字内容的自然宽度决定的，而p 格式给定了列宽却不好控制对齐（可用array 宏包的辅助格式），更何况列与列之间通常还有间距，所以直接生成给定总宽度的表格并不容易。

15. tabularx宏包为我们提供了方便的解决方案。它引入了一个X 列格式，类似p 列格式，不过会根据表格宽度自动计算列宽，多个X 列格式平均分配列宽。X 列格式也可以用array 里的辅助格式修饰对齐方式：

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

16. ![image-20240105202050423](LaTeX.assets/image-20240105202050423-1704516157721-23-1704516183762-81.png)

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

18. ![image-20240105202407972](LaTeX.assets/image-20240105202407972-1704516157721-24-1704516183762-82.png)

19. 三线表由booktabs 宏包支持，它提供了\toprule、\midrule 和\bottomrule 命令用以排版三线表的三条线，以及和\cline 对应的\cmidrule。除此之外，最好不要用其它横线以及竖线：

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

20. ![image-20240105202728473](LaTeX.assets/image-20240105202728473-1704516157721-25-1704516183762-83.png)

21. LaTeX是一行一行排版表格的，横向合并单元格较为容易，由\multicolumn命令实现。

22. LaTeX生成的表格看起来通常比较紧凑。修改参数\arraystretch可以得到行距更加宽松的表格。另一种增加间距的办法是给换行命令`\\`添加可选参数。

    ```latex
    \renewcommand\arraystretch{1.8}
    
    \\[6pt] %在这一行下面加额外的间距，适合用于在行间不加横线的表格
    ```

23. LaTeX本身不支持插图功能，需要由graphicx宏包辅助支持。

24. 使用latex + dvipdfmx 编译命令时，调用graphicx 宏包时要指定dvipdfmx 选项；而使用pdflatex 或xelatex 命令编译时不需要。事实上不同编译命令支持的图片格式种类也不同：

    ```latex
    格式                    矢量图         位图
    latex + dvipdfmx        .eps          N/A
       （调用bmpsize 宏包）  .eps .pdf    .jpg .png .bmp
    pdflatex                .pdf         .jpg .png
       （调用epstopdf 宏包） .pdf .eps    .jpg .png
    xelatex                 .pdf .eps    .jpg .png .bmp
    ```

25. 在调用了graphicx 宏包以后，就可以使用\includegraphics命令加载图片。

    ```latex
    \includegraphics[⟨options⟩]{⟨filename⟩} %图片文件的扩展名一般可不写。文件名里既不要有空格（类似\include），也不要有多余的英文点号。
    %可选参数可以使用⟨key⟩=⟨value⟩的形式给出
    width=⟨width⟩   %将图片缩放到宽度为⟨width⟩
    height=⟨height⟩ %将图片缩放到高度为⟨height⟩
    scale=⟨scale⟩   %将图片相对于原尺寸缩放⟨scale⟩倍
    angle=⟨angle⟩   %将图片逆时针旋转⟨angle⟩度
    ```

26. 另外graphicx宏包还提供了\graphicspath命令，用于声明一个或多个图片文件存放的目录，使用这些目录里的图片时可不用写路径：

    ```latex
    \graphicspath{{figures/}{logo/}}
    ```

27. graphicx 宏包也支持draft/final 选项。当graphicx 宏包或文档类指定draft 选项时，图片将不会被实际插入，取而代之的是一个包含文件名的与原图片等大的方框。

28. 盒子是LaTeX排版的基础单元，每一行是一个盒子，里面的文字从左到右依次排列；每一页也是一个盒子，各行文字从上到下依次排布。

29. 内容丰富的文章或者书籍往往包含许多图片和表格等内容。这些内容的尺寸往往太大，导致分页困难。LaTeX为此引入了浮动体的机制，令大块的内容可以脱离上下文，放置在合适的位置。

30. LaTeX预定义了两类浮动体环境figure 和table。习惯上figure 里放图片，table 里放表格，但并没有严格限制，可以在任何一个浮动体里放置文字、公式、表格、图片等等任意内容，也允许在一个浮动体里面放置多张图。

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

31. ![image-20240105212608227](LaTeX.assets/image-20240105212608227-1704516157721-26-1704516183762-84.png)

32. 限制包括浮动体个数（除单独成页外，默认每页不超过3 个浮动体，其中顶部不超过2 个，底部不超过1 个）以及浮动体空间占页面的百分比（默认顶部不超过70%，底部不超过30%）。

33. 双栏排版环境下，LATEX 提供了table* 和figure* 环境用来排版跨栏的浮动体。它们的用法与table和figure一样，不同之处为双栏的⟨placement⟩ 参数只能用tp两个位置。

34. 浮动体的位置选取受到先后顺序的限制。如果某个浮动体由于参数限制、空间限制等原因在当前页无法放置，就要推迟到之后处理，并使得之后的同类浮动体一并推迟。\clearpage 命令会在另起一页之前，先将所有推迟处理的浮动体排版成页，此时htbp 等位置限制被完全忽略。

35. float 宏包为浮动体提供了H 位置参数，不与htbp 及! 混用。使用H 位置参数时，会取消浮动机制，将浮动体视为一般的盒子插入当前位置。这在一些特殊情况下很有用（如使用multicol宏包排版分栏内容的时候），但尺寸过大的浮动体可能使得分页比较困难。

36. 图表等浮动体提供了\caption命令加标题，并且自动给浮动体编号。可以用带星号的命令\caption*9 生成不带编号的标题，不过要使用caption宏包。

37. 由于标题是横跨一行的，用\caption 命令为每个图片单独生成标题就需要借助\parbox或者minipage环境，将标题限制在盒子内。

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

38. ![image-20240105213751384](LaTeX.assets/image-20240105213751384-1704516157721-27-1704516183762-85.png)

39. 如果要给每个图片定义小标题，就要用到subcaption宏包。subcaption 依赖上文提到过的caption 宏包，因此也支持子图表标题样式的定制。并排子图表的功能也可通过subfig 宏包的\subfloat 命令实现


# 公式

1. AMS宏集合是美国数学学会(American Mathematical Society) 提供的对LATEX原生的数学公式排版的扩展，其核心是amsmath宏包，对多行公式的排版提供了有力的支持。此外，amsfonts宏包以及基于它的amssymb宏包提供了丰富的数学符号，amsthm宏包扩展了LATEX 定理证明格式。

2. 数学公式有两种排版方式：与文字混排的行内公式；单独列为一行的行间公式。

3. 行内公式由一对$ 符号包裹：

   ```latex
   The Pythagorean theorem is $a^2 + b^2 = c^2$.
   ```

4. ![image-20240105215132102](LaTeX.assets/image-20240105215132102-1704516157721-28-1704516183762-86.png)

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

6. ![image-20240105220308953](LaTeX.assets/image-20240105220308953-1704516157721-29-1704516183762-87.png)

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

8. ![image-20240106124701106](LaTeX.assets/image-20240106124701106.png)

9. 为了与文字相适应，行内公式在排版大的公式元素（分式、巨算符等）时显得很“局促”：

   ```latex
   $\lim_{n \to \infty}\sum_{k=1}^n \frac{1}{k^2}= \frac{\pi^2}{6}$.
   
   In display:
   \[ \lim_{n \to \infty}\sum_{k=1}^n\frac{1}{k^2}= \frac{\pi^2}{6} \]
   ```

10. ![image-20240106124929469](LaTeX.assets/image-20240106124929469.png)

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

       ![image-20240106125809479](LaTeX.assets/image-20240106125809479.png)

    5. ```latex
       \usepackage{amsmath}
       \usepackage{amssymb}
       \begin{document}
       $x^{2} \geq 0$\qquad for \textbf{all} $x\in\mathbb{R}$ %尽可能少的在公式中添加文本
       \end{document}
       ```

       ![image-20240106130111557](LaTeX.assets/image-20240106130111557.png)

13. LaTeX默认提供了常用的数学符号，amssymb宏包提供了一些次常用的符号。

14. 希腊字母符号的名称就是其英文名称，例如$\alpha$用`\alpha`表示。大写的希腊字母为首字母大写的命令，例如$\Delta$用`\Delta`表示。

15. 省略号有`\dots`和`\cdots`两种形式，有各自的用途：

    ```latex
    $a_1, a_2, \dots, a_n$ %这里使用cdots时，点就会比逗号的点高出一部分，不好看。
    
    $a_1 + a_2 + \cdots + a_n$ %这里使用cdots和dots结果一样，都会和+的水平线对齐。
    ```

16. ![image-20240106130643731](LaTeX.assets/image-20240106130643731.png)

17. `\ldots`和`\dots`是完全等效的，它们既能用在公式中，也用来在文本里作为省略号。在矩阵中可能会用到竖排的`\vdots`和斜排的`\ddots`。

    ```latex
    $a\vdots b\ddots c$
    ```

18. ![image-20240106131000277](LaTeX.assets/image-20240106131000277.png)

19. 导数符号`'`是一类特殊的上标，可以适当连用表示多阶导数，也可以在其后连用上标：

    ```latex
    $f(x) = x^2 \quad f'(x) = 2x \quad f''^{2}(x) = 4$
    ```

20. ![image-20240106131407462](LaTeX.assets/image-20240106131407462.png)

21. 分式的大小在行间公式中是正常大小，而在行内被极度压缩。amsmath提供了方便的命令\dfrac和\tfrac，令用户能够在行内使用正常大小的分式，或者在行间使用缩小的公式。

    ```latex
    In display style:
    \[
    3/8 \qquad \frac{3}{8} \qquad \tfrac{3}{8}
    \]
    In text style:
    $1\frac{1}{2}$ hours \qquad $1\dfrac{1}{2}$ hours
    ```

22. ![image-20240106131727591](LaTeX.assets/image-20240106131727591.png)

23. 根式命令`\sqrt[n]{}`有一个可选参数，用于表示开方的次数：

    ```latex
    $\sqrt[3]{2}$
    ```

24. ![image-20240106132450210](LaTeX.assets/image-20240106132450210.png)

25. 特殊的分式形式，如二项式结构，由amsmath宏包的\binom命令生成：

    ```latex
    \[ \binom{n}{k} =\binom{n-1}{k} + \binom{n-1}{k-1} \]
    ```

26. ![image-20240106132525160](LaTeX.assets/image-20240106132525160.png)

27. 常见的关系符号除了可以直接输入的=，>，<，其它符号用命令输入。大于等于或小于等于有两种样式，倾斜的关系符号由amssymb提供。

    ```latex
    $a\ge b$ $a \geqslant b$
    ```

28. ![image-20240106133217648](LaTeX.assets/image-20240106133217648.png)

29. LaTeX还提供了自定义二元关系符的命令\stackrel，用于将一个符号叠加在原有的二元关系符之上：

    ```latex
    \[ f_n(x) \stackrel{*}{\approx} 1 \]
    ```

30. ![image-20240106132914033](LaTeX.assets/image-20240106132914033.png)

31. LaTeX将数学函数的名称作为一个算符排版，字体为直立字体。其中有一部分符号在上下位置可以书写一些内容作为条件，类似于后文所叙述的巨算符。作为算符的函数名称汇总如下：

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

32. ![image-20240106133540022](LaTeX.assets/image-20240106133540022.png)

33. 如果LaTeX自带的算符不够用的话，amsmath允许用户在导言区用\DeclareMathOperator定义自己的算符，其中带星号的命令定义带上下限的算符：

    ```latex
    \usepackage{amsmath}
    \DeclareMathOperator{\argh}{argh}
    \DeclareMathOperator*{\nut}{Nut}
    \begin{document}
    \[\argh 3 = \nut_{x=1} 4x\]
    \end{document}
    ```

34. ![image-20240106133742697](LaTeX.assets/image-20240106133742697.png)

35. 积分号，求和号等符号被称为巨算符。他们在行内公式和行间公式的大小和形状有区别。

    ```latex
    $ \sum_{i=1}^n \quad\int_0^{\frac{\pi}{2}} \quad\oint_0^{\frac{\pi}{2}} \quad\prod_\epsilon $
    
    In display:
    \[ \sum_{i=1}^n \quad\int_0^{\frac{\pi}{2}} \quad\oint_0^{\frac{\pi}{2}} \quad\prod_\epsilon \]
    ```

36. ![image-20240106134133801](LaTeX.assets/image-20240106134133801.png)

37. 巨算符的上下标位置可由\limits和\nolimits调整，前者令巨算符的上下标位于正上下方，后者令巨算符的上下标位于右上方和右下方，类似于积分符号的。

    ```latex
    $\sum\limits_{i=1}^n \quad\int\limits_0^{\frac{\pi}{2}} \quad\prod\limits_\epsilon $
    
    In display:
    \[ \sum\nolimits_{i=1}^n \quad\int\limits_0^{\frac{\pi}{2}} \quad\prod\nolimits_\epsilon \]
    ```

38. ![image-20240106134511109](LaTeX.assets/image-20240106134511109.png)

39. amsmath宏包还提供了\substack，能够在下限位置书写多行表达式；subarray 环境更进一步，令多行表达式可选择居中(c) 或左对齐(l)：

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

40. ![image-20240106134657226](LaTeX.assets/image-20240106134657226.png)

41. 数学符号可以像文字一样加重音，使用时要注意重音符号的作用区域，一般应当对某个符号而不是“符号加下标”使用重音。

    ```latex
    $\bar{x_0} \quad \bar{x}_0$
    
    $\vec{x_0} \quad \vec{x}_0$
    
    $\hat{\mathbf{e}_x}\quad\hat{\mathbf{e}}_x$
    ```

42. ![image-20240106134913077](LaTeX.assets/image-20240106134913077.png)

43. LaTeX也能为多个字符加重音，

    ```latex
    $0.\overline{3} =\underline{\underline{1/3}}$
    
    $\hat{XY} \qquad \widehat{XY}$
    
    $\vec{AB} \qquad \overrightarrow{AB}$
    ```

44. ![image-20240106135145752](LaTeX.assets/image-20240106135145752.png)

45. LATEX 提供了多种括号和定界符表示公式块的边界，如小括号`()`、中括号`[]`、大括号`{}`、尖括号`⟨⟩`（\langle，\rangle)等。使用\left和\right命令可令括号（定界符）的大小可变，在行间公式中常用。LaTeX会自动根据括号内的公式大小决定定界符大小。二者必须成对使用。需要使用单个定界符时，另一个定界符写成`\left.`或`\right.`。

    ```latex
    \[
    1 + \left( \frac{1}{1-x^{2}} \right)^3 \qquad \left. \frac{\partial f}{\partial t} \right|_{t=0}
    \]
    ```

46. ![image-20240106203414230](LaTeX.assets/image-20240106203414230.png)

47. 还可以用\big、\bigg等命令生成固定大小的定界符，这些不必成对出现，这使得它可以被断行，这是比`\left`和`\right`好的点。

    ```latex
    $\Bigl((x+1)(x-1)\Bigr)^{2}$
    
    $\bigl( \Bigl( \biggl( \Biggl( \quad
    \bigr\} \Bigr\} \biggr\} \Biggr\} \quad
    \big\| \Big\| \bigg\| \Bigg\| \quad    %||得到的结果不是一样长的竖线
    \big\Downarrow \Big\Downarrow \bigg\Downarrow \Bigg\Downarrow$
    ```

48. ![image-20240106204003183](LaTeX.assets/image-20240106204003183.png)

49. 通常来讲应当避免写出超过一行而需要折行的长公式。如果一定要折行的话，优先在等号前折行，其次在加号、减号之前，再次在乘号、除号之前。其它位置应当避免折行。

50. amsmath宏包的multline环境提供了书写折行长公式的方便环境。它允许用`\\`折行，公式编号在最后一行。多行公式的首行左对齐，末行右对齐，其余行居中。

    ```latex
    \begin{multline}
    a + b + c + d + e + f + g + h + i \\
    	= j + k + l + m + n\\
    	= o + p + q + r + s\\
    	= t + u + v + x + z
    \end{multline}
    ```

51. ![image-20240106205252434](LaTeX.assets/image-20240106205252434.png)

52. 与表格不同的是，公式的最后一行不应写`\\`，如果写了，反倒会产生一个多余的空行。类似equation\*，multline\* 环境排版不带编号的折行长公式。

53. 更多的情况是，我们需要罗列一系列公式，并令其按照等号对齐：

54. LATEX 提供了eqnarray 环境。它按照等号左边——等号——等号右边呈三列对齐，但等号周围的空隙过大，加上公式编号等一些bug，目前已不推荐使用。

55. 目前最常用的是align环境，它将公式用&隔为两部分并对齐。分隔符通常放在等号左边：

    ```latex
    \begin{align}
    	a & = b + c \\
    	& = d + e
    \end{align}
    ```

56. ![image-20240106210002728](LaTeX.assets/image-20240106210002728.png)

57. align环境会给每行公式都编号。我们仍然可以用\notag去掉某行的编号。为了对齐等号，将分隔符放在右侧，并且此时需要在等号后添加一对括号{}以产生正常的间距：

    ```latex
    \begin{align}
    	a ={} & b + c \\
    	={} & d + e + f + g + h + i + j + k + l \notag \\
    	={} & p + q + r + s
    \end{align}
    ```

58. ![image-20240106211057402](LaTeX.assets/image-20240106211057402.png)

59. 将多个公式组在一起公用一个编号，编号位于公式的居中位置。amsmath宏包提供了诸如aligned、gathered等环境，与equation环境套用。aligned环境可以用定界符包裹。

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

60. ![image-20240106210414383](LaTeX.assets/image-20240106210414383.png)

61. 为了排版矩阵，LaTeX提供了array环境，用法与tabular环境极为类似，也需要定义列格式，并用`\\`换行。矩阵可作为一个公式块，在外套用`\left`、`\right`等定界符：

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

62. ![image-20240106211453943](LaTeX.assets/image-20240106211453943.png)

63. 分段函数排版：

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

64. ![image-20240106211841026](LaTeX.assets/image-20240106211841026.png)

65. 可以用array环境排版各种矩阵。amsmath宏包还直接提供了多种排版矩阵的环境，包括不带定界符的matrix，以及带各种定界符的矩阵pmatrix，bmatrix，Bmatrix，vmatrix，Vmatrix。使用这些环境时，无需给定列格式，事实上这些矩阵内部也是用array环境生成的，列格式默认为*{⟨n⟩}{c}，⟨n⟩ 默认为10：

    ```latex
    matrix  %没有定界符
    pmatrix %小括号
    bmatrix %中括号
    Bmatrix %大括号
    vmatrix %单竖线
    Vmatrix %双竖线
    ```

66. 如果矩阵中的元素包含分式时，要用到\dfrac等命令，行与行之间有可能紧贴着，因此需要使用

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

67. ![image-20240106214407804](LaTeX.assets/image-20240106214407804.png)

68. 绝大部分时候，数学公式中各元素的间距是根据符号类型自动生成的，需要手动调整的情况极少。一般用命令\quad和\qquad生成间距。还可以使用\,、\:、\; 以及负间距\!。文本中的\␣ 也能使用在数学公式中。

    ```latex
    aa   %无额外间距
    
    a\,a %1个空格
    
    a\:a %1个空格
    
    a\;a %1个空格
    
    a\quad{}a  %2个空格
    
    a\qquad{}a %4个空格
    
    a\!a   %负1个空格
    ```

69. ![image-20240106221522052](LaTeX.assets/image-20240106221522052.png)

70. 常见的用途是在被积函数f(x)和dx之间增加一个微小的距离。注意微元里的d用的是直立体。

    ```latex
    \[
    \int_a^b f(x)\mathrm{d}x
    \qquad
    \int_a^b f(x)\,\mathrm{d}x
    \]
    ```

71. ![image-20240106220746345](LaTeX.assets/image-20240106220746345.png)

72. 另一个用途是生成多重积分号。如果我们直接连写两个\int，之间的间距将会过宽，此时可以使用负间距`\!`对其修正。不过amsmath提供了更方便的多重积分号，如二重积分\iint、三重积分\iiint等。

    ```latex
    \begin{gather*}
    	\int\int f(x)g(y)\diff x \diff y \\
    	\int\!\!\!\int f(x)g(y) \diff x \diff y \\
    	\iint f(x)g(y) \diff x \diff y \\
    	\iint \quad \iiint \quad \idotsint
    \end{gather*}
    ```

73. LaTeX允许一部分数学符号切换字体，主要是拉丁字母、数字、大写希腊字母以及重音符号等。

74. 

75. 

76. 

77. 

78. 

79. 

80. 

81. 

82. 

83. 

84. 

85. 在ctexset中修改punct键的值

86. ![img](LaTeX.assets/f69e9ce9-9bd4-454f-98a0-45aae8aff908.png)

87. ctexart文档类的可选项，scheme=<chinese|plain>  前者调整默认的字号为5号，调整行距为1.3，汉化各级标题名称（图，表，目录，参考文献等）；后者只提供中文支持，不做任何修改，适合于在英文排版文稿中插入少量中文。

88. 

89. 

90. 

91. LaTeX的目录都是自动生成的，命令是\tableofcontents这会单独生成一个章节，标题为Content，若使用ctex包，标题为“目录”。

92. 自定义目录样式  使用tocloft宏包，进行简单修改，复杂修改使用titletoc宏包。

93. 使用 tocbibind 宏包来为目录项中增加参考文献，目录项本身，索引，图列表，表列表等项目，默认全部增加。可以指定可选参数，不添加某一项。

94. \addcontentsline{toc}{⟨level⟩}{⟨title⟩} 添加在有*的章节标题命令之后，此时正文中不显示序号，但是在目录中会显示。

95. 使用titlepage参数的标题是垂直居中的，而在maketitle之后使用\newpage，并不是居中的，而是在较靠上的地方。

96. ![img](LaTeX.assets/081f803d-0ac0-4203-8da1-da3821238afa.jpg)

97. ![img](LaTeX.assets/4a7b90b1-4d19-48e3-a8b2-4ab75b7418b0.png)

98. 摘要环境abstract默认只在标准文档类中的article和report文档类可用。一般紧跟在\maketitle之后。

99. 标记符号前后不用加空格。

100. 

101. \underline{abc}为{}内的内容添加下划线。此方法无法换行，不够美观。可以使用ulem宏包中的\uline来解决问题。

102. ![img](LaTeX.assets/11045d24-535b-45f2-9041-15376746200f.png)

103. ![img](LaTeX.assets/2dd14a20-5d55-4750-9f94-285638ab2766.png)

104. ![img](LaTeX.assets/8f4e5c5f-2e27-4042-a5c4-c829b53370d2.png)

105. 
