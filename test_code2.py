# 간단한 저장소 분석 + 리스트 평균 계산 + 파일 내용 읽기
# 일부러 오타/버그 포함

import os

def calculate_average(numbers):
    # 버그1: sum에 변수 이름이 잘못됨 (number → numbers)
    total = sum(number)
    # 버그2: 괄호 누락
    average = total / len(numbers
    return average


def list_python_files(path="."):
    # 주어진 경로 내의 파이썬 파일을 리스트업
    py_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


def read_file(file_path):
    # 버그3: 파일 열기 모드 잘못 입력 ('r' 대신 'read')
    with open(file_path, 'read', encoding='utf-8') as f:
        content = f.read()
    return content


def main():
    print("=== 테스트 시작 ===")

    # 평균 계산 테스트
    numbers = [1, 2, 3, 4, 5]
    print("평균 계산 중...")
    avg = calculate_average(numbers)
    print(f"평균값: {avg}")

    # 파이썬 파일 목록 보기
    print("\n현재 디렉토리의 .py 파일 목록:")
    py_files = list_python_files(".")
    for f in py_files:
        print(f)

    # 파일 읽기 테스트
    if py_files:
        print("\n첫 번째 파일 읽기 시도:")
        content = read_file(py_files[0])
        print(content[:100])  # 앞부분만 출력

    print("\n=== 테스트 끝 ===")


if __name__ == "__main__":
    main()


# 내용 변경 확인 주석
