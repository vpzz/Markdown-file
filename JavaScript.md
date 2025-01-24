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

2. 1995年，JavaScript问世，当时的主要用途是代替Perl等服务器端语言，来处理客户端的输入验证。在此之前，验证某个输入的值是否有效，都必须要和服务器进行通信，在那个网速缓慢的年代，在客户端进行验证非常有用。

3. 网景Netscape公司为自家的浏览器Netscape Navigator 2开发了一种客户端脚本语言，一开始叫LiveScript，后来为了蹭Java的热度，改名叫JavaScript。

4. 微软也在IE的最初版本中包含了自己的JavaScript实现（叫JScript，为了避免和网景产生纠纷才起这个名字），即使它有自家的客户端语言VBScript。所以说是微软开启了JavaScript混乱的先河。

5. 网景后来将Navigator浏览器开源为Mozilla Project，后者后来推出了Firefox浏览器。

6. 1998年ISO/IEC将ECMA-262采纳为国际标准。

7. 浏览器对JavaScript的支持体现在对ECMAScript和DOM的实现程度。

8. 完整的JavaScript包含三部分：

   1. ECMAScript，也就是ECMA-262定义的语言，也称为核心JavaScript。

   2. DOM，文档对象模型

   3. BOM，浏览器对象模型

9. 相关的手册规范可以查看MDN（Mozilla Developer Network）。


## ECMAScript

1. ECMAScript并没有输入输出之类的方法，Web浏览器和Node.js是它常见的2个宿主环境。宿主环境提供对ECMAScript额外的扩展，扩展使用ECMAScript的核心类型和语法，提供特定于环境的扩展。

2. 如果不涉及浏览器，ECMA-262定义了如下内容：语法，类型，语句，关键字，保留字，操作符，全局对象。

3. 实现了ECMAScript标准的不只有JavaScript，Adobe的ActionScript也实现了。

4. ECMA-262最新的版本为第10版，ECMA-262的第1版和网景的JavaScript1.1相同，只不过删除了所有与浏览器相关的代码，还做了少量更改。ECMA-262要求使用Unicode标准以支持多语言，而且对象要与平台无关，这也是网景的JavaScript1.1和1.2不符合ECMA-262第1版的原因。

5. ECMA-262的第3版是第一次对这个标准进行更新，这标志着ECMAScrip成为了一门真正的编程语言。

6. 所有浏览器对ES5都提供了完善的支持。


## DOM

1. DOM是一个API，用于在HTML中使用扩展的XML。DOM将整个页面抽象为一组分层的节点，HTML或XML页面的每个组成部分都是一种节点。DOM将HTML和XML文件解析为树型结构，开发者使用DOM API可以轻易地删除，替换，修改，添加节点。

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

   5. screen对象，提供关于用户屏幕分辨率的详细信息

   6. performance对象，提供浏览器内存占用，导航行为和时间统计的详细信息

   7. 对cookie的支持

   8. 其他自定义对象，例如XMLHttpRequest（XHR）对象

3. 因为在很长时间内都没有标准，所以每个浏览器实现的都是自己的BOM。


# 浏览器中的JavaScript

1. 将JavaScript引入HTML中的主要方法是使用`<script`>标签，这个标签由网景创造出，后来被加入了HTML的规范。

2. 使用`<script`>标签有两种方式：

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

3. 该标签有8个可选的属性：

   1. async，表示应该立即下载脚本，但是不能阻止其他页面动作，比如下载资源或等待其他脚本加载。只对外部脚本文件有效。

   2. src，外部js文件的地址

   3. defer，表示脚本可以延迟到文档完全被解析和显示之后再执行，只对外部js文件有效。

   4. type，用来代替language，表示代码块中脚本语言的内容类型，也成为MIME类型。这个值应该始终为"text/javascript"，尽管它已经被废弃了。JavaScript 文件的MIME类型通常是"application/x-javascript"。

   5. integrity，允许对比接受到的资源和指定的加密签名，以验证资源的完整性。如果不匹配，则会报错，且不会执行该脚本。这个属性可以用于确保cdn不会提供恶意内容。

4. 通常推荐使用外部JavaScript，有以下优点：

   1. 可维护性，外部文件容易将JavaScript脚本集中起来管理。

   2. 缓存，浏览器会根据特定的设置，在本地缓存所有外部链接的JavaScript文件，如果两个页面都是用到同一个文件，则只用下载一次。

   3. 适应未来，外部JavaScript不用考虑用XHTML或适配的黑科技。不受HTML和XHTML语法严格程度不同的影响。

5. 在使用行内JavaScript时，代码中不能出现`</script>`，也就是script标签的结束标记。可以用`\`转义`/`即可：

   ```html
   <script>
   function sayHi(){
       console.log("<\/script>");    //在/前面加个\即可
   }
   </script>
   ```

6. 执行行内JavaScript和下载并执行外部JavaScript时，都会阻塞页面。

7. 可以将js代码编写到按钮的onclick中，或者超链接中。

   ```html
   <button onclick = "alert('点我干嘛');">点我一下</button>
   
   <a href = "javascript:alert('又点我');">你也点一下</a>
   
   <!-- 有时候希望超链接不起作用，可以写成如下方式，这样点击时不会执行任何动作-->
   <a href = "javascript:;">你也点一下</a>
   ```

8. 书写在.js文件中，然后在HTML中引入该文件，类似于css，写在外部可以利用浏览器的缓存机制：

   ```html
   <Script type="text/javascript" src = "js/test.js">此时内部的js代码会被浏览器忽略</Script>
   ```

9. ```js
   document.write("向浏览器的页面写入内容");
   console.log("向控制台输出内容");
   document.write(1+"\n")    // 这样并不会换行，需要使用HTML的换行
   document.write(1+"<br />") 
   ```

10. 在XHTML中可以忽略结束标签，但是在HTML中不行。

11. 外部js的优先级高于行内js：

    ```html
    <script src="example.js">    //仅下载并执行外部js,行内js会被忽略。
    function sayHi(){
        console.log("Hi");
    }
    </script>
    ```

12. `<script>`标签可以包含来自**外部域**的js文件，和`<img>`标签一样，其src属性可以包含一个完整的URL，而且整个URL指向的资源可以和包含它的HTML文件不在同一个域中。浏览器在解析外部js文件时，会向src路径发送一个GET请求，以取得相应的资源。这个**初始的请求**不受浏览器同源策略的限制。但是**返回并执行的JavaScript则受限制**。这个请求仍然受父页面HTTP/HTTPS协议的限制。

13. 引用放在别人的服务器上的JavaScript文件必须要小心，因为可能会被恶意篡改。`</script>`标签的integrity属性能够保证这一点。

14. 默认情况下，浏览器按照`<script>`标签在页面中的出现顺序来解释他们，使用async和defer属性的除外。不同`<script>`标签的代码是顺序执行的，后一个必须等前一个解释完才可以解释。

15. 过去，`<script>`标签都被放在`<head`>标签内，这么做的目的是为了把外部的JavaScript和CSS文件都集中到一起，方便管理，例如：

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

16. 不过把所有的JavaScript文件都放在head中，就意味着，必须把所有的JavaScript文件下载并解释完后，才能开始渲染页面。因为页面在浏览器解析到body标签时才开始渲染。这对于包含很多JavaScript的页面来说，会导致明显的延迟，因为在这期间页面会显示为完全空白。因此，现在通常将`</script>`标签放在body标签内的页面内容的后面，也就是body标签的末尾，这样显示空白的时间就变短了，用户会感觉页面加载更快了，如下：

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

17. HTML4.1为`<script`>标签定义了一个defer的属性，这个属性表示，脚本会被延迟到整个页面都解析完毕后（即解析完结束的`</html`>标签）再运行。也就是会立即下载，但是会延迟执行。HTML5规范要求，延迟的脚本也要按照出现的先后顺序执行，都会在DOMContentLoad事件之前执行。不过在实际中，并非总是按顺序或者在该事件前执行。

18. 对defer属性的支持比较早，例如IE4就开始了，但是HTML5要求，defer属性仅对外部脚本有效。而IE8才正式支持HTML5。

19. 对于XHTML文档，指定defer属性时应该写成defer="defer"。

20. HTML5为`<script`>标签定义了async属性，它和defer的功能类似，不同的是，async脚本不能保证按照出现顺序执行。异步脚本保证会在load事件前执行，可能会在DOMContentLoad事件前后执行。使用异步脚本，应该保证其内不会修改DOM。但是好的web开发实践不推荐使用这个方法。

21. 除了使用`<script`>标签，还可以在JavaScript中使用DOM API来动态加载脚本。默认情况下，这种方式加载脚本是异步的，相当于添加了async属性。不过这样做可能会有问题，因为所有浏览器都支持createElement()方法，但不是所有浏览器都支持async属性。因此要统一脚本加载行为，应该将其明确为同步加载。

    ```javascript
    let script = document.createElement('script');
    script.src = 'load.js';
    script.async = false;      //将此脚本设为同步加载
    document.head.appendChild(script);  //在这一步之前并不会发送GET请求。
    ```

22. 动态加载js对于浏览器的预加载器是不可见的，这会严重影响它们在**资源获取队列**中的优先级。可能会严重影响性能。可以在文档头部显式声明，让预加载器知道这些文件动态请求的存在。

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

23. XHTML是将HTML作为XML的应用重新包装的结果，与HTML不同，XHTML中的JavaScript必须包含type属性，且值必须为text/javascript。在HTML中，这个属性是可选的。目前XHTML已经退出了历史舞台。

24. XHTML的语法比HTML严格，这会影响行内JavaScript代码。例如下面的代码在HTML中有效，但是在XHTML中无效：

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

25. 避免上述语法错误有2个方法：

    1. 把所有的<都改为对应的HTML实体形式`&lt`，缺点是会影响阅读。

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

26. 在兼容XHTML的浏览器中可以使用CDATA块来解决问题，但是在不支持CDATA块的非XHTML浏览器中则不行。为此，必须将CDATA作为JavaScript的注释存在，这种格式适用于所有现代的浏览器。

27. XHTML模式会在页面的MIME类型被指定为"application/xhtml+xml"时触发。

28. `<noscript`>标签的出现是用于给不支持或禁用了JavaScript的浏览器显示替代内容。该标签可以包含任何可以出现在body中的元素，script除外。例如：

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Example HTML Page</title>
            <script defer="defer" src="example1.js"></script>
        </head>
        <body>
            <noscript>  <!-- 当且仅当浏览器不支持或禁用了JavaScript时，此标签中的内容<p>标签才会被渲染。-->
                <p>This page requires a JavaScript-enabled browser.</p>
            </noscript>
        </body>
    </html>
    ```


