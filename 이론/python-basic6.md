# Python basic(6) - 클래스1

- 객제지향 프로그래밍
  - 복잡한 문제를 잘게 나누어 객체로 만들고 객체를 조합하여 문제 해결
  - 유지 보수 효율적

```python
class 클래스이름:
	def 메서드(self):
		코드
```

```python
class Person:
  def greeting(self):
    print('Hello')
    
# 인스턴스 = 클래스()
james = Person()

# 메서드 호출
>>> james.greeting()
Hello
```

- 파이썬에서는 자료형도 클래스

```python
>>> a = 10
>>> type(a)
<class 'int'>
>>> b = [0, 1, 2]
>>> type(b)
<class 'list'>
>>> c = { 'x': 10, 'y': 20 }
>>> type(c)
<class 'dict'>
>>> jin = Person()
>>> type(jin)
<class '__main__.Person'>
```

- 메서드 안에서 메서드 호출
  - self.메서드() 형식으로 호출해야 함! self가 없으면 클래스 바깥쪽 함수를 호출한다는 뜻이 됨
- 특정 클래스의 인스턴스인지 확인하기

```python
class Person:
	pass

>>> james.Person()
>>> isinstance(james, Person)
True

# isinstance는 주로 객체의 자료형을 판단할 때 사용
# 예를들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야하는데, 실수와 음의 정수는 계산할 수 없으므로 isinstance를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있음
def factorial(n):
  if not isinstance(n, int) or n < 0: # n이 정수가 아니거나 음수면 끝
    return None
  if n == 1:
    return 1
  return n * factorial(n - 1)
```

- 속성 사용하기
  - 속성을 만들때는 `__init__`메서드 안에서 self.속성에 값을 할당

```python
class 클래스이름:
	def __init__(self):
		self.속성 = 값
    
class Person:
  def __init__(self):
    self.hello = '안녕'
   
  def greeting(self):
    print(self.hello)
    
james = Person()
james.greeting() # 안녕
```

- 인스턴스를 만들 때 값 받기

```python
class 클래스이름:
	def __init__(self, 매개변수1, 매개변수2):
    self.속성1 = 매개변수1
    self.속성2 = 매개변수2
    
class Person:
  def __init__(self, name, age, address, wallet):
    self.hello = '안녕!'
    self.name = name
    self.age = age
    self.address = address
    self.__wallet = wallet # 비공개 속성, 외부에서 접근 불가
    
  def greeting(self):
    print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
    
>>> rimbaud = Person('랭보', 17, '샤를르빌', 1000)
>>> rimbaud.greeting()
안녕! 저는 랭보입니다.

>>> print('이름 : ', rimbaud.name)
이름 : 랭보
```

- 메서드와 속성 앞에 밑줄 두개로 시작하면 비공개 메서드가 됨



출처: [코딩 도장](https://dojang.io/course/view.php?id=7)