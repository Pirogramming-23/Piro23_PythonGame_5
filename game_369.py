# 369 Game

import random
import time

def count_claps(num):
    """숫자에 포함된 3, 6, 9 개수만큼 '짝'을 리턴"""
    return "짝" * sum(1 for d in str(num) if d in ['3', '6', '9'])

def play(name, participants):
    temp=r"""
--------------------------------------------------------------------------------------------
                 _   _ _____ _____ ______    _____          __  __ ______ 
                | \ | |_   _/ ____|  ____|  / ____|   /\   |  \/  |  ____|
                |  \| | | || |    | |__    | |  __   /  \  | \  / | |__   
                | . ` | | || |    |  __|   | | |_ | / /\ \ | |\/| |  __|  
                | |\  |_| || |____| |____  | |__| |/ ____ \| |  | | |____ 
                |_| \_|_____\_____|______|  \_____/_/    \_\_|  |_|______|
                                                                        
--------------------------------------------------------------------------------------------
"""
    time.sleep(0.5)
    print(temp)
    print("❗️ 순서대로 숫자에 3, 6, 9가 들어가면 '짝'이라고 말해야 해요! 들어있는 만큼 '짝짝', '짝짝짝'처럼 해주세요! 틀리면 벌주! 🍺 ❗️")
    time.sleep(0.5)
    print("🍺 3~6~9! 3~6~9! 3~6~9! 3~6~9! 🍺")
    time.sleep(0.5)
    user_name = participants[0]["name"]  # 0번째가 실제 사용자

    current_number = 1
    temp = 0
    turn = 0
    for participant in participants:
        if participant['name'] == name:
            turn = temp
        else:
            temp+=1
    players = [p["name"] for p in participants]

    while True:
        current_player = players[turn % len(players)]
        expected = count_claps(current_number) or str(current_number)
        if current_player == user_name:
            answer = input(f"{user_name}의 차례! 숫자 {current_number} → : ").strip()
            time.sleep(0.5)
        else:
            # 컴퓨터는 85% 확률로 맞추고, 틀릴 때는 무조건 틀리게
            if random.random() < 0.85:
                answer = expected
            else:
                answer = "으아아악 틀렸다!!"
            print(f"→ {current_player} : {answer}")
            time.sleep(0.5)

        if answer != expected:
            print(f"아 누가누가 술을 마셔 😚 {current_player}이(가) 술을 마셔 😜 원~~샷❗️🧨")
            time.sleep(0.5)
            return current_player
        
        turn+=1
        current_number+=1