# 基础

1. STL是泛型编程(使用模板来编写程序)最成功的作品。在早期的版本中，STL主要是使用模板，而很少使用面向对象。现在则不动，原来的一个类变成了多个类，层级变得更多了，不过虚函数使用也比较少。和面向对象鼓励将数据和算法都放到一个类里不同的是，STL的数据和算法是放在不同类里的，algorithm给出的算法都是全局函数，不过有些容器自己也有专门用来处理该容器数据的算法。

2. STL并不是C++标准库，标准库80%左右都是STL的内容。标准库以头文件的形式由编译器给出。

3. 在一个C++程序中可以使用的头文件有：

   1. C++标准库提供的，没有.h后缀名的文件，例如 #include \<vector\>
   2. 新式的C头文件，没有.h后缀名的文件，例如 #include \<cstdio\>，这种头文件实际上是下一种的封装，两者本质上一样。建议使用这种，而不是第三种。
   3. 旧式的C头文件，具有.h后缀名的文件，例如 #include \<stdio.h\>

4. 标准库的组件都封装在std的命名空间中，上面的2,3并没有。

5. 不同平台，不同编译器上标准库的用法对程序员来说都是完全一样的，底层实现可能不同。因为标准库也只是规定了接口，具体的实现由各家编译器自己负责。

6. 标准库对于库类型提供的操作做了详细规定，也对实现的性能做了要求，因此一般场合是足够的。

7. 参考资料：

   1. 网站：http://www.cplusplus.com/，https://en.cppreference.com/w/，https://gcc.gnu.org/。
   2. 书籍：《The C++ Standard Library》，《STL源码剖析》

8. STL主要分为6大部件：容器 container，分配器 allocator，算法 algorithm，迭代器 iterator，适配器 adaptor，仿函数 functor。

9. 每种容器都单独写成了一个头文件，分配器不用单独include头文件。

10. 分配器为容器提供底层支持，容器的第二个参数一般是分配器，不过一般都会使用默认的分配器。算法通过迭代器来操作容器中的数据，迭代器类似可以移动的指针。适配器允许做容器，迭代器，仿函数类型转化。

11. <img src="C++STL标准库和泛型编程.assets/image-20210820134201803.png" alt="image-20210820134201803" style="zoom: 67%;" />

12. 综合使用范例：

    ```c++
    #include <vector>
    #include <algorithm>
    #include <functional>
    #include <iostream>
    using namespace std;
    
    int main(){
        int ia[] = {27, 210, 12, 47, 109, 83};
        vector<int, alloctor<int>> vi(ia,ia+6);
        cout<< count_if(vi.begin(), vi.end(), not1(bind2nd(less<int>(), 40))) << endl; //count_if是算法，计算满足条件的元素的个数。vi.begin()会获得一个指向该vector头部元素的迭代器。less是一个仿函数，用于计算第一个参数是否<第二个。函数适配器bind2nd是将less的第二个参数固定为40。函数适配器not1会将条件反转。即≥40。因此最终结果为4。
        return 0;
    }
    ```

13. STL之所以提供了这么多容器，是因为不同的容器有其擅长的操作方式。例如链表的插入删除性能比数组快，数组的随机访问性能比链表强。

14. 标准库的所有容器都提供begin和end两个迭代器，begin指向第一个元素，end指向最后一个元素的下一个元素，前闭后开。因此*(vi.end())的行为是不确定的，因为vi.end()指向的已经不是容器内的元素了。

    ```c++
    vector<int, allocator<int>> vi(ia, ia + 6);
    vector<int, allocator<int>>::iterator ite;
    ite = vi.begin();
    
    for (;ite < vi.end(); ite++) {     //传统的for用分号分隔。
    cout << *ite <<endl;
    }
    //以上的遍历可以使用C++11提供的新的for还有auto关键字。
    for (auto& elem:vi){      //新的for用:分隔。
        cout<< elem <<endl;
    }
    ```

15. 容器只能放相同类型的东西，因为容器的每个节点大小都是一样的，如果是有一个父类派生出来的多个子类，容器可以用父类指针来存放子类对象。

# 容器

1. 容器大致上分为两类，序列式sequence 和关联式 associative。

2. 序列式容器有：
   1. Array，C++11的特性，是将原本的C风格的数组包装成了一个类。使用的时候需要指定空间大小，超过容易发生溢出。
   2. Vector，起点固定，空间不够的话， 容积自动增长，每次增长的都远大于1个空间，不同标准库的实现对于这里处理不同。
   3. Deque，双向队列，队列queue和栈stack是它的两个特例。
   4. List，双向环链表，
   5. Forward List，C++11的特性，每个节点只有后继指针，比list使用内存更小。
   
