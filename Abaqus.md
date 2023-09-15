# 基础

1. 2005年ABAQUS被法国达索公司收购，公司更名为SIMULA。

2. 接触和摩擦可以看做是非线性约束。

3. ABAQUS/CAE是Complete ABAQUS Environment的缩写。CAE不包含分析模块。

4. ABAQUS有两个主要分析模块，分别为standard（通用分析）和explicit（专门用于显式分析的）。

5. 隐式方法需要同时求解一个方程组或计算刚度矩阵。显示方法则不需要。

6. 应力波的传播例子：应力波沿着一个由3个杆单元构成的杆件模型传播，初始时刻三个杆一样长。 

7. ![image-20200615184541253](Abaqus.assets/image-20200615184541253.png)

8. 在第一个时间增量段内，P使得1节点产生了一个加速度，然后经过第一个时间段，速度，速度对应于应变率。应变率对时间积分得到单元的应变增量。总应变=初始应变+应变增量。这个时间段各单元的的初始应变为0。总应变*弹性模量得到总应力。在第一个时间增量段内，节点2和3不受力，没有移动。

9. ![image-20200615184603600](Abaqus.assets/image-20200615184603600.png)

10. 每个时间增量段的开始都会将上一个时间增量段的单元内力施加到与之直接相连的节点上。因此在第2个时间增量段内，节点1和2都收到了单元的对抗压缩的内力。此时单元1有初始应变，单元2没有。

11. ![image-20200615184940375](Abaqus.assets/image-20200615184940375.png)

12. 可以看到当第3个时间增量段开始时，单元1和2都有了内力，也都传递到了节点1 2 3。

13. ![image-20200615185227581](Abaqus.assets/image-20200615185227581.png)

14. 单元和节点的集合成为网格mesh。网格只是实际结构几何形状的近似表达。

15. 如果静态分析中出现numerical singularity数值奇异或zero pivot主元素为0的错误，一般情况下是缺少了限制刚体位移的约束。

16. ABAQUS使用canvas画布来摆放多个viewport。

17. 除非在interaction模块中指定接触，否则ABAQUS不会自动识别instance之间的力学接触关系。

18. 载荷和边界条件和step分析步有关，用户可以指定他们在哪些step起作用。

19. ABAQUS包含CAE模组，CAD交互接口，后处理接口。

20. ABAQUS的分析模组有3个：
    1. ABAQUS/Standard，通用的有限元模组，也可以做动力分析，使用隐式求解方法。
    2. ABAQUS/Explicit，动力分析首选，使用显式求解方法。也可以求解拟静态问题。
    3. ABAQUS/CFD。
    
21. Standard和Explicit是求解方法不同，不同的求解方法适用于不同的问题形式。

22. ABAQUS/CAE是将所有的模组整合成一个GUI环境。

23. ![image-20200615101623389](Abaqus.assets/image-20200615101623389.png)

24. Standard可以做：静力分析，线性动力学（模态分析，谱分析），非线性动力学（瞬态的）。也可以做热，声学分析。

25. .cae是模型数据库文件，.odb是求解结果数据库文件。一个.cae档可以存放数个model。一个model中可以有多个part，每个model中只能有一个assembly，只有在assembly中的物体才会被最终计算分析。

26. .inp文件是求解输入文件，用来输入到求解器的，类似于ls-dyna的k文件。.odb文件是结果输出文件，output database。.dat文件是结果打印列表，对求解过程进行记录。

27. 重启动数据用于继续分析过程，输出在.res文件中。

28. 一个part需要被实例化为part instance才可以组装为assembly。

29. ABAQUS静力分析的时间不具有真实的意义，而只是用来划分不同的step。一个step可以划分为多个substep。动态问题中，时间是具有真实物理意义的。

30. ABAQUS官方一共给出了三个实例系列：

    1. Abaqus Example Problems Guide
    2. Abaqus Benchmarks Guide     包含了NAFEMS规定的一些例子。
    3. Abaqus Verification Guide

31. ABAQUS官方给的例子中，包含了一系列的inp文件，使用方法：

    ```
    abaqus fetch job=xxx.inp
    ```

32. 如果不加扩展名，则会提取出符合名称的所有后缀文件。


# 建模技巧

1. 创建part时，需要输入approximate size，这个参数原则上和最终part中最大尺寸在一个数量级即可。
2. ABAQUS并不是用特殊的单位，用户只要使用一致的量纲系统即可。
3. 相比于ansys建模时，abaqus不用构建多种坐标系。但也有类似于工作平面的概念，即sketch。part中的三维实体必须是通过二维的面拉伸，旋转。复杂的三维实体建议从CAD软件中导入，ACIS格式的.sat文件和ABAQUS最搭配，因为ABAQUS底层也是使用的这种格式。
4. 材料的方向对于实体单元默认使用全域直角坐标，而shell单元，则是采用在全域直角坐标在参考面上的投影，随着面的法向方向变化。
5. 每个自由度都用数字来表示，123分别表示xyz方向的线位移。456分别表示绕xyz轴旋转。其他的自由度例如温度用11来表示。
6. part包括4种：可变形体，离散刚体（可以使复杂的外形），解析刚体（只能用简单的外形，一般用来定义刚性面），欧拉零件（用于欧拉分析，网格不动，材料在网格内流动）。两种刚体受力都不变形。解析刚体比离散缸体计算效率更高。
7. part的外形可以由一下三种方式定义：
   1. 直接在CAE模组中建立，称为==native geometry==
   2. 从其他CAD系统中导入，分为==原生格式==（proE或CATIA等默认的格式）和==中立格式==（通用的文件交换格式例如.sat）
   3. 导入的单独的网格，==orphan mesh==不含几何部分。这可以同.inp，.odb，.cdb（ANSYS）等文件中导入。
8. 汇入的part都会有一个feature，表示他是哪种格式导入的，例如：
9. ![image-20200614215804301](Abaqus.assets/image-20200614215804301.png)
10. 如果是在CAE模组中建立的part，就会保留许多建立时候的feature，可以进行修改。ABAQUS很少有撤回的动作，都是使用feature来记录操作。删除feature就可以撤销操作。
11. feature就是操作，可以是对part，datum，partition，assembly等的。
12. 2D底稿sketch推荐使用AutoCAD的.dxf格式或.iges格式来导入。
13. 如果导入3Dpart，建议使用ACIS的.sat和STEP的.step格式。不建议使用.iges格式。
14. ACIS的.sat格式是ABAQUS核心使用的方式，是最可靠的导入格式。.step格式是替代.iges格式的。
15. 独立网格（也成为孤儿网格，只有网格，没有几何）支持的格式：
    1. Abaqus input (.inp) file
    2. Abaqus output database (.odb) file
    3. Nastran bulk data (.bdf) file
    4. Ansys input (.cdb) file
    5. STL file (via plug-in)

