# Python basic(5) - 딕셔너리

## 딕셔너리

- 중괄호 안에 키:값 형식으로 저장하며 각 키와 값은 콤마로 구분

- 키 값이 중복되면 가장 뒤에 있는 값을 사용
- 키 값에는 리스트와 딕셔너리를 사용할 수 없음(튜플은 가능)

### dict로 딕셔너리 만들기

```python
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
```

### 딕셔너리 키

- lux['health']처럼 접근하고 값을 추가 할당 및 변경할 수 있음
- 키를 확인하고 싶다면 'health' in lux와 같이 사용할 수 있음

### 연습문제

- 위의 입력값을 아래와 같이 출력하라

```
health health_regen mana mana_regen
575.6 1.7 338.8 1.63
```

```
{'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}
```

- 답

```python
statKey = input.split()
statValue = input.split()
stat = dict(zip(statKey, statValue))
```



## 딕셔너리 응용

- 딕셔너리에 키와 기본값 저장하기

```python
x = { 'a': 10, 'b': 20}
x.setdefault('c')
x.setdefault('d', 40)
>>> x
{ 'a': 10, 'b': 20, 'c': None, 'd': 40 }
```

- 딕셔너리 키 값 수정하기

```python
x.update(a=11, e=50)
>>> x
{ 'a': 11, 'b': 20, 'c': None, 'd': 40, 'e': 50 }

# 또 다른 방법
x.update({ 1: 'ONE', 3: 'THREE' })
x.update([[2, 'TWO'], [4, 'FOUR']])
x.update(zip([1, 2], ['one', 'two']))
```

- setdefault와 update의 차이 : 전자는 키-값 쌍 추가만 가능하고 수정은 불가, 업데이트는 수정가능! setdefault로 이미 있는 키 값 저장해도 값 안바뀜
- 딕셔너리 키-값 삭제하기

```python
x.pop('키')
del x['키']

# 마지막 키 값 삭제
x.popitem()

# 모든 키-값 삭제
x.clear()
```

- 딕셔너리 복사할 때 copy는 중첩 카피가 완전히 복사되지 않으므로 완전히 복사하려면 deepcopy를 사용해야 함



출처: [코딩 도장](https://dojang.io/course/view.php?id=7)

