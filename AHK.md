# 基础

1. AHK，开发以后十多年的历史，是Windows平台自动化的佼佼者。代码不区分大小写。

2. 快速使用 AutoHotkey 最简单的方法是使用示例代码，试用它并根据需要进行调整。

3. 如果发送了一个按下键的指令而不发送抬起键的指令。按键就会"卡在下面"，在这种情况下，退出脚本还不够，因为操作系统仍然认为键被按住了。此时可以通过物理按压来 "松开" 这个键。

4. 如果文件包含非ASCII字符，请确保将文件保存为带有BOM(字节顺序标记)的UTF-8。虽然AHK支持Unicode文本，但它是为了向后兼容而优化的，这意味着==默认为 ANSI 编码==，而不是国际上推荐的 UTF-8。所以除非以字节顺序标记开始，否则AHK不会自动识别UTF-8文件。

5. 没有缩进，AHK脚本也可以正常运行。

6. 默认提供了多种ahk可执行程序。

   ```shell
   AutoHotkey.exe
   AutoHotkeyA32.exe #A32 或 /ANSI: ANSI 32 位
   AutoHotkeyU32.exe #U32: Unicode 32 位
   AutoHotkeyU64.exe #默认的是A64。U64 或 /x64: Unicode 64 位(仅在 64 位系统中有效)
   ```

7. AHK的计数默认从1开始。AutoHotkey没有特定的布尔类型，因此它使用整数值 `0` 表示假，而 `1` 表示真。单词 `true` 和 `false` 是值分别为 1 和 0 的内置变量，使用它们可以增加脚本的可读性。

8. AutoHotkey中没有像其他语言那样有一个独特的表示`nothing，null，nil` 或 `undefined(未定义)`的值。一般用""，空字符串来代替。

9. 对正在运行中的脚本进行编辑保存后不会立即生效。可以通过脚本的托盘图标或Reload函数来重新加载以生效，也可以从热键调用该函数。在许多情况下，也可以通过简单地再次运行脚本来实现，但这需要脚本设置了单例模式#SingleInstance。

10. 脚本可以被编译成一个二进制文件EXE，脱离ahk使用。

11. 两种对脚本的特殊操作：

    1.  Suspend Hotkeys，挂起热键，即通过::定义的热键暂时失效。
    2.  Pause Script，暂停脚本，脚本定义的所有功能，包含热键和正在进行的循环都会停止。

12. `#NoTrayIcon`可以隐藏托盘图标。

13. ；后面的内容是注释。

14. 尽量要在一行放下多个命令或者嵌套多层。

15. AutoHotkey可以做的最简单和最有用的事情就是是创建启动程序的键盘快捷键(热键)。

16. 通过调用Run函数启动程序，将程序的命令行作为该函数的参数：

    ```
    Run "C:\Windows\notepad.exe"    ;会直接启动记事本。此时还没有定义热键，所以函数立即执行，然后自动退出。
    ```

17. Run也可以用来打开文档，文件夹和 URL，这类似于Win+R的功能。

18. 有些程序已经在系统中注册了它们的路径，在这种情况下，你可以只传递程序的文件名，.exe的扩展名也可以省略，例如：

    ```
    Run "notepad"
    Run "notepad.exe"
    Run "notepad C:\license.txt"  ;程序的命令行参数也包含在第一个参数的字符串中。
    ```

19. 如果使用写字板wordpad打开文件时，不能直接使用如下形式：

    ```
    Run "wordpad C:\license.txt"
    ;会报如下错误，可见ahk将整个字符串都当作可执行文件名了，当然找不到这样的一个可执行文件了。
    Error: Failed attempt to launch program or document:
    Action: <wordpad C:\license.txt>
    Params: <>
    ;此时需要显式将可执行文件名和后续的参数区分开，可以有如下方法：
    Run "wordpad.exe C:\license.txt" ;给可执行文件加上.exe后缀名来让ahk识别出这个是可执行文件名
    Run "C:\Program Files\Windows NT\Accessories\wordpad C:\license.txt" ;使用可执行文件的完整路径
    ```