16. ABAQUS可以为part建立基准Datum点线面参考系（分析时不会考虑）。可以利用基准平面来创建任意方向的part。同时基准几何还可以用来在assembly时进行==定位==。
17. ABAQUS支持多种选择模式，可以规定只选择某种类型的元素。也可以指定选择选择框内或外的元素。使用Shift加选，Ctrl减选。
18. partition一般是用来分隔part，进而给同一个part的不同区域分配不同的材料，截面等参数。也可以是为了提高mesh质量而界定边界。在partition的边界处一定会有节点。

# 材料

1. ABAQUS支持工程应变和对数应变两种模式。
2. 工程（名义）应变NE：$\varepsilon_{nom}=\Delta l/l_0$，真实ln（对数）应变LE   $\varepsilon=\textrm{ln}(l/l_0)$。其中$\Delta l=l-l_0$。输出变量E通常对应的是对数应变LE。实验中只能直接得到工程应力和应变数据。
3. ==对数应变和工程应变==的转换关系为：$\varepsilon=\textrm{ln}(1+\varepsilon_{nom})$。
4. 对于非弹性材料，总对数应变=弹性应变+塑性应变+徐变应变。$\varepsilon=\varepsilon^{el}+\varepsilon^{pl}+\varepsilon^{cr}$。
5. 应力也分为工程应力$\sigma_{nom}=F/A$和真实应力$\sigma=F/A$。真实应力和真实应变之间才满足胡克定律。
6. ==对数应力和工程应力==的转换关系如下：$\sigma=\sigma_{nom}(1+\varepsilon_{nom})$。
7. 塑性材料采用真实应力和真实应变。当从实验数据导入ABAQUS时，如果指定是工程应力应变，则会ABAQUS会做转化。
8. 真实塑性应变$\varepsilon^{pl}=\varepsilon-\varepsilon^{el}=\varepsilon-\sigma/E$。
9. 超弹性材料采用工程应力应变。
10. ABAQUS中任意输入的应力和应变都默认是真实应力应变。
11. 如果材料性质和温度有关，则在温度范围内内插，范围外为恒定值，等于边界值。一般来说温度越高，弹性模量会降低，泊松比会升高。
12. 应力应变的输出和材料方向有关。如果想要输出第二种图形，则要建立局部坐标系。
13. ![image-20200614230943958](Abaqus.assets/image-20200614230943958.png)
14. 对于薄膜单元，1方向是全域X轴在参考面上的投影。还有一个面的法线方向（按照顶点顺序，右手定则）作为3方向。2方向由1和3方向确定。
15. ![image-20200614231049674](Abaqus.assets/image-20200614231049674.png)
16. 在几何非线性分析中，梁，薄膜等单元的预设方向会随着元素的运动而运动。实体单元的方向则不会，始终和全域坐标系一致。
17. 对于非各项同性材料，需要使用局部材料方向来定义性质。
18. 线弹性材料也可以是各向同性，正交各相异性的和各向异性。
19. 胡克定律的一般形式：$\sigma=D^{el}:\varepsilon^{el}$。Cauchy应力=弹性张量*弹性真实应变张量。
20. 定义塑性材料需要先定义个弹性行为。塑性应力应变都要使用真实的。例如：
21. ![image-20200614232730999](Abaqus.assets/image-20200614232730999.png)
22. 第一行为屈服应力和0塑性应变。
23. ![image-20200614232836745](Abaqus.assets/image-20200614232836745.png)
24. 以上是定义Mises塑性的步骤。Hill塑性需要使用potential选项。
25. ABAQUS可以建立材料资料库.lib文件，来共享材料数据，存储位置可以选择home（C:/user/xxx/abaqus_plugin目录下）和当前工作目录下的abaqus_plugin文件夹。
26. 存放在home目录下，所有的cae工程都可以使用，如果存在当前目录下，则只有该cae工程可以使用。
27. ![image-20201026152232425](Abaqus.assets/image-20201026152232425.png)
28. ABAQUS对于3D的结构也是用截面来定义材料，选择均质homogeneous即可。壳单元截面包含材料和积分选项，梁单元截面包含截面形状和材料。
29. 梁和壳都需要会提示选择截面积分的方法，对于线性分析，分析前就可以。非线性的话应选择分析中。
30. 同一种材料可以用于不同的section，例如壳和实体都可以用steel材料。将section指定给part（或者part中的单元构成的set region）之后，对应的part就有了材料和尺寸的定义。
31. 没有指定section的part会显示为白色，指定了1个section的为绿色，多个的为黄色。
32. 想要显示壳单元的厚度和梁单元的截面，则需要在view→对应的display option中勾选下面的选项。
33. ![image-20201026154608506](Abaqus.assets/image-20201026154608506.png)
34. 壳和梁都是3D单元，创建part时应选择3D。因为他们都有3个方向的位移。
35. 有限元求解的全部内容都在assembly中。每一个model只包含一个assembly。一个assembly可以包含part的实例instance，也可以包含其他model的assembly。同一个part的所有instance具有相同的section。
36. 有两种实例类型：①独立的，mesh是在instance上的，和part无关，每个instance需要单独划分网格②非独立的，mesh在part上，只需对part划分一次，之后的所有instance都一样。
37. 使用组装的好处是，可以修改part中的模型，进而==自动==修改assembly中的模型。
38. 组装时定位的方式有两种，①平移和旋转②使用constraint来对点线面约束。使用constraint时，可能会产生冲突。注意设定好那些instance是可以动的，那些是不动的。
39. set==集合==用来保存一组选择，可以包含点vertex线面，节点node或单元面。一般用来设定荷载和边界条件，或者定制输出变量。
40. ![image-20201026184547481](Abaqus.assets/image-20201026184547481.png)
41. surfaces==面集合==由几何面face和单元的面组成，是用来定义接触（接触是根据面来判断的，接受surface，而不是set）和施加分布载荷的。
42. ![image-20201026184556207](Abaqus.assets/image-20201026184556207.png)
43. 多选多个set或surfaces，可以进行bool运算。
44. set或者surface中不能既有几何，又有单元。
45. 删除set或surfaces并不会删除真实的几何或单元。
46. 如果在part下建立的set，在assembly中也会看到，会重命名，反之不会。例如在名为trussrod的part中建立名为Set-1的set，那么assembly中存在一个trussrod-3这样的instance，则对应的set名字为trussrod-3.Set-1。 
47. 也可以在assembly中定义set或surface。
48. 显示群组可以用来观察结构的内部，也可以用来进行施加载荷时方便选取，而不用建立set等。
49. ![image-20201026190047643](Abaqus.assets/image-20201026190047643.png)
50. 未进行partition前，一个part由一个cell组成。对于非独立的instance，不能在assembly上进行partition，只能在对应的part上进行。对part切割之后，对应的instance都会变化。

