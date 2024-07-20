# 官方教程

## 几何基础，基本实体，物理组

1. ```python
   import gmsh #Python API都定义在gmsh.py中，包括文档
   import sys
   gmsh.initialize() # 使用任何API前，必须先初始化
   gmsh.model.add("t1") #添加一个新的模型，名称为t1，如果没有调用该函数，则会创建一个未命名的模型。
   # Python API提供对每个支持的CAD内核的直接访问，内置内核的API都是以gmsh.model.geo开头。
   lc = 1e-2
   gmsh.model.geo.addPoint(0, 0, 0, lc, 1) #创建点，前3个参数是坐标，lc是该点附近的目标网格尺寸，最后一个参数是该点的编号，要求>0，且在对应类型内是唯一。这里的tag编号非常类似于Windows变成中的句柄，就是一个数，具体的含义由内部维护的数据结构来决定，这么做会减轻数据拷贝的开销。
   # 提供驼峰(addPoint)和小写下划线(add_point)两种方式，都可以使用。
   # 网格单元尺寸的分布会通过对几何上的网格尺寸进行插值得到，另一种方法是使用通用的网格尺寸场(t10.py)，一种特殊情况时使用背景网格(t7.py)。
   # 如果没有提供目标网格尺寸，则会使用默认的基于整体模型尺寸的粗糙尺寸。
   gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
   gmsh.model.geo.addPoint(.1, .3, 0, lc, 3)
   p4 = gmsh.model.geo.addPoint(0, .3, 0, lc) # 如果没有显式提供标识，则会自动创建标识，并作为函数的返回值返回。
   # 曲线的编号和点的编号互不干扰，每一个维度的几何实体的编号互相独立。
   gmsh.model.geo.addLine(1, 2, 1) #前2个参数是线段的起止点的编号，最后一个参数是线段的编号
   gmsh.model.geo.addLine(3, 2, 2) #创建线段，它是曲线的一种。
   gmsh.model.geo.addLine(3, p4, 3)
   gmsh.model.geo.addLine(4, 1, p4)
   # 为了定义曲面，需要先定义曲线循环，曲线循环就是一组首尾相连的曲线的有序列表。负号作用在列表中的曲线表示该曲线的反向。
   gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1) #第一个参数是一个包含曲线的列表，地热个参数是曲线循环的标识，如果省略，则以返回值返回。
   gmsh.model.geo.addPlaneSurface([1], 1)# 可以使用一个曲线循环的列表来定义曲面，例如圆环就是2个方向相反的曲线循环组成。
   gmsh.model.geo.synchronize()# 在划分网格前，或者说被内置CAD内核之外的函数访问签，CAD实体需要和模型进行同步，这回创建相关的gmsh数据结构，可以在任意时刻进行同步，但是会消耗时间，因此推荐几何建完之后再同步。
   # 可以为几何实体创建物理组，这样方便后续施加载荷和输出请求。默认情况下，如果定义了物理组，那么只会输出包含在任意一个物理组中网格单元，也可以将Mesh.SaveAll选项设置为1来强制保存所有网格单元。物理组也有对应的标识，每个维度之间互相独立，还可以可以赋予名称字符串。使用标识和名称都可以定位到这个物理组。
   gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5) #第一个参数是维度，第二个参数是该维度中几何实体的列表，最后一个参数是标识。
   gmsh.model.addPhysicalGroup(2, [1], name="My surface") #指定名称，方便导出网格后识别。
   gmsh.model.mesh.generate(2) #生成2D网格
   gmsh.option.setNumber("Mesh.SaveAll", 1) #将该选项设置为1
   gmsh.write("t1.msh") #保存到磁盘
   # 默认情况下，Gmsh会保存为最新版本的MSH格式，也可以使用扩展名来指定不同的格式。
   gmsh.write("t1.unv") #保存为.unv格式
   gmsh.option.setNumber("Mesh.MshFileVersion", x) #设置要保存的MSH格式的版本，x是版本号，可以为2或4等。也可以直接在扩展名中指定.msh2或.msh4
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run() #打开Gmsh 图形化界面来显示模型，如果命令行参数包含-nopopup，则不这么做。
   
   # 从Gmsh 3.0开始，可以使用非内置几何内核来构建模型，例如OpenCASCADE，此时API的前缀为gmsh.model.occ。不同的CAD内核有不同的特性，使用OpenCASCADE后，不用自底向上来定义曲面的子实体，可以直接定义曲面。
   gmsh.model.occ.addRectangle(.2, 0, 0, .1, .3) #前三个参数是一个角点的坐标，
   gmsh.model.occ.synchronize() #不同几何内核的同步不一样，同步之后，底层的曲线和点可以通过gmsh.model.getBoundary()获得。
   gmsh.finalize() #使用完毕后，应该调用这个释放内存。
   ```


## 变换，拉伸几何，体积

1. ```python
   import gmsh
   import sys
   import math
   
   gmsh.initialize(sys.argv) #这里将启动python的命令行参数传递给gmsh，例如python t1.py a b c，则argv为["t1.py","a","b","c"]
   gmsh.model.add("t2")
   #下面这段是从t1.py中复制的
   lc = 1e-2
   gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
   gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
   gmsh.model.geo.addPoint(.1, .3, 0, lc, 3)
   gmsh.model.geo.addPoint(0, .3, 0, lc, 4)
   gmsh.model.geo.addLine(1, 2, 1)
   gmsh.model.geo.addLine(3, 2, 2)
   gmsh.model.geo.addLine(3, 4, 3)
   gmsh.model.geo.addLine(4, 1, 4)
   gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
   gmsh.model.geo.addPlaneSurface([1], 1)
   gmsh.model.geo.synchronize()
   gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
   gmsh.model.addPhysicalGroup(2, [1], name="My surface")
   #增加新的点和线段
   gmsh.model.geo.addPoint(0, .4, 0, lc, 5)
   gmsh.model.geo.addLine(4, 5, 5)
   # Gmsh可以进行平移和旋转操作，或者变换的同时复制。
   gmsh.model.geo.translate([(0, 5)], -0.02, 0, 0) #第一个参数是一个包含元组的列表，每个元组代表一个几何实体，元组的第一个元素代表维度，第二个元素代表编号。后三个参数标识dx,dy,dz
   
   gmsh.model.geo.rotate([(0, 5)], 0, 0.3, 0, 0, 0, 1, -math.pi / 4) #第一个参数同上，后续6个参数并非转动轴的两个点，而是一个该轴上的点，一个轴矢量。也就是旋转轴过[0,0.3,0]，且沿z轴正向，最后一个参数是转动角度。
   # Gmsh中的数值没有单位，用户需要自己统一。
   ov = gmsh.model.geo.copy([(0, 3)]) #将一串几何实体复制一份，返回值为元组的列表。
   gmsh.model.geo.translate(ov, 0, 0.05, 0) #将刚才复制的一串几何实体平移。
   
   gmsh.model.geo.addLine(3, ov[0][1], 7) #ov[0]是第一个几何实体，[1]是该实体的编号
   gmsh.model.geo.addLine(ov[0][1], 5, 8)
   gmsh.model.geo.addCurveLoop([5, -8, -7, 3], 10)
   gmsh.model.geo.addPlaneSurface([10], 11)
   
   # 复制编号为1和11的2个曲面，底层的曲线和点也会复制，会自动进行编号。
   ov = gmsh.model.geo.copy([(2, 1), (2, 11)])
   gmsh.model.geo.translate(ov, 0.12, 0, 0)
   
   print("New surfaces " + str(ov[0][1]) + " and " + str(ov[1][1]))
   
   # 类似于定义曲面要先定义曲线循环，定义体积也要定义曲面循环。
   gmsh.model.geo.addPoint(0., 0.3, 0.12, lc, 100)
   gmsh.model.geo.addPoint(0.1, 0.3, 0.12, lc, 101)
   gmsh.model.geo.addPoint(0.1, 0.35, 0.12, lc, 102)
   
   gmsh.model.geo.synchronize() #需要先同步模型，然后再使用getValue获得0维度标号5的几何实体中用参数坐标确定的点的坐标。
   # 根据参数坐标来计算对应的点的空间位置，如果有多个点，则将每个点的参数依次连接起来，例如[u1,v1,u2,v2,...]，此时返回值也会将这多个点的xyz坐标依次连接起来输出，[x1,y1,z1,x2,y2,z2,...]
   xyz = gmsh.model.getValue(0, 5, [])# 第三个参数是包含参数坐标的列表，对于点，该列表应为空，对于曲线，该列表有一个元素，为t，对于曲面，该列表有2个元素，为u,v。
   gmsh.model.geo.addPoint(xyz[0], xyz[1], 0.12, lc, 103) #新的点相当于将5号点沿z轴平移0.12。
   
   gmsh.model.geo.addLine(4, 100, 110) #这里直接使用110编号，是为了避免和之前复制产生的实体的编号冲突。
   gmsh.model.geo.addLine(3, 101, 111)
   gmsh.model.geo.addLine(6, 102, 112)
   gmsh.model.geo.addLine(5, 103, 113)
   gmsh.model.geo.addLine(103, 100, 114)
   gmsh.model.geo.addLine(100, 101, 115)
   gmsh.model.geo.addLine(101, 102, 116)
   gmsh.model.geo.addLine(102, 103, 117)
   
   gmsh.model.geo.addCurveLoop([115, -111, 3, 110], 118)
   gmsh.model.geo.addPlaneSurface([118], 119)
   gmsh.model.geo.addCurveLoop([111, 116, -112, -7], 120)
   gmsh.model.geo.addPlaneSurface([120], 121)
   gmsh.model.geo.addCurveLoop([112, 117, -113, -8], 122)
   gmsh.model.geo.addPlaneSurface([122], 123)
   gmsh.model.geo.addCurveLoop([114, -110, 5, 113], 124)
   gmsh.model.geo.addPlaneSurface([124], 125)
   gmsh.model.geo.addCurveLoop([115, 116, 117, 114], 126)
   gmsh.model.geo.addPlaneSurface([126], 127)
   
   gmsh.model.geo.addSurfaceLoop([127, 119, 121, 123, 125, 11], 128) #创建曲面循环
   gmsh.model.geo.addVolume([128], 129)
   # 如果体积可以通过曲面拉伸得到，则推荐使用extrude更方便，这样不用依次创建所有点，线，面，例如下面的代码。
   ov2 = gmsh.model.geo.extrude([ov[1]], 0, 0, 0.12) #第一个参数是[(2,12)]，也就是面12，将该面沿着向量[0,0,0.12]拉伸，创建一个体积。
   gmsh.model.geo.mesh.setSize([(0, 103), (0, 105), (0, 109), (0, 102), (0, 28),(0, 24), (0, 6), (0, 5)], lc * 3) # 可以批量给几何点设置网格尺寸，第一个参数是元组列表，第二个参数是尺寸。
   gmsh.model.geo.synchronize() #建模结束后，推荐同步一下
   gmsh.model.addPhysicalGroup(3, [129, 130], 1, "The volume") #将3D实体的129和130编号构成一个物理组，编号为1，并命名。这里并没有写成元组列表的形式，因为这里的实体必定是相同维度的。
   gmsh.model.mesh.generate(3)
   gmsh.write("t2.msh")
   # 如果变换工具方便创建复杂集合，有时候生成平坦几何（对所有基础实体的显式表达，也成为展开几何）也有用。使用内置CAD内核，可以将模型保存为.get_unrolled，使用OpenCASCADE内核时，可以保存.brep，也可以保存为STEP格式。
   gmsh.write("t2.geo_unrolled");
   gmsh.write("t2.brep");
   # 需要注意的是，Gmsh从来不会将几何数据转化为一个通用的表达，所有的操作都是在各自的CAD内核上进行，不能将用内置几何内核创建的模型转化为OpenCASCADE的Brep格式，也不能将OpenCASCADE模型转化为.geo_unrolled格式。
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   gmsh.finalize()
   ```


## 拉伸网格，ONELAB参数，选项

1. ```python
   import gmsh
   import math
   import sys
   
   gmsh.initialize()
   
   def createGeometryAndMesh():
       gmsh.clear() #清理所有模型
       gmsh.model.add("t3")
       # 从t1.py复制来的
       lc = 1e-2
       gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
       gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
       gmsh.model.geo.addPoint(.1, .3, 0, lc, 3)
       gmsh.model.geo.addPoint(0, .3, 0, lc, 4)
       gmsh.model.geo.addLine(1, 2, 1)
       gmsh.model.geo.addLine(3, 2, 2)
       gmsh.model.geo.addLine(3, 4, 3)
       gmsh.model.geo.addLine(4, 1, 4)
       gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
       gmsh.model.geo.addPlaneSurface([1], 1)
       gmsh.model.geo.synchronize()
       gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
       gmsh.model.addPhysicalGroup(2, [1], name="My surface")
   
       # 和t2.py不同的时，这里想要拉伸的是网格，而非几何。使用的也是extrude函数，需要指明拉伸几段，每段的参数尺寸。
       h = 0.1
       ov = gmsh.model.geo.extrude([(2, 1)], 0, 0, h, [8, 2], [0.5, 1]) #第一个参数是要拉伸的实体的标识，2表示其维度，后续3个参数为dx,dy,dz，[8,2]表示拉伸2段，第一段8层，第二段2层，[0.5,1]表示这两段的终点的参数坐标，也就是都是h/2。
       # 除了沿某条直线拉伸，还可以绕某个轴旋转拉伸，同样可以指定分层。平面网格如果是三角形，则拉伸出来为棱柱体，如果是四边形，则拉伸出来为六面体。
       ov = gmsh.model.geo.revolve([(2, 28)], -0.1, 0, 0.1, 0, 1, 0, -math.pi / 2, [7]) #第一个参数为实体标识，后6个参数为x,y,z,ax,ay,az(a表示axis)，标识旋转轴上的一个点和轴矢量，下一个参数为转动角的弧度，最后一个参数为转动的分阶段，类似于拉伸的分层，这里只有一个阶段，终点的参数坐标就是[1]，因此不需要指定。
       #对于内置几何内核，旋转角度只能是 < Pi。要实现转动一周，则需要至少转三次，例如每次120°。而OpenCASCADE内核没有这个限制。
       # 拉伸和旋转可以组合起来，称为twist，拉伸扭转。extrude和twist的最后一个参数表示是否将拉伸的网格进行重组。
       angle = gmsh.onelab.getNumber('Parameters/Twisting angle')[0] #这里通过onelab获得转动角度的参数值，单位为角度，而Gmsh中角度的默认单位为弧度，需要手动转化。getNumber返回一个list，因为可能有多个匹配的。
       ov = gmsh.model.geo.twist([(2, 50)], 0, 0.15, 0.25, -2 * h, 0, 0, 1, 0, 0, angle * math.pi / 180., [10], [], True) # [0,0.15,0.25]为x,y,z；[-2*h,0,0]为dx,dy,dz；[1,0,0]为ax,ay,az。后两个参数和拉伸的一样，这里无法像旋转一样，设置分段，因为它相当于是在拉伸的基础上扭转，因此侧面为直纹曲面。
       gmsh.model.geo.synchronize()
       # 所有的拉伸函数都返回一个包含拉伸实体的元组列表，例如ov[0]为拉伸的那个面的元组，ov[1]为新创建的体积，ov[2],ov[3]...等为侧面的标识。
       gmsh.model.addPhysicalGroup(3, [1, 2, ov[1][1]], 101) #定义一个新的体积物理组，包含所有的体积，ov[1][1]就是拉伸的体积。
       gmsh.model.mesh.generate(3)
       gmsh.write("t3.msh")
   # 所有的选项都可以通过API来读写。
   gmsh.option.setNumber("Geometry.PointNumbers", 1) #显示几何点的编号
   gmsh.option.setColor("Geometry.Color.Points", 255, 165, 0) #设置几何点的颜色
   gmsh.option.setColor("General.Color.Text", 255, 255, 255) #设置通用文字的颜色
   gmsh.option.setColor("Mesh.Color.Points", 255, 0, 0) #设置网格点的颜色
   
   # Note that for conciseness "Color." can be ommitted in color options:
   r, g, b, a = gmsh.option.getColor("Geometry.Points") #RGBA格式。
   gmsh.option.setColor("Geometry.Surfaces", r, g, b, a) #这里可以简化，省略了Geometry.Color.Surfaces中的Color.。因为函数本身就是setColor。
   # 创建ONELAB参数来定义转动的角度，ONELAB参数可以通过GUI来动态修改，也可以和其他连接到相同ONELAB数据库的程序交换数据。这个数据库可以通过API来用JSON格式化字符串的形式读写。
   # 三个引号是多行字符串，内部可以包含换行。
   gmsh.onelab.set("""[
     {
       "type":"number",
       "name":"Parameters/Twisting angle",
       "values":[90],
       "min":0,
       "max":120,
       "step":1
     }
   ]""") #这个name用/分隔开，会在GUI中产生一个二级菜单，value是默认值，
   
   createGeometryAndMesh() #在主函数中调用之前定义的函数
   def checkForEvent(): #检查事件，它保存在ONELAB/Action参数中，如果有必要可以使用一个新的角度来重新创建几何。
       action = gmsh.onelab.getString("ONELAB/Action") #返回值为字符串列表，每次修改Parameters/Twisting angle的数值，都会将ONELAB/Action设置为["check"]。
       if len(action) and action[0] == "check":
           gmsh.onelab.setString("ONELAB/Action", [""])
           createGeometryAndMesh()
           gmsh.graphics.draw() #绘制所有的OpenGL场景
       return True
   
   if "-nopopup" not in sys.argv:
       gmsh.fltk.initialize() #初始化fltk，只能在主线程中调用。
       while gmsh.fltk.isAvailable() and checkForEvent(): #这样可以保证修改完参数后，立刻生效并显示出来。
           gmsh.fltk.wait() #等待用户界面事件，然后返回。
   
   # 当启动GUI后，可以在Help->Current Options和Workspace中查看所有的选项的当前值，可以使用File->Export->Gmsh Options或者通过api来保存这些选项。
   gmsh.write("t3.opt");
   gmsh.finalize()
   ```


