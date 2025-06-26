def calculate_average(numbers):
    # 'sum(number)'를 'sum(numbers)'로 수정하여 올바른 변수명을 사용합니다.
    total = sum(numbers)
    # 괄호를 닫지 않은 오류를 수정합니다.
    average = total / len(numbers)
    return average

# 수정된 함수를 테스트합니다.
print(calculate_average([1, 2, 3, 4, 5]))
```

주요 변경 사항:
- `sum(number)`를 `sum(numbers)`로 수정하여 올바른 변수명을 사용했습니다.
- `len(numbers`에서 괄호가 닫히지 않은 오류를 수정하여 `len(numbers)`로 변경했습니다.

이 수정으로 인해 `calculate_average` 함수가 제대로 작동하며, 리스트의 평균을 올바르게 계산할 수 있습니다.