# 分析步

1. step是对时间上进行分割，这样做的目的是为载荷和边界条件的变化提供方便。在step之间可以改变输出量。一个step可以理解为一个工况。每创建一个分析步，都会创建一个分析步的输出要求，包含写入到结果数据库文件中的变量。
2. ABAQUS会自动生成初始步，initial载荷步无法设置load，但是可以设置BC。所有指定在初始步的边界条件都必须赋值为0，这事ABAQUS的要求。
3. 每一个step能够进行的分析类型是独立的。后一个step是在前一个step的基础上进行的。
4. <img src="Abaqus.assets/image-20200615211327823.png" alt="image-20200615211327823" style="zoom:67%;" />
5. 每一个step包含一个分析程序。分为两大类：①一般的，静态，动态，显式隐式分析②线性摄动，最常见的是特征值问题，模态分析，反应谱问题，==不会累加到时间中==。
6. 在Explicit中，只能使用一般分析步。
7. 多个step，每个step都独立计时。
8. ![image-20200615212036783](Abaqus.assets/image-20200615212036783.png)
9. 如果想要替换某个分析步，最好的方法是replace，而不是删除在新增。因为荷载，输出设置都是和step绑定在一起的。replace可以完美继承。
10. 也可以suppress某些分析步，这样会直接跳过该分析步。
11. 有两种输出类型：history和field。history会保留每一个frame结束时的结果，field只会保存最终的结果（最后一个step的）。两者的作用不同，field是用来绘制contour的，history是用来绘制X-Y图的。
12. 场变量的输出频率一般较低，历史变量的输出频率可以较高。
13. 预设的history是整个模型的各种能量。
14. 输出的频率设定：①最后一个增量，即仅在每个step的最后一个增量输出一次。②every n increments是每n个增量步输出一次。③evenly spaced time intervals是一个step内输出固定的次数。④每个多少时间输出一次⑤在给定的时间点进行输出。
15. ![image-20200615214248319](Abaqus.assets/image-20200615214248319.png)
16. Explicit中增量步非常多，需要有选择的输出。
17. 预设的位移或速度在BC中设置。
18. (a)为阶跃载荷stepped，在第一个子步就把整个荷载步的变化施加完，后续维持不变，(b)为斜坡载荷ramped。
19. ![image-20200615215420739](Abaqus.assets/image-20200615215420739.png)
20. 阶跃载荷一般用在有时间意义的程序中，例如瞬态分析。斜坡载荷一般用在没有时间意义的程序中，例如静态等。
21. 在瞬态分析中可以定义amplitude来获得任意随时间变化的荷载。
22. 如果荷载分布不是空间均匀的，可以使用analytical field或discrete field来设置。可以用数学表达式，也可以根据指定点的值差值。
23. 一个荷载和边界条件一旦设定，默认在所有的step都生效，可以设定无效和恢复。
24. predefined field是设置初始状态的。初始速度或初应力。
25. 静态分析，初始时间增量一般为step period的1/10。
26. 在field输出中component表示分量，invariant表示不变量，一般用于张量。magnitude表示向量的模。

# 单元

1. ABAQUS的单元可以从以下5个方面进行特征划分：
   1. 单元族，例如实体单元C，壳单元S，梁单元B，桁架单元T，刚体单元R。不同族的单元所假定的几何形状不同。一般反映在单元名称的第一个字母上。
   2. 自由度，和单元族直接相关。结构实体单元只有平动自由度，梁，壳单元还有转动自由度。热传导单元只有一个温度自由度。自由度1-6分别表示方向123的平动和转动自由度。对于轴对称单元，1表示径向平动，2表示轴向平移，3表示绕轴向的转动。
   3. 节点数目与插值的阶数。插值的阶数也成为单元的阶数。每一个方向上的节点数分别为2,3个，则表示分别为一阶和二阶插值。单元的节点数目也会标注在单元的名称中，例如C3D8表示有8个节点。梁单元稍有不同，它标识的为插值阶数，而不是节点数，例如B32表示2阶插值。
   4. 数学描述，ABAQUS的所有应力分析用的单元都是基于拉格朗日描述的，分析中，材料和单元保持关联，材料不能流出单元的边界。而explicit中的自适应网格技术，将纯拉格朗日和欧拉分析的特点结合，允许单元的运动独立于材料。
   5. 积分，在求整个单元体的能量的时候，需要进行积分。大部分单元可以使用高斯积分的方法。根据积分点数的多少，可以分为完全积分和缩减积分。末尾有R的表示使用了缩减积分，例如C3D8R。
2. 除非在节点定义了局部坐标系，否则节点的123方向和整体坐标系平行。
3. 壳单元有三类：
   1. 一般性目的的壳
   2. 仅适合厚壳
   3. 仅适合薄壳 
4. ABAQUS的某些单元除了提供标准的数学公式描述外，还提供了一些可选择的公式。这些单元在名称上一般表现为末尾附加字母。例如杂交公式的单元C3D8H，B31H，将实体单元的静水压力或梁的轴力处理为一个附加的未知量。
5. 还有一些耦合单元，例如C3D8T具有热学和力学的自由度，可以模拟热-力耦合的问题。
6. 
7. Standard提供了一阶和二阶单元可供选择，而对于explicit，除了二次梁单元和修正的四面体和三角形单元来说，只有线性单元可以使用。
8. Standard提供了完全和缩减积分可供选择，而对于explicit，除了修正的四面体和三角形单元来说，只有缩减积分可以使用。
9. 3D实体单元可以是六面体，楔形（如下图），四面体形状的。一阶四面体单元C3D4具有简单的常应变，不推荐使用，因为需要划分非常细的网格。
10. ![image-20210319164725606](Abaqus.assets/image-20210319164725606.png)
11. 二维实体单元根据离面行为的不同，可以划分为三类：①平面应变，PE，假设离面应变为0②平面应力，PS，假设离面应力为0③轴对称单元。
12. 广义平面应变单元是对平面应变单元的推广，即离面应变随着平面的位置发生线性变化。适合厚截面的热应力分析。
13. 二维实体单元都是三维问题的简化，必须在1-2平面内定义。且单元内节点的序号序号满足右手定则，否则面积为负值。
14. 平面应力和平面应变单元可以指定单元的厚度，默认为1。
15. 实体单元如果发生了大转动，它的积分点的坐标系仍然是按照未变化全局坐标系来的，输出可能会不方便。用户可以为单元变量定义一个局部坐标系，该坐标系跟随积分点旋转，方便输出。
16. 
18. 
19. 
20. 
21. 如果受弯构件在厚度方向上，分层少于4层，则不应使用缩减积分。使用incompatible。
22. wedge 楔形体，实际是三棱柱，是六面体的退化得到的。
23. mesh模块根据指定的划分网格的方法来显示不同的==region==。
24. 绿色表示使用结构网格，黄色表示使用扫略，粉色表示使用自由网格，橙色表示划分技术使用不正确。
25. ![image-20200616004354927](Abaqus.assets/image-20200616004354927.png)
26. 一些几何要经过partition成多个cell后才可以进行结构网格划分。
27. ![image-20200616004812087](Abaqus.assets/image-20200616004812087.png)
28. 单元命名规则：C-continuum连续      3D-3Dimension   R-Reduced integration缩减积分    S-Shell 壳   AX-Axisymmetric轴对称    PE-Plane strain平面应变。B-Beam。
29. B21 Beam 2D，1st-order interpolation
30. 制定网格类型也可以在划分网格后。
31. 对于壳体，可以显示section上不同的point，顶部，底部等。如果是多层复合材料，则要选择plies。
32. ![image-20200616011256150](Abaqus.assets/image-20200616011256150.png)
33. 进行显式分析时，要手动选择显式分析的单元。

