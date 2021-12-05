# Side channel 세미나를 위한 간단한 예시

## 연습할 시 소스코드를 볼 수 없다고 생각하고 풀어주시기 바랍니다.

문제들은 아래에 적힌 파일입니다.

- writefile.py
- runtime.py
- exitcode.py
- error.py
- query.py

Python 3.8에서 만들어졌으므로 그 이전 버전에서는 안 돌아갈 수도 있습니다.

> 최소 Python 3.6 이상은 써주세요

## 문제풀이 가이드

> This program will execute your python code to...

이 문구가 뜨는 문제는 stdin에서 파이썬 코드를 받아서 문제가 명시한 함수를 호출합니다.

이때 주어진 코드는 다음과 같은 조건에서 실행됩니다:

- Flag는 'flag'라는 전역 변수 (global variable)로 접근 가능합니다.
- 주어진 코드가 한 번 실행된 이후, 명시된 함수만 추출되어 실행됩니다.
  - 파일 내 별도로 정의된 함수는 실행이 안 되기 때문에 함수 내 함수로 정의하시길 바랍니다.
- 별도의 안내가 없을 경우, 다음 기본 함수의 사용이 제한됩니다.
  - compile
  - eval
  - exec
  - input
  - memoryview
  - open
  - print
  - \_\_import__ (import 구문)
  - globals
  - locals
  - vars
  - getattr

그 외에 다른 입력을 요구하는 문제는 안내에 맞게 입력값을 넣어주면 됩니다.

## Flag 형식

{flag_[A-Za-z0-9_]+}