

# 音视频基础

1. 播放视频的原理如下：
2. <img src="FFMPEG使用指南.assets/image-20210321105802788.png" alt="image-20210321105802788" style="zoom: 67%;" />
3. 文件是用封装格式将视频流和音频流封装起来的，有的里边音频流不止一个，有的还有字幕流。封装的过程称为mux，使用的是复用器muxer。与之相反的是解复用demux过程。
4. 解复用完后的数据仍然是压缩的，还需要进行解码。解码后的内容，显卡和声卡才能识别。
4. 音视频同步是避免出现音画不同步的情况。
5. 工具：
   1. 封装格式查看：elecard format analyzer
   2. 视频编码数据：elecard stream eye
   3. 视频像素数据：YUV Player
   4. 音频采样数据：Adobe Audition
7. 封装格式（又称为容器）是和文件的扩展名关联的，作用就是将视频码流和音频码流存储到一个文件中，可以看做是打包。常见的封装格式：

   ```
   名称        推出机构             目前使用领域
   AVI      Microsoft Inc.          BT下载影视
   MP4          MPEG               互联网视频网站
   TS           MPEG             IPTV，数字电视，直播
   FLV        Adobe Inc.          互联网视频网站
   MKV       CoreCodec Inc.       互联网视频网站
   RMVB    Real Networks Inc.       BT下载影视
   ```
7. TS格式和其他封装格式最大的区别就是它不包含文件头，从任意一段开始都可以播放，因此它常用于直播和电视传输。
9. FLV封装格式中，如果文件头损坏，整个视频就不能播放了。
10. <img src="FFMPEG使用指南.assets/image-20210321110828338.png" alt="image-20210321110828338" style="zoom: 50%;" />
11. 视频编码是指将RGB或YUV像素点数据压缩为视频码流，主要是为了降低体积。视频编码性能决定了整个音视频技术的好坏。

    ```
    名称           推出机构       推出时间   目前状态
    HEVC(H.265)  MPEG/ITU-T       2013      研发中
    H.264        MPEG/ITU-T       2003      各个领域
    MPEG4        MPEG             2001      不温不火
    MPEG2        MPEG             1994      数字电视
    VP9          Google           2013      研发中
    VP8          Google           2008      不普及
    VC-1         Microsoft Inc.   2006      微软平台
    ```
12. 一张画面就当做一个NALU来存储，所有的NALU构成一个链表。压缩效率在100倍以上。文件后缀一般为.h264。
14. ![image-20210321111207743](FFMPEG使用指南.assets/image-20210321111207743.png)
15. 一共有三种帧类型，IPB，I帧是独立存储，不依赖其他帧，P帧是基于I帧的运动矢量，解码依赖于I帧，B帧是双向预测，前后都依赖。这种存储方式，可以将不动的背景的体积压缩的特别小。
15. 音频编码是将音频采样数据PCM压缩成音频码流，也是为了减小体积。音频本身占的体积较小，即使是不压缩的音频数据WAV，1分钟的体积大约在10M左右。

    ```
    名称  推出机构        推出时间    目前状态
    AAC   MPEG            1997      各个领域(新)
    AC-3  Dolby Inc.      1992      电影
    MP3   MPEG            1993      各个领域(旧)
    WMA   Microsoft Inc.  1999      微软平台
    ```
18. 大部分的视频都是使用AAC格式，AC-3主要用在电影中，声道比较多。同等质量下，MP3比AAC占用的体积更大点。
20. <img src="FFMPEG使用指南.assets/image-20210321232021538.png" alt="image-20210321232021538" style="zoom:50%;" />
21. 视频流解码后就得到视频像素数据，保存了每个像素点的颜色值，常见的有RGB24，RGB32，YUV420P，YUV422P等。最常用的就是YUV420P。使用YUV Player播放。
22. Y是亮度数据，UV为色度数据，利用了人眼对亮度敏感，但是对色度不敏感的特点，对色度采取较为严格的压缩。
23. YUV数据的存储是先存储整幅画面的Y数据，然后是U，最后是V数据。U和V的数据量都只有Y的1/4，相当于长宽都变为原来的一半。
25. YUV数据是没有文件头信息的，因此需要设置分辨率，像素格式和帧率，例如640x360，YUV420p，30fps。通过分辨率和像素格式来确定一帧的数据量，然后根据像素格式来拆分一帧内的Y，U，V的各个分量。
25. RGB数据存储的时候是逐个像素存储，每个像素依次存储RGB数值。8bit量化。.bmp文件就是未压缩的RGB数据。
26. 音频采样数据(PCM)保存了音频的波形，量化一般为16bit，也成为音频的分辨率。这种数据也是没有文件头的，需要设置采样率和声道，量化。
27. 44.1kHz的采样率正好超过人耳的20kHz上限的两倍。常见的采样频率有44.1k或48kHz。立体声音频一般有2个通道，要分别处理。
28. <img src="FFMPEG使用指南.assets/image-20210321233259109.png" alt="image-20210321233259109" style="zoom:50%;" />

