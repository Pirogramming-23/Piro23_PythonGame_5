# Return은 게임에서 진 사람 이름으로,,,

import random
import sys
import time

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def play(player_name, participants):
    print("\n==========================🍻 좋아 GAME START 🍻==========================")
    print("🌸 술도 마셨는데~ 좋아게임 할까~?!")
    print("(다같이) 좋아!! 좋아!! 좋아좋아조아!!!!!")
    print("🌸 게임 시작 🌸")
    print("룰: [이름] 좋아 → 지목받은 사람은 '나도 좋아' or '칵 퉤'\n")

    # ban_count 초기화
    for p in participants:
        if "ban_count" not in p:
            p["ban_count"] = 0

    questioner = player_name

    while True:
        print("\n==========================")
        print(f"현재 질문자: {questioner}")

        # 내 턴이면 내가 입력
        if questioner == player_name:
            while True:
                cmd = input(f"{questioner} 👉 누구 좋아? '[이름] 좋아' 입력 : ").strip()
                if cmd.endswith(" 좋아"):
                    target = cmd[:-3].strip()
                    valid_names = [p["name"] for p in participants]
                    if target == questioner:
                        print("⚠️ 자기 자신에게는 좋아 못합니다!")
                        continue
                    if target not in valid_names:
                        print("⚠️ 존재하지 않는 이름입니다!")
                        continue
                    break
                else:
                    print("⚠️ '[이름] 좋아' 형태로 입력해주세요.")
        else:
            # 내가 아닌 질문자 → 랜덤 지목
            valid_targets = [p["name"] for p in participants if p["name"] != questioner]
            target = random.choice(valid_targets)
            slow_print(f"{questioner} 👉 랜덤 지목: {target} 좋아!")

        slow_print(f"😍 {questioner} 님이 {target} 님에게 좋아를 보냈습니다!")

        # 지목받은 사람이 나면 → 내가 직접 응답
        if target == player_name:
            while True:
                answer = input(f"{player_name} 👉 '나도 좋아' or '칵 퉤' 선택 : ").strip()
                if answer in ["나도 좋아", "칵 퉤"]:
                    break
                else:
                    print("⚠️ '나도 좋아' 또는 '칵 퉤'만 입력해주세요.")
        else:
            # 내가 아닐때 응답
            answer = random.choice(["나도 좋아", "칵 퉤"])
            slow_print(f"🤔 {target}의 응답: {answer}")

        if answer == "나도 좋아":
            slow_print(f"❤️ {target} 님이 '나도 좋아'로 응답!")
            questioner = target

        elif answer == "칵 퉤":
            slow_print(f"🤮 {target} 님이 칵 퉤!!!")
            # 질문자 카운트 증가
            for p in participants:
                if p["name"] == questioner:
                    p["ban_count"] += 1
                    slow_print(f"⚠️ {questioner} 거절 횟수: {p['ban_count']}회")
                    if p["ban_count"] >= 3:
                        slow_print(f"🍻 {questioner} 님이 칵 퉤 3번 당했습니다! 벌주 드세요!")
                        slow_print(f"👉 누가 술을 마셔~ {questioner}(이)가 마셔~! 🍺")
                        p["ban_count"] = 0
                        return questioner
            # 질문자 유지
            slow_print(f"⚠️ 질문자는 계속 {questioner} 님입니다!")
