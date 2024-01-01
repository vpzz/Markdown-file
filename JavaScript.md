# 基础

1. ECMA-262规范定义了JavaScript，但是并没有唯一正确的实现。各种浏览器和JavaScript引擎都按照自己的理解实现了规范。

   ```
   浏览器                   JS实现方式
   FireFox                SpiderMonkey
   Internet Explorer     JScript/Chakra
   Safari                JavaScriptCore
   Chrome                     V8
   Carakan                  Carakan
   ```

2. 1995年，JavaScript问世，当时的主要用途是代替Perl等服务器端语言处理输入验证。在此之前，验证某个输入的值是否有效，都必须要和服务器进行通信。在那个网速缓慢的年代，非常有用。

3. Netscape 公司为自家的浏览器Netscape Navigator 2开发的脚本语言，一开始叫LiveScript，后来为了蹭Java的热度，改名叫JavaScript。

4. 微软也在IE的最初版本中包含了自己的JavaScript实现（叫JScript，为了避免和网景产生纠纷），即使它有自家的客户端语言VBScript。所以说是微软开启了JavaScript混乱的先河。

5. 网景后来将Navigator浏览器开源为Mozilla Project，后者后来推出了Firefox浏览器。

6. 1998年ISO/IEC将ECMA-262采纳为国际标准。

7. 浏览器对JavaScript的支持体现在对ECMAScript和DOM的实现程度。

8. 完整的JavaScript包含三部分：

   1. ECMAScript，也就是ECMA-262定义的语言，也称为核心JavaScript。

   2. DOM，文档对象模型

   3. BOM，浏览器对象模型


## ECMAScript

1. ECMAScript并没有输入输出之类的方法，Web浏览器和Node.js 是它常见的2个宿主环境。宿主环境提供对ECMAScript额外的扩展，扩展使用ECMAScript的核心类型和语法，提供特定于环境的扩展。

2. 如果不涉及浏览器，ECMA-262定义了如下内容：语法，类型，语句，关键字，保留字，操作符，全局对象。

3. 实现了ECMAScript的不只有JavaScript，Adobe的ActionScript也实现了。

4. ECMA-262最新的版本为第10版，ECMA-262的第1版和网景的JavaScript1.1相同，只不过删除了所有浏览器特定的代码，还做了少量更改。ECMA-262要求使用Unicode标准以支持多语言，而且对象要与平台无关，这也是网景的JavaScript1.1和1.2不符合ECMA-262第1版的原因。

5. ECMA-262的第三版是第一次对这个标准进行更新。这标志着ECMAScrip成为了一门真正的编程语言。

6. 所有浏览器对ES5都提供了完善的支持，


## DOM

1. DOM是一个API，用于在HTML中使用扩展的XML。DOM将整个页面抽象为一组分层的节点，HTML或XML页面的每个组成部分都是一种节点。DOM将HTML和XML文件解析为树型结构。开发者使用DOM API可以轻易地删除，替换，修改，添加节点。

2. W3C制定了DOM的标准。DOM并非只能通过JavaScript访问，已经很多语言都已经实现了。

3. DOM Level1 仅仅做了映射文档结构，由两个部分组成，DOM Core和DOM HTML。前者提供了一种映射XML文档的方法，后者增加了特定于HTML的对象和方法。

4. DOM Level2 增加了对鼠标，用户界面事件，范围，遍历的支持，且通过对象接口支持了CSS。

5. DOM Level3 增加了以统一的方式加载和保存文档，验证文档的方法，而且支持了XML1.0的所有特性，例如XPath。


## BOM

1. BOM用于支持访问和操作浏览器的窗口和子窗口(frame)。使用BOM，开发者可以操作浏览器显示界面以外的部分。BOM没有相关的标准。HTML5的出现改变了这个局面，以正式规范的形式涵盖了尽可能多的BOM特性。

2. 通常情况下，人们会把任何特定于浏览器的扩展都归于BOM的范围内。例如：
   1. 弹出新窗口

   2. 移动，关闭浏览器窗口

   3. navigator对象，提供关于浏览器的详细信息

   4. location对象，提供浏览器加载页面的详细信息

   5. screen对象，提供关于用户屏幕分辨率的详细信息。

   6. performance对象，提供浏览器内存占用，导航行为和时间统计的详细信息

   7. 对cookie的支持

   8. 其他自定义对象，例如XMLHttpRequest对象

3. 因为在很长时间内都没有标准，所以每个浏览器实现的都是自己的BOM。


# 浏览器中的JavaScript

1. 将JavaScript引入HTML中的主要方法是使用\<script\>标签，这个标签由网景创造出，后来被加入了HTML的规范。该标签有8个可选的属性。

   1. async，表示应该立即下载脚本，但是不能阻止其他页面动作，比如下载资源或等待其他脚本加载。只对外部脚本文件有效。

   2. src，外部js文件的地址

   3. defer，表示脚本可以延迟到文档完全被解析和显示之后再执行。只对外部脚本文件有效。

   4. type，用来代替language，表示代码块中脚本语言的内容类型，也成为MIME类型。这个值应该始终为"text/javascript"，尽管它已经被废弃了。JavaScript 文件的MIME类型通常是"application/x-javascript"。

   5. integrity，允许对比接受到的资源和指定的加密签名以验证资源的完整性。如果不匹配，则会报错，且不会执行改脚本。这个属性可以用于确保cdn不会提供恶意内容。

2. 使用\<script\>标签有两种方式：

   1. 直接在标签内书写JavaScript源代码，也称为行内JavaScript：

      ```html
      <script>
      function sayHi(){        //一个函数的定义，该定义会被保存在解释器环境中，后面可以调用。
          console.log("Hi");
      }
      </script>
      ```

   2. 引用外部的JavaScript文件，也称为外部JavaScript，外部的js文件扩展名不一定非得为.js，如果不是.js扩展名，应该确保使用了正确的MIME类型：

      ```html
      <script src="example.js"></script>
      ```

3. 通常推荐使用外部JavaScript，有以下优点：

   1. 可维护性，外部文件容易将JavaScript脚本集中起来。

   2. 缓存，浏览器会根据特定的设置缓存所有外部链接的JavaScript文件，如果两个页面都是用到同一个文件，则只用下载一次。

   3. 适应未来，外部JavaScript不用考虑用XHTML或适配的黑科技。不受HTML和XHTML语法严格程度的不同的影响。

4. 在使用行内JavaScript时，代码中不能出现\</script\>，也就是script标签的结束标记。可以用\转义/即可：

   ```html
   <script>
   function sayHi(){
       console.log("<\/script>");    //在/前面加个\即可
   }
   </script>
   ```

5. 执行行内JavaScript和下载并执行外部JavaScript时，都会阻塞页面。

6. 在XHTML中可以忽略结束标签，但是在HTML中不行。

7. 外部js的优先级高于行内js：

   ```html
   <script src="example.js">    //仅下载并执行外部js,行内js会被忽略。
   function sayHi(){
       console.log("Hi");
   }
   </script>
   ```

8. \</script\>标签包含来自外部域的js文件，和\<img\>标签一样，其src属性可以包含一个完整的URL，而且整个URL指向的资源可以和包含它的HTML文件不在同一个域中。浏览器在解析外部js文件时，会向src路径发送一个GET请求，以取得相应的资源。这个初始的请求不受浏览器同源策略的限制。但是返回并执行的JavaScript则受限制。这个请求仍然受父页面HTTP/HTTPS协议的限制。

9. 引用放在别人的服务器上的JavaScript文件必须要小心，因为可能会被恶意篡改。\</script\>标签的integrity属性能够保证这一点。

10. 默认情况下，浏览器按照\</script\>标签在页面中的出现顺序来解释他们，使用async和defer属性的除外。不同\</script\>标签的代码是顺序执行的，后一个必须等前一个解释完才可以解释。

11. 过去，\</script\>标签都被放在\<head\>标签内，这么做的目的是为了把外部的JavaScript和CSS文件都集中到一起，方便管理。

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Example HTML Page</title>
            <script src="example1.js"></script>
            <script src="example2.js"></script>
        </head>
        <body>
        <!-- 这里是页面内容 -->
        </body>
    </html>
    ```

12. 不过把所有的JavaScript文件都放在head中，就意味着，必须把所有的JavaScript文件下载并解释完后，才能开始渲染页面。页面在浏览器解析到body标签时才开始渲染。对于包含很多JavaScript的页面，这回导致明显的延迟，这期间，页面会完全空白。因此，现在通常将\</script\>标签放在body标签内，页面内容的后面，这样显示空白的时间就变短了，用户会感觉页面加载更快了。

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Example HTML Page</title>
        </head>
        <body>
        <!-- 这里是页面内容 -->
            <script src="example1.js"></script>
            <script src="example2.js"></script>
        </body>
    </html>
    ```