20. 诡异的是，单独运行wordpad不加参数`Run "wordpad"`是可以的。主要原因是wordpad程序不在PATH环境变量中目录中。

21. 如果某个命令行参数中包含空格，则需要将该参数用双引号（不过要用`来转义）或单引号括起来。这对于记事本来说是不必要的，但是记事本是一般规则的一个例外。编写代码的方式会影响到 Run 函数中实际使用的引号。例如：

    ```
    Run "wordpad.exe `"C:\Program Files\AutoHotkey\license.txt`""  ;`转义
    Run 'wordpad.exe "C:\Program Files\AutoHotkey\license.txt"'    ;需要在外部使用单引号，内部使用双引号，因为Windows的命令行只识别双引号
    Run "wordpad.exe 'C:\Program Files\AutoHotkey\license.txt'"    ;外双内单会报错
    ```

22. AHK定义了许多内置变量，脚本可以直接读取，例如：

    ```
    A_ComSpec   包含与ComSpec环境变量相同的字符串,通常是命令提示符可执行文件(cmd.exe)的完整路径
    A_ProgramFiles  记录了Program Files目录的路径
    ```

23. 热键和热字符串，是AHK的两种主要快捷方式。

24. ```
    ^j::   ;按下Ctrl+j时，会执行下面的命令，键入My First Script这些字符。
    	Send，My First Script
    Return
    
    ::ftw::Free The Whales         ;输入ftw 然后按下默认的终止符都会激活该热字符串，把ftw替换为Free The Whales
    
    ::btw::            ;热字符串也可以触发命令
        MsgBox you typed btw
    Return
    
    终止符最开始由以下内容组成: -()[]{}':;"/\,.?!`n `t(注意 `n 是 Enter，`t 是 Tab，且在它们之间还有一个原义的空格).
    ```

25. ==热键命令可以换行，可以不换行。但是热字符串替换必须要在同一行。热字符串的命令必须换行。==

26. <img src="AHK.assets/image-20210124210202635.png" alt="image-20210124210202635" style="zoom: 50%;" />

27. 定义组合热键：

    ```
    Numpad0 & Numpad1::       ;按住小键盘数字键0的同时，再按下小键盘数字键1。顺序不能乱。
    MsgBox You pressed Numpad1 while holding down Numpad0.
    Return
    ```

28. 有时候你也许想要热键或热字串只在某些特定窗口上工作(或禁用)。即窗口特定的热键/热字符串。需要使用#开头的命令（#IfWinActive      #IfWinExist)，这些被称为高级命令。可以创建对上下文敏感的热键和热字串。

29. 如果要关闭上下文敏感性，可以使用任意 \#IfWin 指令，但将其所有参数留空即可。

30. ```
    #IfWinActive 无标题 - 记事本  ; 判断该窗口是否被激活。如果是的话，在收到该热键的信号时，才会做出相应。
    #space::
    MsgBox You pressed Win+Spacebar in Notepad.
    Return
    
    #IfWinActive
    !q::
    MsgBox，You pressed Alt+Q in any window.
    Return
    ```

31. 如果 #ifwin 指令在脚本中从未使用，所有的热键和热字串对所有窗口生效。 #ifwin 指令影响他之后的所有热键和热字符串，直到遇到一个新的 #ifwin 指令。

32. 加粗标签的例子

33. ```
    ^b::                                         ; Ctrl+B 热键
    Send，{ctrl down}c{ctrl up}                  ; 复制选定的文本。也可以使用 ^c，但这种方法更加可靠.
    SendInput，[b]{ctrl down}v{ctrl up}[/b]      ; 粘贴所复制的文本，并在文本前后加上加粗标签.
    Return                                       ; 热键内容结束，这之后的内容将不会触发.
    ```

34. Send 命令可以发送按键，模拟打字或按键操作。       ！A  等价于!+a     按键是要区分大小写的。如果不确定，请使用小写字母。

35. ```
    例如，Send +abC 会发送文本 "AbC"，而 Send !+a 会按下 Alt+Shift+a.
    ```

36. **花括号是重要的**。它将告诉 AutoHotkey `{!}` 表示 "感叹号"，而不是要 "按下 Alt 键"。

37. 当你使用 Ctrl 或 Enter(或其他按键) 作为热键时，不要将它们括在 {} 中。

38. ```
    ; 当你创建热键时...
    {LCtrl}::         ; 错误的
    Send，AutoHotkey
    Return
    
    LCtrl::           ; 正确的
    Send，AutoHotkey
    Return
    
    Send，Multiple Enter lines have Enter been sent。; 错误
    Send，Multiple{Enter}lines have{Enter}been sent。; 正确       不会输出Enter这几个字符，而是按下Enter键。
    ```

39. 当时用Send命令时，如果后面的内容不再特殊按键列表中，那么就没必要加上{}。

40. 想要表示按住或松开某个按键，可以将这个键用花括号围起来，同时加上单词 UP 或 DOWN

    ```
    Send，^s                     ; 都表示发送 CTRL+s 键击
    Send，{ctrl down}s{ctrl up}  ; 都表示发送 CTRL+s 键击
    Send，{ctrl down}c{ctrl up}
    Send，{b down}{b up}
    Send，{Tab down}{Tab up}
    Send，{Up down}  ; 按下向上键.
    Sleep，1000      ; 保持 1 秒.
    Send，{Up up}    ; 然后松开向上键.
    ```

41. ```
    MsgBox yo!!      双击会弹出一个对话框，显示yo!!。这个msbbox是命令，其后是参数。使用简洁。
    ```

42. 如果想要把一个命令指定一个快捷键，可以用::来设置，例如：

43. ```
    ^1::MsgBox yo!!       双击不会有任何反应，脚本会在后台监听键盘的输入。一旦按下Ctrl+1，则会执行后面的命令，弹出对话框。没有指定快捷键的脚本不会进入后台。
    ```

44. 脱字符^代表Ctrl键。！代表Alt键，+代表Shift键。他们之间可以组合，例如 ^!1表示同时按下Ctrl，alt，1。前面加上<或>，则表示按下的是键盘的左侧或右侧的对应键。

45. 这里的数字默认是字母上方的，不是小键盘的。

46. 如果命令有多行，则需要在代码结束的默认添加一个return。这样执行到此处就会停止。

47. hotstring，热字符串的功能，可以自动将你输入的字符串替换为另一个字符串。

48. ```
    ::kiss::hha       当输入kiss，再按下tab键后，会自动将kiss替换为hha。 空格也会被替换。
    ```

49. 发送按键命令Send，可以模拟一个按键操作。也可以发送一个字符串。

50. ```
    send ^a      代表按下Ctrl+a键
    ```

51. AHK中逗号是用来分隔参数的，如果要输出逗号，则用`转义。

