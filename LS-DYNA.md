# 基础

1. LSTC公司在2019年被ANSYS公司收购，更名为ANSYS LST公司，LS-DYNA源自LLNL的John O. Hallquist博士于1976年开发的3D有限元分析程序DYNA3D。LSTC公司就在LLNL实验室的北面，都在加州的Livermore。LLNL是美国的核武器研制单位。DYNA3D是为了模拟全引信选项或可调当量核弹在低空释放（撞击速度约为40m/s）时的撞击而开发的。1978年，应法国的要求，DYNA3D源代码被无限制地发布到公共领域。

2. 1988年底，LSTC公司成立，以更专注的方式继续开发DYNA3D，从而产生了LS-DYNA3D（后来缩写为LS-DYNA）。因此，DYNA3D的发布和支持被停止。

3. DYNA的授权方式不是分模组的，而是统计并行节点，即使购买几个节点的证书，也可以使用该软件的全部分析功能。

4. LS-DYNA的授权方式：依据软件同时可以运行的核心数量。例如一个8核的许可证允许以下任何一种情况（以及更多）：

   1. 用户在8个核心上并行运行一个任务；

   2. 用户并行运行两个任务，每个使用4个核心；

   3. 用户运行8个任务，每个使用1个核心。

5. LS-DYNA主要的应用方面：汽车碰撞和乘员安全，金属钣金成型，飞机鸟击，爆炸侵彻，液晃分析，跌落测试。

6. LS-DYNA垄断了国内外汽车厂商的碰撞安全分析应用，全球80%的汽车制造商将它作为首选的碰撞分析工具。Occupant（乘员）是汽车行业中车内人员的专用称呼。

7. DYNA提供了汽车设计的特殊功能，例如焊点，安全带，滑环，预紧器，牵引器，传感器，加速度计，气囊，假人模型，壁障模型等，可以模拟碰撞仿真，气囊展开。

8. 行业专用的分析软件可以在通用软件上开发得到，例如DYNAFORM是在LS-DYNA上开发的。

9. DYNA提供了板料冲压成形模拟的功能，同时也基于这些功能开发专业的软件LS-FORM。

10. DYNA可以交替使用隐式和显式求解器，例如进行薄板冲压成型的回弹分析。

11. 二次开发功能，支持自定义材料模型，状态方程，单元，求解控制，输入输出。二次开发可以调用所有的函数库和共享数据模块，从R9版本开始，二次开发可以使用动态链接库。DYNA可以加载和调用多个用户动态链接库，并按照用户规则将不同的库分配给相应的单元和模块。
12. 对于实际的对称结构，由于天然或人造材料性质的不均匀分布，不一定产生对称的响应，而在FEM中，如果不手动指定不同的材料性质，则必定只会产生对称的响应，因此使用对称模型计算，不会有任何危险，只有收益。
13. 对于跌落问题，如果非要从高处开始分析，可以设置`*DEFORMABLE_TO_RIGID_AUTOMATIC`，将跌落时的变形体设置为刚体，这样计算速度会加快很多。然后在将要发生碰撞时转化为变形体。
14. 战斗部为弹药行业中对毁伤目标的最终毁伤单元的专用称呼。
15. 内弹道发射是指炮弹在炮管内发射，外弹道是指导弹直接发射。

16. 进行汽车碰撞模拟时，可以为每个车轮定义一个刚性墙，这样可以获得每个车轮的反力。
17. Part，Material，Section，EOS，Hourglass都有对应的ID，分别为PID，MID，SID，EOSID，HID。同一个Part内的单元具有相同的以上所有属性。可以在Model→PartData中查看，赋予Part相关的信息，这个比直接在Keyword中修改方便些。
18. 和Abaqus不同，Part关键字在LS-DYNA中是必不可少的，它将材料，截面，沙漏控制等关键字联合起来。Abaqus是通过截面将材料和单元集合关联起来的。因此LS-DYNA中刚体材料关键字`*MAT_RIGID`中是可以设置是否约束使用此材料的part的质心的运动的，当然也支持使用constrained来约束。

19. 鉴于此，推荐为每个Part都创建一个材料编号，即使它和其他part使用相同的材料。这样使得每个Part的所有ID编号都一样，方便纠错。

20. 有时可能发现，在PrePost的模型树中，开关显示某个Part时，图形区域并不会有变化，这是因为没有单元属于该Part，也就是这是一个空Part，可以在Model→Part Data→#Elems来查看单元数量。


# 数值方法

1. 在固体力学中，差分法是有限元法出现前的主要的数值方法，差分法对于复杂边界适用较差。爆炸软件AUTODYN和岩土工程软件FLAC就是使用差分法。
2. 有限元法的缺点是难以处理有极大单元变形的情况，预估产生的误差比较困难。
3. 有限体积法基于积分形式的守恒方程，而非微分方程。
4. 边界元法只在求解域的边界上划分单元，用满足控制方程的函数去逼近边界条件。基本思想是利用格林定理，将全域的控制方程转化为边界上的积分方程。与有限元方法相比，降低了问题的维数和自由度数量。通过引用问题的基本解，而具有解析和离散相结合的特点，使得计算精度较高。缺点是需要存在相应微分算子的基本解，对于非均匀介质等问题难以应用，适用范围远不如有限元法。DYNA的声学和电磁学计算支持边界元功能。
5. 离散元法起源于分子动力学，是为了研究岩体等非连续介质而发展起来的。离散的单元本身为刚体，单元间的相对位移等行为由联接节点间的变形元件来实现，允许单元间的相对运动，不必满足位移连续和变形协调条件。适用于模拟节理系统或离散颗粒混合，分离，输运等过程。
6. SPH法是一种无网格拉格朗日算法，为解决天体物理中涉及的流体质团在三维空间无边界情况下的任意流动拉格朗日问题而开发的，后来发现对于模拟连续结构的解体，断裂等问题或大变形流动非常有效。SPH适合用来求解具有大变形，复杂边界和物质交界面等复杂单相，多相流体动力学问题，是最早的无网格法。
7. SPH使用一系列的粒子来表示求解域，粒子具有质量，速度，温度，粒子之间不需要任何连接，具有无网格特性。理论基础是插值理论，通过一种称之为核函数的积分核进行插值近似，将流体力学微分方程组转化为SPH代数方程组。SPH的近似过程不受网格限制，可以避免网格极度大变形时的精度下降问题。缺点是：拉伸不稳定会引起数值断裂，需要复杂的接触算法。SPH可以模拟金属切削，不存在网格畸变性和单元失效问题，因为它没有网格。PrePost使用SPH Generation来创建SPH的part，只需要提供表面网格即可，内部不用划分网格。
8. 电磁场（EM）模块通过求解麦克斯韦方程模拟涡电流，感应加热，电阻加热等问题，可以与结构，热分析耦合。
9. DYNA是唯一引入近场动力学（PD）的商业软件，基于非连续伽辽金有限元来模拟脆性材料的三维断裂。
10. 光滑粒子伽辽金（SPG）是DYNA独有的，适用于弹塑性及半脆性材料的失效与破坏分析。由于材料的失效导致传统的有限元仿真变得困难，SPG算法区别于其他失效与破坏算法的特点是它可以不删除失效的单元，并且计算结果对失效准则敏感度不高。该算法还可以用于多尺度分析。
11. 传统有限元在模拟结构的破坏时，裂纹位置必须沿着单元的边界，同时在裂纹尖端附近的节点位置也必须特别处理，当裂纹成长时，网格也必须随之重建，建模工作繁琐，可信度不高。
12. 扩展有限元法（XFEM），联合了连续-间断有限元法，由于其位移场通过单位分解引入了强间断，因此能够有效模拟材料破坏引起的结构从连续到间断的状态改变。采用虚拟节点积分法，引入间断的单元可以分解为2个相同类型的虚拟单元。很适合模拟板壳结构的破坏失效和动态裂纹扩展分析。裂纹可以穿过单元内部来扩展，极大地减少了网格离散和网格取向对裂纹扩展的影响。
13. 结构化ALE（S-ALE）能够在DYNA计算开始时，在求解器种自动生成正交结构化ALE网格，可以简化建模过程，提高流固耦合求解的稳定性，降低求解所需内存和时间。
14. 从971R5开始，DYNA陆续增加了一些频域内振动和声学分析计算功能，例如频率响应函数，稳态震动，随机振动和随机疲劳。反应谱分析，有限元声学和边界元声学。
15. 等几何分析IGA，是Hughes提出的一种能够直接在CAD几何模型上进行分析的方法，2014年开始DYNA开发基于IGA的壳单元，实体单元，修剪壳单元等。
16. ICFD求解不可压缩流动，要求马赫数<0.3。可以采用ALE网格运动方法或网格自适应技术解决流体和结构之间的强弱耦合。使用隐式算法。
17. 时-空守恒元CESE，是高精度，单流体，可压缩显式求解器，采用欧拉网格，能够精确捕捉非等熵问题的细节，可用于超音速分析。在其上还开发了精度更高，更稳定的DUALCESE求解器，可用于多相流计算。

# 求解器

1. 求解器最开始输出的预估计算时间不太准确，一般会过大，可以在开始输出后，按Ctrl+C，输入sw2，此时输出的预估计算时间更为准确。
2. Windows下的DYNA没有Linux下的稳定性强。
3. 求解器在命令行的输出会被保存到message中，但是预估的时间会存储到status.out中。
4. LSrun生成的命令行脚本为：

   ```bat
   call "C:\Program Files\ANSYS Inc\v221\ansys\bin\winx64\LSPrePost47\LSDYNAmsvar.bat" && "C:\Program Files\ANSYS Inc\v221\ansys\bin\winx64\LSDYNA_dp.exe" i=D:\LS-DYN~1\BALL_P~1.K ncpu=4 memory=20m
   @echo off
   echo job finished > LSrunjobid5
   pause
   ```
5. 命令行中的`BALL_P~1.K`是8.3格式，这是古早Windows版本的文件命名格式，标识以BALL_P开头的，后缀为.k的第1个文件。可以通过修改注册表来关闭这种功能。

6. 命令行输出中的信息：

   ```shell
   Version : smp d R12  #表示SMP双精度，R12求解器版本
   ```

7. 旧版本的求解器会要求K文件路径中不能有空格，否则会报错 invalid option on the command line : A。这个A是指路径中空格后的第一个字母，求解器将空格作为命令和参数的分隔了，因此会认为A是选项。

8. DYNA的求解器就是一个静态链接的可执行文件：`LS-DYNA_smp_d_R11_1_0_winx64_ifort160`。smp表示对称多处理，就是共享内存，使用OpenMP编程的。d表示双精度，R11_1_0表示求解器为11.1.0版本，ifort160表示Intel Fortran Compiler 版本。

9. 16核以下建议使用共享内存SMP版本，16-512核心建议使用大规模并行MPP版本，512核心以上建议使用HYBRID（CPU内使用SMP，CPU间使用MPP）。

