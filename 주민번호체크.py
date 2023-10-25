import re
import random

def is_valid_korean_resident_number(number):
    # 정규 표현식으로 한국의 주민등록번호 형식 확인
    pattern = r"^\d{6}-[1-2]\d{6}$"
    
    if re.match(pattern, number):
        return True
    else:
        return False

def generate_sample_korean_resident_numbers(num_samples):
    sample_numbers = []
    for _ in range(num_samples):
        # 난수로 연도(YY), 월(MM), 일(DD) 생성
        year = f"{random.randint(0, 99):02}"
        month = f"{random.randint(1, 12):02}"
        day = f"{random.randint(1, 31):02}"
        
        # 첫 번째 자리에 1 또는 2를 선택
        first_digit = str(random.choice([1, 2]))
        
        # 나머지 6자리는 무작위 숫자 생성
        rest_digits = "".join([str(random.randint(0, 9)) for _ in range(6)])
        
        # 주민등록번호 생성 및 리스트에 추가
        sample_numbers.append(f"{year}{month}{day}-{first_digit}{rest_digits}")
    
    return sample_numbers

# 10개의 무작위 샘플 주민등록번호 생성
sample_numbers = generate_sample_korean_resident_numbers(10)

# 주민등록번호 유효성 확인 및 출력
for number in sample_numbers:
    if is_valid_korean_resident_number(number):
        print(f"{number}은(는) 유효한 한국의 주민등록번호입니다.")
    else:
        print(f"{number}은(는) 유효하지 않은 한국의 주민등록번호입니다.")
