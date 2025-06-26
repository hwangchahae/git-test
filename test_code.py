def calculate_average(numbers):
    # 'sum(number)' 대신 'sum(numbers)'로 수정하여 리스트 전체의 합을 구하도록 수정
    total = sum(numbers)
    # 괄호가 닫히지 않은 부분을 수정하여 문법 오류 해결
    average = total / len(numbers)
    return average

# 수정된 함수 호출
print(calculate_average([1, 2, 3, 4, 5]))
```

주요 변경 사항:
- `sum(number)`를 `sum(numbers)`로 수정하여 올바른 변수명을 사용했습니다.
- `len(numbers`의 괄호를 닫아 문법 오류를 해결했습니다.

이 수정은 `calculate_average` 함수의 논리적 오류와 문법 오류를 해결하여 정상적으로 평균을 계산할 수 있도록 합니다.