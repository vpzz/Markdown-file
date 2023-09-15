# 基础

1. Python的整型是变长存储的，不存在C语言中的溢出问题。

2. //表示除法向下取整，Python中的浮点数不区分单精度和双精度。

3. 布尔类型为False和True，开头大写。支持与或非运算。 2>1 and 2<3结果为True。and or not相当于C语言中的 && || ！

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

13. 数据结构关注 时间和空间复杂度，时间尤其重要。

14. 例如利用函数递归来计算斐波那切数列，程序编制十分简单。

15. ```python
    def fib(n):
        if n<=2:
            return 1
        return fib(n-1)+fib(n-2)
    ```

16. 计算流程展开是树形结构，不同的分支存在重复计算。所需时间随着问题规模n的增加指数增加。自顶向下

17. <img src="Python科学计算应用基础.assets/image-20200831141304238.png" alt="image-20200831141304238" style="zoom:50%;" />

18. 可以使用迭代的方式来避免重复计算。所需时间随着问题规模n的增加线性增加。自底向上

19. ```python
    def fib1(n):
        prev,curr = 1,1
        k = 2
        while k<n:
            prev,curr = curr,prev+curr
            k = k+1
        return curr
    ```

20. 常用算法的时间复杂度：O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)

21. python中有4种数据结构类型：list相当于线性表。tuple是只读列表，set是元素不重复的列表，dict是键值对。

22. 数据结构中学到的有链表，数组，二叉树，哈希表，图

23. list 底层使用的是数组。链表和数组的区别是数组是挨个排放的，如果在头部插入，就得把数组整体向后移动。链表则对头尾插入不敏感。数组是单向的，链表是双向的。数组从尾部插入时间复杂度为O(1)，从头部插入时间复杂度为O(n)。O(1)表示和数组的长度n无关。链表从任何地方插入时间复杂度都是O(1)。

24. set底层使用的是哈希表。查找速率飞起，远比数组快得多。时间复杂度为O(1)。数组的查找是从头开始逐个查询。时间复杂度为O(n)。哈希表的方法是将待查询的数据送给hash函数，hash函数输出该数据应在的地址，直接根据地址查找该地址内是否存在该数。时间复杂度为 O(n)。

25. dict也是哈希表。

26. 树的查找算法复杂度为O(logn)，每询问一次，就将问题的规模缩减为原来的一半。

27. <img src="Python科学计算应用基础.assets/image-20200831211316165.png" alt="image-20200831211316165" style="zoom:50%;" />

# Numpy

1. numpy的基本数据类型为多维数组ndarray。      一维数组建议使用小写字母，多维数组建议使用大写字母。

2. 一般使用import numpy as np

3. np.array()可以接受一个list对象，创建一个array类型的对象。

4. ```python
   import numpy as np
   a1 = np.array([1,2,3,4,5])
   type(a1)
   Out[3]: numpy.ndarray
   ```

   Python中常用的列表推导：

5. ```python
   L=[1.0 for i in range(10)]
   等价于
   L=[]
   for i in range(10):
       L.append(1.0)
   上边的代码生成了一个这样的列表：[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
   同理也可以使用如下代码来生成一个等差数列：
   L=[i for i in range(10)]
   此时L=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   也可以对迭代变量进行筛选，如下：
   print([i for i in range(11) if i > 4])
   # 输出结果:
   [5, 6, 7, 8, 9, 10]
   ```

6. 从下面四个求和运算分别花费的时间，可以看出使用全套的numpy的速度最快，其次是全套的Python。而较差使用是比较差的，因为还要进行类型转化。==在Python中，所有的变量都是类的对象，而在numpy中，所有的变量都是C语言的基本数据类型。==

7. python和numpy都有各自的求和函数。

8. ```python
   L = [1.0 for i in range(10000000)]
   sum(L)            #1  49ms
   np.sum(L)         #2  439ms
   
   L1 = mp.array(L)
   sum(L1)           #3  903ms
   np.sum(L1)        #4  13.4ms
   
   ```

9. ==numpy的计算效率比Python原生的速度还要快==。因为它的==底层都是C语言实现的==，因此他和C语言一样有多种整型。例如int8 int16 int32 int64。

10. 同时由于Python对每个数据还要额外保存类型信息，numpy是统一保存，也可以节省空间，额外的信息会在一个array类型中统一保存。

11. 例如Python的源代码中，对于浮点数除了都是用double类型外，还保存了一个对象的头部信息，包含类型和引用次数等信息。

    ```c
    typedef strcut{
        PyObject_HEAD
        double ob_fval;
    }PyFloatObject
    ```

12. ==numpy的基本数据类型，比C语言还丰富。==

14. <img src="Python科学计算应用基础.assets/image-20200831214839715.png" alt="image-20200831214839715" style="zoom:50%;" />

15. ==使用.dtype属性来查看numpy.array对象内存储的数据的类型==。整型默认使用==int32==存储，浮点数默认使用==float64==存储。

16. ```python
    L = numpy.array([1,2,3,4])
    L.dtype
    Out[19]: dtype('int32')
    L.nbytes
    Out[20]: 16
    
    L1 = L.astype(numpy.int64)
    Out[25]: array([1, 2, 3, 4], dtype=int64)
    L1.dtype
    Out[26]: dtype('int32')
    L1.nbytes
    Out[27]: 32
    ```

17. 可以使用==.astype(numpy.int64)来修改存储的数据类型==。通过.nbytes属性来查看对象内所存储的数据占用的==总字节==数。这个数值除以元素个数，就是每个元素的字节数。

18. astype函数并不会修改原来的对象，而是返回一个新的对象。如下：

