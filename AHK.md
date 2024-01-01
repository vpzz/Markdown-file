# 基础

1. AHK，开发以后十多年的历史，是Windows平台自动化的佼佼者。不区分大小写。

2. 如果文件包含非 ASCII 字符, 请确保将文件保存为带有 BOM(字节顺序标记) 的 UTF-8。虽然 AutoHotkey 支持 Unicode 文本, 但它是为了向后兼容而优化的, 这意味着==默认为 ANSI 编码==, 而不是国际上推荐的 UTF-8. 所以除非以字节顺序标记开始, 否则 AutoHotkey 不会自动识别 UTF-8 文件。

3. 没有缩进，AHK脚本也可以正常运行。

4. 默认提供了多种ahk可执行程序。

   ```shell
   AutoHotkey.exe
   AutoHotkeyA32.exe #A32 或 /ANSI: ANSI 32 位
   AutoHotkeyU32.exe #U32: Unicode 32 位
   AutoHotkeyU64.exe #默认的是A64。U64 或 /x64: Unicode 64 位(仅在 64 位系统中有效)
   ```

5. AHK的计数默认从1开始。AutoHotkey 没有特定的布尔类型，因此它使用整数值 `0` 表示假，而 `1` 表示真。单词 `true` 和 `false` 是值分别为 1 和 0 的内置变量。使用它们可以增加脚本的可读性。

6. AutoHotkey 中没有像其他语言那样有一个独特的表示 *nothing*, *null*, *nil* 或 *undefined(未定义)* 的值。一般用""，空字符串来代替。

7. 对正在运行中的脚本进行编辑，保存后，reload才会生效。脚本可以被编译成一个二进制文件EXE，脱离ahk存在。

8. 两种对脚本的特殊操作：

   1.  Suspend Hotkeys，挂起热键，即通过::定义的热键暂时失效。
   2.  Pause Script，暂停脚本，脚本定义的所有功能，包含热键和正在进行的循环都会停止。

9. \#NoTrayIcon    可以隐藏托盘图标。；后面的内容是注释。

10. 尽量要在一行放下多个命令或者嵌套多层。

11. 热键和热字符串，是AHK的两种主要快捷方式。

12. ```
    ^j::              ;按下Ctrl+j时，会执行下面的命令，键入My First Script这些字符。
    	Send, My First Script
    Return
    
    ::ftw::Free The Whales         ;输入ftw 然后按下默认的终止符都会激活该热字符串，把ftw替换为Free The Whales
    
    ::btw::            ;热字符串也可以触发命令
        MsgBox you typed btw
    Return
    
    终止符最开始由以下内容组成: -()[]{}':;"/\,.?!`n `t(注意 `n 是 Enter, `t 是 Tab, 且在它们之间还有一个原义的空格).
    ```

13. ==热键命令可以换行，可以不换行。但是热字符串替换必须要在同一行。热字符串的命令必须换行。==

14. <img src="AHK.assets/image-20210124210202635.png" alt="image-20210124210202635" style="zoom: 50%;" />

15. 定义组合热键：

    ```
    Numpad0 & Numpad1::       ;按住小键盘数字键0的同时，再按下小键盘数字键1。顺序不能乱。
    MsgBox You pressed Numpad1 while holding down Numpad0.
    Return
    ```

16. 有时候你也许想要热键或热字串只在某些特定窗口上工作(或禁用)。即窗口特定的热键/热字符串。需要使用#开头的命令（#IfWinActive      #IfWinExist)，这些被称为高级命令。可以创建对上下文敏感的热键和热字串。

17. 如果要关闭上下文敏感性，可以使用任意 \#IfWin 指令, 但将其所有参数留空即可。

18. ```
    #IfWinActive 无标题 - 记事本  ; 判断该窗口是否被激活。如果是的话，在收到该热键的信号时，才会做出相应。
    #space::
    MsgBox You pressed Win+Spacebar in Notepad.
    Return
    
    #IfWinActive
    !q::
    MsgBox, You pressed Alt+Q in any window.
    Return
    ```
    
19. 如果 #ifwin 指令在脚本中从未使用, 所有的热键和热字串对所有窗口生效。 #ifwin 指令影响他之后的所有热键和热字符串，直到遇到一个新的 #ifwin 指令。

20. 加粗标签的例子