# 语言基础

1. ECMAScript的语法很大程度上借鉴了C语言和其他类C语言。

2. ECMAScript严格区分大小写。每条语句以；结尾，如果不写；浏览器会自动添加，但是会消耗性能。加分号也便于开发者通过删除空行来压缩代码，因为一行可以有多个包含分号的语句。

3. 标识符只能以字母_和$开头。按照惯例ECMAScript标识符推荐使用驼峰命名法。

4. 注释采用C语言风格：

   ```javascript
   /*多行注释
   *
   *  中间的*不是必须的，只是为了美观。
   */
   
   //  单行注释
   ```

5. ECMAScript 5增加了严格模式（strict mode），ECMAScript 3的一些不规范写法在这种模式下会被处理，对于不安全的活动将抛出错误。

   ```javascript
   "use strict"; //这是一个预处理指令，用来控制JavaScript引擎的。对整个脚本启用严格模式，一般放在脚本的开头。
   
   function doSomething() {
       "use strict"; //仅对该函数启用严格模式，
       // 函数体
   }
   ```

6. 控制语句只在执行多条语句时要求必须用代码块包裹起来。但是推荐任何时候都用`{}`包裹起来其子语句。

   ```javascript
   // 有效，但容易导致错误，应该避免，这个和C语言类似
   if (test)
   	console.log(test);
   // 推荐
   if (test) {
   	console.log(test);
   }
   ```

7. ECMAScript是松散类型的，变量可以保存任何类型的数据，三个关键词可以用于声明变量：var，const，let。其中，var在ECMAScript的所有版本中都可以使用，而const和let只能在ECMAScript 6及更晚的版本中使用。


## var

1. 使用var定义变量，变量是没有类型的，可以保存任意类型的值：

   ```javascript
   var message;   //定义了一个变量，可以用它保存任何类型的值。不初始化的情况下，变量会有一个特殊值，undefined。
   var message = "hi";  //定义并初始化。可以随时改变变量的值或类型。
   message = 100; // 合法，但不推荐
   
   var message = "hi", found = false, age = 29;  //同时定义并初始化3个变量
   ```

2. 如果使用var操作符在函数内定义变量，则它会成为函数的局部变量。在函数内定义变量时如果省略var，可以创建一个全局变量。但是不推荐这么做，因为在局部作用域中定义全局变量很难维护。在严格模式下如果省略var，则会被解释器认为是给一个已声明的变量赋值，如果变量未声明过，则会抛出ReferenceError。

   ```javascript
   function test() {
       var message1 = "hi"; // 局部变量
       message2 = "hello";  // 全局变量
   }
   test();  //调用它会创建这个变量并给它赋值，调用之后局部变量随即被销毁。
   console.log(message1); // 出错
   console.log(message2); // 正确
   ```

3. 使用`{}`包裹起来定义并不会使之变为一个更局部的变量，也就是说该变量在会忽略`{}`的存在，这是用于各种分支，判断语句，例如：

   ```javascript
   {
       var age = 26;
   }
   console.log(age); //会输出26，而非undefined。这一点和C语言不一样，需要注意。
   ```

4. 在严格模式下，不能定义名为eval和arguments的变量，否则会导致语法错误。

5. var会将**使用它定义的变量**自动提升到函数作用域的顶部：

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

6. 在全局作用域中使用var定义变量时，JavaScript引擎会将所有由var定义的变量的**定义和初始化**都复制一份到全局作用域的顶部，保持原有的顺序，原来的定义和初始化语句仍然在该位置存在。

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
   name = 'Matt'; //var去掉与否不重要，结果相同
   console.log(name);  //会输出 'Matt'
   name = 'Nicholas';
   console.log(name);  //输出 'Nicholas'
   if (true) {
       name = 'Matt';
       console.log(name); //会输出 'Matt'
   }
   //如果在函数作用域内时，JavaScript引擎仅将定义，而不包括初始化，提升到函数作用域的开头。
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
   //等价于
   function func1(){
       var name;
       console.log(name);  //会输出 "undefined"
       name = 'Nicholas';
       console.log(name);  //输出 'Nicholas'
       if (true) {
           name = 'Matt';
           console.log(name); //会输出 'Matt'
   	}
   }
   func1();
   ```

7. 反复用var声明同1个变量也没有问题：

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

1. let是ES6新定义的关键字。let和var最明显的区别就是，let定义的范围是块作用域，var定义的范围是函数作用域，let的行为和C语言相同，更推荐使用。

   ```javascript
   if (true) {
       var name = 'Matt';
       let age = 26;
       console.log(name); // Matt
       console.log(age); // 26
   }
   console.log(name); // Matt
   console.log(age); // ReferenceError: age 没有定义。
   ```

2. 但是let不允许在同一个**块作用域**内出现冗余声明：

   ```javascript
   {
       let age;
       let age; // 语法错误；标识符age 已经声明过了
   }
   //但是在全局作用域中无所谓
   let age;
   let age; //不会报错
   ```

3. JavaScript引擎会记录用于变量声明的标识符及其所在的块作用域。因此嵌套使用相同的标识符不会出错，因为它们不在同一个作用域中。var和let都可以嵌套定义变量。

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
       let name = 'Matt';  //会在当前块中暂时屏蔽掉之前的同名的name定义，这里不算重复定义，因此不会报错。
       console.log(name); //结果为  'Matt'
   }
   console.log(name);  //结果为 'Nicholas'，因为此时{}内部定义的name已经被删除了
   //let和var
   let name = 'Nicholas';
   if (true) {
       var name = 'Matt';  //错误，因为这里的name是那个用let声明的name。而let不允许重复。
       console.log(name);
   }
   //var和let
   var name = 'Nicholas';
   if (true) {
       let name = 'Matt';  //不会报错
       console.log(name); // 'Matt'
   }
   console.log(name);  //结果为 'Nicholas'，因为此时{}内部定义的name已经被删除了
   ```

4. 使用var和let声明的变量不能彼此重复：

   ```javascript
   var name;
   let name; // SyntaxError
   
   let age;
   var age; // SyntaxError
   ```

