def calculate_average(numbers):
    # 'number' 대신 'numbers'로 수정하여 sum 함수가 올바르게 작동하도록 수정
    total = sum(numbers)
    # 괄호를 닫아 구문 오류를 수정
    average = total / len(numbers)
    return average

# 평균 계산 함수 호출 및 결과 출력
print(calculate_average([1, 2, 3, 4, 5]))
```

위 코드는 `test_code.py` 파일의 오류를 수정한 것입니다. 주요 변경 사항은 다음과 같습니다:
1. `sum(number)`에서 `number`를 `numbers`로 수정하여 올바른 변수명을 사용했습니다.
2. `average = total / len(numbers`에서 괄호를 닫아 구문 오류를 수정했습니다.

이제 이 코드는 정상적으로 작동하여 주어진 숫자 리스트의 평균을 계산하고 출력할 것입니다.