52. ```
    >!a::MsgBox hha
    !z::Send bilibili4
    ```

53. Run 命令可以启动其他程序。

54. ```
    !r::Run notepad.exe              ;有些程序需要写出绝对路径
    !s::Run http://www.baidu.com      会打开浏览器，调到指定网页。
    ```

55. 窗口相关操作：

56. ```
    WinActivate 窗口名            切换到该窗口。窗口名可以在任务管理器中找到。
    WinWaitActive 窗口名          等待该窗口切换完成后再运行之后的命令。
    ```

57. ```
    ^!n::             ; Ctrl+Alt+N       这段脚本用来判断是否存在一个新的记事本，如果有就就将其激活，否则就新建一个。
    if WinExist("无标题 - 记事本")
        WinActivate
    else
        Run Notepad
    return
    ```

58. AutoHotkey 有两个重要的工具供开发者使用: 命令和函数。命令后面的参数无需使用圆括号，而函数需要使用。

59. ```
    Command，参数1，参数2，参数3
    
    Function(参数1，参数2，参数3)
    ```

60. 跟函数不同的是，命令使用 "传统语法"。不能将几条命令放在同一行。

61. ```
    MsgBox，Hello，Run，Notepad.exe     ; 错误
    MsgBox，Hello                       ; 正确
    Run，Notepad.exe                    ; 正确
    ```