## 带洞的曲面，标注，实体颜色

1. ```python
   import gmsh
   import math
   import sys
   import os
   
   gmsh.initialize()
   gmsh.model.add("t4")
   # 所有的参数集中在开头设置
   cm = 1e-02 #认为设置一个单位标识
   e1 = 4.5 * cm #也就是4.5cm
   e2 = 6 * cm / 2
   e3 = 5 * cm / 2
   h1 = 5 * cm
   h2 = 10 * cm
   h3 = 5 * cm
   h4 = 2 * cm
   h5 = 4.5 * cm
   R1 = 1 * cm
   R2 = 1.5 * cm
   r = 1 * cm
   Lc1 = 0.01
   Lc2 = 0.003
   
   def hypot(a, b): #定义一个函数，计算直角三角形的斜边长度，不过math中自带这个函数
       return math.sqrt(a * a + b * b)
   
   ccos = (-h5 * R1 + e2 * hypot(h5, hypot(e2, R1))) / (h5 * h5 + e2 * e2)
   ssin = math.sqrt(1 - ccos * ccos) #根据余弦值计算正弦值
   
   factory = gmsh.model.geo #可以重命名一个命名空间，这样使得代码变短。
   factory.addPoint(-e1 - e2, 0, 0, Lc1, 1)
   factory.addPoint(-e1 - e2, h1, 0, Lc1, 2)
   factory.addPoint(-e3 - r, h1, 0, Lc2, 3)
   factory.addPoint(-e3 - r, h1 + r, 0, Lc2, 4)
   factory.addPoint(-e3, h1 + r, 0, Lc2, 5)
   factory.addPoint(-e3, h1 + h2, 0, Lc1, 6)
   factory.addPoint(e3, h1 + h2, 0, Lc1, 7)
   factory.addPoint(e3, h1 + r, 0, Lc2, 8)
   factory.addPoint(e3 + r, h1 + r, 0, Lc2, 9)
   factory.addPoint(e3 + r, h1, 0, Lc2, 10)
   factory.addPoint(e1 + e2, h1, 0, Lc1, 11)
   factory.addPoint(e1 + e2, 0, 0, Lc1, 12)
   factory.addPoint(e2, 0, 0, Lc1, 13)
   
   factory.addPoint(R1 / ssin, h5 + R1 * ccos, 0, Lc2, 14)
   factory.addPoint(0, h5, 0, Lc2, 15)
   factory.addPoint(-R1 / ssin, h5 + R1 * ccos, 0, Lc2, 16)
   factory.addPoint(-e2, 0.0, 0, Lc1, 17)
   
   factory.addPoint(-R2, h1 + h3, 0, Lc2, 18)
   factory.addPoint(-R2, h1 + h3 + h4, 0, Lc2, 19)
   factory.addPoint(0, h1 + h3 + h4, 0, Lc2, 20)
   factory.addPoint(R2, h1 + h3 + h4, 0, Lc2, 21)
   factory.addPoint(R2, h1 + h3, 0, Lc2, 22)
   factory.addPoint(0, h1 + h3, 0, Lc2, 23)
   
   factory.addPoint(0, h1 + h3 + h4 + R2, 0, Lc2, 24)
   factory.addPoint(0, h1 + h3 - R2, 0, Lc2, 25)
   
   factory.addLine(1, 17, 1)
   factory.addLine(17, 16, 2)
   # Gmsh也可以创建除线段外的其他曲线，例如样条曲线，B-样条曲线，圆弧，椭圆弧等。
   factory.addCircleArc(14, 15, 16, 3) #前三个参数分别为起点，圆心，终点，最后一个参数为编号。
   # 在内置几何内核中，圆弧的的角度应该始终 < Pi。而OpenCASCADE则没有这个限制。
   factory.addLine(14, 13, 4)
   factory.addLine(13, 12, 5)
   factory.addLine(12, 11, 6)
   factory.addLine(11, 10, 7)
   factory.addCircleArc(8, 9, 10, 8)
   factory.addLine(8, 7, 9)
   factory.addLine(7, 6, 10)
   factory.addLine(6, 5, 11)
   factory.addCircleArc(3, 4, 5, 12)
   factory.addLine(3, 2, 13)
   factory.addLine(2, 1, 14)
   factory.addLine(18, 19, 15)
   factory.addCircleArc(21, 20, 24, 16)
   factory.addCircleArc(24, 20, 19, 17)
   factory.addCircleArc(18, 23, 25, 18)
   factory.addCircleArc(25, 23, 22, 19)
   factory.addLine(21, 22, 20)
   
   factory.addCurveLoop([17, -15, 18, 19, -20, 16], 21)
   factory.addPlaneSurface([21], 22)
   # 但是仍需要定义外部曲面，因为这个曲面有个洞，所以需要2个曲线循环来定义该曲面。
   factory.addCurveLoop([11, -12, 13, 14, 1, 2, -3, 4, 5, 6, 7, -8, 9, 10], 23)
   factory.addPlaneSurface([23, 21], 24)
   #如果曲面有n个洞，那么定义它需要n+1个曲线循环，第一个曲线循环定义外部边界，其余的定义洞的边界。
   factory.synchronize()
   
   v = gmsh.view.add("comments") #创建一个后处理视图，此时GUI并没有变化
   #注释分为3D和2D的，根据给定的坐标的维度来决定，3维注释是固定在模型中某个点的，2维注释是固定在屏幕上的某个位置的。
   gmsh.view.addListDataString(v, [10, -10], ["Created with Gmsh"]) #在视图v的屏幕坐标10,-10的位置上添加一个字符串注释。向右为x轴正向，向下为y轴正向，-数代表从反向算起。因此10,-10标识左下角的一个点。
   gmsh.view.addListDataString(v, [0, 0.11, 0], ["Hole"], ["Align", "Center", "Font", "Helvetica"]) #最后一个参数为样式，支持的有字体种类，大小和对齐方式。
   
   # 如果字符串以 file://开头，则后续的内容会被解析为一个图片文件，对于3维注释，图片的大小可以通过在路径的末尾添加@widthxheight来指明长宽的缩放比例，如果其中一个是0，则表示自动根据另一个自动确定，只会进行等比例缩放，如果都是0，则使用原始尺寸。
   png = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 't4_image.png') #通过当前的.py文件获取所在的目录路径，然后通过操作系统的父路径符，组合起来目录和文件。
   gmsh.view.addListDataString(v, [0, 0.09, 0], ["file://" + png + "@0.01x0"], ["Align", "Center"]) #宽度为默认的0.01倍
   
   gmsh.view.addListDataString(v, [-0.01, 0.09, 0], ["file://" + png + "@0.01x0,0,0,1,0,1,0"])# 3维注释可以指定底部和左侧的方向，出现在缩放比例的后面
   
   gmsh.view.addListDataString(v, [0, 0.12, 0], ["file://" + png + "@0.01x0#"], ["Align", "Center"]) #也可以使用#让图片以告示牌的方式显示，也就是总是和相机平行，面对着用户。
   
   gmsh.view.addListDataString(v, [150, -7], ["file://" + png + "@20x0"]) #2维注释的大小可以直接以像素形式给出。
   
   # 这些注释都是由一个基于列表的后处理视图来处理的，对于大规模的后处理数据集，例如包含定义在网格上的真实场数据，应该使用基于模型的后处理视图，它允许高效地存储连续和不来内需的各种标量，向量和张量场，或者任意阶多项式。
   
   # 视图和几何实体都可以设置对双击事件产生响应。
   gmsh.view.option.setString(v, "DoubleClickedCommand", "Printf('View[0] has been double-clicked!');")
   
   gmsh.option.setString(
       "Geometry.DoubleClickedLineCommand",
       "Printf('Curve %g has been double-clicked!', "
       "Geometry.DoubleClickedEntityTag);")
   
   #可以设置几何实体的颜色
   gmsh.model.setColor([(2, 22)], 127, 127, 127)  # 50度灰
   gmsh.model.setColor([(2, 24)], 160, 32, 240)  # 紫色
   gmsh.model.setColor([(1, i) for i in range(1, 15)], 255, 0, 0)  #批量修改，红色
   gmsh.model.setColor([(1, i) for i in range(15, 21)], 255, 255, 0)  # 黄色
   
   gmsh.model.mesh.generate(2)
   gmsh.write("t4.msh")
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 网格尺寸，带洞的体积

1. ```python
   import gmsh
   import math
   import sys
   
   gmsh.initialize()
   gmsh.model.add("t5")
   
   lcar1 = .1
   lcar2 = .0005
   lcar3 = .055
   
   # 如果想要全局地修改网格尺寸，可以维所有网格尺寸设置一个全局缩放因子。
   gmsh.option.setNumber("Mesh.MeshSizeFactor", 0.1)# 也可以通过命令行参数设置 python t5.py -clscale 0.2。相当网格尺寸缩小为原来的1/5，则单元数量会大概为原来的5^3倍。具体统计信息可以通过GUI的Tools->Statistics查看。
   
   # 定义基础实体，创建一个截去一个角的立方体。
   gmsh.model.geo.addPoint(0.5, 0.5, 0.5, lcar2, 1)
   gmsh.model.geo.addPoint(0.5, 0.5, 0, lcar1, 2)
   gmsh.model.geo.addPoint(0, 0.5, 0.5, lcar1, 3)
   gmsh.model.geo.addPoint(0, 0, 0.5, lcar1, 4)
   gmsh.model.geo.addPoint(0.5, 0, 0.5, lcar1, 5)
   gmsh.model.geo.addPoint(0.5, 0, 0, lcar1, 6)
   gmsh.model.geo.addPoint(0, 0.5, 0, lcar1, 7)
   gmsh.model.geo.addPoint(0, 1, 0, lcar1, 8)
   gmsh.model.geo.addPoint(1, 1, 0, lcar1, 9)
   gmsh.model.geo.addPoint(0, 0, 1, lcar1, 10)
   gmsh.model.geo.addPoint(0, 1, 1, lcar1, 11)
   gmsh.model.geo.addPoint(1, 1, 1, lcar1, 12)
   gmsh.model.geo.addPoint(1, 0, 1, lcar1, 13)
   gmsh.model.geo.addPoint(1, 0, 0, lcar1, 14)
   
   gmsh.model.geo.addLine(8, 9, 1)
   gmsh.model.geo.addLine(9, 12, 2)
   gmsh.model.geo.addLine(12, 11, 3)
   gmsh.model.geo.addLine(11, 8, 4)
   gmsh.model.geo.addLine(9, 14, 5)
   gmsh.model.geo.addLine(14, 13, 6)
   gmsh.model.geo.addLine(13, 12, 7)
   gmsh.model.geo.addLine(11, 10, 8)
   gmsh.model.geo.addLine(10, 13, 9)
   gmsh.model.geo.addLine(10, 4, 10)
   gmsh.model.geo.addLine(4, 5, 11)
   gmsh.model.geo.addLine(5, 6, 12)
   gmsh.model.geo.addLine(6, 2, 13)
   gmsh.model.geo.addLine(2, 1, 14)
   gmsh.model.geo.addLine(1, 3, 15)
   gmsh.model.geo.addLine(3, 7, 16)
   gmsh.model.geo.addLine(7, 2, 17)
   gmsh.model.geo.addLine(3, 4, 18)
   gmsh.model.geo.addLine(5, 1, 19)
   gmsh.model.geo.addLine(7, 8, 20)
   gmsh.model.geo.addLine(6, 14, 21)
   
   gmsh.model.geo.addCurveLoop([-11, -19, -15, -18], 22)
   gmsh.model.geo.addPlaneSurface([22], 23)
   gmsh.model.geo.addCurveLoop([16, 17, 14, 15], 24)
   gmsh.model.geo.addPlaneSurface([24], 25)
   gmsh.model.geo.addCurveLoop([-17, 20, 1, 5, -21, 13], 26)
   gmsh.model.geo.addPlaneSurface([26], 27)
   gmsh.model.geo.addCurveLoop([-4, -1, -2, -3], 28)
   gmsh.model.geo.addPlaneSurface([28], 29)
   gmsh.model.geo.addCurveLoop([-7, 2, -5, -6], 30)
   gmsh.model.geo.addPlaneSurface([30], 31)
   gmsh.model.geo.addCurveLoop([6, -9, 10, 11, 12, 21], 32)
   gmsh.model.geo.addPlaneSurface([32], 33)
   gmsh.model.geo.addCurveLoop([7, 3, 8, 9], 34)
   gmsh.model.geo.addPlaneSurface([34], 35)
   gmsh.model.geo.addCurveLoop([-10, 18, -16, -20, 4, -8], 36)
   gmsh.model.geo.addPlaneSurface([36], 37)
   gmsh.model.geo.addCurveLoop([-14, -13, -12, 19], 38)
   gmsh.model.geo.addPlaneSurface([38], 39)
   
   shells = [] #用来存储外部面和每个球的SurfaceLoop
   
   sl = gmsh.model.geo.addSurfaceLoop([35, 31, 29, 37, 33, 23, 39, 25, 27])
   shells.append(sl) #sl为创建的SurfaceLoop的编号，整数类型。先把外部面循环添加进去
   
   def cheeseHole(x, y, z, r, lc, shells):
       # 在体积内创建一个球形的洞，不手动指定编号，让函数来返回它们。
       p1 = gmsh.model.geo.addPoint(x, y, z, lc)
       p2 = gmsh.model.geo.addPoint(x + r, y, z, lc)
       p3 = gmsh.model.geo.addPoint(x, y + r, z, lc)
       p4 = gmsh.model.geo.addPoint(x, y, z + r, lc)
       p5 = gmsh.model.geo.addPoint(x - r, y, z, lc)
       p6 = gmsh.model.geo.addPoint(x, y - r, z, lc)
       p7 = gmsh.model.geo.addPoint(x, y, z - r, lc)
   
       c1 = gmsh.model.geo.addCircleArc(p2, p1, p7)
       c2 = gmsh.model.geo.addCircleArc(p7, p1, p5)
       c3 = gmsh.model.geo.addCircleArc(p5, p1, p4)
       c4 = gmsh.model.geo.addCircleArc(p4, p1, p2)
       c5 = gmsh.model.geo.addCircleArc(p2, p1, p3)
       c6 = gmsh.model.geo.addCircleArc(p3, p1, p5)
       c7 = gmsh.model.geo.addCircleArc(p5, p1, p6)
       c8 = gmsh.model.geo.addCircleArc(p6, p1, p2)
       c9 = gmsh.model.geo.addCircleArc(p7, p1, p3)
       c10 = gmsh.model.geo.addCircleArc(p3, p1, p4)
       c11 = gmsh.model.geo.addCircleArc(p4, p1, p6)
       c12 = gmsh.model.geo.addCircleArc(p6, p1, p7)
   
       l1 = gmsh.model.geo.addCurveLoop([c5, c10, c4])
       l2 = gmsh.model.geo.addCurveLoop([c9, -c5, c1])
       l3 = gmsh.model.geo.addCurveLoop([c12, -c8, -c1])
       l4 = gmsh.model.geo.addCurveLoop([c8, -c4, c11])
       l5 = gmsh.model.geo.addCurveLoop([-c10, c6, c3])
       l6 = gmsh.model.geo.addCurveLoop([-c11, -c3, c7])
       l7 = gmsh.model.geo.addCurveLoop([-c2, -c7, -c12])
       l8 = gmsh.model.geo.addCurveLoop([-c6, -c9, c2])
       #这里需要非平面的曲面来定义球的表面，使用gmsh.model.geo.addSurfaceFilling()来完成，可以创建使用3或4条曲线作为边界的曲面。如果曲线是同心的圆弧，则会构建一个由这些圆弧围起来的球面，否则会使用超限插值，它不同于经典的只在有限个特征点上重合的插值方法，超限插值的结果和原来数据在无穷多个点上都重合。
       # 对于OpenCASCADE内核，gmsh.model.occ.addSurfaceFilling()可以使用任意数量的边界曲线，会生成一个B样条曲线来通过他们。
       s1 = gmsh.model.geo.addSurfaceFilling([l1])
       s2 = gmsh.model.geo.addSurfaceFilling([l2])
       s3 = gmsh.model.geo.addSurfaceFilling([l3])
       s4 = gmsh.model.geo.addSurfaceFilling([l4])
       s5 = gmsh.model.geo.addSurfaceFilling([l5])
       s6 = gmsh.model.geo.addSurfaceFilling([l6])
       s7 = gmsh.model.geo.addSurfaceFilling([l7])
       s8 = gmsh.model.geo.addSurfaceFilling([l8])
   
       sl = gmsh.model.geo.addSurfaceLoop([s1, s2, s3, s4, s5, s6, s7, s8])
       v = gmsh.model.geo.addVolume([sl]) #每个球也会创建体积
       shells.append(sl)
       return v
   
   x = 0
   y = 0.75
   z = 0
   r = 0.09
   for t in range(1, 6): #在立方体内创建5个球
       x += 0.166
       z += 0.166
       v = cheeseHole(x, y, z, r, lcar3, shells)
       gmsh.model.geo.addPhysicalGroup(3, [v], t)
   
   gmsh.model.geo.addVolume(shells, 186) #创建去除5个球后的体积，需要使用6个曲面循环，第一个是外部曲面，其余是描述每个球的曲面循环。
   gmsh.model.geo.synchronize()
   
   # 如果使用OpenCASCADE内核的实体建模，同样的几何，方法却不一样，见t16.py
   # 最终定义一个体积物理组包含去除洞后的体积。
   gmsh.model.addPhysicalGroup(3, [186], 10)
   
   # 可以只显示模型的一部分，来只对这个子集划分网格。
   ent = gmsh.model.getEntities()#获取全体实体，可以提供一个维度参数，如果不提供则返回所有维度的所有实体。
   gmsh.model.setVisibility(ent, False) #关闭所有实体的显示
   gmsh.model.setVisibility([(3, 5)], True, True)# 只显示特定实体
   gmsh.option.setNumber("Mesh.MeshOnlyVisible", 1) #只对显示部分划分网格
   
   gmsh.option.setNumber("Mesh.Algorithm", 6)# 设置全局网格划分算法，6表示Frontal-Delaunay算法。
   gmsh.model.mesh.setAlgorithm(2, 33, 1) #也可以为某个单独的曲面[2,33]设置单独的MeshAdapt算法，这里用1表示，目前支支持2维的情况。
   # 为了生成曲边网格，优化它，使之能产生可证明有效的曲边单元，可以使用以下选项。
   gmsh.option.setNumber("Mesh.ElementOrder", 2) # 2阶单元的边是二次的，可以弯曲
   gmsh.option.setNumber("Mesh.HighOrderOptimize", 2)
   
   gmsh.model.mesh.generate(3)
   gmsh.write("t5.msh")
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 移动网格，删除实体