19. ```python
    L = numpy.array([1,2,3,4])
    L1 = L.astype(numpy.int64)
    L
    Out[4]: array([1, 2, 3, 4])
    L1
    Out[5]: array([1, 2, 3, 4], dtype=int64)
    ```

    可以看到如果ndarray中存储的数据不是对应的默认类型，例如int32和float64，就会显示类型信息dtype。

    ![image-20201003171104736](Python科学计算应用基础.assets/image-20201003171104736.png)

20. 4个int32的整数，每个整数占用4个字节，一共16个字节。4个int64的整数，一个占用8个字节，一共32个字节。

21. 如果通过修改对象的dtype，则不会更改对象的存储方式，只会更改==解释对象内存储内容的方式==。如下：

22. ```
    L
    Out[12]: array([1, 2, 3, 4])
    L1
    Out[12]: array([1, 2, 3, 4],dtype=int64)
    L1.dtype = numpy.int32
    L1
    Out[11]: array([1, 0, 2, 0, 3, 0, 4, 0])
    L1.nbytes
    Out[17]: 32
    ```

23. 可以看到直接修改后，L1的字节数还是32，没有变小为16。同时每个数中间又多了一个0。这是因为在小端存储的内存中，64位的数据是如果按照两个32位来解释，高32位为高地址，低32位为低地址。因此会之前的一个64位的1，现在被解释成了2个32位的数，一个是1，一个是0。

24. ```python
    import numpy as np
    a1 = np.array([1,2,3,4,5])
    print(a1)
    print(a1.flags)   #标志位
    print(a1.shape)   #多维数组的形状 （8,）表示是1维，这1维中有8个元素。8行的意思。
    print(a1.strides) #每个维度元素之间的字节数间隔。实际是该维度元素的大小。
    print(a1.ndim)    #数组的维数
    print(a1.data)	  #存储的数据块的内存地址，同一个数据块可以被不同的ndarray引用。
    print(a1.size)    #总的元素个数，等于shape的各个维度相乘。
    print(a1.itemsize)#每个元素的字节数。
    print(a1.nbytes)  #总的字节数，=itemsize*size。
    print(a1.base)    #表示data是复用的哪个变量，如果flags中的owndata是true，那么base就是none。
    
    [1 2 3 4 5]
      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : True	#true表示这个变量a1拥有a1.data这个数据块。
      WRITEABLE : True
      ALIGNED : True	#对齐相关
      WRITEBACKIFCOPY : False
      UPDATEIFCOPY : False
    
    (5,)
    (4,)
    1
    <memory at 0x0000000008F74280>
    5
    4
    20
    None
    ```

25. 如果对array进行切片操作，例如：

26. ```python
    a2 = a1[0:3]
    print(a2.flags)
      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : False
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False
      UPDATEIFCOPY : False
    ```

    可以发现a2是复用了a1中的数据，此时修改a1中的数据，a2会变化，反之亦然。

27. ```python
    a1 = np.append(a1,[6,7,8,9])
    a1
    Out[24]: array([8, 2, 3, 4, 5, 6, 7, 8, 9]) #9个元素
    a2 = a1.reshape(3,3)
    a2
    Out[25]: 
    array([[8, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
    a2.shape
    Out[27]: (3, 3)
    ```

28. 通过这个append的函数可以看出，np把函数的功能是现在np模块内，而不是ndarray类中，这样可以减小类的体积，运算更快。

29. reshape函数可以变换维度，而不改变数据，其中的一个参数可以写成-1，np会自动计算。该操作不改变内存的数据，只是改变结构化解析数据的方式，所以速度很快。

30. 如果reshape只传递一个参数-1，则会将该数组变为1维数组。

31. 可以看到，对于6这个元素，应先索引到a2数组的第1个元素array([4,5,6])。然后再索引第2个元素，即a2[1,2] 

32. 下标从0开始。==多维数组可以看做是数组的嵌套。==

33. 二维数组最原始的理解应该是把一行或者一列数据进行分割，它和矩阵的关系不是天然的。

34. 可以看到默认的1维数组可以看做列向量，因为他的shape是（9，)，如果要是和二维数组的shape含义统一，那么这个==（9，）就表示（9，1）即9行1列，即是一个列向量==。这两个还是不同的，(9,1)表示1维数组，(1,9)表示2维数组。遍历的时候需要注意。

35. 可以使用reshape来转换行列向量：

36. ```python
    import numpy as np
    a1 = np.array([1,2,3,4,5])
    a1
    Out[8]: array([1, 2, 3, 4, 5])
    a1.shape
    Out[2]: (5,)
    a1.ndim
    Out[3]:1
    a2 = a1.reshape(1,5)
    a2
    Out[7]: array([[1, 2, 3, 4, 5]])
    a2.shape
    Out[9]: (1, 5)
    a2.ndim
    Out[10]:2
    ```

37. 返回的shape是元组类型，使用 row,col = a1.shape来解析。

38. ```python
    import numpy as np
    a1 = np.array([i+1 for i in range(8)])
    a1.shape
    a2 = a1.reshape(2,4)
    a2
    Out[6]: 
    array([[1, 2, 3, 4],
           [5, 6, 7, 8]])
    a2.strides
    Out[5]: (16, 4)  #这个16表示a2[0]和a2[1]头部相差的字节数，表示a2[0]或a2[1]的大小，1个元素4个字节，4个元素一共16字节。这个4表示a2[0][0]和a2[0][1]头部相差的字节数，即a2[0][0]的大小，1个元素就是4个字节。
    a1.flags
    Out[8]: 
      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : True
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False
      UPDATEIFCOPY : False
    a2.flags
    Out[7]: 
      C_CONTIGUOUS : True
      F_CONTIGUOUS : False
      OWNDATA : False
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False
      UPDATEIFCOPY : False
    ```

39. reshape还是复用内存块。如果不想复用，可以使用.copy()函数