5. var和let的另一个重要区别是let不会将变量声明提升到块作用域的开头。在let声明执行前的时段称为暂时性死区。

   ```javascript
   // name 会被提升，全局作用域时，初始化也被提升了
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
   //for循环会快速循环多次(因为设置定时器并不会阻塞)，每次设置1个定时器，然后结束循环。等500ms到达后，多个定时器间隔很近，依次触发。定时器到的时候，会触发指定的函数，环境是当时定义定时器的。
   //setTimeout是设置定时器，第一个参数是到时要执行的函数，第二个为延迟的ms数。这里使用了ES6定义的箭头函数，括号内是参数，{}内为函数体。
   for (let i = 0; i < 5; ++i) {
   	setTimeout(() => {console.log(i)}, 500);
       i=i+2;  //修改的是唯一的那个i。
   }
   //输出为 2 5。JavaScript引擎会在每次循环中为let定义的变量创建一个新的副本，并用用上一轮结束时的值来初始化这个副本，每个setTimeout引用的都是不同的变量实例。因此第一次创建定时器时的i，仅被同一轮循环内的i=i+2修改，第二次循环的i=i+2修改的则是第二次循环时定义的i。第一次进入循环时i=0，退出时i=2，第二次进入循环时i=3，退出时i=5，然后循环结束。
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

1. const的行为与let基本相同，唯一的一个区别是用它定义变量时，必须同时初始化，而且在尝试修改const变量时，会产生运行时错误。const变量也不允许重复定义。

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

2. 如果const 变量引用的是一个对象，那么修改这个对象内部的属性并不违反const的限制。

   ```javascript
   const person = {};
   person.name = 'Matt'; // ok
   person = 32;  //错误
   ```

3. 对于数组也是这样的，因为const修饰的只是arr和person变量：

   ```js
   const arr = ["a","b"];
   arr.push("c");  //不会报错
   console.log(arr); //会输出 ['a', 'b', 'c']
   arr = [1]; //此时会报错，因为修改了arr本身，使其指向别的内容
   ```

4. 因此建议用const来声明数组和对象。


## 使用推荐

1. 通过上面可以发现，var和let混用非常麻烦，而且var本身的行为也和其他编程语言不同，建议以后只用let。let的行为是和其他编程语言完全相同的，都是块作用域，且不能重复声明。

2. 优先使用const，然后才是let。这样可以让静态代码分析工具提前发现不合理的赋值行为。


# 数据类型

1. ECMAScript有6种简单数据类型，Undefined、Null、Boolean、Number、String 和Symbol。Symbol是ES6新增的。还有一种复杂数据类型，Object，即对象类型。对象是一种无序键值对的集合。在ECMAScript6中不能定义自己的类型。

2. typeof 操作符可以用来确定变量的类型：

   ```javascript
   typeof xx;  //也可以用大括号或小括号将xx包裹起来。
   //可能会返回如下7个字符串之一：
   "undefined"  //表示值未定义；
   "boolean"    //表示值为布尔值；
   "string"     //表示值为字符串；
   "number"     //表示值为数值；
   "object"     //表示值为对象（而不是函数）或null(空对象指针)；
   "function"   //表示值为函数；
   "symbol"     //表示值为符号。
   ```

3. 严格来讲，函数在ECMAScript中被认为是1个对象，并不代表一种数据类型。可是，函数也有自己特殊的属性。为此，就有必要通过typeof操作符来区分函数和其他对象。

4. console.dir可以输出对象本身，console.log会将对象当作字符串输出，调试时可能有用。


## Undefined

1. Undefined 类型只有一个值，就是字面值undefined，表示声明了但没有赋值的变量。对于使用var或let定义了，但是没有初始化的变量，都会默认初始化为undefined。

   ```javascript
   let message;
   console.log(message == undefined); // true，而不是 "undefined"，因为后者是一个字符串
   ```

2. 不推荐显式将变量初始化为undefined，因为字面值undefined在ES3之前是不存在的，增加它的目的就是为了正式明确null和未初始化变量的区别。

3. 定义了但未显式初始化的变量和未定义的变量是不同的，后者只能执行一个动作，就是typeof，结果为 "undefined"。对前者执行typeof 时，也会返回"undefined"。虽然对未声明的变量调用delete也不会报错，但这个操作没什么用，实际上在严格模式下会抛出错误。


## Null

1. Null类型也只有一个值，就是null。null表示一个空对象指针，因此`typeof null`会得到 "object"。如果某个变量要用来保存对象，建议使用null来初始化。这样以后只要检查该变量是否是null，就可以知道后续的赋值有没有成功：

   ```javascript
   let car = null;
   null == undefined;  //true，undefined 值是由null 值派生而来的，因此ECMAScript认为它们是相等的。
   if (null){       //null和undefined作为条件都是false
       //不会执行这里
   }
   ```


## Boolean

1. Boolean类型有两个字面值true和false，注意大写的True和False不是布尔类型的值。所有其他ECMAScript类型的值都有相应布尔类型的等价值。可以显式调用Boolean()函数来获取对应的值。

   ```javascript
   //以下结果都为false
   Boolean("")
   Boolean(0)
   Boolean(NaN)
   Boolean(null);  
   Boolean(undefined); 
   ```


## Number

1. Number使用IEEE754来保存整数和浮点数，整数可以用8和16进制来书写。

   ```javascript
   let octalNum = 070;  //结果为56，8进制在严格模式下是无效的。
   let hexaNum = 0x1a;  //结果为26，16进制必须以0x开头，大写的X无效。后续的16进制字母大小写均可。
   //0b开头表示2进制。2进制不是所有的都支持
   ```

2. 要定义浮点值，数值中必须包含小数点，而且小数点后面必须至少有一个数字。因为存储浮点值使用的内存空间是存储整数值的两倍，所以当小数点后没有数字或只有0时，会被转化为整数。浮点值的精确度最高可达17位有效数字。

   ```javascript
   let floatNum1 = 1.1;
   let floatNum2 = 0.1;
   let floatNum3 = .1;
   let floatNum1 = 1.; // 小数点后面没有数字，当成整数1处理
   let floatNum2 = 10.0; // 小数点后面没有只有0，也会被当成10处理
   let floatNum = 3.125e7; //科学计数法计数，等于31250000
   ```

3. js对浮点数的计算不是精确地，整数的是精确地，除非超出边界。

   ```js
   var a = 0.1 + 0.2;
   console.log(a);  //输出为0.30000000000004
   ```

4. ECMAScript将能表示的数值范围存储在以下常量中，如果在某个计算得到的数值超过了可以表示的范围，会被自动转换为Infinity（Number类型的一个字面量）。使用Number.NEGATIVE_INFINITY 和Number.POSITIVE_INFINITY也可以获取正、负Infinity。

   ```javascript
   Number.MIN_VALUE  //在大多数浏览器中为 5e-324
   Number.MAX_VALUE  //在大多数浏览器中为 1.7976931348623157e+308
   //绝对值特别大或特别小（接近0）的数都会无法表示。
   Number.MIN_VALUE/2 //超出范围，会被认为是0。
   Number.MAX_VALUE*2 //超出范围，会被认为是Infinity
   -Number.MAX_VALUE*2 //超出范围的负数会被认为是-Infinity
   
   isFinite(Number.MAX_VALUE*2); //判断参数是否是有限值，结果为 false。
   isFinite(2);   //结果为 true。
   ```

5. NaN是一个特殊的Number类型的字面值，意思是 Not a number。如果一个函数本来要返回数值，但是出现了错误，可以返回NaN，而不是抛出错误。0，+0，-0三个数之间相互作除法，结果都是NaN，它不分正负。非零数除以±0，结果为±Infinity。

   ```javascript
   0/0  0/+0  0/-0  +0/0  -0/+0 ;   //这些都是NaN，因为从极限的角度看，这些都是未定式
   2/+0;  // Infinity
   2/-0;  // -Infinity
   2/0;   // Infinity
   ```

6. 任何涉及NaN的操作结果都是NaN，NaN不等于的任何值，包括它自己。无法通过 == NaN来判定变量是否为NaN，因此js提供了isNaN()函数来判断参数是否为NaN。如果参数是一个对象时，会调用对象的`valueOf()`方法，然后判断返回值能否转化为数值。如果不能，再调用toString()方法，测试返回值。

   ```javascript
   NaN+3;  //结果为NaN
   NaN == NaN;  //false
   
   isNaN(NaN);  //true
   isNaN("10"); //false，可以转化为10
   isNaN("blue"); //true，不能转化为数值
   isNaN(true);  //false，可以转化为1
   isNaN(false); //false，可以转化为0
   ```

## String

1. String类型表示0或多个16位Unicode字符序列。可以用三种引号括起来，彼此没有区别，但是不能混搭，也可以使用\转义引号。

   ```javascript
   let firstName = "John";
   let lastName = 'Jacob';
   let lastName = `Jingleheimerschmidt`  //这个称为重音符号
   "ab" + 'c' //可以拼接
   ```

2. 模板字符串，用于拼接字符串和变量：

   ```js
   //只能用``来包裹
   let age = 18;
   let str1 = `我今年${age}岁了` //结果为 "我今年18岁了"
   ```

## 类型转化

1. 强制类型转化，一般是将其他类型的值转化为number，string，boolean。

2. 其他类型转化为字符串：

   1. 调用被转换类型的toString()方法，可以的到该类型的变量转化后的字符串，不会影响原先的变量。null和undefined没有toString()方法，只能用String()函数。
   2. 调用String()函数。

3. 一般需要在特定的类型中重写toString()方法。

4. 有三个函数可以将非数值转化为数值，如果对非字符串使用，则会先将其转化为字符串，再操作：

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
   //parseInt()的第二个参数，表示进制，可选。
   parseFloat(); //将字符串转化为浮点数，第二个小数点之后的内容无效。"123"→123，"22.5"→22.5， "22.5.2"→22.5，".35"→0.35。只能解析10进制小数。
   ```

5. 其他类型转为boolean类型：只有一种方法，使用Boolean()。

6. 算数运算符会对运算数进行强制类型转化，再运算。

# 运算

1. `+ `不仅仅是算数运算符，还可以用来连接两个字符串。任何值和字符串做拼接，都会强制转化为字符串（隐式）。

2. js支持自增和自减运算。a++或++a。都会让a自增，但是这两个表达式的值不同，a++的值等于自增前的，这点和C语言相通。

3. 逻辑运算符`&&  ||  !`，分别为与，或，非。

4. JS的逻辑运算都是短路的，如果通过第一个操作数就可以判断逻辑值，则不会计算第二个操作数的值。因此通常会使用如下逻辑：操作A&&操作B。 这个表达式，表示如果A执行成功，再执行B，如果A失败，则不会执行B。

5. 赋值运算符 `+=   -=   *=   /=   %=`。

6. 9%4为9除以4的余数，结果为1。

7. 对于比较运算符，如果两端都是字符串，会进行逐个字符的对比，比较的是Unicode编码。

8. js和html分别输出Unicode字符：

   ```js
   console.log("\u2620")    //16进制2620是Unicode对骷髅符号的编码。
   ```

   ```html
   <h1>&#9760;</h1>        <!-- 十进制9760，对应16进制2620，输出的和上面的相同。 -->
   ```

   ![1613920612796](JavaScript.assets/1613920612796.png)

9. == 相等运算符，当左右操作数的类型不同，则会进行隐式类型转换，然后再比较。因此  "1" == 1的结果为true。

10. 全等运算 =\=\= ，不会做类型转化，如果两个变量的类型不同，则直接返回false。

    ```js
    "123" === 123      //false
    null === undefined  //false
    //不全等为！\=\=，可以用！和全等运算替换。
    ```

13. 条件（三元）运算符，`条件表达式 ? 语句1 : 语句2`。对条件表达式求值，如果为真，则执行语句1，并返回结果，否则执行语句2，并返回结果。

15. 逗号运算符，一般在声明多个变量时使用：

    ```js
    var a,b,c;
    ```

16. 运算符的优先级：

17. ![1613926279007](JavaScript.assets/1613926279007.png)

    

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

2. 条件分支语句，switch。 依次判断条件表达式 =\=\= 表达式1，2，3，4，注意这里是三个等号的全等判断。进入case后，直到遇到break，才会退出switch语句。

   ```javascript
   switch(条件表达式){
   	case 表达式1:
   		语句;
   		break;
   	case 表达式2:
   		语句;
   		break;
   	case 表达式3:
   		语句;
   		break;
   	default:
   		语句;
   		break;
   }
   ```

3. while循环：

   ```js
   while(条件表达式){   //条件为真时继续循环
   	break;    //可以跳出循环
   }
   
   do {
            
   } while (条件表达式)  //先执行在判断，条件为真时继续循环
   ```

