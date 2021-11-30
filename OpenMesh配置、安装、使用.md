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

### Cmake生成工程文件()

#### 下载OpenMesh源码:

#### 部署Qt5

> 否则Cmake时出现 `QT5 not found! Skipping some apps.`
>
> > 安装Qt5也报错。。。

#### 使用CMake生成VS工程文件

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
> 
>
> 或者参考第三方库的添加方法
>
> [C++学习笔记（三）：VS2017安装第三方库_Très bien !的博客-CSDN博客_vs安装库](https://blog.csdn.net/weixin_43647192/article/details/99934197)

### 使用Vcpkg进行第三方库的安装管理	~~真的NB~~

> 考虑使用vcpkg
>
> [vcpkg - Open source C/C++ dependency manager from Microsoft](https://vcpkg.io/en/index.html)
>
> [Visual Studio开源库集成器Vcpkg全教程--利用Vcpkg轻松集成开源第三方库_chenjm的专栏-CSDN博客_vcpkg](https://blog.csdn.net/cjmqas/article/details/79282847)
>
> [[工具\]包管理工具Vcpkg 的使用 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/153199835)
>
> > - SomeVcpkgTips
> >
> > ```
> > ..\vcpkg search
> > #查看所有支持的库
> > 
> > ..\vcpkg search [pkgname]
> > #查找是否支持某一个库(这个搜索功能不是完全字匹配,甚至可以匹配到描述文字)
> > 
> > ..\vcpkg install [pkgname]	#安装一个库
> > 
> > #编译某一个架构的开源库:
> > ..\vcpkg install [pkgname]:x86-windows	#安装32位(默认)
> > ..\vcpkg install [pkgname]:x64-windows	#指定安装64位
> > ..\vcpkg help triplet	#查看支持架构列表
> > 
> > 
> > ..\vcpkg list	#查看已安装的库
> > 
> > ..\vcpkg remove [pkgname]	#移除某个库
> > 
> > ..\vcpkg integrate install	##集成库到全局##推荐##
> > ..\vcpkg integrate remove	#移除集成
> > 
> > ```
>
> 


### 直接下载安装OpenMesh库，链接库到项目中

> [OpenMesh入门，安装，运行示例Hello World_偕臧-CSDN博客_openmesh](https://blog.csdn.net/qq_33154343/article/details/93206255)

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
> >   > ~~出现pybind11相关问题~~
> >   >
> >   > 应该是没问题的，python动态语言的特性**不允许直接查看类与方法定义**
> >
> > - 如果使用***VS***，读不到文件的话请调整项目输入输出参数

