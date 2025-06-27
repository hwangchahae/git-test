def calculate_average(numbers):
    # 'sum(number)'를 'sum(numbers)'로 수정하여 올바른 변수명을 사용
    total = sum(numbers)
    # 괄호가 닫히지 않은 부분을 수정하여 문법 오류 해결
    average = total / len(numbers)
    return average

# 평균 계산 함수 호출 및 결과 출력
print(calculate_average([1, 2, 3, 4, 5]))
```

위의 코드에서 `calculate_average` 함수의 오류를 수정했습니다. `sum` 함수의 인자로 잘못된 변수명이 사용되고 있었고, `len(numbers)` 부분의 괄호가 닫히지 않아 문법 오류가 발생하고 있었습니다. 이 두 가지 문제를 해결하여 코드가 정상적으로 작동하도록 수정하였습니다.