# Job

1. 只有在job提交后，才会生成对应的job.inp，计算完成后生成job.odb。也可以使用write input来只生成inp文件而不计算。
2. Job内并没有存储模型的内容，因此如果计算失败，然后修改模型，再进行计算时，可以不用新建Job，直接Submit之前的那个Job即可。这样会覆盖掉之前的那个job对应的结果文件。
3. 
4. 
9. 

# 后处理

1. .dat，.msg和.sta文件中的信息会显示在monitor框内。

2. 视区上的legend，title block，status block的显示，字体大小都在Viewport→Viewport Annotation Options中设置。

3. 一般打开odb文件时，默认都是以只读的方式打开，这样能够防止对数据进行错误修改。

4. 如果要同时查看变形和未变形状态，可以先选中 Allow Multiple Plot States，然后再选中变形和未变形的状态。结果如下，白色表示未变形，绿色表示变形后的状态：

6. ![image-20210319141616757](Abaqus.assets/image-20210319141616757.png)

7. <img src="Abaqus.assets/image-20210319141716019.png" alt="image-20210319141716019" style="zoom:50%;" />

8. 在后处理中显示边界条件，View→ODB Display Option→Entity Option

9. 将数据已报告的形式输出到文本文件中，Report→Field Output

10. 在显式分析的后处理中，位移形状缩放因子默认为1。

11. 后处理中创建的XY表格，都是保存在session中，而不是ODB结果文件中，因为该文件一般都是以只读的形式打开的。

12. ![image-20210319151834552](Abaqus.assets/image-20210319151834552.png)

13. 很多值都是在积分点上求解出来的。积分点在node内部。外面的的node是积分点外插出来的。同一个node属于多个element，多个单元的积分点都在该node有一个外插值，可以设置平均算法。

14. 默认的阈值是75%。表示如果最大的和最小值差异比例小于75%，就平均，如果大于该数值则不要平均。0%表示无论差异多大，都不会平均，这样会看到云图有间断。100%表示无论差异多大，都会平均。

15. 差异比例的计算方法：(节点上各个元素外插的最大值-节点上各个元素外插的最小值)/(模型区域内最大值-模型区域内最小值)

16. 默认的模型区域是截面性质相同的区域。还可以选择为elementset或显示群组。

17. ![image-20200616011552372](Abaqus.assets/image-20200616011552372.png)

18. ![image-20200616012007640](Abaqus.assets/image-20200616012007640.png)

19. 使用探针查看单元的数据时，可以在积分点上查看，可以在单元的中心查看，也可以是单元的节点，也可以是单元的面。

20. ![image-20200616014209105](Abaqus.assets/image-20200616014209105.png)

21. 

22. ```
    单元的积分点
    Part Instance  Element ID        Type     Int. Pt.     S, Mises
    ---------------------------------------------------------------------------
        PART-1-1          31       C3D8I            1         12.9
        PART-1-1          31       C3D8I            2         12.7
        PART-1-1          31       C3D8I            3         13.6
        PART-1-1          31       C3D8I            4         13.5
        PART-1-1          31       C3D8I            5         22.8
        PART-1-1          31       C3D8I            6         22.7
        PART-1-1          31       C3D8I            7         23.7
        PART-1-1          31       C3D8I            8         23.6
    单元中心=积分点的平均值。
    Part Instance  Element ID        Type     S, Mises
    ---------------------------------------------------------------------------
        PART-1-1          31       C3D8I         18.2
    单元的节点
    Part Instance  Element ID        Type         Node     S, Mises
    ---------------------------------------------------------------------------
        PART-1-1          31       C3D8I            1         9.48
        PART-1-1          31       C3D8I            2         9.05
        PART-1-1          31       C3D8I            3         10.7
        PART-1-1          31       C3D8I            4         11.2
        PART-1-1          31       C3D8I            5         24.5
        PART-1-1          31       C3D8I            6         24.4
        PART-1-1          31       C3D8I            7         29.4
        PART-1-1          31       C3D8I            8         29.6
    单元的面
      Part Instance  Element ID        Type         Face     S, Mises
    ---------------------------------------------------------------------------
        PART-1-1          31       C3D8I            1         9.59
        PART-1-1          31       C3D8I            2         26.9
        PART-1-1          31       C3D8I            3         17.5
        PART-1-1          31       C3D8I            4         18.1
        PART-1-1          31       C3D8I            5         18.9
        PART-1-1          31       C3D8I            6         18.3
    
    ```

23. Element Nodal表示每个单元的节点，这个是一个一个二级表单的形式展示的，单元共用的节点会出现多次。Unique Nodal只有一级，和单元无关，不会重复。Centroid表示单元的形心，也不会重复。

24. ![image-20210319145101051](Abaqus.assets/image-20210319145101051.png)

25. ABAQUS只会讲用户自己生成X-Ydata存放在当前的session中，下次再打开odb文件就看不见了。因此应该将其存放到odb文件中。右键save as，然后在XY Data Manager中选择Copy to ODB就可以了。但是ABAQUS在打开odb文件时，默认是只读的，不能存储新的东西。应该使用非只读的打开方式。

26. 下次再使用时，可以load 到session中。

27. 绘图产生的各种数据，可以用Report→XY，将内容输出到rpt文件中，方便后续处理。

# 接触

1. constraint约束，模拟点和点之间的运动关系，常用的①tie，一般用来将两个surface或node region粘在一起，用于连接网格不相容的重合面②coupling，将参考节点和面上的节点耦合，分为两种kinematic和distributing。③shell to solid 用于连接壳和实体单元。

2. tie constraint会将两部分永远连接起来，不适合于模型的脆弱部分。

3. 一般将比较硬的部分，位移和变形小的，网格比较粗糙的设置为master。