1. ```python
   import gmsh
   import math
   import sys
   
   gmsh.initialize()
   gmsh.model.add("t6")
   
   # 从t1.py复制
   lc = 1e-2
   gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
   gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
   gmsh.model.geo.addPoint(.1, .3, 0, lc, 3)
   gmsh.model.geo.addPoint(0, .3, 0, lc, 4)
   gmsh.model.geo.addLine(1, 2, 1)
   gmsh.model.geo.addLine(3, 2, 2)
   gmsh.model.geo.addLine(3, 4, 3)
   gmsh.model.geo.addLine(4, 1, 4)
   gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
   gmsh.model.geo.addPlaneSurface([1], 1)
   
   gmsh.model.geo.remove([(2, 1), (1, 4)]) #删除面和左侧的线
   p1 = gmsh.model.geo.addPoint(-0.05, 0.05, 0, lc)
   p2 = gmsh.model.geo.addPoint(-0.05, 0.1, 0, lc)
   l1 = gmsh.model.geo.addLine(1, p1)
   l2 = gmsh.model.geo.addLine(p1, p2)
   l3 = gmsh.model.geo.addLine(p2, 4)
   
   gmsh.model.geo.addCurveLoop([2, -1, l1, l2, l3, -3], 2)
   gmsh.model.geo.addPlaneSurface([-2], 1)
   
   gmsh.model.geo.mesh.setTransfiniteCurve(2, 20) #这里明确指定曲线上节点的位置，第一个参数为曲线编号，第二个参数指明要均匀生成20个点，包括起止点在内。
   # 右侧的曲线2有20个点，也就是分成了19段，因此左侧的3条曲线也要分成19段，所以5+5+9=19
   gmsh.model.geo.mesh.setTransfiniteCurve(l1, 6)
   gmsh.model.geo.mesh.setTransfiniteCurve(l2, 6)
   gmsh.model.geo.mesh.setTransfiniteCurve(l3, 10)
   
   # 最终，在线1和3上以等比级数的方式放置了30个点
   gmsh.model.geo.mesh.setTransfiniteCurve(1, 30, "Progression", -1.2) #最后一个参数是等比级数的公比，负数表示曲线方向要反向，这是因为曲线1和曲线3的方向是相反的。不可以将第一个参数设为-1，最后一个参数设为1.2。
   gmsh.model.geo.mesh.setTransfiniteCurve(3, 30, "Progression", 1.2)
   
   # setTransfiniteSurface划分网格的约束，使用一种超限插值的算法在曲线的参数平面中，通过结构化的网格(grid)来连接边界上的节点。如果曲面超过了4个角点，则超限插值的角点需要手动指定。
   gmsh.model.geo.mesh.setTransfiniteSurface(1, "Left", [1, 2, 3, 4])# 第一个参数为已有的surface的编号，第二个参数是当曲面没有被标记为重组时，如何排列三角形，可以取值Left，Right，AlternateLeft或AlternateRight。
   # 当曲面的边界上只有3或4个点，则角点的列表可以在调用setTransfiniteSurface()时被省略。
   # 超限插值会被映射为正三角形或正方形，
   gmsh.model.geo.mesh.setRecombine(2, 1) #重组编号为1的曲面，为了创建四边形而非三角形，可以使用setRecombine约束。
   gmsh.model.geo.addPoint(0.2, 0.2, 0, 1.0, 7)
   gmsh.model.geo.addPoint(0.2, 0.1, 0, 1.0, 8)
   gmsh.model.geo.addPoint(0.25, 0.2, 0, 1.0, 9)
   gmsh.model.geo.addPoint(0.3, 0.1, 0, 1.0, 10)
   gmsh.model.geo.addLine(8, 10, 10)
   gmsh.model.geo.addLine(10, 9, 11)
   gmsh.model.geo.addLine(9, 7, 12)
   gmsh.model.geo.addLine(7, 8, 13)
   gmsh.model.geo.addCurveLoop([13, 10, 11, 12], 14)
   gmsh.model.geo.addPlaneSurface([14], 15)
   for i in range(10, 14):
       gmsh.model.geo.mesh.setTransfiniteCurve(i, 10)
   gmsh.model.geo.mesh.setTransfiniteSurface(15)
   gmsh.model.geo.mesh.setTransfiniteSurface(15, "Alternate")# 生成三角形的方式，可以被该函数的第二个参数来控制，可以取值Left，Right和Alternate。
   gmsh.model.geo.synchronize()
   gmsh.option.setNumber("Mesh.Smoothing", 100)# 应用一个椭圆光华去在网格上，来得到更规则的网格
   gmsh.model.mesh.generate(2)
   gmsh.write("t6.msh")
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 背景网格

1. ```python
   import gmsh
   import os
   import sys
   
   # 网格大小可以通过提供一个背景网格的方式来精确指定，例如一个包含目标网格尺寸的后处理视图
   gmsh.initialize()
   path = os.path.dirname(os.path.abspath(__file__))
   gmsh.merge(os.path.join(path, os.pardir, 't7_bgmesh.pos')) #合并一个基于列表的包含目标网格尺寸的后处理视图，会在左侧树状菜单下Post-Processing中添加一个子项。
   #这个后处理视图本质上就是标量三角形格式，例如ST(0.077999455,0.23524011,0,0.068887619,0.23816425,0,0.069899638,0.22912552,0){0.01189957,0.011832084,0.0079913397}; ()内的9个数，分别表示三角形的三个点的xyz坐标，{}内的三个数表示三角形的三个点的标量值。虽然说它是自带网格的，但是这里将它当作背景网格，并不是使用它的网格来作为参考创建新的网格，而是用它在自己网格点上的值来作为网格尺寸场，可以看到这个后处理视图的取值范围为[0.001,0.022]，因此划分出的网格的尺寸取值范围也是这个。
   # 如果后处理视图是基于模型的而非列表，例如它是基于真实网格的，则需要创建一个新的模型，来包含几何，这样在对它划分网格时，不会破坏背景网格，在这里没有必要，因为这个视图是基于列表的，但是也没有害处。
   gmsh.model.add("t7")
   # 创建一个简单的矩形几何
   lc = 1e-2
   gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
   gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
   gmsh.model.geo.addPoint(.1, .3, 0, lc, 3)
   gmsh.model.geo.addPoint(0, .3, 0, lc, 4)
   gmsh.model.geo.addLine(1, 2, 1)
   gmsh.model.geo.addLine(3, 2, 2)
   gmsh.model.geo.addLine(3, 4, 3)
   gmsh.model.geo.addLine(4, 1, 4)
   gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
   gmsh.model.geo.addPlaneSurface([1], 1)
   gmsh.model.geo.synchronize()
   
   bg_field = gmsh.model.mesh.field.add("PostView")# 增加一个新的尺寸场
   gmsh.model.mesh.field.setNumber(bg_field, "ViewIndex", 0)# 将尺寸场和刚才merge的视图关联起来。
   gmsh.model.mesh.field.setAsBackgroundMesh(bg_field) # 将这个场应用为当前背景网格
   
   # 为了仅从背景网格计算网格尺寸，且不考虑其他所有的尺寸约束，可以设置如下，这样无论如何修改lc，都不会改变生成的网格。
   gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
   gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
   gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)
   
   # 可以查看t10.py，背景网格实际上是通用网格场的一种特例。
   gmsh.model.mesh.generate(2)
   gmsh.write("t7.msh")
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```

## 后处理，图片导出和动画

1. ```python
   import gmsh
   import os
   import sys
   
   # 除了创建几何和网格，API还可以用来操作后处理数据集，也就是Gmsh中的views。
   gmsh.initialize()
   
   # 先创建一个简单的几何
   lc = 1e-2
   gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
   gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
   gmsh.model.geo.addPoint(.1, .3, 0, lc, 3)
   gmsh.model.geo.addPoint(0, .3, 0, lc, 4)
   gmsh.model.geo.addLine(1, 2, 1)
   gmsh.model.geo.addLine(3, 2, 2)
   gmsh.model.geo.addLine(3, 4, 3)
   gmsh.model.geo.addLine(4, 1, 4)
   gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
   gmsh.model.geo.addPlaneSurface([1], 1)
   
   gmsh.model.geo.synchronize()
   
   # 合并一些后处理视图
   path = os.path.dirname(os.path.abspath(__file__))
   gmsh.merge(os.path.join(path, os.pardir, 'view1.pos')) #这个后处理视图中也是标量三角形，但是它含有5个时间步，因此每个三角形的数值部分有3*5=15个数。
   gmsh.merge(os.path.join(path, os.pardir, 'view1.pos'))
   gmsh.merge(os.path.join(path, os.pardir, 'view4.pos'))  #内部包含2个视图
   
   # Gmsh可以读取多种格式的后处理视图，view1.pos和view4.pos是Gmsh解析过的格式，可以使用GEO脚本解析器来解释。解析过的格式只应该用于相对较小的数据集。对于大的数据集，使用例如MSH文件则更高效。后处理试图可以通过API来直接创建。
   # We then set some general options:
   gmsh.option.setNumber("General.Trackball", 0)
   gmsh.option.setNumber("General.RotationX", 0)
   gmsh.option.setNumber("General.RotationY", 0)
   gmsh.option.setNumber("General.RotationZ", 0)
   
   white = (255, 255, 255)
   black = (0, 0, 0)
   
   # 颜色选项，setColor函数第一个参数都省略了中间的Color.
   gmsh.option.setColor("General.Background", white[0], white[1], white[2])
   gmsh.option.setColor("General.Foreground", black[0], black[1], black[2])
   gmsh.option.setColor("General.Text", black[0], black[1], black[2])
   
   gmsh.option.setNumber("General.Orthographic", 0)
   gmsh.option.setNumber("General.Axes", 0)
   gmsh.option.setNumber("General.SmallAxes", 0)
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.initialize()
   
   # 如果我们盲目地遵循geo例子，会从相关选项值中读取视图的数量，和使用gmsh.option.setNumber和gmsh.option.setString函数。一种更好的方法是使用gmsh.view.getTags，gmsh.view.option.setNumber()和gmsh.view.option.setString函数。
   
   v = gmsh.view.getTags() #获取所有视图的编号，返回一个包含整数的向量
   if len(v) != 4:
       gmsh.logger.write("Wrong number of views!", "error")
       gmsh.finalize()
       exit()
   
   # 为每一个后处理视图设置一些选项
   gmsh.view.option.setNumber(v[0], "IntervalsType", 2)
   gmsh.view.option.setNumber(v[0], "OffsetZ", 0.05)
   gmsh.view.option.setNumber(v[0], "RaiseZ", 0)
   gmsh.view.option.setNumber(v[0], "Light", 1)
   gmsh.view.option.setNumber(v[0], "ShowScale", 0)
   gmsh.view.option.setNumber(v[0], "SmoothNormals", 1)
   
   gmsh.view.option.setNumber(v[1], "IntervalsType", 1)
   # 注意，还不能在API中设置颜色表
   gmsh.view.option.setNumber(v[1], "NbIso", 10)
   gmsh.view.option.setNumber(v[1], "ShowScale", 0)
   
   gmsh.view.option.setString(v[2], "Name", "Test...")
   gmsh.view.option.setNumber(v[2], "Axes", 1)
   gmsh.view.option.setNumber(v[2], "IntervalsType", 2)
   gmsh.view.option.setNumber(v[2], "Type", 2)
   gmsh.view.option.setNumber(v[2], "AutoPosition", 0)
   gmsh.view.option.setNumber(v[2], "PositionX", 85)
   gmsh.view.option.setNumber(v[2], "PositionY", 50)
   gmsh.view.option.setNumber(v[2], "Width", 200)
   gmsh.view.option.setNumber(v[2], "Height", 130)
   
   gmsh.view.option.setNumber(v[3], "Visible", 0)
   
   # 可以通过GUI中的File->Export来直接保存为MPEG格式。一些预定义的动画被设置用来循环视图中的所有时间步或者在视图之间循环。
   # 但是API可以通过在运行时和重新渲染时修改选项，来创建更加复杂的动画。每一帧可以被保存为一张图片，多个帧就可以编码为一个视频了，下面是一个例子：
   t = 0  # 初始时间步
   for num in range(1, 4):
       for vv in v:
           gmsh.view.option.setNumber(vv, "TimeStep", t) #设置时间步
       current_step = gmsh.view.option.getNumber(v[0], "TimeStep")
       max_step = gmsh.view.option.getNumber(v[0], "NbTimeStep") - 1
       if current_step < max_step:
           t = t + 1
       else:
           t = 0
       gmsh.view.option.setNumber(v[0], "RaiseZ", gmsh.view.option.getNumber(v[0], "RaiseZ") + 0.01 / gmsh.view.option.getNumber(v[0], "Max") * t)
       if num == 3:
           # 当num==3时，缩放图片，创建一个640x480的帧
           gmsh.option.setNumber("General.GraphicsWidth", gmsh.option.getNumber("General.MenuWidth") + 640)
           gmsh.option.setNumber("General.GraphicsHeight", 480)
       frames = 50
       for num2 in range(frames):
           # 逐步旋转场景
           gmsh.option.setNumber("General.RotationX", gmsh.option.getNumber("General.RotationX") + 10)
           gmsh.option.setNumber("General.RotationY", gmsh.option.getNumber("General.RotationX") / 3)
           gmsh.option.setNumber("General.RotationZ", gmsh.option.getNumber("General.RotationZ") + 0.1)
           gmsh.graphics.draw() #绘制场景
           if num == 3:
               # 如下几行可以将每一帧都保存为一张图片
               gmsh.write("t8-{}.gif".format(num2))
               gmsh.write("t8-{}.ppm".format(num2))
               gmsh.write("t8-{}.jpg".format(num2))
       if num == 3:
           # 可以使用ffmpeg来生成视频
           import subprocess
           subprocess.call("ffmpeg -i t8-%d.jpg t8.mpg".split(' '))
           pass
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 插件

1. ```python
   import gmsh
   import os
   import sys
   
   # 可以添加插件来扩展Gmsh的功能，例如后处理插件可以修改视图，基于之前导入的视图来创建新视图，一些默认的插件是静态链接到Gmsh的，例如Isosurface, CutPlane, CutSphere, Skin, Transform 或 Smooth。插件可以通过gmsh.plugin开头的API来控制，或者通过在GUI的视图按钮中右键然后选择Plugins。
   gmsh.initialize()
   # 包含一个三维的标量视图
   path = os.path.dirname(os.path.abspath(__file__))
   gmsh.merge(os.path.join(path, os.pardir, 'view3.pos'))
   v = gmsh.view.getTags()
   if len(v) != 1:
       gmsh.logger.write("Wrong number of views!", "error")
       gmsh.finalize()
       exit()
   
   gmsh.plugin.setNumber("Isosurface", "Value", 0.67) #为Isosufrace插件设置一些参数，然后运行该插件，它会从3D标量视图中提取一个等值面。
   gmsh.plugin.setNumber("Isosurface", "View", 0)
   v1 = gmsh.plugin.run("Isosurface")
   
   # 为CutPlane插件设置一些选项，它会计算3D视图的一个截面，通过平面A*x+B*y+C*z+D=0。
   gmsh.plugin.setNumber("CutPlane", "A", 0)
   gmsh.plugin.setNumber("CutPlane", "B", 0.2)
   gmsh.plugin.setNumber("CutPlane", "C", 1)
   gmsh.plugin.setNumber("CutPlane", "D", 0)
   gmsh.plugin.setNumber("CutPlane", "View", 0)
   v2 = gmsh.plugin.run("CutPlane")
   
   # 增加一个标题，按照约定，对于窗口坐标，大于99999的值表示中心，也可以使用General.GraphicsWidth/2来表示中心，但是这只会将字符串在当前窗口居中。
   gmsh.plugin.setString("Annotate", "Text", "A nice title")
   gmsh.plugin.setNumber("Annotate", "X", 1.e5)
   gmsh.plugin.setNumber("Annotate", "Y", 50)
   gmsh.plugin.setString("Annotate", "Font", "Times-BoldItalic")
   gmsh.plugin.setNumber("Annotate", "FontSize", 28)
   gmsh.plugin.setString("Annotate", "Align", "Center")
   gmsh.plugin.setNumber("Annotate", "View", 0)
   gmsh.plugin.run("Annotate")
   
   gmsh.plugin.setString("Annotate", "Text", "(and a small subtitle)")
   gmsh.plugin.setNumber("Annotate", "Y", 70)
   gmsh.plugin.setString("Annotate", "Font", "Times-Roman")
   gmsh.plugin.setNumber("Annotate", "FontSize", 12)
   gmsh.plugin.run("Annotate")
   
   gmsh.view.option.setNumber(v[0], "Light", 1)
   gmsh.view.option.setNumber(v[0], "IntervalsType", 1)
   gmsh.view.option.setNumber(v[0], "NbIso", 6)
   gmsh.view.option.setNumber(v[0], "SmoothNormals", 1)
   gmsh.view.option.setNumber(v1, "IntervalsType", 2)
   gmsh.view.option.setNumber(v2, "IntervalsType", 2)
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```