4. for 循环：

   ```js
   for (初始化表达式;条件表达式;更新表达式){
   }
   
   for (let i = 0 ; i<10 ; i++){
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

7. continue用来跳过本次循环，开始执行下次循环，不执行本次循环后续的代码，也支持标签。

# 面向对象

1. 常见的对象类型：

   1. 内建对象，由ES标准中定义的，无论是浏览器还会node.js都支持，例如math，string等。
   2. 宿主对象，由JS运行环境提供的，目前主要是浏览器中的BOM和DOM。 例如console，document。
   3. 自定义对象，由开发人员自己创建的。

2. 使用new关键字调用构造函数，来创建对象。

   ```js
   let obj = new Object(); //这点和C++相同
   obj.name = "hha";           //第一次调用表示，为obj对象添加一个属性，
   console.log(obj.age);       //获取未定义的属性时，会返回undefined。
   delete obj.name;            //删除对象的属性。
   ```

3. 对象的属性名不强制要求遵循标识符的规范，不过仍建议遵守。

4. 也可以使用`[]`来操作对象的属性，这样更灵活，因为此时属性名是字符串，可以拼接得到：

   ```js
   let obj = new Object();
   obj["属性名"] = 20;
   console.log(obj.属性名)         //以前版本无法获取，现在可以通用了。
   console.log(obj["属性名"])       //通过任意一种方式都可以获取。
   ```

5. 对象在浏览器中的显示为：

   ```js
   Object {name : 'hha', 属性名 : 20}//类名+键值对，由于键始终为字符串，因此就不加引号了
   ```

6. in运算符，检查一个对象中是否含有指定的属性。

   ```js
   "属性名" in obj      //结果为true。
   ```

7. 基本数据类型和引用类型的主要区别就是赋值时的操作不同。引用类型默认是浅拷贝。

   ```js
   var a = 3;
   var b = a;        //此后a和b完全没有关系，他们的值分别存储在不同的内存空间中。
   var c = new Object();
   var d = c;        //c和d都指向同一块内存空间，修改c的属性，d也会看到。
   ```

8. 任何变量都保存在栈中，基本数据类型的内容直接存在栈中，引用数据类型的内容保存在堆内存中，栈中保存的是其堆内存的地址。

9. 基本数据类型在比较时，比较的是值，引用数据类型在比较时，比较的是内存地址。

10. 可以使用对象字面量来创建对象：

    ```js
    var obj = {};       //等价于 new Object()
    //可以在创建对象时，直接指定属性和值。类似于JSON数据。
    var obj = {name:"hha", age:20, gender:"男"} //属性名可以加引号，也可以不加引号。
    //下面这种写法更清晰
    var obj = {
        name:"hha",
        age:20,
        gender:"男"
    }
    ```

11. for in，可以枚举出对象内的属性和方法：

    ```js
    for (let i in obj){   //每次循环，i都被赋值为obj的属性名称。可以用obj[n]来调用。
    	console.log(obj.i);
    }
    //上面如果使用obj.i来调用，则每次结果都是undefined，因为此时i是一个字符串，无法用obj."name"来获取其name属性。
    ```

12. 在每次的函数调用时，解析器都会额外传递一个隐含参数this。this指向调用函数时的上下文对象，随着函数调用方式的不同，this指向不同的对象。

13. ```js
    function fun(){
    	console.log(this);
    }
    var obj = {callFun:fun} //obj对象有一个属性callFun，它的值为一个函数对象。
    //以函数的形式调用时，this为window
    fun();		     //输出window对象，直接调用，fun变量属于window的属性。
    //以方法的形式调用时，this为调用的对象
    obj.callFun();    //输出obj对象，虽然也是调用fun函数，但是是从不同的位置
    ```

14. 在全局作用域中的this表示window对象。

15. 使用工厂方法(使用的Object类的构造函数)创建大量对象，避免重复书写代码。

    ```js
    function createObj(name, age, gender){
    	return {
            name:name,       //第一个name是属性，默认当做字符串处理，也可以写成"name"。
            age:age,
            gender:gender
        }
    }
    ```

16. 构造函数和普通函数定义方式没有区别，不同的是构造函数习惯于首字母大写，还有调用方式的不同，构造函数要用new关键字调用。

    ```js
    function Person(){
    }
    var per1 = Person();      //普通的函数调用，per1为undefined，因为该函数没有返回值。
    var per2 = new Person();  //构造函数调用，per2为object，因为使用了new。
    ```

17. 构造函数的执行流程：

    1. 调用时立刻创建一个对象。
    2. 将构造函数中的this指向当前要新建的对象，因此可以在构造函数中使用this来引用该对象。
    3. 执行构造函数中的代码，来设置对象的属性。
    4. 将新建的对象作为返回值返回（不用写return）。

18. ```js
    function Person(name){
    	this.name = name;
    }
    var per = new Person();      //此时per是Person类型的，而不是Object。
    console.log(per instanceof Person);     //结果为true。使用 instanceof 关键字来判断一个对象是否是某一个类的实例。任何对象都是Object的实例，因为所有的类都是继承自Object。
    ```

19. 使用同一个构造函数创建的对象，是同一类对象，因此也将构造函数称为一个类。使用该构造函数创建的对象称为该类的一个实例。

20. 定义在对象中的方法。，可以用以下解决办法：

    ```js
    function Person(name){
    	this.name = name;
    	this.sayName = function sayName(){ //这种匿名函数的方式，会在每次创建对象时，都创建一个新的函数，这样是没有必要的。
        };
    }
    //实际上只要给整个类书写一个方法就行了，修改为如下：
    function sayName(){
    //这里也可以使用this，直接调用此函数时，this为window，通过Person类的对象p1调用时，this为p1。
        console.log(this === window);
        console.log(this === p1);
        console.log(this.name);
    }
    function Person(name){
    	this.name = name;
        this.sayName = sayName; //但是这样会把类的内部方法暴露出来，也会污染全局作用域，容易造成命名冲突。
    }
    let p1 = new Person("abc");
    sayName();    //输出true false  。最后一个结果为空字符串""。一般应该为undefined，而这里比较特殊，因为window对象有name属性，就是空字符串。。。
    p1.sayName(); //输出false true "abc"
    ```

# prototype

1. 我们所创建的每一个函数，解析器都会向函数中添加一个属性，prototype。每个函数的prototype都不同。

2. prototype就是所谓的原型对象。

   1. 如果函数作为普通函数调用，prototype没有任何作用。
   2. 如果函数当做构造函数调用时，创建的所有对象中，都有一个属性prototype，指向该构造函数的prototype属性。可以通过`对象.__proto__`来访问。

3. ```js
   function Person(){
   }
   var mc = new Person();
   console.log(mc.__proto__ == Person.prototype);  //结果为true。
   ```

4. 原型对象相当于类的一个公共区域，所有该类的实例都共享该对象，包含一个指向该对象的属性`__proto__`。可以将对象中共有的内容存放到prototype对象中。

5. ```js
   function Person(){
   }
   Person.prototype.a = 123;
   var mc = new Person();
   console.log(mc.a);        //结果输出为123.
   ```

6. 当访问对象的属性或者方法时，会现在对象自身中寻找，如果找的到，就地返回。如果找不到，则会去对象的原型对象中寻找，即`mc.__proto__.a`。

7. ```js
   function Person(){
   }
   Person.prototype.sayName = function (){
   };
   var mc = new Person();
   console.log("sayName" in mc);                //in会检查原型对象，也会返回true。
   console.log(mc.hasOwnProperty("sayName"));  //返回false。hasOwnProperty函数会检查对象自身是否有该属性。
   ```

8. 以后，在书写类的构造函数时，可以将所有对象共有的属性和方法添加到类的原型对象中。

9. 原型对象也有原型对象。直到找到object对象为止，因为该对象没有原型对象，但是也有个`__proto__`属性，值为null。

   ```js
   function Person(){
   }
   var mc = new Person();
   mc.__proto__.__proto__.hasOwnProperty("hasOwnProperty"); //返回true。可以看到hasOwnProperty方法是mc的爷爷中的，也就是Object对象的。
   console.log(mc.__proto__.__proto__.__proto__);   //结果为null。
   ```

10. 从上面可以看出，用户自定义的类，一般都是Object类的孙子。

11. 当使用console.log打印对象时，实际上是调用该对象的toString()，然后将该函数的返回值打印。

12. toString()也在该对象的爷爷object中，可以为该类添加一个共有的toString方法，即给该类的父亲添加一个方法。

    ```javascript
    Person.prototype.toString(){
    }
    ```

13. 由此可以看出，用户自定义类没有直接继承自object，而是中间还有一个中介的原因。该中介用来存放用户自定义类的共有属性和方法。 如果没有该中介，则定义用户自定义类的共有属性时就会修改到object类，进而会影响到所有的类。

14. 垃圾回收 garbage collection。

    ```javascript
    var obj = new Object();
    obj = null;
    ```

15. 当一个对象没有被任何变量引用时，就永远无法再操作该对象。这种对象就是垃圾，过多会占用大量内存空间。JS会自动进行垃圾回收，销毁垃圾对象。用户能做的就是将所有指向该对象的引用赋值为null。这样垃圾回收器会适时回收。

# 作用域

1. 作用域分为全局作用域和函数作用域两种。

2. 全局作用域：直接编写在script标签内的代码，都在全局作用域中。在页面打开时创建，关闭时销毁。window全局对象就表示浏览器的窗口，它是内建的。在全局作用于中创建的变量都会作为全局对象window的属性存在。

   ```js
   var a = 3;
   console.log(window.a)       //会输出3。
   
   //对于没有定义的全局变量，直接使用会报错，而当做window的属性来使用则为undefined。
   console.log(b)          //报错，提示 not defined
   console.log(window.b)   //不会报错，输出undefined
   ```

3. 全局作用域中的变量都是全局变量，在页面的任意部分都可以访问到，可以跨脚本。

4. 使用函数声明来创建的函数，也会和用var声明的变量一样，被提前，而使用函数表达式创建的函数则不会。

   ```js
   fun1();        //由于声明的提前，可以在此处正常调用fun1。当然这需要把这两行放在同一个脚本中，或者在控制台同时执行这两行，分开执行时会报错。
   function fun1(){
   }
   
   fun2();       //会报错，因为不会被提前
   var fun2 = function(){
   };
   ```

5. 函数作用域，会在调用函数时创建，函数执行完毕时销毁。每次调用都会创建一个新的独立的作用域，因此可以递归。

6. 在函数作用域可以访问到全局变量，反之不行。

7. 函数内的局部变量会屏蔽掉外部的全局变量。重复声明的变量不会覆盖掉之前的。

   ```js
   var a = 10;
   function fun(){
   	var a = "hah";           //不会覆盖掉之前的
       c = 9                    //在函数中，不使用var声明的变量都会被当做全局变量。
   	console.log(a);          //输出 hah 。
       console.log(window.a);   //访问的是全局的变量a，输出10。
   }
   console.log(a);             //输出 10。
   console.log(c);             //并不会输出 9，只有执行fun()之后，c才会被定义。
   ```

# 数组

1. 数组也是一个对象，不同的是，普通对象使用字符串来作为属性名，数组使用数字来操作元素。

2. 索引从0开始。数组的存储性能比普通对象好。

   ```js
   var arr = new Array();
   console.log(arr);             //返回空
   console.log(typeof arr);      //返回object。
   ```

3. 数组操作元素使用`[]`。

   ```js
   arr.__proto__.hasOwnProperty("toString")   //可以看到Array类重写了object的toString方法，因此console.log(arr)会输出数组中元素的内容。
   ```

4. 读取未赋值的数组元素时，不会报错，会显示undefined。

5. 数组的常用属性和方法：

   ```js
   var arr = new Array();
   arr.length;      //获取数组的长度，对于非连续数组，结果不是数组中的元素的个数，返回的是已经使用的最大下标+1。
   arr[arr.length] = 20;      //向arr数组的末尾添加一个元素。
   arr.push(31,"hha");         //像数组末尾添加多个元素，返回新的的数组的长度。
   arr.pop();                 //删除最后一个元素，并将之返回。
   arr.shift();               //删除数组开头的元素，并将之返回。
   arr.unshift("hah",23);     //向数组的开头添加多个元素。完成后arr[0]为"hah"。
   arr.slice(2,5);            //切片，将arr[2]到arr[4]提取成一个新的数组。左闭右开，第二个参数可以省略不写，此时会截取其后的所有元素。
   arr.splice(2,1,"hah","ss");           //删除原数组中对应的区间的元素(第一个参数是开始位置，第二个为数量)，返回该区间。第三个及后续参数都将会插入到第一个参数的位置之后。
   arr.concat(arr1,arr2,"hah");          //将arr,arr1,arr2和"hah"拼接为一个新的数组返回，不会修改原数组。
   arr.join();                //返回一个由该数组元素构造的字符串。默认的连接符为逗号，也可以制定一个字符。
   arr.reverse();             //将原数组逆序。
   arr.sort();                //按照元素对应字符串的Unicode编码从小到大对原数组排序。
   arr.sort(1,2,3,4,11);     //结果为1,11,2,3,4。
   //可以自己制定排序的规则，给sort传递一个排序函数。
   arr.sort(function(a,b){
   //会调用很多次，每次传入的两个元素总是一个在左,一个在右,如果返回值>0,则交换两个元素。如果<=0,则不交换。
       return ;
   })
   ```

6. js的数组永远不会越界。length属性可以直接被修改，通过这样可以删除(真实删除)部分末尾元素。

7. 使用数组字面量来创建数组：

   ```js
   var arr = [];                      //空的数组
   var arr1 = [1,2,"hha"];            //创建的同时赋值
   var arr2 = new Array(1,2,"hha");   //使用构造函数创建数组时，也可以添加元素。
   ```

8. 不过存在以下不同：

   ```js
   var arr = [10];                 //创建一个数组，只有一个元素，为10。
   var arr1 = new Array(10);       //创建一个长度为10的数组，即arr1.length = 10
   ```

9. 数组的元素可以是任何类型。数组也可以嵌套，构成高维数组。

10. 数组的遍历：

    ```js
    var arr = [123,22,"ssd"];
    for (var i = 0; i < arr.length; i++){
        console.log(arr[i]);
    }
    ```

11. 也可以使用for each来遍历数组,不过该方法对于IE8及以下的不支持。此时参数一个函数对象，可以使用匿名函数。

    ```js
    arr.forEach(function(a, b, c){
        console.log(a)
    });
    ```

12. 数组中有几个元素，就执行几次。每次会传入如下三个参数：

    1. 对应该次循环的元素
    2. 该次循环元素的下标
    3. 正在遍历的数组

13. 数组的索引可以是负值，索引-1表示索引0的左侧，即最后一个元素。

# 函数对象

1. 函数也是对象，可以使用Function类的构造函数来创建：

   ```js
   var fun1 = new Function(); //创建一个函数对象，此时并不会调用它。此函数的函数体为空，调用它时什么也不做
   var fun2 = new Function("console.log('函数')"); //可以将要封装的代码以字符串的形式传递给构造函数。
   fun2()  //调用函数
   ```

2. 函数对象具有所有普通对象的功能，可以为其设置属性。

3. 实际使用中，很少使用上面的构造函数来创建函数。一般使用函数声明来创建函数，两种方法结果相同。

   ```js
   function 函数名([形参1,形参2,形参3]){    //[]表示可选
   	//具体的代码实现。
   }
   ```

4. 也可以使用函数表达式来创建函数：

   ```js
   var fun1 = function([形参1,形参2,形参3]){ //相当于function fun1 ...
   };
   ```

5. 上面等号右边为匿名函数，可以在创建的时候调用，直接在后面加()。定义匿名函数的时候需要在整个函数的定义外边加上括号，否则不会识别，如果是赋值给变量，则不用加括号。

   ```js
   (function(a,b){ //函数有2个形参
       console.log("a=" + a + " b=" + b);
   })(1,3) //创建的同时调用，传递了2个实参。结果输出为a=1 b=3
   //还有一种方法，在function前面加上!或者+等符号，都可以省略原来的括号。
   !function(a,b){}()
   ```

6. 函数的形参就相当于在函数内声明了一个变量，但是并不赋值，当函数被调用的时候，可以用实参给形参赋值。

7. 调用函数时，解析器不会检查实参的类型，也不会检查实参的数量。多或者少传递参数，不会报错。

8. 使用return 来设置返回值。空的return或者不写return，相当于return undefined。

9. 当函数的参数多了以后，顺序可能会乱，可以将实参和形参都缩减为一个对象。

10. JavaScript的函数中有个内置的对象arguments 。argument对象包含了该次函数调用的参数数组，可以方便地进行参数的使用。

11. 函数对象也可以作为另一个函数的参数，也可以将匿名函数写在另一个函数调用的地方，开发中经常用这种方法设置回调函数。

    ```js
    func(function func2(){
        
    })
    ```

12. 在函数的声明内部也可以声明函数。

13. 当一个函数成为对象的某个属性时，习惯称之为对象的方法。

14. 函数对象的两个方法，call()和apply()，调用时都会运行函数本身。不过这样调用时第一个参数，会被当做this传递到函数内部：

    ```js
    function fun(){
    	console.log(this)
    }
    var obj = new Object();
    fun();                //这里的this是window对象。
    fun.call(obj);        //这里的this是obj对象，即第一个参数。
    fun.apply(obj);       //同上
    //call和apply的区别是apply对于后续的实参，需要封装到一个数组中。
    fun.call(obj,1,2);
    fun.apply(obj,[1,2]);
    ```

15. 调用函数时，除了this，还会传入隐含的arguments参数，封装了所有的实参：

    ```js
    function fun(){               
        console.log(arguments.length);        //类数组对象，也可以通过索引操作元素。
        console.log(arguments.callee == fun); //结果为true。arguments还有一个属性，callee，指向当前正在执行的函数对象。
    }
    func(12,3);          //输出2。
    ```

16. 箭头函数中，没有this。

17. 因此即使不定义形参，也可以使用实参。



# 内建对象

1. Date对象

   ```js
   var d = new Date();    //默认为当前代码执行的时间。
   console.log(d);        //Wed Feb 24 2021 00:32:23 GMT+0800 (中国标准时间)
   var d1 = new Date("12/03/2016 11:20:15")  //接受一个字符串，创建指定日期的时间对象。
   // 格式为      月/日/年 时:分:秒
   ```

3. Math对象，它不是构造函数，而是一个工具类，里边封装了各种数学运算的相关属性和方法。使用Math不用创建对象，直接调用就即可。

   ```js
   var m = new Math();          //不能这样用
   Math.PI;         //常量π
   Math.abs(-2);    //结果为2.
   Math.ceil(1.5);  //结果为2,向上取整。
   Math.floor(1.5); //结果为1,向下取整。
   Math.round(1.4); //四舍五入为整数。
   Math.random();   //获得0-1之间的随机小数，不包括0和1。
   ```

4. 常量属性一般用大写表示。

5. 如果想要获得一个0-10之间的随机数，且能取到0或10，可用如下代码：

   ```js
   Math.round(Math.random()*10);
   ```

# 包装类

1. JS提供了三个包装类，可以将三种基本类型数据转化为对象。String，Number，Boolean。这样就可以使用面向对象的特性了。

   ```js
   var n = new Number(3);
   var s = new String("hah");
   var b = new Boolean(true);
   ```

2. 实际开发中，基本不会使用基本数据类型的包装类，因为在做一些比较时，结果不可预期，它们的存在是为了JS解析器自己使用。

3. ```js
   var b = new Boolean(false);
   if (b){        //由于b是对象，因此会将其转化为bool值，而对象转化的结果始终为true。
       console.log("true")
   }
   ```

4. 方法和属性只能添加给类对象，不能添加给基本数据类型。但是基本数据类型可以使用包装类的属性和方法。

   ```js
   var a = "hah";
   var s = a.toString();          //JS解析器会临时将a转化为对象。调用完成后又将转回基本数据类型。
   a.hello = "sdd"; //是为a转化过去的那个临时的string对象添加了一个属性。
   console.log(a.hello); //结果为undefined，因为这一步转化的string对象是一个新的对象，和上一步的不一样，因此找不到hello属性，所以返回undefined。
   ```

5. 在底层，字符串是以字符数组的形式保存，因此也可以用[ ]来索引，可以使用数组的函数。

   ```js
   var s = "asd";
   var sa = ["a","s","d"];
   s[1] == sa[1] //true
   ```

# 定时器

1. 使用间隔函数来定期调用某个函数：

   ```js
   setInterval(function(){console.log("打印");}, 1000); //每1000ms，调用一次。执行到这里的时候，不是立即调用。
   //该函数的返回值是定时器的编号，后续关闭定时器时需要用到。
   clearInterval(编号); //关闭指定的定时器。
   ```

2. 还有一种是要延迟一定时间后再调用一次的情况，类似于闹钟：

   ```javascript
   setTimeout(回调函数，等待的ms数); //返回值是定时器编号
   clearTimeout(编号); //关闭指定的定时器，一般不用。
   ```

# DOM和BOM

## 结构

1. DOM（Document Object Model），文档对象模型，浏览器对HTML页面进行解析生成DOM树，JS通过DOM来操作网页中的标签，元素。顶级对象是document。

2. ![1614100614015](JavaScript.assets/1614100614015.png)

3. BOM（Browser Object Model），浏览器对象模型，JS通过BOM来操作浏览器窗口，例如alert。顶级对象是window。

4. html文件和`<html>`标签是两个不同的对象。href是对象a的属性。

5. HTML标签，文本，注释，属性，整个文档，都是节点Node。常见的有4类：

   1. 文档节点，整个HTML文档，只有一个，就是document对象。
   2. 元素节点，HTML文档中的各种标签。
   3. 属性节点，标签的属性。
   4. 文本节点，标签内的文本内容。

6. 各种类型节点的3个属性：

7. <img src="JavaScript.assets/1614100841255.png" alt="1614100841255" style="zoom:67%;" />

8. document中保存着对一些顶级标签的引用。

   ```js
   document.documentElement; //<html>根标签。
   document.body;            //<body>
   document.head;            //<head>
   document.all;             //页面中所有的元素，一般为html,head,meta,title,script ,body等元素，不分层级。等价于document.getElementsByTagName("*");
   ```

9. 浏览器提供了现成的对象供程序员操作DOM树，名称为document。它是一个全局变量，是window对象的属性，代表整个HTML文档，也就是说BOM包含了DOM

10. window对象还包含了navigator，location，history，screen对象。

11. location对象，拆分并保存了URL地址的各个组成部分。常用的属性和方法：

    1. href属性，获取完整的URL地址，对其赋值可以进行跳转。

    2. search属性，获取地址中携带的参数，也就是?及后面的部分，例如链接为`https://www.baidu.com?wd=abc&user=1112`，其中有2个参数，分别为wd和user，这里search属性的值为`"?wd=abc&user=1112"`。

    3. hash属性，获取地址中的哈希值，也就是#及以后的部分。在单页面应用中存在，类似于QT编程中的MDI多文档界面，允许不刷新网页，显示不同的页面。例如网易云的主页，`"https://music.163.com/#/friend"`。这里hash属性的值为`"#/friend"`。

    4. reload方法，用来刷新当前的页面，相当于F5，如果传入true参数，则强制刷新，也就是Ctrl+F5，不从本地缓存中取数据。

