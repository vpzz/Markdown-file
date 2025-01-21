# 基础

1. abaqus最早的python是基于python2.7的，而在2020年，python2.7不在维护了。因此从Abaqus 2024x GA版本开始将python解释器的版本从2.7改变为3.10。Abaqus 2024包含一个用于将脚本从Python 2转换为Python 3的工具。它主要基于Python的原生2to3转换工具，但添加了许多其他功能，以方便创建在版本之间交叉兼容的脚本。

   ```shell
   abaqus python -m abqPy2to3 xx.py
   ```

2. 为了更容易安装第三方软件包，从Abaqus 2024 FD02开始添加了abqPip命令。可以使用`abaqus python -m abqPip -h`查看帮助。

3. abaqus的不同版本的脚本之间可能存在兼容性，因为abaqus偶尔会更改一些接口，因此abaqus提供了一个工具来升级脚本

   ```shell
   abaqus python -m upgradeScript xx.py #会升级到当前软件的版本，-backup备份旧版本
   ```

4. ABAQUS的所有GUI操作都有对应的Python命令。这些命令发送到ABAQUS/CAE kernel。工作目录下会有一个.rpy文件记录这些命令，表示replay。Python脚本允许用户绕过GUI直接和kernel交互。

5. 打开CAE之后，再切换工作目录，则不会改变Python脚本的记录位置，即rpy文件，因此推荐先建立新的工作目录，然后通过命令行打开CAE。

6. ABAQUS的基础架构如下：

7. ![image-20210610094648581](ABAQUS-Python脚本.assets/image-20210610094648581.png)

8. 常见的执行.py脚本的方法：

   1. 系统命令行执行`abaqus cae script=myscript.py`或`abaqus cae noGUI=myscript.py`。如下命令可以以不显示GUI的模式运行ABAQUS。方便批量进行前后处理，加快速度。

      ```shell
      abaqus cae noGUI=myscript.py #当使用noGUI执行脚本时，job都是立即执行的，不能推送到job队列中。
      #通过系统命令行执行Python脚本时，可以传递参数，在脚本内通过sys.argv[1]，argv[2]等来获取，需要先导入sys库。
      ```
   2. CAE内的Python命令行执行`execfile('myscript.py')`。
   3. CAE内的File→Run Script，可以是python源文件或编译后的pyc文件。

9. 推荐使用Macro Manager来录制动作，生成指定的Python脚本，然后再进行修改，这样比从头编写效率高，修改完之后，需要reload脚本才可以run。可以手动删除一些视口操作。

10. 所有的ABAQUS Python脚本都必须在开头包含这两行：

   ```python
   from abaqus import *      #这行使得系统默认的session和mdb对象可以被使用。
   from abaqusConstants import *
   
   from odbAccess import *   #访问ODB文件需要
   from visualization import *    #可视化需要
   ```

11. import语法：

   12. import一个模块后，无法卸载它，除非重启Python的解释器。
   13. from math import sin   后可以只用使用sin
   14. import math 后需要通过math.sin来使用

15. rpy文件第一行为如下，mbcs表示多字节编码系统，也就是Windows下的ANSI。对于简体中文Windows系统就是GBK。

    ```python
    # -*- coding: mbcs -*-
    ```

16. 获取ABAQUS教程中的脚本文件，保存到当前目录`abaqus fetch job=scriptName`。

17. ABAQUS的环境文件abaqus_v6.env是Python的语法。replay文件.rpy也是Python语法。

18. 在系统命令行输入abaqus python来使用ABAQUS提供的Python解释器。

19. Python可以用6个"包裹起来多行注释

    ```python
    """
    多行注释
    多行注释
    多行注释
    """
    ```

20. 用户编写的脚本在Script命名空间中执行，称为main。而GUI操作在Journal命名空间中执行，称为journaling。不过不同命名空间都是在操作同一个对象模型树。

    ```python
    p1 = mdb.models['Model A'].parts['Part 3D A']  #例如在replay文件中发现这样一句话，即p1变量是在journal空间中的，在脚本中引用p1会提示找不到。
    ```