13. HTML4.1为\<script\>标签定义了一个defer的属性，这个属性表示，脚本会被延迟到整个页面都解析完毕后（即解析完结束的\</html\>标签）再运行。立即下载，延迟执行。HTML5规范要求，延迟的脚本也要按照先后顺序执行，都会在DOMContentLoad事件之前执行。不过在实际中，并非总是按顺序或者在该事件前执行。

14. 对defer属性的支持比较早，例如IE4就开始了，但是HTML5要求，defer属性仅对外部脚本有效。而IE8才正式支持HTML5。

15. 对于XHTML 文档，指定defer 属性时应该写成defer="defer"。

16. HTML5为\<script\>标签定义了async属性，它和defer的功能类似，不同的是，async脚本不能保证按照顺序执行。异步脚本保证会在load事件前执行，可能会在DOMContentLoad事件前后执行。使用异步脚本，应该保证其内不会修改DOM。好的web开发实践不推荐使用整个方法。

17. 除了使用\<script\>标签，还可以在JavaScript中使用DOM API来动态加载脚本。默认情况下，以下面这种方式加载脚本是异步的，相当于添加了async属性。不过这样做可能会有问题，因为所有浏览器都支持createElement()方法，但不是所有浏览器都支持async属性。因此要统一脚本加载行为，应该将其明确为同步加载。

    ```javascript
    let script = document.createElement('script');
    script.src = 'gibberish.js';
    script.async = false;      //将此脚本设为同步加载
    document.head.appendChild(script);  //在这一步之前并不会发送GET请求。
    ```

18. 动态加载js对于浏览器的预加载器是不可见的，这会严重影响它们在资源获取队列中的优先级。可能会严重影响性能。可以在文档头部显式声明，让预加载器知道这些文件动态请求的存在。

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Example HTML Page</title>
            <link rel="preload" href="gibberish.js">
        </head>
        <body>
        </body>
    </html>
    ```

19. XHTML是将HTML作为XML的应用重新包装的结果，与HTML不同，XHTML中的JavaScript必须type属性，且值必须为text/javascript。在HTML中，这个属性是可选的。XHTML已经退出了历史舞台。

20. XHTML的语法比HTML严格，这会影响行内JavaScript代码。例如下面的代码在HTML中有效，但是在XHTML中无效：

    ```html
    <script type="text/javascript">
    function compare(a, b) {
        if (a < b) {    //在XHTML中 < 会被解释为一个标签的开头。而作为标签开头的<后面有不能有空格，因此会报错。
        	console.log("A is less than B");
        } else if (a > b) {
        	console.log("A is greater than B");
        } else {
        	console.log("A is equal to B");
        }
    }
    </script>
    ```

21. 避免上述语法错误有2个方法：

    1. 把所有的<都改为对应的HTML实体形式 &lt ，缺点是会影响阅读。

    2. 将所有的代码包含在一个CDATA块中，在XML中一个CDATA块表示文档中可以包含任意文本的区块，其内容不会作为标签来解析，里边可以包含任意字符。![CDATA[  块内容  ]]

       ```html
       <script type="text/javascript">
       //<![CDATA[
           function compare(a, b) {
           if (a < b) {
           console.log("A is less than B");
           } else if (a > b) {
           console.log("A is greater than B");
           } else {
           console.log("A is equal to B");
           }
           }
       //]]>
       </script>
       ```

22. 在兼容XHTML的浏览器中可以使用CDATA块来解决问题，但是在不支持CDATA块的非XHTML浏览器中则不行。为此，必须CDATA必须作为JavaScript的注释存在。这种格式适用于所有现代的浏览器。

23. XHTML 模式会在页面的MIME 类型被指定为"application/xhtml+xml"时触发。

24. \<noscript\>标签的出现是用于给不支持或禁用了JavaScript的浏览器显示替代内容。该标签可以包含任何可以出现在body中的元素，script除外。例如：

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Example HTML Page</title>
            <script defer="defer" src="example1.js"></script>
        </head>
        <body>
            <noscript>   <!-- 当且仅当浏览器不支持或禁用了JavaScript时，此标签中的内容才会被渲染。  -->
                <p>This page requires a JavaScript-enabled browser.</p>
            </noscript>
        </body>
    </html>
    ```


# 语言基础

1. ECMAScript 的语法很大程度上借鉴了C 语言和其他类C 语言。

2. ECMAScript 严格区分大小写。每条语句以；结尾，如果不写；浏览器会自动添加，消耗性能。加分号也便于开发者通过删除空行来压缩代码。

3. 标识符只能以字母 _ 和$开头。按照惯例ECMAScript标识符推荐使用驼峰命名法。

4. 注释采用C语言风格：

   ```javascript
   /*多行注释
   *
   *  中间的*不是必须的，只是为了美观。
   */
   
   //  单行注释
   ```

5. ECMAScript 5 增加了严格模式（strict mode）的概念，ECMAScript 3 的一些不规范写法在这种模式下会被处理，对于不安全的活动将抛出错误。

   ```javascript
   "use strict";       //这是一个预处理指令，用来控制JavaScript引擎的。对整个脚本启用严格模式，一般放在脚本的开头。
   
   function doSomething() {
   "use strict";          //仅对该函数启用严格模式，
   // 函数体
   }
   ```

6. 控制语句只在执行多条语句时要求必须有代码块。但是推荐任何时候都用{ }包裹起来其子语句。

   ```javascript
   // 有效，但容易导致错误，应该避免
   if (test)
   	console.log(test);
   // 推荐
   if (test) {
   	console.log(test);
   }
   ```

7. ECMAScript 是松散类型的，变量可以保存任何类型的数据，三个关键词可以用于声明变量：var，const，let。其中，var 在ECMAScript 的所有版本中都可以使用，而const 和let 只能在ECMAScript 6 及更晚的版本中使用。


## var

1. 使用var定义变量，变量是没有类型的，可以保存任意类型的值：

   ```javascript
   var message;   //定义了一个变量，可以用它保存任何类型的值。不初始化的情况下，变量会有一个特殊值，undefined。
   var message = "hi";  //定义并初始化。可以随时改变变量的值或类型。
   message = 100; // 合法，但不推荐
   
   var message = "hi", found = false, age = 29;  //同时定义3个变量
   ```

2. 如果使用var 操作符在函数内定义变量，则它会成为函数的局部变量。在函数内定义变量时如果省略var，可以创建一个全局变量。但是不推荐这么做，因为在局部作用域中定义全局变量很难维护。在严格模式下如果省略var，则会被解释器认为是给一个已声明的变量赋值，如果变量未声明过，则会抛出ReferenceError。

   ```javascript
   function test() {
       var message1 = "hi"; // 局部变量
       message2 = "hello";  // 全局变量
   }
   test();  //调用它会创建这个变量并给它赋值，调用之后变量随即被销毁。
   console.log(message1); // 出错！
   console.log(message2); // 正确
   ```

3. 在严格模式下，不能定义名为eval 和arguments 的变量，否则会导致语法错误。

4. var会将使用它定义的变量自动提升到函数作用域的顶部：

   ```javascript
   function foo() {
       console.log(age);
       var age = 26;
   }
   foo();  //不会报错，但是也不会输出26，因为只是把定义提前了，初始化的部分并没有提前。
   //等价于下面的代码
   function foo() {
       var age;
       console.log(age);  //输出 "undefined"
       age = 26;
   }
   foo();
   ```

5. 在全局作用域中使用var定义变量时，JavaScript引擎会将所有由var定义的变量和初始化都移动到全局作用域的顶部，保持原有的顺序。

   ```javascript
   console.log(name);  //会输出 'Matt'
   var name = 'Nicholas';
   console.log(name);  //输出 'Nicholas'
   if (true) {
       var name = 'Matt';
       console.log(name); //会输出 'Matt'
   }
   //等价于
   var name = 'Nicholas';
   var name = 'Matt';
   console.log(name);  //会输出 'Matt'
   var name = 'Nicholas';
   console.log(name);  //输出 'Nicholas'
   if (true) {
       var name = 'Matt';
       console.log(name); //会输出 'Matt'
   }
   //如果在函数作用域内时，JavaScript引擎仅将定义提升到了函数作用于的开头。
   function func1(){
       console.log(name);  //会输出 "undefined"
       var name = 'Nicholas';
       console.log(name);  //输出 'Nicholas'
       if (true) {
           var name = 'Matt';
           console.log(name); //会输出 'Matt'
   	}
   }
   func1();
   ```