10. DYNA求解器可以接受K文件或DYN文件，其中全部由关键字组成，以*开头。

11. DYNA在求解不同K文件时，求解产生的文件都是同名的，这点和Abaqus不一样，因此一个文件夹中，建议只保存一个K文件及其结果，要不会覆盖。

# PrePost技巧

1. LSTC还开发了自己的预处理器和后处理器LS-PrePost，它是免费分发的，无需许可证即可运行。PrePost的开发工作目前由大连富坤科技公司负责，界面使用WxWidget GUI库和OpenGL图形库，几何引擎使用OpenCascade库。

2. 在PrePost的2.4~4.6版本期间，新旧界面同时存在，可以按F11进行切换。4.7及以后版本，只保留新界面。配置文件名称为.lsppconf。

3. 按下F1键可以设置快捷键；按下Shift+Fn键，可以直接运行对应的Fn.cfile文件，会先在配置文件中functionkey_path变量指定的目录下查找，其次在当前工作目录，最后在配置文件所在的目录。

4. 多边形选取时，单击左键添加角点，单击右键结束选择。

5. 当PrePost提示选择几何或单元时，也可以直接在模型树上点击来选择。

6. PrePost支持将选择的东西临时save起来，后续可以load进来。

7. 在节点上单击鼠标中键可以将其设置为旋转中心，再次单击中键，可以取消设置。

8. File→Update可以更新读取结果文件，适用于一边计算，一边后处理。PrePost可以处理全部格式的LS-DYNA计算结果文件。

9. PrePost支持IGES和STEP两种通用的几何格式。读取时会自动对几何或拓扑错误进行清理，缝合邻接曲面。

10. PrePost中显示云图为Fringe，这个单词为条纹的意思。通过颜色条纹或边缘过渡来展示物理量的分布。

11. PrePost中的Resultant Displacement是指位移向量的幅值。

12. 菜单栏→View→Beam Prism可以查看梁单元的截面。Model→Appearance→Thick，点击Allvis即可显示所有壳单元的厚度。

13. Model→Views中可以保存视图，以便后续查看。

14. Element Tool→Dup Nodes可以设置容差，来检查是否有节点重合，顺便Merge它们。也可以用它检查是否存在Free Edge，这个是网格层面，而非几何层面的。实际就是不相容的单元，例如一条线两侧的单元的节点不重合，这个可以用Node Edit→Replace来处理。

15. Element Tool→Detach可以将共享节点的单元分离，相当于merge的相反操作。

16. Node Edit的align功能，可以将节点对齐到一条线上。

17. 在PrePost中open一个新的K文件，并不会导致关闭旧的，两个都会存在，可以在Model→Model selection中选择。还可以比较两个K文件中的关键字。
18. PrePost可以进行关键字之间的转换，例如将实体网格转化为厚壳网格。在keyword manager中选中实体关键字，然后右键transfer to，选择TSHELL，选中想要转化的实体单元即可。注意，转化并不会删除旧的实体网格。

19. PrePost可以通过壳单元及其section定义来生成相对应的实体单元或厚壳单元。在element generation→solid→solid by shell thickness，需要的话，可以勾选Create tshell element或勾选delete shell。

20. element generation还可以进行单元阶数的转化。例如Hex8→Hex20。

21. Hex20是8个顶点+12个边中点，Hex20是在Hex20的基础上加上6个面心和1个体心。

22. 可以使用Solid→Thick来将由表面构成的壳变厚，这是纯几何操作。

23. Geometry Tool→Model Management可以查看特定ID对应的几何或删除它。

24. Element Tool→Move or Copy的功能是将某些单元复制或移动到目标part中。

25. 可以在PrePost的Post→ASCII→gLStat中查看到，gLStat最多可以输出33个变量，但是默认并非所有都输出（默认为19个），能量相关的可以在`*CONTROL_ENERGY`中开启，例如沙漏能量。

26. PrePost中有些设置可以选择part或part set等，这个一般取决于该参数后面的STYPE参数，PrePost会自动根据后面的参数来决定点击前面参数右上角的实心圆点的效果。

27. 设置显示模式为edge，然后选择active（即当前可见的部分）即可，可以快速选中矩形板的四边。也可以使用by edge，勾选prop。

28. 可以将选择的内容保存save起来，后面直接载入load。

29. 获取part的质量时，使用measure由2种方式：

    1. 获取part，使用by part选择。推荐第一种。

    2. 获取element，使用by part选择。这种计算效率低，会慢点。

30. 有时要获取某个part包含单元或节点数量，可以blank其他part，然后点击菜单栏→view→Model info→Active Entities。也可以在Model→Part Data→show中查看。

31. 在Post→History中可以查看节点位移，这个是存储在d3plot中的，它的频率较低。如果要获取高频率的输出，可以可以开启`*DATABASE_NODOUT`，然后通过`*DATABASE_HISTORY_NODE_OPTION.`定义要输出的点。这个输出的频率可以设置很高。

32. 每次copy单元之后，都应该进行dup node检查，并合并。

33. 提交计算前，应该在Node Edit→delete中删除所有未被引用的节点或单元，并清理模型。

34. 从某个面拉伸生长出来的单元，会和该面的单元共享节点。

35. 在`*DEFINE_CURVE`中如果对横纵坐标轴进行了缩放，在plot时也会体现出来。

36. 复制实体几何时，需要确保filter是实体，否则容易选择到它的表面。

37. 可以使用stich功能将水密的多个面缝合构造成一个实体，勾选Try to Make Solid。

38. 某些关键字需要给定cureve ID，如果点击了NewKeyword，则会跳转到Keyword Manager的curve区域，需要手动选择并双击对应的curve关键字。有时不用手动选择，例如创建section时，因为它没有选择的必要。

39. 使用PrePost的element generation中shell from solid face功能，可以创建和实体单元表面共享节点的壳单元。有时需要将二者进行分离，可以使用detach或将壳单元移动并复制出去一份，然后删除原来的，然后再移动回来。

40. 一般按住Shift+左键可以平移，按住Ctrl+左键可以以edge模式查看的同时平移。所有的free edge都会显示，这有助于查看是否需要merge node。

41. 某些材料可以输出额外的历史变量，可以在`*DATABASE_EXTENT_BINARY`中设置NEIPH进行输出，例如`*MAT_072R3`。可以在PrePost的Fringe component > Misc > history var#n中查看它们。每种材料的历史变量的含义也不同。

42. 获得一个结构的外表面单元构成的网格，对实体单元进行删除操作，先选择所有单元，然后从中删除表面单元，使用prop技术。

43. Element Tool→morph工具可以对网格进行变形（类似于等参元的母子单元映射），例如将矩形正交网格，通过一边拉伸得到梯形网格。选择母实体和子节点，点击constrained，然后移动母实体的节点和边就会同步修改子节点的位置，最后记得回到该工具取消约束。

44. keyword manager左上角的NewID只是新增一个ID，不会修改其余的参数内容，而右上角的Add则还会用默认值填充参数内容。

45. 可以在measure中测量两点间的距离，也可以将它随时间变化的情况，绘制出来。

# K文件

1. K文件以`*KEYWORD`开头，以`*END`结尾，DYNA只会处理二者之间的部分。其中`*END`可以省略，此时会读取到文件末尾。

2. 输入文件可以分为多个子文件。.dyn是主文件，可以将一系列子文件串联起来。

3. 可以将模型文件（只包含`*NODE`，`*ELEMENT_option`，`*SET_option`，不过还有`*KEYWORD`和`*END`）单独保存，而将其余文件存在另一个文件中，在后者中使用如下语句引用：

   ```
   *INCLUDE
   model.k
   ```

4. 使用`*INCLUDE`关键字包含文件，会被当作多个子系统subsystem，后续在PrePost中添加关键字时，会自动存放在current subsystem中。在PrePost中新建子系统时，可以顺便指定它将来要存储的文件名。

5. 每个关键字前的*必须在第一列，数据行紧跟在关键字行之后，直到遇到下一个关键字行为止。关键字不区分大小写。

6. 第一列中的$表示，该行为为注释行。

7. 除了以下关键字的顺序之外，其余所有关键字的顺序可以任意：

   1. *KEYWORD定义开头。
   2. *END定义结尾。
   3. `*DEFINE_TABLE`后面必须紧跟`*DEFINE_CURVE`。因为表格就是多条曲线的组合，即曲线族。
   4. `*DEFINE_TRANSFORM`必须在`*INCLUDE_TRANSFORM`之前定义。
   5. 参数必须先在`*PARAMETER`中定义，才能使用。

8. 每个K文件中，必须具备如下关键字：

   ```
   *KEYWORD
   *CONTROL_TERMINATION
   *NODE
   *ELEMENT
   *MAT
   *SECTION
   *PART
   *DATABASE_BINARY_D3PLOT
   *END
   ```

9. 数据行可以采用固定格式，中间用空格分隔，也可以使用自由格式，中间用逗号分隔。PrePost导出的K文件一般用多个空格分隔，以使得一行80个字符，每项10个字符，这样更美观些，而且还包含用注释表示的每个参数的含义。

10. 自由格式和固定格式可以在不同关键字中混合使用，或者同一关键字的不同行间混合使用，但是同一行不允许混合使用。

    ```
    *NODE
    101 x y z
    102,x,y,z
    *ELEMENT_SHELL
    1001 pid n1 n2 n3 n4
    ```

11. 关键字后的每个数据行都称为一个card卡片，每个数据行由多个参数组成。文档中会指定每个参数的类型，I8表示不超过8位的整数，最大位99999999。A70表示不超过70个字符的字符串。F表示浮点数，无论自由格式还是固定格式，都会忽略每行前80个字符以后的任何内容。

12. 许多关键字具有OPTIONS或{OPTIONS}标识，前者是必选项，必须从多个待选中选择一个才可以，后者是可选的，可有可无。

13. 每个关键字都可以分成多次定义成多个数据组，例如`*NODE`可以在K文件的多处定义。不过使用PrePost到处K文件，会自动汇总排序。

14. 所有具备ID的关键字，都不允许重复使用ID。因为各个关键字之间通过ID来关联，互相引用。

15. 分析的类型通过control系列关键字设置。结果输出在database关键字中设置。

16. 常用的关键字如下：

    ```
    *NODE *ELEMENT
    *PART *MAT *SECTION
    *INITIAL *BOUNDARY *LOAD *CONSTRAINED
    *CONTROL
    *DATABASE *INTERFACE
    ```

17. 关键字在PrePost和手册中是以card卡片的形式给出的。一个关键字可以有多个卡片，有时卡片数量还取决于特定变量的值。每个卡片最多包含8个变量，每个变量都有名称variable，类型type和或默认值default。

18. ![image-20250102183115183](LS-DYNA.assets/image-20250102183115183.png)