3. <img src="C++STL标准库和泛型编程.assets/image-20210821231047854.png" alt="image-20210821231047854" style="zoom:80%;" />

4. 关联式容器有，更适合大数据的查找：

   1. Set/MultiSet，内部使用红黑树实现。默认不允许重复，Multi版本允许出现重复的。
   2. Map/MultiMap，和上面的set几乎一样，不过每个节点是一个键值对。查找的时候以键为准，Multi版本允许键重复。
   3. Unordered Set，不定序容器，内部使用hashtable Separate Chaining实现。碰撞的内容放到一个篮子内的链表中，不过如果碰撞的次数太多，一个篮子的链表过长，也会分在不同的篮子里。
   4. Unordered Map，和上面Unordered Set几乎一样，不过每个节点是一个键值对。

5. <img src="C++STL标准库和泛型编程.assets/image-20210821231224676.png" alt="image-20210821231224676" style="zoom:80%;" />

6. Array的使用测试：

   ```c++
   #define ASIZE (1000000)
   #include <vector>
   #include <array>
   #include <algorithm>
   #include <functional>
   #include <iostream>
   using namespace std;
   
   #include <cstdlib> //qsort,bsearch函数。
   #include <ctime> //time,clock函数
   
   int  compareLongs(const void* a, const void* b) {  //qsort要使用到的比较函数。该函数将前后(有序)两个元素的指针传入，如果函数返回值>0，则交换两个元素的位置，反之保持默认位置。
   	return *(long *)a - *(long *)b;
   }
   
   int main() {
   	auto& c = *(new array<long, ASIZE>());  //必须要放到堆上，否则会发生栈溢出。
   	srand(time(NULL)); //设置随机数种子为当前时间。
   	clock_t timestart = clock();//开始计时。
   	try
   	{
   		for (long i = 0; i < ASIZE; i++) {
   			c[i] = rand();  //返回一个从0到RAND_MAX的随机数，RAND_MAX默认为32767。
   		}
   	}
   	catch (const std::exception& e)
   	{
   		cout << e.what() << endl;
   	}
   	cout << "插入数据花费 " << clock() - timestart << " ms" << endl; // 花费时间为81ms。
   	cout <<c.size() << endl;  //无论里边放了多少数据，都等于ASIZE。
   	cout << c.front() << endl; //获得第一个元素。也可以通过迭代器来获取元素，等价于*(c.begin())。
   	cout << c.back() << endl;  //获得最后一个元素。
   	cout << c.data() << endl; //获得数组对象的地址，相当于&c
       
       /*排序*/
   	long target = 23456;
   	timestart = clock();
   	qsort(c.data(), ASIZE, sizeof(long), compareLongs); //快速排序算法，C语言提供的函数。
   	cout << "排序花费 " << clock() - timestart << " ms" << endl;  //排序花费380ms
       
   	/*查找*/
   	timestart = clock();
   	long* pItem = (long*) bsearch(&target, c.data(), ASIZE, sizeof(long), compareLongs);//二分查找，只能用在已经排序过的数据上，这是C语言提供的函数。
   	cout << "查找花费 " << clock() - timestart << " ms" << endl; //查找花费0ms。
   	if (pItem == NULL) {
   		cout << "没找到" << endl;
   	}
   	else {
   		cout << "找到了,结果为" << *pItem << endl;
   	}
     	return 0;
   }
   ```

7. Vector使用测试：

   ```c++
   auto& c = *(new vector<string>);  //只用给出第一个模板参数即可，分配器使用默认的。
   srand(time(NULL)); //设置随机数种子为当前时间。
   char s[10];  //设置缓冲区，用于存放临时字符串。
   clock_t timestart = clock();
   try
   {
       for (long i = 0; i < ASIZE; i++) {
           snprintf(s, 10, "%d", rand());  //C语言函数，将格式化输出到字符串中。是sprintf的安全版本，第二个参数表示最多接受这么多字符(包括末尾的'\0')。
           c.push_back(string(s));  //返回一个从0到RAND_MAX的随机数，RAND_MAX默认为32767。
       }
   }
   catch (const std::exception& e)
   {
       cout << e.what() << endl;
   }
   cout << "插入数据花费 " << clock() - timestart << " ms" << endl;  //7700ms。
   cout <<c.size() << endl; //已经使用的空间，存放的元素个数。
   cout << c.front() << endl;
   cout << c.back() << endl;
   cout << c.data() << endl;
   cout << c.capacity() << endl; //容量，表示已经分配的空间可容纳的元素个数。
   ```