40. ```python
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

41. 之所以要这么多属性，是为了效率优化。

41. Python标准库中也有一个array库。Python下一共可用4种数组类型。

    ```
    numpy.array    array.array    list      collection.deque
    ```

43. np支持修改数据的存储方式，大小端：

45. ```python
    import numpy as np
    a1 = np.array([i+1 for i in range(8)])
    a1.dtype = '>i2' # <表示小端 >表示大端， int8 in16 in32 int64可以用 i1 i2 i4 i8来替代。
    a1
    Out[5]: 
    array([ 256,    0,  512,    0,  768,    0, 1024,    0, 1280,    0, 1536,
              0, 1792,    0, 2048,    0], dtype=int16)
    ```

46. numpy数组和矩阵的生成有如下几种方法：

    1. zeros，ones（和zeros用法相同，只不过是元素都是1），full（用法也相同，不过可以指定值）

       ```python
       import numpy as np
       a1 = np.zeros(10)    #默认是浮点数
       a2 = np.zeros(10,dtype='int32')   #可以使用dtype来强制使用别的数据类型，这个dtype也可以用np.int32
       a3 = np.zeros((2,3))  #生成多维数组需要使用元组
       a5 = np.full((2,3),fill_value=3.2)
       a5
       Out[10]: 
       array([[3.2, 3.2, 3.2],
              [3.2, 3.2, 3.2]])
       ```

       range()其实是有3个参数，range(2,10,3)是指从2开始数，间隔为3，最后一个数<10。第一和第三个参数默认为0和1。

       ```python
       list(range(2,10,3))
       Out[14]: [2, 5, 8]
       ```

    2. arange(和range的用法一样，不同的是他返回的是ndarray而不是迭代器，同时Python自带的range所有参数只支持整数，而numpy的arange就可以是浮点数)和linspace（适用于知道要分段的数量，而不知道每段的 长度）

       ```python
       np.arange(2,10,3)
       Out[15]: array([2, 5, 8])
       np.linspace(1,5,6)    #把1到5之间分为(6-1)段  即算上开头结尾，一共有6个数。
       Out[20]: array([1. , 1.8, 2.6, 3.4, 4.2, 5. ])    #默认为浮点数
       ```
    
    3. 用随机数填充，numpy自带的随机数库为np.random

       ```python
       np.random.randint(0,10)  #生成一个随机整数，不会取到10，但会取到0。均匀分布
       Out[23]: 5
       np.random.randint(0,10,size=(4,5))   #使用size来生成多个值，构成多维数组。size可以省略，只写元组
       Out[45]: 
       array([[5, 3, 6, 7, 9],
              [5, 7, 7, 8, 5],
              [5, 1, 1, 7, 3],
              [4, 5, 4, 8, 6]])
       np.random.seed(555)
       np.random.randint(0,10,size=(4,5))
       np.random.random(10)   #生成0到1之间的浮点数，10表示size参数。均匀分布
       Out[52]: 
       array([0.8926319 , 0.82475265, 0.56296713, 0.20633491, 0.51901626,
              0.21315057, 0.70473498, 0.63847195, 0.71946907, 0.73001423])
       np.random.normal(10,1,(5,5))   #均值，标准差，默认是标准正态分布，均值为0，标准差为1。
       Out[56]: 
       array([[10.09920756, 10.45973843, 10.46893251, 10.08586251, 10.38594659],
              [12.38408029,  9.4892512 , 11.12220288,  9.98666508,  9.48738844],
              [11.65244153, 10.09515018, 12.05926456,  9.69986765,  8.09086253],
              [10.23936329, 10.90041123,  9.48025634,  8.96784637,  9.66475886],
              [10.69037768, 10.68503437, 10.45207827, 10.52940481,  9.98909406]])
       ```
    
       每次生成随机数的时候，都会使用种子，如果没有设置（紧挨着这个生成的函数前设置才有效），就使用当前时间，如果种子一样，那么随机序列也是一样的。每次生成完成依次随机数，都会修改种子，所以要复现，就必须啊在每次生成前都设置一下随机数。在软件测试时会使用种子，确保测试环境的可重复性。
    
47. 基本操作：

    1. 索引（==a [2] [3]，a [2,3]，a [(2,3)] 是一样的==）和切片(默认不会创建新的内存块)

       ```python
       import numpy as np
       np.arange(15)
       Out[2]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
       x = np.arange(15)
       X = x.reshape(3,5)
       x[3:8]    #切片操作用：  参数是下标，不包含最后一个下标。
       Out[5]: array([3, 4, 5, 6, 7])
       x[3:8:2]  #切片的第三个参数表示间隔，三个参数都可以省略，省略是分别表示从开头，到末尾，间隔为1。
       Out[6]: array([3, 5, 7])
       x[::-1]   #逆序的方法。
       Out[7]: array([14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0])
       
       X
       Out[9]: 
       array([[ 0,  1,  2,  3,  4],
              [ 5,  6,  7,  8,  9],
              [10, 11, 12, 13, 14]])
       X[:2,:3]	#类似于子矩阵一样，取第0，1行，和第0，1，2列相交的所有元素。不能使用x[:2][:3]因为这相当于分开去两次行的操作。所以推荐使用[,]来索引元素。但是Python的list不支持这种方法。
       Out[28]: 
       array([[0, 1, 2],
              [5, 6, 7]])
       ```

       不能离散的进行切片，例如x[1,4,7]不是把x的下标为1，4，7的元素提取出来，而是把取x [1] [4] [7]这个元素。

       如果要跳过行（或者说是所有行），只取某些列，可以用a [:，::2]每隔两列取一个。

       ```python
       X[:,::2]
       Out[29]: 
       array([[ 0,  2,  4],
              [ 5,  7,  9],
              [10, 12, 14]])
       ```

    2. 合并（只能在维度相同的方向上进行合并）和分割（可以通过切片来完成，默认是复用原来的数据）

       ```python
       import numpy as np
       a1 = np.array([i+1 for i in range(8)])
       a1
       Out[2]: array([1, 2, 3, 4, 5, 6, 7, 8])
       a2 = a1.reshape(2,4)
       a3 = np.arange(10,18).reshape(2,4)
       np.vstack([a2,a3])     #垂直方向合并，需要列数相同。可以用np.concatenate([a2,a3])
       Out[5]: 
       array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [10, 11, 12, 13],
              [14, 15, 16, 17]])
       np.hstack([a2,a3])     #水平方向合并，需要行数相同。可以用np.concatenate([a2,a3],axis=1)
       Out[6]: 
       array([[ 1,  2,  3,  4, 10, 11, 12, 13],
              [ 5,  6,  7,  8, 14, 15, 16, 17]])
       a4
       Out[10]: array([30, 31])
       np.hstack([a2,a4.reshape(2,1)])  #在进行合并的时候，向量默认看做是一个只有一行的矩阵，而不是列向量，所以此处需要reshape。
       Out[12]: 
       array([[ 1,  2,  3,  4, 30],
              [ 5,  6,  7,  8, 31]])
       
       
       a1
       Out[14]: array([1, 2, 3, 4, 5, 6, 7, 8])
       x1,x2,x3 = np.split(a1,[2,5])  #第二个参数是分割点的下标，分割点归后一段。
       print(x1,x2,x3)
       [1 2] [3 4 5] [6 7 8]
       ```
    
48. 数组的运算，从下面的例子可以看出numpy对大规模数组的操作效率很高：

    ```python
    n=1000000
    L=[i for i in range(n)]
    A=[]
    %timeit for i in L:A.append(i*2)     #花费167ms
    N=np.array(L)
    %timeit N*2         #花费3.09ms
    ```

49. 数组和数的加减乘除相当于对其中的每一个元素进行该运算

    ```python
    import numpy as np
    X = np.arange(15).reshape(3,-1)
    X
    Out[3]: 
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
    X+1
    Out[4]: 
    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15]])
    X*2
    Out[5]: 
    array([[ 0,  2,  4,  6,  8],
           [10, 12, 14, 16, 18],
           [20, 22, 24, 26, 28]])
    X/2
    Out[6]: 
    array([[0. , 0.5, 1. , 1.5, 2. ],
           [2.5, 3. , 3.5, 4. , 4.5],
           [5. , 5.5, 6. , 6.5, 7. ]])
    X//2
    Out[7]: 
    array([[0, 0, 1, 1, 2],
           [2, 3, 3, 4, 4],
           [5, 5, 6, 6, 7]], dtype=int32)
    1/X       #第一个元素是1/0，报错
    <ipython-input-8-6b91d9b9bddc>:1: RuntimeWarning: divide by zero encountered in true_divide
      1/X
    Out[8]: 
    array([[       inf, 1.        , 0.5       , 0.33333333, 0.25      ],
           [0.2       , 0.16666667, 0.14285714, 0.125     , 0.11111111],
           [0.1       , 0.09090909, 0.08333333, 0.07692308, 0.07142857]])
    
    X**2    #乘方运算是对每个元素进行乘方，而不是矩阵的乘法。
    Out[9]: 
    array([[  0,   1,   4,   9,  16],
           [ 25,  36,  49,  64,  81],
           [100, 121, 144, 169, 196]], dtype=int32)
    ```

50. 除了一些Python中自带的基本运算，还可以使用numpy带的一些数学运算。

    ```python
    np.abs(X-5)
    Out[10]: 
    array([[5, 4, 3, 2, 1],
           [0, 1, 2, 3, 4],
           [5, 6, 7, 8, 9]])
    ```

    还有np.sin(X)   np.exp(X)  np.power(3,X) 第一个参数是指数。

51. 矩阵运算：默认的操作都是针对数组的，矩阵运算要使用特殊的函数，例如：

    ```python
    import numpy as np
    A = np.arange(9).reshape(3,3)
    B = np.arange(10,22).reshape(3,-1)
    A
    Out[4]: 
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
    B
    Out[5]: 
    array([[10, 11, 12, 13],
           [14, 15, 16, 17],
           [18, 19, 20, 21]])
    A.dot(B)      #矩阵乘法A×B，需要前一个矩阵的列数=后一个矩阵的行数
    Out[11]: 
    array([[ 50,  53,  56,  59],
           [176, 188, 200, 212],
           [302, 323, 344, 365]])
    A*B          #数组乘法，需要数组的shape完全相同，否则会报错。
    Traceback (most recent call last):
    
      File "<ipython-input-12-47896efed660>", line 1, in <module>
        A*B
    
    ValueError: operands could not be broadcast together with shapes (3,3) (3,4) 
    ```

52. 其他操作：转置（A.T），求逆（np.linalg.inv(A)），求伪逆（对于非方阵使用，np.linalg.pinv(A)）     linalg表示linear algebra 线性代数

53. 聚合运算（统计运算，此时只有数组（1维或多维），没有矩阵）：

    ```python
    A = np.random.random(10)
    A
    Out[35]: 
    array([[0.09669092, 0.81631401, 0.60266394, 0.69922033, 0.15391563],
           [0.11587795, 0.47536352, 0.5886525 , 0.69323412, 0.08176766]])  
    A.min()    #等价于np.min(A)
    Out[37]: 0.00255415634297651
    A.max()    #等价于np.max(A)，不过类的成员方法不如np的函数丰富。
    Out[38]: 0.9972413822675114
    np.median(A)   #中位数，比平均数更能体现平均水平，因为不容易被个别不合常理数影响。
    Out[41]: 0.6721791308516185
    A.sum()      #求和
    Out[50]: 6.0993883598269285
    A.prod()
    Out[52]: 2.4311519761696168e-05
    np.percentile(A,q=50)    #分位值，50分位就是中位数。
    Out[54]: 0.6721791308516185
    np.var(A)    #方差  =np.std(A)**2
    Out[55]: 0.10153859539741612
    np.std(A)
    Out[56]: 0.3186512127662723
    ```

54. 多维数组也可以进行上述的聚合运算，A.sum()是对所有元素求和，相当看做1维数组。如果要沿行或列方向求和，那么要设置axis值。对min，max等操作也都可以设置axis值。

    ```python
    A = np.arange(9).reshape(3,-1)
    A
    Out[59]: 
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
    A.sum()
    Out[60]: 36
    A.sum(axis=0)      #把二维数组当做多个列向量拼接起来的
    Out[61]: array([ 9, 12, 15])
    A.sum(axis=1)	   #把二维数组当做多个行向量拼接起来的
    Out[62]: array([ 3, 12, 21])
    ```

55. 对于一个2维数组A，3行4列。那么使用A[1,1]来进行索引时，==就是对它的两个axis进行索引==，axis=0的那个轴，范围是0-2；axis=1的那个轴，范围是0-3，二维数组不能按照C语言那样当做一维数组进行索引，例如A[5]会报错，提示5超出了axis=0的范围。

56. arg索引运算，例如a.min()是获得数组a的最小值，而对应的索引运算a.argmin()是获得该最小值的索引位置。

    ```python
    a1 = np.array([i+1 for i in range(8)])
    a1.max()
    Out[67]: 8
    a1.argmax()
    Out[68]: 7      #  a1[a1.argmax()] == a1.max()
    ```

57. 排序：

    ```python
    A = np.arange(16)
    A
    Out[72]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
    np.random.shuffle(A)   #乱序功能
    A
    Out[78]: array([13, 14, 15,  6,  1, 12,  7,  8,  3,  4, 11, 10,  5,  2,  0,  9])
    np.sort(A)       #不改变A的值
    Out[77]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
    np.argsort(A)  #返回的是索引，第一个14表示，排序后的第一个元素位于原序列的下标为14的地方
    Out[89]: 
    array([14,  4, 13,  8,  9, 12,  3,  6,  7, 15, 11, 10,  5,  0,  1,  2],
          dtype=int64)
    A[np.argsort(A)] == np.sort(A)     #讲一个数组传递给数组的索引，得到的也是一个数组，相当于是每个都去索引，然后再拼接成一个数组。
    Out[92]: 
    array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
            True,  True,  True,  True,  True,  True,  True])
    A
    Out[78]: array([13, 14, 15,  6,  1, 12,  7,  8,  3,  4, 11, 10,  5,  2,  0,  9])
    A.sort()         #会改变A的值
    A
    Out[80]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
    
    X = np.random.randint(0,10,size=(4,4))
    X
    Out[83]: 
    array([[8, 9, 9, 5],
           [9, 6, 9, 3],
           [3, 4, 8, 2],
           [6, 8, 2, 3]])
    np.sort(X)   #对二维数组的操作，默认是按照行来进行的，axis=1，个行向量拼接而成的矩阵。
    Out[84]: 
    array([[5, 8, 9, 9],
           [3, 6, 9, 9],
           [2, 3, 4, 8],
           [2, 3, 6, 8]])
    np.sort(X,axis=1)
    Out[85]: 
    array([[5, 8, 9, 9],
           [3, 6, 9, 9],
           [2, 3, 4, 8],
           [2, 3, 6, 8]])
    np.sort(X,axis=0)
    Out[86]: 
    array([[3, 4, 2, 2],
           [6, 6, 8, 3],
           [8, 8, 9, 3],
           [9, 9, 9, 5]])
    np.partition(A,2)    #把A的最小的3个数放到前3个顺序，不排序，其余的乱序。这种方法用在不需要排序的地方，会大大缩减时间。
    Out[99]: array([ 0,  1,  2,  6, 14, 12,  7,  8,  3,  4, 11, 10,  5, 15, 13,  9])
    ```

58. 比较运算和FancyIndex

59. 如果想要单独取某几个元素，可以用以下FancyIndex方法（将一个索引数组（==可以是np.array，也可以是list==）传递到原数组（==只能是np.array==）的索引位置，然后根据索引数组来生成新的数组，这个方法对于Python的list是不成立的）：

    ```python
    import numpy as np
    a1 = np.array([i+1 for i in range(8)])
    a1[[1,3,7]] #相当于从a1从取出来下表为1，3，7的元素，构成一个新的array。
    Out[2]: array([2, 4, 8])
    a1[np.array([1,3,7])]
    Out[5]: array([2, 4, 8])
    a1[np.array([[1,2],[3,5]])]    #索引数组可以是任意维数的，结果数组和索引数组维数相同。
    Out[6]: 
    array([[2, 3],
           [4, 6]])
    ```

60. 如果原数组是多维的，那么索引数组也要多个才可以。例如：

    ```python
    row =np.array([0,1,2])
    col = np.array([0,1,0])
    a1 = a1.reshape(4,-1)
    a1
    Out[30]: 
    array([[1, 2],
           [3, 4],
           [5, 6],
           [7, 8]])
    a1[row,col]
    Out[29]: array([1, 4, 5])
    ```

61. 还可以传递bool型数据来作为索引。

    ```python
    a1
    Out[31]: 
    array([[1, 2],
           [3, 4],
           [5, 6],
           [7, 8]])
    row = [True,True,False,True]   #True表示取该元素
    
    a1[row,1]
    Out[32]: array([2, 4, 8])
    ```

62. 可以结合比较运算来对数组进行筛选，例如：

    ```python
    a1=a1.reshape(-1)
    a1
    Out[39]: array([1, 2, 3, 4, 5, 6, 7, 8])
    a1>3
    Out[40]: array([False, False, False,  True,  True,  True,  True,  True])
    a1[a1>3]
    Out[41]: array([4, 5, 6, 7, 8])
    ```

63. 比较运算，它和fancyindex结合可以帮助更好地索引数据，方便数据预处理。

    ```python
    np.any(a1 == 3)  #主要有一个为True，就输出True
    Out[42]: True
    np.all(a1 == 3)  #只有全部为True，才输出True
    Out[43]: False
    np.count_nonzero(a1 == 3)   #计算a1中=0的元素的个数  等价于  np.sum(a1 == 3) 
    Out[44]: 1
    ```

64. KNN（k个最近邻居）分类算法：

    ```python
    import numpy as np
    from sklearn import datasets
    import matplotlib.pyplot as plt
    from collections import Counter
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    x = np.array([5.0,2.0,2.0,0.4])
    k=7
    plt.scatter(X[y == 0,0],X[y == 0,1])
    plt.scatter(X[y == 1,0],X[y == 1,1])
    plt.scatter(X[y == 2,0],X[y == 2,1])
    plt.scatter(x[0],x[1])
    plt.show()
    plt.scatter(X[y == 0,2],X[y == 0,3])
    plt.scatter(X[y == 1,2],X[y == 1,3])
    plt.scatter(X[y == 2,2],X[y == 2,3])
    plt.scatter(x[2],x[3])
    plt.show()
    def KNN_classify(k,x,X,y):
        print(Counter(y[np.argpartition(np.sum((X-x)**2,axis=1)**0.5,7)[:7]]).most_common(1)[0][0])
    KNN_classify(k,x,X,y)
    ```


# Scipy

1. 主要功能：优化问题求解，插值，数值积分，线性代数，信号处理。

2. scipy.constants模块包含了几乎所有的物理数学化学常数，例如：

   ```python
   import numpy as np
   from scipy import constants as C
   C.c
   Out[11]: 299792458.0
   C.h
   Out[12]: 6.62607015e-34
   C.pi
   Out[13]: 3.141592653589793
   ```

3. scipy.special模块的精度比Python自带的函数要高，当要对一些数值做更精确的计算时，应该用特殊函数库，例如：

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

4. 排列组合：$A_5^3$，$C_5^3$。

   ```python
   sp.perm(5,3)     
   Out[28]: 60.0
   
   sp.comb(5,3)
   Out[29]: 10.0
   ```

5. 优化问题，基本套路都是这样的：①通过分析问题，确定问题的损失函数或者效用函数②通过最优化损失函数或者效用函数，获得机器学习的模型。几乎所有的参数学习算法都是这样的套路。常用的最优化算法有两类：传统的，例如梯度下降，牛顿等；启发式的，例如粒子群，遗传，退火等算法。

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

   9. 线性代数scipy.linalg，numpy下也有这个函数库，scipy的库更丰富。

   10. 求解线性方程组：

       ```python
       import numpy as np
       import matplotlib.pyplot as plt
       import scipy.linalg as linalg
       A = np.array([[1,3,5],[2,5,1],[2,3,8]])
       b = np.array([10,8,3])
       x = linalg.solve(A,b)     #求解线性方程组
       x
       Out[12]: array([-9.28,  5.16,  0.76])
       A.dot(x)-b
       Out[13]: array([ 0.00000000e+00, -1.77635684e-15, -1.77635684e-15])
       linalg.det(A)
       Out[14]: -25.000000000000004
       
       l,v = linalg.eig(A)
       
       l
       Out[16]: array([10.5540456 +0.j, -0.5873064 +0.j,  4.03326081+0.j])
       
       v
       Out[17]: 
       array([[-0.51686204, -0.94195144,  0.11527992],
              [-0.32845853,  0.31778071, -0.81936883],
              [-0.79054957,  0.10836468,  0.56155611]])
       A.dot(v[:,0])-l[0]*v[:,0]  #特征向量是一列一列的，对应的特征值也是l的对应列。
       Out[19]: array([-1.77635684e-15+0.j, -1.77635684e-15+0.j,  0.00000000e+00+0.j])
       A.dot(v[:,1])-l[1]*v[:,1]
       Out[20]: array([-3.99680289e-15+0.j, -4.71844785e-16+0.j, -3.96904731e-15+0.j])
       ```

   11. SVD（奇异值）分解：

       ```python
       import numpy as np
       import scipy.linalg as linalg
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

   12. 数值积分：

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

   13. 信号处理，设计滤波器，过滤噪声：

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

   14. 傅里叶变换，将一个复杂的周期信号分解为多个正弦信号：

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