# 视频编码

1. 1080p表示逐行扫描(progressive scanning)，1080i表示隔行扫描(Interlace Scanning)，也成为交错扫描。
2. 早期的显像管时代，电子枪从上到下，从左到右，扫描一遍，称为一场。后来开发了隔行扫描技术，就是第一帧扫描奇数行，下一帧扫描偶数行，然后依次循环。这样同样的带宽可以支持更高的清晰度了。
3. 现在来看，网络视频都是逐行扫描的，电视中是隔行扫描的。
4. 如果只是为了转封装格式，可以直接复制音视频流的。当新的封装格式不支持原来的编码格式时，就必须得进行视频转码了。
5. 码率直接决定了视频的大小，并且很大程度上决定视频的质量。
6. 考虑到网站的存储空间，带宽和用户的带宽，直播网站有码率限制，视频网站也有一根二压线（不满足该要求的视频会被进行二次压制，质量就不能保证了）。
7. 下面是B站的二压线，视频码率指的是整个文件的平均码率，=文件大小/时间。对于编码率的情况，峰值码率可能会很高。
8. <img src="FFMPEG使用指南.assets/image-20210321215434146.png" alt="image-20210321215434146" style="zoom:50%;" />
9. H.264实际上和AVC是一样的，是两个组织颁布的同一个标准，不同的名字而已。
10. <img src="FFMPEG使用指南.assets/v2-45a5e855ac5c057415d862db506c57fd_720w.jpg" alt="img" style="zoom: 80%;" />
11. GOP，每一组IPB帧的序列一共包含了多少帧，或者说一个I帧之后多久才会出现下一个。I帧也被称作关键帧。该值越大，视频里模拟出来的PB帧就越多，同码率下的视频质量就越高，因为压缩率高了。
12. 三种控制视频码率的方法：
    1. CBR 固定码率，全程码率固定，文件大小可以预期，编码压力小，直播常用。缺点是不能根据场景的复杂度动态调整码率，质量不能保证。
    2. VBR 可编码率，需要设置一个目标码率，编码中会为简单的场景分配更少的码率，为复杂的场景分配更高的码率。VBR可以选择渲染两遍 2-pass，可以更精确地控制质量。
    3. CRF 固定质量，需要给定一个质量值，该值越低，质量越高，码率也是动态变化的。以画质为目标的。
    4. ABR 平均码率，相当于是码率波动更小的VBR。
    5. CQP 固定量化模式，相当于低级的CRF。
13. x264，NVENC（NVIDIA独显），QuickSync（Intel核显）是实现了H264标准的编码器。编码器为了方便使用，定义了许多预设preset，
14. <img src="FFMPEG使用指南.assets/image-20210321221204087.png" alt="image-20210321221204087" style="zoom: 67%;" />
15. 预设越快，渲染时间越短，同码率下的画质就越差。由于没有充足的时间来编码，直播的预设比较快，因此在相同的码率下，直播的画质没有视频的好。预设这一个选项就可以决定80%的画质了。
18. 显卡上有专门用来进行视频编解码的硬件的，和游戏使用的流处理单元不是一回事。因此不会影响游戏的性能。
19. 电影或者说拍摄出来的视频即是只有24帧，也不会觉得卡顿，而电脑游戏帧率低于60，就会觉得卡顿，原因如下：
    1. 电影的每一帧都是带有动态模糊的，而电脑渲染的视频不是，游戏如果不打开动态模糊的话，就会发现每一帧都是锐利的。电影中每一帧实际上是一段时间的影像，游戏中每一帧是一个时刻的影像。动态模糊使得每一帧都衔接连贯。人眼的视觉暂留可以补全中间缺少的内容。游戏的动态模糊和自然界真实的动态模糊不同。特效电影中的特效一般是逐帧修改的，动态模糊比游戏的算法好得多。
    2. 电影的帧间隔十分稳定，游戏由于是实时渲染的，如果场景复杂，导致某一帧的渲染超时，帧间隔就不稳定。开启垂直同步可以使帧生成时间稳定，但是会牺牲交互性。游戏接受玩家的操作也会变慢。一般来说，玩家的操作要3-5帧才会反映到画面中。人对操作的延迟反应大约在100ms左右。因此即使显示器只有60帧，画面的高刷新率也是有用的，是可以更快地将玩家的操作反映到显示器上。
    3. 游戏的操作性强，导致玩家对卡顿更加敏感。
