# 北航离散数学（1）logic.logic库
## 我去除了教科书大部分不合理的实现，但是**我保留了logic.logic，**  
## **只有保留logic.logic，你才知道你学的是北航的离散数学（1）。**
## How to start  
### 要开始使用logic.logic库，在终端输入：（需要安装git）  
`git clone https://github.com/FyVoid/BeiHangDM.git`  
  
将BeiHangDM文件夹中的**logic文件夹**复制入你的python项目，然后输入**mdf的神秘魔咒**:  
  
`import logic.logic as ll`

**使用logic.logic需要掌握基本的python语法**  
### 库仍然在编写过程中，如果要获取最新版本的logic.logic，在终端中进入BeiHangDM目录下，输入  
`git pull https://github.com/FyVoid/BeiHangDM.git`

当然，作为大一的萌新，你也可以重新clone一个库的副本  
### 如何使用： 
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
**文档中的表达式都为字符串类型**
### Encode2DiscreteMath(expr):  
函数接收一个表达式，返回表达式的离散数学编码形式  
**用例：**
将表达式  
`expr = 'A ^ B -> C'`转换为离散数学编码格式：  
`expr = ll.Encode2DiscreteMath(expr)`  
`print(expr)`  
输出：  
A ∧ B → C

### Encode2Human(expr)：
函数接收一个表达式，返回表达式的人类编码形式  
使用方法与Encode2DiscreteMath()相同

### logic_eval(expr, vars):
函数接收一个**任意编码**的表达式expr和声明表达式中每个变量的值的字典vars，返回表达式的值  
**用例：**  
计算表达式`expr = 'A ^ B -> C'`在 A = 1, B = 0, C = 1的情况下的值：  
你需要创建一个**字典**表明每个变量的值：`value_dict = {'A': '1', 'B': '0', 'C': '1'}`  
然后call **logic_eval()**函数：  
`print(ll.logic_eval(expr, value_dict))`  
或是直接将字典传入函数：  
`print(ll.logic_eval(expr, {'A': '1', 'B': '0', 'C': '1'}))`  
输出：  
1  
**注意：字典中每个键的值（即变量的真值）需要用字符串表示，否则会产生TypeError**  

### truthtable(vars, expr):
函数接收一个声明表达式中所有变量变量名的列表vars和表达式expr，输出该表达式的真值表  
函数的内部实现是递归的，和教科书的方法不同，可以输出任意数量变量的真值表  
**用例：**  
输出表达式`expr = 'A ^ B -> C'`的真值表：  
你需要通过一个**列表**告诉函数表达式中有哪些变量：`vars = ['A', 'B', 'C']`  
然后call truthtable():`ll.truthtable(vars, expr)`  
当然，你也可以直接将列表传入函数：`ll.truthtable(['A', 'B', 'C'], expr)`  
输出：  
A B C A ∧ B → C  
1 1 1      1  
1 1 0      0  
1 0 1      1  
1 0 0      1  
0 1 1      1  
0 1 0      0  
0 0 1      1  
0 0 0      0  

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

### isequation(vars, pre, expr):
函数的接口和isargument()相同，区别只在于判断前提和结论是否构成等价关系