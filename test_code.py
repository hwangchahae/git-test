def calculate_average(numbers):
    # 'number'를 'numbers'로 수정하여 sum 함수가 올바르게 작동하도록 수정
    total = sum(numbers)
    # 괄호가 닫히지 않은 부분을 수정하여 문법 오류 해결
    average = total / len(numbers)
    return average

# 평균 계산 함수 호출 및 결과 출력
print(calculate_average([1, 2, 3, 4, 5]))
```

주요 변경 사항:
1. `sum(number)`에서 `number`를 `numbers`로 수정하여 올바른 변수명을 사용하도록 했습니다.
2. `len(numbers`에서 괄호가 닫히지 않은 부분을 수정하여 문법 오류를 해결했습니다.