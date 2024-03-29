# Ansys

1. ANSYS提供多种求解器：①迭代求解器（预条件共轭梯度、雅克比共轭梯度、不完全共轭梯度）②直接求解器（波前、稀疏）③特征值算法（分块lanczos法，子空间法，凝聚法，QR阻尼法）④并行求解器（分布式并行，代数多重网格）。
2. 可以进行几何非线性，材料非线性，接触非线性，单元非线性分析。
3. 支持拓扑优化，对几何外形进行优化。
4. 可以进行多场耦合分析。
5. 结构分析有7种类型，基本位置量是位移，①**静力分析**可以考虑非线性，支持应力刚化，②**特征屈曲分析**可以求解结构的线性屈曲荷载和屈曲模态。非线性屈曲分析和循环对称屈曲分析属于静力分析的范畴。③模态分析可以计算线性结构的固有频率和振型④谐响应分析，确定线性结构在随时间变化的正弦荷载下的响应。⑤瞬态动力分析：计算结构在随时间变化的任意荷载下的响应。可考虑非线性全瞬态和线性模态叠加法。⑥谱分析，模态分析的扩展，计算响应谱和PSD（功率谱密度）输入引起的响应。可考虑单点谱和多点谱。⑦显式动力学分析有LS-DYNA来完成对高度非线性动力学或复杂接触问题。
6. ANSYS按功能模块分为9个处理器，命令必须在对应的处理器下运行。一个命令可以属于多个处理器。刚启动ANSYS时，位于开始级，不处于任何处理器下。
7. ![1589292008531](ANSYS笔记.assets/1589292008531.png)
8. ![1589292033296](ANSYS笔记.assets/1589292033296.png)
9. 日志和错误文件总是采用追加的方式，而不是覆盖。如果结果文件太大，可以分割为多个文件。
10. 命令流中也可以包含GUI的函数，使用命令调用，参数通过窗口输入。
11. 通过/input命令或Utility Menu→File→Read input from读入执行。
12. 也可以拷贝该文件的内容到命令行中执行。
13. ANSYS中常见的单元都是结构单元，如杆，梁，管，壳，2D（实际是3D问题的简化）实体单元，3D实体单元，弹簧，质量单元，接触，显式动力分析单元。
14. 杆单元可以模拟桁架，缆索，连杆，弹簧等构件。节点只有平动的自由度，只能受压或受拉。
15. 易混淆的单元特性
16. 大挠度（deflection）=大变形    支持考虑几何非线性。
17. 大应变=有限应变         支持高阶的应变公式。
18. 应力刚化=几何刚度
19. ![1589292132182](ANSYS笔记.assets/1589292132182.png)
20. 杆单元是均质直杆，仅能承受杆端荷载，单元内应力相同，可以考虑初应变。
21. LINK180在大变形分析时，横截面可以变化，可以是轴向伸长的函数或刚性。可以考虑附加质量。
22. LINK10是非线性单元，需要迭代求解，可以模拟地基弹簧，橡胶支座，支持松弛和间隙的求解，支持仅受拉或受压。
23. LINK180除了不具备双线性特性（LINK10）外，其他情况下均可以使用。
24. LINK1,LINK8,LINK180还可以用于模拟普通钢筋和预应力钢筋。可以用初应变的方式施加预应力。
25. 在进行线性静力分析时，结构不能是几何可变的，否则会提示位移超限的错误。
26. BEAM188是3节点，一个节点用于定位，决定单元方向。是铁木辛柯梁，计入一阶剪切变形。
27. BEAM189是4节点，一个节点用于定位，是二次单元。
28. 2D单元一般都只能在X-Y平面内布置。
29. 考虑剪切变形会增加梁的附加挠度。使得原来垂直于中和轴的截面在变形后不垂直了（违背基尔霍夫假定）。如果考虑翘曲自由度，则不在满足平截面假定，变为曲面。
30. 当梁的高跨比<10时，可以忽略剪切变形的影响。
31. 考虑剪切变形有两种方法：①在经典梁单元的基础上引入剪切变形系数，如BEAM3/4/23/24/44/54。截面的转角由挠度的一阶导数导出②铁木辛柯梁理论BEAM188,BEAM189。截面的转角和挠度独立插值。
32. 梁单元不仅可以传递平动自由度，还可以传递转动自由度，即可以传递集中力和弯矩。不过在某些结构中，不想考虑弯矩的传递。有两种方法达到这种情况：①相连的梁单元使用两个重合节点在同一位置，重合的节点耦合平动自由度，不耦合转动自由度。②像平时建立单元，不使用重合节点，但是在节点处释放单元的自由度，来控制内力的传递。
33. 之前可以用有释放自由度功能的BEAM44单元，Keyopt（7）控制6个方向的自由度。不同释放自由度的单元类型需要不同的element type。
34. ANSYS13.0使用新的endrelease命令实现。beam188/189可以使用这个命令。使用方法如下：
35. ![1589292132182](ANSYS笔记.assets/1589292132182.png)
36. 通过释放自由度可以将刚性节点变为球铰。
37. 梁单元在约束扭转占比较大时，应该激活翘曲自由度。
38. beam188/189支持变截面的梁。不支持跨间集中荷载和跨间部分分布荷载，仅支持整个单元长度上分布的荷载。
39. 对于只输入实常数的梁单元，假定中性轴平分面高度，即最外层纤维到中性轴的距离为梁高的一半，如果不满足该假定，则应力计算没有意义。
40. 管单元相当于是梁单元的简化，包含了对称性和标准管几何尺寸的简化性。已经不推荐使用了，可以使用梁单元代替。
41. 2D实体单元可以用于平面应力，平面应变，轴对称单元。只能在XY平面内，且轴对称分析中，Y轴是对称轴。每个节点都只有2个自由度（谐结构单元除外，ANSYS推荐使用solid272）。
42. 轴对称单元的位移包括轴向（平行对称轴），径向，切向（仅谐结构单元有）。
43. P（polynomial）单元是通过提高单元形函数的阶数，来提高精度，也成为升阶谱单元。形函数的阶数提高后，可以拟合更复杂的边界，减少尖角的出现。可以在不用重新划分网格的基础上获得更优的解。
44. H单元是提高单元的密度，即将单元划分为更细的块，来提高精度。H单元可以看做特殊的P单元，即P=1。
45. 如果在几何体的局部区域有高的应力变化梯度的话, 那么使用混合的hp方法是最好的选择. 对更加关心的局部的区域使用P单元, 而整个几何体的其他部分都可以使用H单元。
46. ![1589292167023](ANSYS笔记.assets/1589292167023.png)
47. 除6节点三角形单元外，其余单元均可退化成三角形单元。
48. 大多数单元支持边界的分布荷载和节点荷载，而P单元只支持节点荷载。
49. 平面应力问题如果输入厚度，施加的分布荷载不是线荷载，而是面荷载。如果不输入厚度，则默认为单位厚度。
50. 3D实体单元每个节点都有3个平动自由度。
51. 除10节点单元不能退化，其余单元均可退化成棱柱，四面体单元。且SOLID95/186又可以退化成金字塔（宝塔）单元。
52. ![1589292224836](ANSYS笔记.assets/1589292224836.png)
53. 壳单元用来模拟平板或曲壳等结构，比梁和实体单元要复杂得多。每个节点有6个自由度。
54. 在薄壁结构用可以使用壳单元，也可以当做3维实体来建模使用solid单元。
55. Shell41是膜壳，可以设置只能受拉。
56. ![1589292242746](ANSYS笔记.assets/1589292242746.png)
57. 通常不计入剪切变形的单元用于薄板壳，计入剪切变形的单元用于中厚度薄板壳。
58. ![1589292270885](ANSYS笔记.assets/1589292270885.png)