8. 在内存中连续存放的容器，如果要扩充，则是新开辟一块大的内存空间，然后把现在已有的数据拷贝过去。例如Array。

9. MSVC实现中Vector的capacity增长规律，不是2倍扩充规律，而是1.5倍。

10. ![image-20210822132229570](C++STL标准库和泛型编程.assets/image-20210822132229570.png)

11. 标准库主要使用了复合关系，例如set对象内部拥有一个rb_tree对象。在C++11中slist改名为forward_list。容器的大小和它内部存储元素种类和数量无关，因为都是通过指针管理的。例如vector\<string\>还有vector\<int\>的大小是一样的。但是不同实现下，大小不一定相同，GNUC 2.9中为12B，而MSVC2107中为16B。

12. <img src="C++STL标准库和泛型编程.assets/image-20210822234600786.png" alt="image-20210822234600786" style="zoom:67%;" />

# 泛型编程

## 模板

1. C++引入类模板，函数模板，用来创建变量类型不同，而操作相同的类和函数，这可以简化程序员的操作。JAVA等语言中称之为泛型。泛型（generic）程序设计是程序设计语言的一种风格，它允许强类型语言在编码时，使用一些实例化时才指定的类型。

2. 模板本身不是类或函数，它可以看作为编译器生成类或函数的一个说明。编译器根据模板创建类或函数的过程称为实例化。vector本身不是一个类，vector\<int\>才是，int是模板参数。

3. 通过模板生成类或者函数的过程是在编译期间完成的，因此使用到模板的库，需要提供源代码，不能只提供二进制库。

4. 有人说模板会造成代码的膨胀，实际上这些代码都是完成工作所必需的。从另一种角度来看模板降低了程序员开发的工作量，减少了出错的可能。

5. 使用模板时，要用<>指定待定的类型，这样编译器会自动生成一份代码，这样也可以减少手动书写出错的概率。使用模板会加大程序的体积，实际上这不是模板的缺点，因为本来不使用模板也要声明多份大同小异的类或者函数。

   ```c++
   /*//类模板的定义*/
   template<typename T>    //T称为模板参数，相同模板参数代表相同的类型。它只在类或函数模板的定义内生效。
   class complex{    //这里只是定义了一个类模板，并没有定义类。
   public:
       complex(T re, T im):re(re),im(im){...}
   	T real() const {return re;}
      	T imag() const {return im;}
   private:
       T re,im;
   };
   /*使用*/
   complex<double> c1(2.1, 5.2);
   complex<int> c2(2, 5);
   ```

6. 类模板和函数模板都是编译时才能确定待定的类型。区别是使用类模板创建对象时，需要显式指定类型。而使用函数模板时，编译器会自动进行==实参类型推导==，不用显式指定。

   ```c++
   /*函数模板定义*/
   template<class T>      //也可以使用typename关键字声明类型T。
   inline
   const T& min(const T& a,const T& b){
       return b < a ? b : a;   //需要对可能使用到min函数的T类型的<运算符进行重载，成员函数或者非成员函数都行。
   }
   /*使用*/
   stone s1(2,3),s2(3,4);
   min(s1,s2);      //调用该函数，会自动进行实参类型推导，根据上面的函数模板生成一个T为stone的函数，以上操作在编译期间完成。
   ```

7. 标准库中有很多类似于min，max之类的算法，都是用模板函数定义，内部转化成运算符。如果一个类要是用这种函数，只需要将对应的运算符重载即可。

8. 除了类模板和函数模板外，还有成员模板，成员模板就是类的成员函数使用模板进行定义。下面的拷贝构造函数就是一个成员模板。

   ```c++
   template <class T1, class T2 = int>  //模板参数的顺序不重要
   struct pair {           //GNU C中的有序对,两个类型可以不相同。
   	typedef T1 first_type;
   	typedef T2 second_type;
   	T1 first;
   	T2 second;
   	pair() :first(T1()), second(T2()) {}   //这里如果用new产生对象，就需要first(*(new T1()),然后还要析构函数中释放堆内存。不如现在这种方便。
   	pair(const T1& a, const T2& b) :first(a), second(b) {}
   template <class U1, class U2> //成员模板
       pair(const pair<U1,U2>& p): first(p.first), second(p.second) {}//需要注意的是，为了保证初始化列表能够顺利执行，需要满足p.first is-a first，即U1类型要继承自T1类型或者是同一类型。
   };
   ```