6. 反复用var声明多个变量也没有问题：

   ```javascript
   function foo() {
       console.log(age);  // "undefined"
       var age = 16;
       console.log(age);  //16
       var age = 26;
       console.log(age);  //26
       var age = 36;
       console.log(age);  //36
   }
   foo();
   //等价于如下代码：
   function foo() {
       var age;
       console.log(age);  // "undefined"
       age = 16;
       console.log(age);  //16
       age = 26;
       console.log(age);  //26
       age = 36;
       console.log(age);  //36
   }
   foo();
   ```


## let

1. let是ES6新定义的关键字。let和var最明显的区别就是，let定义的范围是块作用域，var定义的范围是ha函数作用域。

   ```javascript
   if (true) {
       var name = 'Matt';
       let age = 26;
       console.log(name); // Matt
       console.log(age); // 26
   }
   console.log(name); // Matt
   console.log(age); // ReferenceError: age 没有定义
   ```

2. 但是let不允许在同一个块作用域内出现冗余声明：

   ```javascript
   {
       let age;
       let age; // 语法错误；标识符age 已经声明过了
   }
   ```

3. JavaScript 引擎会记录用于变量声明的标识符及其所在的块作用域。因此嵌套使用相同的标识符不会出错，因为它们不在同一个块中。var和let都可以嵌套定义变量。

   ```javascript
   //var和var
   var name = 'Nicholas';
   if (true) {
       var name = 'Matt';  //相当于对上面声明的name重新赋值，因为var允许重复声明，因此不会报错。
       console.log(name); //结果为  'Matt'
   }
   console.log(name);  //结果为 'Matt'，因为原来的name已经在if里边被修改了。
   //let和let
   let name = 'Nicholas';
   if (true) {
       let name = 'Matt';  //会在当前块中暂时隐藏掉之前的同名的name定义，这里不算重复定义，因此不会报错。
       console.log(name); //结果为  'Matt'
   }
   console.log(name);  //结果为 'Nicholas'
   //let和var
   let name = 'Nicholas';
   if (true) {
       var name = 'Matt';  //错误，因为这里的name是那个用let声明的name。而let不允许重复。
       console.log(name);
   }
   //var和let
   var name = 'Nicholas';
   if (true) {
       let name = 'Matt';  //不会报错，
       console.log(name); // 'Matt'
   }
   console.log(name);  //结果为 'Nicholas'
   ```

4. 使用var和let声明的变量不能彼此重复

   ```javascript
   var name;
   let name; // SyntaxError
   
   let age;
   var age; // SyntaxError
   ```

5. var和let的另一个重要区别是let不会将变量声明提升到块作用域的开头。在let声明执行前的时段称为暂时性死区。

   ```javascript
   // name 会被提升
   console.log(name); // 会输出 'Matt'
   var name = 'Matt';
   
   // age 不会被提升
   console.log(age); // 错误，ReferenceError：age 没有定义
   let age = 26;
   ```

6. 使用let在全局作用域内定义的变量不会成为window对象的属性，而var则会：

   ```javascript
   var name = 'Matt';
   console.log(window.name); // 'Matt'
   
   let age = 26;
   console.log(window.age); // "undefined"
   ```

7. 在let出现前，for循环中定义的循环变量会渗透到循环外。

   ```javascript
   for (var i = 0; i < 5; ++i) {
   	// 循环逻辑
   }
   console.log(i); // 5
   //let则不会出现这种问题。
   for (let i = 0; i < 5; ++i) {
   // 循环逻辑
   }
   console.log(i); // ReferenceError: i 没有定义
   ```

8. 使用var定义迭代变量时，会出现如下奇怪的情况：

   ```javascript
   //for循环会快速循环多次，每次设置1个定时器，然后结束循环。等500ms到达后，多个定时器间隔很近，依次触发。定时器到的时候，会触发指定的函数，环境是当时定义定时器的。
   //这里使用了ES6定义的箭头函数，括号内是参数，{}内为函数体。setTimeout是设置定时器，第一个参数是到时要执行的函数，第二个为延迟的ms数。
   for (let i = 0; i < 5; ++i) {
   	setTimeout(() => {console.log(i)}, 500);
       i=i+2;  //修改的是唯一的那个i。
   }
   //输出为 2 5。JavaScript引擎会在每次循环中为let定义的变量创建一个新的副本，并用用上一轮结束时的值来初始化这个副本，每个setTimeout引用的都是不同的变量实例。因此第一次创建定时器时的i，仅在同一次循环内的i=i+2被修改，第二次循环的i=i+2修改的则是第二次循环的i。第一次进入循环时i=0，退出时i=2，第二次进入循环时i=3，退出时i=5，然后循环结束。
   //使用var则会造成问题。
   for (var i = 0; i < 5; ++i) {
   	setTimeout(() => {console.log(i)}, 500)
       i=i+2;  //此时修改了本次循环的i变量副本。
   }
   //输出为 6 6。因为最后一次进入循环是4，而退出循环时为6。
   //一般来说，这个问题在普通循环中是不会发生的，let定义的循环，在新一轮的循环中会用上一轮结束时的循环变量来初始化新一个轮的变量副本。而上一轮的变量如果没有其他代码使用，则会被垃圾回收器回收。而在这里定时器锚定了循环中的变量副本，使得let和var的行为不同。
   ```

9. 上面的在每次迭代中都会生成一个独立变量的实例的行为适用于所有风格的for循环。


## const

1. const的行为与let基本相同，唯一一个区别是用它定义变量时，必须同时初始化，而且尝试修改const变量时，会产生运行时错误。const变量也不允许重复定义。

   ```javascript
   const age = 26;
   age = 36; // TypeError: 给常量赋值
   const name = 'Matt';
   const name = 'Nicholas'; // 错误
   const name = 'Matt';
   if (true) {
   	const name = 'Nicholas'; //也是块作用域
   }
   console.log(name); // 结果为 "Matt"
   ```

2. 如果const 变量引用的是一个对象，那么修改这个对象内部的属性并不违反const 的限制。

   ```javascript
   const person = {};
   person.name = 'Matt'; // ok
   person = 32;  //错误
   ```


## 使用推荐

1. 通过上面可以发现，var和let混用非常麻烦，而且var本身的行为也和其他编程语言不同，建议以后只用let。let的行为是和其他编程语言完全相同的，都是块作用域，且不能重复声明。

2. 优先使用const，然后才是let。这样可以让静态代码分析工具提前发现不合理的赋值行为。


# 数据类型

1. ECMAScript有6种简单数据类型，Undefined、Null、Boolean、Number、String 和Symbol。Symbol是ES6新增的。还有一种复杂数据类型，Object 对象。对象是一种无序键值对的集合。在ECMAScript6中不能定义自己的类型。

2. typeof操作符可以用来确定变量的类型：

   ```javascript
   typeof xx;  //也可以用括号将xx包裹起来。
   //可能会返回如下7个字符串之一：
   "undefined"  //表示值未定义；
   "boolean"    //表示值为布尔值；
   "string"     //表示值为字符串；
   "number"     //表示值为数值；
   "object"     //表示值为对象（而不是函数）或null(空对象指针)；
   "function"   //表示值为函数；
   "symbol"     //表示值为符号。
   ```

3. 严格来讲，函数在ECMAScript 中被认为是对象，并不代表一种数据类型。可是，函数也有自己特殊的属性。为此，就有必要通过typeof 操作符来区分函数和其他对象。


## Undefined

1. Undefined 类型只有一个值，就是字面值undefined。对于使用var或let定义了，但是没有初始化的变量，都会默认初始化为undefined。

   ```javascript
   let message;
   console.log(message == undefined); // true  而不是 "undefined"
   ```

2. 不推荐显式将变量初始化为undefined，因为字面值undefined在ES3之前是不存在的，增加它的目的就是为了正式明确null和未初始化变量的区别。

3. 定义了但未显式初始化的变量和未定义的变量是不同的，后者只能执行一个动作，就是typeof，结果为 "undefined"。前者执行typeof时，也会返回"undefined"。虽然对未声明的变量调用delete 也不会报错，但这个操作没什么用，实际上在严格模式下会抛出错误。


