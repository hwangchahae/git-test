def calculate_average(numbers):
    # 'sum(number)' 대신 'sum(numbers)'로 수정하여 리스트 전체의 합을 계산하도록 수정
    total = sum(numbers)
    # 괄호를 닫아주어 문법 오류 수정
    average = total / len(numbers)
    return average

# 수정된 함수 호출
print(calculate_average([1, 2, 3, 4, 5]))
```

### 주요 변경 사항
1. `sum(number)`를 `sum(numbers)`로 수정하여 `numbers` 리스트의 합을 올바르게 계산하도록 수정했습니다.
2. `len(numbers`에서 괄호를 닫아 문법 오류를 수정했습니다.

이 수정은 `calculate_average` 함수가 주어진 숫자 리스트의 평균을 올바르게 계산하도록 합니다. 이 변경 사항은 다른 파일에 영향을 미치지 않으며, Python 코드의 문법 오류를 해결하여 정상적으로 실행될 수 있도록 합니다.