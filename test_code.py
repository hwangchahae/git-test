def calculate_average(numbers):
    # 'number' 대신 'numbers'로 수정하여 sum 함수가 올바르게 작동하도록 수정
    total = sum(numbers)
    # 괄호 누락 수정하여 평균 계산이 올바르게 수행되도록 수정
    average = total / len(numbers)
    return average

# 평균 계산 함수 호출 및 결과 출력
print(calculate_average([1, 2, 3, 4, 5]))
```

주요 변경 사항:
1. `sum(number)`에서 `sum(numbers)`로 수정하여 `sum` 함수가 올바르게 작동하도록 했습니다.
2. `len(numbers`에서 괄호를 닫아 `len(numbers)`로 수정하여 구문 오류를 해결했습니다.

이 수정은 `calculate_average` 함수가 주어진 숫자 리스트의 평균을 올바르게 계산하고 반환하도록 합니다.