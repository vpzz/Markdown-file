# 基础

1. Python的整型是变长存储的，不存在C语言中的溢出问题。

2. //表示除法向下取整，Python中的浮点数不区分单精度和双精度。

3. 布尔类型为False和True，开头大写。支持与，或，非运算。 2>1 and 2<3结果为True。and or not相当于C语言中的 && || ！

4. 4种基本数据类型：整型，浮点型，布尔型，字符串类型。

5. 条件判断：      if   elif   else后面要加冒号。

6. Python的函数可以一次return多个值，用逗号分隔。

7. 一个文件就是一个模块，可以把多个功能类似的函数或类放到一个文件中，供多个应用使用。

8. 使用时，import+文件名即可，调用函数的时候要用模块名.函数名的方式。也可以from 模块名 import 函数来只引入部分功能。

9. ```python
   import school as sc
   from school import score2grade as s2g
   from school import *
   ```

10. 使用第三方库时，如果发现有bug，或者想要某个函数实现别的功能，此时可以使用Python的继承功能。不建议直接修改库代码，因为该函数可能在别处有用到或者库更新后，修改会被覆盖。

11. 修改import，然后继承，重写要修改功能的程序。

12. ```python
    from school import student as _student
    class student(_student):
    	def xxx
    ```

13. 数据结构关注：时间和空间复杂度，时间尤其重要。

14. 例如利用函数递归来计算斐波那切数列，程序编制十分简单。

15. ```python
    def fib(n):
        if n<=2:
            return 1
        return fib(n-1)+fib(n-2)
    ```

16. 计算流程展开是树形结构，不同的分支存在重复计算。所需时间随着问题规模n的增加指数增加。自顶向下

17. 可以使用迭代的方式来避免重复计算。所需时间随着问题规模n的增加线性增加。自底向上

18. ```python
    def fib1(n):
        prev,curr = 1,1
        k = 2
        while k<n:
            prev,curr = curr,prev+curr
            k = k+1
        return curr
    ```

19. 常用算法的时间复杂度：O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)

20. python中有4种数据结构类型：list相当于线性表。tuple是只读列表，set是元素不重复的列表，dict是键值对。

21. 数据结构中学到的有链表，数组，二叉树，哈希表，图。

22. list 底层使用的是数组。链表和数组的区别是数组是挨个排放的，如果在头部插入，就得把数组整体向后移动。链表则对头尾插入不敏感。数组是单向的，链表是双向的。数组从尾部插入时间复杂度为O(1)，从头部插入时间复杂度为O(n)。O(1)表示和数组的长度n无关。链表从任何地方插入时间复杂度都是O(1)。

23. set底层使用的是哈希表。查找速率飞起，远比数组快得多。时间复杂度为O(1)。数组的查找是从头开始逐个查询。时间复杂度为O(n)。哈希表的方法是将待查询的数据送给hash函数，hash函数输出该数据应在的地址，直接根据地址查找该地址内是否存在该数。时间复杂度为 O(n)。

24. dict也是哈希表。

25. 树的查找算法复杂度为O(logn)，每询问一次，就将问题的规模缩减为原来的一半。

26. <img src="Python科学计算应用基础.assets/image-20200831211316165.png" alt="image-20200831211316165" style="zoom:50%;" />

27. 可以使用IPython自带的计时功能来对一行或一段代码进行性能分析：

    ```python
    # %timeit对该行重复执行多次（次数不定，如果单次执行时间太短，则会多次执行），然后给出统计值。会调用timeit模块来计时。
    # %time只会执行一次
    a = [1,2,3]
    %timeit a[1] = 5 #测量对列表元素赋值操作消耗的时间，20.9 ns ± 0.0998 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each) 可以看到执行了7轮，每轮1千万次。
    %time a[1] = 5 #结果为 CPU times: total: 0 ns Wall time: 0 ns，因为时间太短了，只有多次运行才能捕捉到这么小的时间间隔。
    
    # %%timeit作用于一段代码
    # %%time也是作用于一段代码
    %%timeit
    a = []
    for i in range(10):
        a.append(i)
    #结果为453 ns ± 4.61 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
    %%time
    a = []
    for i in range(10):
        a.append(i)
    #结果为 CPU times: total: 0 ns Wall time: 0 ns
    ```

# NumPy

1. numpy为python提供了真正的多维数组功能。

2. python自带的列表list可以保存一组类型不同的对象，因此实际保存的是指针。这对于数值计算来说浪费空间和时间。因此python又提供了array模块，只支持同类型对象，能直接保存数值，但是只支持一维数组。也没有各种配套的运算函数。

3. 一些科学计算库也接受python自带的序列类型，不过一般会先转化为ndarray对象，然后运算，结果输出也是ndarray对象。

4. ndarray对象的操作默认是逐元的，也就是说二维数组的乘法，要求维度相同，会进行对应元素的乘积。

5. 使用numpy可以利用python的编码便捷性（代码越少，出错也就越少），和预编译的C代码的高效性。

6. Numpy的两大特性：

   1. 向量化，使得可以使用`c=a*b`来表示同形状多维数组的对应元素乘积，使得代码简洁，省略很多显式的for循环，可读性强，和数学表达近似。

   2. 广播，使得不同维度的数组可以进行运算，例如二维数组和标量的乘积，可以将一个小的数组扩展到和大的数组同形状，然后借助向量化来计算。不过需要保证小数组的扩展不会造成歧义。

7. numpy同时支持面向过程和面向对象两种编程范式，因为ndarray对象可以使用它的类内的方法或全局函数来操作。不过numpy的成员方法不如numpy中的全局函数丰富。许多一元操作，例如sum，max都被实现为成员方法。

8. NumPy提供2种对象：

   1. ndarray：存储同类型数据的n维数组，这是NumPy的基本数据类型。

   2. ufunc：能够对上面数组进行处理的特殊函数，NumPy的所有函数都是围绕ndarray处理的。

   3. masked layers：掩码数组

   4. matrices：矩阵

9. 一维数组建议使用小写字母，多维数组建议使用大写字母。

10. numpy中也含有python内置或math模块中的数学运算函数。

11. print会将ndarray对象当作嵌套列表输出，一维数组当作行，二维数组当作矩阵，三维数组当作矩阵的列表。如果矩阵特别大时，会只输出角部的元素，省略的元素用...替代。

    ```python
    np.set_printoptions(threshold=sys.maxsize) #修改numpy的设置，使得不省略输出
    ```

12. 库版本查看：

    ```python
    import numpy as np #一般都使用这种方式导入
    np.__version__ #结果为str类型 '1.25.2'
    ```


## ndarray对象

1. 6种创建ndarray对象的方法：

   ```python
   #从python的其他序列类型转换
   np.array([1,2,3,4,5])
   #Numpy内置的数组创建函数
   np.ones((2,3))
   #通过复制，连接，更改现有的数组得到
   a = np.array([1, 2, 3, 4, 5, 6])
   b = a[:2]
   #从磁盘读入，可以手动指定格式，或者使用某些专用格式的标准库，例如h5py模块处理HDF5格式数据。
   #例如CSV文件内容如下
   x, y
   0, 0
   1, 1
   2, 4
   3, 9
   np.loadtxt('simple.csv', delimiter = ',', skiprows = 1)#掠过第一行，结果为一个4*2的数组
   #从字节数组创建
   np.fromfile()和np.tofile()配合使用
   #使用其他基于numpy的库会产生ndarray对象
   ```

2. np.array()可以接受一个列表或元组对象，创建一个numpy.ndarray类型的对象。

   ```python
   a1 = np.array([1,2,3,4,5]) #1维数组
   type(a1) # numpy.ndarray
   ```

3. 和列表不同的是，改变ndarray对象的大小会导致创建一个新的ndarray对象，然后删除旧的。允许创建包含python对象或ndarray对象的numpy数组。

4. ndarray对象的数据是按行存储的，和C语言多维数组一样，不过二者获取多维数组元素的方式不同，numpy使用元组作为下标，例如`a[1,2]`，等价于`a[(1,2)]`，C语言使用多次引用，例如`a[1][2]`，numpy也支持这种方式，不过效率比较低，因为会创建一个临时的中间对象`a[1]`。

5. 从下面四个求和运算分别花费的时间，可以看出使用全套的numpy的速度最快，其次是全套的Python。而交叉使用是比较差的，因为要先进行类型转化。

6. ```python
   L = [1.0 for i in range(10000000)] #所有元素的都是1.0
   sum(L)    #1  34.8 ms ± 1.31 ms
   np.sum(L) #2  353 ms ± 2.16 ms per loop
   L1 = np.array(L) #实际上这一步也要消耗不少时间 340 ms ± 642 µs，不过转换过后，后续都可以享受NumPy的高速计算
   sum(L1)    #3  618 ms ± 16.9 ms
   np.sum(L1) #4  10.6 ms ± 127 µs
   ```

7. ndarray对象的属性：

   ```python
   import numpy as np
   a1 = np.array([1,2,3,4,5])
   print(a1) #结果为 [1 2 3 4 5]
   a1.dtype   #结果为 dtype('int32')，根据平台的不同，有时可能是dtype('int64')
   type(a1.dtype) #结果为 numpy.dtypes.Int32DType
   a1.dtype.type  #结果为numpy.int32
   type(a1.dtype.type) #结果为type
   print(a1.flags)   #标志位，之所以要这么多标志，是为了效率优化。
     C_CONTIGUOUS : True
     F_CONTIGUOUS : True
     OWNDATA : True	#true表示这个变量a1拥有a1.data这个数据块。
     WRITEABLE : True
     ALIGNED : True	#对齐相关
     WRITEBACKIFCOPY : False
     UPDATEIFCOPY : False
   print(a1.shape)   #数组的形状，结果为 (5,)
   print(a1.strides) #每个维度元素之间的字节数间隔。实际是该维度元素的大小。结果为 (4,)
   print(a1.ndim)    #数组的维数，结果为 1
   print(a1.data)	  #存储的数据块的内存地址 结果为<memory at 0x0000000008F74280>，同一个数据块可以被不同的ndarray引用。
   print(a1.size)    #总的元素个数，等于shape的各个维度相乘。结果为 5
   print(a1.itemsize)#每个元素的字节数。结果为4。等价于a1.dtype.itemsize
   print(a1.nbytes)  #总的字节数，=itemsize*size。结果为20
   print(a1.base)    #表示data是复用的哪个变量，如果flags中的owndata是true，那么base就是none。结果为None
   ```

8. 由于Python对每个数据还要额外保存类型信息，numpy是统一保存，也可以节省空间。Python的源代码中，对于浮点数除了都是用double类型外，还保存了一个对象的头部信息，包含类型和引用次数等信息。

   ```c
   typedef strcut{
       PyObject_HEAD
       double ob_fval;
   }PyFloatObject
   ```

9. numpy自定义的基本数据类型，比C语言还丰富。

   ```python
   numpy.bool_  #布尔类型
   numpy.int_ #默认的整数类型，类似于C的long类型
   numpy.intc #与C的int类型一样
   numpy.intp #用于索引的整数类型，类似于C的ssize_t
   numpy.int8 int16 int32 int64 #4种带符号整数，python内置类型int等价于int32
   numpy.uint8 uint16 uint32 uint64 #4种无符号整数
   numpy.float_ #等价于float64
   numpy.float16 float32 float64 #半，单，双精度浮点数。python内置类型float等价于float64
   numpy.complex_ #等价于complex128
   numpy.complex64 complex128 #复数，实部和虚部分别为32和64位。
   #实际上numpy还把内置的类型都在其内部重命名了，例如numpy.bool就是内置类型bool，不过在1.20以后就不建议在使用numpy.bool了，推荐直接使用bool。
   ```

10. 对ndarray对象的真值测试会调用其`__bool__`特殊方法，如果数组的元素比1多，则会报错，因为此时是有歧义的，应该使用`all`或`any`方法。

11. 可以直接创建numpy类型的变量：

    ```python
    a = np.int16(200) #16位带符号数，范围为-32768到32767
    print(a*a) #-25536 IPython会提示发生了溢出。结果并不是40000-32767，而是带符号乘法的32位结果的低16位。
    #需要注意的是，numpy类型的变量运算速度比python内置类型要慢得多，不过批量计算的话，还是numpy快。
    a = 3.14
    b = np.float64(3.14)
    %timeit a*a #结果为 28 ns ± 0.788 ns
    %timeit b*b #结果为 61.3 ns ± 2.13 ns
    ```

12. 查看ndarray对象内存储的数据的类型。整型默认使用int32存储，浮点数默认使用float64存储。通过.nbytes属性来查看对象内所存储的数据占用的总字节数。这个数值除以元素个数，就是每个元素的字节数。

    ```python
    L = np.array([1,2,3,4])
    L.dtype   #结果为 dtype('int32')
    L.nbytes  #结果为 16，因此每个元素占用16/4=4个字节
    #astype函数并不会修改原来的对象，而是返回一个新的对象。
    L1 = L.astype(np.int64) #修改存储的数据类型，也就是强制类型转换。np.int64是type类型
    L1.dtype  #结果为 dtype('int64')
    L1.nbytes #结果为 32，因此每个元素占用32/4=8个字节
    ```

13. 不推荐直接修改对象的dtype属性，因为这样只会更改解释对象内存储内容的方式，而不会类型转换：

    ```python
    L = np.array([1,2], dtype = np.int64)
    print(L) #结果为 [1 2]
    L.nbytes #结果为 16
    L.dtype = np.int32 #并不会报错，但是十分危险
    print(L) #结果为 [1 0 2 0]
    L.nbytes #结果为 16，可以看到数据的总长度并没有变化
    
    #在修改类型前，L在内存中以小端形式存储，分别为
    # 01 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00
    #每8个字节作为一个数。修改类型后，每4个字节作为一个数，则为1 0 2 0
    ```

14. 可以通过dtype参数在创建ndarray时指定类型。dtype参数也接收字符串形式，每种数值类型都有几种字符串表示方式。

    ```python
    L = np.array([1,2], dtype = int) #可以使用内置类型，例如int,float,complex，也可以使用numpy自定义的例如int32等，前者会自动转化为后者。
    L.dtype #结果为dtype('int32')
    # np.typeDict可以获得如下字典，不过该功能已经在numpy1.25.0中被删除了。
    {'?': numpy.bool_,
     0: numpy.bool_,
     'byte': numpy.int8,
     'i': numpy.int32,
     5: numpy.int32,
    ...
    }
    #使用如下命令将字典中的值提取出来，set可以去重。
    set(np.typeDict.values()) #结果为 {numpy.bool_, numpy.int8, ...}
    ```

15. 不同dtype的数组之间运算时，会先转化为同类型的数组：

    ```python
    a = np.array([2, 3, 4], dtype=np.uint32)
    b = np.array([5, 6, 7], dtype=np.int32)
    c = a + b #c.dtype为dtype('int64')，会选择一个能够同时容纳两个类型的类型。
    ```

16. 将python内置的列表或元组转化为ndarray对象，效率比较低，可以选择直接创建ndarray对象：

    ```python
    np.arange(0,1,0.1) #结果为array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])，类似于内置函数range，都不包括终值。不过range函数的参数必须都是整数，且它的返回值并不是list或tuple，而是一个range对象，还需要再封装一下。
    #和range的用法一样，不同的是他返回的是ndarray对象而不是range对象，同时Python自带的range所有参数只支持整数
    #不过由于range的步长可以是浮点数，而浮点数存在精度问题，因此可能不一定会产生对应数量的元素。因此建议使用linspace
    np.linspace(0,1,11) #结果为array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])，包括终值，均匀分隔，一共11个点。dtype为numpy.float64
    np.linspace(0,1,10,endpoint=False) #结果为array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])。不包含终值，一共10个点。
    np.logspace(0,3,4) #结果为 array([   1.,   10.,  100., 1000.])。产生10^0到10^3之间的等比数列，包括终值，一共4个点。相当于pow(10,np.linspace(0,3,4))的结果。
    np.logspace(0,3,4,base=2) #结果为 array([1., 2., 4., 8.])。指定基为2，范围变成了2^0到2^3
    np.geomspace(1, 8, num=4) #等比数列，起点为1，终点为8，结果为array([1., 2., 4., 8.])
    ```

17. 从字符串或文件创建一维数组：

    ```python
    s = "abcdefg"
    np.fromstring(s,dtype=np.int8) #结果为 array([ 97,  98,  99, 100, 101, 102, 103], dtype=int8)，不过已经不推荐使用了，推荐用frombuffer替代
    ```

