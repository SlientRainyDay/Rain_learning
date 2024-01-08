# streamlit学习笔记

> Streamlit 是一个用于数据科学和机器学习的开源 Python 框架。它提供了一种简单的方式来构建交互式应用程序，使数据科学家和机器学习工程师可以更轻松地将他们的模型展示给其他人。

## 官方文档：

https://docs.streamlit.io/library/api-reference

## streamlit介绍

[Streamlit](https://link.zhihu.com/?target=https%3A//docs.streamlit.io/en/stable/) 是可以用于快速搭建Web应用的Python库。

Streamlit 的特色：

（1）API简单明了，易上手

API非常友好，事实上一天就能学会。

（2）无须学习前端知识（html、css、javascript）

Streamlit 基于tornado框架，封装了大量互动组件，同时也支持大量表格、图表、数据表等对象的渲染，并且支持栅格化响应式布局。

（3）支持markdown和html文本的渲染

Streamlit的默认渲染语言就是markdown；除此以外，Streamlit也支持html文本的渲染，这意味着你也可以将任何html代码嵌入到streamlit应用里

如果我：

（1）并不熟悉前端设计、或者没有前端艺术细胞；

（2）也不想实现太复杂的网页结构；

（3）只是想给我的python程序用极短的时间快速生成一个基于web的GUI

那么，streamlit就是一个非常好的解决方案。

事实上，streamlit官网也将其主要定位于实现机器学习和数据科学的web应用的工具。当然，你也可以将其用于给自己的python脚本创建前端。

## 安装

```
pip install streamlit
```

## 简单例子

```
import streamlit as st
st.write(hello world")
```

在pycharm终端输入`streamlit run 1.py`命令可在浏览器打开

![image-20230807154616174](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308071546329.png)

显示如图：

![image-20230807154651753](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308071546823.png)



## 支持markdown语法

```
import streamlit as st

# markdown
st.markdown('Streamlit Demo')

# 设置网页标题
st.title('一个傻瓜式构建可视化 web的 Python 神器 -- streamlit')

# 展示一级标题
st.header('1. 安装')

st.text('和安装其他包一样，安装 streamlit 非常简单，一条命令即可')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')

# 展示一级标题
st.header('2. 使用')

# 展示二级标题
st.subheader('2.1 生成 Markdown 文档')

# 纯文本
st.text('导入 streamlit 后，就可以直接使用 st.markdown() 初始化')

# 展示代码，有高亮效果
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')
```

![image-20230811093112257](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308110931449.png)

## Streamlit控件：

Streamlit有很多控件，包括前端需要使用的滑动条，单选，复选框，图标，按钮，图表等等！Streamlit将控件视为变量。Streamlit中没有回调函数！每个交互只是自上而下重新运行脚本。这样使程序代码更加简洁

```text
import streamlit as st
x = st.slider('x')
st.write(x, 'squared is', x * x)
```

仅仅三行代码便可以定义一个slider滑动条

![image-20230807160122895](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308071601950.png)



## 创建数据表格

```
import streamlit as st
import numpy as np
import pandas as pd


df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('第%d列' % (i+1) for i in range(5))
)

st.table(df)
```

![image-20230811093522156](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308110935223.png)

## **原生图表组件**

Streamlit 原生支持多种图表：

- st.line_chart：折线图
- st.area_chart：面积图
- st.bar_chart：柱状图
- st.map：地图

### 折线图

```
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

### 面积图

```
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c'])

st.area_chart(chart_data)
```

### 柱状图

```
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns = ["a", "b", "c"])
st.bar_chart(chart_data)
```

### 地图

```
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)
```

### 外部图表组件

Streamlit 的一些原生图表组件，虽然做到了傻瓜式，但仅能输入数据、高度和宽度，如果你想更漂亮的图表，就像 matplotlib.pyplot、Altair、vega-lite、Plotly、Bokeh、PyDeck、Graphviz 那样，streamlit 也提供了支持：

- st.pyplot
- st.bokeh_chart
- st.altair_chart
- st.altair_chart
- st.vega_lite_chart
- st.plotly_chart
- st.pydeck_chart
- st.graphviz_chart

## 用户操作支持

### button

- 简易button
- radio button
- checkbox

```python
import streamlit as st


st.title("My demo")
st.text("click the follow button to get the prediction of the picture")
page_names = ['prediction1', 'prediction2']
page = st.radio('predict', page_names)
st.write("**the follow result returns:**", page)

if page == 'prediction1':
    st.subheader('The follow result is prediction1')
    st.write('The subject in the picture is')
    check = st.checkbox("Click here")
    st.write('State of the checkbox:',check)
    if check:
        st.write("success")


if page == 'prediction2':
    st.subheader('The follw result is prediction2')
    st.write('The subject in the picture is')
    check = st.checkbox("click here")
    st.write('State of the checkbox:',check)
    if check:
        st.write("success")
```



#### 简易button

> 根据点击输出回显

```
import streamlit as st

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
```

![image-20230811101116941](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308111011998.png)

#### radio button

> 创建可选择的选项

```
import streamlit as st

st.title("My demo")
st.text("click the fellow button to get the prediction of the picture")
page_names = ['prediction1','prediction2']
page = st.radio('predict',page_names)
st.write("**the fellow result returns:**",page)
```

![image-20230811101226623](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308111012696.png)



#### checkbox

> 创建可勾选的方框

```
import streamlit as st


st.title("My demo")
st.text("click the follow button to get the prediction of the picture")
page_names = ['prediction1', 'prediction2']
page = st.radio('predict', page_names)
st.write("**the follow result returns:**", page)

if page == 'prediction1':
    st.subheader('The follow result is prediction1')
    st.write('The subject in the picture is')
    check = st.checkbox("Click here")
    if check:
        st.write("success")
```

![image-20230811112856313](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308111128370.png)

##### checkbox框与点击与否的交互

```
    check = st.checkbox("Click here")
    st.write('State of the checkbox:',check)
    if check:
        st.write("success")
```

**其余按钮事件请参考**

https://docs.streamlit.io/library/api-reference/widgets

## 图片展示

```
import streamlit as st
from PIL import  Image

image = Image.open('car.jpg')
st.image(image,caption = 'picture to be predicted')
```

![image-20230811155413391](https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202308111554583.png)