19. K文件中不需要写variable，只需要按顺序给出数据即可。不过PrePost导出的K文件，都在数据行的上方会以注释的形式给出variable，方便用户后续手动修改。

    ```shell
    *CONTROL_SOLUTION
    $#    soln       nlq     isnan     lcint
         &soln         0         0       100
    ```

20. 使用PrePost读取K文件时，可以打开Misc.→view message info查看是否产生了错误信息。

21. Misc.→Keyword File Separate可以将K文件分割成多个。

22. Model checking可以检查接触，单元质量，关键字中引用的实体是否存在。

23. 在关键字的编辑页面中，可以勾选`use *parameter`，这与`*PARAM`关键字有关。推荐使用PrePost来设置，而非直接修改K文件。在`*PARAMETER`中定义参数，记得点击insert，然后再想要引用的关键字内勾选`use *parameter`，然后点击关键字内某个名字，就会跳出参数选择界面，选择完成后，需要再取消勾选`use *parameter`，然后才可以Accept，这样就完成了对参数的引用。这通常用于LS-DYNA和LS-OPT联合进行参数优化。引用其他参数的选项的输入框中的数据是蓝色的，可以通过这个来区分，直接修改该参数会报错，即使Accept，也会被忽略。

24. `*DEFINE_FUNCTION`，`*DEFINE_CURVE_FUNCTION`，`*DEFINE_FUNCTION_TABULATED`这三个关键采用一种类似于C语言的脚本语言，不用编译，可以自由灵活其定义各类载荷，例如引用计算时间，集合坐标，速度，温度，时间和压力作为自变量。

# 网格划分

1. Shape Mesher和Block Mesher都可以直接创建网格，而不需要借助几何，可以生成四边形或六面体网格。
2. Solid Meshing可以基于映射或扫掠创建结构化的六面体或五面体网格。
3. Auto Mesher借助曲面几何来生成三角形或混合网格（包含四边形），也可以对已有曲面网格重新划分网格（ReMesh）。
4. Tetrahedron Mesher的2种用法：
   1. 借助封闭的曲面网格生成四面体网格，这里的封闭壳网格可以是使用Auto Mesher对几何划分得到的。

   2. 也可以在Tetrahedron Mesher中对封闭曲面或实体（通过选择filter来完成）划分网格（选择skin Geometry），然后利用该曲面网格来划分四面体，步骤：输入edge来进行尺寸控制，然后点击Tria Mesh（这步会生成曲面网格），然后点击TetMesh。
5. Mesh→Element Generation可以根据实体网格抽取壳单元中面。
6. 可以先在几何中建立curve，然后在mesh→element generation中生成梁单元。
7. 为了能够将生成的球体进行删除单元，产生半球或1/4球等，需要将Shape Mesher的density设置为偶数。
8. 在划分完实体网格之后，应该使用Element Tool→Blank检查下实体内部的网格尺寸是否过小，避免稳定时间步长过短，这可以通过最小尺寸参数来控制。
9. 对于一个混凝土板中心受冲击的问题，可以在中心区域加密。例如使用如下网格形式，和S-ALE网格类似。
10. <img src="LS-DYNA.assets/image-20250205000744403.png" alt="image-20250205000744403" style="zoom: 50%;" />

# 截面和单元

1. `*SECTION_option`定义了单元算法，剪切因子和数值积分准则。

2. `*ELEMENT_XX`要使用对应的`*SECTION_XX`。

3. `*SECTION_SHELL`一般就修改以下NIP（厚度方向积分点数量）和厚度T1（修改完，按回车键即可）。

4. 如果使用了完全积分的壳单元，例如公式16，则可以保持默认的2个截面积分点即可，不用增加该值。

5. 在`*SECTION_SOLID`中ELFORM的S/R表示selective reduced（选择性缩减积分）。

6. Solid单元如果是受弯为主，则应使用ELFORM=2，而非默认的单元公式，否则应该在厚度方向上划分4层。

7. 二阶单元使用`*ELEMENT_SOLID_H20`创建，可以通过Element Generation将8节点的实体单元转化为20节点的。

8. LS-DYNA的`*ELEMENT_option`只是负责构建单元拓扑，也就是形状。同样的solid可以使用各种不同的单元公式，而在Abaqus中，这是在单元层面就区分开的，而非在Section层面。这也是LS-DYNA单元数量较少的原因。

9. 实体和壳单元的截面使用不同的关键字，`*SECTION_SOLID`和`*SECTION_SHELL`，但是他们的SID不能重复。单元公式ELFORM也在Section中设置。显式计算默认的单元公式就是一阶缩减积分，在隐式计算中才推荐使用完全积分。

10. 梁单元支持spot weld beam公式，要配合*MAT_SPOTWELD一起使用。

11. 0D单元包括线性弹簧和扭转弹簧。

12. 弹簧的2种定义方式：
    1. 使用`*ELEMENT_DISCRETE`定义单元，`*SECTION_DISCRETE`定义截面，这样定义的弹簧单元需要使用专用的材料`*MAT_SPRING_ELASTIC`，输入劲度系数k即可，比较推荐。

    2. 使用类型6的梁单元（也就是行为和弹簧一样的梁），如果要求弹簧的作用线不是节点N1到N2，即VID≠0，则建议使用这种。

13. 要组合弹簧和阻尼器，不能通过为`*ELEMENT_DISCRETE`设置两种材料来完成，因为一个单元只能属于一个part，而一个part只能有1种材料。可以共用节点，创建2个单元，一个弹簧，一个阻尼器即可。
14. TShell就是厚壳，类似于Abaqus的连续体壳，单元形状和实体一样，但是公式是壳公式。

15. cohesive单元可以使用实体单元的公式19或壳单元公式±29。材料推荐使用`*MAT_COHESIVE_MIXED_MODE`（138）或`*MAT_COHESIVE_GENERAL`（186）。

16. 在Model Check中，如果对于四面体网格使用的Section中elfrom不是4，10或13，则会报error，建议改成10。

17. 多层复合材料可以将`*SECTION_SHELL`中的ICOMP开启，也可以使用`*PART_COMPOSITE`来指定每层的材料，厚度和方向，然后记得将对应的壳单元move到通过`*PART_COMPOSITE`创建新part中。

18. 复合材料铺层的0度可以在Element Edit→Direction→Shell中查看。

19. 对于薄壳结构，可以不抽取中面，而是只使用内或外表面，然后在`*SECTION_SHELL`中设置NLOC为1或-1。

# 沙漏

1. 为了提高计算效率，DYNA中大量使用（一阶缩减）单点积分单元，这可能导致沙漏问题（这是该单元最大的缺点）。沙漏是一种高频零能伪变形模式，不理想的沙漏模式往往具有比结构响应周期短得多的周期，并且通常被观察到是振荡的。它在数学上是稳定的，但是在物理上是不真实的。此时单元没有刚度，结构虽然有变形，但是没有应变，不消耗能量，变形呈现锯齿状。之所以称为沙漏，可以参见下图，两个相邻的四边形，在没有沙漏控制的情况下，变形会得到两个梯形，组合在一起看起来像沙漏。

2. ![image-20250111212335778](LS-DYNA.assets/image-20250111212335778.png)

3. 沙漏控制就是通过消耗一部分能量去抵制这种不正常的变形模式，这个能量就称为沙漏能。采用完全积分单元可以完全避免沙漏问题，但是求解效率会降低，同时可能出现体积自锁问题。DYNA通过`*HOURGLASS`（Part级别）或`*CONTROL_HOURGLASS`（全局级别），增加单元的刚度或粘性，从而提高抗变形的能力。IHQ参数表示沙漏控制模式，高速变形推荐采用粘性控制模式，低速变形推荐采用刚度控制模式。沙漏刚度系数QH默认为0.1，一般取为0.05-0.12，如果太大会导致数值不稳定。
4. 对于壳和膜单元，QM被视为膜沙漏系数，弯曲为QB，翘曲为QW，这些系数可以单独指定，但一般来说，QM=QB=QW就足够了。
5. 计算结束后，应该检查Hourglass Energy，确保<Internal Energy的10%。通常使用`*DATABASE_GLSTAT`输出全局统计和能量，`*DATABASE_MATSUM`输出各个part的能量，它们会输出成同名的文件。在Post→ASCII中打开，如果存在对应的输出文件，则选项后面有星号，Load后，再点击下面的内容进行绘图。

6. 还需要使用`*CONTROL_ENERGY`关键字开启计算沙漏能量，因为计算该能量的消耗不可忽略，所以默认没有开启。


# 后处理

1. DYNA计算结果文件中的d3hsp是ASCII格式，包含大量求解初始化和求解过程中输出信息，由于该文件通常特别大，用户直接打开搜索不太方便，因此可以使用PrePost读取该文件，Misc.→D3hsp以树和列表形式显示内容，还可以搜索。注意不在File→Open中打开。

2. ALE的问题求解完成后，默认只能看到背景网格（一般不变形），看不到流体运动，需要在Select Part中开启左侧的Fluid(ALE)才可以显示ALE Group。

3. 如果在求解没有完成时就查看结果，一般最后一帧的结果会非常失真，这是正常现象。



# 材料模型

1. 材料模型的关键字可以是具体名称，也可以是编号，例如`*MAT_001`等于`*MAT_ELASTIC`。

2. 只有用于实体单元的材料才可能定义状态方程。

3. 常用的材料模型：

   ```shell
   *MAT_ELASTIC #1号，各向同性，线性亚弹性，需要给出密度，弹性模量，泊松比。可用于梁，壳，实体单元。不适用有限应变，如果要模拟有限应变，应该使用MAT_002
   *MAT_PLASTIC_KINEMATIC #3号，各向同性，双线性强化，可以考虑率效应。性价比非常高，可用于梁，壳，实体单元。通过修改β参数来设置强化形式，β=0表示运动强化，β=1表示各向同性强化，如果β在二者之间，则为混合强化。
   ```

4. *MAT_PLASTIC_KINEMATIC材料模型可以使用Cowper Symonds应变率模型来考虑应变率效应，它根据$1+(\frac{\dot{\varepsilon}}{C})^{1/p}$来对屈服应力进行缩放。card2中的SRC和SRP分别为参数C和p，默认均为0，表示不考虑应变率效应的缩放。默认情况下VP=0，表示应变率效应会对屈服应力进行缩放，也可以设置VP=1，此时为完全粘塑性公式，它在屈服面内结合了Cowper Symonds公式。

5. 对于`*MAT_PLASTIC_KINEMATIC`，如果β=1，此时推荐使用`*MAT_ISOTROPIC_ELASTIC_PLASTIC`，12号材料，它需要更少的存储，因为不用存储背应力，且更高效。不过对于壳单元，它的精度不够，还是推荐使用2号材料。