4. ![image-20200616101155000](Abaqus.assets/image-20200616101155000.png)

5. ![image-20200616101344798](Abaqus.assets/image-20200616101344798.png)

6. 不能给tie constraint的slave节点施加边界条件，方程或MPC，因为它的行为已经被master控制，这样会造成过约束，zero pivot。

7. kinematic是将参考点和所有耦合点之间用刚性梁连接，刚硬。distributing是用平均的方式强化，是一个加权的方式，比较柔和。

8. <img src="Abaqus.assets/image-20200616101859947.png" alt="image-20200616101859947" style="zoom:67%;" />

9. shell to solid 用在这种情况：壳体部分使用shell单元，部分使用solid单元。将shell的边和solid的侧面相连。

10. ![image-20200616102303335](Abaqus.assets/image-20200616102303335.png)

11. 刚体是节点和元素的集合，他们的行为有一个参考节点（6个自由度）来控制，自由度缩减，刚体的运算效率高。边界条件施加在参考点上。如果刚体存在旋转，则参考点应放在质心。不需要材料参数和截面性质

12. 如果多个物体之间有接触关系，其中一个物体的刚度远高于另一个，可以将它设置为刚体，例如金属成型中的模具。

13. 刚体part有两种，离散刚体（可以是各种形状，不可是实心的，必须转成薄壳，使用如下单元）和解析刚性面（形状规则，计算较快，不用划分网格，只能用在接触对的设定）。

    ```
    2—D: 
    	R2D2:平面线段
    	RAX2:轴对称薄壳
    3-D:
    	R3D3:三角形薄壳
    	R3D4:四边形薄壳
    ```

14. 除了创建刚体part，还可以使用rigid body constraint。将原本是可变性体的part或其部分变成刚体。这个比刚体part调整更自由。这个需要对物体划分网格，指定材料和截面。

15. ABAQUS可以自动将参考点移动到所选部分的质心。如果想要施加外力矩在刚体上，则不用勾选此选项。

16. ![image-20200616103850406](Abaqus.assets/image-20200616103850406.png)

17. 边界非线性发生在荷载或边界条件随着结构的变形而改变。分为两种①接触，极度不连续的非线性形式②改变外力的方向，例如给气球充气的压力载荷。

18. ![image-20200616104919764](Abaqus.assets/image-20200616104919764.png)

19. 一个step包含多个increment，一个increment可能包含多的iteration。如果在迭代规定次数达不到收敛条件，则会缩小increment，继续迭代尝试。一个attempt内会做几次iteration，如果不收敛会新增一个attempt，以更小的increment进行迭代。

20. ![image-20200616151919353](Abaqus.assets/image-20200616151919353.png)

21. implicit分析通常使用Newton-Raphson法。无条件稳定（任何增量大小都可以使用）。

22. ABAQUS通过判断力残差和位移修正是否满足要求来判断是否收敛。

23. 下面这图是按照力来划分增量（通过time step的划分来加载），第一个迭代结束，力和位移的差距都较大，继续做切线，经过3次迭代，达到收敛条件。

24. ![image-20200616111820537](Abaqus.assets/image-20200616111820537.png)

25. 自动时间步长会监控迭代次数，如果轻易收敛，则会增大increment。每次50%。如果较难收敛，则缩小increment。

26. 如果总增量步数超过max number，或所需的最小增量<定义的Minum，都会中断。几何非线性来自于大位移，预应力，荷载刚度。显式分析默认开启。

27. 求解过程中的信息会输出到jobname.sta或jobname.msg文件

28. 定义接触后就可以传递压力和摩擦力。

29. ABAQUS提供两种基于surface的接触：①general contact，只要是范围内包含的节点和单元之间发生接触就会计算，计算机来考量接触行为。②contact pair，需要逐一定义，每次只能定义两个面之间的，分析范围小，计算速度快。

30. <img src="Abaqus.assets/image-20200616184730505.png" alt="image-20200616184730505" style="zoom: 67%;" />

31. 二者的选择取决于定义接触的难度和所需分析的效率。如果接触难以定义，则使用general contact，如果要求分析效率高，则使用contact pair。

32. 不过有些情况下只有contact pair可以使用。网球拍的面就是node-based，只有点线，没有面。

33. ![image-20200616185252123](Abaqus.assets/image-20200616185252123.png)

34. general contact只能在initial步设置。默认是所有的外表面，也会考虑自接触。也可以排除一些面之间的接触。

35. ![image-20200616190020490](Abaqus.assets/image-20200616190020490.png)

36. 所有的接触属性可能不同，可以特定的接触指定属性。

37. ![image-20200616195405046](Abaqus.assets/image-20200616195405046.png)

38. 定义contact pair（surface to surface contact），要设定master（之能是surface）和slave（可以是surface或node region）。

39. contact和荷载边界条件一样，可以在不同的step中开关。

40. 也可以使用find contact pair来根据指定的tolerance寻找可能的contact pair。这样可以避免使用general contact，提高计算效率。

41. 同一个surface中的单元应该是相容的，同纬度，同阶插值，同为可变性或不可变形的。

42. master的法线方向必须一致，且都指向slave面。

43. ![image-20200616200955606](Abaqus.assets/image-20200616200955606.png)

44. 一般来说接触行为至少包含切向和法向的。

45. 法向接触默认是hard 硬接触（不连续的）。压力的距离的关系如下，未接触时，压力为0，一旦接触，压力可以任意大（随外力变化）。

46. ![image-20200616201505088](Abaqus.assets/image-20200616201505088.png)

47. 除了hard以外都是soft接触。法向行为可以设定接触后是否可以分离。

48. ![image-20200616201818598](Abaqus.assets/image-20200616201818598.png)

49. 指数形式的，为了解决数值计算的问题。

50. ![image-20200616201907131](Abaqus.assets/image-20200616201907131.png)

51. 切向接触行为默认为无摩擦的。达到最大静摩擦力后会滑动，否则不相对滑动。

52. ABAQUS的penalty模式使用coulomb摩擦，临界静摩擦力取决于接触压力。摩擦系数可以是相对滑移速度，压力等的函数。在发生不可恢复滑动之前，ABAQUS允许少量弹性滑动。

53. ![image-20200616210359231](Abaqus.assets/image-20200616210359231.png)

54. frictionless为完全光滑，rough为完全粗糙，不可滑动（同时应将normal behavior设置为接触后不分离）。

55. 可以输出到odb中的接触结果：

56. ![image-20200616210736720](Abaqus.assets/image-20200616210736720.png)

57. 定义surface时，对于解析刚性面，要注意选对面。要接触的那个面。颜色不同。

58. 如果定义一个空的contact properties，也会有normal和tangential两个属性，默认是hard和frictionless。

