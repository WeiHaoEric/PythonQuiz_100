# PythonQuiz_100 Note
This is a challenge to review Python 100 quiz!!
- 過程中，我將整理我所發現的技巧，以利複習。
---
## Progress
- 12/24: 

---

## Tips

### Vscode Python套件
- 之前開發`js`的時候，因為套件`Colonize`，按下`Shift+Enter`可直接產生`;`
- 微軟出的`Python套件`, 在coding python時，可直接按下`Shift+Enter`，然後就會在`console window`印出結果。

### String 
- 假設一個List裡面的element都是*string*，今天我想要用一行呈現所有的element，並以comma-separated隔開，可以如下進行:
```=python
data = ["1", "2", "...", "999"]
print ",".join(data)
```
- `python3`針對func的`input`指令，會將所有的輸入都設定為`string`

- `string`內建的func`split`，可以自動的把內建的某個字元隔開，並回傳一個`list`。而list也可以與`tuple`直接互相轉換喔。

- 快速判斷`str`是否為數字，可以
```python=
dataA = "10"
dataA.isdigit() # True

dataB = "AAA"
dataB.isdigit() # False
```

- `String`好用的`func`
| Func | Desc |
| -------- | -------- |
| '66'.isdigit()     | 確認是否為`數字`     |
| 'A'.isupper()      | 確認是否為`大寫`     |
| 'a'.islower()      | 確認是否為`小寫`     |


### list與str之間的轉換
```python=
a = 1234   
b = str(a) #"1234"
listB = list(b) #['1','2','3','4']
```

### Class
- `class`的基本架構如下:
```python=
class Test(object):
  def __init__(self, para1, para2,...):
    self.publicVar = None
    self.__privateVar = None
    ...
  def funcA(self, para1, para2,...):
    ...
```

### list
- `Python List`可以提供如`JS array.map/filter/reduce`的方法，可[參考教學](https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/)如下介紹:
- `quiz10`學習`set`與`list`的切換，以及 `list`如何使用它內建的`sort` 及外部的func `sorted`，建議可複習。
>- sort方法1:`['c', 'a', 'z'].sort() # ['a', 'c', 'z']`
>- sort方法2: `sorted(['c', 'a', 'z']) #['a', 'c', 'z']`
#### map(func, list)
- in JS: 簡短有力，直接使用`arrow func`來直接處理
```javascript=
let data = [1,3,5,7,9];
data.map((val)=>val*val);
```

- in Python: 可以定義一個`func`或用`lambda 輸入參數:參數處理`來啟用`map`，但要記得用`list(mapObj)`來解開所有迭代處理後的數值。
```python=
def aFunc(val):
  return val*val

data = [1,3,5,7,9]
# method1: map + func
print( list(map(aFunc, data)) )

# method2: map + lambda
print( list(map( lambda val:(val*val), data)) )
```

#### filter
- in JS:
```javascript=
let fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"];
let result = fruit.filter((f)=>f[0]==="A");
```

- in Python:
```python
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
result = [f for f in fruit if f[0]=="A"]

```

#### reduce(func, data)
- in JS:
```javascript=
let data = [1,2,3,4,5];
let result = a.reduce((sum, val)=>sum+val)
```

- in Python:
```python=
from functools import reduce
data = [1,2,3,4,5];
reduce(lambda sum,val:sum+val, data)

```

## 數值轉換
### Binary -> Decimal
```python=
B = "0010"
print(int(B,2))
```

### Decimal to Binary
```python=
D = 10
print(bin(D)) # 0b1010, 含 "0b" prefix
print(bin(D)[2:]) # 1010, 不含 "0b" prefix

```

## Loop迴圈
### break, continue, pass [這篇教學很清楚](https://reurl.cc/e80kob)
- `break`: 跳出迴圈
- `continue`: 跳過這個參數（以下的程式碼不進行），往下個參數進行
>- 當今天要寫一個`多條件檢查`, 用`continue`就非常適合
>```python=
# 假設我要寫一個，過濾`a,c,e`的filter
data = "abcde"
result = []
for i in data:
    if (i == "a"):
      continue
    elif (i == "c"):
      continue
    elif (i == "e"):
      continue
    else:
      pass #<-- pass有寫沒寫，都會往下進行，不過有`if...elif...也要有個else`，故用`pass`補到`else`
    
    result.append(i)
print(result) # $['b','d']
```
- `pass`: 程式碼不進行），往下個參數進行

- <font color="red">強烈建議:</font> quiz-18一定要練習



---
## 一定要複習
- quiz-18