6. 分段线性MAT_024模型中，支持三种输入方式：曲线LCSS；数据点EPS，ES；屈服点和硬化模量。按照曲线>数据点>屈服参数的优先级采用。数据点的横坐标是EPS（有效塑性应变），纵坐标是ES（有效应力），对于单轴拉伸，有效应力就是单轴应力，有效塑性应变为单轴塑性应变，因为一般假设塑性变形是等体积的，即泊松比为0.5。

7. 可以从K文件中导入其中定义的材料，在keyword→loadMatDb，选择对应的K文件即可。不过需要选中mat关键字才会出现loadMatDb。

8. 可压碎泡沫（crushable foam）是指类似于聚氨酯泡沫的材料，受压缩时，它会碎裂，而非海绵一样的泡沫。在DYNA中，可压碎泡沫经常和混凝土，土壤共用相同的简单材料模型。

9. 在Load Cruve中，ordinate表示纵坐标，abscissa表示横坐标。

10. 一些关键字（例如*MAT_005）允许使用关键字自带的表格输入（一般是10个点，每个点一个横坐标，一个纵坐标），也允许通过引用用户定义的曲线来输入，后者的优先级高。

11. unloading表示卸载，而非未加载。

12. 应变硬化（Strain Hardening）是指材料在塑性变形过程中，随着应变的增加，其屈服强度逐渐提高的现象。

13. Tensile cutoff是拉伸截止，也就是破坏时的最大主应力。

14. 很多材料模型都需要配合状态方程使用，因为材料模型仅处理偏应力和塑性变形相关的行为，而压力和体积应变的关系需要状态方程来处理。

15. 状态方程是表征流体内压力，密度，温度等三个热力学量的关系式，当材料内的应力超过屈服强度数倍以上时，材料在高压下的剪切效应可以忽略不计，固体也会呈现出流体性质，相应可以用热力学参数描述。

16. DYNA支持用户自定义材料模型和状态方程。

17. 对于应变率敏感的材料，有的支持输入多条在不同应变率下的应力应变曲线。曲线使用`*DEFINE_CURVE`定义，多条曲线通过`*DEFINE_TABLE`组合起来，横坐标为曲线对应的应变率，纵坐标为曲线编号。

18. 应变率敏感材料有两个点需要注意，不同应变率下会有不同的应力-等效塑性应变的曲线，不同应变率下会有不同的屈服应力。前者通过table定义，后者通过curve定义。这可以在`*MAT_PIECEWISE_LINEAR_PLASTICITY`中的LCSS和LCSR看到。

19. 损伤damage和失效fail是不一样的。前者一般存在一个标量因子，0表示无损伤，1表示完全损伤，损伤一般会影响材料的模量或其他力学性质，使得材料性能退化。失效是用来标识哪些单元要删除的，失效可以是损伤达到阈值或者是单纯地满足某些准则，例如最大主应力，有效塑性应变等。

20. 当发生单元失效而删除时，解一般会出现波动或震荡。

21. 空气的MAT和EOS：见YouTube视频

22. 水的MAT和EOS：

23. 水的密度并非是`1000kg/m^3`，20℃时，为`998.23kg/m^3`。

24. 使用多种基本实验拟合出材料模型后，应该在软件中对基本实验进行建模并计算， 检查对应的输出是否和实验一致。

25. TNT的材料一般为`*MAT_HIGH_EXPLOSIVE_BURN`（8号），EOS一般为`*EOS_JWL`（2号）。

26. 钢材可以使用Johnson-cook材料模型（15号），配合Gruneisen EOS使用（4号）。

27. GFRP布可以使用`*MAT_ENHANCED_COMPOSITE_DAMAGE`（54号）材料来建模。

# 混凝土材料

1. 16、72、96和84号材料支持整体式建模来模拟钢筋混凝土，它将钢筋混凝土当成一种复合材料。也可以进行分离式建模，此时使用梁单元以离散方式对钢筋进行建模。这些梁可以合并到实体混凝土单元（共节点），或者可以使用1-D接触（这可以处理粘结滑移）连接到混凝土单元，或者可以通过`*CONSTRAINED_AGRANGE_IN_solid (CTYPE=2)`连接到混凝土单元。最后一种方法消除了必须将梁节点与实体单元节点对齐的负担，但是要注意钢筋对混凝土的约束可能会与对称边界条件等其他约束冲突并破坏这些约束。
2. 混凝土在DYNA中的材料模型。

   1. MAT_084（Winfrith Concrete Model），输入简单，直接输入抗压强度，抗拉强度即可，裂纹可以显示为条纹图，在d3crack中。需要添加`*DATABASE_BINARY_D3CRACK`关键字，并在求解器命令中添加`q=`选项，值可以是d3crack或crack，对于LS-run，文件名默认为crack。如果没有`q=`选项，则不会输出文件。在PrePost→Open→others→Crack File中打开。裂缝数据要比单元失效更具直观性。该模型没有内置单元失效功能，可以使用`*MAT_ADD_EROSION`来附加。

   2. MAT_159（Continuous Surface Cap Model，CSCM），可考虑实验数据，材料表现稳定，可设置DIF，可以考虑侵蚀失效，参数建议设置为1.05-1.10。14个参数。

   3. MAT_072R3（KCC），第3个版本，有三个剪切破坏面，可考虑实验数据，可设置DIF，需要状态方程配合。可以针对不同围压考虑。9个参数。

   4. MAT_272（RHT），脆性材料，可以考虑高应变率，可设置DIF，不是很完善。
3. 最常用的K&C Concrete模型，是由Karagozian&Case开发的，它是一家国际公认的科学和工程咨询公司，1945年成立，不过也是该公司两个创始人的姓名。
4. 最推荐使用KCC模型，需要输入如下数据：
   1. MAT_072R3关键字。

   2. DEFINE_CURVE，在LCRATE中引用其ID，应变率的规则是受压为正。纵坐标要求是剪力增强因子而非DIF，前者是针对剪力，后者是针对主应力，因为实验数据一般是没有围压的，此时，剪力就是主应力的一般，可以将二个增强因子看成一样。

   3. MAT_ADD_EROSION关键字。用于为本身不包含失效行为的材料添加失效行为。MID参数就是基本材料的ID。支持多种变量来设置失效限值。

   4. EOS_TABULATED_COMPACTION，横轴为体积应变率，纵轴为压力。
5. <img src="LS-DYNA.assets/image-20250126183142959.png" alt="image-20250126183142959" style="zoom:67%;" />

# 钢筋混凝土建模

1. 
2. 钢筋和混凝土的耦合可以使用：

   1. constrained beam in solid，将混凝土的能量全部传递给钢筋，没有能量损耗，梁截面的elform需要时1或11。混凝土为master，钢筋为slave。

   2. constrained Lagrange in solid，将钢筋节点和混凝土节点用弹簧连接，针对握裹力设定弹簧的刚度PFAC，通常为0.1。
3. 有了上面的耦合，就可以不用定义接触了。

4. 喷涂的聚脲涂层和混凝土的粘结关系，可以用tiebreak，达到某个值就会发生分离，用于tie的两个part，网格需要对齐匹配。
5. 钢骨混凝土的建模比较特殊，由于钢材占比较高，不能使用重叠的网格，可以将混凝土中的部分单元转化为钢骨。然后将二者detach，然后设置contact，这里建议使用较高的摩擦系数，例如0.9。


# 接触

1. DYNA具有60多种`*CONTACT`接触类型，例如变形体对变形体，变形体对刚体，刚体对刚体，边边接触，侵蚀接触，拉延筋接触等。`*DEFINE`也可以定义接触，例如`*DEFINE_SPH_TO_SPH_COUPLING`定义SPH part间的接触，`*DEFINE_DE_TO_SURFACE_COUPLING`定义离散元颗粒与有限元结构的接触。

2. 使用`*CONTACT_AUTOMATIC_SINGLE_SURFACE`设定接触时，可以点击名称右侧的小按钮来选择已有的segment set ，shell element set ，part set，part，node set 等，如果没有，则会提示创建，选择NewEntity即可。由于是single surface，只需要选择一个面即可，它既是master，又是slave。

3. segment就是单元的face。不分正反面，相邻单元共享的face认为是一个segment。

4. 摩擦行为通过设置FS（静摩擦系数），FD（动摩擦系数），DC（衰减指数）。显式分析中使用的等效摩擦系数为：$\mu_c=FD+(FS-FD)e^{-DC|v_{rel}|}$​，和相对速度有关。

5. 在可选card A中，可以指定使用罚函数公式（默认），还是约束公式。

6. LS DYNA中会将tie作为接触的一种，因为它的一个特化，tiebreak允许tie失效，而变成可以分离和滑动的普通接触。

7. 罚接触公式中，罚刚度会根据单元尺寸和材料性质来计算：

   1. 对于壳来说，$k_1=sLSfac*sf*K*A/d$。其中sLSfac是全局缩放因子，sf是局部缩放因子，K是体积模量，A是单元面积，d是厚度或最短对角线。

   2. 对于实体来说，$k_1=sLSfac*sf*K*A^2/V$。其中A是segment面积，V是单元体积。

8. 对于罚接触来说，如果接触的两个面的材料相似，计算效率就比较高，如果一个很硬，一个很软，则容易失效，此时可以缩小card3中的slave面的局部缩放因子（例如为0.1），降低slave侧的冲击，减少过大的穿透。

9. bsort参数可以指定搜索接触配对的频率，每隔bsort个增量才会搜索一次，对于single contact，该值为25或100。surface to surface或node to surface，为10~15。如果为0，则由DYNA自己决定，可以在d3hsp中找到，为`number of time steps between contact searching`。如果发现穿透较多，可以降低这个参数的值，来提高搜索频率。

10. sLSfac是在`*control_contact`中设置，默认为0.1。

11. PrePost中可以检查tie的效果或初始穿透，菜单栏→application→Model checking→general checking。

12. tied接触，默认会将slave点拉到master面上，接触面上的单元会变形。

13. mortar contact是DYNA中专门为隐式分析使用的接触公式，它是segment to segment，基于罚函数的。

14. 一般常用contact_automatic_surface_to_surface指定接触对，可以输出接触力。

15. part较多时，可以创建一个包含所有可能接触的part的set，然后使用`*CONTACT_AUTOMATIC_SINGLE_SURFACE`接触。缺点是无法输出接触力，可以使用`*CONTACT_FORCE_TRANSDUCER_PENALTY`来指定特定接触的接触力输出。

16. 对于复杂模型，可以先用contact_automatic_single_surface，试跑一段时间，检查其他keyword，如果没有问题，可以修改为特定的接触类型。

17. 一般需要打开card1的最后2个参数，sapr和sbpr。

18. 推荐设置`*CONTROL_CONTACT`的ENMASS为非零，这样可以让因失效而删除的单元的失效节点在接触算法中保持活动状态。

19. 对于一些高压缩性的泡沫，其材料需要定义致密段，否则可能由于过度软化，造成负体积。也建议设置`*CONTACT_INTERIOR`和`*HOURGLASS`，高速冲击建议IHQ=3，低速冲击建议IHQ=6。设置错误的话，可能会出现波浪状的沙漏状态。

