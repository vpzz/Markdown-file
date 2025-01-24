# 基础

1. PDF（Portable Document Format）是一种电子文档的格式。Portable意味着它在不同的平台上显示是一样的。由Adobe与1991年创立，2008年，成为了一个国际标准，由ISO管理。所有显示需要的内容都保存在一个文件中，这对于传输储存非常方便。
2. PDF可以看作是一个容器，其中包含一些文档级别的数据（例如metadata，书签，安全信息，脚本（可以在特殊事件触发时执行），附件，表格域）和多个页面。除此之外，页面中的图片，字体，色彩空间等资源都是保存在页面外，页面中只记录引用。
3. 虽然看上去表格是属于某些页面的，但是它实际上属于文档级别数据，用户在页面上交互的是表格窗体widget，也就是表格的实例，widget的数据是属于整个文档，而非页面的。
4. 页面被渲染引擎渲染，然后呈现给用户。
5. 字体比较特殊，它并非必须包含（或者说嵌入 embed）在pdf中，如果没有嵌入，则acrobat会在本地文件系统中寻找或使用默认自字体（Helvetica，Times New Roman，Courier，Symbol）。这也是pdf中容易造成传输后显示不同的原因。
6. page包含如下两部分，都使用矢量图形语言描述，也就是postscript语言。
   1. page content，包含静态文字和图片。
   2. annotation，包含浮动的内容，例如表格窗体，注释，多媒体，链接。
7. 渲染引擎在渲染页面时，总是会先绘制page content，然后annotation在列表中的顺序逐个绘制。所有的annotation都叠加在page content上，annotation之间也可以互相叠加。
8. 不同的annotation有不同的显示方式和交互逻辑。
9. page content是高保真的，位置尺寸精准，颜色准确。确保在任何位置显示和打印结果都一样。
10. 矢量图形语言由绘制指令组成，详细规定了线段起点，终点，线性，宽度，颜色等。
11. 注意，annotation也可以包含资源，也就是渲染它所需要的字体，色彩空间等。
12. <img src="Python处理PDF.assets/无标题.png" alt="无标题" style="zoom: 67%;" />

# 基础

1. pypdf是用纯python编写的，安装命令`pip install pypdf`。它还提供了许多额外的库，安装后可以支持更多的操作，例如pypdfimage，pypdfcrypto等。

2. pypdf包含2个核心对象，PdfReader和PdfWriter。

3. PDF有各种版本，PDF2.0的规范有1003页。因此，许多PDF文件没有严格遵循规范。PdfReader有一个参数strict，如果为True，表示如果PDF不符合规范，pypdf将引发异常。如果为False（默认），表示pypdf将尝试宽容并做一些合理的事情，但它会记录一条警告消息。但是PdfWriter没有strict参数，因为不允许用户创建不规范的pdf文件。

4. pypdf可以输出3类消息：

   1. Exception，异常是用户应该明确处理的错误情况。在strict=True下，大多数具有warning级别的log消息将成为异常。这在需要用户修复损坏的PDF的应用程序中非常有用。可以使用try catch捕获异常。大多数PDF文件不符合规范。在这种情况下，pypdf需要猜测在创建PDF文件时可能犯了哪些错误。
   2. Warning，警告是可以避免的问题，例如使用已弃用的类/函数/参数，另一个例子是pypdf缺少功能。此时用户应该调整代码。Warning由warnings模块发出，与日志级别的警告不同。

      ```python
      import warnings
      warnings.filterwarnings("ignore") #忽略警告
      ```
   3. Log，日志是可用于事后分析的消息。大多数时候可以忽略它们。有6个级别，CRITICAL，ERROR，WARNING，INFO，DEBUG，NOTSET。例如，pypdf可以处理的非标准兼容PDF文件，或者导致部分文本无法提取的缺失实现。在某些情况下，日志可能会很嘈杂。可以设置合理的日志级别，减少看到的消息。

      ```python
      import logging
      logger = logging.getLogger("pypdf")
      logger.setLevel(logging.ERROR)
      ```

5. Metadata操作：

   ```python
   from datetime import datetime
   from pypdf import PdfReader, PdfWriter
   reader = PdfReader("example.pdf")
   writer = PdfWriter()
   meta = reader.metadata
   print(meta.title)
   print(meta.author)
   print(meta.subject)
   print(meta.creator)
   print(meta.producer)
   print(meta.creation_date)
   print(meta.modification_date)
   #讲读取的每一页都添加到写入文件中。
   for page in reader.pages:
       writer.add_page(page)
   # 复制旧的metadata
   if reader.metadata is not None:
       writer.add_metadata(reader.metadata)
   # 清空所有metadata
   writer.metadata = {} #或=None
   # 获取当前时间，并格式化
   utc_time = "-05'00'"
   time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")
   # 添加新的metadata到文件
   writer.add_metadata({
           "/Author": "Martin", #key都是以/开头
           "/Producer": "Libre Writer",
           "/Title": "Title",
           "/Subject": "Subject",
           "/Keywords": "Keywords",
           "/CreationDate": time,
           "/ModDate": time,
           "/Creator": "Creator",
           "/CustomField": "CustomField",
       }
   )
   # 保存文件
   with open("meta-pdf.pdf", "wb") as f:
       writer.write(f)
   ```

6. 从页面中提取文本：

   ```python
   from pypdf import PdfReader
   reader = PdfReader("example.pdf")
   page = reader.pages[0]
   print(page.extract_text())
   
   # extract only text oriented up
   print(page.extract_text(0))
   
   # extract text oriented up and turned left
   print(page.extract_text((0, 90)))
   
   # extract text in a fixed width format that closely adheres to the rendered
   # layout in the source pdf
   print(page.extract_text(extraction_mode="layout"))
   
   # extract text preserving horizontal positioning without excess vertical
   # whitespace (removes blank and "whitespace only" lines)
   print(page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False))
   
   # adjust horizontal spacing
   print(page.extract_text(extraction_mode="layout", layout_mode_scale_weight=1.0))
   
   # exclude (default) or include (as shown below) text rotated w.r.t. the page
   print(page.extract_text(extraction_mode="layout", layout_mode_strip_rotated=False))
   ```