## 网格尺寸场

1. ```python
   # 为了在几何的某些点上指定目标网格尺寸(t1.py)或者使用一个背景网格(t7.py)，可以使用通用的网格尺寸场。
   import gmsh
   import sys
   
   gmsh.initialize(sys.argv)
   gmsh.model.add("t10")
   # 创建一个简单的矩形几何
   lc = .15
   gmsh.model.geo.addPoint(0.0, 0.0, 0, lc, 1)
   gmsh.model.geo.addPoint(1, 0.0, 0, lc, 2)
   gmsh.model.geo.addPoint(1, 1, 0, lc, 3)
   gmsh.model.geo.addPoint(0, 1, 0, lc, 4)
   gmsh.model.geo.addPoint(0.2, .5, 0, lc, 5)
   
   gmsh.model.geo.addLine(1, 2, 1)
   gmsh.model.geo.addLine(2, 3, 2)
   gmsh.model.geo.addLine(3, 4, 3)
   gmsh.model.geo.addLine(4, 1, 4)
   
   gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 5)
   gmsh.model.geo.addPlaneSurface([5], 6)
   
   gmsh.model.geo.synchronize()
   # 想要使得网格单元尺寸在曲线2和点5附近为lc/30，其他地方为lc，首先定义了一个Distance场，这个场中每个点的取值是该点到到点5和曲线2的距离（这里会将该在曲线上采样100个点，以此来等效曲线，提高计算效率，曲面也会这么处理，不过该数值是每个维度的离散数量）。到一个曲线距离为常数的点也构成一条与该曲线平行的曲线。
   gmsh.model.mesh.field.add("Distance", 1) #新增一个Distance场
   gmsh.model.mesh.field.setNumbers(1, "PointsList", [5]) #设置该场的参数
   gmsh.model.mesh.field.setNumbers(1, "CurvesList", [2])
   gmsh.model.mesh.field.setNumber(1, "Sampling", 100)
   #这里对Distance场进一步处理，当输入<DistMin时，输出为SizeMin，当输入>DistMax时，输出为SizeMax，当输入在(DistMin,DistMax)之间时，使用SizeMin和SizeMax的插值。
   gmsh.model.mesh.field.add("Threshold", 2)
   gmsh.model.mesh.field.setNumber(2, "InField", 1) #想要进行处理的场的编号，通常是Distance类型的。
   gmsh.model.mesh.field.setNumber(2, "SizeMin", lc / 30)
   gmsh.model.mesh.field.setNumber(2, "SizeMax", lc)
   gmsh.model.mesh.field.setNumber(2, "DistMin", 0.15)
   gmsh.model.mesh.field.setNumber(2, "DistMax", 0.5)
   # gmsh.model.mesh.field.setNumber(2,"Sigmoid",1) #是否启用Sigmoid对输入进行渐变处理，而非线性插值。
   # 可以使用点的空间坐标x,y,z的数学函数来设置该点的网格尺寸场的取值，这里用MathEval场。
   gmsh.model.mesh.field.add("MathEval", 3)
   gmsh.model.mesh.field.setString(3, "F", "cos(4*3.14*x) * sin(4*3.14*y) / 10 + 0.101") #之所以最后加上个0.101，是因为前面的取值范围为[-0.1,0.1]，加上之后就可以保证场的值是恒正得了。
   # 可以在MathEval中引用其他已经定义的场
   gmsh.model.mesh.field.add("Distance", 4)
   gmsh.model.mesh.field.setNumbers(4, "PointsList", [1])
   gmsh.model.mesh.field.add("MathEval", 5)
   gmsh.model.mesh.field.setString(5, "F", "F4^3 + " + str(lc / 100)) #这里的F的值中的F4是指编号为4的场。
   # 使用xyz三个轴的最大和最小值来定义一个盒子，当点在盒子内时，取值为VIn，否则为VOut。如果Thicknes不为0，则会在盒子的边界上的一定厚度区域内逐渐变化场的取值。
   gmsh.model.mesh.field.add("Box", 6)
   gmsh.model.mesh.field.setNumber(6, "VIn", lc / 15)
   gmsh.model.mesh.field.setNumber(6, "VOut", lc)
   gmsh.model.mesh.field.setNumber(6, "XMin", 0.3)
   gmsh.model.mesh.field.setNumber(6, "XMax", 0.6)
   gmsh.model.mesh.field.setNumber(6, "YMin", 0.3)
   gmsh.model.mesh.field.setNumber(6, "YMax", 0.6)
   gmsh.model.mesh.field.setNumber(6, "Thickness", 0.3)
   # 也可以直接从GUI的Mesh->Define->Size fields来创建尺寸场。
   gmsh.model.mesh.field.add("Min", 7)# 这个场会取FieldsList的所有的场的最小值，这样可以起到局部加密的作用。
   gmsh.model.mesh.field.setNumbers(7, "FieldsList", [2, 3, 5, 6])
   gmsh.model.mesh.field.setAsBackgroundMesh(7) #只有在这里设置的场才会被当作背景网格。
   
   def meshSizeCallback(dim, tag, x, y, z, lc):
       return min(lc, 0.02 * x + 0.01)
   
   gmsh.model.mesh.setSizeCallback(meshSizeCallback) #设置全局网格尺寸回调函数，每次需要网格尺寸的时候，都会调用这个函数。它会和背景网格同时起作用，哪个取值小哪个就控制。
   
   # 为了确定网格单元的尺寸，Gmsh会局部地计算以下几个场的最小值，
   # 1) 模型的包围盒的尺寸
   # 2) 如果Mesh.MeshSizeFromPoints为1，则会考虑定义点是时给定的网格尺寸。
   # 3) 如果Mesh.MeshSizeFromCurvature是正数，则网格尺寸会基于曲率来计算，将2*pi弧度划分为这个正数个分段。
   # 4) 背景网格尺寸场
   # 5) 任意其他的和实体相关的尺寸
   # 这个值可以进一步被网格尺寸回调函数修改，如果存在的话。在这之后，还会被约束到[Mesh.MeshSizeMin, Mesh.MeshSizeMax]，再乘以Mesh.MeshSizeFactor缩放因子。还有就是边界网格尺寸默认会插值到内部的曲面或体积，可以通过设置Mesh.MeshSizeExtendFromBoundary为0来取消。
   # 如果网格尺寸完全由网格尺寸长来控制的话，一般会进行如下设置，来取消几何点或曲率的控制，取消从边界到内部的插值。这回避免出现过于精细的网格。
   gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
   gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
   gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)
   gmsh.option.setNumber("Mesh.Algorithm", 5) #默认的2D算法为Frontal-Delaunay(6)，它通常能获得最高的质量，而Delaunay(5)算法通常能较好地处理复杂网格尺寸场，尤其是该场内存在较大的梯度时。
   gmsh.model.mesh.generate(2)
   gmsh.write("t10.msh")
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 非结构四边形网格

1. ```python
   import gmsh
   import sys
   
   gmsh.initialize()
   gmsh.model.add("t11")
   # 非结构网格也可以像t3.py和t6.py那样重组，下面定义一个简单几何的解析网格场
   p1 = gmsh.model.geo.addPoint(-1.25, -.5, 0)
   p2 = gmsh.model.geo.addPoint(1.25, -.5, 0)
   p3 = gmsh.model.geo.addPoint(1.25, 1.25, 0)
   p4 = gmsh.model.geo.addPoint(-1.25, 1.25, 0)
   l1 = gmsh.model.geo.addLine(p1, p2)
   l2 = gmsh.model.geo.addLine(p2, p3)
   l3 = gmsh.model.geo.addLine(p3, p4)
   l4 = gmsh.model.geo.addLine(p4, p1)
   cl = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
   pl = gmsh.model.geo.addPlaneSurface([cl])
   gmsh.model.geo.synchronize()
   
   field = gmsh.model.mesh.field
   field.add("MathEval", 1)
   field.setString(1, "F", "0.01*(1.0+30.*(y-x*x)*(y-x*x) + (1-x)*(1-x))")
   field.setAsBackgroundMesh(1)
   
   gmsh.model.mesh.setRecombine(2, pl) #为了生成四边形而非三角形，可以使用这个函数
   gmsh.option.setNumber("Mesh.RecombineAll", 1) # 如果有多个面，可以使用全局选项
   # 默认的重组算法时Blossom，它使用一种最小花费完美匹配算法来从三角化网格中生成完全四边形网格。
   gmsh.option.setNumber("Mesh.Algorithm", 8)# 对于更好的2D平面四边形网格，可以尝试实验性的Frontal-Delaunay for quads算法，它是一种三角化算法，使得创建的几乎都是直角三角形。
   # 默认的重组算法可能在网格中剩余一些三角形，如果重组所有的三角形，可能会导致较差的网格质量。此时如果要生成完全四边形的网格，或者选择将得到的混合网格进行细分。
   # (Mesh.SubdivisionAlgorithm=1)，或者使用全四边形重组算法，它会在重组，光滑，细分后自动进行粗糙网格划分。
   gmsh.option.setNumber("Mesh.RecombinationAlgorithm", 2) # 或者取值为3
   gmsh.option.setNumber("Mesh.SubdivisionAlgorithm", 1) #也可以单独设置细分步骤
   gmsh.model.mesh.generate(2)
   # 也可以在网格划分完毕后，显式应用重组算法或细分步骤。
   gmsh.model.mesh.recombine() #这个与gmsh.model.mesh.setRecombine(2, pl)和gmsh.option.setNumber("Mesh.RecombineAll", 1)不一样，后两者只是设置，必须再重新划分网格后才会生效，而这个会直接进行重组。
   gmsh.option.setNumber("Mesh.SubdivisionAlgorithm", 1)# 细分算法1会将1个四边形变成4个四边形，1个三角形变成3个四边形。
   gmsh.model.mesh.refine()# 应用细分
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## Cross-patch meshing with compounds

1. ```python
   import gmsh
   import sys
   # 复合网格约束允许生成跨曲面边界的网格，有时从外部导入的CAD模型，会包含一些不想要的小特征，此时用这种方式进行划分非常有用。
   
   # When a `setCompound()' meshing constraint is given, at mesh generation time
   # Gmsh
   #  1. meshes the underlying elementary geometrical entities, individually
   #  2. creates a discrete entity that combines all the individual meshes
   #  3. computes a discrete parametrization (i.e. a piece-wise linear mapping)
   #     on this discrete entity
   #  4. meshes the discrete entity using this discrete parametrization instead
   #     of the underlying geometrical description of the underlying elementary
   #     entities making up the compound
   #  5. optionally, reclassifies the mesh elements and nodes on the original
   #     entities
   
   # Step 3. above can only be performed if the mesh resulting from the
   # combination of the individual meshes can be reparametrized, i.e. if the shape
   # is "simple enough". If the shape is not amenable to reparametrization, you
   # should create a full mesh of the geometry and first re-classify it to
   # generate patches amenable to reparametrization (see `t13.py').
   
   # The mesh of the individual entities performed in Step 1. should usually be
   # finer than the desired final mesh; this can be controlled with the
   # `Mesh.CompoundMeshSizeFactor' option.
   
   # The optional reclassification on the underlying elementary entities in Step
   # 5. is governed by the `Mesh.CompoundClassify' option.
   
   gmsh.initialize()
   lc = 0.1
   gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
   gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
   gmsh.model.geo.addPoint(1, 1, 0.5, lc, 3)
   gmsh.model.geo.addPoint(0, 1, 0.4, lc, 4)
   gmsh.model.geo.addPoint(0.3, 0.2, 0, lc, 5)
   gmsh.model.geo.addPoint(0, 0.01, 0.01, lc, 6)
   gmsh.model.geo.addPoint(0, 0.02, 0.02, lc, 7)
   gmsh.model.geo.addPoint(1, 0.05, 0.02, lc, 8)
   gmsh.model.geo.addPoint(1, 0.32, 0.02, lc, 9)
   gmsh.model.geo.addLine(1, 2, 1)
   gmsh.model.geo.addLine(2, 8, 2)
   gmsh.model.geo.addLine(8, 9, 3)
   gmsh.model.geo.addLine(9, 3, 4)
   gmsh.model.geo.addLine(3, 4, 5)
   gmsh.model.geo.addLine(4, 7, 6)
   gmsh.model.geo.addLine(7, 6, 7)
   gmsh.model.geo.addLine(6, 1, 8)
   gmsh.model.geo.addSpline([7, 5, 9], 9)
   gmsh.model.geo.addLine(6, 8, 10)
   gmsh.model.geo.addCurveLoop([5, 6, 9, 4], 11)
   gmsh.model.geo.addSurfaceFilling([11], 1)
   gmsh.model.geo.addCurveLoop([-9, 3, 10, 7], 13)
   gmsh.model.geo.addSurfaceFilling([13], 5)
   gmsh.model.geo.addCurveLoop([-10, 2, 1, 8], 15)
   gmsh.model.geo.addSurfaceFilling([15], 10)
   gmsh.model.geo.synchronize()
   
   gmsh.model.mesh.setCompound(1, [2, 3, 4]) #在划分网格时，将曲线2，3，4当作一条单独曲线，第一个参数是维度，只能合并同一维度的实体。这样网格就不会在8和9点上强制生成节点了。
   gmsh.model.mesh.setCompound(1, [6, 7, 8])
   gmsh.model.mesh.setCompound(2, [1, 5, 10])#在划分网格时，将曲面1，5，10当作一个单独的曲面，这样就不会在曲线9和10上强制生成节点了。
   # 合并的含义就是减少特征点和特征线，使用统一的参数来遍历多段曲线或曲面构成的整体。
   gmsh.model.mesh.generate(2)
   gmsh.write('t12.msh')
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 重新划分不包含底层CAD模型的STL文件

1. ```python
   import gmsh
   import math
   import os
   import sys
   gmsh.initialize()
   def createGeometryAndMesh():# 创建几何，然后划分网格
       # 清理所有的模型，从父目录合并一个STL网格，
       gmsh.clear()
       path = os.path.dirname(os.path.abspath(__file__))
       gmsh.merge(os.path.join(path, os.pardir, 't13_data.stl'))
       # 首先，通过将原始曲面沿着尖锐的几何特征来分类，这回创造一些离散的曲面，曲线和点。两个三角形之间的夹角如果大于指定的angle时会被认为是尖锐转角。
       angle = gmsh.onelab.getNumber('Parameters/Angle for surface detection')[0]# 从onelab中获取角度参数
       # 对于复杂几何，patch可能会太复杂，太细长或太大以至于无法参数化，设置如下选项将会强制创建可重参数化的patch。
       forceParametrizablePatches = gmsh.onelab.getNumber( 'Parameters/Create surfaces guaranteed to be parametrizable')[0]# 一个Boolean变量
       includeBoundary = True # 对于开放(非闭合)曲面，在分类过程中将包含边界上的边
       curveAngle = 180 #强制曲线在给定的角度上分割
       gmsh.model.mesh.classifySurfaces(angle * math.pi / 180., includeBoundary, forceParametrizablePatches, curveAngle * math.pi / 180.)# 这个函数的分类过程也被称为color上色过程，即相邻网格夹角小于特定角的网格区域会被着色成同一个颜色。如果第三个参数为True，则会创建可以被单个图重参数化的曲线和曲面。如果最后一个参数小于pi，则也会强制曲线根据curveAngle来分段。
       gmsh.model.mesh.createGeometry()# 为网格中所有的离散曲线和曲面创建几何，通过为每一个计算重参数化。
       #注意，如果一个CAD模型，例如存在可用的STEP文件，而非STL网格，通常使用CAD模型比通过网格重参数化的几何更好。实际上，CAD几何通常会更精确，有着更光滑的参数化，会导致更高效和质量更高的网格。在Gmsh中对离散曲面重新划分网格被优化取来处理稠密的STL网格，这一一般来自于图像系统，此时没有CAD模型可用。它不太适合通常由CAD工具生成的用于例如3D打印的低质量STL三角剖分（针对尺寸进行了优化，例如非常细长的三角形）。
       s = gmsh.model.getEntities(2)# 获取所有的曲面
       l = gmsh.model.geo.addSurfaceLoop([e[1] for e in s])#用所有的曲面创建一个曲面循环。
       gmsh.model.geo.addVolume([l]) #从所有的曲面创建一个体积
       gmsh.model.geo.synchronize()
       # 通过施加一个尺寸长来指定网格大小
       f = gmsh.model.mesh.field.add("MathEval")
       if gmsh.onelab.getNumber('Parameters/Apply funny mesh size field?')[0]:
           gmsh.model.mesh.field.setString(f, "F", "2*Sin((x+y)/5) + 3")
       else:
           gmsh.model.mesh.field.setString(f, "F", "4")
       gmsh.model.mesh.field.setAsBackgroundMesh(f)
       gmsh.model.mesh.generate(3)
       gmsh.write('t13.msh')
   # 创建一个ONELAB参数，用于重新划分网格
   gmsh.onelab.set("""[
     {
       "type":"number",
       "name":"Parameters/Angle for surface detection",
       "values":[40],
       "min":20,
       "max":120,
       "step":1
     },
     {
       "type":"number",
       "name":"Parameters/Create surfaces guaranteed to be parametrizable",
       "values":[0],
       "choices":[0, 1] #布尔值，会出现为复选框形式
     },
     {
       "type":"number",
       "name":"Parameters/Apply funny mesh size field?",
       "values":[0],
       "choices":[0, 1]
     }
   ]""")
   
   createGeometryAndMesh()
   def checkForEvent():
       action = gmsh.onelab.getString("ONELAB/Action")
       if len(action) and action[0] == "check":
           gmsh.onelab.setString("ONELAB/Action", [""])
           createGeometryAndMesh()
           gmsh.graphics.draw()
       return True
   if "-nopopup" not in sys.argv:
       gmsh.fltk.initialize()
       while gmsh.fltk.isAvailable() and checkForEvent():
           gmsh.fltk.wait()
   
   gmsh.finalize()
   ```