12. navigator对象，记录了浏览器自身的相关信息。

    1. userAgent属性，保存浏览器的版本和平台。`"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"`。可以用来判断是否是移动端，从而跳转到移动站点。

13. history对象，管理历史记录，功能和浏览器左上角的前进，后退按钮相同。

    1. back方法，后退
    2. forward方法，前进
    3. go(n)，如果n是1，则前进1个页面，如果n是-1，后退1个页面。


## 获取元素

1. 元素的id，type，value等属性都可以使用.来获取，但是class属性不可以，因为class时js的关键字，需要使用className来读取。优先使用ID，其次是className，最后才是标签类型。

2. 推荐使用CSS选择器来选择元素：

   ```js
   // 参数为字符串，包含一个或多个有效的css选择器，选择器之间是且的关系，而非递进。
   document.querySelector(".box1 div");    //在document对象下查找，类名为box1的div标签。该方法只能返回第一个匹配的元素。
   document.querySelectorAll(".box1 div"); //同上，但是返回一个NodeList的数组。实际上是一个伪数组，有长度，有索引号，但是不能push和pop。
   //  #id   根据id属性选择
   //根据相对关系查找
   "A > B" //表示A的子元素中查找满足条件B的元素，不递归。
   "A B" //表示A的所有后代元素中查找满足条件B的元素，递归。
   "A + B" //在A的兄弟元素中寻找B。
   "A.B" //不表示相对关系，而是A标签，且className为B的元素。
   //根据特定或自定义属性来选择
   "[role]" //选择具有role属性的元素
   "[role=main]" //选择具有role属性，且值为main的元素
   ```