7. 可以使用visitor函数来控制要处理和提取页面的哪个部分，也就是对其进行过滤。该函数将为每个运算符或每个文本片段调用。

8. 函数extract_text的参数visitor_text中提供的函数有五个参数：

   1. text：当前文本（尽可能长，最多一行）。
   2. user_matrix：从用户坐标空间（也称为CTM）移动的当前位置得矩阵。
   3. tm_matrix：从文本坐标空间移动到当前位置得矩阵。
   4. font-dictionary：完整字体词典。
   5. font-size：大小（在文本坐标空间中）。

9. 矩阵有六个参数。前四个提供旋转/缩放矩阵，后两个提供平移（水平/垂直）。建议使用user_matrix，因为它适用于所有转换（文本空间/图像空间/形式空间/图案空间）。

10. 获得从文本到用户空间的完整转换，你可以使用mult()函数，txt2user=mult（tm，cm）。字体大小是原始文本大小，受user_matrix的影响。

11. 如果字体未知，字体词典可能为None。如果不是None，它可以包含类似键为/BaseFont，值为/Arial，Bold的键值对。

12. 在复杂的文档中，计算位置可能很难（例如，如果从多个表单移动到页面用户空间）。

# 提取图像

1. 操作图像需要安装pypdfimage库。

2. PDF文档的每一页都可以包含任意数量的图像。文件的名称可能不是唯一的。

   ```python
   from pypdf import PdfReader
   reader = PdfReader("example.pdf")
   page = reader.pages[0]
   for count, image_file_object in enumerate(page.images): #逐个枚举所有图片
       with open(str(count) + image_file_object.name, "wb") as fp: #在文件名前加上count，防止重名
           fp.write(image_file_object.data) #括号内是bytes类型。
   #page.images[0]的类型是ImageFile(name=Image7.jpg, data: 3.4 kB, hash: -7463055775544618449)，包含了名称，文件大小和hash。
   # page.images[0].image的类型是<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=190x63>
   ```

3. 其他一些对象可以包含图像，例如戳记注释，`https://github.com/user-attachments/files/15751424/test_stamp.pdf`这个pdf的右上角的图片就是包含在注释中的。

   ```python
   from pypdf import PdfReader
   reader = PdfReader("test_stamp.pdf")
   im = (
       reader.pages[0]["/Annots"][0].get_object()["/AP"]["/N"]["/Resources"]["/XObject"]["/Im4"].decode_as_image() #类型是<PIL.Jpeg2KImagePlugin.Jpeg2KImageFile image mode=RGBA size=800x600>
   )
   im.show() #展示图片
   # reader.pages[0]的结果可以看作是键值对。
   ```

# 附件

1. PDF文档可以包含附件。附件有一个名称，但它可能不是唯一的。因此，`reader.attachments["attachment_name"]`的值是一个列表。

   ```python
   from pypdf import PdfReader
   reader = PdfReader("example.pdf")
   for name, content_list in reader.attachments.items():
       for i, content in enumerate(content_list):
           with open(f"{name}-{i}", "wb") as fp:
               fp.write(content)
   ```

# 加密解密

1. PDF加密使用不同密钥长度的RC4和AES算法。pypdf支持所有这些，直到PDF-2.0，这是最新的PDF标准。

2. 需要安装额外的依赖，才可以使用AES算法进行加密或解密，推荐cryptography>=3.1。或者可以使用pycryptodome。

3. 加密：

   ```python
   from pypdf import PdfReader, PdfWriter
   reader = PdfReader("example.pdf")
   writer = PdfWriter(clone_from=reader)
   writer.encrypt("123456", algorithm="RC4-40") #设置密码，默认使用RC4算法，但是它已经不太安全了，推荐使用AES。
   with open("encrypted-pdf.pdf", "wb") as f:
       writer.write(f) #保存到文件
   ```

4. 解密：

   ```python
   from pypdf import PdfReader, PdfWriter
   
   reader = PdfReader("encrypted-pdf.pdf")
   
   if reader.is_encrypted: #判断是否加密
       reader.decrypt("my-secret-password")
   
   writer = PdfWriter(clone_from=reader) #克隆内容，密码除外
   with open("decrypted-pdf.pdf", "wb") as f:
       writer.write(f) #保存
   ```

# 合并文件

1. 例子：

   ```python
   from pypdf import PdfWriter
   merger = PdfWriter()
   for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
       merger.append(pdf) #附加整个pdf文件
   
   merger.write("merged-pdf.pdf")
   merger.close()
   ```

2. 更多：

   ```python
   from pypdf import PdfWriter
   merger = PdfWriter()
   input1 = open("document1.pdf", "rb")
   input2 = open("document2.pdf", "rb")
   input3 = open("document3.pdf", "rb")
   
   merger.append(fileobj=input1, pages=(0, 3)) #讲input1文件的前3页添加进来。
   # Insert the first page of input2 into the output beginning after the second page
   merger.merge(position=2, fileobj=input2, pages=(0, 1))#从第2页开始的第一页添加。
   # Append entire input3 document to the end of the output document
   merger.append(input3)#添加整个pdf
   #写入文件，可以用一个来。
   output = open("document-output.pdf", "wb")
   merger.write(output)
   merger.close() #关闭writer
   output.close() #关闭打开的文件
   ```