def calculate_average(numbers):
    # 'sum(number)'를 'sum(numbers)'로 수정하여 올바른 변수명을 사용
    total = sum(numbers)
    # 괄호를 닫지 않은 오류 수정
    average = total / len(numbers)
    return average

# 함수 호출 예시
print(calculate_average([1, 2, 3, 4, 5]))
```

주요 변경 사항:
- `sum(number)`를 `sum(numbers)`로 수정하여 올바른 변수명을 사용했습니다.
- `len(numbers`에서 괄호가 닫히지 않은 오류를 수정하여 `len(numbers)`로 변경했습니다.

이 수정은 `calculate_average` 함수가 주어진 숫자 리스트의 평균을 올바르게 계산할 수 있도록 합니다.