## Null

1. Null类型也只有一个值，就是null。null表示一个空对象指针，因此typeof null会得到 "object"。如果某个变量要用来保存对象，建议使用null来初始化。这样以后只要检查该变量是否是null，就可以知道后续的赋值有没有成功：

   ```javascript
   let car = null;
   null == undefined;  //undefined 值是由null 值派生而来的，因此ECMAScript认为它们是相等的。
   if (null){       //null和undefined作为条件都是false
       //不会执行这里
   }
   ```


## Boolean

1. Boolean类型有两个字面值true和false。True和False不是布尔类型的值。所有其他ECMAScript类型的值都有相应布尔类型的等价值。可以显式调用Boolean()函数来获取对应的值。

   ```javascript
   //以下结果都为false
   Boolean("")
   Boolean(0)
   Boolean(NaN)
   Boolean(null);  
   Boolean(undefined); 
   ```


## Number

1. Number使用IEEE754来保存整数和浮点数，整数可以用8和16进制表示出来。

   ```javascript
   let octalNum = 070;  //结果为56，8进制在严格模式下是无效的。
   let hexaNum = 0x1a;  //结果为26，16进制必须以0x开头，大写的无效。16进制的字母大小写均可。
   ```

2. 要定义浮点值，数值中必须包含小数点，而且小数点后面必须至少有一个数字。因为存储浮点值使用的内存空间是存储整数值的两倍，所以当小数点后没有数字或只有0时，会被转化为整数。浮点值的精确度最高可达17 位小数。

   ```javascript
   let floatNum1 = 1.1;
   let floatNum2 = 0.1;
   let floatNum3 = .1;
   let floatNum1 = 1.; // 小数点后面没有数字，当成整数1处理
   let floatNum2 = 10.0; // 会被当成10处理
   let floatNum = 3.125e7; //科学计数法计数  等于31250000
   ```

3. ECMAScript能表示的数值范围存储在以下中，如果在某个计算得到的数值超过了可以表示的范围，会被自动转换为Infinity（Number类型的一个字面量）。使用Number.NEGATIVE_INFINITY 和Number.POSITIVE_INFINITY 也可以获取正、负Infinity。

   ```javascript
   Number.MIN_VALUE  //在大多数浏览器中为 5e-324
   Number.MAX_VALUE  //在大多数浏览器中为 1.7976931348623157e+308
   Number.MIN_VALUE/2 //超出范围的小的数会被认为是0。
   Number.MAX_VALUE*2 //超出范围的正数会被认为是Infinity
   -Number.MAX_VALUE*2 //超出范围的负数会被认为是-Infinity
   
   isFinite(Number.MAX_VALUE*2); //判断参数是否是有限值，结果为 false。
   isFinite(2);   //结果为 true。
   ```

4. NaN是一个特殊的字面值，意思是 Not a number。如果一个函数本来要返回数值，但是出现了错误，可以返回NaN，而不是抛出错误。0，+0，-0三个数之间相互作除法，结果是NaN。非零数除以±0，结果为±Infinity。

   ```javascript
   0/0  0/+0  0/-0  +0/0  -0/+0 ;   //这些都是NaN
   2/+0;  // Infinity
   2/-0;  // -Infinity
   2/0;   // Infinity
   ```

5. 任何涉及NaN的操作结果都是NaN，NaN不等于的任何值，包括它自己。可以使用isNaN()函数来判断参数是否可以转化为数值。如果参数是一个对象时，会调用对象的valueOf()方法，然后判断返回值能否转化为数值。如果不能，再调用toString()方法，测试返回值。

   ```javascript
   NaN+3;  //结果为NaN
   NaN == NaN;  //false
   
   isNaN(NaN);  //true
   isNaN("10"); //false，可以转化为10
   isNaN("blue"); //true，不能转化为数值
   isNaN(true);  //false，可以转化为1
   isNaN(false); //false，可以转化为0
   ```

6. 有三个函数可以将非数值转化为数值：

   ```javascript
   Number();  //适用于任何类型。true→1，false→0，null→0，undefined→NaN。
   //对于字符串有如下规则："12"→12，"012"→12，"1.12"→1.12，"0x2f"→47，""→0，除了上面的例子外，结果都是NaN,例如"blue"会转化为NaN。
   //对于对象，会调用valueOf()方法，然后按照上述规则转化。如果转化结果是NaN,则调用toString()方法，再按照字符串来转化。
   parseInt(); //将字符串转化为整数。如果第一个非空格字符不是数值字符，正负号，则返回NaN。因此空字符串也会返回NaN。直到字符串结尾或者遇到非数值字符，小数点也是非数值字符。"   124"→124，" s4"→NaN，"123bl"→123，""→NaN，"22.23"→22，"0x2f"→47，"012"→12。
   //不同的数值格式容易混淆，因此parseInt也接受第二个参数，用来指定进制。
   parseInt("10",2);  //二进制
   parseInt("10",8);  //八进制
   parseInt("10",10); //十进制
   parseInt("10",16); //十六进制
   parseFloat(); //将字符串转化为浮点数，第二个小数点之后的内容无效。"123"→123，"22.5"→22.5， "22.5.2"→22.5，".35"→0.35。只能解释10进制小数。
   ```

## String

1. String类型表示0或多个16位Unicode字符序列。可以用三种引号括起来，彼此没有区别，但是不能混搭。

   ```javascript
   let firstName = "John";
   let lastName = 'Jacob';
   let lastName = `Jingleheimerschmidt`
   ```
   
2. 可以将js代码编写到按钮的onclick中，或者超链接中。

   ```html
   <button onclick = "alert('点我干嘛');">点我一下</button>
   <a href = "javascript:alert('又点我');">你也点一下</a>
   
   有时候希望超链接不起作用，可以写成如下方式    javascript:;
   ```

27. 书写在.js文件中，然后在HTML中引入该文件，类似于css，写在外部可以利用浏览器的缓存机制：

    ```html
    <Script type="text/javascript" src = "js/test.js">此时内部的js代码会被浏览器忽略</Script>
    ```

29. ```js
    document.write("向浏览器的页面写入内容");
    Console.log("向控制台输出内容");
    document.write(1+"\n")         // 这样并不会换行，需要使用HTML的换行
    document.write(1+"<br />") 
    ```

30. 字符串可以用单引号或双引号都行，方便嵌套使用。也可以使用\转义引号。

36. Number.MAX_VALUE     JS中数值的最大值，以常量保存。如果数值超过了改值，则结果会变为Infinity，表示正无穷，-Infinity表示负无穷。Infinity就是个字面量，也是number类型，不是字符串。

37. ```js
    var a = "abc" * "bcd";
    console.log(a);    //结果输出为NaN not a number。类型也是number
    ```

38. js对浮点数的计算不是精确地，整数的是精确地，除非超出边界。

39. ```js
    var a = 0.1 + 0.2;
    console.log(a);  //输出为0.30000000000004
    ```

40. null类型的值只有一个，就是null。用来表示一个为空的对象。

    ```js
    var a = null;
    typeof null;       //结果为object
    ```

41. Undefined类型的值只有一个，就是undefined，表示声明了没有赋值的变量。

    ```js
    var b;
    console.log(b);        //未定义值
    typeof b;       //结果为undefined
    ```

42. 强制类型转化，一般是将其他类型的值转化为number，string，boolean。

43. 其他类型转化为字符串：

    1. 调用被转换类型的toString()方法，可以的到该类型的变量转化后的字符串，不会影响原先的变量。null和undefined没有toString()方法，只能用String()函数。
    2. 调用String()函数。

44. 一般需要在特定的类型中重写toString()方法。

45. 其他类型转化为数字：

    1. 调用Number()函数。对于纯数字的字符串，可以正常使用。以外的都返回 NaN。空字符串和空白字符串都会转化为0。null转为0，undefined转为NaN。

    2. 使用parseInt()，parseFloat()函数，专门为字符串准备，将字符串中有效数字内容取出来。如果对非字符串使用，则会先将其转化为字符串，再操作。

       ```js
       parstInt("123px")        //结果为123。
       parstInt("123px223")     //结果为123。
       parstInt("bx123px223")   //结果为NaN。
       parstInt("123.52px223")  //结果为123，忽略小数点。
       parstFloat("123.52px223")  //结果为123.52，忽略小数点。
       ```

46. 数值以0x开头表示16进制，0开头表示8进制，0b开头表示2进制。2进制不是所有的都支持。

