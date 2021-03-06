# 판다스(Pandas) 기본 사용법 익히기
본 글은 판다스(pandas)의 기본 사용법을 소개해 놓은 10 Minutes to pandas 을 번역한 내용입니다. 이에 덧대어 직접 실습을 해 보면서 조금 더 자세한 설명이 필요한 부분을 추가하였습니다. 그러다 보니 원글의 제목과 달리 이를 10분만에 읽어 보기는 쉽지는 않지만, 차근차근 실습을 해 보면서 pandas 의 기본 사용법을 익히시려는 분들께 많은 도움이 되었으면 좋겠습니다.
- 학습한 부분을 md파일로 옮겨적고 있습니다.
- 출처 : https://dandyrilla.github.io/2017-08-12/pandas-10min/#ch1

## 시작하기에 앞서
pandas 를 사용하기 위해서 다음과 같이 모듈을 임포트(import) 합니다. 임포트를 할 때에는 pandas 라는 네임스페이스를 그대로 사용해도 되지만 간결성을 위해 pd 라는 축약된 이름을 관례적으로 많이 사용합니다. 본 실습을 진행하기 위해 pandas 외에도 배열 구조나 랜덤 값 생성 등의 기능을 활용하기 위한 numpy 와 그래프를 그리기 위한 matplotlib 패키지들도 함께 import 해줍니다.
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
## 1. 데이터 오브젝트 생성하기
데이터 오브젝트는 ‘데이터를 담고 있는 그릇’이라고 생각하시면 쉬운데요. 여러분이 pandas 에서 자주 사용하시게 될 데이터 오브젝트는 Series 와 DataFrame 이 있습니다. 이 두 종류의 데이터 오브젝트를 잘 이해하고 사용하는 것이 pandas 의 전부라고 해도 과언이 아닐 정도로 중요합니다. 그렇다면 이 두 종류의 ‘그릇’의 차이점은 무엇일까요? 바로 데이터를 담는 그릇의 ‘형태’가 다른데요. 쉽게 말하자면 **Series 는 1차원 배열로, DataFrame 은 2차원 배열**로 데이터를 담고 있다고 생각하시면 됩니다. 이번 섹션에서는 Series 와 DataFrame 이라는 데이터 오브젝트를 만들어 보는 실습을 해 보겠습니다.
<img src="https://github.com/PhilipBox/Python_Study/blob/master/img/pandas_readme_1.png">
Pandas 의 중요한 데이터 오브젝트 중 하나인 **Series**는 기본적으로 아래와 같이 값의 리스트를 넘겨주어 만들 수 있습니다. 또한 값이 위치하고 있는 정보인 인덱스(index)가 Series 에 같이 저장되게 되는데요. 따로 전달해주지 않는 한 기본적으로 0부터 시작하여 1씩 증가하는 정수 인덱스가 사용됨을 알 수 있습니다.
```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64
```
<br>또 다른 데이터 오브젝트인 **DataFrame**은 여러 형태의 데이터를 받아 생성할 수 있는데요. 그 중 한 방법으로 아래와 같이 numpy array 를 받아 생성이 가능합니다. 앞서 설명드린 것처럼 DataFrame 은 2차원 배열의 형태를 띄고 있습니다. 따라서 우리가 자주 보는 표 형태와 같이 두 가지의 기준에 따라 데이터를 담고 있습니다. 아래의 예제에서는 첫번째 기준은 날짜, 두번째 기준은 장소(A, B, C, D 라는 네 곳의 위치)```1```에 따라 측정된 어떤 값들이 담겨 있다고 생각하면 쉬울 것 같습니다. DataFrame 을 만들기 위해서는 ```pd.DataFrame()``` 라는 클래스 생성자를 사용하며, 행에 해당하는 기준(첫번째 기준)인 인덱스를 ```index``` 라는 인수로 전달하며, 열에 해당하는 기준(두번째 기준)인 컬럼을 ```columns``` 이라는 인수로 전달합니다. 여기에서는 인덱스로 ```pd.date_range()``` 를 사용하여 날짜 값들을 만들어 전달해 주었고, 컬럼의 이름은 A, B, C, D 라는 이름이 담긴 리스트로 넣어보았습니다.
```python
dates = pd.date_range('20130101', periods=6)
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#                   A         B         C         D
# 2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
# 2013-01-04  0.721555 -0.706771 -1.039575  0.271860
# 2013-01-05 -0.424972  0.567020  0.276232 -1.087401
# 2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```
<br>DataFrame 을 생성하는 또 다른 방법으로 아래와 같이 여러 종류의 자료들이 담긴 딕셔너리(dict)를 넣어주어 만들 수 있습니다. 이 때에는 dict 의 key 값이 열을 정의하는 컬럼이 되며, 행을 정의하는 인덱스는 자동으로 0부터 시작하여 1씩 증가하는 정수 인덱스가 사용됩니다.
```
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo
```
DataFrame 의 컬럼들은 각기 특별한 자료형을 갖고 있을 수 있습니다. 이는 DataFrame 내에 있는 dtypes 라는 속성을 통해 확인 가능합니다. 파이썬의 기본적인 소수점은 float64 로 잡히고, 기본적은 문자열은 str 이 아니라 object 라는 자료형으로 나타납니다.
```python
df2.dtypes
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object
```
Jupyter 를 사용하시는 분이라면 ```df2.<TAB>```(‘df2.’까지 입력하고 탭을 누름)을 통해 다음과 같이 dtypes 외에도 다른 속성들이 무엇이 있는지 확인할 수 있습니다.
```python
  In [13]: df2.<TAB>
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.clip_lower
df2.align              df2.clip_upper
df2.all                df2.columns
df2.any                df2.combine
df2.append             df2.combine_first
df2.apply              df2.compound
df2.applymap           df2.consolidate
df2.as_blocks          df2.convert_objects
df2.asfreq             df2.copy
df2.as_matrix          df2.corr
df2.astype             df2.corrwith
df2.at                 df2.count
df2.at_time            df2.cov
df2.axes               df2.cummax
df2.B                  df2.cummin
df2.between_time       df2.cumprod
df2.bfill              df2.cumsum
df2.blocks             df2.D
```
보다시피 컬럼 A, B, C, D 가 자동적으로 생성되어 나타나는 것을 확인할 수 있습니다. 나머지 속성들은 간결성을 위해 생략하였기 때문에 E 도 뒤에 있을 것입니다.
<br>Ipython 을 사용하지 않는 분이라면, python 의 빌트인 함수 ```dir```을 통해 다음과 같이 오브젝트가 갖고 있는 속성 및 메소드들을 모두 확인 가능합니다. (약 400 개가 넘는 항목입니다. 엄청 많습니다.)
```python
dir(df2)
# ['A', 'B', 'C', ... , 'values', 'var', 'where', 'xs']
```
이 외에도 pandas 에서 제공하는 자료 구조들이 무엇이 있는지 알아보시려면 pandas 공식 문서에 있는 [Intro to data structures](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html) 을 참고하시면 됩니다.