20. 电影的帧率也不能太低，人眼的视觉暂留下限支持16帧。现在的数字电影大多为30帧拍摄。

# FFMPEG使用

1. 官网提供三种版本：

   1. 静态链接的，只包含三个体积很大的.exe程序。
   2. 动态链接的，除了3个体积较小的.exe程序外，还有一些dll库。
   3. 开发版本，只有头文件(.h)和导入库文件(.lib)。

2. 下载的压缩包解压之后获得bin目录和doc目录，bin目录内只有三个文件，ffmpeg.exe，ffprobe.exe，ffplay.exe。

3. ```shell
   ffmpeg -i input.mkv output.mp4     #-i后面为输入文件，将.mkv封装格式转化为.mp4格式。
   -y #参数可以在需要用户做选择时，始终选择yes，这样就会覆盖掉已有的重名文件。
   ```
   
4. ffprobe可以探测文件的格式信息

   ```
   .mkv文件的信息
      Input #0, matroska,webm, from 'Friends.S01E02.The Sonogram At The End.mkv':
        Metadata:
          encoder         : libebml v0.7.4 + libmatroska v0.7.6
          creation_time   : 2006-05-23T11:39:28.000000Z
        Duration: 00:24:21.80, start: 0.000000, bitrate: 1009 kb/s
          Stream #0:0: Video: mpeg4 (Simple Profile) (XVID / 0x44495658), yuv420p, 512x384 [SAR 1:1 DAR 4:3], 23.98 fps, 23.98 tbr, 1k tbn, 23.98 tbc (default)
          Stream #0:1: Audio: mp3, 48000 Hz, stereo, fltp, 32 kb/s (default)
          Stream #0:2(chi): Subtitle: dvd_subtitle, 720x480 (default)
          Stream #0:3(eng): Subtitle: dvd_subtitle, 720x480
          Stream #0:4(chi): Subtitle: dvd_subtitle, 720x480
          
   转码后为.mp4格式的信息
      Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'output.mp4':
        Metadata:
          major_brand     : isom
          minor_version   : 512
          compatible_brands: isomiso2avc1mp41
          encoder         : Lavf58.45.100
        Duration: 00:24:21.81, start: 0.000000, bitrate: 849 kb/s
      Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 512x384 [SAR 1:1 DAR 4:3], 717 kb/s, 23.98 fps, 23.98 tbr, 11988 tbn, 47.95 tbc (default)
   Metadata:
        handler_name    : VideoHandler
      Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 128 kb/s (default)
          Metadata:
            handler_name    : SoundHandler
   ```

5. ffmpeg -codecs可以查看支持的所有编解码器。不过一般的视频都是mp4封装，H264视频编码和AAC音频编码。

6. 音频转码和参数设置：

7. ```shell
   ffmpeg -i input.flac -acodec libmp31ame -ar 44100 -ab 320k -ac 2 out.mp3
   -acodec #指定输出文件的编解码器，如果不输入，也可以根据输出文件名的MP3后缀探测，自动选取该编解码器libmp3lame。这会导致重复地解码编码。
   -ar     #采样率，如果不手动指定，则使用音频原来的采样率。常用的有48kHz和41.1kHz，如果和原来不一致，则会进行重采样。
   -ab     #比特率，默认为128k    也可以用 -b:a 128k  替代
   -ac     #声道数，1为单声道，2为双声道立体声，默认采用原音频的声道数
   ```

8. 视频转码和参数设置：

10. ```shell
    ffmpeg -i in.webm -s 1920x1080 -pix_fmt yuv420p -vcodec libx264 -preset medium -profile:v high -level:v 4.1 -crf 23 -acodec aac -ar 44100 -ac 2 -b:a 128k out.mp4
    -s        #视频分辨率大小
    -pix_fmt  #像素格式，颜色空间 yuv420p是最常见
    -vcodec   #是h264的软件编码器，也可以用-c:v libx264来代替。
    -acodec   #可以直接写AAC，也可以用-a:v aac来代替。
    -preset   #是编码器功能的预设，默认是medium，一般在录制视频时，使用veryfast，以空间换效率。在压制视频时，用时间换空间。
    -crf      #恒定速率因子模式，画质均衡，但是无法对码率进行控制。范围是0-51，默认是23，数值越小，质量越高。通常在18-28之间选择。
    -r 30     #设置帧率为30，帧率的改变不会修改视频的时长，只会进行抽帧和插帧的操作。此选项不能和copy共同使用。
    -f flv    #设置输出封装格式为flv，一般不会使用该选项，而是让程序根据输出文件的后缀名来判断封装格式。
    ```
    
