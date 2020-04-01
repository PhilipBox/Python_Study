# 참조 문제를 유발하는 코드
```
def func_1(dataframes):
    users = dataframes["users"]
    users.insert(3, "age", age)
    # dataframes은 main 위치의 data를 참조합니다.
    # dataframes["users"]를 참조하는 users는 결국 main 위치의 data["users"]를 참조합니다.
    # 따라서 insert 작업은 main 위치의 data(원본)에 영향을 줍니다.

def func_2(dataframes):
    users = dataframes["users"]
    users.insert(3, "age", age)
    # dataframes은 main 위치의 data를 참조합니다.
    # dataframes["users"]를 참조하는 users는 결국 main 위치의 data["users"]를 참조합니다.
    # 여기서의 insert 작업도 main 위치의 data(원본)에 영향을 줍니다.
    # 하지만 func_1 함수의 수행으로 원본 데이터에 age라는 column이 이미 추가되어 있으므로 이 부분에서 에러가 발생합니다.

def main():
    data = load_dataframes()
    func_1(data)
    func_2(data)
    ...

if __name__ == "__main__":
    main()
```

# 참조 문제를 유발하지 않는 코드
```
def func_1(dataframes):
    users = dataframes["users"].copy()
    users.insert(3, "age", age)
    # dataframes은 main 위치의 data를 참조합니다.
    # user는 copy() 메소드를 통해 새로운 객체를 할당(복사)받으므로 원본 데이터를 참조하지 않습니다.
    # 따라서 이 부분의 insert 작업은 main 위치의 data(원본)에 영향을 주지 않습니다.

def func_2(dataframes):
    users = dataframes["users"].copy()
    users.insert(3, "age", age)
    # dataframes은 main 위치의 data를 참조합니다.
    # user는 copy() 메소드를 통해 새로운 객체를 할당(복사)받으므로 원본 데이터를 참조하지 않습니다.
    # 따라서 이 부분의 insert 작업은 main 위치의 data(원본)에 영향을 주지 않습니다.

def main():
    data = load_dataframes()
    func_1(data)
    func_2(data)
    ...

if __name__ == "__main__":
    main()
```


**관련 커밋 : https://lab.ssafy.com/s02-bigdata-sub1/s02p21c149/commit/2ad086e3f8e5ca5a55090e9eb9d01fe48ad2e76e**


**관련 자료 : https://stackoverflow.com/questions/27673231/why-should-i-make-a-copy-of-a-data-frame-in-pandas**