18. 创建已填充值的数组，以下默认都是numpy.float64类型：

    ```python
    np.empty((2,3)) #创建一个2行3列的二维数组，不进行初始化，，数值为内存中原来的随机值，速度最快。
    np.zeros((2,3)) #全0
    np.ones((2,3))  #全1
    np.full((2,3),np.pi) #用np.pi初始化
    np.eye(3) #创建3阶单位方阵
    np.eye(3, 5) #创建3行5列的单位矩阵，相当于3阶方阵，然后再扩展2列
    np.eye(3,k=1) #主对角线向上移动1格，结果为
    array([[0., 1., 0.],
           [0., 0., 1.],
           [0., 0., 0.]])
    np.diag(x) #如果x是矩阵，则返回主对角线元素构成的向量。如果x是一个向量，那么构造一个方阵，使之主对角线的元素为x，其他元素为0。
    np.trace(x) #主对角线元素的和
    x = np.array([1, 2, 3, 5])
    N = 3
    np.vander(x, N) #创建一个范德蒙矩阵，结果为
    array([[ 1,  1,  1],
           [ 4,  2,  1],
           [ 9,  3,  1],
           [25,  5,  1]])
    #以上函数都有_like版本
    a = np.arange(15).reshape(3,5)
    np.ones_like(a) #结果的shape和a一样。
    ```

19. ndarray对象的strides跨步属性保存的是每个维度的上，相邻（该维度下标相差1）两个元素的地址差，也就是ndarray的data属性：

    ```python
    #如果strides的值正好和该维度所占用的字节数相同，则数据是连续存储的。通过切片下标获得数组是原数组的一个视图，但是二者的strides不同。
    a = np.array([1,2,3,4,5,6]).reshape((2,3)) #2个维度，长度分别为2和3。
    a.strides #结果为(12,4) 默认按行存储，a[0,0]和a[1,0]相差3个int32元素，即3*4=12字节。a[0,0]和a[0,1]相差1个int32元素，即1*4=4字节。
    
    #这个16表示a2[0]和a2[1]头部相差的字节数，表示a2[0]或a2[1]的大小，1个元素4个字节，4个元素一共16字节。这个4表示a2[0][0]和a2[0][1]头部相差的字节数，即a2[0][0]的大小，1个元素就是4个字节。
    
    #通过strides可以从a[i,j]的地址A得到a[i+m,j+n]的地址B，B=A+m*12+n*4
    ```

20. NumPy默认使用C语言的数组排序，即按行存储。也可以在创建时设置order参数，使用Fortran的按列存储顺序。

21. 高维数组的索引：

    ```python
    a = np.ones((2, 3, 4)) #创建一个3维数组a，a[0]和a[1]都是是一个3*4的二维数组。a[0]等价于a[0,:,:]
    x = np.arange(15).reshape(3,5) #x为如下
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
    x[:2,:3] #结果如下，相当于x的2个维度同时索引，也就是一个子矩阵
    array([[0, 1, 2],
           [5, 6, 7]])
    x[:2][:3] #结果如下，相当于x[:2,:][:3,:],会分两步索引，第一步得到前两行构成的子矩阵，第二部会在上一步子矩阵的基础上，得到前3行构成的子矩阵，因为第一部的子矩阵只有2行，因此第二步的结果和第一步一样。
    array([[0, 1, 2, 3, 4],
           [5, 6, 7, 8, 9]])
    #因此还是推荐使用numpy自带的索引模式。
    ```

22. np支持修改数据的存储方式，大小端：

    ```python
    import numpy as np
    a1 = np.array([i+1 for i in range(8)])
    a1.dtype = '>i2' # <表示小端 >表示大端， int8 in16 in32 int64可以用 i1 i2 i4 i8来替代。
    a1
    Out[5]: 
    array([ 256,    0,  512,    0,  768,    0, 1024,    0, 1280,    0, 1536,
              0, 1792,    0, 2048,    0], dtype=int16)
    ```

23. 数据拷贝的情况：

    1. 函数传参和变量赋值不会导致numpy数据的复制：

       ```python
       a = np.array([0,  1,  2,  3])
       b = a #不会复制
       b is a #True，同一个ndarray对象的两个名字而已。is操作符比较的是两个对象的id
       def f(x):
           print(id(x))
       f(a) #2543492345424
       id(a) #2543492345424
       ```

    2. 使用view方法来和一个已有的ndarray对象共享数据，可以认为是浅拷贝：

       ```python
       a = np.array([0,  1,  2,  3])
       c = a.view() #type(c)也是numpy.ndarray类型
       c == a #结果为array([ True,  True,  True,  True])，二者的元素完全一样
       c is a #False，因为二者的id不同，是两个对象
       c.base is a #True，可以认为c的所有索引都会代理给a。
       c.flags.owndata #结果为False，c不拥有数据，数据实际是a拥有
       c = c.reshape((2, 2)) #不会改变a的shape
       c[1, 1] = 1234 #但是会改变a的数据
       ```

    3. 对一个数组使用切片也会返回它的一个视图：

       ```python
       a = np.array([0,  1,  2,  3])
       s = a[:2]
       s.base is a #True
       ```

    4. 使用copy方法来进行深拷贝：

       ```python
       a = np.array([0,  1,  2,  3])
       d = a.copy() #拷贝对象本身和它的数据
       d is a #False
       d.base is a #False
       d[0] = 5 #对d的修改不会影响到a本身。
       d.flags.owndata #True，d自己拥有数据
       #如果a是一个中间结果，b是a的切片，也是最终需要的结果，建议在切片后进行深拷贝，然后删除a，这样可以减少内存空间占用。
       #新的数组的WRITEABLE标志会被设置为True
       a = np.arange(int(1e8))
       b = a[:100].copy() #如果没有对b进行深拷贝，就del a则会导致b的数据发生危险，虽然不一定立即影响b的使用，b会在垃圾清理之后变得不可用。
       del a #如果对b进行深拷贝后，没有del a，则a的内存不会释放。
       ```

24. 数组的邻接连续Contiguous的2个条件：

    1. 数组占据一块连续的空间
    2. 下标大的元素的地址也大，意味着每一维的stride都是非负的。

25. ndarray对象的内部内存布局：

    1. 该对象由两部分组成，内存中的一段连续的空间（可能是自己的或其他对象的）和一个索引模式，可以将N个整数映射到一个内存地址上。
    2. 这N个整数中每个的范围由shape属性约束。
    3. Numpy支持多种带跨步的索引模式（strided indexing scheme）。N维索引，$(n_0,n_1,...,n_{N-1})$对应的地址偏移为：$\sum_{k=0}^{N-1}s_kn_k$。其中$s_k$为每一个维度的stride。
    4. 最常见的有两种索引模式，行优先（C风格的）和列优先（Fortran和Matlab风格）。
    5. 通过dtype属性来确定该内存地址的数据占用多少字节，如何解析字节。

26. C风格的strides计算方法：$s_k = itemsize\times \prod_{j=0}^{k-1}d_j$，F风格的strides计算方法：$s_k = itemsize\times \prod_{j=k+1}^{N-1}d_j$，其中$d_j=self.shape[j]$，也就是第`j`维的尺寸。

27. C风格和F风格：

    ```python
    x = np.array([[1,2,3],[4,5,6]], order='C') #默认就是C
    y = np.array([[1,2,3],[4,5,6]], order='F')
    #二者的shape都是(2,3)
    x == y #结果为True，也就是说x[i,j] == y[i,j]
    #可以见在使用上没有任何区别
    z = x + y #结果如下，可以见运算也是可以正常进行的。
    array([[ 2,  4,  6],
           [ 8, 10, 12]])
    z.flags["C_CONTIGUOUS"] # 结果为True，可见，默认生成的都是C风格的。
    yc = y.copy() # yc.flags["C_CONTIGUOUS"]的结果也是True。因为copy方法有一个默认参数是order，默认值为"C"。"F"表示使用Fortran风格，"A"表示和原来的保持一样。
    x.shape #结果为(2,3)
    x.strides #s_0 = 4×(1)=4，s_1 = 4×(2=8)
    
    ```

28. 高级索引会产生新的数据，因此其strides可能会和原有的数组不同，shape也不一样了

    ```python
    x = np.array([[ 0,  1,  2],
                  [ 3,  4,  5],
                  [ 6,  7,  8],
                  [ 9, 10, 11]])
    rows = [0, 3]
    columns = [0, 2]
    newx = x[np.ix_(rows, columns)] #新数组也是默认的C邻接
    x.shape #结果为 (4, 3)
    x.strides #结果为 (12, 4)
    newx.shape #结果为 (2, 2)
    newx.strides #结果为 (8, 4)
    ```

## 形状

1. 数组的形状可以通过ndarray.shape属性获得，结果为描述各个维度元素数量的元组：

   ```python
   a1 = np.array([1,2,3,4,5]) #1维数组
   a1.shape #结果为 (5,)，表示该元组只有一个元素，括号内的逗号不能省略，否则会被当作单个整数。
   a2 = np.array([[1,2,3],[4,5,6]]) #2维数组
   a2.shape #结果为 (2,3)
   a2[1,0] #第1行，第0列的元素，结果为 4
   1 2 3
   4 5 6
   ```

2. 可以直接对数组的shape属性进行修改，不过不会修改内存中的数据，也不是将二维数组表示的矩阵转置（转置会交换实际数据）。如果某一个维度的大小被设置为了-1，则会自动计算：

   ```python
   a = np.array([[1,2,3],[4,5,6]])
   1 2
   3 4
   5 6
   a.shape = (3,2)
   a[1,0] #第1行，第0列的元素，结果为 3
   #类似于a.reshape((3,2))，但是reshape并不修改a本身，而是将结果返回。reshape的两个数组共享同一块内存数据，不过a的flags中OWNDATA为true，而b的flags中OWNDATA为false
   a = np.array([1,2,3,4,5,6])
   b = a.reshape((3,2))
   a[2] = 10
   print(b[1,0]) #结果为 10
   a.resize((3,2)) #修改a本身
   a.ravel() #平坦化，相当于a.reshape(-1)，如果a是其他数组的一个非连续切片，这一步可能会产生元素的复制。
   ```

3. 数组的转置：

   ```python
   a = np.array([[1,2,3],[4,5,6]])
   a.data == a.T.data #结果为False，都是memoryview对象，而该对象内保存了邻接性。
   a.flags #结果为
     C_CONTIGUOUS : True #默认是C连续的
     F_CONTIGUOUS : False
     OWNDATA : True      
     WRITEABLE : True    
     ALIGNED : True
     WRITEBACKIFCOPY : False
   a.T.flags #结果为
     C_CONTIGUOUS : False
     F_CONTIGUOUS : True #且现在是Fortran连续的
     OWNDATA : False #可以看到不拥有数据
     WRITEABLE : True
     ALIGNED : True
     WRITEBACKIFCOPY : False
   #如果没有指定axis，那么如下结果恒成立
   transpose(a).shape == a.shape[::-1]
   ```

4. 一维数组可以看作是行向量，列向量实际上是只有一列的二维数组。

5. reshape函数可以变换维度，而不改变数据，只是改变了解析数据的方式，所以速度很快。

6. 如果reshape只传递一个参数`(-1,)`，则会将该数组变为1维数组。

7. 二维数组最原始的理解应该是把一行或者一列数据进行分割，它和矩阵的关系不是天然的。

8. 可以看到默认的1维数组可以看做列向量，因为他的shape是（9，)，如果要是和二维数组的shape含义统一，那么这个（9，）就表示（9，1）即9行1列，即是一个列向量。这两个还是不同的，(9,1)表示1维数组，(1,9)表示2维数组。遍历的时候需要注意。可以使用reshape来转换行列向量：

   ```python
   import numpy as np
   a1 = np.array([1,2,3,4,5]) #行向量，shape为(5,)，ndim为1
   a2 = a1.reshape(1,5) #一列的矩阵，shape为(1, 5)，ndim为2
   a3 = np.array([[1, 2, 3, 4, 5]]) #可以直接创建一列的矩阵，在原来的列表外边再加上一个[]即可
   ```

9. reshape还是复用内存块。如果不想复用，可以使用.copy()函数

10. ```python
    a3 = a1.copy()
    a3.flags
    Out[10]: 
      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : True
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False
      UPDATEIFCOPY : False
    ```

## 索引

1. ndarray可以和列表一样进行切片操作，二者的用法和效果一摸一样，不同的是，ndarray通过整数或切片获得的只是原始数组的一个视图，二者共享数据，而list是复制了一份新的数据。

   ```python
   a1 = np.array([1, 2, 3, 4])
   a2 = a1[0:2] #a2.flags的OWNDATA为false，而a1.flags的OWNDATA为true
   a2[1] = 10 #此时a1也会变成[1, 10, 3, 4]
   ```

2. 切片中的省略：

   ```python
   #假设切片对应的维度一共有n个元素
   a[::] #等价于a[:],都是a[slice(None,None,None)]
   slice(None,None,None) #相当于slice(0,n,1)
   slice(None,j,k) #如果k>0，相当于i = 0, 否则相当于i = n-1
   slice(i,None,k) #如果k>0，相当于j = n, 否则相当于i = -n-1
   slice(i,j,None) #如果省略k，那么k默认为1
   ```

3. 高级索引（FancyIndex）：除了python序列本身就支持的整数或切片索引外，numpy还支持使用整数列表（数组）和布尔列表（数组）来获取不连续下标的元素，这不能称为切片操作，列表也不支持这一操作。这称之为高级索引。通过这一方式获得的数组不和原数组共享数据，但是可以通过对它的复制该改变原来的数据：

   ```python
   #高级索引的特点是：索引对象是非元组的序列对象，dtype为整数或布尔类型的ndarray对象
   x = np.array([10,  9,  8,  7,  6,  5,  4,  3,  2]) #
   x[(1, 2, 3),] #选择对象为一个元组，即((1,2,3),)，该元组只有一个元素，也是一个元组。元组形式的选择对象会被拆包，因此等价于x[[1,2,3]]，结果为array([9, 8, 7])
   x[(1, 2, 3)]  #等价于x[1,2,3]
   x[np.array([3, 3, 2])]  #结果为 array([7, 7, 8])，等价于x[[3, 3, 2]]，但是不等于x[(3, 3, 2)]，因为后者会自动对元组进行拆包，等价于x[3, 3, 2]，将x当作一个3维数组，因此会报错。
   ```

4. 如果用于索引的整数列表是多维的：

   ```python
   a = np.array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100, 121])
   j = np.array([[3, 4], [9, 7]])
   a[j] #结果如下，结果为一个分块矩阵，块形状和j一样，每个元素分别为a[?]，其中?分别为对应位置的j的取值。即a[j][k,m,...] == a[j[k,m,...]]。这里实际上是只考虑a的第0维，因为j[k,m,...]是一个具体的数。
   array([[ 9, 16],
          [81, 49]])
   #palette为调色板，二维数组
   palette = np.array([[0, 0, 0],         # black
                       [255, 0, 0],       # red
                       [0, 255, 0],       # green
                       [0, 0, 255],       # blue
                       [255, 255, 255]])  # white
   image = np.array([[0, 1, 2, 0],  # 索引图像中存储的像素颜色
                     [0, 3, 4, 0]])
   palette[image] #结果是一个三维数组，shape为(2,4,3)，可以看作2*4的2维数组，每个元素都是一个颜色三元组，也就是palette中的一个元素。
   ```

5. 用于索引的整数列表也可以是多个：

   ```python
   a = np.array([[ 0,  1,  2,  3],
                 [ 4,  5,  6,  7],
                 [ 8,  9, 10, 11]])
   i = [[0, 1],[1, 2]]
   j = [[2, 1],[3, 3]]
   a[i, j] #要求每个维的列表的形状必须一样，i.shape == j.shape 为True，或者可以广播成一样也行。结果为array([[ 2,  5],[ 7, 11]])
   #结果的形状和i或j一样，a[i, j][k,m,...] = a[i[k,m,...], j[k,m,...]]，例如a[i,j]的[0,0]就是a[i[0,0], j[0,0]]。
   #和一维的不同，多维情况下a[np.array([i,j])]会报错，必须写成a[i,j]或a[tuple(np.array([i,j]))]
   a[i, 2] #会将标量2扩展为和i同形状的数组，等价于a[i, np.ones_like(i)*2]
   a[:, j] #相当于np.array([a[0,j], a[1,j], a[2,j]])
   a[i] #等价于a[i,:] 不等于 np.array([a[i,0], a[i,1], a[i,2], a[i,3]])
   ```

6. 布尔索引：

   ```python
   a[[True,False,True,False]] #结果为 array([1, 3])，获取第0和2个元素。这个操作在numpy1.10之前，会将True和False分别当作1和0，套用整数列表的方法。
   a[[1,0,1,0]] #结果为 array([2, 1, 2, 1])，不会自动当作布尔数组。
   #布尔数组和列表的形状尺寸需要和原数组一模一样，索引的结果都是一维数组。布尔数组一般不是手动构造的，而是通过函数运算得来的，例如
   x = np.array([5, 7, 7, 1, 0, 3])
   x[x>5] #筛选出>5的值，结果为 array([7, 7])
   x[x>5] = 0 #赋值会改变x本身，将x中比5大的元素都设为0，结果为 array([5, 0, 0, 1, 0, 3])
   #不过这种修改可以通过reshape为1维，再直接修改，然后再reshape回来，比较简单。.flat属性也可以获得该多维数组的C风格的一维视图，这样就可以省略2次reshape的过程。
   x = np.array([[0, 1], [1, 1], [2, 2]])
   a = x == 1 #结果为
   array([[False,  True],
          [ True,  True],
          [False, False]])
   #如果要将x中值为1的元素都设置为-1，则可以使用
   x[a] #相当于x[a.nonzero()]，其中a.nonzero()为(array([0, 1, 1], dtype=int64), array([1, 0, 1], dtype=int64))
   #布尔索引可以和整数索引联合使用
   x = np.array([[ 0,  1,  2],
                 [ 3,  4,  5],
                 [ 6,  7,  8],
                 [ 9, 10, 11]])
   rows = (x.sum(-1) % 2) == 0 #结果为array([False,  True, False,  True])
   columns = [0, 2]
   np.ix_(rows, columns) #结果为(array([[1],[3]]), array([[0, 2]])) ，因此rows的作用就相当于[1,3]
   ```