3. 通过document对象，获取它的子元素节点。

   ```javascript
   getElementById()         //通过id属性来获取一个元素节点对象
   getElementsByTagName()   //通过标签名获取一组元素节点对象
   getElementsByName()      //通过name属性获取一组元素节点对象
   ```

4. 元素的ID是唯一的。即使根据TagName或Name查询到的对象只有一个，也会封装到数组中。

5. jQuery就是用来简化DOM查询的。

6. 通过具体元素来获取其他元素。

   ```js
   btn.getElementsByTagName(); //方法，在btn节点的子孙中查询
   //以下三个都是属性
   btn.childNodes; //返回所有子节点的数组
   btn.firstChild; //第一个子节点
   btn.lastChild;  //最后一个子节点
   ```

7. childNodes，firstChild，并非只获得元素节点，标签间的文本也会被当做文本节点（IE8及以下不会考虑空白文本节点）。children，firstElementChild只返回子元素节点，例如：

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

8. 获取父节点和兄弟节点：

   ```js
   btn.parentNode; //btn节点的父节点
   btn.previousSibling; //前一个兄弟节点
   btn.nextSibling; //下一个兄弟节点
   ```

9. 父节点肯定是元素，因为文本没有子节点。但是兄弟节点可能是标签间的文本。而previousElementSibling之类的就可以忽略标签之间的空白文本，不过IE8及以下不支持。

10. 如果是用在移动端的网页，则不用考虑兼容IE8。

11. 如下代码，要获取标签内的北京这个字符串，如下三种方法可以：

    ```html
    <li id="bj">北京</li>
    <script>
    	document.getElementById("bj").innerHTML;
        document.getElementById("bj").innerText;
        document.getElementById("bj").firstChild.nodeValue;      //复杂，不建议使用。
    </script>
    ```

12. DOM树的增删改操作：

    ```js
    appendChild();  //添加子节点
    removeChild();  //删除子节点
    replaceChild(); //替换子节点
    insertBefore(); //在指定的子节点前插入新的子节点
    createAttribute(); //创建属性节点
    createElement();   //创建元素节点
    createTextNode();  //创建文本节点
    getAttribute();    //返回指定的属性值
    setAttribute();    //设置指定的属性值
    ```

## 修改内容和属性

1. innerHTML是用来获取标签内部的HTML代码，这个对于自结束标签没用。innerText相当于将获取到的HTML标签去除。

   ```html
   <input type="radio" name="gender" value="male"/>
   
   <div class="box"><strong>内容</strong></div>
   <script>
   	const box = document.querySelector(".box");
       console.log(box.innerHTML);  //输出为"<strong>内容</strong>"
       console.log(box.innerText);  //输出为"内容"
       //因此使用innerHTML进行的设置会被解析，而innerText设置的不会被解析。一般不推荐这么来设置样式，可以通过css来设置。
   </script>
   ```

2. 通过style属性的子属性修改某个元素的样式，这样修改的是内联样式，也就是通过标签的style属性设置的：

   ```js
   对象.style.width = "200px"; //设置宽度为200像素，单位不能省略
   //特殊情况 css样式的background-color在js中-会被判定错误，需要用backgroundColor替代，即小驼峰命名。
   //这种方法只能逐个修改样式，比较麻烦
   ```

3. 操作类名来修改样式：

   ```js
   对象.className = "box"  //修改对象的类名（不用加点，会覆盖掉旧的），这样他就会应用box类的所有样式。相当于切换到了一整套预设方案。需要在css中存在.box这样的一个样式。
   //设置多个类，也就是会应用多套样式。
   对象.className = "box nav"
   //有时候为了追加样式，就必须在新的类名中包含原有的类名，这比较麻烦，因为不知道原来类名是什么
   ```

4. 通过classList来修改样式：

   ```js
   元素.classList.add("类名");     //增加一个类名
   元素.classList.remove("类名");  //删除一个类名
   元素.classList.toggle("类名");  //切换类，有就删除，没有就添加。
   ```

5. 获取表单的内容，使用`.value`属性，而不能用innerHTML或innerText。

6. 设置复选框的勾选状态，使用`.checked`属性，用true和false表示。

7. 设置按钮的可点击状态，使用`.disabled`属性，也是true和false。

8. html5支持data-自定义属性，用来替代set和getAttribute方法（因为后者可以随便设置属性，不规范），在标签上，都是data-开头。在DOM中使用dataset的形式获取：

   ```html
   <div class="box" data-id="10">盒子</div>
   <script>
       const box = document.querySelector(".box");
       console.log(box.dataset.id); //输出 "10"，box.dataset是DOMStringMap类型。
   </script>
   ```

# 事件处理

1. 事件就是浏览器或文档中发生的一些特定的瞬间。

2. 事件流描述的是从页面中接受事件的顺序。网页上的元素存在多层的嵌套关系，点击任何一个元素，这个点击事件不仅仅发生在对应的元素上，而且也会影响到它的父节点。

3. 事件，对于所有元素的操作都是事件，可以编写代码对事件做出响应，用户和浏览器的交互行为都依赖于事件。

4. 在事件的响应函数中，this指的是绑定事件的元素。

5. 修改标签对象的事件处理函数：可以在HTML标签中直接修改，也可以在JS代码中获取对象，然后进行修改。

   ```html
   <button id="btn" onclick = "alert('点我干嘛')">我是一个按钮</button>
   <!-- 第一种方法不推荐使用，一般来说，HTML标签的属性应该只包含一些class，id，name就好了。 -->
   <script>
       document.getElementById("btn").onclick = function (){
           alert('点我干嘛');
       };
   </script>
   ```

6. 常见的事件类型：

   1. 鼠标事件，click（单击），mouseenter（移入该区域），mouseleave（移出该区域）。
   2. 焦点事件，focus（获得焦点），blur（失去焦点），和表单有关，获得焦点后可以接收键盘的输入。
   3. 键盘事件，keydown（按下按键），keyup（抬起按键）。
   4. 文本事件，input（用户输入事件，当文本框的内容发生变化时触发）。
   5. 窗口事件，resize（窗口尺寸变化时触发，注册在window上，响应式页面需要使用）。