47. parseInt()的第二个参数，表示进制，可选。

48. 其他类型转为boolean类型：只有一种方法，使用Boolean()。

49. 0，NaN，null，undefined和空字符串会转为false。     空白字符串，"false"，对象都会转为true。

50. 算数运算符会对运算数进行强制类型转化，再运算。

51. 任何值和NaN做算数运算还是NaN。

52. +不仅仅是算数运算符，还可以用来连接两个字符串。任何值和字符串做拼接，都会强制转化为字符串（隐式）。

53. js支持自增和自减运算。a++或++a。都会让a自增，但是这两个表达式的值不同，a++的值等于自增前的。

54. 逻辑运算符 &&    ||      !    与或非。

55. JS的逻辑运算都是短路的，如果通过第一个操作数就可以判断逻辑值，则不会计算第二个操作数的值。因此通常会使用如下逻辑：

    1. 操作A&&操作B。 这个表达式，表示如果A执行成功，再执行B，如果A失败，则不执行B。

56. 赋值运算符      +=   -=   *=   /=   %=

57. 9%4为9除以4的余数，结果为1。

58. 对于比较运算符，如果两端都是字符串，会进行逐个字符的对比，Unicode编码。

59. 输出Unicode字符：

    ```js
    console.log("\u2620")      //16进制2620是Unicode对骷髅符号的编码。
    ```

    ```html
    <h1>&#9760;</h1>           //十进制9760，对应16进制2620，输出的和上面的相同。
    ```

    ![1613920612796](JavaScript.assets/1613920612796.png)

60. 相等运算符，左右操作数的类型不同，则会进行隐式类型转换，然后再比较。因此  "1" == 1的结果为true。

61. undefined衍生自null，所以null == undefined 结果为true。

62. NaN不和任何值相等，包括NaN。因此无法通过 == NaN来判定变量是否为NaN，因此JS提供了isNaN函数来判断。isNaN（NaN）返回true。

63. ！= 表示不等运算符。

64. 全等运算 =\=\= ，不会做类型转化，如果两个变量的类型不同，则直接返回false。

    ```js
    "123" === 123      //false
    null === undefined  //false
    ```

65. 不全等为！\=\=，可以用！和全等运算替换。

66. 条件运算符，三元，        条件表达式？语句1：语句2。对条件表达式求值，如果为真，则执行语句1，并返回结果，否则执行语句2，并返回结果。

67. 逗号运算符，一般在声明多个变量时使用：

    ```
    var a,b,c;
    ```

68. 运算符的优先级：

69. ![1613926279007](JavaScript.assets/1613926279007.png)

70. 在JS中可以为语句进行分组，使用{}将其包裹，称为一个代码块。代码块只是格式上的分割，不具备变量使用范围的效果（和其他语言不同）。

# 流程控制

1. IF语句

   ```js
   if (条件表达式) {
   	语句
   }
   
   if (条件表达式) {
   
   } else {
   
   }
   
   if (条件表达式) {
   
   } else if {
   
   } else {
   
   }
   ```

2. 条件分支语句，switch。 依次判断条件表达式 =\=\= 表达式1，2，3，4。进入case后，直到遇到break，才会退出switch语句。

   ```javascript
   switch(条件表达式){
   	case 表达式1:
   		语句;
   		breal;
   	case 表达式2:
   		语句;
   		breal;
   	case 表达式3:
   		语句;
   		breal;
   	default:
   		语句;
   		breal;
   }
   ```

3. while循环：

   ```js
   while(条件表达式){
   	break;    //可以跳出循环
   }
   do {
            
   } while (条件表达式)      //先执行在判断。
   ```

4. for 循环：

   ```js
   for (初始化表达式;条件表达式;更新表达式){
   }
   for (var i = 0 ; i<10 ; i++){
   }
   ```

5. break用来退出最近的一层循环语句，不能用于if。

6. 如果要终止用break来终止外层循环，可以为外层循环设置标签，例如：

   ```js
   outer:
   for (;;){
       for (;;){
           break outer;      //终止标签为outer的循环。
       }
   }
   ```

7. continue用来跳过本次循环，开始执行下次循环，不执行本次循环后续的代码。也支持标签。

# 面向对象

1. 常见的对象类型：

   1. 内建对象，由ES标准中定义的，无论是浏览器还会node.js，例如math，string等。
   2. 宿主对象，由JS运行环境提供的，目前主要是浏览器中的，BOM，DOM。 例如console，document。
   3. 自定义对象，由开发人员自己创建的。

2. 使用new关键字调用的函数，为构造函数，创建对象。

3. ```js
   var obj = new Object();
   obj.name = "hha";           //第一次调用表示，为obj对象添加一个属性，
   console.log(obj.age);       //获取为定义的属性，则会返回undefined。
   delete obj.name;            //删除对象的属性。
   ```

4. 对象的属性名不强制要求遵循标识符的规范吗，不过不建议这样。

5. 也可以使用[]来操作对象的属性，使用[]操作更灵活，属性名可以用字符串拼接：

   ```js
   obj["属性名"] = 20;
   vconsole.log(obj.属性名)         //无法获取。
   console.log(obj["属性名"])       //需要通过相同的方式获取。可以认为是两类不同的属性。
   ```

6. 对象在浏览器中的显示为：

   ```js
   Object {name = "hah",age = 20}              //类名+键值对。
   ```

7. in运算符，检查一个对象中是否含有指定的属性。

   ```js
   "属性名" in obj      //返回true或false。
   ```

8. 基本数据类型和引用类型的主要区别就是赋值时的操作不同。默认是浅拷贝。

   ```js
   var a = 3;
   var b = a;        //此后a和b完全没有关系，他们的值分别存储在不同的内存空间中。
   var c = new Object();
   var d = c;        //c和d都指向同一块内存空间，修改c的属性，d也会看到。
   ```

9. 变量都保存在栈中，基本数据类型的值直接存在栈中，对象的内容保存在堆内存中，栈中保存的是堆内存的地址。

10. 基本数据类型在比较时，比较的是值，引用数据类型在比较时，比较的是内存地址。

11. 使用对象字面量来创建对象：

    ```js
    var obj = {};       //等价于 new Object()
    //可以在创建对象时，直接制定属性和值。类似于JSON数据。
    var obj = {name:"hha", age:20, gender:"男"}
    //下面这种写法更清晰
    var obj = {
        name:"hha",
        age:20,
        gender:"男"
    }
    ```

12. 属性名可以加引号，也可以不加引号。

13. 函数也是对象：

    ```js
    var fun = new Function();       //可以将要封装的代码以字符串的形式传递给构造函数。
    var fun = new Function("console.log('函数')");
    ```

14. 封装到函数中的代码并不会立即执行。使用函数对象()来调用。

15. 函数对象具有所有普通对象的功能，可以为其设置属性。

16. 实际使用中，很少使用构造函数来创建函数。一般使用函数声明来创建函数，两种方法结果相同。

    ```js
    function 函数名([形参1,形参2,形参3]){    //[]表示可选
    	//具体的代码实现。
    }
    ```

17. 也可以使用函数表达式来创建函数：

    ```js
    var func = function([形参1,形参2,形参3]){
    };
    ```
    
18. 上面等号右边为匿名函数，可以在创建的时候调用，直接在后面加()。定义匿名函数的时候需要在整个函数的定义外边加上括号，否则不会识别，如果时赋值给变量，则不用加括号。

19. 函数的形参就相当于在函数内声明了一个变量，但是并不赋值，当函数被调用的时候，可以用实参给形参赋值。

20. 调用函数时，解析器不会检查实参的类型，也不会检查实参的数量。多或者少传递参数，不会报错。

21. 使用return 来设置返回值。空的return或者不写return，相当于return undefined。

22. 当函数的参数多了以后，顺序可能会乱，可以将实参和形参都缩减为一个对象。

23. 函数对象也可以作为参数，也可以将匿名函数写在另一个函数调用的地方。开发中经常用这种方法设置回调函数。

    ```js
    func(function func2(){
    })
    ```
    
24. JavaScript 函数有个内置的对象 arguments 。argument 对象包含了函数调用的参数数组。可以方便地进行参数的使用。

25. 在函数的声明内部也可以声明函数。

26. 匿名函数可以用来创建一个立即执行的函数，只用一次。

    ```js
    (function(){
    })();             //函数定义完毕后，立即调用，也可以在后面的括号中传入参数。1
    ```
    
27. 当一个函数称为对象的属性时，称之为对象的方法。

