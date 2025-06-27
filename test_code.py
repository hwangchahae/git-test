def calculate_average(numbers):
    # 'number' 대신 'numbers'로 변수명 수정
    total = sum(numbers)
    # 괄호 닫기 추가
    average = total / len(numbers)
    return average

# 함수 호출 예제
print(calculate_average([1, 2, 3, 4, 5]))
```

주요 변경 사항:
- `sum(number)`에서 `number`를 `numbers`로 수정하여 올바른 변수명을 사용하도록 했습니다.
- `len(numbers`에서 괄호를 닫지 않은 오류를 수정하여 `len(numbers)`로 변경했습니다.

이 수정은 `calculate_average` 함수가 정상적으로 작동하도록 보장합니다. 이 변경 사항을 GitHub에 푸시하려면, 로컬 저장소에서 커밋을 생성하고 원격 저장소에 푸시해야 합니다.