7. 浏览器加载页面是按照自上而下的顺序，如果在head中写的JS程序想要获取body中的标签，则会获取到null。不过可以将JS程序放在开头，但是要设置在页面加载完毕后执行即可。

8. 页面的加载完毕后，也会触发一个事件。也可以为一个图片设置加载完成事件响应函数。

9. ```js
   window.onload = function(){  //或者window.addEventListener("load", ...)
       //可以将一些js脚本写在这里，此时获取任何元素都不会有问题
       //不过还是推荐将js脚本卸载</body>结束标签前的最后部分。
   };
   ```

10. 还有一个类似的事件，DOMContentLoaded，它是在初始的HTML文档被完全加载解析后触发，此时css，js，图像等资源可能还在获取中，因此它比load事件更早出现。这个要给document对象而非window添加。

11. 追求性能的话，可以将js代码写到后面。为了方便管理使用，可以写到前面。

12. 在事件触发，调用处理程序时，会将事件对象作为第一个参数传入。

    ```js
    document.getElementByID("box").onclick = function (e){
        console.log(e);        //输出事件对象。
        console.log(event);    //也可以直接使用event对象。
        console.log(this);     //在事件处理程序中，this指的就是事件的目标对象，也就是document.getElementByID("box")获得的对象，也就是说谁调用该函数，this就指向谁。
    }
    ```

13. 事件对象中封装了很多有用的信息。event对象中的属性：

    1. type，事件的类型，click，focus等，和addEventListener的第一个参数相同，并非事件对象e的类型。
    2. clientX，clientY，光标相对于浏览器可见窗口左上角的位置。
    3. offsetX，offsetY，光标相对于当前DOM元素左上角的位置。
    4. key，用于按键的值，不提倡使用之前的keyCode。
    5. tagName，标签名，可以是li，p等。

# 事件流

1. 事件流是指，事件完整执行过程中的流动路径。

2. 实际工作中主要使用冒泡，很少使用捕获，因为冒泡是从子元素传递到父元素的，这个符合点击的习惯。

3. 对于事件的传播顺序有两种方案，子元素是包含在父元素中的：

   1. IE方案，向上冒泡流，从子元素到父元素，最后到document。
   2. Netscape，向下捕获流，从父元素到子元素，最后是具体点击的元素。

4. ```js
   document.getElementByID("box");      //从上到下，依次变大。
   document.body;
   document.documentElement;
   document;
   window;
   ```

5. 可以使用元素的addEventListener()，为元素设定对应事件的回调函数，以及是在捕获阶段还是在冒泡阶段处理事件。一个事件可以同时为捕获和冒泡阶段都编写处理函数。

   ```js
   document.getElementByID("box").addEventListener("click",function(){},true); //第三个参数为true表示要在捕获阶段响应该事件。
   document.getElementByID("box").addEventListener("click",function(){},false); //默认情况。
   ```

6. 例子：

   ```html
   <!DOCTYPE html>
   <html>
       <head>
           <title>Example HTML Page</title>
           <style>
               .father {
                   width:500px;
                   height:500px;
                   background-color:blue;
               }
               .son {
                   width:200px;
                   height:200px;
                   background-color:red;
               }
           </style>
       </head>
       <body>
           <div class="father">
               <div class="son"></div>
           </div>
           <script>
               const father = document.querySelector(".father");
               const son = document.querySelector(".son");
               document.addEventListener("click", function(){console.log("document");});
               father.addEventListener("click", function(){console.log("father");},true); //只有这个设置了true，因此如果点击了son元素，会在捕获节点处理father，然后到son后，再在冒泡阶段处理document。综上输出为father,son,document。
               son.addEventListener("click", function(){console.log("son");});
           </script>
       </body>
   </html>
   ```

7. 需要注意的是如果同时给document，father，son三个元素都添加了捕获和冒泡的处理程序，一共6个，则点击1次son，会依次输出 document，father，son，son，father，document。son会出现2次。

8. 事件所处的阶段：捕获阶段→目标阶段→冒泡阶段。这是DOM二级事件规定的事件流。

9. ![1614180274294](JavaScript.assets/1614180274294.png)

10. 事件处理程序的种类：

    1. HTML的事件处理程序，写在HTML标签的属性中。在该处理程序中，this指的就是对应的标签，可以使用使用标签的属性名来使用对应的属性。缺点是HTML和JS耦合在一起了。

       ```html
       <!-- 第一种方法 -->
       <button onclick="function(){console.log(this);}"></button>   <!-- 这里的this指的是button对象。 -->
       
       <!-- 第二种方法 -->
       <button onclick="fun1()"></button>
       <script>
       	function fun1(){
               console.log(this);           //单击按钮，输出的是window对象。
           }
       </script>
       ```

    2. DOM0 级事件处理程序，即将一个函数赋值给元素和某事件对应的特定属性，例如onclick。不能给同一个元素的同一个事件绑定多个处理程序，因为会覆盖。这种事件处理程序只能在冒泡阶段执行。使用简单方便，兼容性最好。

       ```js
       document.getElementByID("box").onclick = function(){};
       document.getElementByID("box").onclick = null;   //忽略该事件，不处理。
       ```

    3. DOM2 级事件处理程序，可以为一个元素的一个事件绑定多个处理程序，可以设置在捕获还是冒泡阶段处理。IE8不支持DOM2级事件处理程序。

       ```js
       document.getElementByID("box").addEventListener("click",function(){
           //设置捕获阶段的处理函数
       },true);    //第一个参数为事件名，第二个为处理程序的函数。第三个参数默认为false,表示在冒泡阶段处理事件。
       document.getElementByID("box").removeEventListener("click",fn);//参数同上，为了方便之后移除，还是不使用匿名函数。可以有第三个参数，来指定捕获还是冒泡阶段。
       ```

    4. IE事件处理程序，只能在冒泡阶段处理，只有IE支持。

       ```js
       document.getElementByID("box").attachEvent("onclick",function(){});//参数含义同DOM2。
       ```

11. HTML级别的处理程序都会被DOM0覆盖掉。对于非IE<9的浏览器，DOM0→DOM2。对于IE8及以下，DOM0→IE。

12. 有时候，需要阻止冒泡，希望事件只在被点击的元素处执行，不继续向上传递。使用`e.stopPropagation()`即可组织事件对象继续传递，处于冒泡和捕获阶段的事件都可以被阻止。不过不会组织当前事件处理程序的执行。

13. 事件冒泡传递可以用来做事件委托，可以一次性个多个同类对象注册事件处理程序，可以减少注册次数。例如给ul注册事件处理程序，这样点击其中任意一个li时，由于冒泡，都会执行到ul注册的事件处理程序。不过需要通过事件对象e，来判断具体是哪个li触发的。

14. 例子如下，用户会点击`li`标签：

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Example HTML Page</title>
        </head>
        <body>
    		<ul id="box">
    			<li id="list1"></li>
    			<li id="list2"></li>
    		</ul>
    		<script>
    			document.getElementById("box").addEventListener("click", function(e){
    				console.log(e); //e为1个PointerEvent对象
    				console.log(e.currentTarget); //ul标签。不过在chrome浏览器的控制台中观察时，就为null了，因为此时的事件e是冒泡结束了的那个，已经不是我们想要的那个了。
    				console.log(e.target); //被点击的哪个li标签
    				console.log(this === e.currentTarget); //结果为true，都是ul标签。
    			});
                // currentTarget属性指向事件当前所在的节点，正在执行的监听函数所绑定的节点。随着事件对象的流动，会改变。
                // target属性指向事件的实际目标对象。在整个事件流中是不会变化的。
    		</script>
    	</body>
    </html>
    ```

15. 鼠标经过事件比较特殊，有2套：

    1. mouseover，mouseout，会有冒泡效果。
    2. mouseenter，mouseleave，没有冒泡效果，更推荐使用。
    3. 除此之外，如果将光标从父元素移动到子元素时，不会触发父元素的leave，但是会触发out，将光标从子元素移动到父元素时，不会触发父元素的enter。

16. 例子：

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Example HTML Page</title>
            <style>
                .father {
                    width:500px;
                    height:500px;
                    background-color:blue;
                }
                .son {
                    width:200px;
                    height:200px;
                    background-color:red;
                }
            </style>
        </head>
        <body>
            <div class="father">
                <div class="son"></div>
            </div>
            <script>
                const father = document.querySelector(".father");
                const son = document.querySelector(".son");
                father.addEventListener("mouseover", function(){console.log("father mouseover");});
                father.addEventListener("mouseout", function(){console.log("father mouseout");});
                son.addEventListener("mouseover", function(){console.log("son mouseover");});
                son.addEventListener("mouseout", function(){console.log("son mouseout");});
                //对于这种情况，从外部移入父元素时，会输出father mouseover。从父元素移入子元素时，会依次输出 father mouseout，son mouseover，father mouseover。最后会出现father mouseover的原因，mouseover会冒泡。
                //从子元素移动到父元素时，会依次输出son mouseout，father mouseout，father mouseover。会出现father mouseout的原因，mouseout会冒泡。从父元素移到外部时，会输出father mouseout。
            </script>
        </body>
    </html>
    ```

17. 如果将上面的over和out替换为enter和leave，则会少去很多事件，更为清晰，因此推荐使用这个：

    1. 从外部移入父元素时，会输出father mouseenter；
    2. 从父元素移入子元素时，会输出son mouseenter；
    3. 从子元素移动到父元素时，会输出son mouseleave；
    4. 从父元素移到外部时，会输出father mouseleave。

18. 有时需要阻止事件的默认行为，例如阻止链接的跳转和表单的提交,，当用户点击表单提交时，需要先判断输入是否合法，如果不合法，需要阻止提交。可以使用事件对象`e.preventDefault`。


# JS执行机制

1. JS最大的特点是单线程，它的诞生是为了解决页面中的交互，以及操作DOM。由于DOM树的操作必须要严格按照顺序执行，因此单线程是适合的。如果JS代码执行时间太长，会造成页面渲染不连贯，产生阻塞的感觉。

