def calculate_average(numbers):
    # 'sum(number)' 대신 'sum(numbers)'로 수정하여 리스트 전체의 합을 구하도록 수정
    total = sum(numbers)
    # 괄호를 닫아주어 구문 오류를 수정
    average = total / len(numbers)
    return average

# 평균을 계산하여 출력
print(calculate_average([1, 2, 3, 4, 5]))
```

위 코드에서는 두 가지 오류를 수정했습니다:
1. `sum(number)`를 `sum(numbers)`로 수정하여, 리스트의 모든 요소를 합산하도록 했습니다.
2. `len(numbers`의 괄호를 닫아 `len(numbers)`로 수정하여 구문 오류를 해결했습니다.

이제 이 코드는 주어진 숫자 리스트의 평균을 올바르게 계산하여 출력할 것입니다.