# Django basic(1)

- 모델, 뷰 템플릿 계층

- 모델 계층 : 데이터베이스에 데이터를 읽고 쓸때는 보통 sql을 사용하는데, 장고에서는 파이썬을 이용해 함수를 호출하여 사용할 수 있음
  - 데이터베이스를 설정해주지 않아도 프레임워크 안에서 해결 가능
  - sql은 복잡하게 작성 가능하기 때문에 이것만으로는 한계가 있음

- 뷰 계층 : 비즈니스 로직에 필요한 것들(url 파싱, 요청, 응답)
- 템플릿 계층 : 디자이너에게 친숙한 문법 제공(html 코드)
  - 내가 원하는 데이터를 html로 표현하면서 동시에 변수와 반복문 사용 가능하도록 문법 제공
- 데이터를 정의하고 / 동작하고 / 뭘 보여주고 : 모델, 뷰, 템플릿

## 가상환경 설정

- `pip3 install virtualenv`
  - 한 pc에서 여러프로젝트를 할 수 있기 때문에 프로젝트마다 버전이 다를 수 있으므로 사용
  - `virtualenv django-venv` 라고 치면 방금 입력한 이름으로 폴더가 생성됨
  - 독립된 환경을 위해 폴더를 구축하고 환경을 만든 것
  - 맥의 경우는 `source django-venv/bin/activate`라고 치면 해당 가상환경을 사용하고 있다는 뜻
  - 여기까지 완료되면 `pip3 install Django`
- 가상환경 설정을 완료하면 프로젝트를 해보자
  - `Django-admin startproject mu_community`
    - 앱을 만드는 명령어 `Django-admin startproject`
    - 코드 구조를 만들어줌
  - `cd mu_community`
  - `Django-admin startapp board`

- 프로젝트는 뭐고 앱은 뭐지?
  - 하나의 프로젝트(프로그램)에 여러가지 앱이 있음
  - 묶음 단위로 제공하는 것이 앱(예를들면 위에서 생성한 보드)

## Django의 mvc

- board(앱)폴더 안에 templates폴더 생성
  - 장고에서 사용하는 템플릿 엔진이 각 앱에 템플릿 폴더를 바라보고 있기 때문에 바로 사용할 수 있음
- models.py에는 클래스를 만들어서 모델을 만듦
- view.py에는 def로

- mtv를 만들려면 templates를 만들어주어야 한다. model, view는 자동으로 만들어져있음
- `django-admin startapp muuser`로 생성
- 프로젝트를 등록해야 하는데 mucummunity > settings.py안에 INSTALLED_APPS에 board와 muuser를 넣어주어야 함 -> 그래야 템플릿 사용 가능

## 코드 짜보기

- models.py

```python
from django.db import models

# Create your models here.

class Muuser(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    class meta:
        db_table = 'musical_muuser' # 테이블명 지정
```

- `python3 manage.py makemigrations`
  - 명령어 입력시 필드가 이러이런게 있구나 하면서 db를 이렇게 만들어야겠다..

- `python3 manage.py migrate`
  - 앱들이 사용하는 테이블들을 자동으로 생성
- `sqlite3 db.sqlite3`입력 후 .tables입력서 살펴볼 수 있음
- 데이터베이스 클래스를 변경할 경우 python3 manage.py makemigrations -> python3 manage.py migrate을 통해 코드 관리할 수 있음

## django의 admin

- 기본으로 생성되어 있음
- urls.py를 보면 path('admin/', admin.site.urls)가 있는데 이는 admin 하위는 다 여기로 연결을 하겠다는 의미
- `python3 manage.py runserver`
- `python3 manage.py createsuperuser`를 통해 유저 생성 가능
- username을 알아보기 힘들 때: 이 함수가 없으면 Muuser object라는 이름으로 나옴

```python
def __str__(self):
		return self.username
```

- username뿐 아니라 여러가지 정보를 보고 싶을 때에는 `list_display = ('username', 'password')와 같이 사용할 수 있음`

- 모델명 변경할 때에는 meta클래스 안에
  - verbose_name = '변경할 이름'
  - verbose_name_plural = '복수형은 여기에'

## 회원가입 페이지 만들기

- templates폴더 안에 register.html 파일 생성
- views.py폴더에

```python
def register(request):
    return render(request, 'register.html')
```

- url설정을 해줘야하는데, user와 관련된 url은 muuser.urls에서 관리하겠다.
  - `path('muuser/', include('muuser.urls'))`
- 폼은 서버에 데이터를 전달하는건데, 크로스 도메인을 막기 위해 폼 태그 내부에 {% csrf_token %}을 넣어줌 -> 장고에서는 기본값이므로 꼭 써주자
- 현재 input에 name값이 없음 -> 서버에 들어오면 하나의 키가 됨

- password와 re-password가 같은가, 값이 비었는가 아닌가

```python
# views.py
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None) # .get None은 기본값 저장
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해주세요.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            muuser = Muuser(
                username=username,
                password=make_password(password), # 비밀번호 암호화 저장
            )

            muuser.save()

        return render(request, 'register.html', res_data)
```