2. 但是又有定时之类的需求，为了解决这类问题，H5允许JavaScript创建多个线程，出现了同步和异步的概念。

3. 同步任务都是在主线程中执行，形成一个执行栈，而异步任务是通过回调函数实现的，会放到任务队列中。

4. 一般而言，异步任务有如下三种：

   1. 普通事件，click，resize等
   2. 资源加载，load，error等
   3. 定时器，setTimeout，setInterval等。

5. JS执行机制：

   1. JS引擎读取整个脚本，把所有同步语句都放入执行栈中，依次执行。
   2. 所有的异步语句，都会被交给浏览器处理，因为浏览器可以是多线程的，所以这里没问题。然后继续执行其后的语句。
   3. 在JS执行同步任务的时候，浏览器负责处理异步任务，例如在定时到了以后，将回调函数放到任务队列中，等待JS来取。
   4. 一旦执行栈中的所有同步任务执行完毕，系统会按顺序读取任务队列中的异步任务，并执行，这一步会反复进行，也成为事件循环。

6. 例子：

   ```javascript
   console.log(1);
   console.log(2);
   setTimeout(function(){
       console.log(3)
   },0); //虽然延迟为0，最后输出也是1243。
   console.log(4);
   ```

# 本地存储

1. 随着互联网的发展，基于网页的应用越来越普遍，经常会遇到需要在本地存储数据的情况，H5提出了相关的方法。数据存储在用户浏览器中，设置，读取方便，刷新页面不会丢失。容量较大。分为2类，sessionStorage和localStorage，约5M左右。

2. localStorage可以将数据永久地存储在用户的电脑中，除非手动删除，及时重新打开浏览器也存在。可以多窗口（页面）共享，不同域名的网页默认不共享，需要跨域，不同浏览器之间的不共享。以键值对的方式存储。可以在F12→Application→Storage→Local storage中找到。

3. 例子：

   ```javascript
   //键必须是字符串，值任意，都会被转化成字符串，因为只能存储字符串。
   localStorage.setItem(key, value); //新增或者修改已有的键值对。
   localStorage.getItem(key); //根据键获取值。
   localStorage.removeItem(key); //删除键值对
   localStorage.clear(); //清除所有的键值对
   ```

4. sessionStorage会在关闭浏览器窗口后释放，用法和localStorage相同。

5. 存储对象的方法：

   ```javascript
   const obj1 = {
       uname:"pink",
       age:18,
       gender:"女"
   }
   localStorage.setItem("obj1", obj1); //这里会执行obj1.toString()，将返回值存储键中，之后再读取，就无法还原对象了。
   //此时需要将对象序列化，然后在存储。这里将其转化为JSON字符串。
   localStorage.setItem("obj1", JSON.stringify(obj1));
   //JSON字符串如下，可以看到为键和值都加上的双引号，最外侧为一对单引号。
   '{"uname":"pink","age":18,"gender":"女"}'
   const obj2 = JSON.parse(localStorage.getItem("obj1"));
   obj1 == obj2; //结果为false，但是二者的属性和方法都是一样的。
   ```

# Cookie，session

1. HTTP本身是无状态的，但是有时需要区分不同用户的访问，此时可以在本地存储一些数据，让用户请求时，附加上这些数据来鉴别身份。无状态可以使得浏览器和服务器之间不用保持链接，这样服务器可以同时服务多个浏览器。
2. 浏览器第一次发起HTTP请求后，服务器除了返回网页文件外，还会进行Cookie（就是键值对）设置，也就是Set-Cookie。浏览器接收到Cookie之后，会保存起来，这样浏览器对这个网站后续的每个请求都会附上这个Cookie。由于Cookie是以明文存储的，因此存在安全风险。
3. 之所以称之为Cookie，是因为认为请求的文件是正餐，而附带的这个数据是小点心。
4. Session机制是把原来需要通过Cookie保存的各种数据都保存在服务器端，然后给这些数据一个SessionID，把这个ID发给浏览器，用作通信的身份。这样就无法从浏览器来窃取数据了。
5. session是用来进行保密通信的，因为如果直接将网站的用户名和密码存储在浏览器，容易被黑客获取，因此当浏览器第一次发送给服务器账号密码时，服务器验证成功后，就生成一个随机数的SessionID和Max-age（过期时间），将其作为Cookie发送给浏览器。浏览器收到后，将它们作为Cookie存储，同时将Cookie的结束时间设置为会话的结束时间。这样黑客及时拿到了SessionID也无法从中推断出用户名和密码。实际上这个会话结束时间还可以被服务器延长，例如只要相邻两次登录间隔不太长，Cookie就不会过期。SessionID在被盗后，确实是可以伪装用户的登陆状态。
6. session也有一些问题，例如第一次请求是由A服务器响应，第二次的请求发送到了B服务器，B服务器在收到这个SessionID后，还需要去找A服务器获取对应的信息，会带来性能的开销。
7. CSRF（Cross Site Request Forgery 跨域请求伪造）攻击：A网站设置了一个Cookie，B网站是恶意网站，它在其JS中执行了一个对A网站的请求，此时可能会携带A网站之前设置的Cookie。
8. 每个Cookie都有一个samesite属性：
   1. Strict，只有请求的发起者是同一个网站时才会携带Cookie数据。
   2. Lax，其他网站通过超链接，预加载，表单提交时，允许携带此Cookie数据，其他方式不允许。这是默认级别。
   3. None，没有限制。
9. token是另一种形式的Cookie，不属于浏览器的规范，需要前后端程序来维护。token是服务器端负责加密的，浏览器端一般不大会需要解密。是否携带也是由JS代码来控制的，浏览器不会自动携带，因此可以避免上述CSRF攻击。
10. token还取代了session，其中自然包含了用户的基本信息，临时状态。token使用数字签名来防伪，一般包含用户ID，IP地址，登录时间等信息。服务器使用其私钥对这些数据加密，然后将签名附加在末尾。这样伪造或修改其中任意一段，都会导致解密后对不上。
11. <img src="JavaScript.assets/image-20240729215047211.png" alt="image-20240729215047211" style="zoom: 50%;" />
12. token已经取代了Cookie，称为前端验证的主流方式。

# 浏览器内核

1. 内核有很多模块组成：
2. ![1614005511889](JavaScript.assets/1614005511889.png)
3. 需要根据HTML代码和CSS代码来在内存中生成对应的对象树，然后方便后续的操作。
4. node.js是一个基于chrome v8引擎的js运行环境，可以让js脱离浏览器运行在服务端，能够做到和php等语言相同的功能。
5. V8引擎本身使用了一些最新的编译技术，这使得用Javascript这类脚本语言编写出来的代码运行速度获得了极大提升。V8本身就是一个C++程序。
6. V8引擎包含以下三个部分。
   1. 解析器(parser)，将JS代码解析为抽象语法树AST。
   2. 解释器(interpreter)，负责将AST解释成字节码，解释器也可以解释执行代码。字节码是和平台无关的。
   3. 编译器(compiler)，负责将字节码编译成运行更加高效的机器代码。
7. 浏览器的工作原理：
   1. 首先根据网页地址，获取html文件。
   2. 解析该文件，构建DOM树。
   3. 构建DOM树时，如果遇到CSS，图片和JS文件，会同时发送请求。
   4. CSS和图片不会阻塞DOM树的构建，而JS可能会改变DOM树，因此会等待JS下载，执行完成JS后再继续解析HTML，构建DOM树。因此JS代码的位置十分重要。

# 油猴脚本

1. 元信息，作为注释存在，可以被油猴插件或脚本仓库网站来使用：

   ```javascript
   // ==UserScript==
   // @name         CFD Print  脚本名称，显示在油猴控制界面中
   // @namespace    http://tampermonkey.net/ 用来避免重名，一般用域名
   // @version      1.0  版本
   // @description  try to take over the world! 会显示在GreasyFork中
   // @author       You
   // @match        https://doc.cfd.direct/notes/cfd-general-principles/* 在那些网页上启用该脚本
   // @icon         https://www.google.com/s2/favicons?sz=64&domain=cfd.direct 图标，显示在油猴的控制界面中
   // @grant        none 特殊权限，调用GM_开头的函数时，需要先申请权限。
   // @include     https://doc.cfd.direct/notes/cfd-general-principles/*  和@match差不多，但是@match只支持通配符，这个支持正则表达式，更推荐使用这个。
   // @connect example.com   如果脚本要访问跨域资源，则需要提前声明。
   // @license AGPL-3.0     授权许可信息
   // ==/UserScript==
   ```

2. 打印pdf的例子：

   ```js
   // ==UserScript==
   // @name         CFD Print
   // @namespace    http://tampermonkey.net/
   // @version      1.0 
   // @description  try to take over the world!
   // @author       You
   // @match        https://doc.cfd.direct/notes/cfd-general-principles/*
   // @icon         https://www.google.com/s2/favicons?sz=64&domain=cfd.direct
   // @grant        none
   // ==/UserScript==
   
   (function() { //之所以使用匿名函数，是为了避免从外部访问函数内的东西。
       'use strict';
       let note = document.querySelector("#content > article > div > div.note")
       note.firstElementChild.remove()
       document.body.appendChild(note)
       document.querySelector("#page").remove()
       note.style.marginBottom = 0
       document.body.style.paddingTop = "20px"
       document.body.style.paddingBottom = "20px"
       document.body.style.paddingLeft = "40px"
       document.body.style.paddingRight = "40px"
       document.title = document.title.slice(35).replace(".","-")
       window.print()
   })();
   ```

3. 另一种，可以运行在console中的代码：

   ```js
   divObject = document.querySelector("#content > article > div > div.note"); //要打印的标签，使用F12→Copy→js path来选择
   function printdiv(divObject){
       var headstr ="<html><head><title>打印 div 标签</title></head><body>";
       var footstr ="</body>";
       var newstr = divObject.innerHTML;
       var oldstr = document.body.innerHTML;
       document.body.innerHTML = headstr + newstr + footstr; //设置新场景
       window.print();
       document.body.innerHTML = oldstr; //恢复场景
       return false;
   }
   printdiv(divobject);
   ```