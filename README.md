# PythonQuiz_100 Note
This is a challenge to review Python 100 quiz!!
- 過程中，我將整理我所發現的技巧，以利複習。
---
## Progress
- 12/24: 

---

## Tips
### String 
- 假設一個List裡面的element都是*string*，今天我想要用一行呈現所有的element，並以comma-separated隔開，可以如下進行:
```=python
data = ["1", "2", "...", "999"]
print ",".join(data)
```
- `python3`針對func的`input`指令，會將所有的輸入都設定為`string`

- `string`內建的func`split`，可以自動的把內建的某個字元隔開，並回傳一個`list`。而list也可以與`tuple`直接互相轉換喔。

### Vscode Python套件
- 之前開發`js`的時候，因為套件`Colonize`，按下`Shift+Enter`可直接產生`;`
- 微軟出的`Python套件`, 在coding python時，可直接按下`Shift+Enter`，然後就會在`console window`印出結果。


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
- `Python List`可以提供如`JS array.map/filter/reduce`的方法，如下介紹:
#### map in Python and JS
- in JS: 簡短有力，直接使用`arrow func`來直接處理
```javascript=
let data = [1,3,5,7,9]
data.map((val)=>val*val)
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