10. 10个编码器预设 ：

    ```
    -preset选项的参数
    ultrafast superfast veryfast faster   fast
    medium    slow      slower   veryslow placebo
    ```

12. 所谓码率控制就是决定为每一个帧画面分配多少bit的空间来存储。

14. ffmpeg一共支持3种码率控制模式：

    1. -qp 恒定量化器模式，通过算法将画质转化为数字，每一帧的画面都对应一个数字。范围0-51，0为无损。一般不使用这种模式，除非要无损压制视频。
    2. -crf 恒定速率因子模式，其实就是一个浮动的qp模式，根据人眼对不同画面的敏感度，相应地提高降低码率，因此画质的变化几乎看不出来。这是最适合大众的码率控制模式，最常用。
    3. -b 固定目标码率模式，视频的码率恒定和文件体积都是确定。适用于对码率和体积有限制的情况，不常用。

15. 一般的视频网站都会二次转码。现在的网络视频基本都是平均比特率ABR的方式。

16. 提取音频或视频，如果不显式声明copy的话，默认是不copy的。如果使用了这个copy参数，则输出文件编码应该和原视频容器内的编码相同。这样就不用进行重复地编解码了，速度大大加快。

17. ```shell
    ffmpeg -i input.mp4 -vcodec copy -an output.mp4
    ffmpeg -i input.mp4 -acodec copy -vn output.m4a
    -an #是禁用音频，也就是提取视频。
    -vn #是禁用视频，表示提取音频。如果是mp4→mp3，不用-vn参数也是可以的，因为mp3容器默认只有音频流。
    -vcodec copy #表示使用原视频的编码器。
    -acodec copy #表示使用原音频的编码器。
    
    ffmpeg -i a.m4a -i v.mp4 -c copy output.mp4 #将之前提取的音视频合并为一个视频。
    -c #后面接编码器，copy表示复制原来的流，不用进行重新的解码编码。
    ```
    
24. 对于有多个音轨的视频，加上 -map 对应的流序号即可。
    
    ```
    Stream #0:2[0x81]:Audio:ac3,48000Hz,5.1,s16,384 kb/s
    Stream #0:3[0x82]:Audio:ac3,48000Hz,5.1,s16,384 kb/s
    Stream #0:4[0x80]:Audio:ac3,48000Hz,5.1,s16,448 kb/s
    
    -map 0:3
    ```
    
26. 一般视频中的音频流编码都是aac格式的，如果不进行转码，直接copy流，则导出的为m4a格式的文件。如果要导出mp3格式的文件，则应去掉copy选项。ffmpeg会自动选取对应的编码器。

19. 截取音视频，一般都应加上-c copy，复制流，不进行重新编解码。

    ```shell
    ffmpeg -i input.mp3 -ss 0:0 to 1:20 -acodec copy output.mp3
    -ss -to #表示起始和终止时刻，单位是秒，格式有 00:00:10 00:10 10 三种格式，都表示第10秒
    -t      #可以指定截取时长。配合-ss使用,表示从ss开始截取-t的时间。如果只有-t,ss默认为0。
            #如果搭配 -sseof 和-t表示从末尾开始截取固定时长。
    ```

20. 将-ss参数放到-i前，ffmpeg会启用关键帧技术，效率更高，不过时间戳可能会乱，再加上-copyts，时间戳就准了。（经过试验，加上-copyts反而不会输出正确的文件）

    ```shell
    ffmpeg -i in.mp4 -ss 00:01:00 -to 00:01:10 -c copy out.mp4
    ffmpeg -ss 00:01:00 -i in.mp4 -to 00:01:10 -c copy out.mp4
    ffmpeg -ss 00:01:00 -i in.mp4 -to 00:01:10 -c copy -copyts out.mp4
    ```

21. 拼接不同的音视频文件，两种情况：

    1. 不同段的音视频编码相同，一般都为h264和aac。可以直接按照下面的代码进行拼接。
    2. 不同段的音视频编码不同。需要先调整为同一个音视频编码，再进行拼接。

26. 最好将各段视频都转封装为ts格式，然后进行拼接，再转封装为mp4格式。