21. Abaqus PDE(Python development environment)可以在CAE内打开，也可以单独打开。PDE可以识别.py或.guiLog文件，后者是通过CAE录制的脚本。

22. ABAQUS默认的选择是通过mask，这种方式对于大量选择效率很高，但是不方便用户查看，可以在env文件中加入如下代码来达到开启cae时，就设置：

    ```python
    def onCaeStartup():
        session.journalOptions.setValues(replayGeometry=INDEX)
    ```

23. 如果要在程序中提交job后直接进行后处理分析，需要写成如下形式：

    ```python
    mdb.jobs[job1].submit() #提交到求解器
    mdb.jobs[job1].waitForCompletion() #等待求解结束
    ... #后续代码
    ```

24. 提交之后，CAE就会卡死，此时可以通过.sta文件查看迭代收敛的情况。

25. 可以使用abaqus自带的RSG（Really Simple GUI） Dialog Builder来创建待GUI界面的用户插件。参考手册为Abaqus GUI Toolkit User's Guide。

# 对象与方法

1. sessiong对象没有构造函数，只要开启一个Session，ABAQUS就会自动创建。该对象是用来控制一些和显示相关的参数，例如viewport，它不会被保存到模型数据库中。

2. mdb对象是就是.cae文件的抽象，保存着模型和求解控制信息。可以自己创建一个该对象，也可以通过from abaqus import * 来使用ABAQUS提供的默认模型数据库对象。

   ```python
   mdb1 = MDdb()
   mdb2 = openMdb(path = 'xxx.cae')  #打开一个.cae文件
   ```

3. point参数接受一个点的坐标（2D或3D），以元组形式给出，例如(1,2)或者(1,2,3)这样的。

4. ABAQUS的构造函数名都是大写字母开头。例如mdb.Model()。使用mdb.来调用Model构造函数，是将构造出的Model对象存储在mdb内，这样可以形成一个对象树。

5. 脚本允许从kernel中读取结果，即使它还没被写入到odb文件中。

6. 容器对象：

   1. repository：类似于Python中的Dictionary，使用对象的名称作为key来索引。例如myOdb.steps是一个repository对象，里边存储着多个Step对象，每个Step对象在创建时都有一个必选参数，字符串name，可以使用myOdb.steps['Step-1']来获取name属性为'Step-1'的Step对象。和字典类似，repository中的键值对是无序的，没有数字索引，也无法进行切片。
   2. sequence：类似于Python中的List，使用数字下标作为索引(0表示第一个，-1表示最后一个)。例如firstStep.frames就是一个sequence对象。

7. ![image-20210610101430141](ABAQUS-Python脚本.assets/image-20210610101430141.png)

8. ![image-20210610095429741](ABAQUS-Python脚本.assets/image-20210610095429741.png)

9. 一般来说如果创建对象时，需要给出name属性时，那么该对象就是存储在repository容器中，否则就是sequence容器中。

10. 当新增或删除某类型的对象时，该对象所在的容器也会自动更新。不能通过容器删除对象，只能del指定的对象。

11. 容器对象的命名习惯为全小写，复数。例如存储Step对象的容器名称为steps。

12. repository对象可以用如下方法来查看键值对的对应关系。

13. ![image-20210610101559563](ABAQUS-Python脚本.assets/image-20210610101559563.png)

14. deformed variable 是用来确定变形后模型的形状。primary variable是用来确定云图或符号图的数值的。

15. 使用type() 来获取一个对象的类型。

16. 构造函数都会返回它构造的对象，同样的构造函数可以依附在part或assembly上，例如：

    ```python
    mdb.models[name].parts[name].Set()   #该Set对象附属于对应的part对象。
    mdb.models[name].rootAssembly.Set()  #该Set对象附属于对应的rootAssembly对象。
    ```

