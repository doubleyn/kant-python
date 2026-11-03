# 🐍 파이썬 종합 실습 (회원 필터링 · 숫자 맞추기 게임)

---

## 📓 Chapter 06. 종합 실습

지금까지 배운 **리스트 · 딕셔너리 · 조건문 · 반복문**을 함께 사용하는 실습

---

### 실습 1. 마케팅 대상 회원 필터링

**사용 개념:** 딕셔너리의 리스트, `for`, 중첩 `if`, 누적 변수

```python
user_database = [
    {"name": "손흥민", "level": "VIP", "active": True, "point": 15000},
    {"name": "김민재", "level": "Silver", "active": False, "point": 9000},
    {"name": "조규성", "level": "VIP", "active": True, "point": 12000},
    {"name": "이강인", "level": "Gold", "active": True, "point": 8000},
    {"name": "홍명보", "level": "Bronze", "active": False, "point": 1000}
]

total_vip_points = 0   # VIP 포인트 누적
active_user_count = 0  # 활성 회원 수

for user in user_database:
    if user["active"]:              # ① 활성 회원만
        active_user_count += 1

        if user["level"] == "VIP":  # ② 등급별 처리
            total_vip_points += user["point"]
            print(f"[VIP 등급] {user['name']} 회원님에게 VIP 쿠폰이 발행되었습니다.")
        elif user["level"] == "Gold":
            print(f"[Gold 등급] {user['name']} 회원님에게 Gold 쿠폰이 발행되었습니다.")

print(f"\n전체 활성 회원 수: {active_user_count}명")
print(f"활성 VIP 포인트 누적: {total_vip_points}점")
```

```
[VIP 등급] 손흥민 회원님에게 VIP 쿠폰이 발행되었습니다.
[VIP 등급] 조규성 회원님에게 VIP 쿠폰이 발행되었습니다.
[Gold 등급] 이강인 회원님에게 Gold 쿠폰이 발행되었습니다.

전체 활성 회원 수: 3명
활성 VIP 포인트 누적: 27000점
```

> 💡 **포인트**
> - 누적 변수는 반복문 **밖에서** `0`으로 초기화
> - f-string 안에서 딕셔너리 키를 쓸 때는 바깥과 **다른 따옴표** 사용: `f"{user['name']}"`

---

### 실습 2. 숫자 맞추기 게임

**사용 개념:** `random`, `while True`, `input()`, `break` / `continue`, 형 변환

```python
import random

number = random.randint(1, 100)  # 1 ~ 100 사이 난수 (100 포함)
try_count = 0

while True:
    user_input = input("컴퓨터의 숫자를 맞춰보세요 (1 ~ 100): ")

    # ① 종료 입력
    if user_input.lower() == 'q':
        print(f"게임을 종료합니다. 정답은 {number}입니다.")
        break

    # ② 숫자가 아니면 다시 입력
    if not user_input.isdecimal():
        print("숫자만 입력해주세요.")
        continue

    user_number = int(user_input)  # str → int 변환

    # ③ 범위 검사
    if user_number < 1 or user_number > 100:
        print("1부터 100 사이의 숫자를 입력해주세요.")
        continue

    try_count += 1

    # ④ 정답 비교
    if user_number < number:
        print("Up! 더 큰 수입니다.")
    elif user_number > number:
        print("Down! 더 작은 수입니다.")
    else:
        print(f"정답입니다. {try_count}회 만에 성공했습니다.")
        break
```

### 핵심 정리

| 개념 | 설명 |
| --- | --- |
| `random.randint(a, b)` | a 이상 b **이하** 정수 난수 (`range`와 달리 끝 값 포함) |
| `input()` | 입력값은 항상 **문자열(`str`)** |
| `int()` | 문자열 → 정수 변환 |
| `.lower()` | 소문자로 변환 → `Q`, `q` 모두 처리 |
| `.isdecimal()` | 숫자로만 이루어졌는지 검사 (`-30`, 빈 입력은 `False`) |
| `while True` + `break` | 조건을 만족할 때까지 무한 반복 |
| `continue` | 잘못된 입력이면 아래 코드를 건너뛰고 다시 입력받기 |

> ⚠️ 파이썬에는 `++` / `--` 연산자가 없다 → `try_count += 1` 사용

> 💡 **입력 검증 순서:** 종료 확인 → 숫자인지 확인 → 범위 확인 → 로직 실행
> 숫자 확인 전에 `int()` 를 호출하면 문자 입력 시 `ValueError` 가 발생한다.