# Sympy

1. Sympy依赖于mpmath。符号计算可以利用符号进行表达式推导。符号计算又称为计算代数系统 computer algebra system  CAS。Sympy可以简化表达式，求导，积分，求极限，解方程，处理矩阵等。可以将结果输出成图片或Latex结果。

   ```python
   import math
   math.sqrt(8)   #结果为 2.8284271247461903 是近似值
   
   import sympy
   sympy.sqrt(3)  #结果为 sqrt(3)。会保留精确值。
   sympy.sqrt(8)  #结果为 2*sqrt(2)。会化简
   ```
2. 所有的符号变量都要用symbols定义。

   ```python
   from sympy import symbols
   x, y = symbols('x y')  #可以同时定义多个符号变量，符号变量可以有多个字符。符号的内容可以是python不允许的变量，例如: s1 = symbols("1s")
   expr = x + 2*y   #并不会计算表达式的值，而是保留符号
   expr - x   #输出2*y，x和-x会消掉。
   x*expr     #输出x*(x + 2*y)。而不是展开多项式。
   ```
3. 符号计算的结果可以设置不同的输出形式，展开或者因式分解形式。

   ```python
   from sympy import expand, factor
   x, y = symbols('x y')
   expr = x + 2*y
   expanded_expr = expand(x*expr)  #结果为x**2 + 2*x*y
   factor(expanded_expr)           #结果为x*(x + 2*y)
   ```