27. 使用ts流方法进行合并时，视频的分辨率可以不同，但是编码格式要统一，音频的编码格式和参数都要统一。

28. ```shell
    ffmpeg -i 01.mp4 -vbsf h264_mp4toannexb -c copy 01.ts   #因为分离某些封装格式中的h264码流时，需要首先写入sps和pps，否则会导致分离出来的码流无法播放，使用该比特流过滤器可以完成该工作。
    
    ffmpeg -i "concat:01.ts|02.ts" -c copy output.mp4 #拼接或合并
    ffmpeg -f concat -i tslist.txt -c copy output.mp4
    #要求ts.list.txt为如下格式:
    file '01.ts'
    file '02.ts'
    ```

25. 提取码流数据，并使用ffplay播放。

    ```shell
    ffmpeg -i test.mp4 -pix_fmt yuv420p test.yuv    #设置像素格式为yuv420p。不指定的话会使用mp4文件内的像素格式。
    ffplay -pixel_format yuv420p -video_size 1280x720 -framerate 24 test.yuv #可以换成-pix_fmt
    
    ffmpeg -i test.mp3 -ar 48000 -ac 2 -f s16le test.pcm  #16位量化，小端存储 signed
    ffplay -ar 48000 -ac 2 -f s16le test.pcm
    ```

26. 将视频中的一部分保存为图片：

    ```shell
    ffmpeg -i test.mp4 -f image2 -ss 00:00:02 -vframes 1 test.jpg   #截取第2秒的那一帧
    ffmpeg -i test.mp4 -t 5 -r 15 frame%03d.jpg   #将前5秒的视频，按照帧率为15输出成一系列图片，名称为frame001.jpg frame002.jpg 等宽格式，左侧补零。
    ffmpeg -f image2 -i frame%03d.jpg -r 15 out.mp4   #将一系列图片按照帧率15合并为一个视频。
    ffmpeg -i test.mp4 -t 5 -r 25 image.gif   #输出一个帧率25的gif。GIF的色彩空间会比较小。256色。
    ffmpeg -f gif -i image.gif output.mp4     #将GIF文件转化为视频。
    ```

# FFMPEG编程

## 配置

1. 下载shared开发包，包含三个文件夹，bin(动态库) lib(导入库) include(头文件)。分别在VS中包含进去，如果是新建的空项目是没有c/c++卡片的，需要新建一个c或c++文件才可以。：

2. 头文件：

3. ![image-20210327213718373](FFMPEG使用指南.assets/image-20210327213718373.png)

4. 导入库目录

5. ![image-20210327213822452](FFMPEG使用指南.assets/image-20210327213822452.png)

6. 导入库文件，用到了哪个库就输入哪个。

7. ![image-20210327214044418](FFMPEG使用指南.assets/image-20210327214044418.png)

8. 动态库可以复制到.exe的目录下，也可以进行如下配置：

9. ![image-20210327220524501](FFMPEG使用指南.assets/image-20210327220524501.png)

10. 选择项目配置是要注意，如果库文件是64位的，那么程序也要选择为64位的。如果库文件是32位的，程序可以是32或64位的。

11. 在项目的属性也选中x64，然后设置各种上面的目录。

12. ![image-20210327220758460](FFMPEG使用指南.assets/image-20210327220758460.png)

13. 生成器也要选择对应的x64。

15. 测试环境代码：

    ```c
    //C语言环境
    #include <stdio.h>
    #include "libavcodec/avcodec.h"
    
    int main() {
    	printf("%s",avcodec_configuration());
    	return 0;
    }
    
    //C++环境
    #define __STDC_CONSTANT_MACROS  //两个宏__STDC_CONSTANT_MACROS和__STDC_CONSTANT_MACROS，是为在C++中使用C99定义的一些宏，它们定义在<stdint.h>中。这些宏，如：UINT8_MAX, INT64等。虽然这两个宏不是C++标准的内容，但是被不只一种实现采用。当前在C++11和C11已经不再检测这个宏了，vs2022中默认使用c++14。
    #include <stdio.h>
    extern "C" {
    #include "libavcodec/avcodec.h"    //必须要将头文件包含在extern "C" 中，否则会报链接错误
    }
    
    int main() {
    	printf("%s",avcodec_configuration());
    	return 0;
    }
    ```

15. 编译时出现以下警告，主要原因是该文件的编码不对，可以在文件→高级保存选项中保存为Unicode 代码页-1200。而VS2017隐藏了“高级保存选项”命令。可以通过工具→自定义→命令，调出来。

    ```c
    warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    ```

