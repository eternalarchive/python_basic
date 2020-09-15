# Python basic(1) - 기초 입출력

## 출력

```python
print('Hi')
print("Hello")

# Hi
# Hello
```

- 작은 따옴표, 큰 따옴표 모두 사용 가능

```python
print(1, 2, 3, sep="+")

# 1+2+3
```

- sep에 문자열 입력시 여러 변수 사이에 해당 문자가 입력되어 출력됨

```python
print(1, end=' ')
print(2)

# 1 2
```

- 한 줄씩 띄어 쓸 경우 자동 개행이 되는데, end에 문자열을 지정하면 출력 값 끝에 해당 문자가 출력되고 개행이 되지 않음

```python
print(1, 2, 3)
print('1\n2\n3')

# 1 2 3
# 1
# 2
# 3
```

- 한 번에 값을 여러개 출력할 수 있고 ,(콤마)로 구분
- 개행을 원하는 문자 뒤쪽에 \n을 붙여주면 개행되어 출력

## 입력

- input입력값은 항상 문자열

```python
input()

# 입력값 변수에 할당
a = input()
b = input('내용을 입력해주세요:')

# 한 번에 여러개 입력(split기본은 공백 기준)
# split에 문자열 입력시 나누는 기준 문자열이 됨
a, b = input().split()

# 입력값 타입 지정
a = int(input())
b = float(input())

# map으로 다양한 입력값 타입 지정
a, b = map(int, input().split())
```

## 변수명 규칙

- 영문 문자와 숫자 사용 가능(한글도 사용할 수 있으나 사용하지 않는 것이 바람직)
- 대소문자 구분하여 사용
- 문자부터 시작해야 하며 숫자부터 시작할 수 없음
- _(밑줄 문자)로 시작 가능
- 특수 문자(하이픈 포함)는 사용할 수 없음
- 파이썬 키워드는 사용할 수 없음

## 변수 생성

```python
# 다음과 같이 변수를 생성할 수 있음
x = 1

# 변수를 여러개 생성할 때
a, b, c = 10, 20, 30

# 같은 값을 가진 변수를 여러개 생성할 때
a1 = b1 = c1 = 10

# 입력 받은 값으로 변수에 할당하기
z = input()
```

## 변수(객체) 타입 알아보기

### 파이썬 데이터 타입

- Number(int float, complex)
- String
- Boolean
- Byte
- List
- Tuple
- Set
- Dictionaries

### 데이터 타입을 알아보는 방법

```python
>>> type(9.14)
<class 'flaot'>

>>> type(10)
<class 'int'>
```



출처: [코딩 도장](https://dojang.io/course/view.php?id=7)

