def calculate_average(numbers):
    # 'sum(number)'에서 'sum(numbers)'로 수정하여 리스트 전체의 합을 구하도록 수정
    total = sum(numbers)
    # 괄호가 닫히지 않은 부분 수정
    average = total / len(numbers)
    return average

# 평균 계산 함수 호출
print(calculate_average([1, 2, 3, 4, 5]))
```

위 코드에서는 `sum(number)`를 `sum(numbers)`로 수정하여 리스트의 합을 올바르게 계산하도록 했습니다. 또한, `len(numbers` 부분의 괄호를 닫아 문법 오류를 수정했습니다. 이러한 수정으로 인해 `calculate_average` 함수가 정상적으로 작동하게 됩니다.