7. 使用slice生成切片对象，可以用该对象来取切片：

   ```python
   a = np.array([1, 2, 3, 4])
   idx = slice(None,None,2) #idx等价于::2
   a[idx] #结果为 array([1, 3])
   #使用python内置的
   ```

8. numpy还提供了一个更方便的方法来创建slice对象：

   ```python
   np.s_[::2,2:]  #等价于(slice(None, None, 2), slice(2, None, None))。2个slice对象构成的元组，可以作为二维数组的下标。
   #s_并不是np的一个函数，而是一个IndexExpression类的对象，对该对象使用[]下标语法，会调用它的__getitem__(self, index)方法。
   ```

9. ndarray对象除了支持元组索引的方式来获取多维数组的元素，还支持python自带的索引方式：

   ```python
   a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #定义了一个3维数组，shape为(2,2,3)
   a[0] == a[0,:,:] #结果为2*3的全为True的二维数组，前者为python的风格，后者为numpy风格。二者都是：array([[1, 2, 3], [4, 5, 6]])
   a[0][1] == a[0,1,:] #结果为1*3的全为True的二维数组。二者都是array([4, 5, 6])
   ```

10. 多维数组的每个维度都接收一个切片或索引，如果有的维度没有指定，则用：替代。python允许使用`...`来补全索引元组：

    ```shell
    #假设x为5维数组
    x[1,2,...] #等价于x[1,2,:,:,:]
    x[...,3] #等价于x[:,:,:,:,3]
    ```

11. 对多维数组进行迭代时，是将其当作一维数组看待的，即只对第0维进行迭代：

    ```python
    a = np.array([[1,2,3],[4,5,6]])
    for row in a:
        print(row) #分两次输出[1 2 3]和[4 5 6]
    #a.flat可以获得将其看作一维数组的迭代器
    for ele in a.flat:
        print(ele) #依次输出1 2 3 4 5 6
    ```

12. 索引的结果可以直接进行赋值，修改的是原数组的数据，不过等号两侧的形状要相同，或者通过广播可以变得相同：

    ```python
    a = np.arange(5)
    a[[1, 3, 4]] = 0#此时a为array([0, 0, 2, 0, 0])
    a[[0, 0, 2]] = [1, 2, 3] #如果列表有重复的元素，则会进行多次赋值。不过不建议这么使用
    ```

13. 使用where来获得满足特定条件的元素的索引：

    ```python
    a = np.array([[0, 1, 2],[3, 4, 5]])
    indices = np.where(a % 2 == 0) #获取a中偶数元素的索引，结果为(array([0, 0, 1]), array([0, 2, 1])，表示3个元素
    a[indices] #结果为 array([0, 2, 4])
    ```

14. 网格：

    ```python
    #numpy.ix_的参数为多个1维数组，可以是整数或布尔类型，
    np.ix_([1,3],[2,5]) #结果为一个包含2个数组的元组(array([[1],[3]]), array([[2, 5]])) 第一个为2*1，第二个为1*2
    
    x = [0,2,3]
    y = [1,4]
    mx, my = np.meshgrid(x, y) #创建网格，接收多个一维序列，
    #mx为
    array([[0, 2, 3],
           [0, 2, 3]])
    #my为
    array([[1, 1, 1],
           [4, 4, 4]])
    ix, iy = np.ix_(x,y)
    #ix为
    array([[0],
           [2],
           [3]])
    #iy为
    array([[1, 4]])
    #当把ix和iy当作索引时，会分别进行列复制和行复制为ixx和iyy。
    ixx = array([[0],[0]
                 [2],[2]
                 [3],[3]])
    iyy = array([[1, 4],
                 [1, 4],
                 [1, 4]])
    Matrix = np.array([[ 0,  1,  2,  3,  4], 
                       [ 5,  6,  7,  8,  9], 
                       [10, 11, 12, 13, 14], 
                       [15, 16, 17, 18, 19]])
    Matrix[tuple(np.meshgrid(x, y))] #由于meshgrid的结果是list，因此必须要转成tuple，否则会出错，结果为
    array([[ 1, 11, 16],
           [ 4, 14, 19]])
    Matrix[np.ix_(x,y)] #结果如下，可以发现二者互为转置。不过.T的转置并非是修改数据，而是修改CONTIGUOUS标志属性，可以看作是原数组的一个view。
    array([[ 1,  4],
           [11, 14],
           [16, 19]])
    #可以看到ix_是C风格的，行优先。而meshgrid是Fortran风格的，列优先。
    ```

## 广播

1. 广播使得通用函数可以处理shape不一样的两个数组，广播需要遵守两个规则：

2. 由于广播过程会在C语言级别进行，因此它的速度比直接在python中给出广播后的结果更快。广播并不会实际产生复制的数据，因为复制的数据都是重复的，没有必要。

3. numpy会从后往前，依次比较待运算的两个数组的每一个维度的尺寸，如果一个是1或，二者相等，则认为是相同的。前者需要广播成后者的样子，一维一维处理。否则会产生异常`ValueError: operands could not be broadcast together`。

   ```python
   a = np.array([1,2,3,4,5,6]).reshape(2,3)
   b = np.array([1,2,3]).reshape(1,3)
   a + b #b会被广播成(2,3)，通过复制第一行的方式完成
   ```

4. 代运算的两个数组的维度不一定要相等。缺失维度的尺寸默认是1，可以和任意大小兼容。先用1将维度扩充成相同的数量，然后从后往前，依次广播。

   ```python
   A      (4d array):  8 x 1 x 6 x 1
   B      (3d array):      7 x 1 x 5 #广播为1 x 7 x 1 x 5，从后往前进行。
   Result (4d array):  8 x 7 x 6 x 5 #A和B运算产生Result
   
   A      (2d array):  5 x 4
   B      (1d array):      1 #(1, 1)→(1, 4)→(5, 4)
   Result (2d array):  5 x 4
   
   A      (2d array):      2 x 1
   B      (3d array):  8 x 4 x 3 #倒数第二个维度不兼容，无法广播，会报错
   ```

5. 标量的shape为`()`，可以和任意数组兼容，相当于任意多个尺寸都是1的维度。

6. 例子：

   ```python
   a = np.array([[1,2,3],[4,5,6]])
   a = 10 #并不是给a的所有元素都复制为10，而是将变量a重新绑定到10上，这会导致ndarray对象被垃圾回收。
   x = np.array([[ 0,  1,  2],
                 [ 3,  4,  5],
                 [ 6,  7,  8],
                 [ 9, 10, 11]])
   #想要获取4个角点的元素构成的2*2的矩阵
   #手动给出不需要广播的结果
   rows = [[0, 0], [3, 3]]
   columns = [[0, 2], [0, 2]]
   x[rows, columns] #结果为array([[ 0,  2],[ 9, 11]])
   #自动广播
   rows = [[0], [3]]
   columns = [[0, 2]]
   x[rows, columns] #结果和上面的一样，不同的是，这里发生了广播，因为rows为2*1，而columns为1*2。二者都会被广播为2*2。
   broadcasted_rows = [[0,0],[3,3]] #向右复制一列
   broadcasted_columns = [[0, 2],[0, 2]] #向下复制一行
   x[rows, columns] == x[broadcasted_rows, broadcasted_columns]
   #使用numpy.ix_()函数来快速构造
   rows = [0, 3]
   columns = [0, 2]
   np.ix_(rows, columns) #结果就是一个2元组，分别为array([[0],[3]])和array([[0, 2]])。因为是元组，因此可以直接送入索引
   x[np.ix_(rows, columns)] #也可以得到正确的结果
   ```

## ufunc

1. 对于那些包含axis参数的数组方法，默认是None，此时会将数组当作一个一维数组看待。

2. 用随机数填充，numpy自带的随机数库为np.random

   ```python
   np.random.randint(0,10)  #生成一个随机整数，不会取到10，但会取到0。均匀分布
   np.random.randint(0,10,size=(4,5))   #使用size来生成多个值，构成多维数组。size关键字可以省略
   np.random.seed(555) #每次生成随机数的时候，都会使用种子，如果没有设置（紧挨着这个生成的函数前设置才有效），就使用当前时间，如果种子一样，那么随机序列也是一样的。每次生成完成依次随机数，都会修改种子，所以要复现，就必须在每次生成前都设置一下随机数。在软件测试时会使用种子，确保测试环境的可重复性。
   np.random.randint(0,10,size=(4,5))
   np.random.random(10)   #生成0到1之间的浮点数，10表示size参数。均匀分布
   np.random.normal(10,1,(5,5))   #均值，标准差，默认是标准正态分布，均值为0，标准差为1。也就是说从正态分布中选取5*5=25个数值，构成5*5的二维数组。
   ```

3. 合并（只能在维度相同的方向上进行合并）和分割（可以通过切片来完成，默认是复用原来的数据），不建议对二维以上的数组使用这些函数，逻辑很复杂。

   ```python
   import numpy as np
   #stack系列函数接收一个可迭代对象，逐个取出，按照规定方式合并
   a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(2,4)
   a2 = np.arange(10,18).reshape(2,4)
   np.vstack([a1,a2])   #垂直方向合并，需要列数相同。可以用np.concatenate([a1,a2])。结果为
   array([[ 1,  2,  3,  4],
          [ 5,  6,  7,  8],
          [10, 11, 12, 13],
          [14, 15, 16, 17]])
   np.hstack([a1,a2])    #水平方向合并，需要行数相同。可以用np.concatenate([a2,a3],axis=1)，结果为
   array([[ 1,  2,  3,  4, 10, 11, 12, 13],
          [ 5,  6,  7,  8, 14, 15, 16, 17]])
   a3 = np.array([30, 31])
   np.hstack([a1,a3.reshape(2,1)])  #在进行合并的时候，向量默认看做是一个只有一行的矩阵，而不是列向量，所以此处需要reshape。结果为
   array([[ 1,  2,  3,  4, 30],
          [ 5,  6,  7,  8, 31]])
   a = np.array([4, 2])
   b = np.array([3, 8])
   np.column_stack([a, b]) #结果如下，实际上是将行向量当作列向量来按列组合。因此不建议将向量当作矩阵使用。
   array([[4, 3],
          [2, 8]])
   np.hstack([a, b]) #结果为array([4., 2., 3., 8.])，和上面的结果不同
   #比较诡异的是
   np.column_stack is np.hstack #结果为 False
   np.row_stack is np.vstack #结果为 True
   
   x1,x2,x3 = np.split(a1,[2,5])  #第二个参数是分割点的下标，分割点归后一段。返回的是一个包含ndarray的list
   print(x1,x2,x3)
   [1 2] [3 4 5] [6 7 8]
   ```

4. 组装分块矩阵：

   ```python
   #使用block函数从嵌套的块中组装矩阵
   A = np.eye(2) * 2
   B = np.eye(3) * 3
   np.block([[A,np.zeros((2, 3))],[np.ones((3, 2)),B]]) #分块矩阵为2行2列，用户需要保证各块之间的兼容性，结果为
   array([[2., 0., 0., 0., 0.],
          [0., 2., 0., 0., 0.],
          [1., 1., 3., 0., 0.],
          [1., 1., 0., 3., 0.],
          [1., 1., 0., 0., 3.]])
   ```

5. 矩阵运算：默认的操作都是针对数组的，矩阵运算要使用特殊的函数，例如：

   ```python
   A.dot(B) #矩阵乘法A×B，需要前一个矩阵的列数=后一个矩阵的行数。python3.5后支持A@B
   A*B      #数组乘法，需要数组的shape完全相同，否则会报错
   A.T #数组转置，和矩阵的转置是一样的，结果为A的一个视图。等价于transpose(a)
   np.linalg.inv(A) #求逆矩阵
   np.linalg.pinv(A) #求伪逆，非方阵可以使用
   ```

6. 矩阵可以和向量的乘法，Numpy中可以和矩阵做乘法的向量有3种：

   ```python
   A = np.array([[1,2],[3,4],[5,6]]) #shape为(3,2)
   b1 = np.array([[5],[6]]) #shape为(2,1)，A.dot(b1)可以正确执行，(3,1)的矩阵也是最推荐的。
   b2 = np.array([[5,6]])   #shape为(1,2)，是一个2维数组，A.dot(b2.T)和A.dot(b1)等价，结果同上，都是array([[17],[39],[61]])。
   #以上两种都是推荐的方法
   b3 = np.array([5,6])     #shape为(2,)，是一个1维数组，也称作行向量。b3.T也是np.array([5,6])。不过A.dot(b3)和A.dot(b3.T)也都是可行的，结果为(3,)，都是array([17, 39, 61])。
   A.dot(b3) == A.dot(b1).T #结果为True，这里只能对后者进行转置，因为前者转置不变。
   #注意上面的矩阵和行向量的乘法，也不是左乘，这里都是右乘。
   ```

7. 三维矢量的叉乘：

   ```python
   import numpy as np
   G_1 = np.array([1, 0, 0])
   G_2 = np.array([0, 1, 0])
   G_3 = np.cross(G_1, G_2) #可得G_3 = array([0, 0, 1])
   ```

8. 向量的并矢，可以构成矩阵：

   ```python
   import numpy as np
   u = np.array([1, 2, 3])
   v = np.array([4, 5])
   np.outer(u, v)# 计算并矢，相当于u^T和v的矩阵乘法，结果为
   array([[ 4,  5],
          [ 8, 10],
          [12, 15]])
   ```

9. 用矢量拼接构成矩阵：

   ```python
   import numpy as np
   G_1 = np.array([1, 0, 0])
   G_2 = np.array([0, 1, 0])
   G_3 = np.array([1, 1, 1])
   G_xy = np.array([G_1,G_2,G_3])
   # 结果为
   array([[1, 0, 0],
          [0, 1, 0],
          [1, 1, 1]])
   #如果想当作列向量拼接，可以对上述结果转置.T即可。
   ```

10. 例子，计算度量张量在两个互相对偶的基底下的矩阵是互逆的：

   ```python
   import numpy as np
   G_1 = np.array([1, 0, 2]) #G_1,G_2,G_3为一个基底
   G_2 = np.array([0, 3, 0])
   G_3 = np.array([1, 1, 1])
   k = np.dot(np.cross(G_1, G_2), G_3)
   G1 = np.cross(G_2, G_3)/k #G1,G2,G3是和上面对偶的基底
   G2 = np.cross(G_3, G_1)/k
   G3 = np.cross(G_1, G_2)/k
   A = np.array([G_1, G_2, G_3])
   B = np.array([G1, G2, G3])
   G_xy = A.dot(A.T) #G_1,G_2,G_3构成的度量矩阵
   Gxy = B.dot(B.T)  #G1,G2,G3构成的度量矩阵
   G_xy.dot(Gxy)     #结果为单位矩阵
   ```

11. 统计运算，默认将多维数组看作一维的：

   ```python
   A.min()      #等价于np.min(A)
   A.max()      #等价于np.max(A)
   np.median(A) #中位数，比平均数更能体现平均水平，因为不容易被个别不合常理数影响。
   A.sum()      #所有元素求和
   A.prod()     #所有元素连乘
   np.percentile(A,q=50) #将所有元素从小到大排列，取分位值，50分位就是中位数。
   np.var(A)    #方差  =np.std(A)**2
   np.std(A)    #标准差
   #针对布尔数组的统计
   np.any(a == 3)  #只要有一个为True，就输出True
   np.all(a == 3)  #只有全部为True，才输出True
   np.count_nonzero(a1 == 3)  #计算a中=0的元素的个数，等价于np.sum(a1 == 3) 
   ```

11. 如果要沿行或列方向进行统计，那么要设置axis值。对min，max等操作也都可以设置axis值。

    ```python
    A = np.arange(9).reshape(3,-1) #结果为
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
    A.sum() #默认当作一维数组看，结果为36
    A.sum(axis=0) #把二维数组当做多个列向量拼接起来的，结果为array([ 9, 12, 15])
    A.sum(axis=1) #把二维数组当做多个行向量拼接起来的，结果为array([ 3, 12, 21])
    ```

