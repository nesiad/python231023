import re

# 정규 표현식 패턴 (이메일 주소 검사)
# - ^: 문자열의 시작을 나타냄
# - [\w\.-]+: 한 개 이상의 문자, 숫자, 밑줄, 점 또는 대시 문자를 나타냄
# - @: '@' 문자
# - [\w\.-]+: 한 개 이상의 문자, 숫자, 밑줄, 점 또는 대시 문자를 나타냄
# - \.: '.' 문자
# - [a-zA-Z]+: 한 개 이상의 알파벳 문자를 나타냄
# - $: 문자열의 끝을 나타냄
pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$'

# 예시 이메일 주소
sample_emails = [
    "user@example.com",              # 유효한 이메일 주소
    "john.doe1234@gmail.com",        # 유효한 이메일 주소
    "info@company.co.uk",           # 유효한 이메일 주소
    "invalid-email",                # 유효하지 않은 이메일 주소
    "user@.com",                    # 유효하지 않은 이메일 주소
    "user@company.",                # 유효하지 않은 이메일 주소
    "@example.com",                 # 유효하지 않은 이메일 주소
    "user@-website.com",            # 유효하지 않은 이메일 주소
    "user@company.c",               # 유효하지 않은 이메일 주소
    "user@company.123"              # 유효하지 않은 이메일 주소
]

for email in sample_emails:
    if re.search(pattern, email):
        print(f"{email} 는 유효한 이메일 주소입니다.")
    else:
        print(f"{email} 는 유효하지 않은 이메일 주소입니다.")
