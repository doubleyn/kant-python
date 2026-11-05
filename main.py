# 클래스 정의(선언) : 붕어빵 틀
class User:
    def __init__(self, name): # 생성자 : 클래스가 처음 생성될 때 자동으로 호출
        self.name = name # 변수를 초기화

    def show(self): # 메서드(Method)
        return f"회원 이름: {self.name}"

# 인스턴스 생성 : 붕어빵 만들기
user_a = User("손흥민")

# User 클래스로 생성한 인스턴스 (메모리에 생성)

# 클래스의 인스턴스 변수
print(user_a.name)

# 클래스의 메서드 접근
print(user_a.show())


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f""


account_a = BankAccount("이재현", 100_000)
account_c = BankAccount("홍길동", 200_000)
print([account_a, account_c])