## 同调与上同调计算

1. ```python
   # Gmsh的同调计算使用模型的网格，寻找相对(上)同调空间的表示链，表示基链以物理组的方式存储在网格，每一个链作为一个物理组。
   import gmsh
   import sys
   gmsh.initialize(sys.argv)
   gmsh.model.add("t14")
   m = 0.5  # 网格尺寸
   h = 2  # z方向的几何高度
   gmsh.model.geo.addPoint(0, 0, 0, m, 1)
   gmsh.model.geo.addPoint(10, 0, 0, m, 2)
   gmsh.model.geo.addPoint(10, 10, 0, m, 3)
   gmsh.model.geo.addPoint(0, 10, 0, m, 4)
   gmsh.model.geo.addPoint(4, 4, 0, m, 5)
   gmsh.model.geo.addPoint(6, 4, 0, m, 6)
   gmsh.model.geo.addPoint(6, 6, 0, m, 7)
   gmsh.model.geo.addPoint(4, 6, 0, m, 8)
   gmsh.model.geo.addPoint(2, 0, 0, m, 9)
   gmsh.model.geo.addPoint(8, 0, 0, m, 10)
   gmsh.model.geo.addPoint(2, 10, 0, m, 11)
   gmsh.model.geo.addPoint(8, 10, 0, m, 12)
   gmsh.model.geo.addLine(1, 9, 1)
   gmsh.model.geo.addLine(9, 10, 2)
   gmsh.model.geo.addLine(10, 2, 3)
   gmsh.model.geo.addLine(2, 3, 4)
   gmsh.model.geo.addLine(3, 12, 5)
   gmsh.model.geo.addLine(12, 11, 6)
   gmsh.model.geo.addLine(11, 4, 7)
   gmsh.model.geo.addLine(4, 1, 8)
   gmsh.model.geo.addLine(5, 6, 9)
   gmsh.model.geo.addLine(6, 7, 10)
   gmsh.model.geo.addLine(7, 8, 11)
   gmsh.model.geo.addLine(8, 5, 12)
   gmsh.model.geo.addCurveLoop([6, 7, 8, 1, 2, 3, 4, 5], 13)
   gmsh.model.geo.addCurveLoop([11, 12, 9, 10], 14)
   gmsh.model.geo.addPlaneSurface([13, 14], 15)
   e = gmsh.model.geo.extrude([(2, 15)], 0, 0, h)
   gmsh.model.geo.synchronize()
   # 创建物理组，用来定义(上)同调计算的区域和相对(上)同调计算的子域。
   # 整体区域
   domain_tag = e[1][1]
   domain_physical_tag = 1001
   gmsh.model.addPhysicalGroup(3, [domain_tag], domain_physical_tag, "Whole domain")
   # 模型的4个terminals
   terminal_tags = [e[3][1], e[5][1], e[7][1], e[9][1]]# 四个角点的小面
   terminals_physical_tag = 2001
   gmsh.model.addPhysicalGroup(2, terminal_tags, terminals_physical_tag, "Terminals")
   boundary_dimtags = gmsh.model.getBoundary([(3, domain_tag)], False, False)# 获取体积的所有曲面边界
   boundary_tags = []
   complement_tags = []
   for tag in boundary_dimtags:
       complement_tags.append(tag[1])
       boundary_tags.append(tag[1])
   for tag in terminal_tags:
       complement_tags.remove(tag)# 去除4个角部的面后的其他剩余面
   
   # 求解域面的全集
   boundary_physical_tag = 2002
   gmsh.model.addPhysicalGroup(2, boundary_tags, boundary_physical_tag, "Boundary")
   # 相对于四个角部面的补集
   complement_physical_tag = 2003
   gmsh.model.addPhysicalGroup(2, complement_tags, complement_physical_tag, "Complement")
   
   # Find bases for relative homology spaces of the domain modulo the four
   # terminals.
   gmsh.model.mesh.addHomologyRequest("Homology", [domain_physical_tag], [terminals_physical_tag], [0, 1, 2, 3])# 第一次参数决定了是同调空间还是上同调空间，第二个参数要求以物理组列表的方式提供计算域。第三个方式以同样方式给出子域，如果为空则计算绝对的(上)同调。如果请求发生在网格生成前，则会在网格生成的最后进行计算。
   
   # Find homology space bases isomorphic to the previous bases: homology spaces
   # modulo the non-terminal domain surface, a.k.a the thin cuts.
   gmsh.model.mesh.addHomologyRequest("Homology", [domain_physical_tag], [complement_physical_tag], [0, 1, 2, 3])
   
   # Find cohomology space bases isomorphic to the previous bases: cohomology
   # spaces of the domain modulo the four terminals, a.k.a the thick cuts.
   gmsh.model.mesh.addHomologyRequest("Cohomology", [domain_physical_tag], [terminals_physical_tag], [0, 1, 2, 3])
   
   # more examples
   # gmsh.model.mesh.addHomologyRequest()
   # gmsh.model.mesh.addHomologyRequest("Homology", [domain_physical_tag])
   # gmsh.model.mesh.addHomologyRequest("Homology", [domain_physical_tag], [boundary_physical_tag], [0,1,2,3])
   
   # 生成网格，执行要求的同调计算。
   gmsh.model.mesh.generate(3)
   gmsh.write("t14.msh")
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 嵌入点，线，面

1. ```python
   # 默认情况下，如果低维实体位于高维实体的边界上（例如，点、曲线或曲面是体积边界的一部分），则Gmsh生成的跨几何维度网格才是共形的。嵌入约束允许强制网格与其他低维实体共形
   import gmsh
   import sys
   gmsh.initialize()
   lc = 1e-2
   gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
   gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
   gmsh.model.geo.addPoint(.1, .3, 0, lc, 3)
   gmsh.model.geo.addPoint(0, .3, 0, lc, 4)
   gmsh.model.geo.addLine(1, 2, 1)
   gmsh.model.geo.addLine(3, 2, 2)
   gmsh.model.geo.addLine(3, 4, 3)
   gmsh.model.geo.addLine(4, 1, 4)
   gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
   gmsh.model.geo.addPlaneSurface([1], 1)
   
   lc = lc * 4 #改变网格尺寸来生成一个更粗糙的网格
   gmsh.model.geo.mesh.setSize([(0, 1), (0, 2), (0, 3), (0, 4)], lc)
   gmsh.model.geo.addPoint(0.02, 0.02, 0., lc, 5)#定义一个新的点
   gmsh.model.geo.synchronize() #必须在嵌入是提前进行synchronize
   gmsh.model.mesh.embed(0, [5], 2, 1) #使用embed函数来讲这个点嵌入到2D网格中。前两个参数指明低维的实体，可以有多个，所以第二个参数是列表，后两个参数指明高维的实体，只能有一个。
   #低维嵌入高维后，就会在高维的网格的低维中增加约束，例如将一个点嵌入一条曲线，则该曲线的网格就会强制在该点生成一个节点。
   gmsh.model.geo.addPoint(0.02, 0.12, 0., lc, 6)
   gmsh.model.geo.addPoint(0.04, 0.18, 0., lc, 7)
   gmsh.model.geo.addLine(6, 7, 5)
   gmsh.model.geo.synchronize()
   gmsh.model.mesh.embed(1, [5], 2, 1)# 同样，也可以使用embed将曲线强制嵌入到一个2D网格中。
   gmsh.model.geo.extrude([(2, 1)], 0, 0, 0.1)
   p = gmsh.model.geo.addPoint(0.07, 0.15, 0.025, lc)
   gmsh.model.geo.synchronize()
   gmsh.model.mesh.embed(0, [p], 3, 1)# 点和曲线也可以嵌入到体积中。
   
   gmsh.model.geo.addPoint(0.025, 0.15, 0.025, lc, p + 1)
   l = gmsh.model.geo.addLine(7, p + 1)
   gmsh.model.geo.synchronize()
   gmsh.model.mesh.embed(1, [l], 3, 1)
   
   gmsh.model.geo.addPoint(0.02, 0.12, 0.05, lc, p + 2)
   gmsh.model.geo.addPoint(0.04, 0.12, 0.05, lc, p + 3)
   gmsh.model.geo.addPoint(0.04, 0.18, 0.05, lc, p + 4)
   gmsh.model.geo.addPoint(0.02, 0.18, 0.05, lc, p + 5)
   gmsh.model.geo.addLine(p + 2, p + 3, l + 1)
   gmsh.model.geo.addLine(p + 3, p + 4, l + 2)
   gmsh.model.geo.addLine(p + 4, p + 5, l + 3)
   gmsh.model.geo.addLine(p + 5, p + 2, l + 4)
   ll = gmsh.model.geo.addCurveLoop([l + 1, l + 2, l + 3, l + 4])
   s = gmsh.model.geo.addPlaneSurface([ll])
   gmsh.model.geo.synchronize()
   gmsh.model.mesh.embed(2, [s], 3, 1)# 可以将一个曲面嵌入到体积中
   
   # 使用OpenCASCADE内核时，当fragment()函数被应用到不同维度的实体时，较低维度的实体会被自动嵌入到高维的实体中，如果可能的话。
   gmsh.model.mesh.generate(3)
   gmsh.write("t15.msh")
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 构造实体几何，OpenCASCADE几何内核

1. ```python
   # 从Gmsh3开始，就允许用户使用其他几何内核了，这里使用OpenCASCADE内核。
   import gmsh
   import math
   import sys
   gmsh.initialize()
   gmsh.model.add("t16")
   # 这里会构建和t5.py相同的几何，不过使用过的是构造实体几何constructive solid geometry。
   # 可以记录下所有的消息以便后续处理
   gmsh.logger.start()
   # 首先创建2个立方体
   gmsh.model.occ.addBox(0, 0, 0, 1, 1, 1, 1)
   gmsh.model.occ.addBox(0, 0, 0, 0.5, 0.5, 0.5, 2)
   gmsh.model.occ.cut([(3, 1)], [(3, 2)], 3) #应用布尔差运算，结果是一个立方体减去了它的1/8。
   # OpenCASCADE的布尔运算总是会创建新的实体，默认情况，cut()函数的额外参数removeObject和removeTool都为True，也就是说会删除掉原来的实体。
   # 创建5个球
   x = 0
   y = 0.75
   z = 0
   r = 0.09
   holes = []
   for t in range(1, 6):
       x += 0.166
       z += 0.166
       gmsh.model.occ.addSphere(x, y, z, r, 3 + t)
       holes.append((3, 3 + t))
   # 如果需要5个球洞，可以直接使用cut来将它们删除，而这里需要保留球，而且它的网格需要和立方体的共形，也就是界面上的网格相同，因此使用fragment()，它会以共形的方式来求体积的交叉，这里的共形是指，在界面上不会产生2个重合的面，而是共用一个面。
   ov, ovv = gmsh.model.occ.fragment([(3, 3)], holes)
   # ov包含了所有的和输入实体维度相同生成的实体，是元组的列表
   print("fragment produced volumes:")
   for e in ov: #[(3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9)]
       print(e)
   
   # ovv包含了所有输入实体的父-子关系，是元组列表的列表。
   print("before/after fragment relations:")
   # zip函数每次会从每个参数中都取一个元素，构成一个元组，
   for e in zip([(3, 3)] + holes, ovv):#[[(3, 9), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],[(3, 4)],[(3, 5)],[(3, 6)],[(3, 7)],[(3, 8)]]
       print("parent " + str(e[0]) + " -> child " + str(e[1]))
   
   gmsh.model.occ.synchronize()
   # 当布尔操作导致实体的简单修改时，如果删除了原有的实体，则Gmsh会尝试给实体赋予相同的编号，这一行为由Geometry.OCCBooleanPreserveNumbering控制。
   #为每个球各自定义一个物理组，这里的5个编号已经不是原来创建的对应的球了，它们在fragment中已经被删除了，但是新创建的球的编号和原来的相同。
   for i in range(1, 6):
       gmsh.model.addPhysicalGroup(3, [3 + i], i)
   
   gmsh.model.addPhysicalGroup(3, [ov[-1][1]], 10) #立方体的编号会被改变，因此需要程序化地获取它。
   # 使用构造实体几何创建实体非常强大，但是会导致一些实际的问题，例如在点上设置网格尺寸或者识别边界。为了获得点或其他边界实体，可以利用getEntities，getBoundary和getEntitiesInBoundingBox等函数。
   lcar1 = .1
   lcar2 = .0005
   lcar3 = .055
   gmsh.model.mesh.setSize(gmsh.model.getEntities(0), lcar1)# 为所有点指定一个网格尺寸。
   # getEntities()默认获取所有维度的实体，参数0表示只是获取点，返回一个元组列表，因为默认情况下，多个维度都有。
   gmsh.model.mesh.setSize(gmsh.model.getBoundary(holes, False, False, True), lcar3)# 覆盖这5个球上的尺寸约束。
   # getBoundary获取边界，第一个参数是指明实体的元组列表，后三个参数分别为combined，默认是True；oriented，默认是True(将编号和方向相乘)；recursive(是否递归到最低维度，也就是点，)，默认是False(表示只取低一维的边界)；返回值也是元组列表。
   eps = 1e-3
   ov = gmsh.model.getEntitiesInBoundingBox(0.5 - eps, 0.5 - eps, 0.5 - eps, 0.5 + eps, 0.5 + eps, 0.5 + eps, 0)# 根据几何来选择角点，前6个参数分别是一个立方体的包围盒的xyz的最小值和最大值，最后一个参数是维度。只有完全被包含在包围盒中的实体才会被选中
   gmsh.model.mesh.setSize(ov, lcar2)
   gmsh.model.mesh.generate(3)
   gmsh.write("t16.msh")
   # t18.py,t19.py,t20.py都是使用OpenCASCADE内核创建的
   log = gmsh.logger.get()# 检查消息
   print("Logger has recorded " + str(len(log)) + " lines")
   gmsh.logger.stop()
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 各项异性的背景网格

1. ```python
   # 从在t7.py中可以看出，网格尺寸可以通过背景网格以相当精确的方式指明，例如一个包含了目标网格尺寸的后处理视图。这里背景网格代表了一个定义在矩形上的度量张量场。可以使用bamg作为2D网格生成器来创建各向异性网格。某些流动问题需要这种网格，沿流动方向和垂直于该方向的网格尺寸可以不一样。
   # 这里的t17_bgmesh.pos文件中存储的是TT（张量三角形）格式，TT(1.3595577,0.75626045,0,1.6283393,0.7627584,0,1.114271,0.9760711,0){14.440502,18.724785,0,18.724785,47.687943,0,0,0,1,9.94486,10.091231,0,10.091231,23.46719,0,0,0,1,4.652728,6.513453,0,6.513453,25.61624,0,0,0,1};其中()内的9个数是三角形三个顶点的xyz坐标。{}中每9个数，三角形的一个点的度量张量在R^3中的分量。可以看到这三个张量都是关于xy轴对称的。
   # 这种以张量形式提供的背景网格，会导致同一个点在不同方向上的尺寸不同，因为张量在不同方向上的分量不同。
   import gmsh
   import math
   import os
   import sys
   gmsh.initialize()
   gmsh.model.add("t17")
   gmsh.model.occ.addRectangle(-2, -2, 0, 4, 4)
   gmsh.model.occ.synchronize()
   path = os.path.dirname(os.path.abspath(__file__))
   gmsh.merge(os.path.join(path, os.pardir, 't17_bgmesh.pos'))# 合并一个包含目标各向异性网格尺寸的后处理视图。
   bg_field = gmsh.model.mesh.field.add("PostView")
   gmsh.model.mesh.field.setNumber(bg_field, "ViewIndex", 0)
   gmsh.model.mesh.field.setAsBackgroundMesh(bg_field)# 将后处理视图当作背景网格
   
   # 使用 bamg
   gmsh.option.setNumber("Mesh.SmoothRatio", 3)#在BAMG算法中使用，同一条边上的不同节点之间的网格尺寸的比值。
   gmsh.option.setNumber("Mesh.AnisoMax", 1000)# 网格的最大各向异性
   gmsh.option.setNumber("Mesh.Algorithm", 7)#BAMG算法
   gmsh.model.mesh.generate(2)
   gmsh.write("t17.msh")
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 周期性网格

