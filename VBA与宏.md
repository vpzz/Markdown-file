# VBA

1. VB是微软推出的一个编程语言，而VBA Visual Basic for Applications，是一个工具，用来操作office套件的。宏是一系列的指令组成的程序。后缀名为.vbs。不区分大小写。

2. 使用VBA编写宏，有利于高效地完成重复性的工作。

3. 打开Excel的开发工具后，可以看到左侧的Visual Basic为VBA控制台。左侧第二个为宏管理器，可以查看所有可用的宏。

4. 录制宏的时候需要制定宏名称，快捷键，也可以加上一个说明。

5. <img src="VBA与宏.assets/image-20210211232001768.png" alt="image-20210211232001768" />

6. 下图为VBA控制台，一个Excel文件中可以看到分为两个部分，录制的宏存放在模块中。这个环境成为VBE 环境。

7. <img src="VBA与宏.assets/image-20210211231945399.png" alt="image-20210211231945399" />

8. VBA程序使用'单引号来作为注释的开头。并不会执行。

9. ```vbscript
   Sub 宏2()    '表示子程序的开始
   '
   ' 宏2 宏
   '
   ' 快捷键: Ctrl+Shift+N
   '
       Range("H4").Select
       With Selection.Font
           .Color = -16776961
           .TintAndShade = 0
       End With
   End Sub        '表示子程序的结束
   ```

10. 录制的宏是有Excel自动生成代码。

11. 如果要保存带宏程序的Excel文件，格式需要为。为了保证安全，只有文件的扩展名为xlsm（启用宏的工作簿）时，Excel才会加载宏，单独处理，因为宏中可能隐藏着病毒。

12. 如果企图将带有宏的文件保存为xlsx格式，则会提示如下。

13. <img src="VBA与宏.assets/image-20210211233710170.png" alt="image-20210211233710170" />

14. 打开带有宏的xlsm文件时，Excel会提示是否启用对应的宏。只有启用了宏，才可以后续使用。

15. <img src="VBA与宏.assets/image-20210211233846641.png" alt="image-20210211233846641" />

16. Excel选项→信任中心→受信任的位置，该文件夹下的所有Excel文件会自动加载宏，而不会提示。

17. 录制宏的时候可以选择是否使用相对引用，使用相对引用录制的宏，代码中的单元格位置都是根据active cell来进行定位的。即ActiveCell。就是单击录制宏的那一刻，所选中的单元格。

18. 如下代码ActiveCell.Range("A1:H1").Select表示以当前活动单元格来选择相对于它的A1:H1的范围。即该行的A到H列。后面的那个ActiveCell.Offset(2,0)表示将活动单元格移动，竖向2个单位，横向0个单位。在进行选择相对位置为A1的单元格。

19. <img src="VBA与宏.assets/image-20210212000159186.png" alt="image-20210212000159186" />

20. 使用相对引用来录制宏时，宏要录制一个周期，这样才可以循环使用。

21. 为使用相对引用录制的宏，其中的单元格索引都是使用的绝对引用。不会随着ActiveCell的改变而改变。

22. <img src="VBA与宏.assets/image-20210212001041910.png" alt="image-20210212001041910" />

23. 可以插入表单控件来使之触发宏。也可以将其添加到快速访问工具栏。

24. 宏的操作无法撤销。

25. 保存在单独工作簿中的宏，只有打开该文件才可以使用该宏。打开后，其他文件也可以利用该宏。

26. 录制时，选择保存在个人宏工作簿中，可以发现宏是保存在一个名为PERSONAL.XLSB的文件中。不过该工作簿默认是隐藏的，可以在视图选项卡中取消隐藏。该工作簿没有任何数据，只有宏。个人宏工作簿是保存在本地电脑中的，任何外来的或新建的Excel文件都可以访问该宏。

27. Excel会自动打开PERSONAL.xlsb文件。

28. <img src="VBA与宏.assets/image-20210212002554738.png" alt="image-20210212002554738" />

