# 编译安装

1. Openfoam需要使用专用的ParaView，因为这里边有专门为Openfoam编写的读取模块。

2. 如果使用源码编译Openfoam时，也可以不手动编译paraview，而使用官方仓库提供内编译好的paraview。然后需要添加paraview的bin目录到PATH中。

   ```shell
   sudo apt install paraviewopenfoam510 #这个只会单独安装paraview
   #添加到.bashrc中
   PATH=$PATH:/opt/paraviewopenfoam510/bin
   ```

3. 新版本的paraview已经原生支持openfoam结果文件了，可以直接`sudo apt install paraview`安装即可。使用的时候，需要在对应的结果目录下创建一个任意的后缀名为.foam的文件即可。使用paraFoam时，会自动创建一个临时的.foam文件。也可以使用`paraFoam -touch`来创建一个永久的文件。

4. ThirdParty-11仓库中主要包含的是Scotch软件的源码，因为早期版本的Debian自带的Scotch版本比较落后，因此需要使用源码编译安装，不过在Ubuntu22.04中，可以使用`sudo apt install scotch`安装即可。

5. 源码目录中可能有冗余的文件，只有包含在Make/files中的文件才会被编译。这点可以从.dep文件的对应发现。

6. 源代码目录下的lnInclude目录中包含同级目录及其子目录的所有源文件，包括.C和.h。

   ```shell
   zj@zj-hit:~/OpenFOAM/OpenFOAM-11/src/fileFormats$ tree
   .
   ├── lnInclude
   │   ├── NASCore.C -> ../nas/NASCore.C
   │   ├── NASCore.H -> ../nas/NASCore.H
   │   ├── OBJstream.C -> ../obj/OBJstream.C
   │   ├── OBJstream.H -> ../obj/OBJstream.H
   │   ├── STARCDCore.C -> ../starcd/STARCDCore.C
   │   ├── STARCDCore.H -> ../starcd/STARCDCore.H
   │   ├── vtkUnstructuredReader.C -> ../vtk/vtkUnstructuredReader.C
   │   ├── vtkUnstructuredReader.H -> ../vtk/vtkUnstructuredReader.H
   │   ├── vtkUnstructuredReaderTemplates.C -> ../vtk/vtkUnstructuredReaderTemplates.C
   │   ├── vtkWriteOps.C -> ../vtk/vtkWriteOps.C
   │   ├── vtkWriteOps.H -> ../vtk/vtkWriteOps.H
   │   ├── vtkWriteOpsTemplates.C -> ../vtk/vtkWriteOpsTemplates.C
   │   ├── vtkWritePolyData.H -> ../vtk/vtkWritePolyData.H
   │   └── vtkWritePolyDataTemplates.C -> ../vtk/vtkWritePolyDataTemplates.C
   ├── Make
   │   ├── files
   │   └── options
   ├── nas
   │   ├── NASCore.C
   │   └── NASCore.H
   ├── obj
   │   ├── OBJstream.C
   │   └── OBJstream.H
   ├── starcd
   │   ├── STARCDCore.C
   │   └── STARCDCore.H
   └── vtk
       ├── vtkUnstructuredReader.C
       ├── vtkUnstructuredReader.H
       ├── vtkUnstructuredReaderTemplates.C
       ├── vtkWriteOps.C
       ├── vtkWriteOps.H
       ├── vtkWriteOpsTemplates.C
       ├── vtkWritePolyData.H
       └── vtkWritePolyDataTemplates.C
   
   6 directories, 30 files
   ```

7. 总的配置文件为`/home/zj/OpenFOAM/OpenFOAM-11/etc/bashrc`。

8. 

9. 

10. 

11. debug 调试，可以对软件进行单步执行、堆栈跟踪、调试等操作来发现bug
    release 发行版，如果最终调试后程序没有明显bug，可以作为可用的软件分享给他人使用就可以使用这个选项编译。
    profiling 性能分析。可以对软件执行过程中的cpu利用率，内存占有进行分析。也可以用来发现、分析异常、bug
