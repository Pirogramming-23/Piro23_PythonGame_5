#딸기 게임
import random
import time

def delayed_print(text, delay=1.0):
    print(text)
    time.sleep(delay)

def play(name, participants):
    delayed_print("="*50)
    delayed_print("\n🧺 ")
    delayed_print("\n🍓딸기🍓 게임을 시작합니다!")
    delayed_print("\n🍓가 좋아")
    delayed_print("\n🍓가 좋아")
    delayed_print("\n 좋아")
    delayed_print("\n 좋아")
    delayed_print("\n 좋아 좋아 좋아")
    delayed_print("\n✨    규칙   ✨")
    delayed_print("\n  1. 각 사람은 턴마다 정해진 개수만큼 '🍓딸기'를 외쳐요!")
    delayed_print("\n  2. 개수는 1~8까지 올라갔다 내려가는 패턴입니다!")
    delayed_print("\n  3. 실수한 사람이 술을 마십니다! 🍺")
    delayed_print("=" * 50)

    pattern = [1,2,3,4,5,6,7,8,7,6,5,4,3,2]
    pattern_index = 0

    user_name = participants[0]['name']
    player_names = [p['name'] for p in participants]
    start_index = player_names.index(name)
    player_names = player_names[start_index:] + player_names[:start_index]
    turn = 0

    while True:
        current_player = player_names[turn % len(player_names)]
        current_count = pattern[pattern_index]

        delayed_print(f"\n🎯 {current_player}님의 차례입니다!")

        if current_player == user_name:
            try:
                user_input = input("몇 번 외치시겠어요? (딸기 몇 번?): ").strip()
                user_count = int(user_input)
                delayed_print(f"😎 {current_player}: {'딸기 ' * user_count}")  # ✅ 먼저 출력

                if user_count != current_count:
                    delayed_print(f"❌ 틀렸습니다! 정답은 {current_count}번이에요!")
                    delayed_print(f"🥴 누가 술을 마셔~ {current_player}이(가) 술을 마셔🍺 ~")
                    return current_player
            except:
                delayed_print(f"❌ 잘못된 입력입니다! 🥴 누가 술을 마셔~ {current_player}이(가) 술을 마셔🍺 ~")
                return current_player
        else:
            time.sleep(1)
            if random.random() < 0.15:
                wrong_count = random.choice([i for i in range(1, 9) if i != current_count])
                delayed_print(f"🙋‍♂️ {current_player}: {'딸기 ' * wrong_count}")
                delayed_print(f"❌ 틀렸습니다! 정답은 {current_count}번이에요!")
                delayed_print(f"🥴 누가 술을 마셔~ {current_player}이(가) 술을 마셔🍺 ~")
                return current_player
            else:
                delayed_print(f"🙋‍♂️ {current_player}: {'딸기 ' * current_count}")

        pattern_index = (pattern_index + 1) % len(pattern)
        turn += 1
        time.sleep(0.5)
