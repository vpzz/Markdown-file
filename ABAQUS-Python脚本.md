# 基础

1. 使用Python脚本编程允许用户跳过CAE直接和后台的kernel交互。ABAQUS的基础架构如下：

2. ![image-20210610094648581](ABAQUS-Python脚本.assets/image-20210610094648581.png)

3. 常见的执行.py脚本的方法：

   1. 系统命令行执行 abaqus cae script=myscript.py  或abaqus cae noGUI=myscript.py
   2. CAE内的Python命令行执行 execfile('myscript.py')

4. 当时用noGUI执行脚本时，job都是立即执行的，不能推送到job队列中。

5. 获取ABAQUS教程中的脚本文件，保存到当前目录：abaqus fetch job=scriptName

6. 在系统命令行输入abaqus python来使用ABAQUS提供的Python解释器。

7. Python可以用6个"包裹起来多行注释

   ```python
   """
   多行注释
   多行注释
   多行注释
   """
   ```

8. sessiong对象没有构造函数，只要开启一个Session，ABAQUS就会自动创建。该对象是用来控制一些和显示相关的参数，例如viewport，它不会被保存到模型数据库中。

9. mdb对象是就是.cae文件的抽象，保存着模型和求解控制信息。可以自己创建一个该对象，也可以通过from abaqus import * 来使用ABAQUS提供的默认模型数据库对象。

   ```python
   mdb1 = MDdb()
   mdb2 = openMdb(path = 'xxx.cae')  #打开一个.cae文件
   ```

10. point参数接受一个点的坐标（2D或3D），以元组形式给出，例如(1,2)或者(1,2,3)这样的。

11. ABAQUS的构造函数名都是大写字母开头。例如mdb.Model()。使用mdb.来调用Model构造函数，是将构造出的Model对象存储在mdb内，这样可以形成一个对象树。

12. 脚本允许从kernel中读取结果，即使他还没被写入到odb文件中。

13. 容器对象：

    1. repository：类似于Python中的Dictionary，使用对象的名称作为key来索引。例如myOdb.steps是一个repository对象，里边存储着多个Step对象，每个Step对象在创建时都有一个必选参数，字符串name，可以使用myOdb.steps['Step-1']来获取name属性为'Step-1'的Step对象。和字典类似，repository中的键值对是无序的，没有数字索引，也无法进行切片。
    2. sequence：类似于Python中的List，使用数字下标作为索引(0表示第一个，-1表示最后一个)。例如firstStep.frames就是一个sequence对象。

14. ![image-20210610101430141](ABAQUS-Python脚本.assets/image-20210610101430141.png)

15. ![image-20210610095429741](ABAQUS-Python脚本.assets/image-20210610095429741.png)

16. 一般来说如果创建对象时，需要给出name属性时，那么该对象就是存储在repository容器中，否则就是sequence容器中。

17. 当新增或删除某类型的对象时，该对象所在的容器也会自动更新。不能通过容器删除对象，只能del指定的对象。

18. 容器对象的命名习惯为全小写，复数。例如存储Step对象的容器名称为steps

19. repository对象可以用如下方法来查看键值对的对应关系。

20. ![image-20210610101559563](ABAQUS-Python脚本.assets/image-20210610101559563.png)

21. ==需要确认下displacement1和stress1的类型==

22. deformed variable 是用来确定变形后模型的形状。primary variable是用来确定云图或符号图的数值的。

23. ABAQUS的环境文件abaqus_v6.env是Python的语法。replay文件.rpy也是Python语法。

24. 使用type() 来获取一个对象的类型。

25. 通过系统命令行执行Python脚本时，可以传递参数，在脚本内通过sys.argv[1]，argv[2]等来获取，需要先导入sys库。

26. import语法：

    1. import一个模块后，无法卸载它，除非重启Python的解释器。
    2. from math import sin   后可以只用使用sin
    3. import math 后需要通过math.sin来使用

27. 所有的ABAQUS Python脚本都必须在开头包含这两行：

    ```python
    from abaqus import *      #这行使得系统默认的session和mdb对象可以被使用。
    from abaqusConstants import *
    
    from odbAccess import *   #访问ODB文件需要
    from visualization import *    #可视化需要
    ```