28. for in，可以枚举出对象内的属性和方法：

    ```js
    for (var n in obj){  //每次循环，n都被赋值为obj的属性名称。可以用obj[n]来调用。
    	console.log(obj[n]);
    }
    //上面不能使用obj.n来调用。
    ```

29. 作用于分为全局和函数作用域两种。

30. 全局作用域，直接编写在script标签内的代码，都在全局作用域中。在页面打开时创建，关闭时销毁。window 全局对象就表示浏览器的窗口，内建。在全局作用于中创建的变量都会作为全局对象window的属性存在。

    ```js
    var a = 3;
    console.log(window.a)       //会输出3。
    
    //对于没有定义的全局变量，直接使用会报错，而当做window的属性来使用则为undefined。
    console.log(b)          //报错，提示 not defined
    console.log(window.b)   //不会报错，输出undefined
    ```

31. 全局作用于中的变量都是全局变量，在页面的任意部分都可以访问到。

32. 使用var关键字声明的变量会在所有的代码执行之前被声明（但是不会赋值）：

    ```js
    console.log(a);       //不会报错，会输出undefined。
    var a = 123;
    
    //上面的代码相当于如下：
    var a;
    console.log(a);
    a = 123;
    ```

33. 使用函数声明来创建的函数，也会和用var生命的变量一样，被提前，而使用函数表达式创建的函数则不会。

    ```js
    fun1();        //由于声明的提前，可以在此处正常调用fun1。
    function fun1(){
    }
    fun2();       //会报错。
    var fun2 = function(){
    };
    ```
    
34. 函数作用域，在调用函数时创建，函数执行完毕时销毁。每次调用都会创建一个新的，独立。

35. 在函数作用域可以访问到全局变量。反之，不行。

36. 函数变量优先于局部变量。重复生命的变量不会覆盖掉之前的。

    ```js
    var a = 10;
    function fun(){
    	var a = "hah";           //不会覆盖掉之前的
    	console.log(a);          //输出 hah 。
        console.log(window.a);   //访问的是全局的变量a，输出10。
    }
    
    console.log(a);             //输出 10。
    ```

37. 在函数作用域中，也有声明提前的特性。

38. 在函数中，不适用var声明的变量都当做全局变量。

39. 在每次的函数调用时，解析器都会额外传递一个隐含参数，this。this指向函数执行的上下文对象，随着函数调用方式的不同，this指向不同的对象。

40. ```js
    function fun(){
    	console.log(this);
    }
    var obj = {callFun:fun}
    
    fun();		     //输出window对象
    obj.callFun();    //输出obj对象
    ```

41. 以函数的形式调用时，this为window；以方法的形式调用时，this为调用的对象。

42. 全局作用域中的this表示window对象。

43. 使用工厂方法(使用的Object的构造函数)创建大量对象，避免重复书写代码。

    ```js
    function createObj(name, age, gender){
    	return {
            name:name,       //第一个name是属性，默认当做字符串处理，也可以写成"name"。
            age:age,
            gender:gender
        }
    }
    ```

44. 构造函数和普通函数的创建方式没有区别，不同的是构造函数习惯于首字母大写，还有调用方式的不同，构造函数要用new关键字调用。

    ```js
    function Person(){
    }
    var per1 = Person();      //per1为undefined，因为该函数没有返回值。
    var per2 = new Person();  //per2为object，因为使用了new。
    ```
    
45. 构造函数的执行流程：

    1. 调用时立刻创建一个对象
    2. 将新建对象设置为构造函数函数中的this，因此可以在构造函数中使用this来引用要创建的对象。
    3. 执行构造函数中的代码
    4. 将新建的对象作为返回值返回（不用写return）。

46. ```js
    function Person(name){
    	this.name = name;
    }
    var per = new Person();      //此时per是Person类型的，而不是Object。
    console.log(per instanceof Person);     //结果为true。
    ```

47. 使用同一个构造函数创建的对象，是一类对象，因此也将构造函数称为一个类。使用该构造函数创建的对象称为该类的一个实例。

48. 使用instanceof 关键字来判断一个对象是否是某一个类的实例。任何对象都是Object的实例，因为所有的类都是继承自Object。

49. 定义在对象中的方法如果以this.func(){}来书写，则对于每创建一个对象，都会创建一个新的函数方法。这样是没有必要的。实际上只要给整个类书写一个方法就行了。可以用以下解决办法：

    ```js
    function Person(name){
    	this.name = name;
    	this.sayName = function sayName(){
        };
    }
    //修改为如下，但是这样会把类的内部方法暴露出来，也会污染全局作用域的命名空间，容易造成命名冲突。
    function sayName(){
    }
    function Person(name){
    	this.name = name;
        this.sayName = sayName;  
    }
    ```
    
50. 我们所创建的每一个函数，解析器都会向函数中添加一个属性，prototype。每个函数的prototype都不同。

51. prototype就是所谓的原型对象。

    1. 如果函数作为普通函数调用，prototype没有任何作用。
    2. 如果函数当做构造函数调用时，创建的所有对象中，都有一个属性prototype，指向该构造函数的prototype。可以通过对象.\_\_proto\_\_来访问。

52. ```js
    function Person(){
    }
    var mc = new Person();
    console.log(mc.__proto__ == Person.prototype);  //结果为true。
    ```
    
53. 原型对象相当于类的一个公共区域，所有该类的实例都共享该对象。可以将对象中共有的内容设置到prototype中。

54. ```js
    function Person(){
    }
    Person.prototype.a = 123;
    var mc = new Person();
    console.log(mc.a);        //结果输出为123.
    ```
    
55. 当访问对象的属性或者方法时，会现在对象自身中寻找，如果找的到，就地返回。如果找不到，则会去对象的原型对象中寻找，即mc.\_\_proto\_\_.a。

56. ```js
    function Person(){
    }
    Person.prototype.sayName = function (){
    };
    var mc = new Person();
    console.log("sayName" in mc);                //in检查会考虑，也会返回true。
    console.log(mc.hasOwnProperty("sayName") );  //返回false。该函数检查对象自身是否有该属性。
    ```
    
57. 以后，可以在书写类的构造函数时，将所有对象共有的属性和方法添加到类的原型对象中。

58. 原型对象也有原型对象。直到找到object对象，因为该对象没有原型对象，但是也有个\_\_proto\_\_属性，值为null。

    ```js
    function Person(){
    }
    var mc = new Person();
    mc.__proto__.__proto__.hasOwnProperty("hasOwnProperty");   //返回true。可以看到hasOwnProperty方法是mc的爷爷中的，也就是Object对象的。
    console.log(mc.__proto__.__proto__.__proto__);   //结果为null。
    ```
    
59. 从上面可以看出，用户自定义的类，一般都是Object类的孙子。

60. 当使用console.log打印对象时，实际上是调用该对象的toString()，将该函数的返回值打印。

61. toString()也在该对象的爷爷object中，可以为该类添加一个共有的toString方法，即给该类的父亲添加一个方法。

    ```javascript
    Person.prototype.toString(){
    }
    ```
    
62. 由此可以看出，用户自定义类没有直接继承自object，而是中间还有一个中介的原因。该中介用来存放用户自定义类的共有属性和方法。 如果没有该中介，则定义用户自定义类的共有属性时就会修改到object类，进而会影响到所有的类。

63. 垃圾回收 garbage collection。

    ```javascript
    var obj = new Object();
    obj = null;
    ```

64. 当一个对象没有被任何变量引用时，就永远无法再操作该对象。这种对象就是垃圾，过多会占用大量内存空间。JS解析会自动进行垃圾回收，销毁垃圾对象。用户能做的就是讲所有指向该对象的引用赋值为null。这样垃圾回收器会适时回收。

# 数组

1. 数组也是一个对象，不同的是，普通对象使用字符串来作为属性名，数组使用数字来操作元素。

2. 索引从0开始。数组的存储性能比普通对象好。

3. ```js
   var arr = new Array();
   console.log(arr);             //返回空
   console.log(typeof arr);      //返回object。
   ```

4. 数组操作元素使用[ ]。

5. ```js
   arr.__proto__.hasOwnProperty("toString")   //可以看到Array类重写了object的toString方法，因此console.log(arr)会输出数组中元素的内容。
   ```

6. 读取未赋值的数组元素，不会报错，会显示undefined。