16. <img src="FFMPEG使用指南.assets/image-20220528222840187.png" alt="image-20220528222840187" style="zoom:80%;" />

17. FFMPEG本身是用纯C写的，如果要在cpp文件中引入对应的头文件，需要用extern "C"{   }包裹起来。

18. SDL库封装了视音频底层的交互操作，跨平台的。FFMPEG解封装，解码，得到YUV数据，然后由SDL将YUV数据绘制到屏幕上。

19. ![image-20210327223029594](FFMPEG使用指南.assets/image-20210327223029594.png)

20. 由于ffmpeg的程序是在linux下开发的，因此行尾都是\n，而Windows下的main.c文件行尾为\r\n。所以会提示如下：

22. <img src="FFMPEG使用指南.assets/image-20210328123358236.png" alt="image-20210328123358236" style="zoom:80%;" />

## 类库

1. 一共有8个类库：

   ```c
   avcodec     //编解码
   avformat    //封装格式处理
   avfilter    //滤镜特效处理
   avdevice    //各种设备的输入输出
   avutil      //工具库，大部分的库都需要这个库的支持
   postproc    //后加工
   swresample  //音频采样数据格式转换
   swscale     //视频像素数据格式转换
   ```

2. FFMPEG常见工作流程

4. <img src="FFMPEG使用指南.assets/image-20210327224055880.png" alt="image-20210327224055880" style="zoom:80%;" />

4. 流程中的函数：

   ```c
   av_register_all()            //注册所有组件,初始化的过程
   avformat_open_input()        //打开输入文件
   avformat_find_stream_info()  //获取文件信息
   avcodec_find_decoder()       //查找解码器
   avcodec_open2()              //打开解码器
   av_read_frame()              //从输入文件中读入一帧的压缩数据
   avcodec_decode_video2()      //解码一帧的压缩数据
   avcodec_close()              //关闭解码器
   avformat_close_input()       //关闭输入视频文件
   ```

5. AVPacket是编码后的一帧的数据，AVFrame是解码后一帧一帧的画面。

7. 使用到的结构体：

8. <img src="FFMPEG使用指南.assets/image-20210327230341729.png" alt="image-20210327230341729" style="zoom:67%;" />

8. 常用的结构体：

   ```c
   AVFormatContext  //封装格式上下文结构体，也是统领全局的结构体，保存了音视频文件封装格式的相关信息。
   AVInputFormat    //指明了文件用的是什么封装格式,每种封装格式(例如flv,mp4,mkv等)对应一个结构体。
   AVStream         //流结构体数组，音视频文件中每个流对应于一个结构体，一般0号为视频，1号为音频。
   AVCodecContext   //编码器上下文结构体，保存了音视频编解码相关的信息。
   AVCodec          //每种音视频编解码(例如H.264,H.264等)其对应于一个结构体。
   AVPacket         //存储一帧解码前压缩的数据。
   AVFrame          //存储一帧解码后像素或音频采样数据。
   ```

10. 结构体的成员：

12. ![image-20210327231002766](FFMPEG使用指南.assets/image-20210327231002766.png)

13. ![image-20210328015529681](FFMPEG使用指南.assets/image-20210328015529681.png)

14. ![image-20210328022138884](FFMPEG使用指南.assets/image-20210328022138884.png)

15. FFMPEG中主要的结构体可以分为以下几类：

    1. 解协议：AVIOContext，URLProctocol，URLContext，每种协议都对应一个URLProtocol结构体。文件也被看做是一种协议file。
    2. 解封装：AVFormatContext主要存储视音频封装格式中包含的信息；AVInputFormat存储输入视音频使用的封装格式。每种视音频封装格式都对应一个AVInputFormat 结构。
    3. 解码：AVStream表示一个视频/音频流数据；它的相关信息保存在对应的AVCodecContext，每个AVCodecContext中对应一个AVCodec，包含该视频/音频对应的解码器。每种解码器都对应一个AVCodec结构。
    4. 存数据：AVPacket→AVFrame。每个结构包含一帧视频或几帧音频。

16. timebase 时基指的是用来记录每帧画面应该播放的时刻的，他是作为一个单位。每一帧中只要记录在多少个单位播放即可。

15. pts 显示时间戳，表示该帧应该在什么时刻被显示。整数，单位为时基。

16. av_register_all函数是所有基于ffmpeg的应用程序中第一个被调用的函数，只有调用了该函数，才能正常使用ffmpeg的各项功能，如复用/解复用器，编码/解码器，以及各种协议等等。 现在的av_register_all()是ffmpeg的过时函数(deprecated)。ffmpeg5.0中这个函数已经被删除了。

