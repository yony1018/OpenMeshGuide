# OpenMesh初探

> 一切要从OpenMesh原项目文档开始:
>
> [OpenMesh - HomePage](https://www.graphics.rwth-aachen.de/software/openmesh/)
>
> [OpenMesh Documentation](https://www.graphics.rwth-aachen.de/media/openmesh_static/Documentations/OpenMesh-Doc-Latest/index.html)
>
> [xmuli提供的中文文档/](https://github.com/xmuli/openMesh/tree/master/docORpdf)



# OpenMesh是什么

> OpenMesh is a generic and efficient data structure for representing and manipulating polygonal meshes. 

# OpenMesh部署

## C++环境部署

### 下载OpenMesh源码:

### 部署Qt5

> 否则Cmake时出现 `QT5 not found! Skipping some apps.`

### 使用CMake生成VS工程文件

> 参考:
>
> [使用CMake生成sln项目和VS工程遇到的问题 - DoubleLi - 博客园 (cnblogs.com)](https://www.cnblogs.com/lidabo/p/8652429.html)
>
> [使用cmake自动构建工程 - 在于思考 - 博客园 (cnblogs.com)](https://www.cnblogs.com/chengxuyuancc/p/5347646.html)
>
> 
>
> 使用静态库后编译出现
>
> [链接器工具错误 LNK2019 | Microsoft Docs](https://docs.microsoft.com/zh-cn/cpp/error-messages/tool-errors/linker-tools-error-lnk2019?f1url=%3FappId%3DDev16IDEF1%26l%3DZH-CN%26k%3Dk(LNK2019)%26rd%3Dtrue&view=msvc-170)
>
> 考虑使用vcpkg
>
> [vcpkg - Open source C/C++ dependency manager from Microsoft](https://vcpkg.io/en/index.html)
>
> 或者参考第三方库的添加方法
>
> [C++学习笔记（三）：VS2017安装第三方库_Très bien !的博客-CSDN博客_vs安装库](https://blog.csdn.net/weixin_43647192/article/details/99934197)

## Python环境部署

> 很简单，[OpenMesh / openmesh-python · GitLab (rwth-aachen.de)](https://gitlab.vci.rwth-aachen.de:9000/OpenMesh/openmesh-python)
>
> 根着官网的手册几句命令行就装好了
> > 测试代码在交互界面直接跑的话，
> > 输出test.off在`C:\ProgramData\Anaconda3`目录下
>
> > 项目地址也提供了一个测试程序集，以便我们学习和参考
> >
> > [tests · master · OpenMesh / openmesh-python · GitLab (rwth-aachen.de)](https://gitlab.vci.rwth-aachen.de:9000/OpenMesh/openmesh-python/-/tree/master/tests)
> >
> > - 使用***pycharm***就~~可以直接跑了~~
> >
> >   > 出现pybind11相关问题
> >
> > - 如果使用***VS***，读不到文件的话请调整项目输入输出参数

