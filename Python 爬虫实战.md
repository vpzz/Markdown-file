1. 爬虫是通过编写程序，模拟浏览器上网，然后让其抓取数据的过程。浏览器获取的是完整的页面，而有用的信息只是很少一部分，爬虫的效率更高。

2. http请求的两种主要方法：①get，明文传输，不安全，参数长度有限制②post，安全，数据没有限制。上传数据多用。

3. 向服务器发送请求本质和上传数据是一样的。都先要吧数据发送到服务器上。

4. http请求头中的connection字段表明是长连接还是短连接。

5. cookies一般用于网站登录，保存在本地。

6. Referer字段是请求发起的地址，即从哪个网页跳转过来的。

7. 爬虫可以分为通用爬虫（搜索引擎，目标不明确，返回内容大部分是用户不需要的）和聚焦爬虫（一般用途，特定网站，可以对内容过滤）。

8. 深度爬虫，可能需要解析js。

9. 爬虫的工作原理步骤：

   1. 确认抓取的URL，有的URL可能被隐藏。
   2. 使用编程语言发送请求。
   3. 解析数据，例如大文件可能被分段等。中间可能会遇到新的URL，还要再回到第2步。
   4. 数据持久化，保存到本地，数据库或文件。

10. Python3内置了一个http请求库，urllib，官方标准库。Python2中为urllib和urllib2，Python3中整合为了urllib。

11. 如果只是用Python3，那么只需要知道urllib库即可。

12. python2.X 有这些库名可用: urllib, urllib2, urllib3, httplib, httplib2, requests

13. python3.X 有这些库名可用: urllib, urllib3, httplib2, requests

14. 两者都有的urllib3和requests, 它们不是标准库. urllib3 提供线程安全连接池和文件post支持,与urllib及urllib2的关系不大. requests 自称HTTP for Humans, 使用更简洁方便。

15. Python3和2的urllib结构不一样：

16. ![1591067050341](Python 爬虫实战.assets/1591067050341.png)

17. urllib和urllib2的主要区别:

    urllib2可以接受Request对象为URL设置头信息,修改用户代理,设置cookie等, urllib只能接受一个普通的URL.
    urllib提供一些比较原始基础的方法而urllib2没有这些, 比如 urlencode

18. httplib 和 httplib2 httplib 是http客户端协议的实现,通常不直接使用, urllib是以httplib为基础 httplib2 是第三方库, 比httplib有更多特性

    httplib比较底层，一般使用的话用urllib和urllib2即可

19. python2.X 中的 urllib.urlopen()被废弃, urllib2.urlopen()相当于python3.X中的urllib.request.urlopen() 

20. 

21. urllib库一共分为4个模块：

    1.  request：主要负责构造和发起网络请求,定义了适用于在各种复杂情况下打开 URL (主要为 HTTP) 的函数和类
    2. error：处理异常
    3. parse：解析各种数据格式
    4. robotparser：解析robot.txt文件

22. 

23. 

24. 

25. Python3中对字符串和二进制数据流做了明确的区分，本文总是Unicode编码，使用string封装。二进制数据流则由bytes类型封装，

26. 编码就是把一个字符用二进制表示出来。字符串就是由很多字符构成的。

27. 

28. 形如：

29. ```html
    &name;
    &#dddd;
    &#xhhhh;    =  \uhhhh
    ```

30. 的一串字符是HTML等语言的转义序列。代表一个字符。第一种是 character entity reference，后接预先定义的 entity 名称，而 entity 声明了自身指代的字符。 例如&lt表示<，&nbsp表示空格。&amp表示&本身。

31. numeric character reference（NCR），数字取值为目标字符的 Unicode code point。以「&#」开头的后接十进制数字，以「&#x」开头的后接十六进制数字。

32. 例如：“中国”这两个字的Unicode编码为4e2d和56fd。可以写作：

33. ```html
    &#x4e2d;&#x56fd;     16进制表示
    &#20013;&#22269;     10进制表示
    ```