12. arg索引运算，例如a.min()是获得数组a的最小值，而对应的索引运算a.argmin()是获得该最小值的索引位置。

    ```python
    A = np.arange(9).reshape(3,-1)
    a1.max() #结果为8
    a1.argmax() #结果为8。和max一样，它可以可以使用axis参数。
    a1.reshape(-1)[a1.argmax()] == a1.max() #结果恒为True
    ```

13. 排序：

    ```python
    A = np.arange(16)
    np.random.shuffle(A)   #就地乱序功能
    np.sort(A)   #返回一个新的排序后的ndarray对象，不改变A本身
    A.sort()     #就地排序
    np.argsort(A)  #返回的是索引，第一个14表示，排序后的第一个元素位于原序列的下标为14的地方
    Out[89]: 
    array([14,  4, 13,  8,  9, 12,  3,  6,  7, 15, 11, 10,  5,  0,  1,  2],
          dtype=int64)
    A[np.argsort(A)] == np.sort(A)     #将一个数组传递给数组的索引，得到的也是一个数组，相当于是每个都去索引，然后再拼接成一个数组。结果为全True的数组
    X = np.random.randint(0,10,size=(4,4)) #结果为
    array([[8, 9, 9, 5],
           [9, 6, 9, 3],
           [3, 4, 8, 2],
           [6, 8, 2, 3]])
    np.sort(X)   #对二维数组的操作，默认是按照行来进行的，axis=1，个行向量拼接而成的矩阵。#结果为
    array([[5, 8, 9, 9],
           [3, 6, 9, 9],
           [2, 3, 4, 8],
           [2, 3, 6, 8]])
    np.sort(X,axis=1) #结果为
    array([[5, 8, 9, 9],
           [3, 6, 9, 9],
           [2, 3, 4, 8],
           [2, 3, 6, 8]])
    np.sort(X,axis=0)#结果为
    array([[3, 4, 2, 2],
           [6, 6, 8, 3],
           [8, 8, 9, 3],
           [9, 9, 9, 5]])
    np.partition(A,2)    #把A的最小的3个数放到前3个顺序，不排序，其余的乱序。这种方法用在不需要排序的地方，会大大缩减时间。结果为
    array([ 0,  1,  2,  6, 14, 12,  7,  8,  3,  4, 11, 10,  5, 15, 13,  9])
    ```

14. 适用于浮点数组的近似比较：

    ```python
    numpy.isclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False) #逐个比较数组a和b中对应的元素。rtol为相对差异，以b的元素为基准，atol为绝对差异，都应是正值。如果待比较的数字本身很小，则atol可能不合适。
    #比较的公式为 abs(a - b) <= (atol + rtol * abs(b))。满足公式时，结果中对应的元素才为True。
    np.isclose([1e10,1e-7], [1.00001e10,1e-8]) #第一个元素，公式左侧为1e5，右侧为1.00001e5+1e-8，满足等式；第二个元素，公式左侧为9e-8，右侧为1e-8+1e-13，不满足等式。因此结果为array([ True, False])。
    numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False) #如果isclose比较的结果为全True，则allclose返回True，否则为False。
    ```

# pytorch

1. pytorch是从torch来的，torch最早是用lua写的。pytorch的tensor使用方法和numpy一样，但是二者底层不同，MXNET的API和numpy是一样的。

2. pytorch的默认数据类型是张量，它和numpy的ndarray可以自由转换。

   ```python
   A = X.numpy() # A的类型为numpy.ndarray
   B = torch.tensor(A) #B的类型为torch.Tensor
   
   #将大小为1的张量转化为python的标量
   a = torch.tensor([3.5])
   a.item() #结果为内置浮点数3.5
   float(a) #结果同上
   ```

3. 运行一些操作可能导致为新的结果分配新内存。

   ```python
   before = id(Y) 
   Y = Y + X
   id(Y) == before #可能不等
   #执行原地操作
   Z = torch.zeros_like(Y) #创建一个和Yshape相同的张量，数值都填充为0
   Z[:] = X + Y #这一步仅仅会更新Z中的值，而不会分配新的内存。
   #或者使用原地操作符
   X += Y #这个和X = X + Y不同
   ```

4. 一般使用pandas来读取存储在csv格式中的数据集。

   ```python
   pandas.read_csv(data_file) #即可获得一个二维的数组。
   ```

