def calculate_average(numbers):
    # sum() 함수의 인자로 number가 아닌 numbers를 사용하도록 수정
    total = sum(numbers)
    # 괄호를 닫아 구문 오류를 수정
    average = total / len(numbers)
    return average

# 수정된 함수 호출
print(calculate_average([1, 2, 3, 4, 5]))
```

### 주요 변경 사항
1. `sum(number)`를 `sum(numbers)`로 수정하여 `numbers` 리스트의 합계를 올바르게 계산하도록 했습니다.
2. `len(numbers`에서 괄호를 닫지 않아 발생하는 구문 오류를 수정했습니다. `len(numbers)`로 수정하여 리스트의 길이를 올바르게 계산하도록 했습니다.

이러한 수정은 `calculate_average` 함수가 정상적으로 작동하도록 하며, 주어진 숫자 리스트의 평균을 올바르게 계산할 수 있게 합니다.