29. 一个Excel在VBE中对应于一个工程。一个工程中的Microsoft Excel对象包含整个工作簿和所有的工作表。每个对应一个对象。可以针对整个工作簿或某个工作表来进行编写VBA程序。

30. 编写的宏代码一般放在模块中。

31. 编写的模块可以保存为.bas文件。VBA程序会自动进行大小写和括号修正。

32. ```vb
    '注释
    Sub 第一个宏()
        MsgBox "第一个VBA代码"                        '缩进不是必要的
        MsgBox "B9的内容为" & Range("B9").Value       '&进行字符串连接，range来获取单元格cell范围。
    End Sub
    ```

33. 一个模块中可以有多个子程序。可以在VBE中调出立即窗口，输入   Call 子程序名    来调用对应的子程序。

34. Excel支持的变量数据类型：Currency是货币，Date是日期。

35. <img src="VBA与宏.assets/image-20210212103751180.png" alt="image-20210212103751180" />

36. ```vb
    Dim Score As Integer     '变量名为Score,类型为整型。
    Score = 100              '给变量赋值
    Dim date1 As Date
    date1 = #11/20/1988#     '加上#是为了方便Excel识别
    MsgBox date1             '显示的结果和本机日期格式一致
    ```

37. 字符串要用双引号包裹起来。

38. 同时定义多个变量：

    ```vb
    Dim Score As Integer,date1 As Date   
    Dim i,j,k As Integer
    ```

39. Dim后面如果没有加As来给变量指定数据类型，那么变量的类型为variant，可变数据类型。可以进行混乱的赋值。不过不推荐使用。

40. 当去引用一个未定义的变量时，默认不会报错，只是变量的值为空。可以声明Option Explicit来使得VBE对避免这种情况。这种可以避免变量名书写错误的发生。可以在VBE中设置要求变量声明，这样新建的模块都会自动添加Option Explicit声明。

41. <img src="VBA与宏.assets/image-20210212205540321.png" alt="image-20210212205540321" />

42. 在子程序中定义的变量只能在子程序内使用。作用范围就是子程序内。定义在子程序外的变量的作用范围是整个模块内。

43. 将Dim 修改为Public，可以将变量的作用范围扩展到整个Excel工程中。其内的任意模块都可以访问到。

44. 数值型变量不赋值默认为0

45. 使用&进行字符串连接时，其他类型会自动转化为字符串类型。

46. 将Dim修改为Static，可以让该变量在子程序运行结束后，不消失。下一次再执行整个函数时，该变量的值还是上次执行的。具有记忆功能。

47. 单击重新设置按钮，可以将变量的值都释放掉，即使是static修饰的。

48. <img src="VBA与宏.assets/image-20210212211209223.png" alt="image-20210212211209223" />

49. 工作簿关闭时，所有变量也都会被释放掉。

50. 使用Const替代Dim来定义常量，一般会在定义时就进行赋值。因为变量在定义时就会赋予默认值0，而常量不会。

    ```vb
    Const Pi As Double = 3.14
    
    '模块间常量的声明
    Public Const Pi As Double = 3.14
    ```

51. 在面向对象编程中，VB内置了很多的常量，例如vbRed，vbBlue等。      在立即窗口中输入?vbRed可以查看vbRed常量的值。

52. 数学运算符 + - * / ^ Mod    最后两个是乘方和取余。/除法运算是浮点运算，不取整。20 Mod 3 的结果为2，余数。

53. 如果将一个小数存储到整数变量中，则会进行舍去运算。

54. 如果变量的数值超出范围，则会提示溢出。

55. <img src="VBA与宏.assets/image-20210212213001409.png" alt="image-20210212213001409"  />

56. 比较运算符 >   >=    <    <=    =     <>     最后两个是判定是否相等或不等。运算结果为Boolean数据类型，该数据类型可以自动转化为Integer类型，0对应False，1对应True。

57. 判定等于可以添加括号，便于区分。

