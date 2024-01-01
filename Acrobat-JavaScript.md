# 基础

1. app对象指的是整个软件。

   ```js
   app.activeDocs;  //返回一个doc对象的数组，包含了当前打开的所有文档。
   this;            //全局的this指的是当前聚焦的文档。
   app.newDoc();    //新建一个PDF文件，默认大小为8x11 inch。
   app.openDoc();   //打开特定PDF文件。路径类型如下："/c/temp/myDoc.pdf" 也可以使用相对路径。
   ```

2. 在打开acrobat软件的时候，会加载系统和用户JavaScript目录中的.js脚本。

3. ```js
   app.getPath("app", "javascript");       //可以获取系统的js目录
   ```

4. 颜色使用一个数组来表示，一共有5种形式，格式为：[类型，数据]，例如：

   ```js
   [ "T" ]               //透明
   [ "G", 0 ]            //灰度模式，0表示黑色,1表示白色,0.5表示中性灰。
   [ "RGB", 1,0,0 ]      //RGB模式，表示红色，color.red
   [ "CMYK", 1,0,0,0 ]   //CMYK模式，表示青色。
   //数据都在0-1之间。
   ```

5. console对象时JS控制台，运行脚本或者出错时进行调试。

   ```js
   console.show();       //显示控制台
   console.hide()        //关闭控制台
   console.clear();      //清空控制台
   console.println();    //打印内容
   ```

6. Doc对象指的就是一个个打开的PDF文档，通常使用this或者app.activeDocs[i]获得。

   ```js 
   myDoc.saveAs(myDoc.path);      //另存为PDF文件
   myDoc.closeDoc(true);          //关闭对应的PDF。
   this.info;                     //获取信息对象，可以进而获取如下信息：Title, Author,Subject,Keywords,Creator,Producer,CreationDate
   this.mouseX;                   //获取当前鼠标相对于页面的的位置。
   this.numPages;                 //页面总数。
   this.path;                     //获取当前文件的设备无关路径。
   this.pageNum；                 //读取或设置当前页面的页码，从0开始。
   this.zoom;                     //设置缩放比例，从8.33-6400%，不输入%。
   this.zoomType = zoomtype.fitW; //适应宽度缩放。 
   ```

7. 一系列操作页面的函数：

   ```js
   deletePages    insertPages     extractPages      replacePages
     movepage        newpage        scroll
   ```

8. 数据持久化，需要使用到global对象。

9. 创建全局属性，

   ```js
   global.radius = 8;        //不加global定义的变量，默认是属于对应的文件，在其他文件中不能访问到。全局变量在任何地方使用的时候都要加上global。
   delete global.radius;     //删除全局变量。
   ```

10. 持久化的数据都存放在了用户文件夹中的glob.js中。在下次程序打开时，又被加载。只能持久化字符串，数值，bool型数据。有2-4KB的大小限制。

    ```js
    global.radius = 8;  
    global.setPersistent("radius", true);    //设置持久化，第二个参数如果为false，则表示移除持久化。
    ```

11. 数据持久化的操作，只有在关闭软件时，才会修改对应的文件。

12. 经验证，windows上数据实际存储在了用户文件夹中的JSCache/GlobData文件中。格式如下：

    ```
    <</global [/c <<	/myVariable [/d 1.000000]
    	/newp [/d 32.000000]
    >>]
    >>
    ```

13. 上面一共是存储了两个量，global.myVariable和global.newp。该文件夹中的另一个文件GlobSettings，存储了对应的持久化变量储存时的文档，为了安全性考虑。

14. global还有个subscribe函数，可以为全局变量注册更新器，当该变量的值发生变化时，自动调用对应的函数。