59. 对于实体单元，pinned（铰接）和encastre（刚接）是一样的。因为节点本来就没有转动自由度。

60. 在BC中进行位移加载时。如果设置不为0的位移，则物体会动。对于垂直下压的刚性面，不仅要设置下压的位移，其他方向的位移要约束住，否则会乱动。

61. partition有3种情况，edge，face，cell。分别产生新的点，线，面。

62. ABAQUS中一般称壳（包含shell membrane）和梁单元（包含beam truss）为结构单元。membrane和truss不能受弯。

63. 结构单元是简化的单元，运算成本低于实体单元。但是这些结构单元的使用是有条件的。满足一定的假设，即壳的厚度和梁的截面尺寸应该<全域结构尺寸的1/10。

64. 壳体单元舍弃了对厚度方向上变化的观察。如果在局部区域需要更详细的结果时，可以使用多点约束导入3维模型，或进行子结构分析。

65. 使用实体元素模拟弯曲问题可能会出现hourglass。

66. 使用二阶单元模拟时，可以较好地模拟弯曲，结果可靠。CPE8平面应变，8节点单元，完全积分。C3D20R，20个节点，缩减积分，所以一共有2\*2\*2=8个积分点。没有剪应力，厚度方向上的应变为0。不论是全积分还是缩减积分，二阶单元都可以精确地模拟弯曲问题。

67. ![image-20200616230637910](Abaqus.assets/image-20200616230637910.png)

68. PS表示平面应力，PE表示平面应变。接触分析只能使用线性单元，4节点的平面矩形单元又称为双线性bilinear单元。

69. ![image-20200616231613914](Abaqus.assets/image-20200616231613914.png)

70. 使用一阶全积分实体单元（CPE4，CPS4，C3D8）模拟。因为这些单元的边界不可以是曲线，所以会出现如下的夹角变化，即在积分点上产生了真实情况下不存在的剪应变。能量没有像真实情况那样全部施加到$\varepsilon_{xx}$上，而是有一部分施加到了$\varepsilon_{xy}$上，使得单元表现得更刚硬，这称为发生了剪力自锁（shear locking）。

71. shear locking在一阶全积分单元上是无法避免的，所以基本不会使用一阶全积分单元（尤其是不在弯曲问题中使用）。

72. ![image-20200616232329017](Abaqus.assets/image-20200616232329017.png)

73. 如果使用一阶缩减积分单元(CPE4R，C3D8R)模拟弯曲，积分点在中心，可以看出积分点上没有剪应变$\varepsilon_{xy}$（经过该点的等参线没有夹角的变化，消除了剪力自锁），也没有$\varepsilon_{xx}$和$\varepsilon_{yy}$。但是会产生hourglass沙漏问题。即有变形却没有应变能，零能量变形，沙漏化。

74. 如果厚度方向只有一层的话，这些单元都会crash，因为单元非常的软。可以通过在厚度方向划分多层（至少4层，经验建议6层）来消除沙漏问题。下图可以看出，3层和2层是一样的，因为3层的中间层是不受力的，没有刚度。

75. 下面的上一张图就是沙漏化后的结果。ABAQUS有内建的沙漏化控制，能够减少因为沙漏造成的问题。分析完成后，要确认，用来控制沙漏化的虚假能量（增加到单元的应变能中，使得单元显得没有那么软）应该<<内能（1%以下）。

76. ![image-20200617000216877](Abaqus.assets/image-20200617000216877.png)

77. 出现沙漏问题的网格，虚假能量占比为2%。

78. ![image-20200617000512386](Abaqus.assets/image-20200617000512386.png)

79. 沙漏化现象很容易随着网格传播，造成不可靠的结果。

80. ![image-20200616234803295](Abaqus.assets/image-20200616234803295.png)

81. 厚度方向分多层的一阶缩减积分单元是一种有效地解决手段。即使使用多层，计算量仍然要比二姐元素低。

82. 非协调元（incompatible）模式可能是用来模拟弯曲变形为主的问题的最有效的实体单元形式了。没有剪力自锁和沙漏问题。厚度方向只要一层即可模拟弯曲问题。但是如果从厚度方向看去，单元必须要非常规整，如果单元是平心四边形时会降低精度，梯形时精度会非常差。例如：

83. 下图中C3D20可以看做是真实解，C3D8是完全错误的，因为剪力自锁，比真实解更硬。C3D8I在偏角小的时候，精度还是很高的，随着偏角的增大，单元变硬。

84. ![image-20200616235633458](Abaqus.assets/image-20200616235633458.png)

85. C3D8I适用于足够规整，又非常薄的结构，例如玻璃。

86. 二阶元素在分析应力集中和静止裂缝上的问题时，比一阶积分更好。缩减积分元素也是可以的，例如C3D20R。

87. <img src="Abaqus.assets/image-20200617003056431.png" alt="image-20200617003056431" style="zoom: 67%;" />

88. ![image-20200617003145732](Abaqus.assets/image-20200617003145732.png)

89. 三角形和四面体对扭曲没有四边形和六面体敏感。

90. 下图左边的网格划分较好。

91. ![image-20200617003945747](Abaqus.assets/image-20200617003945747.png)

92. 不可压缩材料，即泊松比=0.5。几乎不可压缩材料（ 泊松比>0.475）。常见的有橡胶，和有大塑性应变的金属材料。

93. 传统的有限元网格通常会因为体积自锁volumetric locking而表现出刚硬的行为。在材料被约束严密时（例如被钢板严密包裹的橡胶）表现地更为明显。

94. ![image-20200617004306209](Abaqus.assets/image-20200617004306209.png)

95. 对于不可压缩材料，每一个积分点的体积要保持不变，例如全积分6面体单元使用8个积分点，每个单元上比之前多了8个约束（即积分点的体积不变）。使得单元显得比原来刚硬了。

96. 体积自锁最常发生在全积分单元中，缩减积分可以较好地减少体积自锁。

97. 在使用standard隐式求解时，可以使用hybrid单元，该单元将压应力看做基本求解变量，使得减轻体积自锁，但会增加求解时间。几乎所有单元都有其对应的hybrid类型。尽量使用四边形或六面体的Hybrid单元，而不是三角形或四面体的。

98. ABAQUS在拓扑上只有一下12种单元。

99. <img src="Abaqus.assets/image-20200617011220167.png" alt="image-20200617011220167" style="zoom:80%;" />

100. 一阶的三角形/四面体元素的精度较差，收敛速度慢，及时使用Hybrid单元模拟不可压缩材料仍可能出现体积自锁。如果使用三角形/四面体则推荐使用二阶的。

101. 网格收敛性分析，随着网格的细化，关键变量差异变小。如下图中绿线左侧不可靠。

102. ![image-20200617012032048](Abaqus.assets/image-20200617012032048.png)