20. 有时，表面参与接触的单元可能会由于失效而被删除，此时由于内部单元的表面没有被定义接触，因此会直接产生穿透，此时使用by part来选择所有的segment，来作为参与接触的surface。

21. single surface，constraint-based，automatic surface-to-surface，和automatic nodes-to-surface始终会考虑接触时壳单元的厚度。

22. GFRP包裹混凝土柱分析中，二者的相互作用使用`*CONTACT_TIED_NODES_TO_SURFACE_OFFSET`。Node为混凝土的外表面节点，surface为GFRP的内表面segment。不过这种情况下，GFRP只会和混凝土的外表面相互作用，如果混凝土外表面发生失效，则会失真。之所以使用offset，是因为建模的时候，二者是分离的，间距为GFRP层的一半厚度。

23. 对于切削模拟，contact中，如果工件是以part或part set指定的，则他的表面被破坏后，内部并不会和刀头产生接触，因此应该使用segment set，然后使用by part选择，这样该part的所有单元的face都会和刀头产生接触。


# 初始和边界条件

1. 可以在create entity中创建CNRB（constrained nodal rigid body），它是由节点构成的刚体域。

2. constrained_joint可以构建球铰，销钉等连接单元。

3. *CONSTRAINED_RIGID_BODIES可以将两个刚体连接起来，刚体需要是由\*MAT_RIGID构成的，但是不是CNRB。

4. `*BOUNDARY_SPC`限制自由度，`*BOUNDARY_PRESCRIBED_MOTION`边界运动，`*INITIAL_VELOCITY_GENERATION`指定初始条件，`*LOAD_NODE`和`*LOAD_BODY_`指定集中力和体积荷载。体积载荷是以加速度的形式给出，默认全局赋予，除非使用`*LOAD_BODY_PARTS`指定要施加的part set。`*LOAD_BODY_Z`的加速度以-Z方向为正，因为会替换成惯性力。

5. 推荐使用`INITIAL_VELOCITY_GENERATION`而非`INITIAL_VELOCITY`，因为后者只能给nodeset施加速度，这样如果重新划分网格，则会失效，前者可以给part或part set施加。

6. 这些边界条件可以对单个节点或节点构成的集合设置，推荐使用CreateEntity来使用。

7. `*RIGIDWALL_option`是专门用来创建刚性墙的关键。这样可以简化其他部分和刚性墙的接触定义，其输出也可以方便的在`*DATABASE_RWFORC`中设置。可以创建移动的刚性墙，不过只能设置初始条件，如果设置其质量非常大，则可以认为速度不变，相当于边界条件，而不仅是初始条件。

8. 位移边界条件处的节点反力通过`*DATABASE_BNDOUT`输出。

9. 或者`*DATABASE_NODFOR`和`*DATABASE_NODAL_FORCE_GROUP`输出，前者开启输出，后者定义节点的集合。

10. 转动初始条件也使用`*INITIAL_VELOCITY_GENERATION`，OMEGA参数就是转动就角速度。角度使用弧度单位。只需要定义转动中心坐标和转动轴的向量即可。


# 加载

1. 可以使用`*LOAD_NODE_SET`对节点集合施加荷载，该值为合力，会在每个节点上均分。
1. Conwep只能用在非接触爆炸，也就是距离较远的情况。ALE对于接触和非接触爆炸都可以。
1. 使用`*LOAD_BLAST_ENHANCED`来设置TNT炸药时，还需要使用`*LOAD_BLAST_SEGMENT`，设置哪些segment会受到该爆炸的作用。可以使用`*DATABASE_BINARY_BLSTFOR`输出爆炸压力。
1. 使用ALE来模拟爆炸行为，需要对炸药物质进行具体建模，TNT炸药和空气都是ALE的多物质组，加载的结构是Lagrange部分。使用`*INITIAL_DETONATION`来引爆TNT的part，起爆点一般设置为part的中心位置。

# 求解输出控制

1. DYNA将增量称为时间步长time step，这个和Abaqus不一样，一般在1e-6秒数量级。可以使用使用`*CONTROL_TIMESTEP`指定初始时间步长DTINIT，目标时间步长DT2MS（会使用质量缩放来确保）。如果是冲击问题，默认的初始时间步长，对于较低的速度来说，还需要多个时间步长才会真正发生碰撞，因此可以手动计算间隙，然后除以速度，来得到初始时间步长，实际设置的比这个略小即可，这样可以快速略过无意义的时间。

2. 一般质量缩放后，超重应该低于10%，可以使用endmas参数控制。在求解输出的message中也可以查看到这个，calculation with mass scaling for minimum dt的ratio。

3. 使用质量缩放求解准静态问题完成后，应该检查全局的动能应该＜5%的全局总能量。

4. 对于高速变形问题，建议使用粘性沙漏控制。刚度控制通常更适合较低的速度，特别是在时间步长较大的情况下。

5. 普通求解时，会将`*CONTROL_TIMESTEP`的TSSFAC设置为0.9，如果是高速碰撞，建议设置为0.67。这个用来控制实际使用的时间步长和计算得到的时间步长的比值。

6. DYNA自动计算的dt和负体积无关，后者主要和网格品质有关。

7. `*CONTROL_TERMINATION`用来指定求解终止的时间。其中的DTMIN可以指定time step相比于初始时间步长（DYNA自动计算的，并非用户设置的）的缩小下限，如果小于这个值，则会终止。

8. 可以输出的内容有：ASCII DATABASE，BINARY DATABASE，INTERFACE。

   1. ASCII的输出频率可以设置较高，可以输出特定资料。要输出的项就在关键字中的项前勾选即可，每项可以单独指定dt，都会在工作目录中生成对应的文件。在手册中已经分类整理好了。在post→ASCII中查看，有星号标记则表示存在该数据，可以查看，点击对应项，然后load即可。

   2. `*DATABASE_BINARY_PLOT`可以设置输出d3plot（也就是1帧）的时间间隔。即使不设置，也会至少将求解时长切分20份。在Post→Fringe中查看动画。

   3. INTERFACE包含part的应力应变及其边界条件，以关键字的形式输出，可以作为后续分析导入。

9. d3plot文件的数量并非输出的帧数，DYNA会自己觉得何时创建新的文件。

10. `*DATABASE_ASCII_option`中可以统一设置DT，输入完成后，敲击回车即可为所有选项设置DT。

11. D3PLOT关键字中可以设置DT，也可以设置一共输出多少次NPLTC，这个会覆盖前面的DT设定，即DT=ENDTIM/NPLTC。

12. 对于`DATABASE_BINARY_option`，还可以指定LCDT来设置随时间变化的输出频率。例如接触前和分离后使用低频率输出，其余时间使用高频率输出。

13. 如果要输出特定节点（集合）或单元（集合）的时间历程数据，可以使用`*DATABASE_BINARY_D3THDT`。

14. 勾选`DATABASE_ELOUT`，可以开启输出单元数据功能，具体输出哪些单元，需要在`*DATABASE_HISTORY_`中设置。可以在CreateEntity中创建，根据单元类型选择。

15. 有些database的输出直接勾选即可输出，有些勾选完成之后还需要指定对哪些对象进行输出，例如secforc，还需要定义`*DATABASE_CROSS_SECTION`。

16. 可以在select part中设置，只显示部分part等，然后在file→save as→save active keyword as来只保存显示部分的关键字，不过这样会导致引用未显示部分的关键字出错。

17. 一般来说动态分析使用单精度就够了，隐式或准静态使用双精度（因为存在很多矩阵操作）。

18. 显式求解对于内存的需求比隐式小得多，一般几百M就够了。

19. 求解过程中的信息保存在message文件中。有些重复性的消息并不会全部输出到命令行窗口，但是都会记录在message文件中。

20. 求解过程中，在命令行界面，按Ctrl+C可以中断求解器，提示enter sense switch。可选的有：

    ```shell
    sw1 #输出重启动文件d3dump，然后终止此次求解
    sw2 #输出预估的剩余计算时间，实际时间一般会比这个值要低。
    ```

21. 重复运行时，建议每次运行前，将之前的d3plot文件都删除掉，否则可能会将2次的结果串接起来，造成混淆。

22. 尽量不要定义重复的接触。

23. 使用PrePost进行后处理时，只需要选择d3plot即可，后续的文件会自动打开。

24. 一个d3plot文件会包含多个帧，DYNA根据文件大小自动决定何时构建一个新的文件。

25. 负体积问题可能的原因：

    1. 网格品质差，例如长宽比过大，一旦受力，短边节点容易跑到另一侧。

    2. 所选材料模型不合适，造成冲击瞬间，结构发生很大变形。

    3. 如果给与模型过大的冲击速度或力量，也会造成很大变形。可以检查并修改contact中的摩擦系数或scale factor。

    4. 较薄零件若无缓冲效果，例如胶结，可以不使用此零件，直接使用tiebreak contact将两边零件tie住。

26. binout和d3plot是LS-DYNA中两种不同的文件格式，虽然它们都用于存储仿真结果，但它们的用途和内容有所不同。区别如下：

    1. d3plot存储几何和结果数据，主要用于后处理可视化，可以产生动画或进行时间序列分析。文件通常较大，文件名通常为d3plot、d3plot01、d3plot02等（用于分卷存储）。

    2. binout是用于存储纯结果数据的二进制文件，主要用于高效存储和提取特定结果数据。 不包含几何信息，只存储结果数据。文件结构更紧凑，适合快速读取特定数据。可以通过LS-PrePost→post→binout或编程工具（如Python）提取数据。

27. 实际上binout是和ascii out对应的，这个可以在`*DATABASE`的BINARY选项。SMP的默认输出为ASCII，MPP的默认输出为binout。

28. 可以在系统命令行启动LSPrePost时，使之读取cfile：

    ```shell
    LS-PrePost c=commandfile #可以加入-nographics，不启动GUI，但仍以批处理模式执行命令
    ```

29. `*CONTROL_ACCURACY`关键字可以控制求解的精度。

30. `*CONTROL_SOLUTION`中SOLN可以指定分析的类型为纯结构，纯热力学或耦合分析。

31. 热分析一般要定义`*CONTROL_THERMAL_SOLVER`，需要设置是否是瞬态ATYPE，是否是线性PTYPE。如果求解报错，可以尝试修改SOLVER。

32. 热分析的分析步相关设定为`*CONTROL_THERMAL_TIMESTEP`关键字。

33. 摩擦生热的问题中，需要修改`*CONTROL_CONTACT`的FRCENG为1。

34. 结构热耦合分析中，可以勾选`*DATABASE_TPRINT`输出耦合结果。

35. 热分析中，需要设置初始条件`*INITIAL_TEMPERATURE_SET`，一般为室温。如果没有设置，可能会报错。

