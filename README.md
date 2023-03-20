# 北航离散数学（1）logic.logic库
## 我去除了教科书大部分不合理的实现，但是**我保留了logic.logic，**  
## **只有保留logic.logic，你才知道你学的是北航的离散数学（1）。**
## How to start  
### 要开始使用logic.logic库，在终端输入：（需要安装git）  
`git clone https://github.com/FyVoid/BeiHangDM.git`  
  
将BeiHangDM文件夹中的logic**文件夹**放入你的python项目，然后输入mdf的神秘魔咒:  
  
`import logic.logic as ll`

**如何使用：**  
以字符串的形式输入一个简单的逻辑表达式：  
`s = 'A ∧ (B → C)'`  
或是使用**人类编码**  
`s = 'A ^ (B -> C)'`  
call **ll.logic_eval()** 函数，第一个变量为表达式字符串，第二个变量为代表表达式中每个变量真值的字典（真值用字符串形式表示）：  
`print(ll.logic_eval(s, {'A': '1', 'B': '0', 'C': '1'}))`  
得到如下输出：  
`1`  
如果要输出真值表，你可以call **ll.truthtable()** 函数，第一个变量为一个列表，声明表达式中出现的所有变量名，第二个变量为表达式：  
`ll.truthtable(['A', 'B', 'C'], s)`  
输出为：  
A B C A ∧ (B → C)  
1 1 1       1  
1 1 0       0  
1 0 1       1  
1 0 0       1  
0 1 1       0  
0 1 0       0  
0 0 1       0  
0 0 0       0  
详细的使用方法见后：[**文档**](#文档)

## 编码
logic.logic采用两套编码方式：离散数学编码和人类编码  
离散数学编码中采用Unicode字符集中表示离散数学相关符号的字符表示数学运算符，函数的输出大多采用这个编码方式  
人类编码为方便编程输入设计，具体字符映射如下：  
|离散数学编码|人类编码 |  
|----------|-------|  
|┐         |~      |  
|∧         |^      |  
|∨         |v(字母v)|  
|⊕         |@      |  
|→         |->     |  

你可以通过**ll.Encode2DiscreteMath()** 和 **ll.Encode2Human()** 函数在两种编码之间转换

## 文档
文档中的表达式都为字符串类型
### Encode2DiscreteMath(expr):  
函数接收一个表达式，返回表达式的离散数学编码形式  

### Encode2Human(expr)：
函数接收一个表达式，返回表达式的人类编码形式  

### logic_eval(expr, vars):
函数接收一个**任意编码**的表达式expr和声明表达式中每个变量的值的字典vars，返回表达式的值

### truthtable(vars, expr):
函数接收一个声明表达式中所有变量变量名的列表vars和表达式expr，输出该表达式的真值表  
函数的内部实现是递归的，和教科书的方法不同，可以输出任意数量变量的真值表

### isargument(vars, pre, expr):
函数接收一个声明表达式中所有变量变量名的列表vars，前提条件表达式列表pre和结论表达式expr，输出该前提下是否能推出结论的真值表，例如：  
要通过真值表判定P，Q -> (P -> R) ╞ Q → R是否成立，使用以下代码：  
`import logic.logic as ll`  
`pre = ['P', 'Q -> (P -> R)']`  
`expr = 'Q -> R'`  
`ll.isargument(['P', 'Q', 'R'], pre, expr)`  
运行后，控制台会输出该推论在变量P，Q，R取不同值时的真值表  
**注意，与教科书的实现不同，输出中包含了整个推论在变量取不同真值时的真值，因此比教科书多一列**  
同样，函数内部实现是递归的，可以输出任意数量变量，前提的推论式真值表

### isequilent(vars, pre, expr):
函数的接口和isargument()相同，区别只在于判断前提和结论是否构成等价关系