103. .inp文件是ABAQUS/CAE和求解器之间的唯一沟通媒介。.inp文件中没有几何，只有网格。一个job对应一个jobname.inp文件。

104. *开头表示是关键字。**开头表示注释。黄色区块内的关键字已经要在蓝色之后，区块内部的关键字顺序可以互换。

105. ![image-20200617012530360](Abaqus.assets/image-20200617012530360.png)

106. interactive表示使用CAE建模，keyword表示使用inp文件。

107. 开头行下面可以接多个资料行。

108. 之所以存在inp文件，是因为某些功能在CAE中还不支持。

109. 如果直接编辑.inp文件，这是不会影响CAE中的设定的。如果要运行修改后的inp，可以在create job是选择使用input file。

110. ![image-20200617013334428](Abaqus.assets/image-20200617013334428.png)

111. 另外一种方式是在CAE中编辑inp文件，这样CAE中会变更，此时如果再生成inp文件时也会保存之前的修改。

112. ![image-20200617013536948](Abaqus.assets/image-20200617013536948.png)

113. inp文件也可以作为一个ABAQUS和其他软件之间交互的媒介（可以包含除了几何以外的任意数据）。import的方法会丢弃CAE不支持的特性。

114. ABAQUS 的.cae文件不同版本是向下兼容。但是.inp文件是前后都兼容的。可以跨版本。

115. 使用命令行来执行inp文件。job名可以不加.inp后缀。还可以在最后添加int参数，进行互动，展示计算信息。

     ```
     abq6111 job=要执行的inp文件名 oldjob=多个分析工作之间如果有数据传输需求，这里为数据来源的文件名 cpus=使用的核心数量
     ```

116. 每个方向布置3个积分点，可以模拟5次函数，因为3个积分点，有6个变量（每个点的位置和权重）可以达到5次函数的精度。坐标分别为0（8/9），$±\sqrt{\frac{3}{5}}$（5/9）。缩减积分的话是每一行或列比完全积分少一个积分点。

117. ![img](Abaqus.assets/v2-330bf75a1ad2e8a67c3c167ac24d2e61_720w.jpg)

118. 通常说的一阶单元指的是位移好分布是一阶的，因而应力和应变是常量。二阶单元的位移是平方关系，应变和应力是1阶的，能量是2阶的。

119. 一个instance无论如何切分partition，都是相连的，划分网格后，节点是共用的。

120. 第一次预览动画的时候会卡，走完正的steptime后就会平顺些。

121. assembly多个instance可以生成一个新的part。

122. 使用embedded region构件钢筋混凝土构件时，可以打开透视，来选择混凝土内部的钢筋骨架。

123. 模拟加载和制作的垫块时，可以在垫块上建立一个ref point，将对应的surface 耦合到该ref point。然后把荷载和位移约束施加到refpoint上。

124. 注意，对于实体单元来说，只有平动自由度，而coupling到ref point后，该point是具有转动自由度的。视情况进行约束。

125. 显式分析默认是instantaneous，隐式分析默认是ramp。不过都可以通过amplitude进行设置，让显式分析使用逐渐变化的荷载（tabular，设置两个点，ABAQUS会自动在者之间进行插值），实现准静态分析。

126. 使用calibration来导入单轴拉伸实验的材料数据。然后导入dataset。可以自动进行工程→真实应力应变转化。然后编辑一个behavior，将它赋予给一个空的material。ABAQUS会用多段线性来拟合这个数据。

127. ![image-20200617193057304](Abaqus.assets/image-20200617193057304.png)

128. 可以将constraint转化成固定的，打断，并且instance保持现在位置，这样做是为了防止后续的其他修改影响其他。

129. ![image-20200617194404766](Abaqus.assets/image-20200617194404766.png)

130. ABAQUS可以使用 by angle来选择一些夹角在一定范围内的面或线等。

131. 勾选下面的选项，会使得在分析一开始，就将tie的两个面贴合到一起。一般不推荐使用，因为可能造成零件反转等位置情况。

132. <img src="Abaqus.assets/image-20200617200015295.png" alt="image-20200617200015295" style="zoom: 80%;" />

133. 对于位移BC的设置，在initial步只能设定某些为0或不为0。不能设定值（例如按照位移加载）。在其他的载荷步可以设置。

134. 设置global seed时，使用的curvature control时，设定的最大偏差值，是曲线和直线之间的最大间隙/曲线上单元边的长度。该数值越小，直线就越贴合曲线，需要划分更多的段数。下方会显示大约的分段数。

135. 偏差系数=h/L，其中h为几何与单元之间的容许间隙，L为单元的长度

136. 一个圆孔最少需要3个单元的边来模拟。

137. ![image-20200617211411996](Abaqus.assets/image-20200617211411996.png)

138. 6面体和四边形网格的生成算法有两种，①advancing front②medial axis。第二种对于圆孔较多的图形能够划分更好。

139. <img src="Abaqus.assets/image-20200617212645972.png" alt="image-20200617212645972" style="zoom: 50%;" /> <img src="Abaqus.assets/image-20200617213117618.png" alt="image-20200617213117618" style="zoom: 50%;" />

140. ABAQUS会将默认30个数据达成一个group。，可以右键 group children，取消group。

141. 时间历程会输出位移-时间，应力-时间的曲线，如果要输出位移-力的曲线，则应该将二者combine起来。先后选择要作为X和Y的数据，然后右键save as，勾选combine(XY,XY)即可。

142. XYdata 输出场变量时，如果勾选积分点，则应选择单元，如果勾选unique nodal，则应勾选节点。

143. 默认的history 输出会将所有的能量输出出来，他可以帮助判断模型是否有问题。例如将artificial strain energy和internal energy对比来观察hourglass情况的严重与否。

144. internal energy=artificial strain energy+plastic dissipation +strain energy

# 动力学

1. 理论上来说，静力问题也可以当做动力问题来求解，不过这会浪费较多时间。当惯性力不可忽略，且随时间变化较快时，动力问题就不可以忽略。

2. 求解动力问题需要在时间域内对运动方程进行积分。显式方法是直接积分，耗时较长。

3. 模态分析和稳态动力学都不需要对时间进行积分，他们是在频率域进行的。

4. 运动方程：M质量矩阵为常数，不随时间变化。C和速度乘积为阻尼力，K和节点位移乘积为结构内力。$M\ddot{u}(t)+C(t)\dot{u}(t)+K(t)u(t)=P(t)$。

5. 如果K和C都是常数，则称之为线性动力学。如果第一项M和加速度乘积足够小，可以简化为静力平衡式。

6. 可以用ABAQUS求解的线性动力问题如下： 

   1. 自然频率求取（不需要积分）
   2. 振型叠加
   3. 隐式动力分析（直接积分）
   4. 简谐加载（不需要积分）
   5. 反应谱分析（不需要积分）
   6. 随机振动（不需要积分）