34. 使用Python解析NCR：

35. ```python
    from html import unescape
    print (unescape('&#20013;&#22269;&lt;&amp'))
    输出：中国<&
    ```

36. 同时，

37. ```
    &gt;&#62;&#x3e;    都表示的是>这个字符。
    ```

38. 查询Unicode码表（https://www.ssec.wisc.edu/~tomw/java/unicode.html），可以看到之前的那个正则表达式是根据Unicode来匹配字符的。

39. ```
    [\u4e00-\u9fa5]
    ```

40. ![1591094386594](Python 爬虫实战.assets/1591094386594.png)

41. 

# 网络信息爬取

## Request库

1. requests库：目前公认的最好的爬取网页的第三方库。

2. ```python
   import requests as rq
   r = rq.get('http://www.baidu.com')
   print(r.status_code)
   r.encoding = 'utf-8'
   print(r.text)
   ```

3. requests库的方法：

   ```python
   requests.request()  #构造一个请求，是支撑以下各方法的基础方法，下面的方法只不过是封装了一下，变得更适合使用。
   requests.get()   #获取HTML网页的主要方法，对应于HTTP的GET
   requests.head()  #获取网页头信息的主要方法，对应于HTTP的HEAD
   requests.post()  #向网站服务器提交POST请求，对应于HTTP的POST
   requests.put()   #向网站服务器提交PUT请求，对应于HTTP的PUT
   requests.patch   #向网站服务器提交局部修改请求，对应于HTTP的PATCH
   requests.patch() #向网站服务器提交删除请求，对应于HTTP的DELETE
   ```

4. Request对象是在库内部生成的。Response对象包含了爬虫返回的所有内容。

   ```python
   requests.get(url, params = None, **kwargs) #url为拟获取的页面的url链接。可选参数params是url中的额外参数，字典或字节流格式。**kwargs为12个控制访问的参数
   ```

5. get 方法实际上内部是调用request方法。实际上request只有一个方法，不过封装出了几个分支，使用个更方便。

6. Response对象中包含此次请求使用的Requests对象，属性如下。

   ```python
   r.status_code       #HTTP请求的返回状态，200表示成功，404表示失败
   r.text              #HTTP相应内容的字符串形式，即对应的页面内容
   r.encoding          #从HTTP头中猜测的响应内容的编码方式
   r.apparent_encoding #从内容中分析出的响应内容编码方式
   r.content           #HTTP响应内容的二进制形式
   ```

7. encoding字段是根据相应的headers中的charset字段来获得的。如果有该字段，则说明服务器对其内容作了编码的说明，应该按照该编码去解析内容。如果没有该字段，则默认设置为'ISO-8859-1'（单字节编码，支持部分欧洲语言，但是不支持中文）。因此出现了一个apparent_encoding，它是根据内容部分分析得到的编码，更加可靠。

8. 可能产生的异常：

   ```python
   request.ConnectionError   #网络连接错误，例如DNS查询失败，拒绝连接等
   requests.HTTPError        #HTTP错误异常，通用的
   requests.URLRequired      #URL缺失异常
   requests.TooManyRedirects #超过最大重定向次数
   requests.ConnectTimeout   #连接远程服务器超时
   requests.Timeout          #请求URL超时
   #通常使用如下方法来检测是否产生了异常
   r.raise_for_status()  #如果status_code不是200，则产生requests.HTTPError
   ```

9. 爬取网页的通用框架，为了使爬取网页更稳定，可靠

10. ```python
    import requests
    def getHtmlText(url):
        try:
            r = requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return '产生异常'
    if __name__ == '__main__' :
        url = 'http://www.baidu.com'
        print(getHtmlText(url))    
    ```

11. HTTP是基于请求与相应，无状态（请求之间无关联）的应用层协议。使用URL作为定位网络资源的标识。

12. head方法一般用在资源很大的情况下， 先只获取一小部分（此时Response对象的.text是空）。post，put，patch都是向服务器提交数据。