36. DYNA中将每次输出，称为一个state，类似于Abaqus的frame。


# 隐式分析

1. 隐式分析需要设置如下关键字：
   1. `*CONTROL_IMPLICIT_GENERAL`，将IMFLAGS设置为1，才会开启隐式分析功能，默认为显式。DT0为隐式分析的初始时间步长，一般为总时间的1/10到1/100。

   2. `*CONTROL_IMPLICIT_AUTO`，将IAUTO设置为1，使用自动时间步长。每一个time step使用迭代次数在11±5次内。

   3. `*CONTROL_IMPLICIT_SOLUTION`，NSOLVER设定使用的求解方法，默认是非线性求解器，如果是线性的，可以手动设置以加速求解，这里类似于Abaqus的几何非线性开关。还可以设置收敛容差，DCTOL为位移相对收敛容差，ECTOL为能量，RCTOL为力残差。

   4. `*CONTROL_IMPLICIT_SOLVER`，LSOLVER设定使用的线性方程求解器。

   5. `*CONTROL_IMPLICIT_DYNAMICS`，IMASS设定静态（默认）还是动态分析（使用Newmark积分）。

2. 当进行隐式静态分析时，时间只是代表加载的比例，而非具体的时间，因此时间的单位也不重要了，一般将结束时间都设置为1。隐式静态分析时，初始时间步长一般设置为总长的5%。

3. 当使用隐式分析时，推荐使用mortar版本的接触方式。

4. 模态分析提取使用`*CONTROL_IMPLICIT_EIGENVALUE`关键字，对应的结果文件为d3eigv。

5. 隐式分析中，使用的荷载曲线应该是渐变（ramp）的，而非显式的突变（step）。

6. 进行隐式转显式分析时，会生成DYNAin文件，他是一个包含初始应力的k格式文件。

7. DYNA默认进行显式求解，除非指定隐式关键字。

8. DYNA的焊接可以处理点焊，对焊，角焊。


# ALE

1. 为了使得拉格朗日算法能够处理大变形问题，提出了自适应网格重划分（Adaptive Remesh）方法，它根据计算结果估计误差，按需重新划分网格，将旧网格中的物理量映射到新的高质量网格上，继续计算，这样一直循环。缺点：每次重划分会导致一些物质扩散和历史纪录的丢失。通常用于薄板冲压，薄壁结构受压屈曲，三维锻压等大变形问题。除此之外，DYNA还有无网格伽辽金和ALE自适应网格重划分方法。

2. 欧拉分析和ALE可以克服拉格朗日算法在网格畸变时数值求解困难的问题，易处理大变形问题，也可以进行流固耦合分析。缺点：难以获得材料场变量的时间历程。难以跟踪材料界面。因为ALE会将变形后网格中单元变量映射到ALE网格中，因此也会产生误差。

3. 在DYNA的Multi-Material ALE算法中，一个单元最多可容纳20种材料。

4. DYNA中壳单元厚度方向的积分规则可以是高斯积分或Lobatto积分，后者是固定左右边界点的高斯积分，牺牲一定的灵活性，但是确保考虑边界。Lobatto和Simpson类似，都会考虑边界，但是Simpson是均匀的，Lobatto是非均匀的。默认是2点的高斯积分。Lobatto规则对于2点积分特别不准确，因此最少3个积分点。

5. 定义结构网格时，可以指定局部坐标系ID，来生成转动过的结构网格。

6. ALE不支持隐式积分和动态松弛（DYNAmic relaxation）。

7. 欧拉分析相比拉格朗日来说多了个固定的背景参考网格，而ALE相比欧拉分析来说，该背景参考网格可以移动。S-ALE相比ALE多了自动生成网格的步骤。

8. ALE求解器没有湍流或边界层特征，因此它不适用于对需要这些特征的传统CFD问题进行建模。

9. 除了ALE公式5支持接触外，ALE通常不支持接触。

10. 三维空间中，ALE仅支持一个点实体单元。可以是六面体、五面体或四面体。后者被视为退化六面体单元，因此，对流计算可能不准确，并导致LS-DYNA崩溃，因此建议仅使用具有六面体单元的ALE网格。

11. 对于每种ALE多材料，在单个积分点对每个固体单元中的应变和应力进行评估。从这个意义上讲，ALE单元公式等价于ELEFORM=1的实体单元公式。

12. `*BOUNDARY_SALE_MESH_FACE`可以简化对ALE网格施加边界条件。

13. 对于模拟油罐车刹车制动，可以为液体和空气域设置初始速度，汽车本身设置速度边界条件（迅速降低到0），前者的速度和后者的速度应该一致。这个问题和铁球跌落入水不同的是，这里还需要设置参考系来描述ALE网格的运动。使用`*ALE_REFERENCE_SYSTEM_NODE`定义一组控制ALE网格运动的节点，实际是一个由3个节点定义的坐标系。然后在`*ALE_REFERENCE_SYSTEM_GROUP`中的PRID引用上述定义。

14. 如果是实体单元，则不用考虑法线问题，因为始终是part的外表面参与耦合。如果使用壳单元作为ALE分析中的拉格朗日结构，则必须要确保它的法线是指向ALE部分的。两种思路：

    1. 修改壳单元的法线指向。
    2. 修改`*CONSTRAINED_Lagrange_IN_SOLID`的NORM参数，因为拉格朗日segment将仅在该segment的一侧与流体耦合。NORM决定哪一边。类似于接触分析中的one-way。

15. 使用penalty-based的流固耦合算法，会产生一些穿透，这个和接触问题是类似的。

16. 一般涉及到液体和固体的流固耦合问题，空气部分可以设置为真空Vacuum（只需要给一个特别小的密度即可），这样可以省略状态方程。例如液晃问题，或落水冲击问题。

17. 对于水这样的纯流体，材料可以是`*MAT_NULL`，这种材料允许在不计算偏应力的情况下考虑状态方程。如果是实体单元使用该材料，必须配合状态方程使用，如果是水的话，一般为`*EOS_GRUNEISEN`，`*EOS_MURNAGHAN`，`*EOS_MIE_GRUNEISEN`。

18. 多物质ALE单元的elform一般为11。

19. ALE一般要指定hourglass关键字。

20. 流固耦合问题中，需要使用`CONSTRAINED_Lagrange_IN_SOLID`将结构耦合到ALE的流体单元中。如果ALE网格和拉格朗日网格重合较好，尺寸相似，参数NQUAD（分布在每个耦合拉格朗日曲面segment上的耦合点数量）可以使用默认，否则应该增加，例如3*3。

21. 流固耦合的方向一般选择法向受压比较稳定，即DIREC=2。这样流体不会反向拉动固体，类似于可以分离的接触。

22. 如果是像铁球跌落入水的问题，CTYPE建议为4，如果是封闭界面的液晃问题，建议为3。对于TNT在空气中爆炸，对结构加载，建议为5，这是因为结构可能会失效，造成内部的单元暴露出来，ctype=5允许对侵蚀的单元加载，如果是4，则只会和表面单元耦合。

23. 可以设置MCOUP=1来简化流固耦合计算，也就是只和密度最高的材料耦合。通常不建议使用MCOUP = 0，这会将耦合应用到所有材料，导致无法准确计算流体界面（因为体积分数总是 100%）。没有明确的界面，就无法跟踪流体泄漏。

24. LS-DYNA 通过计算耦合的 ALE材料的体积分数来确定流体耦合界面。具体来说，界面位于体积分数为 50% 的位置。

25. 使用`*ALE_MULTI-MATERIAL_GROUP`来定义使用ale单元公式的每个group，一般一个part作为一个group。

26. 推荐将`*CONTROL_ALE`设置为：DCT=-1（使用增强的对流逻辑，尤其是对于爆炸来说），AFAC=-1（光滑权重因子，-1表示关闭）。

27. FSI中，一般会将`*CONTROL_TIMESTEP`的TSSFAC设置为0.67，虽然可能是低速冲击，但是考虑到流体的存在，建议这么设置。

28. 流固耦合中可以额外输出`*DATABASE_BINARY_FSIFOR`ALE界面的力，需要给定part set的ID。同时还需要在求解器的命令中添加`h=fsifor`参数，这可以通过LS-run的功能完成。

29. `*DATABASE_FSI`

30. 当拉格朗日网格与欧拉或ALE网格重叠时，流体-结构（或ALE-拉格朗日）耦合作用通常使用`*CONSTRAINED_AGRANGE_IN_SOLID`或`*ALE_STRUCTURED_FSI`进行建模。`*DATABASE_FSI`导致将与上述2个关键字中定义的选定拉格朗日曲面上的通量和负载相关的某些耦合信息写入基于ASCII的dbfsi文件，或者在MPP-DYNA的情况下写入binout文件。DBFSI_ID就是一个编号，可以不用输入。

31. DYNA中用于模拟气囊展开的方法：控制体积CV法，ALE流固耦合，S-ALE流固耦合，微粒法，CESE流固耦合，SPH法。其中控制体积法使用最广泛，计算速度最快。气囊采用壳单元和纤维材料。

32. ALE算法的主要特点是：有限元网格的任意性，计算网格可随特定物理问题，采用自己独特的运动方式。单元网格不一定用于描述物体的几何形状，而只是用来覆盖物体可能运动的空间。它可以用于计算流体或固体的大变形问题，尤其适合处理高速流体冲击，侵蚀拉格朗日结构等问题，例如爆炸，罐内液体晃动，容器坠落，鸟击，物体入水。

33. ALE采用算子分裂方法处理扩散项和迁移项，一个时间步长内，单元会经历一个常规的拉格朗日时间步和一个额外的输运时间步。

34. 在通常的拉格朗日算法中，一个时间步包含如下3个动作：

    1. 更新速度和位移。

    2. 在变形后得到新的单元应变率，进而得到新的单元应力。

    3. 由节点的内力，外力及质量计算出新时间步的加速度。

35. 输运时间步的作用是将变形后网格中个单元的应力应变和其他历史变量映射到ALE网格的单元中。输运过程发生在上述拉格朗日时间步的（2）和（3）之间。包括以下2个步骤：

    1. ALE网格运动，在此之前，单元网格已随该时间步物质点的运动而运动。此时的网格位置与当前时间步开始时的网格位置的差值，就是此时间步的位移。根据不同的问题，选择不同的网格运动方式：如果将网格移回当前时间步开始时的网格位置，就是欧拉网格；如果完全不做网格运动，就是拉格朗日网格。`*ALE_REFERENCE_SYSTEM_GROUP`中的PTYPE=8可以作为一个ALE网格运动的粒子。参数EFAC控制网格欧拉类型的比例，新节点位置=欧拉网格节点的位置\*EFAC+\*拉格朗日节点位置（1-EFAC）。

    2. 输运过程（advection，mapping）又称为映射过程，实际上是一个加权平均过程，权函数是体积。对于单元变量，首先计算出各个单元表面的流入/流出体积。然后利用如下公式求出输运后单元变量的新值：新值=（旧值\*单元旧体积+各面流入或流出体积\*流入或流出值）/（单元旧体积+各面流入或流出体积）。

