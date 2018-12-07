#  [JS 基础教程](https://www.cnblogs.com/liwenzhou/p/8004649.html)

##  [基础知识](http://www.w3school.com.cn/js/js_intro.asp)

- 引入

  ```javascript
  <script>
    // 在这里写你的JS代码
  </script>
  <script src="myscript.js"></script># 外部引用
  ```

- 注释+结束符

  ```
  // 这是单行注释
  
  /*
  这是
  多行注释
  */
  ;#结束
  ```

- 声明变量 var

### [数据类型](http://www.w3school.com.cn/jsref/jsref_obj_date.asp)

![](https://images2018.cnblogs.com/blog/867021/201803/867021-20180311224027096-1902975546.png)

函数

```javascript
// 普通函数定义
function f1() {
  console.log("Hello world!");
}

// 带参数的函数
function f2(a, b) {
  console.log(arguments);  // 内置的arguments对象
  console.log(arguments.length);
  console.log(a, b);
}

// 带返回值的函数
function sum(a, b){
  return a + b;
}
sum(1, 2);  // 调用函数

// 匿名函数方式
var sum = function(a, b){
  return a + b;
}
sum(1, 2);

// 立即执行函数
(function(a, b){
  return a + b;
})(1, 2);
//arguments 保存不定长参数
```

- 运算符
  | 运算符 | 描述 | 例子                      |
  | ------ | ---- | ------------------------- |
  | &&     | and  | (x < 10 && y > 1) 为 true |
  | \|\|   | or   | (x==5 \|\| y==5) 为 false |
  | !      | not  | !(x==y) 为 true           |

###  流程控制

- 判断

  ```javascript
  if (条件 1)
    {
    当条件 1 为 true 时执行的代码
    }
  else if (条件 2)
    {
    当条件 2 为 true 时执行的代码
    }
  else
    {
    当条件 1 和 条件 2 都不为 true 时执行的代码
    }
  ```

  ```javascript
  switch(n)
  {
  case 1:
    执行代码块 1
    break;
  case 2:
    执行代码块 2
    break; //break 来阻止代码自动地向下一个 case 运行
  default:
    n 与 case 1 和 case 2 不同时执行的代码
  }
  ```

- 循环

  - *for* - 循环代码块一定的次数

  - *for/in* - 循环遍历对象的属性

  - *while* - 当指定的条件为 true 时循环指定的代码块

  - *do/while* - 同样当指定的条件为 true 时循环指定的代码块

    ```js
    for (语句 1; 语句 2; 语句 3)
      {
      被执行的代码块
      }
    var person={fname:"John",lname:"Doe",age:25};
    // 语句 1 在循环（代码块）开始前执行
    // 语句 2 定义运行循环（代码块）的条件
    // 语句 3 在循环（代码块）已被执行之后执行
    for (x in person)
      {
      txt=txt + person[x];
      }
    ```

    ```javascript
    while (条件)
      {
      需要执行的代码
      }
    ```

    ```javascript
    cars=["BMW","Volvo","Saab","Ford"];// 高级操作
    list:
    {
    document.write(cars[0] + "<br>");
    document.write(cars[1] + "<br>");
    document.write(cars[2] + "<br>");
    break list;
    document.write(cars[3] + "<br>");
    document.write(cars[4] + "<br>");
    document.write(cars[5] + "<br>");
    }
    ```

- 捕获错误

  ```javascript
  try
    {
    var x=document.getElementById("demo").value;
    if(x=="")    throw "empty"; //自定义错误
    if(isNaN(x)) throw "not a number";
    if(x>10)     throw "too high";
    if(x<5)      throw "too low";
    }
  catch(err)
    {
    var y=document.getElementById("mess");
    y.innerHTML="Error: " + err + ".";
    }
  ```
### 函数词法分析

**函数是先分析 再执行**


```javascript
var age = 18;
function foo(){
  console.log(age); 					//3 func  
  var age = 22;     //1 AO.age=22  		//4 AO.age=22 
  console.log(age);						//5 22 
  function age(){   //2 AO.age=func  	//6 AO.age=func 
    console.log("呵呵");
  }
  console.log(age);						//7 22 ? func 没有改变AO
}
foo();  // 执行后的结果是？
func 22 22
```
当函数调用的前一瞬间，会先形成一个激活对象：Avtive Object（AO），并会分析以下3个方面：

1. 函数参数，如果有，则将此参数赋值给AO，且值为undefined。如果没有，则不做任何操作。
2. 函数局部变量，如果AO上有同名的值，则不做任何操作。如果没有，则将此变量赋值给AO，并且值为undefined。
3. 函数声明，如果AO上有，则会将AO上的对象覆盖。如果没有，则不做任何操作。

### [DOM](http://www.w3school.com.cn/htmldom/index.asp)



![DOM](http://www.w3school.com.cn/i/ct_htmltree.gif)

- JavaScript 能够改变页面中的所有 HTML 元素

  ```
  document.getElementById(id).innerHTML=new HTML
  ```

- JavaScript 能够改变页面中的所有 HTML 属性

  ```
  document.getElementById(id).attribute=new value
  ```

- JavaScript 能够改变页面中的所有 CSS 样式

  ```
  document.getElementById(id).style.property=new style
  ```

- JavaScript 能够对页面中的所有事件做出反应

  ```
  <button type="button" onclick="document.getElementById('id1').style.color='red'">
  ```

#### 事件

- 当用户点击鼠标时 onclick
- 当网页已加载时
- 当图像已加载时
- 当鼠标移动到元素上时
- 当输入字段被改变时
- 当提交 HTML 表单时
- 当用户触发按键时

绑定 

```javascript
document.getElementById("myBtn").onclick=function(){displayDate()};
```

