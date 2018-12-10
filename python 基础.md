# python 基础

## 类

### 私有属性

```python
class Room:
    def __init__(self,name,length,width):
        self.__name = name
        self.__length = length
        self.__width = width
    def get_name(self):
        return self.__name
    def set_name(self,newName):   ## 约束属性
        if type(newName) is str and newName.isdigit() == False:
            self.__name = newName
        else:
            print('不合法的姓名')
    def area(self):
        return self.__length * self.__width
```

会用到私有的这个概念的场景
1. 隐藏起一个属性 不想让类的外部调用
2. 我想保护这个属性，不想让属性随意被改变
3. 我想保护这个属性，不被子类继承

### 类装饰器

- property : 方法 伪装成属性
```python
  from math import pi
  class Circle:
      def __init__(self,r):
          self.r = r
      @property   # 后面不加参数
      def perimeter(self):
          return 2*pi*self.r
      @property
      def area(self):
          return self.r**2*pi
        
        
   class Person:
    def __init__(self,name):
        self.__name = name
    @property     
    def name(self):
        return self.__name + 'sb'
    @name.setter  # 修改装饰器属性
    def name(self,new_name):
        self.__name = new_name
```

- classmethod   # 把一个方法 变成一个类中的方法，这个方法就直接可以被类调用，不需要依托任何对象
  ```
  def change_discount(cls,new_discount):  # 修改折扣
  	cls.__discount = new_discount
  ```

- staticmathod  # 如果一个函数 既和对象没有关系 也和类没有关系 那么就用staticmethod将这个函数变成一个静态方法