36. 对于单元变量的值的选取，假设该值在单元内为常数，则输运过程就是一阶，如果假设他是线性变化的，则输运过程就是二阶。

37. 节点变量的处理稍微复杂，DYNA采用了Half Index Shift的处理方法，每个单元的8个节点变量都要被逐个放置于单元中心，当作单元变量处理，以防止输运过程中产生过多的认为扩散。

38. 输运时间步是指ALE变形后后的输运过程，这个过程使得ALE网格脱离了物质点的运动而独立存在，也带了处理复杂度和人为误差。

39. ALE单元本身只是一个积分域的描述，并不包含任何物质界面信息，DYNA的ALE使用界面重构法来构造不同流体间的物质界面，从而使同一网格内可以进行多流体计算，ALE多物质单元支持多流体计算，设置如下：

    1. 一维模型，在*SECTION_ALE1D中设置ALEFORM=11
    2. 二维模型，在*SECTION_ALE1D中设置ALEFORM=11
    3. 三维模型，在*SECTION_SOLID中设置ELFORM=11

40. 在ALE多物质单元中，可在有限元网格划分时用单元网格描述物质的初始几何形状，也可以由`*INITIAL_VOLUME_FRACTION_GEOMETRY`（填充part或part set，推荐使用）或`*INITIAL_VOLUME_FRACTION`（填充单个单元，不推荐使用）定义每种物质的体积占比，即它占据单元体积的比例。界面重构采用体积占比重构物质界面。为了简化计算，ALE界面重构有以下几个假设：

    1. 单元中的物质界面是一个平面，物质界面在单元间不连续，物质界面的形状随每次输运而变化。注意，这也是造成流固耦合中泄露leakage的根源之一。

    2. 单元中物质界面的数量=物质种类数量-1。

    3. 单元中物质的排列顺序与*ALE_MULTI-MATERIAL_GROUP中的顺序一致。

    4. 物质在它处于的物质界面中均匀分布，即界面重构过程中，原单元中的某种物质和新流入的同种物质被同一化，也就是均匀混合。

41. ALE多物质单元有\*ALE_MULTI-MATERIAL_GROUP定义。\*ALE_MULTI-MATERIAL_GROUP的每一行分别为一个Part ID或Part Set ID定义一种物质。而Part由\*Part定义，与网格无关。

42. 使用多物质ALE单元建模时，单元网格并不一定描述物体的几何形状，而只是用来覆盖物体可能运动的空间。物体的几何描述可根据体积占比经由物质界面重构而实现。这正是ALE问题的边界条件施加的特点。

43. 边界分为2类：

    1. 应力边界，也称为自然边界条件，ALE网格边界处一般只能施加零压力或环境压力ambient pressure。这是因为ALE边界并非物质边界，物质并没有在这里截断（施加位移边界时除外）。大部分问题中，边界一般被一个大气压力的空气或零应力的`*MAT_VACCUM`所占据。零压力边界，与拉格朗日边界问题相同，无须特殊处理。环境压力的值由`*CONTROL_ALE`的PREF设定。考虑重力时，还需要设置`*ALE_AMBIENT_HYDROSTATIC`和`*INITIAL_HYDROSTATIC_ALE`。

    2. 位移边界，也称为本质边界条件，包含：
       1. 固定边界，边界上一点的所有方向均固定，与拉格朗日问题相同，可使用`*BOUNDARY_SPC`指定。

       2. 对称边界，在某一全局方向上，边界上点的位移为零，设置方法同上。

       3. 滑移边界，法相方向移动受限，切线方向可以自由滑动。这是ALE独有的，使用`*ALE_ESSENTIAL_BOUNDARY`定义。通常在管道流动时，ALE网格的边界就是管道的内壁，液体在管道内流动时，摩擦力微弱，可以忽略不计。它类似于一个简化的流固耦合问题，此耦合中，固体要么被固定，要么质量和刚度足够大，使得固体本身的变形和移动可以忽略不计，流体携带的动量在耦合过程中没有损失。在R6之前，滑移边界由`*CONTROL_ALE`中的EBC=2指定，但是原有算法只对非常简单的边界形状有效。对于稍复杂的边界就会失效。旧算法对于角点corner和边缘点edge的处理也是错误的。新算法可以正确处理这些，还考虑针对输运时间步的速度修正，从而保证动量和冲量守恒。

       4. 流入流出是ALE特有的边界条件。通常需要同时设置速度边界条件和流入/流出液体的材料性质。后者的设定可以参考`*BOUNDARY_AMBIENT_EOS`和`*SECTION_SOLID(AMBIENT=4)`。在设置速度时，必须注意对环境ambient单元的所有点都施加速度，这样才可以保证环境单元无变形，从而确保单元应力即其他单元变量不变。

44. DYNA为处理流固耦合提供了ALE-FSI方法，此时流体通常采用ALE多物质单元重构流体物质界面，固体使用通常的拉格朗日单元。流体采用欧拉方法，固体采用拉格朗日方法。同一空间位置流体和固体结构网格可以同时存在，相互重叠。在流体和固体物质界面间，信息交换的方法有两种，和接触算法类似：

    1. 约束法：在物质界面处，在遵循动量守恒的前提下，人为改变流体和固体的速度，使之一致。

    2. 罚函数法：在物质界面处，流体和固体之间添加无质量的弹簧，用惩罚力去纠正流体和固体运动间的不协调。

45. DYNA的ALE流固耦合一般采用罚函数法，因为约束法无法处理流体和固体的分离。处理瞬态问题时，约束法会导致较大的能量损失。约束法必须和所有流体耦合，而罚函数法可只耦合与某一种特殊流体。

46. 罚函数法分为三步：

    1. 确定固体物质界面。首先将固体表面网格构成一个segment set，然后在每个面段上生成N*N个结构耦合点。固体物质界面就由这些耦合点代表。
    2. 确定伪流体（pseudo）物质界面。在固体的每个耦合点处判断，这个耦合点是否已经接触到流体物质表面。如果已经解除，在欧拉网格中于此固体耦合点同一位置处标注流体耦合点，伪流体物质界面由这些流体耦合点组成。
    3. 施加惩罚力。在每一对结构和流体耦合点间施加一个无质量弹簧。接下来结构耦合点和流体耦合点分别跟随固体和流体运动，它们之间的相对位移会产生弹簧力，以此施加惩罚力。

47. 传统ALE方法支持的流固耦合关键字有：

    ```
    *CONSTRAINED_LANGRANGE_IN_SOLID
    *ALE_COUPLING_NODAL_CONSTRAINT
    *ALE_COUPLING_NODAL_DRAG
    *ALE_COUPLING_NODAL_PENALTY
    *ALE_COUPLING_RIGID_BODY
    *ALE_FSI_PROJECTION
    ```


# S-ALE

1. 2015年，陈皓将结构化ALE（S-ALE）加入DYNA，目前正在将AUTODYN的FCT算法引入DYNA的S-ALE中，以提高计算精度。

2. DYNA中的ALE模型大多采用规则的立方体正交网格，也成为IJK网格，可以利用这一特点，来降低算法复杂度，减少计算时间，降低内存需求。

3. DYNA原有的ALE算法开发之初是为了解决固体大变形问题的，这类问题中，网格随物质边界变形而移动，而固体也只是用单个材料单元来模拟。虽然后来又扩展了原程序来支持多物质材料和网格运动。但是算法和逻辑远非最优，例如难以解决流固耦合的泄露问题。

4. 最近，ALE模型的单元数量增长很快，输入文件极为庞大，修改编辑关键字输入文件耗时很长。而对于规则网格来说，完全可以根据用户提供的简单几何信息，由程序本身去创建网格，从而省去用户创建网格和程序读入的麻烦，同时也节省了大量读写操作带来的时间消耗。

5. S-ALE求解器和原有ALE求解器的理论完全相同，采用相同的输运和界面重构算法，但是具有以下优点：

   1. 网格生成简单，S-ALE可以在内部自动生成ALE正交网格，K文件简洁容易维护，I/O时间更少。
   2. 计算时间缩短20-40%。
   3. 并行效率高，S-ALE适合处理大规模ALE模型，目前由SMP，MPP，HYBRID。借助于MPP算法的全新设计，MPP的可扩展性得到极大提高，运行在400核上的大型算例，可以得到0.9的加速比。S-ALE成功实现SMP并行及结果一致性，而原有ALE求解器无法实现SMP并行计算。
   4. 求解稳健，在流固耦合的泄露方面改进很大。控制参数大大减少。
   5. 减少了PrePost使用的内存。

6. S-ALE可以生成多块网格，每块网格独立求解。不同网格可占据相同的空间区域。

7. 定义了两种part：

   1. 网格part，由一系列单元和节点组成，没有材料信息，也不包括单元算法，仅仅是一个网格part。由`*ALE_STRUCTURED_MESH`的DPID定义，用户只需给出一个未使用过的Part ID即可，不用为他设置*Part卡片，S-ALE会自动定义该这个part并指明其为S-ALE网格part。在所有的ALE相关的关键字中，PID指的是Part ID，仅引用其中的网格，而非材料。
   1. 材料part，与网格part相反，不包含任何网格信息。S-ALE网格中流动的多物质材料与材料part一一对应，可以有多个卡片，每个卡片定义了一种多物质材料（`*MAT`+`*EOS`+`*HOURGLASS`）。其ID仅出现在`*ALE_MULTI-MATERIAL_GROUP`中，其他任何对该ID的引用都是错误的。

8. 定义S-ALE时，用户需要指定3个方向的网格间距。通过一个节点定义网格源节点，可用于指定网格平动，另外3个节点定义局部坐标系，可用于指定网格旋转。