17. AVFormatContext常见的成员介绍：

    ```c
    typedef struct AVFormatContext {
        const AVClass *av_class;
        const struct AVInputFormat *iformat; //输入文件的封装格式，解封装会用到，由avformat_open_input()设置。
        const struct AVOutputFormat *oformat; //输入文件的封装格式，封装会用到，必须在调用avformat_write_header()之前设置。
        void *priv_data; //封装格式相关的私密数据。
        AVIOContext *pb; //I/O相关的上下文。
        int ctx_flags; //流信息。
        unsigned int nb_streams; //流的数量。
        AVStream **streams; //结构体指针数组，使用avformat_new_stream()创建新的流。
        char *url; //输入或输出的链接。
        int64_t start_time; //文件第一帧的时间，参考AV_TIME_BASE fractional seconds。
        int64_t duration;  //文件总时间长度。
        int64_t bit_rate; //总的流码率,不要手动设置，ffmpeg会自动根据文件大小和时间计算。
        unsigned int packet_size; //一帧码流包的大小。
        int max_delay;
        int flags; //影响复用/解复用器的行为的标志。AVFMT_FLAG_*的形式。
        int64_t probesize;
        const uint8_t *key;
        int keylen;
        unsigned int nb_programs;
        AVProgram **programs;
        enum AVCodecID video_codec_id;  //设置的视频编解码器ID，由用户设置
        enum AVCodecID audio_codec_id;  //设置的音频编解码器ID
        enum AVCodecID subtitle_codec_id; //设置的字幕编解码器ID
        unsigned int max_index_size; //流索引内存上限
        unsigned int max_picture_buffer; //实时捕捉设备帧缓冲内存上限。
        unsigned int nb_chapters;
        AVChapter **chapters;
        AVDictionary *metadata;
        int64_t start_time_realtime; //视频创造的真实时间，从1970年开始计算，单位是毫秒。
        int fps_probe_size;
        int error_recognition; //错误识别的级别
        AVIOInterruptCB interrupt_callback;
        int debug;  //开启调试的标志
        int64_t max_interleave_delta;
        int strict_std_compliance; //允许非标准，实验性的扩展
        int event_flags;
        int max_ts_probe;
        int avoid_negative_ts;
        int ts_id;
        int audio_preload; //音频预载入的时间，单位为毫秒
        int max_chunk_duration;
        int max_chunk_size;
        int use_wallclock_as_timestamps;
        int avio_flags;
        enum AVDurationEstimationMethod duration_estimation_method;
        int64_t skip_initial_bytes; //打开流时跳过开头的数据，单位为字节。
        unsigned int correct_ts_overflow;
        int seek2any; //允许强制跳转到任意帧，也就说没有关键帧。
        int flush_packets;
        int probe_score;
        int format_probesize;
        char *codec_whitelist; //解码器白名单，逗号分隔的字符串。如果是NULL，则表示允许所有。
        char *format_whitelist; //封装格式白名单，同上
        int io_repositioned;
        const AVCodec *video_codec; //强制设置视频解码器
        const AVCodec *audio_codec; //强制设置音频解码器
        const AVCodec *subtitle_codec; //强制设置字幕解码器
        const AVCodec *data_codec; //强制设置数据解码器
        int metadata_header_padding; //元数据头的填空大小，单位为字节。
        void *opaque; //用户自定义数据
        av_format_control_message control_message_cb; //回调函数，用于设备和应用沟通。
        int64_t output_ts_offset;
        uint8_t *dump_separator;
        enum AVCodecID data_codec_id;
        char *protocol_whitelist; //协议白名单，同上
        int (*io_open)(struct AVFormatContext *s, AVIOContext **pb, const char *url,
                       int flags, AVDictionary **options); //回调函数，打开新的流时会被调用，用来获得一个AVIOContext。
        void (*io_close)(struct AVFormatContext *s, AVIOContext *pb);
        char *protocol_blacklist; //协议黑名单
        int max_streams;  //流的最大允许数量
        int skip_estimate_duration_from_pts;
        int max_probe_packets; //能被探测到的包最大数量。
        int (*io_close2)(struct AVFormatContext *s, AVIOContext *pb); //回调函数，会在关闭使用io_open打开的流时调用。
    } AVFormatContext;
    ```

29. AVInputFormat结构体中常用的成员介绍：