17. 对象.\_\_members\_\_可以获取该对象的所有属性名。对象的属性都是只读的，不能通过简单地通过=赋值来修改，需要通过setValues来修该属性的值。

18. getattr(对象,"属性名")  允许通过字符串形式的属性名，可以获得对象的属性值。

19. 可以在容器对象后输入[，再按tab键进行补全该容器内存储的对象。shift+tab逆序。

20. ABAQUS的对象模型主要分为三种：Session树，Mdb树，Odb树。session对象和mdb对象只能有一个。

21. ![img](ABAQUS-Python脚本.assets/cmd-int-model-overview-nls.png)

22. mdb对象包含jobs和models容器。

23. odb文件中不仅存储了结果数据，也存储了模型的数据。有两种方式来打开一个.odb文件：

    ```python
    import odbAccess
    shockLoadOdb = odbAccess.openOdb(path='myOdb.odb')  #这种方法一般用在CAE以外，例如直接在ABAQUS的Python解释器中读取odb文件。这种情况下只允许同时打开一个.odb文件。
    
    import visualization
    session.openOdb(name='myOdb', path='stress.odb', readOnly=True)  #这种一般在CAE内使用，session对象会将新建的odb对象保存到odbs容器中。这种情况下，允许打开多个.odb文件。
    ```

24. part对象：

25. ![img](ABAQUS-Python脚本.assets/cmd-int-model-part-nls.png)

26. rootAssembly对象：

27. ![img](ABAQUS-Python脚本.assets/cmd-int-model-assembly-nls.png)

28. initialStep类继承自Step，他们之间是is-a关系。Step类是一个抽象基类，该类没有实例，而Feature类是一个基类，但不是抽象类，因此有实例。

29. ![img](ABAQUS-Python脚本.assets/cmd-int-abstract-nls.png)

30. ABAQUS使用基类的repository来存储所有的派生类对象。例如上面的initialStep和StaticStep对象都存储在steps容器中。

31. ABAQUS的对象支持通过复制已有对象的方法来创建新对象。会调用类的拷贝构造函数：

    ```python
    firstBolt = mdb.models['Metric'].Part(name='boltPattern', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    secondBolt = mdb.models['Metric'].Part(name='newBoltPattern', objectToCopy=firstBolt) #原对象的所有子对象都被被拷贝一份。
    ```

32. 可以使用del来删除一个对象：

    ```python
    myMaterial = mdb.models['Model-1'].Material(name='aluminum')  #创建一个新的对象
    del mdb.models['Model-1'].Material['aluminum']  #成功删除对象，此时myMaterial还存在，但是已经不能根据它找到之前的对象了。
    del myMaterial   #删除对应的变量。
    
    myMaterial = mdb.models['Model-1'].Material(name='aluminum') #创建一个新的对象
    del myMaterial  #只是删除了变量标记，对象仍然存在。
    myNewMaterial = mdb.models['Model-1'].materials['aluminum']  #可以给对象重新赋予一个变量标记。
    ```

33. 一般来说，Python中如果一个对象只有一个引用，那么删除这个引用后，这个对象也会被垃圾收集器回收。而在ABAQUS中不同，它维护这一个mdb或session的对象树，对象树中对象的引用不止用户的那一个，因此del对应的变量，不会是的对象的引用计数变为0。

34. ==一个assembly中的vertex数量和part中的vertex数量有什么关系，还有编号==

35. Cell，Face，Edge，Vertex对象分别是3，2，1，0维的几何区域对象。他们都存储在Part或Assembly对象的中。

36. part对象的cells，faces，edges，vertices类型分别为CellArray，FaceArray，EdgeArray，VertexArray。这些类型容纳了一个Part或Assembly中所有的同类对象。都是GeomSequence类的派生类。

37. GeomSequence类，MeshSequence类还有SurfSequence类是Sequence的派生类。

38. Part或Assembly对象和cell对象之间的关系是has-a。拷贝或删除part对象会复制或删除cell对象。

39. 每个几何区域对象都有一个index属性，标识了他们在整个Array中的编号。这个编号的作用域是Part或Assembly内。

40. Vertex对象：

    1. index属性，返回该Vertex对象在整个Part或Assembly的VertexArray容器中的位置。
    2. pointOn属性，返回该几何点的空间坐标构成的一个元组。
    3. getNodes()方法，返回一个MeshNodeArray对象，该容器包含了和该vertex有关联的所有MeshNode对象。

41. MeshNode对象：

    1. label属性，返回该MeshNode对象再整个Part或Assembly中的位置。
    2. coordinates属性，返回该节点的空间坐标构成的一个元组。

42. point是空间内任意坐标表示的点，是一个有浮点数构成的元组。vertex是构成edge对象的点，是一个ABAQUS对象。

43. 可以使用findAt函数在以上Array容器中找到特定位置的对象。例如VertexArray对象的findAt方法：

    ```python
    verts = v.findAt(coordinates = (20.19686, -169.513997, 27.798593))  #coordinates参数接受的是 A sequence of Floats
    #该函数使用ACIS引擎的默认距离误差大小，即1e-6。如果带point到最近的vertex距离超过了1e-6，那么就会返回None
    ```

44. 可以使用VertexArray对象的getByBoundingSphere方法来获取该VertexArray中落在一个球体范围内的所有Vertex。

45. 可以用如下方法找到VertexArray中距离某些point最近的vertices：

    ```python
    r=v.getClosest(coordinates=((20.0,20.0,10.0),(-1.0, -15.0, 15),))  #coordinates默认接受A sequence of Floats，表示要查找的一个point。但是也可以接受A sequence of a sequence of floats，也就是一个由point构成的元组，表示要查找的一系列point。
    r[0]  #结果是一个字典类型。键是从0开始的，表示coordinate中的一个一个point。
    (mdb.models['Model-1'].parts['Part-1'].vertices[0],(15.7090625762939, 29.1666641235352, 20.0))  #值是找到的距离该point最近的vertex构成一个list。给出了路径和vertex的坐标。
    ```

46. 通过以下方法可以设置视口显示的对象：

    ```python
    session.viewports[name].setValues(displayedObject=object)  #可以显示的有part,assembly,sketch,Data from an output database,X–Y plot,Empty。可以设置为Empty，减少性能开销。
    ```

47. Region和Set对象：

48. 下面的函数，instanceList参数接受一个含有多元素的元组，如果只有一个元素，则应在该元素后面加上逗号。

    ```python
    a.translate(instanceList=(e1[0].name,),vector=(v1,v2,v3))
    ```

49. mdb.models 属性返回的是repository类型，其实类似于Python的字典类型。键是model的名字，值时对应的model对象。changeKey函数可以修改对应对象的名字。

50. ```python
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

51. 使用rootassembly来获取model的assembly对象。

52. ```python
    mdb.models[name].rootAssembly
    ```

53. 下图表示有两种方式可以获取到该对象。

54. ![image-20200615104814484](ABAQUS-Python脚本.assets/image-20200615104814484.png)

55. 下图表明了该对象的构造函数的使用方法。需要加上路径。

56. ![image-20200615104929601](ABAQUS-Python脚本.assets/image-20200615104929601.png)

57. 下图这样的函数是对象的方法。

58. ![image-20200615105007297](ABAQUS-Python脚本.assets/image-20200615105007297.png)

59. 使用dir函数来查看对象的所有属性和方法。包含了.\_\_members\_\_和.\_\_methods\_\_属性。

    ```python
    >>> dir(h1)
    ['__abs__', '__add__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pos__', '__pow__', '__radd__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'addData', 'conjugateData', 'data', 'description', 'name', 'type']
    
    >>> h1.__methods__
    ['addData']
    
    >>> h1.__members__
    ['conjugateData', 'data', 'description', 'name', 'type']
    ```