def calculate_average(numbers):
    # 'sum(number)' 대신 'sum(numbers)'로 수정하여 올바른 변수명을 사용
    total = sum(numbers)
    # 괄호가 닫히지 않은 오류 수정
    average = total / len(numbers)
    return average

# 함수 호출 예제
print(calculate_average([1, 2, 3, 4, 5]))
```

주요 변경 사항:
1. `sum(number)`를 `sum(numbers)`로 수정하여 올바른 변수명을 사용했습니다.
2. `len(numbers`의 괄호가 닫히지 않은 오류를 수정하여 `len(numbers)`로 변경했습니다.

이러한 수정은 `calculate_average` 함수가 정상적으로 작동하도록 합니다. 이 코드는 이제 주어진 숫자 리스트의 평균을 올바르게 계산할 것입니다.