13. patch也是HTTP协议改良后的一个方法。HTTP协议和requests库对应的。

14. patch和put的区别：假设URL位置有一组数据UserInfo，包括UserID，UserName，等20个字段，现在用户修改了UserName，其他不变，如果采用PATCH，则仅向URL提交UserName的局部更新请求；如果采用PUT，则必须将所有20个字段一并提交到URL，未提交的字段将会被服务器删除。PATCH有助于节省带宽。

15. post方法根据用户提交数据的不同，会做相关的转化。

    ```python
    payload = {"key1":"value1","key2":"value2"}
    r = requests.post("http://httpbin.org/post",data=payload)  #像URLpost一个字典，自动编码为表单
    print(r.text)
    {
      "args": {},
      "data": "",
      "files": {},
      "form": {
        "key1": "value1",
        "key2": "value2"
      },
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "23",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.28.1",
        "X-Amzn-Trace-Id": "Root=1-62e8aa48-6ac868ea561c32082c124d22"
      },
      "json": null,
      "origin": "111.42.148.66",
      "url": "http://httpbin.org/post"
    }
    
    r = requests.post("http://httpbin.org/post",data="ABC")  #向URL post一个字符串，自动编码为data。
    print(r.text)
    {
      "args": {},
      "data": "ABC",
      "files": {},
      "form": {},
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "3",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.28.1",
        "X-Amzn-Trace-Id": "Root=1-62e8aacc-097922b33fb5e8d9701c0f23"
      },
      "json": null,
      "origin": "111.42.148.66",
      "url": "http://httpbin.org/post"
    }
    ```

16. post和put的唯一区别是，put是覆盖性的，post是附加性的。

17. requests方法

    ```python
    requests.request(method,url,**kwargs)  #method表示请求方式，一共有7种。GET、HEAD、POST、PUT、PATCH、delete、OPTIONS。**kwargs为访问控制参数，共13个，均为可选项。
    requests.request("GET","http://python123.io/ws",params = {"key1":"value1","key2":"value2"} )
    print(r.url)
    http://python123.io/ws?key1=value1&key2=value2  #params参数会将键值对增加到url末尾。明文参数。
    ```

18. data是向服务器提交信息时使用，参数可以为字典，字节序列或文件对象。提交的内容放在URL对应的地方作为数据存储。

    ```python
    kv = {"key1":"value1", "key2":"value2"}
    r = requests.request("POST", "http://python123.io/ws", data = kv)
    body = "主题内容"
    r = requests.request("POST", "http://python123.io/ws", data = body)
    ```

19. header参数为字典，可以定义HTTP请求头

    ```python
    hd = {"user-agent":"Chrome/10"}
    r = requests.request("POST", "http://python123.io/ws", header = hd)
    ```

20. cookies参数为字典或CookieJar，HTTP会话需要

21. auth参数为元组，支持HTTP认证功能

22. 例子：

    ```python
    pxs = {
        "http":"http://user:pass@10.10.10.1:1234",
        "https":"https://10.10.10.1:4321"
        }     #使用代理可以隐藏用户的源IP地址信息，防止对爬虫的逆追踪。
    fs = {"file":open("data.xls","rb")}  #要传输文件
    jsonkv = {"key1":1,"key2":2}  #要传输的键值对
    r = requests.request("GET", "http://www.baidu.com", proxies = pxs, timeout = 10, files = fs, json = jsonkv)
    #10秒内没有响应则不再等待，直接返回。
    ```

23. allow_redirects：布尔类型参数，默认为True，是否允许重定向

24. stream：布尔类型参数，默认为True，获取内容是否立即下载

25. verify：布尔类型参数，默认为True，是否认证SSL证书

26. cert：指向本地SSL证书路径

27. 爬虫的级别：

    1. 小规模，数据量小，对速度不敏感，只爬取个别网页。使用requests库。

    2. 中规模，数据量较大，速度敏感，一般会爬取网站或系列网站。使用Scrapy库。

    3. 大规模，搜索引擎使用的，需要定制开发。