7. 数组的常用属性和方法：

   ```js
   var arr = new Array();
   arr.length;      //获取数组的长度，对于非连续数组，结果不是数组中的元素的个数，返回的是已经使用的最大小标+1。
   arr[arr.length] = 20;      //向arr数组的末尾添加一个元素。
   arr.push(2,"hha");         //像数组末尾添加多个元素，返回新的的数组的长度。
   arr.pop();                 //删除最后一个元素，并将之返回。
   arr.shift();               //删除数组开头的元素，并将之返回。
   arr.unshift("hah",23);     //向数组的开头添加多个元素。
   arr.slice(2,5);            //切片，将arr[2]到arr[4]提取成一个新的数组。左闭右开。第二个参数可以省略不写，此时会截取其后的所有元素。
   arr.splice(2,5,"hah","ss");           //删除原数组中对应的区间的元素(第一个参数是开始位置，第二个为数量)，返回该区间。第三个及后续参数都将会插入到第一个参数的位置之后。
   arr.concat(arr1,arr2,"hah");          //将arr,arr1,arr2和"hah"拼接为一个新的数组，不会修改原数组。
   arr.join();                //返回一个由该数组元素构造的字符串。默认的连接符为,  也可以制定一个字符。
   arr.reverse();             //将原数组逆序。
   arr.sort();                //按照元素对应字符串的Unicode编码从小到大对原数组排序。
   arr.sort(1,2,3,4,11);     //结果为1,11,2,3,4。
   //可以自己制定排序的规则，给sort传递一个排序函数。
   arr.sort(function(a,b){
   //会调用很多次，每次传入的两个元素总是一个在左,一个在右,如果返回值>0,则交换两个元素。如果<=0,则不交换。
       return ;
   })
   ```

8. js的数组永远不会越界。length 属性可以被修改，通过这样可以删除(真实删除)部分末尾元素。

9. 使用数组字面量来创建数组：

   ```js
   var arr = [];                      //空的数组
   var arr1 = [1,2,"hha"];            //创建的同时赋值
   var arr2 = new Array(1,2,"hha");   //使用构造函数创建数组时，也可以添加元素。
   ```

10. 不过存在以下不同：

    ```js
    var arr = [10];                 //创建一个数组，只有一个元素，为10。
    var arr1 = new Array(10);       //创建一个长度为10的数组，即arr1.length = 10
    ```

11. 数组的元素可以是任何类型。数组也可以嵌套，构成高维数组。

12. 数组的遍历：

    ```js
    var arr = [123,22,"ssd"];
    for (var i = 0;i<arr.length;i++){
        console.log(arr[i]);
    }
    //也可以使用for each来遍历数组,不过该方法对于IE8及以下的不支持。
    //参数为一个函数对象。可以使用匿名函数。
    arr.forEach(function(a, b, c){
        console.log(a)
    });
    ```

    

13. 数组中有几个元素，就执行几次。每次会传入如下三个参数，

    1. 对应该次循环的元素
    2. 该次循环元素的下标
    3. 正在遍历的数组

14. 数组的索引可以是负值，索引-1表示索引0的左侧，即最后一个元素。

# 函数对象

1. 函数对象的两个方法，call()和apply()，调用时，都会运行函数本身。不过这样调用时第一个参数，会被当做this传递到函数内部。：

   ```js
   function fun(){
   	console.log(this)
   }
   var obj = new Object();
   fun();                //这里的this时window对象。
   fun.call(obj);        //这里的this是obj对象，即第一个参数。
   fun.apply(obj);       //同上
   //call和apply的区别是apply对于后续的实参，需要封装到一个数组中。
   fun.call(obj,1,2);
   fun.apply(obj,[1,2]);
   ```

2. 调用函数时，除了this，还会传入隐含的arguments参数，封装了所有的实参：

   ```js
   function fun(){               
       console.log(arguments.length);        //类数组对象，也可以通过索引操作元素。
       console.log(arguments.callee == fun); //结果为true。
   }
   func(12,3);          //输出2。
   ```

3. 因此即使不定义形参，也可以使用实参。

4. arguments还有一个属性，callee，指向当前正在执行的函数对象。

# 内建对象

1. Date对象

2. ```js
   var d = new Date();    //默认为当前代码执行的时间。
   console.log(d);        //Wed Feb 24 2021 00:32:23 GMT+0800 (中国标准时间)
   var d1 = new Date("12/03/2016 11:20:15")  //接受一个字符串，创建指定日期的时间对象。
   // 格式为      月/日/年 时:分:秒
   ```

3. Math对象，他不是构造函数，而是一个工具类，里边封装了各种数学运算的相关属性和方法。使用Math不用创建对象，直接调用就即可。

   ```js
   var m = new Math();          //不能这样用
   Math.PI;         //常量π
   Math.abs(-2);    //结果为2.
   Math.ceil(1.5);  //结果为2,向上取整。
   Math.floor(1.5); //结果为1,向下取整。
   Math.round(1.4); //四舍五入为整数。
   Math.random();   //获得0-1之间的随机数。不包括0和1。
   ```

4. 常量属性一般用大写表示。

5. 如果想要获得一个0-10之间的随机数，且能取到0或10，可用如下代码：

   ```js
   Math.round(Math.random()*10);
   ```

# 包装类

1. JS提供了三个包装类，可以将三个基本类型数据转化为对象。String，Number，Boolean。这样就可以使用面向对象的特性了。

   ```js
   var n = new Number(3);
   var s = new String("hah");
   var b = new Boolean(true);
   ```

3. 实际开发中，基本不会使用基本数据类型的包装类，他们的存在是为了JS解析器自己使用。因为在做一些比较时，结果不可预期。

4. ```js
   var b = new Boolean(false);
   if (b){        //由于b是对象，因此将其转化为bool值，始终为true。
   }
   ```
   
5. 方法和属性只能添加给对象，不能添加给基本数据类型。但是基本数据类型可以使用包装类的属性和方法。

   ```js
   var a = "hah";
   var s = a.toString();          //JS解析器会临时将a转化为对象。调用完成后又将转回基本数据类型。
   a.hello = "sdd";
   console.log(a.hello);        //结果为undefined，因为上一步并没有给变量a赋予属性，因此此步会把a转化为String，然后寻找hello属性，找不到则返回undefined。
   ```

6. 在底层，字符串是以字符数组的形式保存，因此也可以用[ ]来索引，可以使用数组的函数。

   ```js
   var s = "asd";
   var sa = ["a","s","d"];
   ```

# DOM和BOM

1. DOM Document Object Model，文档对象模型，JS通过DOM来对HTML页面进行解析，因此可以操作网页中的元素。   文档→对象。

2. ![1614100614015](JavaScript.assets/1614100614015.png)

3. html文件和\<html\>标签是两个不同的对象。href是对象a的属性。

4. HTML标签，文本，注释，属性，整个文档，都是节点Node。常见的有4类：

   1. 文档节点，整个HTML文档。
   2. 元素节点，HTML文档中的各种标签。
   3. 属性节点，元素的属性。
   4. 文本节点，标签内的文本内容。

5. 节点的属性：

6. <img src="JavaScript.assets/1614100841255.png" alt="1614100841255" style="zoom:67%;" />

7. 浏览器提供了现成的对象document，文档节点，用于使用DOM树。它是一个全局变量，window对象的属性。代表整个HTML网页。

8. ```html
   <button id="btn">我是一个按钮</button>
   <script>
   	var btn = document.getElementById("btn");
       btn.innerHTML = "修改后的按钮";
   </script>
   ```

9. 事件，对于所有元素的操作都是事件。可以编写代码对事件做出响应。用户和浏览器的交互行为都依赖于事件。

10. 修改标签对象的事件处理函数，可以在HTML标签中直接修改，也可以在JS代码中获取对象，进行修改。

    ```html
    <button id="btn" onclick = "alert('点我干嘛')">我是一个按钮</button>
    ```

    ```js
    document.getElementById("btn").onclick = function (){
    };
    ```
    
11. 第一种方法不推荐使用，一般来说，HTML标签的属性只包含一些class，id，name就好了。

12. 浏览器加载页面时是按照自上而下的顺序，如果在head中写的JS程序想要获取body中的标签，则会获取到null。也可以将JS程序放在开头，不过设置在页面加载完毕后执行即可。

13. 页面的加载完毕后，也会触发一个事件。也可以为一个图片设置加载完成事件相应函数。

14. ```js
    window.onload = function(){
    };
    ```
    
15. 追求性能的话，可以将js代码写到后面。为了方便管理使用，可以写到前面。