5. pandas中也包含一些数据预处理的函数，例如对于缺省值NaN的处理，可以将其替换为非NaN数据的平均值，如果是非数值数据，则可以使用独热编码，例如：有2个离散状态（Pave和NaN），则可以将它们表示为2个向量：(10)和(01）。

   ```python
   inputs.fillna(inputs.mean()) #每个数值列都用该列的平均值填充
   pd.get_dummies(inputs, dummy_na=True) #将NaN也作为一个离散状态，独立编码
   torch.tensor(inputs.values) #此时inputs的内容都是数值了，可以转化为张量了。
   ```

6. 深度学习一般使用32位浮点数，计算速度较快。

7. 张量创建

   ```python
   torch.tensor(3.0) #0阶，shape为torch.Size([])
   torch.tensor([3.0]) #1阶，shape为torch.Size([1])
   torch.tensor([3.0, 2.0]) #1阶，shape为torch.Size([2])
   a = torch.arange(12).reshape(3,4) #2阶，shape为torch.Size([3, 4])
   a.numel() #元素个数，不考虑shape，当作1维数组看。
   ```

8. 视图与克隆：

   ```python
   A = torch.tensor([3.0, 2.0])
   B = A #此处没有进行内存分配，而是创建了A的一个视图，二者共享数据，修改B的同时也会修改A
   C = A.clone() #显式声明要内存分配，此时不是视图
   ```

9. 两个矩阵按元素位置相乘，称为哈达玛积，使用$A\odot B$表示。在torch中使用$A*B$表示。

10. 默认情况下，调用求和函数会沿所有的轴降低张量的维度，使它变为一个标量。 我们还可以指定张量沿哪一个轴来通过求和降低维度，被指定的轴会在结果的shape中消失。

    ```python
    a = torch.arange(12).reshape(3,4) #shape为torch.Size([3, 4])
    a.sum() #结果为标量tensor(66)，类型为torch.Size([])
    a.sum(axis=0) #结果为tensor([12, 15, 18, 21])，shape为torch.Size([4])，被指定的第0轴没了
    a.sum(axis=1) #结果为tensor([ 6, 22, 38])，shape为torch.Size([3])
    #也可以同时按照多个轴求和，默认就是按照所有轴求和。
    a.sum(axis=[0,1]) #结果为tensor(66)，shape为torch.Size([])，
    #也可以令keepdims=True来保留被求和的轴，该轴的size则为1。keepdims默认为False
    a.sum(axis=1, keepdims=True) #结果为tensor([[6], [22], [38]])，shape为torch.Size([3, 1])。这样a.sum和a就是同维度的张量，可以应用广播机制来进一步处理。
    a/a.sum(axis=1) #会报错，因为[3]无法通过扩展和[3,4]匹配。
    a/a.sum(axis=0) #不会报错，因为[4]可以扩展为[1,4]，等价于a/a.sum(axis=0, keepdims=True)
    #可以做累加求和
    a.cumsum(axis=0) #每一列都是之前所有列的和。
    tensor([[ 0,  1,  2,  3],
            [ 4,  6,  8, 10],
            [12, 15, 18, 21]])
    ```

11. 矩阵和向量的乘法：

    ```python
    torch.mv(A, x) #其中A为[3,4]，x为[4]，则结果为[3]。mv表示matrix和vector的成绩
    torch.mm(A, B) #矩阵乘法
    ```

12. 范数，如果tensor的元素类型不是浮点数或复数时，求范数会报错：

    ```python
    a = torch.tensor([3.0,4.0])
    torch.norm(a) #向量的2范数，结果为tensor(5.)，
    torch.abs(a).sum() #向量的1范数，先对每个元素求绝对值，再求和。
    A = torch.arange(12.0).reshape(3,4) #浮点数元素
    torch.norm(A) #矩阵的F范数，结果为tensor(22.4944)
    ```

13. 标量对列向量求导会得到行向量，这个行向量应该当作矩阵来看待，$|x|^2$对$x$求导，结果为$2x^T$​。列向量对标量求导会得到列向量。这种被称为分子布局符号，也就是说分子是列向量时，结果还是列向量。

14. $<x,y>$对$y$的偏导数为$x^T$，本质是一个标量对列向量的导数，结果为一个行向量。

15. m维列向量y对n维列向量x求导结果为$m\times n$的矩阵，第$(i,j)$元素为$\frac{\partial y[i]}{\partial x[j]}$。可以先把分子展开，得到一个列向量，然后再把每一项展开，每一项都会变成一个行向量。

16. <img src="Python科学计算应用基础.assets/image-20240524213504231.png" alt="image-20240524213504231" style="zoom:67%;" />

17. $Ax$对$x$求偏导为$A$，$x^TA$对$x$求偏导为$A^T$，其中$A$不是$x$的函数。

18. $m\times n$阶矩阵A对$k\times l$阶矩阵求导，结果为4阶张量$m\times n\times l\times k$。第$(i,j,p,q)$元素为A的第$(i,j)$元素对B的第$(p,q)$元素的偏导。分母不变，分子逆序。

19. 向量求导的链式法则：![image-20240524221736716](Python科学计算应用基础.assets/image-20240524221736716.png)

# SciPy

1. SciPy的核心计算部分都是久经考验的Fortran数值计算库，例如线性代数（LAPACK），快速傅里叶变换（FFTPACK），常微分方程（ODEPACK），非线性方程组或最小值（MINPACK）。

2. 如果scipy使用了优化过的ATLAS LAPACK 和 BLAS库，可以获得很快的速度。

3. 由多个子模块组成，主要功能：聚类，常用常量和单位变换，优化和求根，插值，数值积分，线性代数，快速傅里叶变换，信号处理，N维图像处理，稀疏矩阵，特殊函数，统计分布。

4. scipy.constants模块包含了几乎所有的物理数学化学常数，例如：

   ```python
   import scipy #有量纲的值，其单位默认为国际单位
   scipy.constants.c #光速 299792458.0
   scipy.constants.h #普朗克常数 6.62607015e-34
   scipy.constants.pi #圆周率: 3.141592653589793
   #还包括国际单位的前缀，例如
   scipy.constants.mega #结果为10^6
   scipy.constants.nano #结果为10^{-9}
   #包括各种非国际单位到国际单位的换算关系，即1个该单位相当于多少国际单位
   scipy.constants.lb #结果为0.45359236999999997，表明，1 lb=0.45359236999999997 kg
   #涉及的领域包括：质量(kg)，时间(s)，长度(m)，角度(弧度)，压力(Pa)，面积(m^2)，体积(m^3)，速度(m/s)，温度(K)，能量(J)，功率(W)，力(N)，
   #温度比较特殊，因为它不是齐次线性的关系，因此提供了一个函数：
   scipy.constants.convert_temperature(val, old_scale, new_scale) #val为待转换的数值，old_scale和new_scale分别为表示旧和新的单位的字符串。常用的有：摄氏度:"C"，开尔文:"K"，华氏度:"F"，兰金温标:"R"
   scipy.constants.convert_temperature(0,"C","K") #0摄氏度 = 273.15 K
   ```

5. scipy.special模块的精度比Python自带的函数要高，当要对一些数值做更精确的计算时，应该用特殊函数库，例如：

   ```python
   import math
   math.log(1+1e-20)
   Out[16]: 0.0
   from scipy import special as sp
   sp.log1p(1e-20)   #log1p表示1 plus，实际是对1+1e-20求自然对数。这里用的是泰勒级数
   Out[18]: 1e-20
   
   sp.round(3.1)  #四舍五入，如果是.5则返回距离该数最近的偶数 np.round是同样的效果。
   Out[20]: 3.0
   sp.round(3.5)
   Out[21]: 4.0
   sp.round(4.5)
   Out[22]: 4.0
   int(3.1)	#取整函数，舍去小数部分。
   Out[23]: 3
   int(3.5)
   Out[24]: 3
   
   np.round(4.837,0)	#numpy还可以规定精确到的小数位数，special没有这个功能。
   Out[25]: 5.0
   np.round(4.837,1)
   Out[26]: 4.8
   np.round(4.837,2)
   Out[27]: 4.84
   ```

6. 排列组合：$A_5^3$，$C_5^3$。

   ```python
   sp.perm(5,3)     
   Out[28]: 60.0
   
   sp.comb(5,3)
   Out[29]: 10.0
   ```

7. 优化问题，基本套路都是这样的：①通过分析问题，确定问题的损失函数或者效用函数②通过最优化损失函数或者效用函数，获得机器学习的模型。几乎所有的参数学习算法都是这样的套路。常用的最优化算法有两类：传统的，例如梯度下降，牛顿等；启发式的，例如粒子群，遗传，退火等算法。

   1. 最小二乘拟合（leastsq），步骤如下：

      1. 需要先定义一个残差函数，leastsq会调用这个函数，将初始参数[1,0]传给p
      2. 根据p，计算所有(x,y)对的差值（一维数据），然后对这个一维数据求平方和，记作该初始值p对应的损失函数loss function。
      3. 然后变换初始值p，搜寻（损失函数是k，b的函数）使得损失函数取最小值的对应的p，即可获得k，b。

      ```python
      import numpy as np
      from scipy.optimize import leastsq
      import matplotlib.pyplot as plt
      x = np.linspace(-1,1,10)
      y = x*3+np.random.random(10)+5
      def residuals(p):
          k,b = p
          return y-(k*x+b)
      r = leastsq(residuals,[1,0])
      print(r)
      y1 = r[0][0]*x+r[0][1]
      plt.scatter(x, y)
      plt.plot(x, y1)
      plt.grid()
      plt.show()
      ```

      $$
      a=\frac{\sum\limits_{i=1}^m(x^{(i)}-\bar{x})(y^{(i)}-\bar{y})}{\sum\limits_{i=1}^m(x^{(i)}-\bar{x})^2}\quad\quad\phi=\bar{y}-a\bar{x}
      $$

   2. 函数最小值（fmin），Rosenbrock函数是一个常用来测试最优化算法性能的非凸函数，$f(x,y)=(1-x)^2+100(y-x^2)^2$。其全域最小值位于抛物线型的山谷中，但是在山谷中值的变化不大，要找到全域的最小值相当困难。

   3. ![image-20201007103553654](Python科学计算应用基础.assets/image-20201007103553654.png)

   4. ```python
      import numpy as np
      from scipy import optimize as opt
      def Rosenbrock(p):
          x,y = p
          z = (1-x)**2+100*(y-x**2)**2
          return z
      result = opt.fmin(Rosenbrock,[2,2])   #默认使用梯度下降算法
      print(result)
      Optimization terminated successfully.
               Current function value: 0.000000
               Iterations: 62
               Function evaluations: 119
      [0.99998292 0.99996512]
      ```

   5. 非线性方程组求解（fsolve）

      ```python
      import numpy as np
      from scipy import optimize as opt
      from math import sin
      def f(x):
          x0,x1,x2 = x   #三个未知数
          return [5*x1+3,4*x0**2-2*sin(x1*x2),x1*x2-1.5]   #三个方程等号右端默认为0。实际上就是求那种x的组合，使得这3个数最接近0。
      result = opt.fsolve(f,[1,1,1])    #需要提供一个初始值
      print(result,f(result))
      [-0.70622057 -0.6        -2.5       ]
      [0.0, -9.126033262418787e-14, 5.329070518200751e-15] 带入检验是否满足方程组。
      ```

   6. 插值和拟合不同，拟合适用于数据量比较大的情况，不要求拟合曲线通过所有的数据点，如果此时还要求通过所有的数据点，则会受误差影响较大；而插值要求必须经过所有的点，适合于数据量较少的情况，例如测量困难的情况。：

      ```python
      import numpy as np
      from scipy import optimize as opt
      from scipy import interpolate as ip
      import matplotlib.pyplot as plt
      x = np.linspace(0,10,11)
      y = np.sin(x)
      plt.scatter(x,y)
      for kind in ["slinear","zero","nearest","quadratic","cubic"]:   #分段线性，左连续，中间跳跃，二次样条，三次样条。
          xnew = np.linspace(0,10,100)
          f = ip.interp1d(x,y,kind=kind)    #返回的是一个函数，只能进行内插，即函数的定义域在插值范围内。
          ynew = f(xnew)
          plt.plot(xnew,ynew)
      plt.show()
      
      #小范围外推
      import numpy as np
      from scipy import optimize as opt
      from scipy import interpolate as ip
      import matplotlib.pyplot as plt
      x = np.linspace(0,10,11)
      y = np.sin(x)
      plt.scatter(x,y)
      
      xnew = np.linspace(0,12,100)     #范围12时，如左下图，范围15时，如右下图。
      f = ip.UnivariateSpline(x,y,s=0) #设置S可以降低噪声的影响。
      ynew = f(xnew)
      plt.plot(xnew,ynew)
      plt.show()
      ```

   7. mgrid

      ```python
      x,y = np.mgrid[-1:1:5j,-1:1:5j]  #这一步是在x,y平面划分了一个网格，x∈[-1，1]，y∈[-1，1]，每个方向5个点。一共有25个点。依次给点编上一个坐标号(编号的位置要和定义mgrid的顺序相同，此处都是先x后y)，从左下角开始是(0,0)，右下角为(4,0)，左上角为(0,4)，右上角为(4,4)，中心点为(2,2)。这些点对应的具体坐标通过查询x,y数组获得。右下角得坐标为(x[4,0],y[4,0])=(1,-1)
      x
      Out[22]: 
      array([[-1. , -1. , -1. , -1. , -1. ],
             [-0.5, -0.5, -0.5, -0.5, -0.5],
             [ 0. ,  0. ,  0. ,  0. ,  0. ],
             [ 0.5,  0.5,  0.5,  0.5,  0.5],
             [ 1. ,  1. ,  1. ,  1. ,  1. ]])
      y
      Out[23]: 
      array([[-1. , -0.5,  0. ,  0.5,  1. ],
             [-1. , -0.5,  0. ,  0.5,  1. ],
             [-1. , -0.5,  0. ,  0.5,  1. ],
             [-1. , -0.5,  0. ,  0.5,  1. ],
             [-1. , -0.5,  0. ,  0.5,  1. ]])
      (x[0,0],y[0,0])     #左下角点的坐标
      Out[24]: (-1.0, -1.0)
      (x[4,0],y[4,0])     #右下角的坐标
      Out[25]: (1.0, -1.0)
      x[2,1],y[2,1]	    #中心点下方的那个点
      Out[21]: (0.0, -0.5)
      ```

   8. 二维插值：

      ```python
      import numpy as np
      from scipy import interpolate as ip
      import matplotlib.pyplot as plt
      from mpl_toolkits.mplot3d import Axes3D
      from matplotlib import cm #颜色模式
      def func(x,y):
          return (x+y)*np.exp(-5.0*(x**2+y**2))
      x,y = np.mgrid[-1:1:15j,-1:1:15j]
      z = func(x,y)   #z也是网格化的数据，和x,y维度相同。
      fig = plt.figure()
      ax = Axes3D(fig)
      ax.plot_surface(x,y,z,cmap=cm.coolwarm)   #该函数接受网格化的参数。cmap是颜色模式。
      plt.show()
      fig1 = plt.figure()
      ax = Axes3D(fig1)
      newFunc = ip.interp2d(x,y,z,kind="cubic")
      xnew,ynew = np.mgrid[-1:1:100j,-1:1:100j]
      znew = newFunc(np.linspace(-1,1,100),np.linspace(-1,1,100))  #这里不接受网格化的数据，而是接受1维的数组，不能用znew = newFunc(xnew,ynew)来求znew。不过得出的znew还是网格化的数据。这个函数是当做普通数学函数来使用的，例如可以求 newFunc(1,0.3)得出array([0.00558487])
      ax.plot_surface(xnew,ynew,znew,cmap=cm.coolwarm)
      plt.show()
      ```

## linalg

1. 线性代数scipy.linalg，包含了numpy.linalg的所有功能。scipy.linalg总是和配有高效的BLAS库，而numpy.linalg则不一定，因此推荐使用scipy.linalg。

2. 虽然numpy.matrix比numpy.ndarray支持更方便的矩阵操作，但是不推荐使用它，因为后者更通用。

3. 接受的对象应为二维数组，结果也是二维数组。

4. 矩阵的逆：

   ```python
   A = np.array([[1, 3, 5],
                 [2, 5, 1],
                 [2, 3, 8]])
   InverseA = scipy.linalg.inv(A) #结果为
   array([[-1.48,  0.36,  0.88],
          [ 0.56,  0.08, -0.36],
          [ 0.16, -0.12,  0.04]])
   A.dot(InverseA) #结果如下，可以认为是单位矩阵
   array([[ 1.00000000e+00, -1.11022302e-16,  4.85722573e-17],
          [ 3.05311332e-16,  1.00000000e+00,  7.63278329e-17],
          [ 2.22044605e-16, -1.11022302e-16,  1.00000000e+00]])
   ```

5. 求解线性方程组：

   ```python
   #也可以先对系数矩阵求逆，然后再进行乘法。不过linalg.solve速度更快，数值稳定性更好。
   A = np.array([[1,3,5],[2,5,1],[2,3,8]])
   b = np.array([10,8,3])
   x = scipy.linalg.solve(A,b)  #求解线性方程组，结果为，array([-9.28,  5.16,  0.76])
   A.dot(x)-b #检验，结果为array([ 0.00000000e+00, -1.77635684e-15, -1.77635684e-15])
   ```

6. 求方阵的行列式：

   ```python
   A = np.array([[1,3,5],[2,5,1],[2,3,8]])
   scipy.linalg.det(A) #结果为 -25.000000000000004
   ```

7. 向量范数：$\begin{split}\left\Vert \mathbf{x}\right\Vert =\left\{ \begin{array}{cc} \max\left|x_{i}\right| & \textrm{ord}=\textrm{inf}\\ \min\left|x_{i}\right| & \textrm{ord}=-\textrm{inf}\\ \left(\sum_{i}\left|x_{i}\right|^{\textrm{ord}}\right)^{1/\textrm{ord}} & \left|\textrm{ord}\right|<\infty.\end{array}\right.\end{split}$

8. 矩阵范数：$\begin{split}\left\Vert \mathbf{A}\right\Vert =\left\{ \begin{array}{cc} \max_{i}\sum_{j}\left|a_{ij}\right| & \textrm{ord}=\textrm{inf}\\ \min_{i}\sum_{j}\left|a_{ij}\right| & \textrm{ord}=-\textrm{inf}\\ \max_{j}\sum_{i}\left|a_{ij}\right| & \textrm{ord}=1\\ \min_{j}\sum_{i}\left|a_{ij}\right| & \textrm{ord}=-1\\ \max\sigma_{i} & \textrm{ord}=2\\ \min\sigma_{i} & \textrm{ord}=-2\\ \sqrt{\textrm{trace}\left(\mathbf{A}^{H}\mathbf{A}\right)} & \textrm{ord}=\textrm{'fro'}\end{array}\right.\end{split}$

9. ```python
   #对向量来说，默认为2范数，
   b = np.array([1,2,3])
   scipy.linalg.norm(b) #等于sqrt(1+4+9) = sqrt(14) = 3.7416573867739413
   #对矩阵来说默认为Frobenius范数，可以使用上面的公式计算，等价于所有元素的模的平方和，再开平方。
   A=np.array([[1,2],[3,4]])
   scipy.linalg.norm(A) #等于sqrt(1+4+9+16) = sqrt(30) = 5.477225575051661
   #无穷范数的ord应使用numpy.inf或-numpy.inf
   ```

10. 线性最小二乘：寻找预测模型中的线性参数，使得观测值和预测值之间的差的平方和取最小值，该平方和关于参数的梯度向量为0，是取最值的必要条件，对该等式进行变换就可以得到矩阵A伪逆的定义$\mathbf{A}^{\dagger}=\left(\mathbf{A}^{H}\mathbf{A}\right)^{-1}\mathbf{A}^{H}$。通过伪逆来求最小二乘解：$c=\mathbf{A}^{\dagger}y$，不过这个方法是比较繁琐低效的。

11. 线性最小二乘法等价于求一个线性方程组的最小二乘解问题，$Ac=y$。linalg.lstsq函数要求提供A和y，求解c。

    ```python
    x = np.array([1, 2.5, 3.5, 4, 5, 7, 8.5]) #采样点
    y = np.array([0.3, 1.1, 1.5, 2.0, 3.2, 6.6, 8.6]) #观测值
    #计划采用的模型为： y = a + b*x**2，2个参数分别为(a,b)，对应的函数为(1, x**2)。根据函数向量来计算矩阵A
    A = x.reshape(-1,1)**[0, 2]
    #或者使用
    A = np.column_stack(([1]*len(x),x**2)) #将多个向量按列堆叠。
    c, res, rank, s = scipy.linalg.lstsq(A, y) #底层使用LAPACK的gelsd算法，会先进行矩阵的A奇异值分解，也可以用lapack_driver参数指定其他方法。
    #c为 array([0.20925829, 0.12013861])，分别为参数a和b。
    #res为  0.4082665237440342。为残差向量Ac-y的2范数的平方，即scipy.linalg.norm(A.dot(c)-y)**2
    #rank为 2。A的有效秩
    #s为 array([93.25228799,  1.7883749 ])。A的奇异值
    #当求解不收敛时会报错LinAlgError。
    ```

12. 广义逆也就是伪逆，都是指最常用的Moore–Penrose逆：

    ```python
    A = np.array([[ 1.  ,  1.  ],
                  [ 1.  ,  6.25],
                  [ 1.  , 12.25],
                  [ 1.  , 16.  ],
                  [ 1.  , 25.  ],
                  [ 1.  , 49.  ],
                  [ 1.  , 72.25]]) #7*2，广义逆为2*7。
    #也可以利用广义逆来求最小二乘解：
    scipy.linalg.pinv(A).dot(y) #结果为array([0.20925829, 0.12013861])，和上面的c一样。
    ```

13. 只有可被相似对角化的方阵才可以进行特征值分解：$\mathbf{A}=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}$。$\mathbf{V}$是特征向量构成的矩阵，$\Lambda$为特征值构成的对角矩阵。

14. 方阵的特征值和特征向量：

    ```python
    l,v = scipy.linalg.eig(A)
    # 特征值l构成的向量为 array([10.5540456 +0.j, -0.5873064 +0.j,  4.03326081+0.j])
    # 特征向量v构成的列向量矩阵如下，每个特征向量长度都被归一化了。
    array([[-0.51686204, -0.94195144,  0.11527992],
           [-0.32845853,  0.31778071, -0.81936883],
           [-0.79054957,  0.10836468,  0.56155611]])
    #l[0]特征值对应的特征向量为v的第0列，v[:,0]
    A.dot(v[:,0])-l[0]*v[:,0] #检验一下，结果为 array([-1.77635684e-15+0.j, -1.77635684e-15+0.j,  0.00000000e+00+0.j])
    v.dot(np.diag(l)).dot(scipy.linalg.inv(v)) #特征值分解的检验结果和A相等。
    #标准特征值问题是广义特征值问题的一个特例，即B为单位矩阵。
    Av = λBv
    ```

15. SVD（奇异值）分解：

    ```python
    A = np.array([[1,3,5],[2,5,1],[2,3,8]])
    b = np.array([10,8,3])
    x = linalg.solve(A,b)
    X = np.array(     #7x5的矩阵
    [[0,0,0,2,2],
     [0,0,0,3,3],
     [0,0,0,1,1],
     [1,1,1,0,0],
     [2,2,2,0,0],
     [5,5,5,0,0],
     [1,1,1,0,0]
     ])
    U,s,Vh = linalg.svd(X)
    np.round(U,3)    #7x7的正交矩阵，U.dot(U.T)为单位矩阵。
    Out[5]: 
    array([[ 0.   , -0.535, -0.82 , -0.014,  0.118, -0.168,  0.007],
           [-0.   , -0.802,  0.481, -0.004, -0.351, -0.043,  0.002],
           [ 0.   , -0.267,  0.195,  0.04 ,  0.819,  0.467, -0.018],
           [-0.18 ,  0.   ,  0.089,  0.883,  0.161, -0.393,  0.016],
           [-0.359,  0.   ,  0.177, -0.417,  0.322, -0.619, -0.423],
           [-0.898,  0.   , -0.106,  0.032, -0.193,  0.379, -0.015],
           [-0.18 ,  0.   ,  0.089, -0.209,  0.161, -0.265,  0.906]])
    np.round(s,3)    #5    奇异特征值，构成一个对角矩阵。
    Out[6]: array([9.644, 5.292, 0.   , 0.   , 0.   ])
    np.round(Vh,3)      #5x5的正交矩阵，Vh.dot(Vh.T)为单位矩阵。
    Out[7]: 
    array([[-0.577, -0.577, -0.577,  0.   ,  0.   ],
           [-0.   ,  0.   ,  0.   , -0.707, -0.707],
           [-0.62 , -0.151,  0.77 ,  0.   ,  0.   ],
           [-0.   ,  0.   , -0.   ,  0.707, -0.707],
           [ 0.532, -0.802,  0.271,  0.   , -0.   ]])
    #SVD算法本身不会对数据进行压缩，而是找出那些非主要成分可以去除，使得矩阵中更多的数变得相同，然后后续由其他压缩算法来进行压缩。
    ```

16. 数值积分：

    ```python
    import numpy as np
    import scipy.linalg as linalg
    from scipy import integrate
    def f(x):
        return x**2
    integrate.quad(f,0,1)     #数值积分范围为[0,1]
    Out[13]: (0.33333333333333337, 3.700743415417189e-15)
    #二重积分
    import numpy as np
    import scipy.linalg as linalg
    from scipy import integrate
    def fc(x):
        return (1-x**2)**0.5
    def fs(x,y):
        return (1-x**2-y**2)**0.5
    integrate.dblquad(fs,-1,1,lambda x:-fc(x),lambda x:fc(x))
    Out[15]: (2.094395102393199, 1.0002356720661965e-09)
    ```

17. 信号处理，设计滤波器，过滤噪声：

    ```python
    import numpy as np
    import scipy.linalg as linalg
    from scipy import integrate
    import scipy.signal as signal
    import matplotlib.pyplot as plt
    t = np.arange(0,20,0.1)
    noise = np.random.normal(size = t.shape)
    x = np.sin(t)+noise*0.1
    
    x2 = signal.medfilt(x,7)  #中值滤波器，第二个参数表示取前3个，加后3个，加当前点的平均值作为当前点的滤波后的值，所以第二个参数必须为奇数，一般为5，7不宜太大。这个属于低通滤波器，过滤高频的干扰。
    #medfile2d 可以对2维数组做平均，噪点多的图像可以通过中值滤波来变清晰。对清晰地图像进行中值滤波后会变模糊。
    plt.plot(t,x)
    plt.plot(t,x2)
    plt.show()
    
    ```

    ![image-20201007194028190](Python科学计算应用基础.assets/image-20201007194028190.png)

18. 傅里叶变换，将一个复杂的周期信号分解为多个正弦信号：

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import fftpack
    
    def signal_sample(t):
        return np.sin(np.pi*t)+np.sin(4*np.pi*t+0.5)  #最高频率为2Hz.
    
    N=1000
    f_s=10
    t = np.linspace(0,N/f_s,N)
    f_t = signal_sample(t)    #模拟采样的过程，1秒采样10次，一共100秒，一共1000个点。
    
    F = fftpack.fft(f_t)   #复数数组，每一个复数表示一个三角函数，幅值和初相位由复数的幅值和幅角得出，频率是顺次变化的
    f = fftpack.fftfreq(N, 1/f_s)   #频率域的自变量，从-5到+5。采样率被一分为2。
    plt.plot(f,np.abs(F)/N)
    plt.xlim(0,3)       #只看正半轴的情况
    plt.show()
    F_filter =  F*(abs(f)<1.5)
    f_filter = fftpack.ifft(F_filter)     #逆变换，还原到时域。
    plt.plot(t,f_t)
    plt.plot(t,f_filter.real)
    plt.xlim(0,5)    #只显示前5秒的信号。
    plt.show()
    ```

# 稀疏矩阵

1. 工程计算中经常用到稀疏矩阵（大多数元素是0的矩阵）。稀疏因子：非零元素数/总元素的个数 当稀疏因子＜0.05时，就认为是稀疏矩阵。

2. 以常规的二维数组来表示稀疏矩阵有以下问题：
   1. 零值元素占用了大量的空间。
   2. 计算中要进行很多和0相关的无意义运算。

3. 尽可能少存或不存零值元素；尽可能减少和0相关的运算。

4. 同时还要运算方便，能够尽快根据下标找到对应的元素。能尽快地找到同一行/列的非零元素。

5. 稀疏矩阵中存在一类特殊的，例如三角矩阵和对角矩阵，非零元素的分布都比较规律。线性化存储较为容易。

6. 稀疏矩阵的代价是：访问单个成员变得更加复杂，需要额外的结构才能明确地恢复原始矩阵。

7. 根据非零元的数量和分布，可以使用不同的数据结构，大致分为如下两类：
   1. 支持高效修改的，可以很方便地对往原始矩阵中假如新的元素, 或者从原始矩阵中删去元素 (增加元素指的是将原来为0的元素变为非0, 同样删除同理)。如DOK（Dictionary of keys，密钥字典）、LIL（List of lists，列表的列表）或COO（Coordinate list，坐标列表）。这些格式通常用于构建矩阵。
   2. 支持快速访问到特定位置的元素的数据结构以及支持基于矩阵形式的操作, 即两个稀疏矩阵相加或者相减等，如CSR（Compressed Sparse Row，压缩稀疏行）或CSC（Compressed Sparse Column，压缩稀疏列）。

8. 上面的第一种格式如果要进行矩阵乘法或求逆，应该先转化成第二种中的一种格式，lil格式内部的数据是按行存储的，因此转化为CSR更快。

9. CSR，CSC，COO格式之间的互转都是快速的，线性时间复杂度。

10. CSR格式尤其适合进行矩阵和向量的乘积，使用`A.dot(v)`进行。

11. CSR和CSC格式，在内部存储时，不一定按照行或列进行排序，如果需要内部是有序时，可以使用`.sort_indices()`函数。

12. Python的scipy.sparse模块提供了对稀疏矩阵的支持。

13. 对于一个`sparse.spmatrix`（抽象基类），可以用`.tocoo, tocsr`等方法来进行存储方式的转换。

14. `sparse.save_npz`函数将稀疏矩阵序列化，`sparse.load_npz`反序列化。

15. `sparse.hstack`和`sparse.vstack`函数用于稀疏矩阵的拼接。

16. 稀疏矩阵与向量相乘用`.dot`方法。

17. `scipy.sparse.linalg`包有稀疏矩阵的一些线性代数方法。

18. 稀疏矩阵可以存储显式的零：

    ```python
    row = [0,0,1,1,2,2]
    col = [0,3,1,2,2,3]
    data = [1,2,4,1,5,0]
    csr = sp.sparse.csr_array((data, (row, col)))
    csr
    <Compressed Sparse Row sparse array of dtype 'int64'
         with 6 stored elements and shape (3, 4)>
    csr.eliminate_zeros() #移除显式的零，就地操作。
    csr
    <Compressed Sparse Row sparse array of dtype 'int64'
         with 5 stored elements and shape (3, 4)>
    ```

19. COO格式中可以包含重复的键值对，在转化为CSR或CSC格式时，位置重合的键值对的值会自动求和，这对于构建有限元的刚度和质量矩阵很有帮助。

    ```python
    row = [0,0,1,1,1,2]
    col = [0,3,1,1,2,2]
    data = [1,2,1,3,1,5]
    dupes = sp.sparse.coo_array((data, (row, col))) #可以看到，在(1,1)的位置上有2个元素，取值为1和3。
    dupes
    <COOrdinate sparse array of dtype 'int64'
         with 6 stored elements and shape (3, 4)> #认为有6个元素，虽然只有5个位置
    dupes.todense()
    array([[1, 0, 0, 2],
          [0, 4, 1, 0],
          [0, 0, 5, 0]])
    dupes.sum_duplicates() #对重复下标的元素求和，就地进行。
    ```

20. 一些稀疏矩阵格式在标准形式下会有较高的效率，例如没有重复的下标项，下标按顺序排列。coo_array，csr_array，csc_array格式的矩阵都是标准形式，也可以使用`.has_canonical_format`函数来检查矩阵是否是标准形式。

21. 大部分对于稠密矩阵来说可用的算法，对于稀疏矩阵来说也是可用的。

22. 稀疏矩阵的`.nnz`属性，可以返回其中非零元素的数量。

23. 对稀疏矩阵应用归约函数时，例如mean，sum，max等，结果以非稀疏矩阵形式返回。

24. 有时稀疏矩阵之间的操作的结果的格式不一定和原来一样，这是因为SCIPY会选择计算效率最高的格式。例如2个COO格式的矩阵的乘法，结果为CSR格式。

25. 给定非零元素的下标及其值来构建矩阵：

    ```python
    row = np.array([0, 0, 1, 2, 2, 2]) #row和col数组不要求有序
    col = np.array([0, 2, 1, 0, 1, 2])
    data = np.array([1, 2, 3, 4, 5, 6])
    mtx = sparse.coo_matrix((data, (row, col)), shape=(3, 3)) #将行和列的列表以元组形式包装, 然后再将该元组与data组成一个新的元祖作为第一个参数传入。
    print(mtx) #输出所有的非零元及其下标
      (0, 0)        1
      (0, 2)        2
      (1, 1)        3
      (2, 0)        4
      (2, 1)        5
      (2, 2)        6
    mtx.toarray() #输出成二维数组，numpy.ndarray类型
    array([[1, 0, 2],
           [0, 3, 0],
           [4, 5, 6]])
    mtx.todense() #输出成矩阵，numpy.matrix类型。将稀疏矩阵变成稠密矩阵，注意转换后的内存消耗。
    matrix([[1, 0, 2],
            [0, 3, 0],
            [4, 5, 6]])
    ```

26. 所有的稀疏矩阵格式支持使用`numpy.ndarray`二维数组来构建：

    ```python
    mtx = sparse.lil_matrix([[0, 1, 2, 0], [3, 0, 1, 0], [1, 0, 0, 1]])
    print(mtx.todense())
    [[0 1 2 0]
     [3 0 1 0]
     [1 0 0 1]]
    ```

27. 所有的矩阵都可以使用如下方式来构建一个所有的元素都为0的矩阵

    ```python
    mtx = sparse.coo_matrix((3, 4), dtype=np.int8)
    print(mtx) #注意这里输出的是空值, 因为只构造了一个(5,5)的零矩阵, 其中没有非0元素自然没有非零元素键值对。
    ```

## COO

1. COO的思想是按照（行，列，值）的方式存储每一个非0元素，所以存储的数据结构就应该是一个以三元组为元素的列表`List[Tuple[int, int, int]]`。为了方便检索矩阵某个位置的元素，这些三元组最好应该按顺序（比如先行后列）排列，这样在访问时可以使用二分查找加速。

2. 优点： 转化快速，还能转化成CSR/CSC格式的稀疏矩阵。

3. 缺点： 不支持切片和下标索引，矩阵计算。

4. 例子：

   ```python
   from scipy import sparse
   import numpy as np
   row = np.array([0, 3, 1, 0])
   col = np.array([0, 3, 1, 2])
   data = np.array([4, 5, 7, 9])
   mtx = sparse.coo_matrix((data, (row, col)), shape=(4, 4))
   print(mtx)
   (0, 0)    4
   (3, 3)    5
   (1, 1)    7
   (0, 2)    9
   
   print(mtx.todense())
   [[4 0 9 0]
    [0 7 0 0]
    [0 0 0 0]
    [0 0 0 5]]
   
   row = np.array([0, 0, 1, 3, 1, 0, 0])
   col = np.array([0, 2, 1, 3, 1, 0, 0])
   data = np.array([1, 1, 1, 1, 1, 1, 1])
   mtx = sparse.coo_matrix((data, (row, col)), shape=(4, 4))
   print(mtx.todense())
   [[3 0 1 0]
    [0 2 0 0]
    [0 0 0 0]
    [0 0 0 1]]
   
   mtx[2, 3] #不支持索引，会报错。
   ```

## DOK

1. DOK的内部是一个哈希表`unordered_set<pair<int, int>>`，以`(row_index, column_index)`为key。访问某个位置只需要 O(1) 的时间。所以这种存储方式能比较好的支持矩阵的索引。这种格式支持矩阵运算。是一种高效的增量构建稀疏矩阵的方式。

2. 这种格式的储存方式非常适合增删改查，只需要直接向字典中加入或删除一个键值对就行，但如果要查某一个位置的元素是否是非0元素，也不用遍历整个字典的keys，因为内部是哈希表。

3. 例子：

   ```python
   from scipy import sparse
   import numpy as np
   mtx = sparse.dok_matrix((5, 5), dtype=np.float64) #创建一个全为0.0的矩阵
   for ir in range(5):
       for ic in range(5):
           mtx[ir, ic] = 1.0 * (ir != ic) #除了对角线外，所有单元都赋值为1.0
   
   print(mtx.todense())
   [[0. 1. 1. 1. 1.]
    [1. 0. 1. 1. 1.]
    [1. 1. 0. 1. 1.]
    [1. 1. 1. 0. 1.]
    [1. 1. 1. 1. 0.]]
   ```

## LIL

1. LIL：对于矩阵的每一行，都用一个列表来记录下非0的位置和值。这种格式支持切片和索引。

2. LIL的数据结构是列表, 每一行对应着的矩阵中该行, 而LIL中每一行都是一个列表, 包含在该行出现非0元素的列位置以及非0元素的值, 可能的实现方式是每一行都包含一个列表, 该列表是个升序排序后的列表，每个元素代表在原矩阵中在该行非0元素出现的列位置。

3. 例子：

   ```python
   from scipy import sparse
   from numpy.random import rand
   import numpy as np
   mtx = sparse.lil_matrix((4, 5)) #全为0的稀疏矩阵
   data = np.round(rand(2, 3)) #二维数组
   
   print(data)
   [[0. 1. 0.]
    [1. 1. 1.]]
   
   mtx[:2, [1, 2, 3]] = data #对第0，1行，第1，2，3列的交叉项构成的子矩阵赋值
   
   print(mtx)
   (0, 2)        1.0
   (1, 1)        1.0
   (1, 2)        1.0
   (1, 3)        1.0
   
   print(mtx.todense())
   [[0. 0. 1. 0. 0.]
    [0. 1. 1. 1. 0.]
    [0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0.]]
   
   print(mtx[:2, :]) #取第0和1行的子矩阵
   (0, 2)        1.0
   (1, 1)        1.0
   (1, 2)        1.0
   (1, 3)        1.0
   
   print(mtx[:2, :].todense())
   [[0. 0. 1. 0. 0.]
        [0. 1. 1. 1. 0.]]
   
   print(mtx[1:2, [0,2]].todense())
   [[0. 1.]]
   ```

## CSR

1. CSR用三个列表来表达稀疏矩阵，和COO较为相似，但比COO更进一步的是其还将每一行的空间压缩了，这种类型的数据结构支持快速row access和矩阵的相加，同理CSC支持快速column access和矩阵的相加。

2. 优点：高效的矩阵加法和乘法操作；高效的行切片；快速的矩阵和向量乘法。

3. 缺点：较慢的列切片，稀疏结构的更改代价高昂。

4. 例子：

   ```python
   import numpy as np
   from scipy import sparse
   indptr = np.array([0, 2, 3, 6]) #除了最后一个元素意外，以第i个元素的值作为下标，在indices数组中作用，结果就是第i行的非零元素的列号。最后一个元素代表整个矩阵中所有非0元素的数量。例如，用indptr的值当作下标，来对数组indices进行切片，[[0,2],[1],[0,1,2]]，这就表明第0行的第0和2列有非零元素，第1行的第1列有非零元素，第2行的第0,1,2列有非零元素。
   indices = np.array([0, 2, 1, 0, 1, 2]) #代表每一行的非0元素的位置
   data = np.array([1, 2, 3, 4, 5, 6])
   mtx = sparse.csr_matrix((data, indices, indptr), shape=(3, 3)) #和mtx1完全相同
   print(mtx) #可以根据下面的键值对来分别还原上述三个数组数组，首先需要将所有非零元素先按照行排序，然后按照列排序：
   # 将所有的列按照顺序输出即可得到indices数组，也就是[0,2,1,0,1,2]。
   # 将行号变化的编号输出得到[0,2,3]，然后追加上非零元素的总数，得到[0,2,3,6]。
   # 将所有键值对的值按顺序输出即可得到data数组，也就是[1,2,3,4,5,6]。
     (0, 0)        1
     (0, 2)        2
     (1, 1)        3
     (2, 0)        4
     (2, 1)        5
     (2, 2)        6
   mtx.toarray()
   array([[1, 0, 2],
          [0, 3, 0],
          [4, 5, 6]])
   ```

## CSC

1. CSC和CSR的构造方式几乎一样，只不过之前是一行一行开始扫描indptr和indices的，现在变为一列一列了。

2. 优点：高效的矩阵加法和乘法操作；高效的列切片；快速的矩阵和向量乘法。

3. 缺点：较慢的行切片，稀疏结构的更改代价高昂。

4. 例子：

   ```python
   import numpy as np
   from scipy import sparse
   
   indptr = np.array([0, 2, 3, 6])
   indices = np.array([0, 2, 2, 0, 1, 2])
   data = np.array([1, 2, 3, 4, 5, 6])
   mtx = sparse.csc_matrix((data, indices, indptr), shape=(3, 3))
   print(mtx) #可以看到以csc格式存储的数组，默认是按列存储的，一列存储完再存储下一列。
   (0, 0)        1
   (2, 0)        2
   (2, 1)        3
   (0, 2)        4
   (1, 2)        5
   (2, 2)        6
   mtx.toarray()
   array([[1, 0, 4],
          [0, 0, 5],
          [2, 3, 6]])
   ```


# 稀疏矩阵特征值问题

1. SCIPY支持使用ARPACK库来求解稀疏矩阵的特征值。两个接口，`scipy.sparse.linalg.eigs`用来求解非对称的实/复矩阵的特征值/特征向量。`scipy.sparse.linalg.eigsh`用来求解实对称/复共轭对称矩阵的特征值/特征向量。
2. ARPACK可以求解标准$Ax=\lambda x$或广义特征值问题$Ax=\lambda Mx$：
3. ARPACK的强大在于，它可以只计算一部分的特征值/特征向量对，这通过which参数来确定：
   1. `which = 'LM'`：
   2. `which = 'SM'`：
   3. `which = 'LR'`：
   4. `which = 'SR'`：
   5. `which = 'LI'`：
   6. `which = 'SI'`：
   7. `which = 'LA'`：
   8. `which = 'SA'`：
   9. `which = 'BE'`：
4. ARPACK通常更擅长寻找极值特征值，例如最大幅值的特征值。因此如果`which="SM"`，可能会导致求解缓慢或结果异常。推荐使用移位逆（Shift-invert）模式。

# SymPy

1. SymPy是一套符号运算的扩展库，完全采用python编写。

2. SymPy依赖于mpmath。符号计算可以利用符号进行表达式推导。符号计算又称为计算代数系统 computer algebra system  CAS。Sympy可以简化表达式，求导，积分，求极限，解方程，处理矩阵等。可以将结果输出成图片或Latex结果。

   ```python
   import math
   math.sqrt(8)   #结果为 2.8284271247461903 是近似值
   
   import sympy
   sympy.sqrt(3)  #结果为 sqrt(3)。会保留精确值。
   sympy.sqrt(8)  #结果为 2*sqrt(2)。会化简
   ```
   
3. 所有的符号变量都要用symbols定义。

   ```python
   from sympy import symbols
   x, y = symbols('x y')  #可以同时定义多个符号变量，符号变量可以有多个字符。符号的内容可以是python不允许的变量，例如: s1 = symbols("1s")
   expr = x + 2*y   #并不会计算表达式的值，而是保留符号
   expr - x   #输出2*y，x和-x会消掉。
   x*expr     #输出x*(x + 2*y)。而不是展开多项式。
   ```
   
4. 符号计算的结果可以设置不同的输出形式，展开或者因式分解形式。

   ```python
   from sympy import expand, factor
   x, y = symbols('x y')
   expr = x + 2*y
   expanded_expr = expand(x*expr)  #结果为x**2 + 2*x*y
   factor(expanded_expr)           #结果为x*(x + 2*y)
   ```
   
5. 例子：

   ```python
   from sympy import *
   x, t, z, nu = symbols('x t z nu')
   init_printing(use_unicode=True)    #使用Unicode字符输出，更美观
   diff(sin(x)*exp(x), x)  #对x求导。结果如下，高一格是幂次。
    x           x       
   ℯ ⋅sin(x) + ℯ ⋅cos(x)
   integrate(exp(x)*sin(x) + exp(x)*cos(x), x)  #计算不定积分，结果如下：
    x       
   ℯ ⋅sin(x)
   integrate(sin(x**2), (x, -oo, oo))  #计算定积分，oo表示无穷大。
   √2⋅√π
   ─────
     2
   limit(sin(x)/x, x, 0)  #求x→0时的极限
   1
   solve(x**2 - 2, x)     #解方程x^2-2=0，自变量为x。结果如下，2个根。
   [-√2, √2] 
   
   Matrix([[1, 2], [2, 2]]).eigenvals()  #求矩阵[1&2//2&1]的特征值
   ⎧3   √17     3   √17   ⎫
   ⎨─ - ───: 1, ─ + ───: 1⎬
   ⎩2    2      2    2    ⎭
   latex(Integral(cos(x)**2, (x, 0, pi)))  #输出latex结果
   \int\limits_{0}^{\pi} \cos^{2}{\left(x \right)}\, dx
   ```
   
6. 使用符号变量构造其他变量后，二者就没有关系了：

   ```python
   x = symbols('x')
   expr = x + 1
   x = 2     #此时变量x就不代表符号x了。
   print(expr) #结果还是x+1，
   ```
   
7. 符号表达式可以通过将符号变量替换为具体数值，来求值：

   ```python
   x = symbols('x')
   expr = x + 1
   expr.subs(x, 2)   #结果为3
   ```
   
8. =在Sympy中表示赋值，==只是比较结构是否相等，而不是产生一个表达式：

   ```python
   x + 1 == 4       #结果为 False，因为x+1可能是任意值，不恒等于4。
   2*(x+1) == 2*x+2 #结果为 True
   Eq(x+1,4)    #产生一个符号表达式，判断x+1是否等于4.
   Eq(x+1,4).subs(x,3)   #结果为true，因为3+1 == 4。
   ```

# Matplotlib

1. matplotlib十分适合编写短小的脚本来进行快速绘图，采用面向对象技术实现，

2. 例子：

   ```python
   import numpy as np
   import matplotlib.pyplot as plt
   x = np.linspace(0,20,100)
   y = np.sin(x)
   plt.plot(x, y)    #默认是折线图
   plt.show()
   
   siny=np.sin(x)
   cosy=np.cos(x)
   plt.figure(figsize=(5,3),dpi=300)   #单位 inch
   plt.plot(x, siny,label='U1',color='red',linestyle='--',linewidth=3)
   plt.plot(x, cosy,label='U2',color='y',linestyle='-.',marker='*')#为每条线增加标识
   plt.legend()     #显示图例
   plt.xlim(0,5)    #设置坐标轴的范围
   plt.ylim(-0.5,1)
   plt.grid()       #设置网格
   plt.rcParams['font.sans-serif']=['SimHei']
   plt.rcParams['axes.unicode_minus']=False
   plt.xlabel('t/s')		#坐标轴标题
   plt.ylabel('Volt/V')
   plt.title('电压')        #题目
   plt.savefig('test')   #保存到当前目录下，默认为png格式。
   plt.show()       #一张图中画了两条曲线。
   ```

3. ![image-20201019095656225](Python科学计算应用基础.assets/image-20201019095656225.png)

4. 子图

   ```python
   plt.subplot(211)   #2行1列，第1个
   plt.plot(x, siny,label='U1',color='red',linestyle='--',linewidth=3)
   plt.subplot(212)   #2行1列，第2个
   plt.plot(x, cosy,label='U2',color='y',linestyle='-.',marker='*')
   ```

5. 默认大小为6x4inch，dpi为72。

6. 也可以使用子图对象来控制子图

7. ```python
   fig1 = plt.figure(dpi=150)   #单位 inch
   sub = [plt.subplot(221+i) for i in range(4)]
   
   for i in range(4):
       plt.sca(sub[i])   #切换当前要绘制的子图对象。
       plt.xlim(0,5)
       plt.plot(x, np.sin(i*x),label='U1',color='b',linestyle='-.',linewidth=1)
       
   plt.show()
   ```

   ![image-20201019151416047](Python科学计算应用基础.assets/image-20201019151416047.png)

8. 可用的线型有    '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

9. plt.plot()  折线图，plt.scatter()   散点图

10. 柱状图：plt.bar() 

11. ```python
    plt.figure(figsize=(5,3),dpi=100)   #单位 inch 
    cites = ['BJ','SH','TJ','CQ']
    GDP = [12400,13900,9386,9143]
    plt.bar(range(4),GDP)   #柱状图
    plt.title('GDP')
    plt.ylabel('GDP')
    plt.xticks(range(4),cites)
    
    plt.show()
    #横排的柱状图
    plt.barh(range(4),GDP)
    plt.title('GDP')
    plt.xlabel('GDP')
    plt.yticks(range(4),cites)
    plt.show()
    ```

12. 直方图是一种概率统计图

    ```python
    x = np.random.normal(70,10,10000000)
    plt.hist(x,100)   # 若开启density=True，则会绘制概率，总面积为1。
    plt.show()
    ```

    ![image-20201019153922560](Python科学计算应用基础.assets/image-20201019153922560.png)

13. 使用opencv读取图片，结果为ndarray类型，3维数组，每个数据是uint8。

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import cv2
    #%%
    img = cv2.imread(r'G:\Python file\test.png')[:,:,::-1] #opencv存储颜色是按照bgr的顺序，一般图片都是rgb的顺序。对像素1维进行倒序。
    img.shape
    Out[10]: (600, 900, 3)
    ```


# Pandas

1. Pandas在NumPy的基础上提供了类似于电子表格的数据结构DataFrame，核心运算函数使用CPython编写，灵活而高效。

2. numpy是数据处理的基础包，pandas是在其上进行封装，相当于一个代码版的Excel。

3. 常见的读取函数：pandas.read_csv或pandas.read_sql（读取MySQL的数据库）或pandas.read_excel

4. ```python
   pvuv = pd.read_csv(
       fpath,
       sep="\t",  #tab键分割
       header=None,  #数据没有表头
       names=['pdate', 'pv', 'uv']    #手动指定表头
   )
   ```

5. 最重要的数据类型是DataFrame，相当于Excel中的一个sheet，当数据量巨大时，Excel就hold不住了。也类似于数据库中的一条一条的记录。

6. DataFrame的dtypes属性，可以给出每一列的数据类型。

7. ![image-20201007212851391](Python科学计算应用基础.assets/image-20201007212851391.png)

8. ```python
   data.index
   Out[7]: RangeIndex(start=0, stop=50, step=1)
   data.columns
   Out[8]: 
   Index(['排名', '球员', '球队', '得分', '命中-出手', '命中率', '命中-三分', '三分命中率', '命中-罚球',
          '罚球命中率', '场次', '上场时间'],
         dtype='object')
   data.shape   #50行，12列。表示有50条记录，每条记录有12个属性。
   Out[10]: (50, 12)
   data.values     #返回一个二维数组array
   Out[13]: 
   array([[1, '詹姆斯-哈登', '火箭', 34.3, '9.90-22.30', '44.4%', '4.40-12.40',
           '35.5%', '10.20-11.80', '86.5%', 68, 36.5],
          [2, '布拉德利-比尔', '奇才', 30.5, '10.40-22.90', '45.5%', '3.00-8.40',……
   data['得分']    #Series类型。   data.得分    也可以。
   Out[22]: 
   0     34.3
   ……
   48    17.8
   49    17.6
   Name: 得分, dtype: float64
   data[data['得分']<20]     #FancyIndex
   Out[24]: 
       排名            球员   球队    得分       命中-出手  ...  三分命中率      命中-罚球  罚球命中率  场次  上场时间
   26  27       尼古拉-约基奇   掘金  19.9  7.70-14.70  ...  31.4%  3.40-4.10  81.7%  73  32.0
   27  27        吉米-巴特勒   热火  19.9  6.00-13.10  ...  24.4%  7.60-9.10  83.4%  58  33.8
   ……
   49  50        克里斯-保罗   雷霆  17.6  6.20-12.70  ...  36.5%  3.60-4.00  90.7%  70  31.5
   [24 rows x 12 columns]
   data[data['得分']<20].to_csv("hh.csv")     #将一个dataframe保存到csv文件中，默认使用utf-8编码，Excel2010在打开时，会默认当做ANSI编码，也就是GBK编码，所以会乱码，用记事本保存一下就好了。因为csv文件本质上是纯文本文件，没有保存编码。不用额外的库。
   data[data['得分']<20].to_excel("kk.xlsx")   #不会发生乱码。需要安装openpyxl库。
   ```

9. Series相当于是在numpy数组基础上加了一个索引，索引不一定是数字，也可以是字符串等，类似于键值对。

10. dataframe是把多个列组合到一起，并为每一列添加了列名。

11. ![image-20201007223738443](Python科学计算应用基础.assets/image-20201007223738443.png)

12. ```python
    import numpy as np
    import pandas as pd
    s1 = pd.Series([56,78,89,80]) #默认会增加一个从0开始的索引。
    s1
    Out[2]: 
    0    56
    1    78
    2    89
    3    80
    dtype: int64
    s1.index      #默认的索引。
    Out[3]: RangeIndex(start=0, stop=4, step=1)
    s1.values
    Out[4]: array([56, 78, 89, 80], dtype=int64)
    s2 = pd.Series([56,78,89,80],index=['张三','李四','王五','赵六'])    #可以用list自定义index。
    s2
    Out[6]: 
    张三    56
    李四    78
    王五    89
    赵六    80
    dtype: int64
    s2.index
    Out[7]: Index(['张三', '李四', '王五', '赵六'], dtype='object')
    s2.values
    Out[8]: array([56, 78, 89, 80], dtype=int64)
    s2.to_dict()     #根据Series生成一个字典。
    Out[12]: {'张三': 22, '李四': 78, '王五': 89, '赵六': 80}
    pd.Series(s2.to_dict())    #和Python的字典类型特别像，可以用字典来创建Series。
    Out[13]: 
    张三    22
    李四    78
    王五    89
    赵六    80
    dtype: int64
    data={
            'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
            'year':[2000,2001,2002,2001,2002],
            'pop':[1.5,1.7,3.6,2.4,2.9]
        }
    df = pd.DataFrame(data)    #使用字典创建dataframe，字典的键是列名，值是多个行的对应的列的数据。一个键值对对应一个列的Series。
    df
    	state	year	pop
    0	Ohio	2000	1.5
    1	Ohio	2001	1.7
    2	Ohio	2002	3.6
    3	Nevada	2001	2.4
    4	Nevada	2002	2.9
    s2>60	#可以做比较运算，算数运算。
    Out[15]: 
    张三    False
    李四     True
    王五     True
    赵六     True
    dtype: bool
    ```

13. dataframe，相当于是np的二维数组，不过加了两种索引，一种是行index，一种是列columns。这里的一个index对应一条记录，也就是一个一维数组。

    ```python
    import numpy as np
    import pandas as pd
    dict_1 = {'国家':['中国','日本','韩国'],'首都':['北京','东京','首尔'],'人口':['2153','1178','1004']}
    d1 = pd.DataFrame(dict_1)
    d1
    Out[21]: 
       国家  首都    人口
    0  中国  北京  2153
    1  日本  东京  1178
    2  韩国  首尔  1004
    
    d1['国家']   #Series类型 默认索引。多了一个name属性。 这种方法只能索引列。
    Out[36]: 
    0    中国
    1    日本
    2    韩国
    Name: 国家, dtype: object
    d1.loc[0]   #Series类型，字符串索引。多了一个name属性。这种方法可以索引行，如果有两个参数，就是索引单元格。
    Out[37]: 
    国家      中国
    首都      北京
    人口    2153
    Name: 0, dtype: object
    d1.loc[0,'国家']
    Out[47]: '中国'
    d1.loc[[0,1],['国家','人口']]       #每个参数也可以是list。   
    Out[48]: 
       国家    人口
    0  中国  2153
    1  日本  1178
    df.loc[1:3]     #和Python不同，切片操作会包含末尾的值。
    	state	year	pop
    1	Ohio	2001	1.7
    2	Ohio	2002	3.6
    3	Nevada	2001	2.4
    d1.iloc[:2,:2]       #按照行和列的序号来索引。
    Out[56]: 
       国家  首都
    0  中国  北京
    1  日本  东京
    ```

14. 修改索引：

    ```python
    df.head()
    	ymd	bWendu	yWendu	tianqi	fengxiang	fengli	aqi	aqiInfo	aqiLevel
    0	2018-01-01	3℃	-6℃	晴~多云	东北风	1-2级	59	良	2
    1	2018-01-02	2℃	-5℃	阴~多云	东北风	1-2级	49	优	1
    2	2018-01-03	2℃	-5℃	多云	北风	1-2级	28	优	1
    3	2018-01-04	0℃	-8℃	阴	东北风	1-2级	28	优	1
    4	2018-01-05	3℃	-6℃	多云~晴	西北风	1-2级	50	优	1
    df.set_index('ymd', inplace=True)   #将ymd一列作为索引，改变dataframe。
    df.head()
    		   bWendu yWendu tianqi fengxiang fengli aqi aqiInfo aqiLevel
    ymd								
    2018-01-01	3℃	-6℃	晴~多云	东北风	1-2级	59	良	2
    2018-01-02	2℃	-5℃	阴~多云	东北风	1-2级	49	优	1
    2018-01-03	2℃	-5℃	多云	北风	1-2级	28	优	1
    2018-01-04	0℃	-8℃	阴	东北风	1-2级	28	优	1
    2018-01-05	3℃	-6℃	多云~晴	西北风	1-2级	50	优	1
    df.loc['2018-01-03':'2018-01-05', 'bWendu']    #传入的行是一个区间参数，他会默认进行连续索引。
    ymd
    2018-01-03    2
    2018-01-04    0
    2018-01-05    3
    Name: bWendu, dtype: int32
    df.loc[df["yWendu"]<-10, :]     #可以使用FancyIndex来作为索引。
    df.loc[lambda df : (df["bWendu"]<=30) & (df["yWendu"]>=15), :]  #使用lambda表达式来索引，其中的参数是整个dataframe。lambda表达式的结果也应是一个表示True或False的Series。
    ```

15. 也可以通过一个二维数组+行索引（可省略）+列索引（可省略）的方式来构建DataFrame：

    ```python
    d1 = pd.DataFrame([[200,300,200],[100,100,400],[200,100,300]],index=['2018','2019','2020'],\
                      columns=['北京','上海','广州'])
    d1
    Out[13]: 
         北京  上海  广州
    2018  200  300  200
    2019  100  100  400
    2020  200  100  300
    d1 = pd.DataFrame([[200,300,200],[100,100,400],[200,100,300]])
    d1
    Out[16]: 
         0    1    2
    0  200  300  200
    1  100  100  400
    2  200  100  300
    ```

16. 新增列：

    ```python
    df.assign(
        yWendu_huashi = lambda x : x["yWendu"] * 9 / 5 + 32,    #可以同时新增多个列，
        # 摄氏度转华氏度
        bWendu_huashi = lambda x : x["bWendu"] * 9 / 5 + 32
    )
    ```

17. Mapping和replace

    ```python
    import numpy as np
    import pandas as pd
    s1 = pd.Series([56,78,89,80])
    s2 = pd.Series([56,78,89,80],index=['张三','李四','王五','赵六'])
    dict_1 = {'国家':['中国','日本','韩国'],'首都':['北京','东京','首尔'],'人口':['2153','1178','1004']}
    d1 = pd.DataFrame(dict_1)
    dict_2 = {'北京':'炸酱面','首尔':'拌饭','东京':'寿司'}
    d1['首都'].map(dict_2)  # 把首都一列当做键，取dict_2字典中找出对应的值，结果构成一个新的Series。
    Out[3]: 
    0    炸酱面
    1     寿司
    2     拌饭
    Name: 首都, dtype: object
    d1['小吃']=d1['首都'].map(dict_2) #然后把这个Series添加到dataframe中。
    d1['小吃'].replace(['炸酱面','拌饭'],['炒肝','辣白菜'])  #原Series中的内容当做键，在replace函数的第一个参数中查找，替换为第二个参数中对应的内容。 结果构成一个新的Series。
    d1['小吃']=d1['小吃'].replace(['炸酱面','拌饭'],['炒肝','辣白菜'])
    ```

18. 对于Series和DataFrame的操作：

    ```python
    import numpy as np
    import pandas as pd
    s1 = pd.Series([56,78,89,80])
    s1.describe()     #只对数值列做统计，如果是文件读入的数据，可以用map进行强制类型转化。
    Out[2]: 
    count     4.000000
    mean     75.750000
    std      14.008926   # 计算的是样本方差，/n-1 
    min      56.000000
    25%      72.500000
    50%      79.000000
    75%      82.250000
    max      89.000000
    dtype: float64
    s1.sum(求和) .mode(众数)  .median(中位数)   .value_counts(统计出现的次数)
    ```

19. 两个序列做运算，会找键相同的值进行运算，不是共有的键，则产生NaN。

    ```python
    import numpy as np
    import pandas as pd
    s1 = pd.Series([56,78,89,80],index=['A','B','C','D'])
    s2 = pd.Series([56,78,89,80],index=['A','B','E','F'])
    s3=s1+s2
    s3
    Out[15]: 
    A    112.0
    B    156.0
    C      NaN
    D      NaN
    E      NaN
    F      NaN
    dtype: float64
    s3.notnull()     #判断是否是NaN。也可以用s3.isnull()。
    Out[16]: 
    A     True
    B     True
    C    False
    D    False
    E    False
    F    False
    dtype: bool
    s3 = s3.fillna(0) #用0填充NaN的单元格，
    s3
    Out[20]: 
    A    112.0
    B    156.0
    C      0.0
    D      0.0
    E      0.0
    F      0.0
    dtype: float64
    ```

20. 对于dataframe求和，也可以按照numpy的做法，来指定axis。

21. 协方差，相关系数：

    ```python
    df.cov()
    		bWendu  	yWendu  	aqi	      aqiLevel
    bWendu	140.613247	135.529633	47.462622	0.879204
    yWendu	135.529633	138.181274	16.186685	0.264165
    aqi	     47.462622	16.186685	2697.364564	50.749842
    aqiLevel	0.879204	0.264165	50.749842	1.060485
    df.corr()    #等于协方差矩阵对应元素除以对应的行和列的标准差的乘积。
           	bWendu	 	 yWendu			aqi		aqiLevel
    bWendu	1.000000	0.972292	0.077067	0.071999
    yWendu	0.972292	1.000000	0.026513	0.021822
    aqi	0.077067	0.026513	1.000000	0.948883
    aqiLevel	0.071999	0.021822	0.948883	1.000000
    import numpy as np
    hh = np.array(df.std().to_list()).reshape(4,1)  #获取标准差，并转化为列向量
    qq = df.cov()/hh.dot(hh.reshape(1,-1))   #对应元素相除。列向量×行向量得矩阵。
    round(qq-df.corr(),4)
    	bWendu	yWendu	aqi	aqiLevel
    bWendu	-0.0	-0.0	0.0	0.0
    yWendu	-0.0	0.0	-0.0	0.0
    aqi	0.0	-0.0	-0.0	0.0
    aqiLevel	0.0	0.0	0.0	-0.0
    ```

22. 排序

    ```python
    s3 = pd.Series(np.random.rand(10))
    s3
    Out[4]: 
    0    0.611097
    1    0.683698
    2    0.504156
    3    0.472029
    4    0.392766
    5    0.182160
    6    0.687666
    7    0.957690
    8    0.898446
    9    0.303043
    dtype: float64
    s3.sort_values()   #默认按照升序排列，ascending=True，修改为False则为降序。index也会跟着排序。并不会修改s3的值。
    Out[5]: 
    5    0.182160
    9    0.303043
    4    0.392766
    3    0.472029
    2    0.504156
    0    0.611097
    1    0.683698
    6    0.687666
    8    0.898446
    7    0.957690
    dtype: float64
    s3.sort_values().sort_index()  #按照index进行排序，也就是还原。
    Out[10]: 
    0    0.611097
    1    0.683698
    2    0.504156
    3    0.472029
    4    0.392766
    5    0.182160
    6    0.687666
    7    0.957690
    8    0.898446
    9    0.303043
    dtype: float64
    d1
    Out[16]: 
         0    1    2
    0  200  300  200
    1  100  100  400
    2  200  100  300
    d1.sort_values(0)     #只能按照列来排序，此处以第0列为主，从小到大排序。也可以用d1.sort_index()来恢复。
    Out[17]: 
         0    1    2
    1  100  100  400
    0  200  300  200
    2  200  100  300
    ```

23. Merge（两个dataframe要有公共的列才可以合并）

    ```python
    import numpy as np
    import pandas as pd
    d1 = pd.DataFrame({'City':['BJ','SH','GZ','SZ'],'GDP':[35271,38155,23628,26927]})
    d2 = pd.DataFrame({'City':['BJ','SH','CQ'],'People':[3016,2153,2423]})
    d1
    Out[3]: 
      City    GDP
    0   BJ  35271
    1   SH  38155
    2   GZ  23628
    3   SZ  26927
    d2
    Out[4]: 
      City  People
    0   BJ    3016
    1   SH    2153
    2   CQ    2423
    pd.merge(d1,d2,on='City') #将City作为主键，合并两个dataframe。首先把在两个dataframe中寻找主键相同的行，然后合并对应行的其余列。
    Out[5]: 
      City    GDP  People
    0   BJ  35271    3016
    1   SH  38155    2153
    
    pd.merge(d1,d2,on='City',how='inner')  #默认是inner，保留共有的。
    Out[5]: 
      City    GDP  People
    0   BJ  35271    3016
    1   SH  38155    2153
    pd.merge(d1,d2,on='City',how='left') #保留左边的那个参数的所有行。
    Out[6]: 
      City    GDP  People
    0   BJ  35271  3016.0
    1   SH  38155  2153.0
    2   GZ  23628     NaN
    3   SZ  26927     NaN
    pd.merge(d1,d2,on='City',how='right') #保留右边的那个参数的所有行。
    Out[7]: 
      City      GDP  People
    0   BJ  35271.0    3016
    1   SH  38155.0    2153
    2   CQ      NaN    2423
    pd.merge(d1,d2,on='City',how='outer') #左右都保留所有行。
    Out[8]: 
      City      GDP  People
    0   BJ  35271.0  3016.0
    1   SH  38155.0  2153.0
    2   GZ  23628.0     NaN
    3   SZ  26927.0     NaN
    4   CQ      NaN  2423.0
    ```

24. Concat（类似于numpy中的多维数组合并np.concatenate）和Combine(去重合并)

    ```python
    import numpy as np
    import pandas as pd
    s1 = pd.Series([35271,38155],index=['BJ','SH'])
    s2 = pd.Series([23628,23605],index=['GZ','CQ'])
    pd.concat([s1,s2])   #默认axis=0，竖着合并。还是Series。
    Out[10]: 
    BJ    35271
    SH    38155
    GZ    23628
    CQ    23605
    dtype: int64
    pd.concat([s1,s2],axis=1)   #如果axis=1，则会变成dataframe。
    Out[11]: 
              0        1
    BJ  35271.0      NaN
    SH  38155.0      NaN
    GZ      NaN  23628.0
    CQ      NaN  23605.0
    
    s1
    Out[15]: 
             BJ     SH     SZ
    2018  35271  38155  26927
    s2
    Out[16]: 
             BJ     SH     GZ
    2019  30320  23628  23605
    pd.concat([s1,s2])
    Out[17]: 
             BJ     SH       SZ       GZ
    2018  35271  38155  26927.0      NaN
    2019  30320  23628      NaN  23605.0
    
    s1
    Out[20]: 
    BJ    35271
    SH    38155
    dtype: int64
    s2
    Out[21]: 
    BJ    23628
    CQ    23605
    dtype: int64
    s1.combine_first(s2)   #如果有重复的index，则保留s1的数据。
    Out[22]: 
    BJ    35271.0
    CQ    23605.0
    SH    38155.0
    dtype: float64
    ```

25. Apply操作，根据axis参数来逐行或逐列调用函数，构成一个series：

    ```python
    import numpy as np
    import pandas as pd
    
    df = pd.DataFrame({'data':['city:BJ,GDP:35271,people:3016','city:SH,GDP:38155,people:2135',\
                               'city:CQ,GDP:23605,people:2423']})
    df1 = df['data'].apply(lambda line:pd.Series([item.split(':')[1]for item in line.split(',')]))#每个行返回一个series，对所有行调用完该匿名函数后，组成一个dataframe
    df1.columns=[item.split(':')[0]for item in df.data[0].split(',')]
    df1
    Out[56]: 
      city    GDP people
    0   BJ  35271   3016
    1   SH  38155   2135
    2   CQ  23605   2423
    # Series的apply函数接受一个函数参数，它会对每一行调用这个函数参数，并依次将每一行的内容作为参数传给这个函数。可以用lambda匿名函数。     类似于Excel中单独对一列进行操作一样。
    df1.GDP[0]
    Out[19]: '35271'   #可以看出这里的GDP是字符串类型，可以进行强制类型转化。
    df1.GDP = df1.GDP.map(float)  #这里的float是一个函数，
    df1.GDP[0]
    Out[23]: 35271.0      #可以看出转化成了浮点数。
    ```

26. 去重和清洗：

    ```python
    df1
    Out[4]: 
      city    GDP people
    0   BJ  35271   3016
    1   SH  38155   2135
    2   CQ  23605   2423
    df1.loc[3]=['BJ',35271,3016]
    df1
    Out[6]: 
      city    GDP people
    0   BJ  35271   3016
    1   SH  38155   2135
    2   CQ  23605   2423
    3   BJ  35271   3016
    df1.city.unique()     #查看这一列一共有多少种情况，重复的不多计算。
    Out[14]: array(['BJ', 'SH', 'CQ'], dtype=object)
    df1.city.value_counts()   #进行出现次数统计
    Out[15]: 
    BJ    2
    SH    1
    CQ    1
    Name: city, dtype: int64
    df1.city.duplicated()    #第一次出现时都记作False，后续出现的重复都记作True。
    Out[16]: 
    0    False
    1    False
    2    False
    3     True
    Name: city, dtype: bool
    df1.city.drop_duplicates() #去重
    Out[17]: 
    0    BJ
    1    SH
    2    CQ
    Name: city, dtype: object
    df1 = df1.drop_duplicates(['city'])   #删除city列重复的行，保留第一个出现的。
    df1
    Out[20]: 
      city    GDP people
    0   BJ  35271   3016
    1   SH  38155   2135
    2   CQ  23605   2423
    ```

27. 分箱（类似于Excel的筛选，为每一行增加一个新的列数据）和分组（）：

    ```python
    import numpy as np
    import pandas as pd
    scores = np.random.randint(0,100,size = 200)
    bins = [0,59,70,80,90,100]  #边界数组。分为了5段。左开右闭。
    pd.cut(scores,bins)
    Out[4]: 
    [(90, 100], (0, 59], (70, 80], (0, 59], (70, 80], ..., (0, 59], (0, 59], (0, 59], (59, 70], (0, 59]]
    Length: 200
    Categories (5, interval[int64]): [(0, 59] < (59, 70] < (70, 80] < (80, 90] < (90, 100]]
    pd.cut(scores,bins,labels=['E','D','C','B','A'])    #也可以给每段做标记。
    Out[7]: 
    [A, E, C, E, C, ..., E, E, E, D, E]
    Length: 200
    Categories (5, object): [E < D < C < B < A]
    pd.Series(pd.cut(scores,bins,labels=['E','D','C','B','A'])) #可以将分享的结果生成一个序列。
    df1 = pd.DataFrame(scores)
    df1['grade']=pd.cut(scores,bins,labels=['E','D','C','B','A'])
    ```

28. Excel操作，读取Excel2003的.xls文件需要xlrd库，读取Excel2007以后的.xlsx文件需要xlrd或openpyxl库：

29. ![image-20201009141656736](Python科学计算应用基础.assets/image-20201009141656736.png)

30. 默认返回第一个sheet的dataframe。如果参数是是none，那么字典的键是各个sheet的名字字符串。

31. ![image-20201009141731212](Python科学计算应用基础.assets/image-20201009141731212.png)

32. 对于没有表头的表格，需要设定header=none，如果有表头，则设置为0。

33. 默认情况下header=0，index_col=None。如果设置了header不为0，那么会跳过header上面的行。

34. ![image-20201009142701957](Python科学计算应用基础.assets/image-20201009142701957.png)

35. usecols参数可以只读取部分列，提高效率。切片包含左右边界值。下图中的AAA那一行为表头。str-list方法比较好，可读性好，也不怕列顺序变动。

36. ![image-20201009143401457](Python科学计算应用基础.assets/image-20201009143401457.png)

37. skiprows跳过行。一般如果要跳过列的话，可以用usecols来操作。

38. ![image-20201009144034860](Python科学计算应用基础.assets/image-20201009144034860.png)

39. 如果源文件没有标题行，则可以使用names来手动设置，记得设置header=None，也可以在读完之后，用dataframe.columns=来设置。

40. 可以通过dtype参数传入一个字典，来对每一列设置类型。

41. ![image-20201009144642905](Python科学计算应用基础.assets/image-20201009144642905.png)

42. 设置Series内储存数据的类型，object表示Series内的数据类型不唯一。下图中画框的类型是可以自动推导的。其余的要手动设置。也可以在dataframe的dtypes属性中查看类型。使用dataframe的astype()函数设置类型。

43. 当一列的数据只有几种情况时，可以设置为分类数据类型category。可以更快的索引，节约内存，还可以排序。

44. 设置dtype的目的是，不同的类型有不同的操作函数。所以一般都要有一个明确的类型，而不是object。

45. <img src="Python科学计算应用基础.assets/image-20201009144801373.png" alt="image-20201009144801373" style="zoom: 50%;" />

46. 选择对应的列为日期列，并解析它们。

47. ![image-20201009150223029](Python科学计算应用基础.assets/image-20201009150223029.png)

48. 下图左边的标准日期类型，不用设置日期解析器，右边的非标准的日期就需要手动设置。

49. ![image-20201009150310684](Python科学计算应用基础.assets/image-20201009150310684.png)

50. 在自动推导的时候，会参考Excel的列类型。可以通过多个分别表示时间的列（例如，年月日放在3个不同的列）合并成一个。

51. ![image-20201009152929202](Python科学计算应用基础.assets/image-20201009152929202.png)

52. data_parser接受一个函数，如下format参数可以解析2002年2月13日之类的日期。

53. ![image-20201009153646698](Python科学计算应用基础.assets/image-20201009153646698.png)

54. Pandas中常用NaN表示缺失值，是一个float类型。可以用na_values参数来指定那些内容被解析为NaN。可接受list，或字符串，数字等。默认全局的对应内容都会被解析为NaN，可以使用字典来直解析某些列中对应的内容为NaN（key是列名）。

55. ![image-20201009154410609](Python科学计算应用基础.assets/image-20201009154410609.png)

56. na_values = ['a',1]，这样所有内容为'a'或1的单元格会被解析为NaN。

57. 值转换函数，参数为一个字典，键为列明或索引，值为函数，可以对指定的列进行修改。可以用来对数据进行清洗，预处理。

58. ![image-20201009155038237](Python科学计算应用基础.assets/image-20201009155038237.png)

59. true_values false_values两个参数可以接受list，将对应的字符串转化为true或FALSE，只有某一列的内容全部可以转化时，才会转化该列。只对字符串有效。

60. ![image-20201009155450713](Python科学计算应用基础.assets/image-20201009155450713.png)

61. Excel中的列名可以重复，但是dataframe中不可以重复。

62. nrows参数可以指定要解析的行数（除了表头以外的）。

63. 使用dataframe.to_excel（）将对应的dataframe写入Excel文件。

64. <img src="Python科学计算应用基础.assets/image-20201009160627716.png" alt="image-20201009160627716" style="zoom: 67%;" />

65. 一般如果是默认的列索引，则可以不输出列索引。

66. ![image-20201009160801818](Python科学计算应用基础.assets/image-20201009160801818.png)

67. 在写入的时候，需要确保该文件当前没有被打开。

68. 实际使用的时候，index列也应该有一个名字，可以使用dataframe.index.name = 来设置。

69. ![image-20201009161227716](Python科学计算应用基础.assets/image-20201009161227716.png)

70. 使用ExcelWriter可以一次写入多个sheet，同时修改时间格式。用ExcelWriter打开一个文件，to_excel可以往该writer代表的文件中写入多次数据。

71. ![image-20201009162057738](Python科学计算应用基础.assets/image-20201009162057738.png)

72. 不过以上的所有的to_excel都会导致覆盖原有的所有数据，这时需要使用openpyxl引擎来操作Excel。例如：

    ```python
    import pandas as pd
    import openpyxl
    excel_path = "testxl.xlsx"
    
    #对工作簿进行修改，使用openpyxl来操作。新建，复制等。
    wb = openpyxl.Workbook(excel_path)
    wb.save(excel_path)
    
    #使用pandas读入数据
    data = pd.read_excel(excel_path,sheet_name='S1')
    
    #修改data
    
    #使用openpyxl引擎写入数据，避免覆盖。
    writer = pd.ExcelWriter(excel_path,engine='openpyxl')
    writer.book = openpyxl.load_workbook(writer.path)  #这一步不可少，否则会覆盖掉之前的所有表。这一步只是确定了工作簿，并没有决定要写入的工作表。
    data.to_excel(writer,sheet_name='S22')
    writer.save()
    
    #最后应该close，close前的所有操作，及时sheet_name相同，也不会覆盖。
    #而close之后，起始还可以写入，此时sheet_name相同，则会覆盖。
    writer.close()
    ```

73. 读写CSV文件。大部分参数和Excel是一样的。读写CSV文件需要特别注意编码。CSV文件在写入时，都要设置index=False，否则产生不是标准的CSV文件。

74. ![image-20201009195256960](Python科学计算应用基础.assets/image-20201009195256960.png)

# openpyxl

1. openpyxl没有关闭的概念，因为根本就没有打开过，只需要新建→保存或者打开→保存。
2. 和pandas不同，他是以workbook为主操作的。pandas的写入是以writer为主的。
3. 不存在另存为，可以保存到另一个路径下即可。
4. 用[]从工作簿中获得工作表，不可以使用数字索引，只能使用工作表名称。可以用wb.worksheets[0]来索引第一个工作表。
5. wb.active获取保存前的那个工作表，也就是用软件打开的默认的那个工作表。
6. ![image-20201010202522664](Python科学计算应用基础.assets/image-20201010202522664.png)
7. 
8. ![image-20201010204129508](Python科学计算应用基础.assets/image-20201010204129508.png)
9. 工作表['A1']或者工作表.cell(1,1)都可以或得单元格，单元格.value可以获得单元格的值。行列的起始从0开始。
10. 也可以进行行列区域的选择，例如   ['A2:C4']  交叉的单元格  或者   ['A:C']  A-C列    或者    ['2:5']   2-5行。
11. 对于['A2:C4']，获得的是一个二维的元组，索引方式类似于二维数组。['A2:C4']\[0\]获得的是第2行的数据。先索引行，再索引列。
12. 对于['A:C']，也是一个二维的元组，虽然没有指定行的范围，但是会默认取到最大的有数据的行，如果是空表，则去前4行。不过此时，单元格的索引时先列后行，基['A:C']\[0\]是A列。

# CPython

1. python的动态特性虽然方便了程序的开发，但是会极大降低运行的速度。CPython可以将添加了类型声明的Python程序编译为C语言程序，再编译为扩展模块，从而提高程序的运行速度。