28. 服务器上的资源有产权归属，爬取有风险。

29. 爬虫带来的问题：对服务器性能骚扰；法律风险；个人隐私泄露。

30. 网络爬虫的限制

    1. 来源审查，根据User-Agent进行限制，只响应浏览器或友好爬虫的访问。

    2. 发布公告，Robots协议，告知所有爬虫本网站的爬取策略，要求爬虫遵守。

       ```python
       #https://www.jd.com/robots.txt显示的内容如下：
       User-agent:*      #所有爬虫都应适用
       Disallow: /?*     #匹配的目录不允许爬取
       DIsallow: /pop/*.html
       Disallow: /pinpai/*.html?*
       User-agent: EtaoSpider  #EtaoSpider爬虫使用
       Disallow: /             #所有目录均不可爬取
       User-agent: HuihuiSpider
       Disallow:/
       ```

31. 默认的请求头部使用Python-requests的UA。可能会被某些网站限制。

    ```python
    r.request.headers
    {	"User-Agent":"python-requests/2.22.0",
    	"Accept-Encoding":"gzip,deflate",
     	"Accept":"*/*",
     	"Connection":"keep-alive"
    }
    ```

32. 使用自定义的UA，大小写都可以。这只会替换headers中的UA键，不会删除其他的键值对。

33. ```python
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,timeout=30,headers = kv)
    r.request.headers
    {'user-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    ```

34. 搜索引擎关键词提交接口：

    ```python
    http://www.baidu.com/s?wd=keyword  #百度
    http://www.so.com/s?q=keyword      #360搜索
    ```


## BeautifulSoup库

1. BeautifulSoup库可以解析HTML为树形结构。解析，遍历的功能库。

2. ```python
   from bs4 import BeautifulSoup   #从bs4库中导入一个类
   ```

3. 创建BeautifulSoup对象是可以使用HTML字符串，也可以使用文件标识符。

4. 其实HTML解析器也可以解析XML文档。

   ```python
   解析器                使用方法                            条件
   bs4的HTML解析器       BeautifulSoup(mk,"html.parser")   安装bs4库
   lxml的HTML解析器      BeautifulSoup(mk,"lxml")          pip install lxml
   lxml的xml解析器       BeautifulSoup(mk,"xml")           pip install lxml
   html5lib的解析器      BeautifulSoup(mk,"html5lib")      pip install html5lib
   ```

5. BeautifulSoup类的基本元素和一个HTML标签一一对应：

   ```python
   <p class = "title">...</p>   #其中标签<p>和</p>成对出现，class为属性，"title"为该属性的值，可以没有属性，...为标签的内容
   基本元素     说明
   Tag          #标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
   Name         #标签的名字，标签<p> </p>的名字是"p"，使用<tag>.name获取
   Attributes   #标签的属性，以字典形式组织，使用<tag>.attrs获取
   NavigableString #标签内非属性字符串，即<>...</>中的字符串，使用<tag>.string获取
   Comment      #标签内字符串的注释部分，一种特殊的Comment类型
   ```

6. soup.a 返回第一个超链接的对象。

7. ```python
   soup.a
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
   soup.a.name
   'a'
   soup.a.attrs
   {'href': 'http://www.icourse163.org/course/BIT-268001',
    'class': ['py1'],
    'id': 'link1'}
   soup.a.string
   'Basic Python'
   ```

8. p标签内还包含一个b标签，但是string并不输出b标签。可以跨越标签层次。

9. ```python
   soup.p
   <p class="title"><b>The demo python introduces several python courses.</b></p>
   
   soup.p.string
   'The demo python introduces several python courses.'
   ```

10. 注释和文本的类型不同，且都不是str类型。

    ```python
    newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
    newsoup.b.string  #结果为 "This is a comment"
    type(newsoup.b.string) # 类型为bs4.element.Comment，并非str类型
    newsoup.p.string  #结果为 'This is not a comment'
    type(newsoup.p.string) #类型为bs4.element.NavigableString
    ```

