# 판다스(Pandas) 기본 사용법 익히기
본 글은 판다스(pandas)의 기본 사용법을 소개해 놓은 10 Minutes to pandas 을 번역한 내용입니다. 이에 덧대어 직접 실습을 해 보면서 조금 더 자세한 설명이 필요한 부분을 추가하였습니다. 그러다 보니 원글의 제목과 달리 이를 10분만에 읽어 보기는 쉽지는 않지만, 차근차근 실습을 해 보면서 pandas 의 기본 사용법을 익히시려는 분들께 많은 도움이 되었으면 좋겠습니다.
- 학습한 부분을 md파일로 옮겨적고 있습니다.
- 출처 : https://dandyrilla.github.io/2017-08-12/pandas-10min/#ch1

## 시작하기에 앞서
pandas 를 사용하기 위해서 다음과 같이 모듈을 임포트(import) 합니다. 임포트를 할 때에는 pandas 라는 네임스페이스를 그대로 사용해도 되지만 간결성을 위해 pd 라는 축약된 이름을 관례적으로 많이 사용합니다. 본 실습을 진행하기 위해 pandas 외에도 배열 구조나 랜덤 값 생성 등의 기능을 활용하기 위한 numpy 와 그래프를 그리기 위한 matplotlib 패키지들도 함께 import 해줍니다.
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```