34. ```c
    typedef struct AVInputFormat {
        const char *name; //封装格式名称
        const char *long_name; //关于该封装格式描述性的名字，给人看的
        int flags; //标志
        const char *extensions; //扩展名，如果定义了扩展名，则不进行封装格式探测，尽量避免使用，因为不可靠。
        const struct AVCodecTag * const *codec_tag;
        const AVClass *priv_class; ///< AVClass for the private context
        const char *mime_type; //MIME类型，逗号分隔的字符串。
    
        /*****************************************************************
         * No fields below this line are part of the public API. They
         * may not be used outside of libavformat and can be changed and
         * removed at will.
         * New public fields should be added right above.
         *****************************************************************
         */
        /**
         * Raw demuxers store their codec ID here.
         */
        int raw_codec_id;
    
        /**
         * Size of private data so that it can be allocated in the wrapper.
         */
        int priv_data_size;
    
        /**
         * Internal flags. See FF_FMT_FLAG_* in internal.h.
         */
        int flags_internal;
    
        /**
         * Tell if a given file has a chance of being parsed as this format.
         * The buffer provided is guaranteed to be AVPROBE_PADDING_SIZE bytes
         * big so you do not have to check for that unless you need more.
         */
        int (*read_probe)(const AVProbeData *); //函数指针，可以看做结构体的方法。
    
        /**
         * Read the format header and initialize the AVFormatContext
         * structure. Return 0 if OK. 'avformat_new_stream' should be
         * called to create new streams.
         */
        int (*read_header)(struct AVFormatContext *);
    
        /**
         * Read one packet and put it in 'pkt'. pts and flags are also
         * set. 'avformat_new_stream' can be called only if the flag
         * AVFMTCTX_NOHEADER is used and only in the calling thread (not in a
         * background thread).
         * @return 0 on success, < 0 on error.
         *         Upon returning an error, pkt must be unreferenced by the caller.
         */
        int (*read_packet)(struct AVFormatContext *, AVPacket *pkt);
    
        /**
         * Close the stream. The AVFormatContext and AVStreams are not
         * freed by this function
         */
        int (*read_close)(struct AVFormatContext *);
    
        /**
         * Seek to a given timestamp relative to the frames in
         * stream component stream_index.
         * @param stream_index Must not be -1.
         * @param flags Selects which direction should be preferred if no exact
         *              match is available.
         * @return >= 0 on success (but not necessarily the new offset)
         */
        int (*read_seek)(struct AVFormatContext *,
                         int stream_index, int64_t timestamp, int flags);
    
        /**
         * Get the next timestamp in stream[stream_index].time_base units.
         * @return the timestamp or AV_NOPTS_VALUE if an error occurred
         */
        int64_t (*read_timestamp)(struct AVFormatContext *s, int stream_index,
                                  int64_t *pos, int64_t pos_limit);
    
        /**
         * Start/resume playing - only meaningful if using a network-based format
         * (RTSP).
         */
        int (*read_play)(struct AVFormatContext *);
    
        /**
         * Pause playing - only meaningful if using a network-based format
         * (RTSP).
         */
        int (*read_pause)(struct AVFormatContext *);
    
        /**
         * Seek to timestamp ts.
         * Seeking will be done so that the point from which all active streams
         * can be presented successfully will be closest to ts and within min/max_ts.
         * Active streams are all streams that have AVStream.discard < AVDISCARD_ALL.
         */
        int (*read_seek2)(struct AVFormatContext *s, int stream_index, int64_t min_ts, int64_t ts, int64_t max_ts, int flags);
    
        /**
         * Returns device list with it properties.
         * @see avdevice_list_devices() for more details.
         */
        int (*get_device_list)(struct AVFormatContext *s, struct AVDeviceInfoList *device_list);
    
    } AVInputFormat;
    ```
    
35. AVStream结构体常见的成员介绍：

36. ```c
    typedef struct AVStream {
        int index; //当前流在AVFormatContext中的编号。
        int id; //格式相关的流ID。
        void *priv_data;  //私密数据
        AVRational time_base;
        int64_t start_time;
        int64_t duration; //流的时间长度，以流的time_base为单位。
        int64_t nb_frames; //当前流的帧数
        int disposition;
        enum AVDiscard discard;
        AVRational sample_aspect_ratio;
        AVDictionary *metadata;
        AVRational avg_frame_rate; //平均帧率
        AVPacket attached_pic;
        AVPacketSideData *side_data;
        int nb_side_data;
        int event_flags;
        AVRational r_frame_rate; //流的真实基础帧率
        AVCodecParameters *codecpar; //和这个流相关的编解码器参数，调用avformat_find_stream_info时填充。替代原来的AVCodecContext *codec成员。
        int pts_wrap_bits;
    } AVStream;
    ```