21. ```
    ^b::                                         ; Ctrl+B 热键
    Send, {ctrl down}c{ctrl up}                  ; 复制选定的文本. 也可以使用 ^c, 但这种方法更加可靠.
    SendInput, [b]{ctrl down}v{ctrl up}[/b]      ; 粘贴所复制的文本, 并在文本前后加上加粗标签.
    Return                                       ; 热键内容结束, 这之后的内容将不会触发.
    ```

22. Send 命令可以发送按键, 模拟打字或按键操作。       ！A  等价于!+a     按键是要区分大小写的。如果不确定, 请使用小写字母。

23. ```
    例如, Send +abC 会发送文本 "AbC", 而 Send !+a 会按下 Alt+Shift+a.
    ```

24. **花括号是重要的**. 它将告诉 AutoHotkey `{!}` 表示 "感叹号", 而不是要 "按下 Alt 键"。

25. 当你使用 Ctrl 或 Enter(或其他按键) 作为热键时, 不要将它们括在 {} 中。

26. ```
    ; 当你创建热键时...
    {LCtrl}::         ; 错误的
    Send, AutoHotkey
    Return
    
    LCtrl::           ; 正确的
    Send, AutoHotkey
    Return
    
    Send, Multiple Enter lines have Enter been sent. ; 错误
    Send, Multiple{Enter}lines have{Enter}been sent. ; 正确       不会输出Enter这几个字符，而是按下Enter键。
    ```
    
27. 当时用Send命令时，如果后面的内容不再特殊按键列表中，那么就没必要加上{}。

28. 想要表示按住或松开某个按键, 可以将这个键用花括号围起来, 同时加上单词 UP 或 DOWN

    ```
    Send, ^s                     ; 都表示发送 CTRL+s 键击
    Send, {ctrl down}s{ctrl up}  ; 都表示发送 CTRL+s 键击
    Send, {ctrl down}c{ctrl up}
    Send, {b down}{b up}
    Send, {Tab down}{Tab up}
    Send, {Up down}  ; 按下向上键.
    Sleep, 1000      ; 保持 1 秒.
    Send, {Up up}    ; 然后松开向上键.
    ```

29. ```
    MsgBox yo!!      双击会弹出一个对话框，显示yo!!。这个msbbox是命令，其后是参数。使用简洁。
    ```

30. 如果想要把一个命令指定一个快捷键，可以用::来设置，例如：

31. ```
    ^1::MsgBox yo!!       双击不会有任何反应，脚本会在后台监听键盘的输入。一旦按下Ctrl+1，则会执行后面的命令，弹出对话框。没有指定快捷键的脚本不会进入后台。
    ```

32. 脱字符^代表Ctrl键。！代表Alt键，+代表Shift键。他们之间可以组合，例如 ^!1表示同时按下Ctrl，alt，1。前面加上<或>，则表示按下的是键盘的左侧或右侧的对应键。

33. 这里的数字默认是字母上方的，不是小键盘的。

34. 如果命令有多行，则需要在代码结束的默认添加一个return。这样执行到此处就会停止。

35. hotstring，热字符串的功能，可以自动将你输入的字符串替换为另一个字符串。

36. ```
    ::kiss::hha       当输入kiss，再按下tab键后，会自动将kiss替换为hha。 空格也会被替换。
    ```

37. 发送按键命令Send，可以模拟一个按键操作。也可以发送一个字符串。

38. ```
    send ^a      代表按下Ctrl+a键
    ```