11. 下行遍历，列表中的元素为Tag类型。

    ```python
    属性           说明
    .contents    #子节点的列表，将<tag>的所有子节点存入到一个list中
    .children    #子节点的迭代类型，用于循环遍历所有子节点
    .descendants #子孙节点的迭代类型，用于循环遍历所有子孙节点
    ```

12. 标签的儿子节点不仅包括标签节点，还包括字符串节点（例如换行）。

13. body 标签中有5个子节点，其中有3个是换行，2个是标签节点。

14. ```python
    soup.body
    Out[37]: 
    <body>
    <p class="title"><b>The demo python introduces several python courses.</b></p>
    <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
    <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
    </body>
    soup.body.contents
    Out[38]: 
    ['\n',
     <p class="title"><b>The demo python introduces several python courses.</b></p>,
     '\n',
     <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
     <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>,
     '\n']
    ```

15. 一个节点只有一个父亲节点。html是最高级标签，它的父节点还是它自己。

    ```python
    属性            说明
    .parent      #节点的父亲标签
    .parents     #节点先辈标签的迭代类型，用于循环遍历先辈节点
    ```

16. 平行遍历，同一个父亲节点，才能平行遍历，互为兄弟节点。可能遍历到字符串。

    ```python
    属性                    说明
    .next_sibling        #按照HTML文本顺序的下一个兄弟节点
    .previous_sibling    #按照HTML文本顺序的上一个兄弟节点
    .next_siblings       #迭代类型，用于遍历按照HTML文本顺序的所有后续兄弟节点
    .previous_siblings   #迭代类型，用于遍历按照HTML文本顺序的所有前驱兄弟节点
    ```

17. 字符串的类型：

    ```python
    type (soup.a.string)
    bs4.element.NavigableString
    ```

18. soup.prettify()在每个标签后边加了一个换行符。方便显示。

19. ```python
    print(soup.a)
    <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
    
    print(soup.a.prettify())
    <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
     Basic Python
    </a>
    ```

20. bs4库使用utf-8编码。

21. find_all，name要严格匹配，如果要查找多个name，可以给一个列表。['a','p'] 如果是True，则打印返回所有的标签。也可以使用正则表达式。

22. ```python
    <>.find_all(name, attrs, recursive, string, **kwargs) #返回一个列表类型，存储查找的结果，元素是tag类型的，可以进行后续的遍历等该操作。其中name是对标签名称的检索字符串；attrs是对标签属性值的检索字符串，可标注属性检索；recursive表示是否对子孙全部检索，默认为True；string是对<>...</>中字符串区域的检索字符串
    import re
    soup.find_all(string=re.compile('python'))
    Out[18]: 
    ['This is a python demo page',
     'The demo python introduces several python courses.']
    ```

23. 由于find_all函数非常常用，因此可以使用如下快捷方法：

    ```python
    <tag>(...)  等价于 <tag>.find_all(...)
    soup(...)   等价于 soup.find_all(...)
    ```

24. 有7个扩展的查找方法：

    ```python
    <>.find()   #搜索，且只返回一个结果，字符串类型
    <>.find_parents() #在先辈节点中搜索，返回列表类型
    <>.find_parent()  #在先辈节点中搜索，返回一个结果，字符串类型
    <>.find_next_siblings #在后续兄弟节点中搜索，返回列表类型
    <>.find_next_sibling  #在后续兄弟节点中搜索，返回一个结果，字符串类型
    <>.find_prev_siblings #在前驱兄弟节点中搜索，返回列表类型
    <>.find_prev_sibling  #在前驱兄弟节点中搜索，返回一个结果，字符串类型
    ```

25. 定向爬虫：只爬取给定的URL。还有一种是根据爬取内容中的链接，继续爬取。

26. 有些内容是通过js生成的，则需要解析js之后才能爬取内容。

27. 定向爬取中国大学排名

