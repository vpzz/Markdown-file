# 基础

## Windows发展

1. Windows桌面版本更替：Windows1.0→95→98→ME→2000→XP→Vista→7→8→8.1→10。
2. Windows服务器版本更替：Windows server 2003→2008→2016。
3. Windows提供一致的用户界面，都有标题栏，菜单栏，状态栏等。
4. Windows提供了几千种API函数调用。提供设备无关性的编程，应用程序不直接访问硬件，Windows虚拟化了所有的硬件，只要有设备驱动程序，硬件就可以使用。应用程序不需要关心硬件的具体型号，而是面向驱动程序编程。
5. Windows提供内存分页和虚拟内存的管理，每个32位程序都拥有独立的4GB地址空间，64位系统支持的地址空间更大。
6. Windows API是构筑Windows框架的基石，它基于Windows内核，其上层是所有的Windows应用程序。
7. VS默认的构建是32位的Debug版本。

## 示例代码

1. 示例代码，会弹出如下消息框：

   ```c
   #include <Windows.h>
   int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow){
       MessageBox(NULL, TEXT("Hello, World!"), TEXT("Caption"), MB_OKCANCEL | MB_ICONINFORMATION | MB_DEFBUTTON2);
   }
   ```

2. ![image-20230314203053410](assets/image-20230314203053410.png)

3. Windows.h是Windows编程中最重要的头文件，主要包含了如下头文件：

   1. WinDef.h        基本数据类型类型
   2. WinBase.h      Kernel(内核有关定义)
   3. WinGdi.h        图形设备接口有关定义
   4. WinUser.h      用户界面有关定义

4. Windows程序的入口是WinMain函数，和main函数不同的是，该函数在WinBase.h中有声明。

   ```c
   int __stdcall WinMain (
       _In_ HINSTANCE hInstance,   //应用程序当前实例的句柄。
       _In_opt_ HINSTANCE hPrevInstance,  //应用程序的上一个实例的句柄
       _In_ LPSTR lpCmdLine,
       _In_ int nShowCmd
       );
   ```

## 调用约定和64位程序

1. __stdcall是调用约定，也成为标准调用约定。调用约定描述了函数参数的传递方式和由谁来平衡栈。
2. Win 32 API都使用标准调用约定。标准调用约定规定了参数从右到左，依次压入栈中，且由被调用者负责平衡栈。
3. Windows程序的栈是向小地址方向增长。
4. 由于函数内部也有局部变量，栈顶esp也会变化，因此函数内部使用相对于栈底ebp的偏移来使用参数和局部变量。所以在函数内部首先将ebp压入栈中（保存当前的ebp），然后将esp赋值给ebp，待到函数推出前，再将ebp从栈中弹出。
5. 平衡栈的操作就是将增加esp，增加的大小是函数的参数在栈中所占的字节数，恢复到调用函数前的值。
6. 另一个常见的调用约定是 __cdecl，C调用约定。他也是按照参数从右到左入栈，但是由调用方来负责平衡栈。
7. 64位CPU除了段寄存器，其余都是64位的。64位通用寄存器增加了8个，共有16个。其中8个为了兼容32位程序，将原来的E\*\*改为了R\*\*。其余8个命名为R8\~R15。EIP和EFLAGS也改为RIP和RFLAGS。浮点寄存器还是64位的，为MMX0\~MMX7。还增加了16个128位的多媒体寄存器XMM0\~XMM15，成为SSE指令。
8. RAX等8个通用寄存器的低32位，16位，8位都可以用EAX，AX，AL来表示。R8等寄存器的低32位，16位，8位都可以用R8D，R8W，R8B表示。
9. 64位程序的函数调用有所不同，64位程序最多可以通过寄存器传递4个参数，前4个参数从左到右依次存放在RCX，RDX，R8，R9中。从第5个参数开始使用栈传递。这样可以提高函数调用的速度。64位程序习惯用mov指令将参数传递到寄存器或栈中。不再使用EBP来引用参数和局部变量，直接使用RSP。由调用者负责堆栈平衡（和__cdecl一样）。使用x64Dbg调试64位程序。

## 参数批注

1. \_In\_是用来给程序员提示该参数是输入函数输出参数。有以下几种情况：
2. 出现在参数前\_\_In\_\_的是参数批注，一共有8种：
   1. \_\_In\_\_         输入参数，调用函数时要设置一个值，函数内部不可以修改该值。
   2. \_\_Inout\_\_    输入输出参数，调用函数时要设置一个值，函数内部会修改该值。
   3. \_\_Out\_\_      输出参数，函数内会给该参数赋值。
   4. \_\_Outptr\_\_ 输出参数，函数内会给该参数赋予一个指针的值。
3. 以上4种的每个还有一个对应的可选的批注，例如\_\_In\_opt\_\_。
4. VS2019前，编译器并不要求在函数声明和定义中设置参数批注。