1. ```python
   # 周期性网格约束可以施加在曲面和曲线上
   import gmsh
   import math
   import os
   import sys
   gmsh.initialize()
   gmsh.model.add("t18")
   gmsh.model.occ.addBox(0, 0, 0, 1, 1, 1, 1)
   gmsh.model.occ.synchronize()
   gmsh.model.mesh.setSize(gmsh.model.getEntities(0), 0.1)
   gmsh.model.mesh.setSize([(0, 1)], 0.02)#给一个点单独设置一个更小的网格尺寸，这样方便观察周期性约束是否成功添加。
   
   # 为了确保曲面2的网格和曲面1完全对应，应该设置以下的约束。
   # 仿射变换可以由一个非奇异的线性变换+一个平移变换组合而成。也就是y=Ax+b，也可以写成[y,1]^T=[A,b;0,1][b,1]^T，其中等号右侧的矩阵的0是一个行向量，尺寸和b的行数相同，这个是齐次坐标表示。setPeriodic所需要的矩阵就是齐次坐标之间的变换矩阵。
   # 周期性变换通过提供一个4x4的仿射变换矩阵来完成，按行输入。
   translation = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]# 这里的A为单位矩阵，b为[1,0,0]^T。
   gmsh.model.mesh.setPeriodic(2, [2], [1], translation)# 在划分网格时，曲面2上的网格会通过从曲面1上复制得到，这里也可以看到将曲面1上的点或者三角形网格，进行仿射变换，就会得到它们在曲面2上的像。
   gmsh.model.mesh.setPeriodic(2, [6], [5], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1])# 矩阵A为单位矩阵，b为[0,0,1]^T。
   gmsh.model.mesh.setPeriodic(2, [4], [3], [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1])# 矩阵A为单位矩阵，b为[0,1,10]^T。
   # 对于更复杂的情况，手动来寻找对应的面可能会比较繁琐。尤其是当几何式通过实体建模得到的
   gmsh.model.occ.addBox(2, 0, 0, 1, 1, 1, 10)# 这里创建一个立方体和几个球
   x = 2 - 0.3
   y = 0
   z = 0
   gmsh.model.occ.addSphere(x, y, z, 0.35, 11)
   gmsh.model.occ.addSphere(x + 1, y, z, 0.35, 12)
   gmsh.model.occ.addSphere(x, y + 1, z, 0.35, 13)
   gmsh.model.occ.addSphere(x, y, z + 1, 0.35, 14)
   gmsh.model.occ.addSphere(x + 1, y + 1, z, 0.35, 15)
   gmsh.model.occ.addSphere(x, y + 1, z + 1, 0.35, 16)
   gmsh.model.occ.addSphere(x + 1, y, z + 1, 0.35, 17)
   gmsh.model.occ.addSphere(x + 1, y + 1, z + 1, 0.35, 18)
   # 首先对所有的体积求交叉，这会使得球的一部分超出立方体
   out, _ = gmsh.model.occ.fragment([(3, 10)], [(3, i) for i in range(11, 19)])
   gmsh.model.occ.synchronize()
   # 让OpenCASCADE使用STL网格计算实体的更精确的包围盒
   gmsh.option.setNumber("Geometry.OCCBoundsUseStl", 1)
   # 获取包含在原始立方体包围盒内的所有体积，删除其外的所有体积。
   eps = 1e-3
   vin = gmsh.model.getEntitiesInBoundingBox(2 - eps, -eps, -eps, 2 + 1 + eps, 1 + eps, 1 + eps, 3)# 仅获取体积
   for v in vin:
       out.remove(v)
   gmsh.model.removeEntities(out, True)  # 递归删除外部的实体，不仅删除体积，还删除低维的实体，当然不会删除和未删除其他实体所共享的低维实体。
   # 设置一个非均匀的网格尺寸约束，这是为了方便观察结果
   p = gmsh.model.getBoundary(vin, False, False, True)  # 获取所有点
   gmsh.model.mesh.setSize(p, 0.1)
   p = gmsh.model.getEntitiesInBoundingBox(2 - eps, -eps, -eps, 2 + eps, eps, eps, 0)
   gmsh.model.mesh.setSize(p, 0.001)
   # 现在，我们自动识别几何体左侧和右侧的相应曲面。
   # 首先获得左侧的所有曲面。
   sxmin = gmsh.model.getEntitiesInBoundingBox(2 - eps, -eps, -eps, 2 + eps, 1 + eps, 1 + eps, 2)
   for i in sxmin:
       xmin, ymin, zmin, xmax, ymax, zmax = gmsh.model.getBoundingBox(i[0], i[1]) #获得左侧的每一个曲面的包围盒。
       sxmax = gmsh.model.getEntitiesInBoundingBox(xmin - eps + 1, ymin - eps, zmin - eps, xmax + eps + 1, ymax + eps, zmax + eps, 2)# 通过平移包围盒获得在右侧的相对的那个面，即沿x轴平移一个单位。
       # 对于所有复合条件的面，依次检查左右包围盒的坐标是否足够接近。
       for j in sxmax:
           xmin2, ymin2, zmin2, xmax2, ymax2, zmax2 = gmsh.model.getBoundingBox(j[0], j[1])
           xmin2 -= 1
           xmax2 -= 1
           if (abs(xmin2 - xmin) < eps and abs(xmax2 - xmax) < eps and
               abs(ymin2 - ymin) < eps and abs(ymax2 - ymax) < eps and
               abs(zmin2 - zmin) < eps and abs(zmax2 - zmax) < eps):
               gmsh.model.mesh.setPeriodic(2, [j[1]], [i[1]], translation)# 如果匹配的话，则应用周期性约束
   
   gmsh.model.mesh.generate(3)
   gmsh.write("t18.msh")
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 截面、圆角、管道、曲率网格大小

1. ```python
   # OpenCASCADE几何内核支持一些有用的固体建模特征
   import gmsh
   import math
   import os
   import sys
   gmsh.initialize()
   gmsh.model.add("t19")
   # 体积可以通过addThruSections()函数由闭合的曲线循环来构建。
   gmsh.model.occ.addCircle(0, 0, 0, 0.5, 1)
   gmsh.model.occ.addCurveLoop([1], 1)
   gmsh.model.occ.addCircle(0.1, 0.05, 1, 0.1, 2)
   gmsh.model.occ.addCurveLoop([2], 2)
   gmsh.model.occ.addCircle(-0.1, -0.1, 2, 0.3, 3)
   gmsh.model.occ.addCurveLoop([3], 3)
   gmsh.model.occ.addThruSections([1, 2, 3], 1)
   gmsh.model.occ.synchronize()
   # 可以强制创建直纹曲面
   gmsh.model.occ.addCircle(2 + 0, 0, 0, 0.5, 11)
   gmsh.model.occ.addCurveLoop([11], 11)
   gmsh.model.occ.addCircle(2 + 0.1, 0.05, 1, 0.1, 12)
   gmsh.model.occ.addCurveLoop([12], 12)
   gmsh.model.occ.addCircle(2 - 0.1, -0.1, 2, 0.3, 13)
   gmsh.model.occ.addCurveLoop([13], 13)
   gmsh.model.occ.addThruSections([11, 12, 13], 11, True, True)
   gmsh.model.occ.synchronize()
   
   # We copy the first volume, and fillet all its edges:
   # 复制第一个体积，平移，对它的所有边进行倒角
   out = gmsh.model.occ.copy([(3, 1)])
   gmsh.model.occ.translate(out, 4, 0, 0)
   gmsh.model.occ.synchronize()
   e = gmsh.model.getBoundary(gmsh.model.getBoundary(out), False)#对体积的边界再进行获取边界，就会得到它的所有曲线边界。
   gmsh.model.occ.fillet([out[0][1]], [abs(i[1]) for i in e], [0.1])# 第一个参数是体积的编号，第二个是要倒角的曲线的编号，第三个是倒角的尺寸，可以都用一个尺寸，也可以每个曲线单独指定，这样要求它和第二个参数的元素一样多，也可以是第二个参数的元素的两倍，这样每条曲线的首尾倒角的尺寸都不一样。默认会删除原有的体积。返回值为倒角后的体积，以元组列表的形式。
   gmsh.model.occ.synchronize()
   # OpenCASCADE也允许沿着一个平滑的路径进行通用的拉伸，首先定义一个样条曲线。
   nturns = 1.
   npts = 20
   r = 1.
   h = 1. * nturns
   p = []# 用来存储样条点
   for i in range(0, npts):# 依次生成所有的样条点
       theta = i * 2 * math.pi * nturns / npts
       gmsh.model.occ.addPoint(r * math.cos(theta), r * math.sin(theta), i * h / npts, 1, 1000 + i)# 这是一个螺旋线
       p.append(1000 + i)
   gmsh.model.occ.addSpline(p, 1000)
   gmsh.model.occ.addWire([1000], 1000)# Wire类似于curveloop，但是它是可开可闭的。
   # 定义一个要沿着样条曲线拉伸的圆盘
   gmsh.model.occ.addDisk(1, 0, 0, 0.2, 0.2, 1000)# 前三个参数为椭圆的重心，后两个为x轴和y轴的半径，最后为编号。
   gmsh.model.occ.rotate([(2, 1000)], 0, 0, 0, 1, 0, 0, math.pi / 2)
   gmsh.model.occ.addPipe([(2, 1000)], 1000, 'DiscreteTrihedron')# 将第一个参数沿着样条曲线(第二个参数)拉伸来创造一个管子，扫掠类型也可以指定为Frenet。
   # 删除源曲面，增加边的编号，为了更好地显示几何。
   gmsh.model.occ.remove([(2, 1000)])
   gmsh.option.setNumber("Geometry.NumSubEdges", 1000)# 用于绘制曲线的细分数量
   gmsh.model.occ.synchronize()
   #必须要进行如下设置，因为上边所有的行为都没有指定一个网格场。
   gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 20)
   gmsh.option.setNumber("Mesh.MeshSizeMin", 0.001)
   gmsh.option.setNumber("Mesh.MeshSizeMax", 0.3)
   gmsh.model.mesh.generate(3)
   gmsh.write("t19.msh")
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## STEP导入和操作，几何切分