4. 例子：

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
5. 使用符号变量构造其他变量后，二者就没有关系了：

   ```python
   x = symbols('x')
   expr = x + 1
   x = 2     #此时变量x就不代表符号x了。
   print(expr) #结果还是x+1，
   ```
6. 符号表达式可以通过将符号变量替换为具体数值，来求值：

   ```python
   x = symbols('x')
   expr = x + 1
   expr.subs(x, 2)   #结果为3
   ```
7. =在Sympy中表示赋值，==只是比较结构是否相等，而不是产生一个表达式：

   ```python
   x + 1 == 4       #结果为 False，因为x+1可能是任意值，不恒等于4。
   2*(x+1) == 2*x+2 #结果为 True
   Eq(x+1,4)    #产生一个符号表达式，判断x+1是否等于4.
   Eq(x+1,4).subs(x,3)   #结果为true，因为3+1 == 4。
   ```
8. 
9. 
10. 
11. 
12. 
13. 
14. 
15. 
16. 
17. 
18. 
19. 
20. 
21. 
22. 
23. 
24. 
25. 
26. 

# Matplotlib

1. ```python
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

   ![image-20201019095656225](Python科学计算应用基础.assets/image-20201019095656225.png)

2. 子图

   ```python
   plt.subplot(211)   #2行1列，第1个
   plt.plot(x, siny,label='U1',color='red',linestyle='--',linewidth=3)
   plt.subplot(212)   #2行1列，第2个
   plt.plot(x, cosy,label='U2',color='y',linestyle='-.',marker='*')
   ```

3. 默认大小为6x4inch，dpi为72。

4. 也可以使用子图对象来控制子图

5. ```python
   fig1 = plt.figure(dpi=150)   #单位 inch
   sub = [plt.subplot(221+i) for i in range(4)]
   
   for i in range(4):
       plt.sca(sub[i])   #切换当前要绘制的子图对象。
       plt.xlim(0,5)
       plt.plot(x, np.sin(i*x),label='U1',color='b',linestyle='-.',linewidth=1)
       
   plt.show()
   ```

   ![image-20201019151416047](Python科学计算应用基础.assets/image-20201019151416047.png)

6. 可用的线型有    '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

7. plt.plot()  折线图， plt.scatter()   散点图 

8. 柱状图   plt.bar() 

9. ```python
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

