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