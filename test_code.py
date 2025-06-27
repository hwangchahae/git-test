def calculate_average(numbers):
    # 'sum(number)'를 'sum(numbers)'로 수정하여 리스트 전체의 합을 구하도록 수정
    total = sum(numbers)
    # 괄호가 빠져있던 부분을 수정하여 평균을 올바르게 계산하도록 수정
    average = total / len(numbers)
    return average

# 평균 계산 함수 호출 및 결과 출력
print(calculate_average([1, 2, 3, 4, 5]))
```

주요 변경 사항:
1. `sum(number)`를 `sum(numbers)`로 수정하여 `numbers` 리스트의 합을 올바르게 계산하도록 수정했습니다.
2. `len(numbers` 부분의 괄호가 빠져있던 것을 수정하여 평균 계산이 정상적으로 이루어지도록 했습니다.

이 변경 사항은 `calculate_average` 함수가 주어진 숫자 리스트의 평균을 정확히 계산하도록 합니다.