9. 步骤如下：

   1. 生成S-ALE网格和网格part
      1. 设置1-3条`*ALE_STRUCTURED_MESH_CONTROL_POINTS`关键字，给出3个局部坐标方向网格集合。

      2. 采用`*ALE_STRUCTURED_MESH`关键字生成网格。

   2. 定义S-ALE多物质，及定义S-ALE网格中的材料
      1. 采用`*PART`定义材料part，对于每一种ALE材料，定义一个part，该part将`*SECTION`，`*MAT`，`*EOS`，`HOURGLASS`等组合在一起，由此形成Part。

      2. 采用`*ALE_MULTI-MATERIAL_GROUP`关键字定义ALE多物质。

   3. 定义各ALE多物质材料的初始体积占比。初始阶段在S-ALE网格part中填充多物质材料，这通过`*INITIAL_VOLUME_FRACTION_GEOMETRY`（其中part ID为网格Part）或`*ALE_STRUCTURED_MESH_VOLUME_FILLING`（其中part ID为S-ALE网格ID）。程序内部通过界面重构算法来构建物质界面。

   4. 其他设置
      1. 通过`*CONTROL_ALE`设置物质输运算法：Donor cell（一阶）或Van Leer（二阶）。设置AFAC=-1可以关闭ALE光滑。

      2. 采用`*INITIAL_DETONATION`设置起爆点，注意PID必须是网格Part ID。

   5. 设置边界条件
      1. 采用`*BOUNDARY_SPC`设置固定或对称边界条件
      2. 采用`*BOUNDARY_PRESCRIBED_MOTION`施加速度边界条件
      3. 采用`*LOAD_SEGMENT`施加压力边界条件，正值表示和segment的法线相反。
   6. 流固耦合设置
      1. 推荐采用`*ALE_STRUCTURED_FSI`。
      2. 也可以采用`*CONSTRAINED_Lagrange_IN_SOLID`。除了唯一的对MCOUP参数的小改动外，使用方法与原有ALE基本相同。在原有的ALE中，MCOUP=0表示结构与所有流体耦合；MCOUP=1表示结构与密度最大的流体耦合；MCOUP=-N表示与由ID=N的`*SET_MULTI-MATERIAL_GROUP_LIST`中列出的一个或几个流体耦合。现在，为了避免额外的`*SET_MULTI-MATERIAL_GROUP_LIST`关键字，这里规定，当MCOUP=-N并且N≠1时，N代表一个Part Set，这样就可以将要耦合的AMMG用他们的材料Part代替了。

10. S-ALE支持SMP，MPP和HYBRID并行计算。原有的ALE求解器在并行计算方面存在严重的缺陷，无法实现SMP并行计算。MPP虽然能实现，但是并行效率低。S-ALE在设计时就考虑这些问题，所有算法和实现都采用了对并行计算最优的选择，S-ALE成功实现了SMP并行，加速比很高，实现了计算结果的一致性。在MPP方面，重新设计了MPP通信模式，使得S-ALE相比原有ALE运行速度提高很多，可扩展性也很优异。

11. SMP并行计算，参与计算的多个核共享同一内存空间，也就是说内存的地址对于每个核是一致的，都可以直接读写。运行的机器可以看作多核的一台独立的机器，也可以是插在同一块主板上的多个CPU，这在服务器领域比较常见，他们共享主板上的内存。

12. DYNA的SMP一般使用OPENMP指令实现。它是由开发者至于一段程序之前的指令，这个指令通知编译器，这段程序的数据之间没有相关性，可以被并行执行。一般是循环或独立的子程序。提高加速比的关键在于将尽可能多的循环或子程序SMP化，尽量减少串行编码的比例。

13. ALE求解器本身非常耗时，这是因为额外的输运时间步包括非常多的计算量，这些计算大多每次都牵涉到同时进行2个单元的操作。这样每个单元的数据处理必须依靠它相邻的6个单元，数据处理不能以单元为单位，像拉格朗日单元处理那样独立进行。正是因为这些困难，原有的ALE求解器才没有将输运过程SMP化，尽管它耗时最多。

14. 新的S-ALE求解器在实现时考虑了SMP化的需求，改变了输运过程的计算方法，实现了输运过程的SMP化。保证了计算结果的一致性，也就是说计算结果和使用多少核心无关。

15. SMP使用命令如下：

    ```shell
    LSDYNA i=main.k ncpu=-4 jobid=smp4 #其中-4表示使用4个cpu并需要保证结果一致。S-ALE只支持结果一致选项，即ncpu=-4而非ncpu=4。使用后者不会在S-ALE求解器中带来任何加速。
    ```

16. MPP和SMP完全不同，SMP试图尽可能地把大部分的程序并行化，这一过程中必定有一些程序只能串行执行，但往往是这些只能顺序执行的部分严重阻碍并行效率的提高，这就是amdahl定律。

17. MPP的思路是将整个问题分解为多个块，分别放置在多个CPU上运行。这样程序本身做到了100%的并行。理论上并行效率可达到1，但是实际中，由于MPP的数据传输交换，并行效率可能远低于此。MPP分解到每个CPU上的子问题通常都不能作为独立问题求解，这些子问题间都是有着互相联系的，这些联系体现在算法上，就需要在各个子问题所在的CPU间进行数据传输。任意两个CPU间数据传输的大小由这两个CPU所含子问题的共有区域决定。例如拉格朗日问题中一个固体part被分在两个CPU上分别求解，那么在每个时间步长内，他们共有的节点量如速度，加速度，坐标就需要在这两个CPU间传输。

18. 原有的ALE和S-ALE求解器在传输数据的量上是一样的，但是S-ALE在实现时，对计算方法和步骤做了精心的设计，试图将数据传输尽可能地集中，以减少传输次数和等待时间，从而使得S-ALE的MPP并行效率和扩展性大为提高。

19. 对于大规模ALE问题，需要的ALE单元数量庞大，这样在MPP执行的初始阶段分解问题时，CPU0读入模型并创建数据库存储，它对内存的需求往往特别高。这也是MPP对内存要求最高的时候。随后大的完整模型被拆分为多个单独的小模型，并写成多个独立的输入文件，最后其他CPU再分别读入各自的输入文件，此时内存需求会大大减少。陈皓重构了S-ALE的初始化阶段，S-ALE网格只在初始化的最后阶段才产生，每个CPU只拥有各自的小模型，使内存需求大大减少。

20. MPP的命令如下：

    ```shell
    mpirun -np=4 mppDYNA i=main.k jobid=mpp4 #其中-np=4指明使用4个CPU。
    ```

21. 注意，由于问题被分解，截断误差使得不同数量的CPU的MPP计算结果无法保持一致。

22. HYBRID时MPP和SMP的简单叠加，本身在实现上没有难度，体现是一种计算思想上的进步。对同一工程问题的不断细分，在每个CPU上的单元数越来越少，但是需要进行数据交换的节点越来越多，因此达到一定数量的CPU以后，MPP的加速比将不再增大，甚至有可能变低。

23. 当MPP接近饱和时，可以引入SMP，因为增加SMP线程的个数并不会增加MPP中交换的数据量。即使SMP的加速效率通常不如MPP，但是在MPP饱和的情况下，SMP就成了唯一的选择了。

24. S-ALE既支持MPP，又支持SMP，因此不同任何特殊处理，S-ALE就可以使用HYBRID。而旧的ALE求解器不支持SMP，因此不能使用HYBRID。

25. HYBRID的命令如下：

    ```shell
    mpirun -np=4 mppDYNA ncpu=-2 i=main.k jobid=mpp4s2 #指定使用4个MPP进程，每个MPP进程上运行2个SMP线程。
    ```

26. SMP的引入并不会导致结果不一致，因此HYBRID和MPP一样。

27. 运行HYBRID时，需要注意CPU绑定。这一绑定配置文件随系统而异。例如存在一个48核心的MPP机器，包含4个RANK，每个RANK有12个核心。运行时会希望同一个MPP进程的几个SMP线程尽可能分配在同一个RANK的核心上，否则运行效率会降低。

28. S-ALE有多个新增的关键字，均以`*ALE-STRUCTURED`开头：

    ```shell
    *ALE-STRUCTURED_FSI 
    *ALE-STRUCTURED_MESH
    *ALE-STRUCTURED_MESH_CONTROL_POINTS
    *ALE-STRUCTURED_MESH_MOTION #在模拟过程中控制网格运动
    *ALE-STRUCTURED_MESH_REFINE #将ALE-STRUCTURED_MESH定义的结构网格进行细化，每个方向指定一个整数倍数。
    *ALE-STRUCTURED_MESH_TRIM #修剪/取消修剪生成的网格
    *ALE-STRUCTURED_MESH_VOLUME_FILLING
    ```

29. `*ALE-STRUCTURED_MESH_CONTROL_POINTS`是用来定义控制点序列的，`*ALE-STRUCTURED_MESH`通过引用这些控制点序列来生成结构网格，在它的CPIDX等中选择对应的控制点序列即可，相当于3个序列的笛卡尔积。控制点的格式如下：

    ```shell
    N     X     RATIO
    1    0.4     0    #注意，第一个控制点的编号必须是1
    6    0.5     0    #至少有2行
    28   0.72    0
    40   0.78    0
    62   1.0     0
    67   1.1     0    #最后一个控制点的编号定义了节点的总数。
    #第一列控制点编号，第二列为坐标，第三列控制网格尺寸在控制点之间是如何变化。
    #6个控制点，可以构成5段，每段的端点就是控制点的坐标值。例如第一段有5小段，长度为0.5-0.4=0.1
    ```

30. S-ALE网格默认不显示，需要在左侧模型树中点击ALE→Structured Mesh才可以。

31. 除了这两个关键字外，还需要额外定义一个空的part用于存放S-ALE网格（仅指定Part ID不行），这个Part的ID会在`*ALE-STRUCTURED_MESH`的DPID中引用。该Part的定义中，只需要给定ID，其余的选项都是零即可，因为这里的part仅指网格，而非材料。因为用户定义的MATID不可能为0，因此Part中引用编号为0的MAT表示不使用任何材料。此part定义在输入阶段自动生成，既不包含材料也不包含单元公式信息。之所以有这个规定，是为了满足遗留规则，即每个单元都必须与一个part相关联。此ID还用作网格合并的指示器，即如果将相同的Part ID用于多个相邻的自动生成的网格，则它们将合并在一起，形成由这些子网格组成的单个网格。

32. 通过结构化网格，单元和节点的连接变得简单，用于ALE耦合的搜索算法也大大简化。避免了许多检查，因为这些网格只包含六面体单元。因此当ALE网格是结构化时，推荐使用S-ALE求解器。

33. 一旦使用`*ALE_STRUCTURED_mesh`生成ALE网格，就会调用S-ALE求解器并执行ALE对流时间步长。对于流固耦合，建议使用`*ALE_STRUCTURED_FSI`而不是`*CONSTRAINED_Lagrange_IN_SOLID`，因为前者具有更好的自动泄漏检测和控制功能，输入更清晰、更容易，专为S-ALE求解器设计。

34. `*ALE_STRUCTURED_mesh`关键字可以多次使用。每次都会构建一个独立的网格。这些网格可以占据不同或相同的空间域，模拟在这些网格中独立执行。


# SPH

1. SPH的Part和结构接触时，需要使用Node to Surface。

2. SPH问题需要设置`*CONTROL_SPH`，指明问题的维度，即IDIM参数。
3. 可以生成的实体的壳单元表面，然后使用SPH Generation来生成SPH粒子。输入材料的密度（这样才会给每个粒子分配质量），点击Set Params，还有每个方向的粒子数量，然后点击Create。然后就可以删除掉壳单元的表面了，分析的时候使用生成的sphnode的Part。

4. 可以使用菜单栏→Settings→General Settings→SPH/Particle来改变SPH的显示样式。