28. 构造函数都会返回它构造的对象，同样的构造函数可以依附在part或assembly上，例如：

    ```python
    mdb.models[name].parts[name].Set()   #该Set对象附属于对应的part对象。
    mdb.models[name].rootAssembly.Set()  #该Set对象附属于对应的rootAssembly对象。
    ```

29. 对象.\_\_members\_\_可以获取该对象的所有属性名。对象的属性都是只读的，不能通过简单地通过=赋值来修改，需要通过setValues来修该属性的值。

30. getattr(对象,"属性名")  允许通过字符串形式的属性名，可以获得对象的属性值。

31. 可以在容器对象后输入[，再按tab键进行补全该容器内存储的对象。shift+tab逆序。

32. ABAQUS的对象模型主要分为三种：Session树，Mdb树，Odb树。session对象和mdb对象只能有一个。

33. ![img](ABAQUS-Python脚本.assets/cmd-int-model-overview-nls.png)

34. mdb对象包含jobs和models容器。

35. odb文件中不仅存储了结果数据，也存储了模型的数据。有两种方式来打开一个.odb文件：

    ```python
    import odbAccess
    shockLoadOdb = odbAccess.openOdb(path='myOdb.odb')  #这种方法一般用在CAE以外，例如直接在ABAQUS的Python解释器中读取odb文件。这种情况下只允许同时打开一个.odb文件。
    
    import visualization
    session.openOdb(name='myOdb', path='stress.odb', readOnly=True)  #这种一般在CAE内使用，session对象会将新建的odb对象保存到odbs容器中。这种情况下，允许打开多个.odb文件。
    ```

36. part对象：

37. ![img](ABAQUS-Python脚本.assets/cmd-int-model-part-nls.png)

38. rootAssembly对象：

39. ![img](ABAQUS-Python脚本.assets/cmd-int-model-assembly-nls.png)

40. initialStep类继承自Step，他们之间是is-a关系。Step类是一个抽象基类，该类没有实例，而Feature类是一个基类，但不是抽象类，因此有实例。

42. ![img](ABAQUS-Python脚本.assets/cmd-int-abstract-nls.png)

43. ABAQUS使用基类的repository来存储所有的派生类对象。例如上面的initialStep和StaticStep对象都存储在steps容器中。

45. ABAQUS的对象支持通过复制已有对象的方法来创建新对象。会调用类的拷贝构造函数：

    ```python
    firstBolt = mdb.models['Metric'].Part(name='boltPattern', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    secondBolt = mdb.models['Metric'].Part(name='newBoltPattern', objectToCopy=firstBolt) #原对象的所有子对象都被被拷贝一份。
    ```

46. 可以使用del来删除一个对象：

    ```python
    myMaterial = mdb.models['Model-1'].Material(name='aluminum')  #创建一个新的对象
    del mdb.models['Model-1'].Material['aluminum']  #成功删除对象，此时myMaterial还存在，但是已经不能根据它找到之前的对象了。
    del myMaterial   #删除对应的变量。
    
    myMaterial = mdb.models['Model-1'].Material(name='aluminum') #创建一个新的对象
    del myMaterial  #只是删除了变量标记，对象仍然存在。
    myNewMaterial = mdb.models['Model-1'].materials['aluminum']  #可以给对象重新赋予一个变量标记。
    ```

47. 一般来说，Python中如果一个对象只有一个引用，那么删除这个引用后，这个对象也会被垃圾收集器回收。而在ABAQUS中不同，它维护这一个mdb或session的对象树，对象树中对象的引用不止用户的那一个，因此del对应的变量，不会是的对象的引用计数变为0。

48. ==一个assembly中的vertex数量和part中的vertex数量有什么关系，还有编号==

51. Cell，Face，Edge，Vertex对象分别是3，2，1，0位的几何区域对象。他们都存储在Part或Assembly对象的中。

52. part对象的cells，faces，edges，vertices类型分别为CellArray，FaceArray，EdgeArray，VertexArray。这些类型容纳了一个Part或Assembly中所有的同类对象。都是GeomSequence类的派生类。

53. GeomSequence类，MeshSequence类还有SurfSequence类是Sequence的派生类。

54. Part或Assembly对象和cell对象之间的关系是has-a。拷贝或删除part对象会复制或删除cell对象。

55. 每个几何区域对象都有一个index属性，标识了他们在整个Array中的编号。这个编号的作用域是Part或Assembly内。

56. Vertex对象：

    1. index属性，返回该Vertex对象在整个Part或Assembly的VertexArray容器中的位置。
    2. pointOn属性，返回该几何点的空间坐标构成的一个元组。
    3. getNodes()方法，返回一个MeshNodeArray对象，该容器包含了和该vertex有关联的所有MeshNode对象。

57. MeshNode对象：

    1. label属性，返回该MeshNode对象再整个Part或Assembly中的位置。
    2. coordinates属性，返回该节点的空间坐标构成的一个元组。

58. point是空间内任意坐标表示的点，是一个有浮点数构成的元组。vertex是构成edge对象的点，是一个ABAQUS对象。

59. 可以使用findAt函数在以上Array容器中找到特定位置的对象。例如VertexArray对象的findAt方法：

    ```python
    verts = v.findAt(coordinates = (20.19686, -169.513997, 27.798593))  #coordinates参数接受的是 A sequence of Floats
    #该函数使用ACIS引擎的默认距离误差大小，即1e-6。如果带point到最近的vertex距离超过了1e-6，那么就会返回None
    ```

60. 可以使用VertexArray对象的getByBoundingSphere方法来获取该VertexArray中落在一个球体范围内的所有Vertex。

61. 可以用如下方法找到VertexArray中距离某些point最近的vertices：

    ```python
    r=v.getClosest(coordinates=((20.0,20.0,10.0),(-1.0, -15.0, 15),))  #coordinates默认接受A sequence of Floats，表示要查找的一个point。但是也可以接受A sequence of a sequence of floats，也就是一个由point构成的元组，表示要查找的一系列point。
    r[0]  #结果是一个字典类型。键是从0开始的，表示coordinate中的一个一个point。
    (mdb.models['Model-1'].parts['Part-1'].vertices[0],(15.7090625762939, 29.1666641235352, 20.0))  #值是找到的距离该point最近的vertex构成一个list。给出了路径和vertex的坐标。
    ```

62. ABAQUS的几何引擎使用的是Spatial Technology公司的ACIS引擎。Fluent，Nastran，AutoCAD等软件都使用了该引擎。

63. ![image-20210610132031893](ABAQUS-Python脚本.assets/image-20210610132031893.png)

60. 用户编写的脚本在Script命名空间中执行，称为main。而GUI操作在Journal命名空间中执行，称为journaling。不过不同命名空间都是在操作同一个对象模型树。

    ```python
    p1 = mdb.models['Model A'].parts['Part 3D A']  #例如在replay文件中发现这样一句话，即p1变量是在journal空间中的，在脚本中引用p1会提示找不到。
    ```

61. 通过以下方法可以设置视口显示的对象：

    ```python
    session.viewports[name].setValues(displayedObject=object)  #可以显示的有part,assembly,sketch,Data from an output database,X–Y plot,Empty。可以设置为Empty，减少性能开销。
    ```

62. Region和Set对象：

63. 

64. 

65. 

66. 

67. 

68. 

69. Abaqus PDE(Python development environment)可以再CAE内打开，也可以单独打开。PDE可以识别.py或.guiLog文件，后者是通过CAE录制的脚本。

70. 

71. ABAQUS默认的选择是通过mask，这种方式对于大量选择效率很高，但是不方便用户查看，可以在env文件中加入如下代码来达到开启cae时，就设置：

    ```python
    def onCaeStartup():
        session.journalOptions.setValues(replayGeometry=INDEX)
    ```

    

72. 

73. 

74. 

75. 下面的函数，instanceList参数接受一个含有多元素的元组，如果只有一个元素，则应在该元素后面加上逗号。

    ```python
    a.translate(instanceList=(e1[0].name,),vector=(v1,v2,v3))
    ```

76. mdb.models 属性返回的是repository类型，其实类似于Python的字典类型。键是model的名字，值时对应的model对象。changeKey函数可以修改对应对象的名字。

78. ```python
    >>> type(mdb.models)
    <type 'Repository'>
    >>> mdb.models.keys()
    ['Model-1']
    >>> mdb.models.values()
    [mdb.models['Model-1']]
    >>> mdb.models.items()
    [('Model-1', mdb.models['Model-1'])]
    >>> mdb.models.changeKey('Model-1','myModel')
    ```

79. 使用rootassembly来获取model的assembly对象。

80. ```python
    mdb.models[name].rootAssembly
    ```

81. 下图表示有两种方式可以获取到该对象。

82. ![image-20200615104814484](ABAQUS-Python脚本.assets/image-20200615104814484.png)

83. 下图表明了该对象的构造函数的使用方法。需要加上路径。

84. ![image-20200615104929601](ABAQUS-Python脚本.assets/image-20200615104929601.png)

85. 下图这样的函数是对象的方法。

86. ![image-20200615105007297](ABAQUS-Python脚本.assets/image-20200615105007297.png)

87. 使用dir函数来查看对象的所有属性和方法。包含了.\_\_members\_\_和.\_\_methods\_\_属性。

    ```python
    >>> dir(h1)
    ['__abs__', '__add__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pos__', '__pow__', '__radd__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'addData', 'conjugateData', 'data', 'description', 'name', 'type']
    
    >>> h1.__methods__
    ['addData']
    
    >>> h1.__members__
    ['conjugateData', 'data', 'description', 'name', 'type']
    ```

88. ABAQUS的所有GUI操作都有对应的Python命令。这些命令发送到ABAQUS/CAE kernel。工作目录下会有一个.rpy文件记录这些命令。replay

89. Python脚本允许用户绕过GUI直接和kernel交互。

90. 前处理可以使用任意交互方式，但ABAQUS的求解器只认识.inp文件。

91. 

92. 可以使用Marco Manager来录制动作，生成指定的Python脚本。

93. 可以使用execfile()函数来执行一个Python脚本。如下命令可以以不显示GUI的模式运行ABAQUS。方便批量进行前后处理，加快速度。

94. ```
    abaqus cae noGUI=myscript.py
    ```

95. 下面的两组是所有的ABAQUS脚本都要使用的。

96. ```python
    from abaqus import *
    from abaqusConstants import *
    ```

97. 所有的构造函数都是大写字母开头的。

98. ABAQUS的step下面细分是frame。

99. ```python
    # Open the tutorial output database.
    myOdb = visualization.openOdb(path='viewer_tutorial.odb')
    # Associate the output database with the viewport.
    myViewport.setValues(displayedObject=myOdb)
    ```

100. 打开CAE之后，再切换工作目录，则不会改变Python脚本的记录位置，即rpy文件。

101. rpy文件第一行为如下，mbcs表示多字节编码系统，也就是Windows下的ANSI。对于简体中文Windows系统就是GBK。

     ```
     # -*- coding: mbcs -*-
     ```

102. 也可以利用field output的数据创建x-ydata。不过只能在各个frame上取值。而通常情况下history output的频率就可以设置的比较高，例如在本例中，一共进行了6779个增量步，但是由于field output中设置了均匀输出40次。在history output中设置了均匀输出200次。可以看到每个增量步的时间长度都差不多≈7.37e-7。

103. ![image-20201028134102635](ABAQUS-Python脚本.assets/image-20201028134102635.png)

104. 时间均匀切割，产生40个frame。

105. ![image-20201028134302869](ABAQUS-Python脚本.assets/image-20201028134302869.png)

106. 试件均匀切割，产生200个history 输出点。

107. ![image-20201028134438604](ABAQUS-Python脚本.assets/image-20201028134438604.png)

108. 可以将ABAQUS的显示设置保存在文件中，abaqus_v6.14.gpr。放到路径(用户的家目录，对于Windows为 C:\Users\Administrator)中，就可以在打开的时候自动读取。

108. 在特定目录下打开ABAQUS。切换到该目录，Shift+右键，在此处打开命令窗口，输入：

     ```
     abaqus cae=xxx.cae
     ```