16. 通过document对象，获取元素节点。

    ```javascript
    getElementById()         //通过id属性来获取一个元素节点对象
    getElementsByTagName()   //通过标签名获取一组元素节点对象
    getElementsByName()      //通过name属性获取一组元素节点对象
    ```

17. 元素的ID是唯一的。即使根据TagName或Name查询到的对象只有一个，也会封装到数组中。

19. innerHTML是用来获取标签内部的HTML代码，这个对于自结束标签没用。innerText相当于将获取到的HTML标签去除。

    ```html
    <input type="radio" name="gender" value="male"/>
    ```

20. 元素的id，type，value等属性都可以使用.来获取，但是class属性不可以，因为class时js的关键字，需要使用className来读取。

21. jQuery就是用来简化DOM查询的。

22. 通过具体元素来获取其他元素，这个getElementsByTagName和document的函数不同的是，他只在对应的元素以下查询。

23. ![1614104527485](JavaScript.assets/1614104527485.png)

24. childNodes，firstChild，并非只获得元素节点，标签间的文本也会被当做文本节点（IE8及以下不会考虑空白文本节点）。children，firstElementChild只返回子元素节点，例如：

    ```html
    <ul id="city">
        <li id="bj">北京</li>
        <li>上海</li>
        <li>东京</li>
        <li>首尔</li>
    </ul>
    
    <script type="text/javascript">
        document.getElementById("city").childNodes;   //获取到9个子节点，4个li节点，还有5个换行造成的文本节点。
        document.getElementById("city").children;     //获取到4个节点。
    </script>
    ```

25. 

26. ![1614139918001](JavaScript.assets/1614139918001.png)

27. 父节点肯定是元素，因为文本没有子节点。但是兄弟节点可能是标签间的文本。而previousElementSibling之类的就可以忽略标签之间的空白文本不过IE8及以下不支持。

28. 如果是用在移动端的网页，则不用考虑兼容IE8。

29. 如下代码，要从获取标签内的北京这个字符串，如下三种方法可以：

    ```html
    <li id="bj">北京</li>
    <script>
    	document.getElementById("bj").innerHTML;
        document.getElementById("bj").innerText;
        document.getElementById("bj").firstChild.nodeValue;      //复杂，不建议使用。
    </script>
    ```

30. 在事件的响应函数中，this指的是绑定事件的元素。

31. document中保存着对一些顶级标签的引用。

    ```js
    document.body;            //<body>
    document.head;            //<head>
    document.documentElement; //<html>根标签。
    document.all;             //页面中所有的元素，一般为html,head,meta,title,script ,body等元素，不分层级。等价于document.getElementsByTagName("*");
    ```

32. JS支持通过CSS选择器来选择元素：

    ```js
    document.querySelector(".box1 div");      //在类名为box1的元素中查找div标签。该方法只能返回第一个匹配的元素
    document.querySelectorAll(".box1 div");    //在所有的box1类中查找所有的div元素，返回一个数组。
    ```

33. DOM的增删改操作

33. ![1614145305734](JavaScript.assets/1614145305734.png)

# 事件

1. 事件就是浏览器或文档中发生的一些特定的瞬间。

2. 事件流描述的是从页面中接受事件的顺序。网页上的元素存在多层的嵌套关系，点击任何一个元素，这个点击事件不仅仅发生在对应的元素上，而且也会影响到它的父节点。

3. 对于事件的传播顺序有两种方案：

   1. IE方案，冒泡流，从小元素到大元素，最后到document。
   2. Netscape，捕获流，从大元素到小元素，最后是具体点击的元素。

4. ```js
   document.getElementByID("box");      //从上到下，依次变大。
   document.body;
   dcument.documentElement;
   document;
   window;
   ```

5. 可以使用元素的addEventListener()，为元素设定对应事件的回调函数，以及时在捕获阶段还是在冒泡阶段接受事件。一个事件可以同时为捕获和冒泡阶段都编写处理函数。

6. ```js
   document.getElementByID("box").addEventListener("click",function(){
       //设置捕获阶段的处理函数
   },true);
   document.getElementByID("box").addEventListener("click",function(){
       //设置冒泡阶段的处理函数
   },false);
   ```

8. 事件所处的阶段：捕获阶段→目标阶段→冒泡阶段。这是DOM二级事件规定的事件流。

9. ![1614180274294](JavaScript.assets/1614180274294.png)

10. 事件处理程序：

    1. HTML的时间处理程序，写在HTML标签的属性中。在该处理程序中，this指的就是对应的标签，可以使用使用标签的属性名来使用对应的属性。缺点是HTML和JS耦合在一起了。

       ```html
       <button onclick="function(){this;}"></button>   <-->这里的this指的是button对象。</-->
       <-->第二种方法</-->
       <button onclick="fun1()"></button>
       <script>
       	function fun1(){
               console.log(this);           //单击按钮，输出的是window对象。
           }
       </script>
       ```

    2. DOM0级时间处理程序，即讲一个函数赋值给事件的处理程序的属性。不能给同一个元素的同一个事件绑定多个处理程序，因为会覆盖。这种事件的处理程序只能在事件的冒泡阶段处理。使用简单方便，最多，兼容性最好。

       ```js
       document.getElementByID("box").onclick = function(){};
       document.getElementByID("box").onclick = null;   //忽略改事件，不处理。
       ```

    3. DOM2级事件处理程序，可以为一个元素的一个事件绑定多个处理程序，可以设置在捕获还是冒泡阶段处理。IE8不支持DOM2级事件处理程序。

       ```js
       document.getElementByID("box").addEventListener("click",function(){
           //设置捕获阶段的处理函数
       },true);    //第一个参数为事件名，第二个为处理程序的函数。第三个参数默认为false,表示在冒泡阶段处理事件。
       document.getElementByID("box").removeEventListener();//参数同上，为了方便之后移除，还是不使用匿名函数。
       ```

    4. IE事件处理程序，只能在冒泡阶段处理，只有IE支持。

       ```js
       document.getElementByID("box").attachEvent("onclick",function(){});//参数含义同DOM2。
       ```

11. HTML级别的处理程序都会被DOM0覆盖掉。对于非IE<9的浏览器，DOM0→DOM2。对于IE8及以下，DOM0→IE。

12. 在事件处理程序中，this指的就是事件的目标对象。在事件触发，调用处理程序时，会将事件对象作为第一个参数传入。事件对象中封装了很多有用的信息。

    ```js
    document.getElementByID("box").onclick = function (e){
        console.log(e);        //输出事件对象。
        console.log(event);    //也可以直接使用event对象。
    }
    ```

13. event对象中的属性：

    1. currentTarget属性指向事件当前所在的节点，正在执行的监听函数所绑定的节点。随着事件对象的流动，而改变。
    2. target属性指向事件的实际目标对象。在整个事件流中是不会变化的。

14. 例子如下，当用户点击li标签时，box的事件处理程序执行时e.currentTarget为，，：

    ```html
    <ul id="box">
        <li id="list1"></li>
        <li id="list2"></li>
    </ul>
    <script>
    	document.getElementById("box").onclick = function(e){
            console.log(e);
            console.log(e.currentTarget);
            console.log(e.Target);
            console.log(this);
        };
    </script>
    ```

# 浏览器内核

1. 内核有很多模块组成：
2. ![1614005511889](JavaScript.assets/1614005511889.png)
3. 需要根据HTML代码和CSS代码来在内存中生成对应的对象树，然后方便后续的操作。
4. node.js是一个机遇chrome v8引擎的js运行环境，可以让js脱离浏览器运行在服务端。能够做到和php等语言相同的功能。
5. V8引擎本身使用了一些最新的编译技术。这使得用Javascript这类脚本语言编写出来的代码运行速度获得了极大提升。
6. V8引擎包含以下三个部分，解析器(parser)，解释器(interpreter)，编译器(compiler)。V8本身就是一个C++程序。
7. 解析器将JS代码解析为抽象语法树AST。解释器负责将AST解释成字节码，解释器也可以解释执行代码，编译器负责将字节码编译成运行更加高效的机器代码。
8. 字节码是和平台无关的。
9. 浏览器的工作原理：
   1. 首先根据网页地址，获取html文件。
   2. 解析该文件，构建DOM树。
   3. 构建DOM树的同时遇到CSS和图片，JS文件同时发送请求。
   4. CSS和图片不会阻塞DOM树的构建，而JS可能会改变DOM树，因此会等待JS下载，执行完成JS后再继续解析HTML，构建DOM树。因此JS代码的位置十分重要。