10. 直方图是一种概率统计图

    ```python
    x = np.random.normal(70,10,10000000)
    plt.hist(x,100)   # 若开启density=True，则会绘制概率，总面积为1。
    plt.show()
    ```

    ![image-20201019153922560](Python科学计算应用基础.assets/image-20201019153922560.png)

11. 使用opencv读取图片，结果为ndarray类型，3维数组，每个数据是uint8。

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import cv2
    #%%
    img = cv2.imread(r'G:\Python file\test.png')[:,:,::-1] #opencv存储颜色是按照bgr的顺序，一般图片都是rgb的顺序。对像素1维进行倒序。
    img.shape
    Out[10]: (600, 900, 3)
    ```

12. 


# Pandas

1. numpy是数据处理的基础包，pandas是在其上进行封装，相当于一个代码版的Excel。

2. 常见的读取函数：pandas.read_csv或pandas.read_sql（读取MySQL的数据库）或pandas.read_excel

3. ```python
   pvuv = pd.read_csv(
       fpath,
       sep="\t",  #tab键分割
       header=None,  #数据没有表头
       names=['pdate', 'pv', 'uv']    #手动指定表头
   )
   ```

4. 最重要的数据类型是DataFrame，相当于Excel中的一个sheet，当数据量巨大时，Excel就hold不住了。也类似于数据库中的一条一条的记录。

5. DataFrame的dtypes属性，可以给出每一列的数据类型。

6. ![image-20201007212851391](Python科学计算应用基础.assets/image-20201007212851391.png)

7. ```python
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

