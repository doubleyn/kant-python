import random

# 가위 바위 보 게임 미니 프로젝트
print("=" * 30)
print("가위바위보 게임")
print("=" * 30)

dict = {1: "가위", 2: "바위", 3: "보"}

user_name = input("이름을 입력해주세요. : ")
user_streak = 0
user_score = 0
computer_score = 0
score_history = []
retry = True

def get_result(user_pick, computer_pick):
    global user_score
    global computer_score
    global user_streak
    result = (user_pick - computer_pick) % 3
    
    if result == 0:
        return "비김"
    elif result == 1:
        user_score += 1
        user_streak += 1
        return "승리"
    else:
        computer_score += 1
        user_streak = 0
        return "패배"

while(retry):
    computer_pick = random.randint(1, 3)

    print("1. 가위 / 2. 바위 / 3. 보")

    try:
        user_pick = int(input("번호를 선택하세요. : "))
    except:
        print("⚠️ 1 ~ 3 범위에서 골라 주세요.")
        continue

    if (user_pick < 1 or user_pick > 3):
        print("⚠️ 1 ~ 3 범위에서 골라 주세요.")
        continue

    print("\n[게임 결과]")
    print(f"{user_name}: {dict[user_pick]} vs 컴퓨터: {dict[computer_pick]}")
    print(f"=> {get_result(user_pick, computer_pick)}")

    current_score = f"{user_name} {user_score} : {computer_score} 컴퓨터"
    score_history.append(current_score)
    print(f"\n현재 스코어 {current_score}")

    if (user_streak > 0):
        print(f"🚀 현재 {user_streak}연승 중!")

    if (user_score == 2 or computer_score == 2):
        print(f"🎉 최종 승리 : {user_name if user_score == 2 else '컴퓨터'}")
        for i in range(len(score_history)):
            print(f"{i+1}| {score_history[i]}")
        retry = False
        break

    retry_input = input(f"\n다시 도전 (yes/no) : ")
    retry = True if retry_input == "yes" else False