39. AHK中逗号是用来分隔参数的，如果要输出逗号，则用`转义。

40. ```
    >!a::MsgBox hha
    !z::Send bilibili4
    ```

41. Run 命令可以启动其他程序。

42. ```
    !r::Run notepad.exe              ;有些程序需要写出绝对路径
    !s::Run http://www.baidu.com      会打开浏览器，调到指定网页。
    ```

43. 窗口相关操作：

44. ```
    WinActivate 窗口名            切换到该窗口。窗口名可以在任务管理器中找到。
    WinWaitActive 窗口名          等待该窗口切换完成后再运行之后的命令。
    ```

45. ```
    ^!n::             ; Ctrl+Alt+N       这段脚本用来判断是否存在一个新的记事本，如果有就就将其激活，否则就新建一个。
    if WinExist("无标题 - 记事本")
        WinActivate
    else
        Run Notepad
    return
    ```

46. AutoHotkey 有两个重要的工具供开发者使用: 命令和函数。命令后面的参数无需使用圆括号, 而函数需要使用。

47. ```
    Command, 参数1, 参数2, 参数3
    
    Function(参数1, 参数2, 参数3)
    ```

48. 跟函数不同的是, 命令使用 "传统语法"。不能将几条命令放在同一行。

49. ```
    MsgBox, Hello, Run, Notepad.exe     ; 错误
    MsgBox, Hello                       ; 正确
    Run, Notepad.exe                    ; 正确
    ```

50. 函数内的参数可以使用运算，变量不需要加%，可以嵌套另一个函数，不过文本前后需要加上" "。函数通常会返回一个值, 这一点与命令也不一样。

51. ```
    SubStr(37 * 12, 1, 2)
    
    SubStr(A_Now, 7, 2)
    
    SubStr(A_Now, 7, 2)
    
    SubStr(A_AhkPath, InStr(A_AhkPath, "AutoHotkey"))
    
    SubStr("I'm scripting, awesome!", 16)
    ```

52. ```
    MyVar := SubStr("I'm scripting, awesome!", 16)            ;将函数值赋值给变量
    ```

53. 代码块就是用一对花括号 {  }  包围起来的一段代码。经常用在if和loop中。如果不适用 { } ，那就只有下面的第一行代码被执行。

54. 变量的赋值方法：

55. ```MyVar = Text
    MyVar = Text             ;传统的文本赋值方法。
    MyVar = %MyVar2%         ;传统的变量赋值。
    MyVar = %MyVar2% some text %MyVar3%.         ;传统的混合赋值。
    MyVar := "Text"                 ;表达式文本赋值。
    MyVar := MyVar2                  ;表达式变量赋值。
    MyVar := 6 + 8 / 3 * 2 - Sqrt(9)    ;表达式数字赋值。
    MyVar := "The value of 5 + " MyVar2 " is: " 5 + MyVar2     ;表达式的混合赋值
    在表达式模式中，字符串需要加""，变量不用加%%。
    ```

56. 变量赋值的例子：

57. ```
    ; 下面的例子展示了什么时候该使用百分号, 什么时候不该.
    Var = Text  ; 赋值一些文本给一个变量(传统的).
    Number := 6  ; 赋值一个数字给一个变量(表达式).
    Var2 = %Var%  ; 赋值一个变量给另一个(传统的).
    Var3 := Var  ; 赋值一个变量给另一个(表达式).
    Var4 .= Var  ; 追加一个变量到另一个的末尾(表达式).
    Var5 += Number  ; 将变量的值与另一个相加(表达式).
    Var5 -= Number  ; 将变量的值减去另一个(表达式).
    Var6 := SubStr(Var, 2, 2)  ; 变量在函数中. 这总是一个表达式.
    Var7 = %Var% Text  ; 赋值一个变量给另一个变量并带有一些额外的文本(传统的).
    Var8 := Var " Text"  ; 赋值一个变量给另一个变量并带有一些额外的文本(表达式).
    MsgBox, %Var%  ; 变量在命令中.
    StringSplit, Var, Var, x  ; 在命令中的变量, 但是它们作为输入或输出变量.
    if (Number = 6)  ; 只要 IF 有括号, 它就是一个表达式, 所以不需要百分号.
    if (Var != Number)  ; 只要 IF 有括号, 它就是一个表达式, 所以不需要百分号.
    if Number = 6  ; 如果没有括号, 那么 IF 是传统的. 不过, 只有赋值语句"右边"的变量需要百分号. 
    if Var1 < %Var2%  ; 如果没有括号, 那么 IF 是传统的. 不过, 只有赋值语句"右边"的变量需要百分号. 
    ```

58. 对象是更高一级的组织数据的方式。可以使数组和键值对。

59. 创建对象的方法：

60. ```
    MyObject := ["one", "two", "three", 17]      ;索引数组
    
    Banana := {"Color": "Yellow", "Taste": "Delicious", "Price": 3}     ;关联数组，键值对的集合。
    
    MyObject := Array("one", "two", "three", 17)    ;利用数组函数来创建数组
    
    Banana := Object("Color", "Yellow", "Taste", "Delicious", "Price", 3)     ;利用对象函数，来创建关联数组，键值对。
    ```

61. 使用对象的值：

62. ```
    Banana["Pickled"] := True          ;给Banana对象中的Pickled键赋予True的值。
    Banana.Consistency := "Mushy"      ;同上
    如果想要往对象中添加一个新的键值对，指定给一个原本不存在的键即可。
    ```