7. ABAQUS中模态分析，忽略阻尼。也是无法考虑接触行为。如果在模态分析前考虑过几何非线性，是可以接着进行模态分析的。$M\ddot{u}+Ku=0$。

8. 三种可用的求解器用来求解特征值问题。

   1. Automatic multi-level substructuring (AMS) 需要大量特征值时，最快速的求解器，对standard而言，AMS是内建的分析工具
   2. Lanczos （预设）用于超大型结构，使用SIM架构
   3. Subspace iteration 子空间迭代

9. 所有的动力问题都需要定义密度。

10. 当存在材料非线性，几何非线性，接触非线性任意一个时，评估结构的动态响应需要使用非线性动力学。

11. 线性动力学采用模态叠加，非线性动力学采用直接积分的方法。隐式和显式方法使用不同的时间积分策略。

12. ABAQUS使用隐式求解方法，需要求切线刚度矩阵。每个时间点时都要进行迭代求出该矩阵。无条件稳定。
    $$
    \bar{K_i}=\frac{M}{\beta\Delta t^2}+\frac{\gamma}{\beta\Delta}C+K_i
    $$
    
13. 显式方法只需建立一次系统的刚度矩阵，不用计算切线刚度矩阵。条件稳定，只有时间增量小于一个临界值，才可以计算出有限解。稳定时间增量取决于最高特征频率和该模态的临界阻尼。
    $$
    \Delta t_{\min} \le \frac{2}{\omega_{\max}}(\sqrt{1+\xi^2}-\xi)
    $$
    
14. 或者用单元尺寸/波速 $\Delta t=L_e/c_d$。

15. Standard和Explicit的区别：

    1. Standard
       1. 时间增量的大小没有限制，通常少于所设定的时间增量数，就能完成模拟
       2. 每个时间增量都是珍贵的，每一次推进都要求解复杂的方程

    2. Explicit
       1. 时间增量大小受限制，通常需要更多的时间增量数来完成模拟
       2. 每个时间增量相对廉价，因为不需要求解复杂的方程
       3. 计算耗时与否取决于元素的计算

16. obd文件中没有几何信息，只有网格信息。

17. ABAQUS print到file，可以选择eps格式，再输出为tif，这样既清晰，体积又小。

18. 运行datacheck也会产生inp文件和odb文件，不过对应的输出都是0。

19. face是单元的表面，由node构成。

20. ![image-20201027200533170](Abaqus.assets/image-20201027200533170.png)

21. report输出时，integration point是积分点，对于本例的C3D20R。一共有2x2x2=8个积分点。centroid是指单元的中心，一个单元只有1个。element nodal对于本例，1个单元有20个。unique Nodal对于本例，也是20个。

22. ![image-20201027210122298](Abaqus.assets/image-20201027210122298.png)

23. 对于两个相邻的C3D20R单元来说，element Nodal是按照单元来组织的，2个单元，每个20个，但是其中会有重复的，相邻的face上的所有Node都有重复。而Unique Nodal是不考虑单元，只考虑这些node，不重复出现。一共有2x20-8=32个。

24. 

# 命令

1. ABAQUS的两个主要模块为cae和viewer。可以使用如下命令启动。在cae中可以打开.cae和.odb文件，但是在viewer中只能打开.odb文件。replay选项支持一个Python脚本，启动后会立即执行该脚本。

   ```
   abaqus cae or viewer 
                                                       [database=database-file]
                                                       [replay=replay-file]
                                                       [recover=journal-file]
                                                       [startup=startup-file]
                                                       [script=script-file]
                                                       [noGUI=[noGUI-file]]
                                                       [noenvstartup]
                                                       [noSavedOptions]
                                                       [noSavedGuiPrefs]
                                                       [noStartupDialog]
                                                       [custom=script-file]
                                                       [guiTester=[GUI-script]]
                                                       [guiRecord]
                                                       [guiNoRecord]
   ```

3. 通过命令行给Python脚本传递参数，这些参数会被CAE忽略，但是会传递给Python解释器。

   ```python
   import sys
   print sys.argv[-1]     #获取最后一个参数，即argument1。
   
   abaqus cae script=try.py -- argument1      #运行该命令，会打开ABAQUS，在Python输出窗口输出argument1
   ```

4. 从下面可以看出：除了额外输入的3个参数，一共还有8个参数。

   ```
   G:\Abaqus file>abaqus cae noGui=checkPartValidity.py -- test.cae Model-1 Part-1
   Abaqus License Manager checked out the following license(s):
   "cae" release 6.14 from Flexnet server 20190927ZJ
   <1023 out of 1024 licenses remain available>.
   D:\SIMULIA\Abaqus\6.14-1\code\bin\ABQcaeK.exe
   -cae
   -noGUI
   checkPartValidity.py
   -lmlog
   ON
   -tmpdir
   C:\Users\ADMINI~1\AppData\Local\Temp
   test.cae
   Model-1
   Part-1
   ```

5. 不打开ABAQUS图形界面运行。这个可以和参数结合使用。

   ```python
   abaqus cae noGui=checkPartValidity.py
   ```

6. ABAQUS会将用户对GUI界面的设置保存在abaqus_v6.14.gpr文件中，还会将用户的操作保存在abaqus.rpy文件（Python脚本）中，方便用户复现之前的操作。每次打开CAE都会新建一个rpy文件，并将之前存在的rpy文件重命名。

7. 如果启动CAE时，使用了noSavedOptions 选项。CAE将不会读取abaqus_v6.14.gpr中的设置。

8. 默认情况下，启动CAE时，会依次读取家目录和启动CAE是的目录中的.gpr文件。关闭CAE时，会自动保存当前的GUI设置到家目录中的文件。也可以删除该文件，来还原设置。

9. CAE内部包含了一个非活动的计时器，如果应用长时间不活动，license就会被服务器收回，给其他用户使用。默认时间是60分钟。可以通过修改环境变量文件abaqus_v6.env中的cae_timeout来更改时间。

10. 系统的abaqus_v6.env文件放在/SMA/site路径下。也可以在用户家目录，启动目录中存放该文件。CAE启动的时候会依次读取。使用的是Python语法。

11. 视图中的部分，在打印出图时会用到：

    1. viewport decorations→title border
    2. viewport annotations→legend, state block, title block, view orientation triad, and 3D compass

12. 链接的窗口只能有一个，打开该功能后，勾选需要链接的窗口即可。链接的窗口可以选择要同步的选项。一般来说就同步位置和视角就行了，而具体的field output就按照各个

13. <img src="Abaqus.assets/image-20210320111520801.png" alt="image-20210320111520801" style="zoom: 80%;" />

14. 

15. 

16. 