62. 函数内的参数可以使用运算，变量不需要加%，可以嵌套另一个函数，不过文本前后需要加上" "。函数通常会返回一个值，这一点与命令也不一样。

63. ```
    SubStr(37 * 12，1，2)
    
    SubStr(A_Now，7，2)
    
    SubStr(A_Now，7，2)
    
    SubStr(A_AhkPath，InStr(A_AhkPath，"AutoHotkey"))
    
    SubStr("I'm scripting，awesome!"，16)
    ```

64. ```
    MyVar := SubStr("I'm scripting，awesome!"，16)            ;将函数值赋值给变量
    ```

65. 代码块就是用一对花括号 {  }  包围起来的一段代码。经常用在if和loop中。如果不适用 { } ，那就只有下面的第一行代码被执行。

66. 变量的赋值方法：

67. ```MyVar = Text
    MyVar = Text             ;传统的文本赋值方法。
    MyVar = %MyVar2%         ;传统的变量赋值。
    MyVar = %MyVar2% some text %MyVar3%。        ;传统的混合赋值。
    MyVar := "Text"                 ;表达式文本赋值。
    MyVar := MyVar2                  ;表达式变量赋值。
    MyVar := 6 + 8 / 3 * 2 - Sqrt(9)    ;表达式数字赋值。
    MyVar := "The value of 5 + " MyVar2 " is: " 5 + MyVar2     ;表达式的混合赋值
    在表达式模式中，字符串需要加""，变量不用加%%。
    ```

68. 变量赋值的例子：

69. ```
    ; 下面的例子展示了什么时候该使用百分号，什么时候不该.
    Var = Text  ; 赋值一些文本给一个变量(传统的).
    Number := 6  ; 赋值一个数字给一个变量(表达式).
    Var2 = %Var%  ; 赋值一个变量给另一个(传统的).
    Var3 := Var  ; 赋值一个变量给另一个(表达式).
    Var4 .= Var  ; 追加一个变量到另一个的末尾(表达式).
    Var5 += Number  ; 将变量的值与另一个相加(表达式).
    Var5 -= Number  ; 将变量的值减去另一个(表达式).
    Var6 := SubStr(Var，2，2)  ; 变量在函数中。这总是一个表达式.
    Var7 = %Var% Text  ; 赋值一个变量给另一个变量并带有一些额外的文本(传统的).
    Var8 := Var " Text"  ; 赋值一个变量给另一个变量并带有一些额外的文本(表达式).
    MsgBox，%Var%  ; 变量在命令中.
    StringSplit，Var，Var，x  ; 在命令中的变量，但是它们作为输入或输出变量.
    if (Number = 6)  ; 只要 IF 有括号，它就是一个表达式，所以不需要百分号.
    if (Var != Number)  ; 只要 IF 有括号，它就是一个表达式，所以不需要百分号.
    if Number = 6  ; 如果没有括号，那么 IF 是传统的。不过，只有赋值语句"右边"的变量需要百分号。
    if Var1 < %Var2%  ; 如果没有括号，那么 IF 是传统的。不过，只有赋值语句"右边"的变量需要百分号。
    ```

70. 对象是更高一级的组织数据的方式。可以使数组和键值对。

71. 创建对象的方法：

72. ```
    MyObject := ["one"，"two"，"three"，17]      ;索引数组
    
    Banana := {"Color": "Yellow"，"Taste": "Delicious"，"Price": 3}     ;关联数组，键值对的集合。
    
    MyObject := Array("one"，"two"，"three"，17)    ;利用数组函数来创建数组
    
    Banana := Object("Color"，"Yellow"，"Taste"，"Delicious"，"Price"，3)     ;利用对象函数，来创建关联数组，键值对。
    ```

73. 使用对象的值：

74. ```
    Banana["Pickled"] := True          ;给Banana对象中的Pickled键赋予True的值。
    Banana.Consistency := "Mushy"      ;同上
    如果想要往对象中添加一个新的键值对，指定给一个原本不存在的键即可。
    ```