58. ```vb
    Result = (10 = 20)
    ```

59. 逻辑运算符  And Not Or  结果也是Boolean类型。

60. IF结构：

    ```vb
    If Score >=60 Then
    	MsgBox "PASS"
    End If
    
    If Score >=60 Then
    	MsgBox "PASS"
    Else 
        MsgBox "No PASS"
    End If
    '树状判断
    If Score >=90 Then
    	MsgBox "优秀"
    ElseIf Score >=80 Then
        MsgBox "中上"
    ElseIf Score >=60 Then
        MsgBox "及格"
    Else
        MsgBox "不及格"
    End If
    ```

61. For Next循环，Next标识了for循环的结尾。

    ```vb
    For num = 1 To 5  'num初始为1，当num>5时，循环停止。    循环5次。
    	MsgBox num
    Next num    '等同于 num = num + 1 自增。
    
    
    For num = 1 To 5 Step 2 'num初始为1，当num>5时，循环停止。    当遇到Next Num时，自增2。
    	MsgBox num
    Next num    '等同于 num = num + 2 。
    ```

62. vbNewLine表示换行。

63. ```vb
    For num = 1 To 5  
    	MsgBox num
    	If num >3 Then
        	Exit For   '退出For循环
    	End If
    Next num
    ```

64. Do While 循环

    ```vb
    Do While num <= 10      '如果满足条件，就继续循环。
    	MsgBox num
    	num = num+1
    Loop
    ```

65. Do Until循环

    ```vb
    Do Until num > 10      '如果满足条件，就不再继续循环。
    	MsgBox num
    	num = num+1
    Loop
    ```

66. 子过程，子程序，子函数都是一样的。

    ```vb
    Sub 子程序名称()
        Exit Sub   '退出子程序，类似于return。
    End Sub 
    
    Sub 子程序名称(Num As Integer)  '带参数的子过程，多个参数用逗号分隔
        Exit Sub   '退出子程序，类似于return。
    End Sub 
    子程序名称()   '即可调用子程序，如果是无参数的子程序，可以不加括号。有参数的可以用空格来代替括号。
    ```

67. 函数过程，使用Function关键字。函数过程有返回值，子过程没有。函数过程可以在Excel单元格中使用，类似于Excel自带的函数一样。

    ```vb
    Function CubeSum (x As Double, y As Double) As Double   '可以设置返回值的类型，也可以不设置。
        CubeSum = x^3+y^3      '将要返回的值，赋值给函数名，就是返回值。
    End Function
    ```

# 面向对象

1. 为了使控件不随着单元格的改变而改动，需要设置控件格式为大小和位置均固定。

2. <img src="VBA与宏.assets/image-20210215101252905.png" alt="image-20210215101252905" />

3. Range对象

   ```vb
   Range("A1") = 1    '给A1单元格赋值为1
   
   For i = 1 To 100
   	Range("A" & i) = 1             '执行100次，修改A1→A100为1。
   Next
   ```

4. For循环中可以倒序，例如 For i = 10 To 2 Step -1。需要标明step为负数。

5. Worksheets，工作表对象：

6. <img src="VBA与宏.assets/image-20210215125703679.png" alt="image-20210215125703679" />

7. 工作表对象的3种表示方法：

8. ```vb
   Sheet1           'Sheet1，这个和表的名称无关。按照顺序排。Sheet1始终表示第一个表的对象。
   Sheets("1月")    '名称为"1月"的那个表。
   Sheets(1)        '第一张表。以Excel左下角显示的为准，计数从1开始。
   Sheets           '当前所有表的集合
   ```

9. 单元格对象的表示方法：

   ```vb
   [A1]
   Range("A1")
   ```