1. ```python
   # OpenCASCADE几何内核允许导入STEP文件然后修改它们。
   import gmsh
   import math
   import os
   import sys
   gmsh.initialize()
   gmsh.model.add("t20")
   # 载入STEP文件(一个六角螺母)，这里使用importShapes而非merge，这样允许直接获取最高维导入实体的编号。
   path = os.path.dirname(os.path.abspath(__file__))
   v = gmsh.model.occ.importShapes(os.path.join(path, os.pardir, 't20_data.step'))#适用于BREP, STEP 或者 IGES格式
   # 如果在合并STEP文件前指定了gmsh.option.setString('Geometry.OCCTargetUnit', 'M')，则OpenCASCADE会将单位转化为m，否则使用默认的mm单位。
   xmin, ymin, zmin, xmax, ymax, zmax = gmsh.model.occ.getBoundingBox(v[0][0], v[0][1])#获取体积的包围盒
   N = 5  # 切分的段数
   dir = 'X' # 使用垂直于某个方向的平面来切分
   surf = False  # 是否只保留曲面
   dx = (xmax - xmin)
   dy = (ymax - ymin)
   dz = (zmax - zmin)
   L = dz if (dir == 'X') else dx
   H = dz if (dir == 'Y') else dy
   # 创建第一个切平面
   s = []
   s.append((2, gmsh.model.occ.addRectangle(xmin, ymin, zmin, L, H)))
   if dir == 'X':
       gmsh.model.occ.rotate([s[0]], xmin, ymin, zmin, 0, 1, 0, -math.pi/2)
   elif dir == 'Y':
       gmsh.model.occ.rotate([s[0]], xmin, ymin, zmin, 1, 0, 0, math.pi/2)
   tx = dx / N if (dir == 'X') else 0
   ty = dy / N if (dir == 'Y') else 0
   tz = dz / N if (dir == 'Z') else 0
   gmsh.model.occ.translate([s[0]], tx, ty, tz)# 平移到位
   for i in range(1, N-1):
       s.extend(gmsh.model.occ.copy([s[0]]))# extend会将参数迭代器中的元素都活取出来，然后附加在s后面。
       gmsh.model.occ.translate([s[-1]], i * tx, i * ty, i * tz) #依次复制并平移切平面
   
   gmsh.model.occ.fragment(v, s)# 使用所有切平面来切分体积
   gmsh.model.occ.remove(gmsh.model.occ.getEntities(2), True)# 这里虽然是要删除所有的曲面，但是如果一个曲面是体积的边界，则不会被删除。这里切割平面“伸出”体积的部分会被删除。
   gmsh.model.occ.synchronize()
   if surf:    # 如果只想保留用于切分的平面，则围绕着切平面的包围盒来获取曲面。
       eps = 1e-4
       s = []
       for i in range(1, N):
           xx = xmin if (dir == 'X') else xmax
           yy = ymin if (dir == 'Y') else ymax
           zz = zmin if (dir == 'Z') else zmax
           s.extend(gmsh.model.getEntitiesInBoundingBox( xmin - eps + i * tx, ymin - eps + i * ty, zmin - eps + i * tz, xx + eps + i * tx, yy + eps + i * ty, zz + eps + i * tz, 2))
       # 删除掉其他所有的实体，因为后续将不会修改任何OpenCASCADE实体
       dels = gmsh.model.getEntities(2)
       for e in s:
           dels.remove(e)
       gmsh.model.removeEntities(gmsh.model.getEntities(3))
       gmsh.model.removeEntities(dels)# 只删除特定的曲面
       gmsh.model.removeEntities(gmsh.model.getEntities(1))
       gmsh.model.removeEntities(gmsh.model.getEntities(0))
   
   # 生命一个全局网格尺寸，对切分后的模型划分网格。
   gmsh.option.setNumber("Mesh.MeshSizeMin", 3)
   gmsh.option.setNumber("Mesh.MeshSizeMax", 3)
   gmsh.model.mesh.generate(3)
   gmsh.write("t20.msh")
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 网格切分

1. ```python
   import gmsh
   import sys
   # Gmsh可以使用不同的算法来切分网格，例如图切分器Metis或者SimplePartition插件。对于所有切分算法，网格单元和网格切分之间的关系通过新创建的离散基本实体（切分实体）来编码。切分实体看上去和其他基本离散基本实体一样，唯一的区别是，它们跟踪网格切分索引及它的父实体
   # 这个方法的主要优点是它允许维持一个对切分实体的完整的边界表示，如果设置了Mesh.PartitionCreateTopology，Gmsh会自动创建。
   gmsh.initialize()
   # 创建一个简单的几何，2个相邻的巨型，共享一个边。
   gmsh.model.add("t21")
   gmsh.model.occ.addRectangle(0, 0, 0, 1, 1, 1)
   gmsh.model.occ.addRectangle(1, 0, 0, 1, 1, 2)
   gmsh.model.occ.fragment([(2, 1)], [(2, 2)])
   gmsh.model.occ.synchronize()
   gmsh.model.mesh.setSize(gmsh.model.getEntities(0), 0.05)
   
   # 为每一个矩形创建一个物理组
   gmsh.model.addPhysicalGroup(2, [1], 100, "Left")
   gmsh.model.addPhysicalGroup(2, [2], 200, "Right")
   gmsh.model.mesh.generate(2)
   
   # 定义一些ONELAB参数来微调网格切分的过程
   gmsh.onelab.set("""[
     {
       "type":"number",
       "name":"Parameters/0Mesh partitioner", #这里的0表示顺序，并不会显示出来
       "values":[0],
       "choices":[0, 1],
       "valueLabels":{"Metis":0, "SimplePartition":1} #下拉菜单
     },
     {
       "type":"number",
       "name":"Parameters/1Number of partitions",
       "values":[3],
       "min":1,
       "max":256,
       "step":1
     },
     {
       "type":"number",
       "name":"Parameters/2Create partition topology (BRep)?",
       "values":[1],
       "choices":[0, 1]
     },
     {
       "type":"number",
       "name":"Parameters/3Create ghost cells?",
       "values":[0],
       "choices":[0, 1]
     },
     {
       "type":"number",
       "name":"Parameters/3Create new physical groups?",
       "values":[0],
       "choices":[0, 1]
     },
     {
       "type":"number",
       "name":"Parameters/3Write file to disk?",
       "values":[1],
       "choices":[0, 1]
     },
     {
       "type":"number",
       "name":"Parameters/4Write one file per partition?",
       "values":[0],
       "choices":[0, 1]
     }
   ]""")
   
   def partitionMesh():
       N = int(gmsh.onelab.getNumber("Parameters/1Number of partitions")[0])# 通过onelab获取切分的段数
       # 应该创建切分实体的边界表示码？
       gmsh.option.setNumber("Mesh.PartitionCreateTopology", gmsh.onelab.getNumber("Parameters/2Create partition topology (BRep)?")[0])
       # 应该创建幽灵单元吗？
       gmsh.option.setNumber("Mesh.PartitionCreateGhostCells", gmsh.onelab.getNumber("Parameters/3Create ghost cells?")[0])
       # 应该在切分实体上自动创建新的物理组吗？
       gmsh.option.setNumber("Mesh.PartitionCreatePhysicals", gmsh.onelab.getNumber("Parameters/3Create new physical groups?")[0])
       # 应该和Gmsh4之前保持向后兼容性吗？例如保存为MSH2格式。
       gmsh.option.setNumber("Mesh.PartitionOldStyleMsh2", 0)
       # 应该为每个一个切分都保存一个网格文件吗？
       gmsh.option.setNumber("Mesh.PartitionSplitMeshFiles", gmsh.onelab.getNumber("Parameters/4Write one file per partition?")[0])
       if gmsh.onelab.getNumber("Parameters/0Mesh partitioner")[0] == 0:
           gmsh.model.mesh.partition(N)# 使用Metis将当前模型切分为N份。
           # 可以为Metis设置一些选项，Mesh.MetisAlgorithm，Mesh.MetisObjective，Mesh.PartitionTriWeight，Mesh.PartitionQuadWeight等。
       else:
           # 使用SimplePartition插件来创建国际象棋棋盘状的切分
           gmsh.plugin.setNumber("SimplePartition", "NumSlicesX", N)# X方向
           gmsh.plugin.setNumber("SimplePartition", "NumSlicesY", 1)
           gmsh.plugin.setNumber("SimplePartition", "NumSlicesZ", 1)
           gmsh.plugin.run("SimplePartition")
   
       # 保存网格文件，如果设置了Mesh.PartitionSplitMeshFiles，则会保存多个文件
       if gmsh.onelab.getNumber("Parameters/3Write file to disk?")[0] == 1:
           gmsh.write("t21.msh")
   
       # 对每一个切分后的实体进行迭代，打印一些信息
       entities = gmsh.model.getEntities()
       for e in entities:
           partitions = gmsh.model.getPartitions(e[0], e[1])# 在切分过的模型中，返回实体所属分区的标签
           if len(partitions):
               print("Entity " + str(e) + " of type " + gmsh.model.getType(e[0], e[1]))# getType可以获取实体的类型。
               print(" - Partition(s): " + str(partitions))
               print(" - Parent: " + str(gmsh.model.getParent(e[0], e[1])))
               print(" - Boundary: " + str(gmsh.model.getBoundary([e])))
   
   partitionMesh()
   # 启动GUI，处理check事件，根据GUI的选择来重新划分网格
   def checkForEvent():
       action = gmsh.onelab.getString("ONELAB/Action")
       if len(action) and action[0] == "check":
           gmsh.onelab.setString("ONELAB/Action", [""])
           partitionMesh()
           gmsh.graphics.draw()
       return True
   
   if "-nopopup" not in sys.argv:
       gmsh.fltk.initialize()
       while gmsh.fltk.isAvailable() and checkForEvent():
           gmsh.fltk.wait()
   
   gmsh.finalize()
   ```


## 几何和网格数据

1. ```python
   # 使用API可以做到比.geo脚本更多的功能。额外的功能通过扩展教程来引入，例如x1.py
   # 这里使用API来访问基本几何和网格数据
   import gmsh
   import sys
   gmsh.initialize()
   if len(sys.argv) > 1 and sys.argv[1][0] != '-':
       # 如果提供了一个参数，将它当作Gmsh要读取的文件，例如MSH格式，"python x1.py file.msh"
       gmsh.open(sys.argv[1])
   else:
       # 否则，创建几何然后划分网格
       gmsh.model.occ.addCone(1, 0, 0, 1, 0, 0, 0.5, 0.1)# 创建一个圆锥，前三个参数为底面圆心的坐标，后三个为底面的法向，最后2个为底面和顶面的半径，如果顶面半径为0，则表示圆锥，否则为圆台。
       gmsh.model.occ.synchronize()
       gmsh.model.mesh.generate()
   
   # 打印模型名称和维度
   print('Model ' + gmsh.model.getCurrent() + ' (' + str(gmsh.model.getDimension()) + 'D)')# getCurrent返回当前模型名称，getDimension返回当前模型维度。
   # 模型实体可以是CAD实体（从内置内核或者OCC内核）或者是离散实体（通过网格定义）
   entities = gmsh.model.getEntities()
   for e in entities:
       dim = e[0]
       tag = e[1]
       nodeTags, nodeCoords, nodeParams = gmsh.model.mesh.getNodes(dim, tag)# 获取特定实体的网格节点，如果实体是一个点，则只会返回该点的节点，如果实体是一个线/面/体，则其边界和内部。如果有多个复合条件的，则返回列表。nodeCoords为节点的全局xyz坐标，nodeParams为节点的参数坐标。
       elemTypes, elemTags, elemNodeTags = gmsh.model.mesh.getElements(dim, tag)#获取特定实体的网格单元，如果划分了3维网格，则只会存在3D单元，只要给定的几何实体和该单元有交集，该单元就会被返回。elemNodeTags是每个单元所包含的节点的编号。
       # 可以通过getElementsByType()获取指定类型的单元，可以通过getElementTypes()获取单元的类型。
       type = gmsh.model.getType(dim, tag)# 获取几何实体的类型字符串，例如Point,Curve,Surface,Volume等。
       name = gmsh.model.getEntityName(dim, tag)# 获取几何实体的名称，对于大多数几何实体，都为空。
       if len(name): name += ' '
       print("Entity " + name + str(e) + " of type " + type)
       # 网格节点和单元的数量
       numElem = sum(len(i) for i in elemTags)
       print(" - Mesh has " + str(len(nodeTags)) + " nodes and " + str(numElem) + " elements")
       up, down = gmsh.model.getAdjacencies(dim, tag)#分别获取高/低一维的相关联的实体。例如对于曲线来说，高一维度就是将该曲线作为边界的曲面，低一维度就是该曲线的端点。
       if len(up):
           print(" - Upward adjacencies: " + str(up))
       if len(down):
           print(" - Downward adjacencies: " + str(down))
       physicalTags = gmsh.model.getPhysicalGroupsForEntity(dim, tag)# 获取这个实体所属的物理组
       if len(physicalTags):
           s = ''
           for p in physicalTags:
               n = gmsh.model.getPhysicalName(dim, p)
               if n: n += ' '
               s += n + '(' + str(dim) + ', ' + str(p) + ') '
           print(" - Physical groups: " + s)
       # 这个实体是切分实体吗？如果是的话，它的父实体是？
       partitions = gmsh.model.getPartitions(dim, tag)
       if len(partitions):
           print(" - Partition tags: " + str(partitions) + " - parent entity " + str(gmsh.model.getParent(dim, tag)))
       # 列出构成实体网个的所有单元的类型
       for t in elemTypes:
           name, dim, order, numv, parv, _ = gmsh.model.mesh.getElementProperties(t)
           print(" - Element type: " + name + ", order " + str(order) + " (" + str(numv) + " nodes in param coord: " + str(parv) + ")")
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.clear()# 清理所有的模型数据
   gmsh.finalize()
   ```


## 网格导入，离散实体，混合模型，地形网格

1. ```python
   import gmsh
   import sys
   import math
   # API可以用来导入网格而不用从文件中读取它，通过动态创建节点，将他们保存在模型实体中，这些模型实体可以是已有的CAD实体，也可以是离散实体，完全由网格定义。离散实体可以被重参数化(t13.py)，这样它们可以后续被重新划分网格，也可以和内置的CAD模型合并来创建混合模型。
   # 这里结合了所有这些功能来执行地形网格划分，其中地形由离散曲面（后续对其进行重新参数化）与地下CAD表示相结合来描述。
   gmsh.initialize()
   gmsh.model.add("x2")
   N = 100# 地形曲面网格为(N+1)x(N+1)个输入数据点
   def tag(i, j):#一个帮助函数，可以返回i,j下标出的节点编号,左下角点编号为1，然后向上逐个增加编号，到最顶后(编号为N+1)的下一个点为第二列的最下面的点，编号为N+2，依次类推。
       return (N + 1) * i + j + 1 # i和j的取值范围为[0,N]
   
   coords = [] # 存储所有节点的xyz坐标。
   nodes = [] # 存储对应节点的编号，和coords的配合使用，可以获得任意编号的节点xyz坐标。
   # coords和nodes是几何信息，tris和lin是网格的拓扑信息。
   tris = [] # 地形曲面上三角形单元（每个单元有3个节点）的连接性。
   lin = [[], [], [], []] #4个边界上的线单元（每个单元有2个节点）的连接性。
   pnt = [tag(0, 0), tag(N, 0), tag(N, N), tag(0, N)]#4个角上的点单元的连接性（每个点单元有1个节点）
   for i in range(N + 1):# range(N+1)是[0:N]
       for j in range(N + 1):
           nodes.append(tag(i, j))#追加i,j位置的节点
           coords.extend([float(i) / N, float(j) / N, 0.05 * math.sin(10 * float(i + j) / N)])# 追加该节点的x,y,z坐标
           if i > 0 and j > 0:# 这里把内部的NxN个正方形切分成2N^2个三角形。
               tris.extend([tag(i - 1, j - 1), tag(i, j - 1), tag(i - 1, j)])
               tris.extend([tag(i, j - 1), tag(i, j), tag(i - 1, j)])
           if (i == 0 or i == N) and j > 0:# 左右两边，分别为lin[3]，lin[1]
               lin[3 if i == 0 else 1].extend([tag(i, j - 1), tag(i, j)])#将该点下方的单元加入
           if (j == 0 or j == N) and i > 0:# 上下两边，分别为lin[2]，lin[0]
               lin[0 if j == 0 else 2].extend([tag(i - 1, j), tag(i, j)])
           #因此四个边，最下边是0，然后逆时针依次是1,2,3
   
   for i in range(4):
       gmsh.model.addDiscreteEntity(0, i + 1)# 为地形曲面的4个角点创建4个离散点
   
   gmsh.model.setCoordinates(1, 0, 0, coords[3 * tag(0, 0) - 1])# 为上面创建的离散点设置xyz坐标。
   gmsh.model.setCoordinates(2, 1, 0, coords[3 * tag(N, 0) - 1])
   gmsh.model.setCoordinates(3, 1, 1, coords[3 * tag(N, N) - 1])
   gmsh.model.setCoordinates(4, 0, 1, coords[3 * tag(0, N) - 1])
   # 将之前创建的离散点实体作为新创建的离散边界曲线的边界点。
   for i in range(4):
       gmsh.model.addDiscreteEntity(1, i + 1, [i + 1, i + 2 if i < 3 else 1])# 分别添加[1,2][2,3][3,4][4,1]，四个1维实体。前两个参数为dim，tag，最后一个参数为边界列表。这里创建的是上下左右每个边由2个离散点组成，而非每个边由一系列的短边组成。
   gmsh.model.addDiscreteEntity(2, 1, [1, 2, -3, -4])#创建一个离散曲面和它的包围曲线。
   gmsh.model.mesh.addNodes(2, 1, nodes, coords)#添加曲面上的所有节点
   # 为4个角点添加点单元，4条曲线添加线单元，曲面添加三角形单元
   for i in range(4):
       gmsh.model.mesh.addElementsByType(i + 1, 15, [], [pnt[i]])#点单元类型为15
       gmsh.model.mesh.addElementsByType(i + 1, 1, [], lin[i])# 2节点线单元类型为1，批量添加多个线单元，
   
   gmsh.model.mesh.addElementsByType(1, 2, [], tris)# 3节点三角形单元类型为2
   gmsh.model.mesh.reclassifyNodes()# 对曲线和点上的节点重新分类，因为为了简化，在addNodes之前将它们放置在了曲面上。
   gmsh.model.mesh.createGeometry()# 为离散曲线和曲面创建一个几何，这样后续可以重新划分网格
   # 注意，对于更复杂的网格，例如输入的非结构STL网格，可以使用classifySurfaces来自动创建离散实体和拓扑，但是后续必须提取边界。
   # 创建其他内置的CAD实体来构成一个在地形面之下的体积，足以到，只有内置CAD实体可以是混合的，例如在边界上拥有离散实体，OCC不支持这种特性。
   p1 = gmsh.model.geo.addPoint(0, 0, -0.5)
   p2 = gmsh.model.geo.addPoint(1, 0, -0.5)
   p3 = gmsh.model.geo.addPoint(1, 1, -0.5)
   p4 = gmsh.model.geo.addPoint(0, 1, -0.5)
   c1 = gmsh.model.geo.addLine(p1, p2)
   c2 = gmsh.model.geo.addLine(p2, p3)
   c3 = gmsh.model.geo.addLine(p3, p4)
   c4 = gmsh.model.geo.addLine(p4, p1)
   c10 = gmsh.model.geo.addLine(p1, 1)
   c11 = gmsh.model.geo.addLine(p2, 2)
   c12 = gmsh.model.geo.addLine(p3, 3)
   c13 = gmsh.model.geo.addLine(p4, 4)
   ll1 = gmsh.model.geo.addCurveLoop([c1, c2, c3, c4])
   s1 = gmsh.model.geo.addPlaneSurface([ll1])
   ll3 = gmsh.model.geo.addCurveLoop([c1, c11, -1, -c10])
   s3 = gmsh.model.geo.addPlaneSurface([ll3])
   ll4 = gmsh.model.geo.addCurveLoop([c2, c12, -2, -c11])
   s4 = gmsh.model.geo.addPlaneSurface([ll4])
   ll5 = gmsh.model.geo.addCurveLoop([c3, c13, 3, -c12])
   s5 = gmsh.model.geo.addPlaneSurface([ll5])
   ll6 = gmsh.model.geo.addCurveLoop([c4, c10, 4, -c13])
   s6 = gmsh.model.geo.addPlaneSurface([ll6])
   sl1 = gmsh.model.geo.addSurfaceLoop([s1, s3, s4, s5, s6, 1])
   v1 = gmsh.model.geo.addVolume([sl1])
   gmsh.model.geo.synchronize()
   
   transfinite = False # 可以将这个设置为True来创建一个完全六面体的网格
   transfiniteAuto = False
   
   if transfinite:
       NN = 30
       for c in gmsh.model.getEntities(1):
           gmsh.model.mesh.setTransfiniteCurve(c[1], NN)
       for s in gmsh.model.getEntities(2):
           gmsh.model.mesh.setTransfiniteSurface(s[1])
           gmsh.model.mesh.setRecombine(s[0], s[1])
           gmsh.model.mesh.setSmoothing(s[0], s[1], 100)
       gmsh.model.mesh.setTransfiniteVolume(v1)
   elif transfiniteAuto:
       gmsh.option.setNumber('Mesh.MeshSizeMin', 0.5)
       gmsh.option.setNumber('Mesh.MeshSizeMax', 0.5)
       gmsh.model.mesh.setTransfiniteAutomatic()# 这个函数使用尺寸约束来设置点的数量
   else:
       gmsh.option.setNumber('Mesh.MeshSizeMin', 0.05)
       gmsh.option.setNumber('Mesh.MeshSizeMax', 0.05)
   
   gmsh.model.mesh.generate(3)
   gmsh.write('x2.msh')
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```

## 后处理数据导入，基于列表的

1. ```python
   import gmsh
   import sys
   gmsh.initialize(sys.argv)
   # Gmsh支持两种后处理数据，基于列表和基于模型的，两种数据类型都通过view接口来处理，基于列表的view完全独立于任何模型和网格，它们是自持的，只是包含坐标和值的列表，一个单元一个单元地存储。三种场，标量S，向量V，张量T，一些单元类型，点P，线段L，三角形T，四边形Q，四面体S，六面体H，棱柱体I，金字塔Y。基于模型的教程可以查看x4.py。
   t1 = gmsh.view.add("A list-based view")#首先应该创建一个新的view
   # 通过将类型指定为一个2字符的字符串来添加基于列表的数据，一个是场类型，另一个是单元类型。然后是单元的所有节点的坐标，
   triangle1 = [0., 1., 1., # x1,x2,x3
                0., 0., 1., # y1,y2,y3
                0., 0., 0.] # z1,z2,z3
   triangle2 = [0., 1., 0., 0., 1., 1., 0., 0., 0.]
   # 追加10个时间步的数据
   for step in range(0, 10):
       triangle1.extend([10., 11. - step, 12.])  #每一步都要给三个节点赋值s1,s2,s3
       triangle2.extend([11., 12., 13. + step])
   
   # 基于列表的数据只需要将所有三角形的数据拼接起来就可以了
   gmsh.view.addListData(t1, "ST", 2, triangle1 + triangle2)# 第三个参数是追加的单元数量，数据本身不用写成2维列表的形式，平坦即可。
   # 在内部，通过.geo文件解析器解析的后处理视图，会创建这种基于列表的数据，例如t7.py，t8.py，独立于任何网格。
   #向量和张量场也可以以同样的方式导入，唯一的区别是，向量在每个节点有3个分量，张量在每个节点有9个分量。
   # For example a vector field on a line element can be added as follows:
   # 线单元上的矢量场
   line = [
       0., 1.,   # x1,x2
       1.2, 1.2, # y1,y2
       0., 0.    # z1,z2
   ]
   for step in range(0, 10):
       line.extend([10. + step, 0., 0.,  # 1号节点的u,v,w
                    10. + step, 0., 0.]) # 2号节点的u,v,w
   gmsh.view.addListData(t1, "VL", 1, line)
   
   # 基于列表的数据也可以存储2D(屏幕坐标)和3D(模型坐标)字符串，例如t4.py。
   gmsh.view.addListDataString(t1, [20., -20.], ["Created with Gmsh"])#在屏幕左下角添加一个字符串。
   gmsh.view.addListDataString(t1, [0.5, 1.5, 0.],
                               ["A multi-step list-based view"],
                               ["Align", "Center", "Font", "Helvetica"])# 在模型的[0.5,1.5,0.]位置添加一个字符串。
   # 可以通过option接口来查询和修改视图的各种属性
   gmsh.view.option.setNumber(t1, "TimeStep", 5)
   gmsh.view.option.setNumber(t1, "IntervalsType", 3)
   ns = gmsh.view.option.getNumber(t1, "NbTimeStep") #获取时间步的总数
   print("View " + str(t1) + " has " + str(ns) + " time steps")
   
   # 也可以通过插件来查询或修改视图的属性，或者直接通过gmsh.view.probe()来探测点(0.9, 0.1, 0)
   print("Value at (0.9, 0.1, 0)", gmsh.view.probe(t1, 0.9, 0.1, 0))
   gmsh.view.write(t1, "x3.pos")#也可以将视图保存为.pos文件
   # 高阶数据集可以通过显式设置插值矩阵来提供，这里创建一个在四边形上二阶插值的视图。
   t2 = gmsh.view.add("Second order quad")# 添加一个新的视图。
   # 设置节点坐标
   quad = [0., 1., 1., 0., # x1,x2,x3,x4
           -1.2, -1.2, -0.2, -0.2, # y1,y2,y3,y4
           0., 0., 0., 0.] # z1,z2,z3,z4
   
   quad.extend([1., 1., 1., 1., 3., 3., 3., 3., -3.])# 增加9个值，后续会用二阶基函数来插值。
   # 设置2个插值矩阵，c和e，系数矩阵c是dxd的，指数矩阵e是dx3的，都是按照行来存储为一个列向量。
   # 定义为d=9的基函数，u,v,w是参考单元中的坐标。
   # Set the two interpolation matrices c[i][j] and e[i][j] defining the d = 9
   # basis functions: f[i](u, v, w) = sum_(j = 0, ..., d - 1) c[i][j] u^e[j][0]
   # v^e[j][1] w^e[j][2], i = 0, ..., d-1, with u, v, w the coordinates in the
   # reference element:
   gmsh.view.setInterpolationMatrices(t2, "Quadrangle", 9,
                                      [0, 0, 0.25, 0, 0, -0.25, -0.25, 0, 0.25,
                                       0, 0, 0.25, 0, 0, -0.25, 0.25, 0, -0.25,
                                       0, 0, 0.25, 0, 0, 0.25, 0.25, 0, 0.25,
                                       0, 0, 0.25, 0, 0, 0.25, -0.25, 0, -0.25,
                                       0, 0, -0.5, 0.5, 0, 0.5, 0, -0.5, 0,
                                       0, 0.5, -0.5, 0, 0.5, 0, -0.5, 0, 0,
                                       0, 0, -0.5, 0.5, 0, -0.5, 0, 0.5, 0,
                                       0, 0.5, -0.5, 0, -0.5, 0, 0.5, 0, 0,
                                       1, -1, 1, -1, 0, 0, 0, 0, 0],
                                      [0, 0, 0,
                                       2, 0, 0,
                                       2, 2, 0,
                                       0, 2, 0,
                                       1, 0, 0,
                                       2, 1, 0,
                                       1, 2, 0,
                                       0, 1, 0,
                                       1, 1, 0])
   # 注意2个额外的插值矩阵也可以提供来对几何插值，例如插值曲边单元。
   gmsh.view.addListData(t2, "SQ", 1, quad)# 像视图中增加数据
   # 为了显示高阶场，必须激活自适应可视化，设置一个可视化误差限值，和最大细分级别，Gmsh会根据需要的精度来自动进行网格精细化来显示高阶场。
   gmsh.view.option.setNumber(t2, "AdaptVisualizationGrid", 1)
   gmsh.view.option.setNumber(t2, "TargetError", 1e-2)
   gmsh.view.option.setNumber(t2, "MaxRecursionLevel", 5)
   # 注意，自适应可视化数据可以通过为gmsh.view.getListData设置returnAdaptive参数来获取。
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 后处理数据导入，基于模型

