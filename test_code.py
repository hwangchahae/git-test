def calculate_average(numbers):
    # 'number'가 아니라 'numbers'를 사용하여 리스트의 합계를 계산
    total = sum(numbers)
    # 괄호를 닫아 평균을 계산
    average = total / len(numbers)
    return average

# 평균 계산 함수 호출 및 결과 출력
print(calculate_average([1, 2, 3, 4, 5]))
```

위의 코드에서 두 가지 오류를 수정했습니다:
1. `sum(number)`에서 `number` 대신 `numbers`를 사용하여 리스트의 합계를 올바르게 계산하도록 수정했습니다.
2. `average = total / len(numbers`에서 괄호가 닫히지 않은 문제를 해결했습니다. 이제 `len(numbers)`로 리스트의 길이를 올바르게 계산합니다.

이제 `calculate_average` 함수는 주어진 숫자 리스트의 평균을 정확히 계산하고 출력합니다.