10. ```vb
    Sheet1.Select      '切换到Sheet1工作表。
    Sheets.Add         '在当前选中表的前一个位置插入一个表。
    Sheets.Add After:=Sheet3       '在Sheet3的后面插入一个表。     :=是给After参数赋值。还有count参数，可以指定插入的个数。
    Sheet1.Range("A1") = 3    '修改Sheet1的A1单元格为3。如果不指明表的话，会以当前工作表为操作对象。
    Range("A1") = Sheets.Count   '获取工作簿中表的数量，赋值给A1单元格。只读属性。
    Sheet1.name            '表名的属性，可以修改。
        Sheet1.delete      '删除Sheet1，不过这会让Excel弹出对话框，让用户确定，可以设置是否产生警告来取消弹出对话框。
    Application.DisplayAlerts = False      '这样就不会弹出对话框，让用户确认了，不过建议做完相应的操作，立即修改过来。
    Application.DisplayAlerts = True
    Sheet1.Copy   '这个函数会将Sheet1复制到一个单独的Excel文件中。
    Sheet1.Copy After:=Sheet3    '将Sheet1复制到Sheet3后面，仍然在当前Excel文件中。
    ```

11. 模块中的代码，在执行时，会以当前的表为操作对象，如果没有指定表的话。

12. 工作簿中至少要有一个工作表，即最后一个工作表是删除不掉的。

13. 在Excel中删除表或者行列的时候，从前往后和从后往前是不一样，从前往后删的时候，后面的表或行列会进行补齐。从后往前比较好。

14. Sheets对象表示所有的表的集合，WorkSheets对象表示所有的工作表的集合。Excel的表除了有工作表外还可以有如下

15. <img src="VBA与宏.assets/image-20210215183436400.png" alt="image-20210215183436400" />

16. For each循环，适合于对象迭代：

    ```vb
    Dim danyuange As Range
    
    For each danyuange in Range("A1:A10")
    	danyuange = 1           'danyuange变量依次为Range("A1")，Range("A1")等等。
    Next
    ```

17. 在For Each循环内如果也要用到计数，可以在循环外定义一个变量，在循环内手动自增。

18. 没有sheet类型，只有worksheet类型。有sheets和worksheets这两个变量。

19. Workbooks 工作簿对象就是一个Excel文件。

    ```vb
    Workbooks.Open(Filename:="D:/data/1.xlsx")      '打开指定的文件。
    
    ActiveWorkbooks        '当前激活的工作簿对象
    ActiveWorkSheets       '当前激活的工作表对象
    ActiveWorkbooks.Save   '保存Excel文件
    ActiveWorkbooks.Close  '关闭Excel文件
    ```

20. 如果要打开文件，修改然后关闭，这样操作屏幕会一闪而过，可以设置不更新屏幕，有时候有大量操作时，会设置这个，防止Excel卡死，可以提高效率：

    ```vb
    Application.ScreenUpdating = False
    Application.ScreenUpdating = True     '成对出现
    ```

21. 新建Excel文件，然后保存：

    ```vb
    Workbooks.Add
    ActiveWorkbook.Save      '会默认存储到  我的文档 目录下。
    ActiveWorkbook.SaveAs Filename:="D:/data/新建文件"      '另存为可以选择路径。
    ActiveWorkbook.Close
    ```

22. select非当前表的单元格时候，必须要先select对应得表。

23. 单元格对象Range。表示单元格对象的方式：

    ```vb
    [C2]          'C2单元格，不支持变量拼接
    cells(2,3)    '第2行第3列的单元格，即C2。
    Range("C2")   'C2单元格，最广泛地方式，灵活
    Range("C2").value = 1  '给单元格赋值的完全方法，.value也可以省略。因为value是Range对象的默认属性。
    
    Range("C2").offset(2,1)  '以C2单元格为基准，向下移2行，向右移动1列，所得到的单元格。
    Range("C2").End(xlDown)  '参数为4个方向，xlUp,xlDown,xlLeft,xlRight。
    Range("C2").Row          '属性，返回单元格的行号，Column同理。
    
    Range("C2").Resize(2,3)   '以C2为基准，选中2行3列的区域。等价于Range("C2:E3")
    Range("C2").EntireRow     'C2单元格所在的行，即第2行。EntireColumn同理。
    
    Range("C2:E3").Copy Range("N7")    '把对应的单元格选取，复制到N7,C2到N7，依次对应。
    
    Selection      '表示当前选中的单元格或区域。
    
    Range("C2").Delete    '删除单元格，会涉及到周围单元格的移动
    Range("C2").ClearContents  '清楚内容
    ```