9. 模板本身是泛化的概念，与它相对的是特化Specialization，也称为模板参数的绑定。普通的模板来说，模板参数对于所有的类型都是一视同仁的。但是有些时候，希望对某些特定类型的模板参数进行单独处理，C++提供这样的精细化处理用于提高性能，例如：

   ```c++
   template<class key>  //定义一个完全泛化的类模板。
   struct hash {};
   
   template<>
   struct hash <char>{};  //定义一个完全特化的类模板，特化类型为char。
   
   template<>
   struct hash<int>{};
   /*使用*/
   struct hash<long> h1;  //会调用泛化模板。
   struct hash<int>  h2;  //会调用特化模板。
   ```

10. 特化的模板必须是在完全泛化的基础上进行的，否则特化模板不会被识别，类似于派生的关系。模板的特化是由编译器根据类型匹配原则进行选择的。

11. 偏特化Partial Specialization有两种：

   12. 数量上的偏特化，只对部分模板参数进行特化。

       ```c++
       template <class T1, class T2, class T3>  //全泛化的模板
       class vector {};
       
       template <class T11,class T33>   //将上面的全泛化模板的第一个参数进行特化。不同模板参数的偏特化，类型命名可以完全不同。
       class vector<T11, bool, T33> {}; //不同模板之间的参数顺序可以不同。
       /*使用*/
       vector<long, bool,int> v2;    //会使用偏特化的模板。
       ```

   13. 范围上的偏特化，

       ```c++
       template <class T>
       class C{};
       
       template <class T>  //数量上没有进行偏特化。
       class C<T*>{};     //范围上偏特化，这个特化只接受指针类型。
       
       /*使用*/
       C<int> c1;         //调用全泛化的模板
       C<int*> c2;        //调用偏特化的模板
       ```

14. 模板模板参数：模板参数本身也是一个模板，例如：

    ```c++
    template <class T, template<class T> class Container>   //第二个模板参数不是一个普通的类，而是模板类。两个模板参数之间有关联。
    class XCLs{
    private:
        Container<T> c;
    };
    
    /*错误用法*/
    XCLs<string, list> mylist2; //这里list是标准库中的容器，他有1个必须模板参数+多个默认模板参数，但是Container定义为只有1个模板参数，因此编译错误。
    
    /*使用*/ 
    template <class T>  //额外定义一个和Container匹配的list模板，算是模板的偏特化。
    using Lst = list<T, allocator<T>>;   //类似于typedef,不过是对模板的，C++11特性。
    XCLs<string, Lst> mylist1;  //纵观整体，有2个模板参数，T和Container，而Container又依赖于T。这里第一个参数确定了T的类型，第二个确定了Container的类型。
    ```

15. 以下代码不是模板模板参数，因为Sequence可以不是模板类，而是普通的关联模板参数：

    ```c++
    template <class T, class Sequence = std::deque<T> >  //模板参数可以有默认值，即默认的类型。
    class stack {
    private:
    	Sequence s;
    };
    /*使用*/
    stack<int> s1;  //使用默认模板参数，类型为  Sequence为std::deque<int,std::allocator<int>>
    stack<int, std::list<int>> s2; //第二个模板参数不可以是std::list,类型为stack<int,std::list<int,std::allocator<int> > >
    ```

16. 数量不定的模板参数 Variadic Templates，C++11的特性。允许模板的参数个数不固定，例如：

    ```c++
    void print() {}  //递归的平凡情况。
    
    template <class T, class... Ts>   //...，在此处用于定义模板参数。
    void print(const T& firstArg, const Ts&... args) {   //在此处用于定义函数参数类型。
    	cout << firstArg << "***" << sizeof...(args) << endl;  //输出第一个参数和args中参数的个数。
    	print(args...);  //递归调用，在此处用于定义函数参数。
    }
    
    /*使用*/
    print(2,"ss",5);  //第一次调用first为2，args是"ss"和5组成的包，第二次调用first为"ss",args为5组成的包。第三次调用first为5,args为空。第四次调用会根据类型匹配，转到最开始print()函数中。进而递归开始返回。
    ```

17. 三个点表示包pack，一个包可以容纳的数据是不确定的。可以使用sizeof...(args)