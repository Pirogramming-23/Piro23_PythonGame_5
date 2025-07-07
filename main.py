import random
import time
from game_like import play as game1
from game_bs31 import play as game2
from game_sblike import play as game3
from game_bs31 import play as game4

# 게임 리스트
game_list = [
    ("좋아 게임", game1),
    ("369 게임", game2),
    ("딸기 게임", game3),
    ("베스킨라빈스 31 게임", game4),
]

# 게임 인트로
def show_intro():
    intro_art = r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ___    __    __________  __  ______  __       _________    __  _________
               /   |  / /   / ____/ __ \/ / / / __ \/ /      / ____/   |  /  |/  / ____/
              / /| | / /   / /   / / / / /_/ / / / / /      / / __/ /| | / /|_/ / __/   
             / ___ |/ /___/ /___/ /_/ / __  / /_/ / /___   / /_/ / ___ |/ /  / / /___   
            /_/  |_/_____/\____/\____/_/ /_/\____/_____/   \____/_/  |_/_/  /_/_____/   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ︵(≧o≦)︵ ︵(≧o≦)︵  안주 먹을🍗 시간이⏰ 없어요❌ 마시면서 배우는 술게임🍺🍻 ︵(≧o≦)︵ ︵(≧o≦)︵
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    print(intro_art)
    
    while True:
        answer = input("게임을 진행할까요? (y/n): ").strip().lower()
        if answer == "y":
            print("\n게임을 시작합니다!\n")
            return True
        elif answer == "n":
            print("게임을 종료합니다. 다음에 또 만나요!")
            return False
        else:
            print("⚠️ y 또는 n으로 입력해주세요.")

# 사용자 이름 받기
def get_player_name():
    name = input("🌟 오늘 거하게 취해볼 당신의 이름은? : ").strip()
    while not name:
        print("이름을 입력해주세요!")
        name = input("🌟 오늘 거하게 취해볼 당신의 이름은? : ").strip()
    print(f"\n반가워요, {name}님! 🥳")
    return name

# 주량 선택
def select_drink_limit():
    temp = r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~🍺 소주 기준 당신의 주량은? 🍺~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            🍺 1. 소주 반병 (2잔)
                            🍺 2. 소주 반병에서 한병 (4잔)
                            🍺 3. 소주 한병에서 한병 반 (6잔)
                            🍺 4. 소주 한병 반에서 두병 (8잔)
                            🍺 5. 소주 두병 이상 (10잔)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    print(temp)

    while True:
        choice = input("당신의 치사량(주량)은 얼마만큼인가요? (1~5를 선택해주세요) : ").strip()
        if choice not in ['1', '2', '3', '4', '5']:
            print("⚠️ 1부터 5 사이의 숫자를 입력해주세요!\n")
            continue
        choice = int(choice)
        drink_amount = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}[choice]
        print(f"\n🍺 당신의 주량은 {drink_amount}잔으로 설정되었습니다! 🍺\n")
        break
    return drink_amount

# 친구 초대
def invite_friends(player_name, player_limit):
    participants = [{
        "name": player_name,
        "limit": player_limit,
        "drank": 0
    }]

    names = {"은서": 2, "하연": 4, "연서": 6, "예진": 8, "현도": 10}

    if player_name in names:
        del names[player_name]

    while True:
        try:
            count = int(input("함께 취할 친구들은 얼마나 필요하신가요? (최대 3명까지 초대할 수 있어요!) : "))
            if 1 <= count <= 3:
                break
            else:
                print("⚠️ 1명에서 3명 사이로 입력해주세요!\n")
        except ValueError:
            print("⚠️ 숫자를 입력해주세요!\n")

    friends = random.sample(list(names.items()), count)
    for name, limit in friends:
        participants.append({
            "name": name,
            "limit": limit,
            "drank": 0
        })
        print(f"오늘 함께 취할 친구는 {name}입니다! (치사량: {limit})")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    for p in participants:
        print(f"{p['name']}은(는) 지금까지 {p['drank']}🍺! 치사량까지 {p['limit'] - p['drank']}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return participants

# 게임 진행 라운드
def play_game_round(participants, my_name):
    for player in participants:
        temp = r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~🍺 오늘의 Alcohol Game 🍺~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            🍺 1. {}
                            🍺 2. {}
                            🍺 3. {}
                            🍺 4. {}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""".format(game_list[0][0], game_list[1][0], game_list[2][0], game_list[3][0])
        print(temp)

        if player['name'] == my_name:
            # 내 턴이면 직접 입력
            while True:
                try:
                    choice = int(input(f"{player['name']} (이)가 좋아하는 랜덤 게임 ~ 랜덤 게임 ~ 무슨 게임 ? : "))
                    if 1 <= choice <= len(game_list):
                        print(f"{player['name']} 님이 선택한 게임 번호 : {choice} - {game_list[choice - 1][0]}")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        break
                    else:
                        print("⚠️ 올바른 번호를 입력해주세요.")
                except ValueError:
                    print("⚠️ 숫자를 입력해주세요.")
        else:
            # AI 턴 → 랜덤 선택 + 출력
            answer = input(f"술게임 진행중! {player['name']}의 턴입니다. 그만하려면 'exit', 계속하려면 아무 키나 눌러주세요! : ").strip().lower()
            if answer == 'exit':
                print("게임을 종료합니다!")
                exit()

            choice = random.randint(1, len(game_list))
            print(f"\n🎲 {player['name']} (이)가 게임을 선택 중...")
            time.sleep(1)
            print(f"{player['name']} (이)가 선택한 게임 번호 : {choice} - {game_list[choice - 1][0]}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        _, game_func = game_list[choice - 1]
        drinker_name = game_func(player['name'], participants)

        # 결과 반영
        for p in participants:
            if p["name"] == drinker_name:
                p["drank"] += 1
        show_status(participants)

        for p in participants:
            if p['drank'] >= p['limit']:
                game_over(p['name'])
                exit()

# 상태 출력
def show_status(participants):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for p in participants:
        print(f"{p['name']}은(는) 지금까지 {p['drank']}🍺! 치사량까지 {p['limit'] - p['drank']}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 게임 종료
def game_over(name):
    print("--------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------")
    print(r"""
              _____          __  __ ______    ______      ________ _____  
             / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
            | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
            | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
            | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
             \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
""")
    print("--------------------------------------------------------------------------------------------")
    print(f"{name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t\t🍺 다음에 술 마시면 또 불러주세요~ 안녕! 🍺")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    exit()

# 메인 실행
if __name__ == "__main__":
    if show_intro():
        name = get_player_name()
        limit = select_drink_limit()
        participants = invite_friends(name, limit)
        while True:
            play_game_round(participants, name)
    else:
        exit()