8. Series相当于是在numpy数组基础上加了一个索引，索引不一定是数字，也可以是字符串等，类似于键值对。

9. dataframe是把多个列组合到一起，并为每一列添加了列名。

10. ![image-20201007223738443](Python科学计算应用基础.assets/image-20201007223738443.png)

11. ```python
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

12. dataframe，相当于是np的二维数组，不过加了两种索引，一种是行index，一种是列columns。这里的一个index对应一条记录，也就是一个一维数组。

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

13. 修改索引：

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

14. 也可以通过一个二维数组+行索引（可省略）+列索引（可省略）的方式来构建DataFrame：

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

15. 新增列：

    ```python
    df.assign(
        yWendu_huashi = lambda x : x["yWendu"] * 9 / 5 + 32,    #可以同时新增多个列，
        # 摄氏度转华氏度
        bWendu_huashi = lambda x : x["bWendu"] * 9 / 5 + 32
    )
    ```

16. Mapping和replace

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

17. 对于Series和DataFrame的操作：

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

18. 两个序列做运算，会找键相同的值进行运算，不是共有的键，则产生NaN。

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

19. 对于dataframe求和，也可以按照numpy的做法，来指定axis。

20. 协方差，相关系数：

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

21. 排序

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

22. Merge（两个dataframe要有公共的列才可以合并）

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

23. Concat（类似于numpy中的多维数组合并np.concatenate）和Combine(去重合并)

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

24. Apply操作，根据axis参数来逐行或逐列调用函数，构成一个series：

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

25. 去重和清洗：

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

26. 分箱（类似于Excel的筛选，为每一行增加一个新的列数据）和分组（）：

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

27. Excel操作，读取Excel2003的.xls文件需要xlrd库，读取Excel2007以后的.xlsx文件需要xlrd或openpyxl库：

28. ![image-20201009141656736](Python科学计算应用基础.assets/image-20201009141656736.png)

    

29. 默认返回第一个sheet的dataframe。如果参数是是none，那么字典的键是各个sheet的名字字符串。

30. ![image-20201009141731212](Python科学计算应用基础.assets/image-20201009141731212.png)

31. 对于没有表头的表格，需要设定header=none，如果有表头，则设置为0。

32. 默认情况下header=0，index_col=None。如果设置了header不为0，那么会跳过header上面的行。

33. ![image-20201009142701957](Python科学计算应用基础.assets/image-20201009142701957.png)

34. usecols参数可以只读取部分列，提高效率。切片包含左右边界值。下图中的AAA那一行为表头。str-list方法比较好，可读性好，也不怕列顺序变动。

35. ![image-20201009143401457](Python科学计算应用基础.assets/image-20201009143401457.png)

36. skiprows跳过行。一般如果要跳过列的话，可以用usecols来操作。

37. ![image-20201009144034860](Python科学计算应用基础.assets/image-20201009144034860.png)

38. 如果源文件没有标题行，则可以使用names来手动设置，记得设置header=None，也可以在读完之后，用dataframe.columns=来设置。

39. 可以通过dtype参数传入一个字典，来对每一列设置类型。

40. ![image-20201009144642905](Python科学计算应用基础.assets/image-20201009144642905.png)

41. 设置Series内储存数据的类型，object表示Series内的数据类型不唯一。下图中画框的类型是可以自动推导的。其余的要手动设置。也可以在dataframe的dtypes属性中查看类型。使用dataframe的astype()函数设置类型。

42. 当一列的数据只有几种情况时，可以设置为分类数据类型category。可以更快的索引，节约内存，还可以排序。

43. 设置dtype的目的是，不同的类型有不同的操作函数。所以一般都要有一个明确的类型，而不是object。

44. <img src="Python科学计算应用基础.assets/image-20201009144801373.png" alt="image-20201009144801373" style="zoom: 50%;" />

45. 选择对应的列为日期列，并解析它们。

46. ![image-20201009150223029](Python科学计算应用基础.assets/image-20201009150223029.png)

47. 下图左边的标准日期类型，不用设置日期解析器，右边的非标准的日期就需要手动设置。

48. ![image-20201009150310684](Python科学计算应用基础.assets/image-20201009150310684.png)

49. 在自动推导的时候，会参考Excel的列类型。可以通过多个分别表示时间的列（例如，年月日放在3个不同的列）合并成一个。

50. ![image-20201009152929202](Python科学计算应用基础.assets/image-20201009152929202.png)

51. data_parser接受一个函数，如下format参数可以解析2002年2月13日之类的日期。

52. ![image-20201009153646698](Python科学计算应用基础.assets/image-20201009153646698.png)

53. Pandas中常用NaN表示缺失值，是一个float类型。可以用na_values参数来指定那些内容被解析为NaN。可接受list，或字符串，数字等。默认全局的对应内容都会被解析为NaN，可以使用字典来直解析某些列中对应的内容为NaN（key是列名）。

54. ![image-20201009154410609](Python科学计算应用基础.assets/image-20201009154410609.png)

55. na_values = ['a',1]，这样所有内容为'a'或1的单元格会被解析为NaN。

56. 值转换函数，参数为一个字典，键为列明或索引，值为函数，可以对指定的列进行修改。可以用来对数据进行清洗，预处理。

57. ![image-20201009155038237](Python科学计算应用基础.assets/image-20201009155038237.png)

58. true_values false_values两个参数可以接受list，将对应的字符串转化为true或FALSE，只有某一列的内容全部可以转化时，才会转化该列。只对字符串有效。

59. ![image-20201009155450713](Python科学计算应用基础.assets/image-20201009155450713.png)

60. Excel中的列名可以重复，但是dataframe中不可以重复。

61. nrows参数可以指定要解析的行数（除了表头以外的）。

62. 使用dataframe.to_excel（）将对应的dataframe写入Excel文件。

63. <img src="Python科学计算应用基础.assets/image-20201009160627716.png" alt="image-20201009160627716" style="zoom: 67%;" />

64. 一般如果是默认的列索引，则可以不输出列索引。

65. ![image-20201009160801818](Python科学计算应用基础.assets/image-20201009160801818.png)

66. 在写入的时候，需要确保该文件当前没有被打开。

67. 实际使用的时候，index列也应该有一个名字，可以使用dataframe.index.name = 来设置。

68. ![image-20201009161227716](Python科学计算应用基础.assets/image-20201009161227716.png)

69. 使用ExcelWriter可以一次写入多个sheet，同时修改时间格式。用ExcelWriter打开一个文件，to_excel可以往该writer代表的文件中写入多次数据。

70. ![image-20201009162057738](Python科学计算应用基础.assets/image-20201009162057738.png)

71. 不过以上的所有的to_excel都会导致覆盖原有的所有数据，这时需要使用openpyxl引擎来操作Excel。例如：

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

72. 读写CSV文件。大部分参数和Excel是一样的。读写CSV文件需要特别注意编码。CSV文件在写入时，都要设置index=False，否则产生不是标准的CSV文件。

73. ![image-20201009195256960](Python科学计算应用基础.assets/image-20201009195256960.png)

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
13. 
14. 
19. 
20. 