24. Excel中在单元格上上边线双击会跳转到所在区域的边界（内部），不是表格的边界。区域之间由空白行和列分隔。

25. <img src="VBA与宏.assets/image-20210215211238211.png" alt="image-20210215211238211"  />

26. 筛选：

    ```vb
    Sheet1.Range("A1:F1048").AutoFilter Field:=4, Criterial:="一车间"    '筛选，第4列，值等于“一车间”
    Sheet1.Range("A1:F1048").AutoFilter         '再运行一次就表示关闭筛选功能。
    ```

27. 通过输入框获取用户输入：

    ```vb
    i= Inputbox("请输入内容")
    ```

28. 对象的前缀相同可以使用with来简化代码。

    ```vb
    Sheet1.name = "12"
    Sheet1.Range("A1") = 23
    Sheet2.Range("B3") = 45
    
    '上述代码等价于下面的代码。
    With Sheet1
        .name = "12"
        .Range("A1") = 23
    	Sheet2.Range("B3") = 45      '不以.开头的按照常规进行索引。
    End With
    ```

29. 对齐的设置

30. <img src="VBA与宏.assets/2020050522052860.png" alt="在这里插入图片描述" />

31. 字体格式的设置

32. <img src="VBA与宏.assets/20200505220640749.png" alt="在这里插入图片描述" />

33. Excel内置了一些事件，可以在某些动作被执行时，自动触发。例如选取变化。类似于回调函数。在VBE中，双击对应的Sheet或者Workbook，在最上边勾选对应的事件，添加代码即可。

34. <img src="VBA与宏.assets/image-20210215234041165.png" alt="image-20210215234041165" />

35. <img src="VBA与宏.assets/20200505220938485.png" alt="在这里插入图片描述"  />

36. <img src="VBA与宏.assets/20200505220938455.png" alt="在这里插入图片描述"  />

37. 有时候需要关闭事件侦测功能，可以用一下设定：

    ```vb
    Application.EnableEvents = False
    Application.EnableEvents = True
    ```

38. Excel中的空间分为两类，表单控件和active控件。表单控件需要指定宏，active控件具备设置事件的功能，可操作性更强，可编程的。

39. 在VBA中使用公式，工作表函数(使用WorksheetFunction调用)和VBA函数。

40. ```vb
    Application.WorksheetFunction.Cos(Range("A1"))      'Application可以省略，等价于单元格中的工作表函数       =Cos("A1")
    
    VBA.Strings.Left()        'VBA函数，字符串截取左侧
    ```

41. ![1613577860036](VBA与宏.assets/1613577860036.png)

42. 一整行或一整列的表示方法：

    ```vb
    Range("A:A")     Range("3:3")
    Range("A3").EntireRow     Range("A3").EntireColumn
    ```

43. 在VBA中调用某些函数，可能会出错，例如利用VLookUp进行查找时，此时可以设置，使得程序继续运行下面的代码：

    ```vb
    On Error Resume  Next     '一旦该行出错，执行下一行，而不是报错停止运行。
    On Error Go To
    ```

44. 给定义了类型的变量赋予不对应的值，会引发错误，例如给整型变量赋予字符串。

45. ```vb
    Val("4")          '结果为数字4。
    IsNumeric (3)     '判断参数是否为数字，返回值为布尔型。
    InStr("2015-07-27", "-")   '在字符串中寻找字符-，返回位置，结果为5，如果找不到则返回0。
    Split("2015-07-27", "-")  '用第二个参数讲第一个参数分割，返回一个字符串数组。
    ```