1. ```python
   import gmsh
   import sys
   gmsh.initialize(sys.argv)
   # 基于模型的视图是基于一个或多个网格，和基于列表的视图相比，它在每一步都会连接到一个模型上，后处理数据存储在MSH格式时，会创建这种基于模型的视图。
   gmsh.model.add("simple model")
   surf = gmsh.model.addDiscreteEntity(2)# 创建一个2维离散实体
   # 增加4个节点，和2个三节点三角形，单元类型为2
   gmsh.model.mesh.addNodes(2, surf, [1, 2, 3, 4], [0., 0., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0.])
   gmsh.model.mesh.addElementsByType(surf, 2, [1, 2], [1, 2, 3, 1, 3, 4])
   # 创建一个基于模型的视图，向其中添加了10个基于节点的数据时间步。
   t1 = gmsh.view.add("Continuous")
   for step in range(0, 10):
       gmsh.view.addHomogeneousModelData(
           t1, step, "simple model", "NodeData",
           [1, 2, 3, 4],  # 节点编号
           [10., 10., 12. + step, 13. + step])  # 每个节点的数据
   
   # 除了基于节点的数据（这会产生连续场），也可以添加通用的里三场，它在每个单元的节点上定义，使用ElementNodeData。
   t2 = gmsh.view.add("Discontinuous")
   for step in range(0, 10):
       gmsh.view.addHomogeneousModelData(
           t2, step, "simple model", "ElementNodeData",
           [1, 2],  # tags of elements
           [10., 10., 12. + step, 14., 15., 13. + step])  # data per element nodes
   
   # Constant per element datasets can also be created using "ElementData". Note
   # that a more general function `addModelData' to add data for hybrid meshes
   # (when data is not homogeneous, i.e. when the number of nodes changes between
   # elements) is also available.
   
   # Each step of a model-based view can be defined on a different model, i.e. on a
   # different mesh. Let's define a second model and mesh it
   gmsh.model.add("another model")
   gmsh.model.occ.addBox(0, 0, 0, 1, 1, 1)
   gmsh.model.occ.synchronize()
   gmsh.model.mesh.generate(3)
   
   # We can add other steps to view "t" based on this new mesh:
   nodes, coord, _ = gmsh.model.mesh.getNodes()
   for step in range(11, 20):
       gmsh.view.addHomogeneousModelData(
           t1, step, "another model", "NodeData", nodes,
           [step * coord[i] for i in range(0, len(coord), 3)])
   
   # This feature allows to create seamless animations for time-dependent datasets
   # on deforming or remeshed models.
   
   # High-order node-based datasets are supported without needing to supply the
   # interpolation matrices (iso-parametric Lagrange elements). Arbitrary
   # high-order datasets can be specified as "ElementNodeData", with the
   # interpolation matrices specified in the same as as for list-based views (see
   # `x3.py').
   
   # Model-based views can be saved to disk using `gmsh.view.write()'; note that
   # saving a view based on multiple meshes (like the view `t1') will automatically
   # create several files. If the `PostProcessing.SaveMesh' option is not set,
   # `gmsh.view.write()' will only save the view data, without the mesh (which
   # could be saved independently with `gmsh.write()').
   gmsh.view.write(t1, "x4_t1.msh")
   gmsh.view.write(t2, "x4_t2.msh")
   
   # Launch the GUI to see the results:
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   
   ```


## 额外的几何数据，参数化，法向，曲率

1. ```python
   import gmsh
   import sys
   import math
   gmsh.initialize(sys.argv)
   # API以与CAD内核无关的方式提供对几何数据的访问
   # 创建要给简单的CAD模型，通过将一个球和立方体融合起来，然后在曲面上划分网格
   gmsh.model.add("x5")
   s = gmsh.model.occ.addSphere(0, 0, 0, 1)
   b = gmsh.model.occ.addBox(0.5, 0, 0, 1.3, 2, 3)
   gmsh.model.occ.fuse([(3, s)], [(3, b)])# 布尔加运算
   gmsh.model.occ.synchronize()
   gmsh.model.mesh.generate(2)
   
   # We can for example retrieve the exact normals and the curvature at all the
   # mesh nodes (i.e. not normals and curvatures computed from the mesh, but
   # directly evaluated on the geometry), by querying the CAD kernels at the
   # corresponding parametric coordinates.
   normals = []
   curvatures = []
   
   # For each surface in the model:
   for e in gmsh.model.getEntities(2):
       # Retrieve the surface tag
       s = e[1]
   
       # Get the mesh nodes on the surface, including those on the boundary
       # (contrary to internal nodes, which store their parametric coordinates,
       # boundary nodes will be reparametrized on the surface in order to compute
       # their parametric coordinates, the result being different when
       # reparametrized on another adjacent surface)
       tags, coord, param = gmsh.model.mesh.getNodes(2, s, True)
   
       # Get the surface normals on all the points on the surface corresponding to
       # the parametric coordinates of the nodes
       norm = gmsh.model.getNormal(s, param)
   
       # In the same way, get the curvature
       curv = gmsh.model.getCurvature(2, s, param)
   
       # Store the normals and the curvatures so that we can display them as
       # list-based post-processing views
       for i in range(0, len(coord), 3):
           normals.append(coord[i])
           normals.append(coord[i + 1])
           normals.append(coord[i + 2])
           normals.append(norm[i])
           normals.append(norm[i + 1])
           normals.append(norm[i + 2])
           curvatures.append(coord[i])
           curvatures.append(coord[i + 1])
           curvatures.append(coord[i + 2])
           curvatures.append(curv[i // 3])
   
   # Create a list-based vector view on points to display the normals, and a scalar view on points to display the curvatures
   vn = gmsh.view.add("normals")
   gmsh.view.addListData(vn, "VP", len(normals) // 6, normals)
   gmsh.view.option.setNumber(vn, 'ShowScale', 0)
   gmsh.view.option.setNumber(vn, 'ArrowSizeMax', 30)
   gmsh.view.option.setNumber(vn, 'ColormapNumber', 19)
   vc = gmsh.view.add("curvatures")
   gmsh.view.addListData(vc, "SP", len(curvatures) // 4, curvatures)
   gmsh.view.option.setNumber(vc, 'ShowScale', 0)
   
   # We can also retrieve the parametrization bounds of model entities, e.g. of
   # curve 5, and evaluate the parametrization for several parameter values:
   bounds = gmsh.model.getParametrizationBounds(1, 5)
   N = 20
   t = [bounds[0][0] + i * (bounds[1][0] - bounds[0][0]) / N for i in range(N)]
   xyz1 = gmsh.model.getValue(1, 5, t)
   
   # We can also reparametrize curve 5 on surface 1, and evaluate the points in the parametric plane of the surface:
   uv = gmsh.model.reparametrizeOnSurface(1, 5, t, 1)
   xyz2 = gmsh.model.getValue(2, 1, uv)
   
   # Hopefully we get the same x, y, z coordinates!
   if max([abs(a - b) for (a, b) in zip(xyz1, xyz2)]) < 1e-12:
       gmsh.logger.write('Evaluation on curve and surface match!')
   else:
       gmsh.logger.write('Evaluation on curve and surface do not match!', 'error')
   
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   
   gmsh.finalize()
   ```


## 积分点，雅可比，基函数

1. ```python
   import gmsh
   import sys
   
   gmsh.initialize(sys.argv)
   gmsh.model.add("x6")
   # The API provides access to all the elementary building blocks required to
   # implement finite-element-type numerical methods. Let's create a simple 2D
   # model and mesh it:
   gmsh.model.occ.addRectangle(0, 0, 0, 1, 0.1)
   gmsh.model.occ.synchronize()
   gmsh.model.mesh.setTransfiniteAutomatic()
   gmsh.model.mesh.generate(2)
   
   # Set the element order and the desired interpolation order:
   elementOrder = 1
   interpolationOrder = 2
   gmsh.model.mesh.setOrder(elementOrder)
   
   def pp(label, v, mult):
       print(" * " + str(len(v) / mult) + " " + label + ": " + str(v))
   
   # Iterate over all the element types present in the mesh:
   elementTypes = gmsh.model.mesh.getElementTypes()
   
   for t in elementTypes:
       # Retrieve properties for the given element type
       elementName, dim, order, numNodes, localNodeCoord, numPrimNodes =\
       gmsh.model.mesh.getElementProperties(t)
       print("\n** " + elementName + " **\n")
   
       # Retrieve integration points for that element type, enabling exact
       # integration of polynomials of order "interpolationOrder". The "Gauss"
       # integration family returns the "economical" Gauss points if available, and
       # defaults to the "CompositeGauss" (tensor product) rule if not.
       localCoords, weights =\
       gmsh.model.mesh.getIntegrationPoints(t, "Gauss" + str(interpolationOrder))
       pp("integration points to integrate order " +
          str(interpolationOrder) + " polynomials", localCoords, 3)
   
       # Return the basis functions evaluated at the integration points. Selecting
       # "Lagrange" and "GradLagrange" returns the isoparamtric basis functions and
       # their gradient (in the reference space of the given element type). A
       # specific interpolation order can be requested using "LagrangeN" and
       # "GradLagrangeN" with N = 1, 2, ... Other supported function spaces include
       # "H1LegendreN", "GradH1LegendreN", "HcurlLegendreN", "CurlHcurlLegendreN".
       numComponents, basisFunctions, numOrientations =\
       gmsh.model.mesh.getBasisFunctions(t, localCoords, "Lagrange")
       pp("basis functions at integration points", basisFunctions, 1)
       numComponents, basisFunctions, numOrientations =\
       gmsh.model.mesh.getBasisFunctions(t, localCoords, "GradLagrange")
       pp("basis function gradients at integration points", basisFunctions, 3)
   
       # Compute the Jacobians (and their determinants) at the integration points
       # for all the elements of the given type in the mesh. Beware that the
       # Jacobians are returned "by column": see the API documentation for details.
       jacobians, determinants, coords =\
       gmsh.model.mesh.getJacobians(t, localCoords)
       pp("Jacobian determinants at integration points", determinants, 1)
   
   gmsh.finalize()
   
   ```


## 额外网格数据，内部edge和face

1. ```python
   import sys
   import gmsh
   gmsh.initialize(sys.argv)
   gmsh.model.add("x7")
   # Meshes are fully described in Gmsh by nodes and elements, both associated to
   # model entities. The API can be used to generate and handle other mesh
   # entities, i.e. mesh edges and faces, which are not stored by default.
   gmsh.model.occ.addBox(0, 0, 0, 1, 1, 1)
   gmsh.model.occ.synchronize()
   gmsh.option.setNumber("Mesh.MeshSizeMin", 2.)
   gmsh.model.mesh.generate(3)
   # Like elements, mesh edges and faces are described by (an ordered list of)
   # their nodes. Let us retrieve the edges and the (triangular) faces of all the
   # first order tetrahedra in the mesh:
   elementType = gmsh.model.mesh.getElementType("tetrahedron", 1)
   edgeNodes = gmsh.model.mesh.getElementEdgeNodes(elementType)
   faceNodes = gmsh.model.mesh.getElementFaceNodes(elementType, 3)
   
   # Edges and faces are returned for each element as a list of nodes corresponding
   # to the canonical orientation of the edges and faces for a given element type.
   
   # Gmsh can also identify unique edges and faces (a single edge or face whatever
   # the ordering of their nodes) and assign them a unique tag. This identification
   # can be done internally by Gmsh (e.g. when generating keys for basis
   # functions), or requested explicitly as follows:
   gmsh.model.mesh.createEdges()
   gmsh.model.mesh.createFaces()
   
   # Edge and face tags can then be retrieved by providing their nodes:
   edgeTags, edgeOrientations = gmsh.model.mesh.getEdges(edgeNodes)
   faceTags, faceOrientations = gmsh.model.mesh.getFaces(3, faceNodes)
   
   # Since element edge and face nodes are returned in the same order as the
   # elements, one can easily keep track of which element(s) each edge or face is
   # connected to:
   elementTags, elementNodeTags = gmsh.model.mesh.getElementsByType(elementType)
   edges2Elements = {}
   faces2Elements = {}
   for i in range(len(edgeTags)): # 四面体的6个边
       if not edgeTags[i] in edges2Elements:
           edges2Elements[edgeTags[i]] = [elementTags[i // 6]]
       else:
           edges2Elements[edgeTags[i]].append(elementTags[i // 6])
   for i in range(len(faceTags)): # 四面体的4个面
       if not faceTags[i] in faces2Elements:
           faces2Elements[faceTags[i]] = [elementTags[i // 4]]
       else:
           faces2Elements[faceTags[i]].append(elementTags[i // 4])
   
   # New unique lower dimensional elements can also be easily created given the
   # edge or face nodes. This is especially useful for numerical methods that
   # require integrating or interpolating on internal edges or faces (like
   # e.g. Discontinuous Galerkin techniques), since creating elements for the
   # internal entities will make this additional mesh data readily available (see
   # `x6.py'). For example, we can create a new discrete surface...
   s = gmsh.model.addDiscreteEntity(2)
   
   # ... and fill it with unique triangles corresponding to the faces of the
   # tetrahedra:
   maxElementTag = gmsh.model.mesh.getMaxElementTag()
   uniqueFaceTags = set()
   tagsForTriangles = []
   faceNodesForTriangles = []
   for i in range(len(faceTags)):
       if faceTags[i] not in uniqueFaceTags:
           uniqueFaceTags.add(faceTags[i])
           tagsForTriangles.append(faceTags[i] + maxElementTag)
           faceNodesForTriangles.append(faceNodes[3 * i])
           faceNodesForTriangles.append(faceNodes[3 * i + 1])
           faceNodesForTriangles.append(faceNodes[3 * i + 2])
   elementType2D = gmsh.model.mesh.getElementType("triangle", 1)
   gmsh.model.mesh.addElementsByType(s, elementType2D, tagsForTriangles, faceNodesForTriangles)
   
   # Since the tags for the triangles have been created based on the face tags,
   # the information about neighboring elements can also be readily created,
   # useful e.g. in Finite Volume or Discontinuous Galerkin techniques:
   for t in tagsForTriangles:
       print("triangle " + str(int(t)) + " is connected to tetrahedra " +
             str(faces2Elements[t - maxElementTag]))
   
   # If all you need is the list of all edges or faces in terms of their nodes, you can also directly call:
   edgeTags, edgeNodes = gmsh.model.mesh.getAllEdges()
   faceTags, faceNodes = gmsh.model.mesh.getAllFaces(3)
   if '-nopopup' not in sys.argv:
       gmsh.fltk.run()
   gmsh.finalize()
   ```