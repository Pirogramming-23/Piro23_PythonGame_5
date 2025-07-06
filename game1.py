# Return은 게임에서 진 사람 이름으로,,,

def play(player_name, participants):
    print("\n==========================🍻 좋아 GAME START 🍻==========================")
    print("🌸 술도 마셨는데~ 좋아게임 할까~?!")
    print("(다같이) 좋아!! 좋아!! 좋아좋아조아!!!!!")
    print("🌸 게임 시작 🌸")
    print("룰: [이름] 좋아 라고 지목 → 상대는 '나도 좋아' 또는 '칵 퉤'로 응답\n")

    # ban_count 초기화 없으면 추가
    for p in participants:
        if "ban_count" not in p:
            p["ban_count"] = 0

    questioner = player_name

    while True:
        print(f"\n==========================")
        print(f"현재 질문자: {questioner}")

        # 질문자가 지목
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

        print(f"😍 {questioner} 님이 {target} 님에게 좋아를 보냈습니다!")

        # 응답
        while True:
            answer = input(f"{target} 👉 '나도 좋아' or '칵 퉤' 선택 : ").strip()
            if answer == "나도 좋아":
                print(f"❤️ {target} 님이 '나도 좋아'로 응답!")
                questioner = target
                break
            elif answer == "칵 퉤":
                print(f"🤮 {target} 님이 칵 퉤!!!")
                # 질문자 카운트 +1
                for p in participants:
                    if p["name"] == questioner:
                        p["ban_count"] += 1
                        print(f"⚠️ {questioner} 거절 횟수: {p['ban_count']}회")
                        if p["ban_count"] >= 3:
                            print(f"🍻 {questioner} 님이 칵 퉤 3번 당했습니다! 벌주 드세요!")
                            p["ban_count"] = 0  # 초기화
                            return questioner
                # 거절되면 질문자 유지
                print(f"⚠️ 질문자는 계속 {questioner} 님입니다!")
                break
            else:
                print("⚠️ '나도 좋아' 또는 '칵 퉤'만 입력 가능합니다.")