28. ```python
    import requests
    from bs4 import BeautifulSoup
    
    def getHtmlText(url):
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    
    def fillUnivList(ulist,html):
        soup = BeautifulSoup(html,'html.parser')
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            ulist.append([tr.div.string,tr('td')[2].string,\
               tr('td')[3].string,tr('td')[5].string])
    
    def printUnixList(ulist,num):
        tplt1 = '{0:{5}^4}{1:{5}^9}{2:{5}^10}{3:{5}^9}{4:{5}^8}'
        tplt2 = '{0:{5}^4}{1:{5}^10}{2:{5}^10}{3:{5}^10}{4:{5}^10}'
        print(tplt1.format('排名','大学','省份','分数','比例',chr(12288)))
        for i in range(num):
            print(tplt2.format(i,ulist[i][0],ulist[i][1],ulist[i][2],ulist[i][3],chr(12288)))
    
    def main():
        ulist = []
        url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
        html = getHtmlText(url)
        fillUnivList(ulist, html)
        printUnixList(ulist, 20)
    main()
    
    　排名　　　　大学　　　　　　　　省份　　　　　　　分数　　　　　　　比例　　　
    　0　　　　　清华大学　　　　　　北京市　　　　　　　95.9　　　　　97.90%　　
    　1　　　　　北京大学　　　　　　北京市　　　　　　　82.6　　　　　95.96%　　
    　2　　　　　浙江大学　　　　　　浙江省　　　　　　　　80　　　　　　96.46%　　
    　3　　　　上海交通大学　　　　　上海市　　　　　　　78.7　　　　　96.76%　　
    　4　　　　　复旦大学　　　　　　上海市　　　　　　　70.9　　　　　97.04%　　
    　5　　　　　南京大学　　　　　　江苏省　　　　　　　66.1　　　　　98.58%　　
    　6　　　中国科学技术大学　　　　安徽省　　　　　　　65.5　　　　　91.30%　　
    　7　　　哈尔滨工业大学　　　　　黑龙江省　　　　　　63.5　　　　　94.32%　　
    　8　　　　华中科技大学　　　　　湖北省　　　　　　　62.9　　　　　92.07%　　
    　9　　　　　中山大学　　　　　　广东省　　　　　　　62.1　　　　　93.45%　　
    　10　　　　东南大学　　　　　　江苏省　　　　　　　61.4　　　　　98.69%　　
    ```

## XML，JSON，YAML

1. 信息标记可以帮助更好地理解信息，标记后的信息才可以正确理解。

2. 国际公认的信息标记方式有三种：XML，JSON，YAML。

3. 历史发展上，先有HTML后又XML，XML是基于HTML发展的一种通用的信息表达形式。

4. 当标签内没有内容时，可以使用一对尖括号表达：

   ```xml
   <name> ... </name>
   <name />
   <!-- 注释 -->
   ```

5. JSON是JavaScript中对面向对象信息的表达形式。是有类型的键值对，这样编程语言可以直接使用。

6. 键值对中，键都是字符串，值如果是数字，则不用带双引号。不能使用单引号。如果一个键对应多个值，使用[，]来组织，实际上是对应一个列表。

   ```json
   {
       "name":["BIT","HIT"]
       "qiantao":{"one":1,"two":2}      嵌套使用，值可以是一个新的json
   }
   ```

7. YAML  YAML Ain't Markup Language   采用无类型的键值对。通过缩进表达包含关系。用-表达并列关系

   ```yaml
   name :
   	newname : BIT
   	oldname : YAS
   ```

8. XML→JSON→YAML 越来越简化。有效信息比例高。

9. JSON一般用在对接口的调用中，缺点是无法体现注释。

10. 使用领域：

    1. XML       Internet上的信息交互与传递

    2. JSON    移动引用云端和节点的信息通信，无注释

    3. YAML    各类系统的配置文件，有注释，易读。

11. 信息提取的两种方法：①先解析成结构化数据，也就是反序列化，再寻找②直接进行字符串匹配搜索。