## WinMain函数的参数

1. 第一个参数是HINSTANCE类型的变量，HINSTANCE是handle of instance，实例句柄。

2. ```c
   #define DECLARE_HANDLE(name) struct name##__{int unused;}; typedef struct name##__ *name
   ```

3. 将DECLARE_HANDLE(HINSTANCE)做宏展开后，得到如下代码：

   ```c
   struct HINSTANCE__{
       int unused;
   }
   typedef struct HINSTANCE__ *HINSTANCE;
   //上面的代码定义了一个结构体和该结构体的指针。因此HINSTANCE是一个结构体指针类型，指向的结构体中只有一个int数据unused。
   ```

4. 句柄就是其结构体中unused的值，程序使用句柄来标识对象，实例句柄揪唯一地标识了正在运行中的exe程序文件。在Win Main函数内hInstance不为0。

5. 模块代表一个运行中的exe和dll文件，表示这个文件的所有代码和资源。磁盘上的文件载入内存运行时叫做模块。当应用程序调用其他动态链接库中的函数时，这些dll文件也会载入内存，因此产生了dll模块。为了区分地址空间中的不同模块，使用模块句柄来标识。模块句柄实际上就是一个内存基地址，系统将exe和dll文件加载到地址空间的这个位置。

6. 实例是从Win16来的，Win16中运行的不同程序的地址空间并非完全隔离。一个可执行文件运行后形成模块，多次加载同一个可执行文件，这个模块是公用的，为了区分多次加载的复制，把每个复制成为实例。每个实例均使用不同的实例句柄来标识。但是在Win32中，每个运行的程序的地址空间都是隔离的，每个实例都有自己的4GB地址空间，不存在一个模块有多个实例的情况，因此在Win32中，实例句柄就是模块句柄。但是很多API函数还是使用实例句柄，而非模块句柄。

7. 第二个参数也是HINSTANCE类型的变量，标识应用程序的上一个实例的句柄，在Win16中，当同时运行者一个程序的多个副本时，这些实例间共享代码和只读数据，一个程序可以通过查看hPrevInstance得知是否存在该程序的其他实例也在运行，这样可以直接复制一些数据到自己这里。对于Win32程序，这个参数始终为NULL，即空指针。

8. 第三个参数是LPSTR类型，LPSTR是指向CHAR的指针，CHAR是char。因此LPSTR就是char*类型。该指针指向应用程序的命令行参数，，不包括可执行文件名。可以调用Get Command Line来获取完整的命令行参数。GUI中双击某个文件时，会调用对应的应用程序，并且将该文件名作为命令行参数传递给应用程序。

   ```c
   typedef _Null_terminated_ CHAR *NPSTR, *LPSTR, *PSTR  //_Null_terminated_表示是以\0(空字符)结尾的字符串。LP是Long Pointer长指针，是Win16遗留的概念，Win32中不区分长短指针，都是32位的。
   typedef char CHAR;
   ```

9. 第四个参数表示应用程序最初如何显示，例如在任务栏上正常显示，最大化到全屏显示或最小化显示。

## MessageBox函数

1. 该函数显示一个消息提示框，可以包含一个系统图标，一组按钮，一个标题和一个内容。

   ```c
   int WINAPI MessageBoxW(
       _In_opt_ HWND hWnd,
       _In_opt_ LPCWSTR lpText,
       _In_opt_ LPCWSTR lpCaption,
       _In_ UINT uType);
   ```


# 控制台输出调试信息

1. Win32 GUI程序默认没有控制台，因此printf，scanf之类的函数都被导向了空文件中，此时可以为程序分配一个控制台窗口，关联之后，即可使用对应的函数：

    ```c
    setlocale(LC_ALL, "chs");  //需要设置下，否则在控制台输出中文会有问题
    AllocConsole();  //分配控制台
    FILE* pfStdOut = nullptr;
    FILE* pfStdIn = nullptr;
    freopen_s(&pfStdOut, "CONOUT$", "w", stdout); //使用特殊文件名"CONOUT$"重新打开标准流
    freopen_s(&pfStdIn, "CONIN$", "r", stdin);
    _tprintf(TEXT("输出中文 No problem\n")); //会在对应的控制台窗口输出内容
    FreeConsole(); //将控制台从调用进程分离
    ```

2. 一个进程最多可以附加一个控制台，进程可以使用FreeConsole函数将其自身从其控制台分离。 如果其他进程共享控制台，则控制台不会被销毁，但是调用FreeConsole的进程不能引用它。 当连接到它的最后一个进程终止或调用FreeConsole时，控制台关闭。 在进程调用FreeConsole之后，它可以调用AllocConsole函数来创建一个新的控制台或AttachConsole来附加到另一个控制台。

3. 在使用完控制台程序之后一定要记得调用FreeConsole函数释放该控制台，否则会造成内存泄露。free前应该先fclose掉stdin和stdout两个流。