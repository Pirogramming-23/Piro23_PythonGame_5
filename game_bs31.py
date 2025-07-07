import random
import time

def play(name, participants):
    print("""🍦 베스킨 라빈스 31~~~~~ 
    귀엽고~~~ 깜찍하게~~~ 31~~!🍦""")
    print("규칙:")
    print("- 각 사람은 1~3개의 숫자를 연속으로 말해요")
    print("- 1부터 시작해서 순서대로 진행해요")
    print("- 31을 말한 사람이 술을 마셔요~ 🍺")
    print("=" * 50)
    
    # 게임 상태 초기화
    current_number = 0
    player_names = [p['name'] for p in participants]
    user_name = participants[0]["name"]

    temp = 0
    turn = 0
    for participant in participants:
        if participant['name'] == name:
            turn = temp
        else:
            temp+=1
    
    # 게임 시작
    while current_number < 31:
        current_player = player_names[turn % len(player_names)]
        print(f"\n현재 숫자: {current_number}")
        print(f"🎯 {current_player}님의 차례입니다!")
        
        if current_player == user_name:
            # 사용자 턴
            while True:
                try:
                    max_count = min(3, 31 - current_number)
                    user_input = input(f"숫자를 말하세요 (예: {current_number + 1} 또는 {current_number + 1},{current_number + 2} 또는 {current_number + 1},{current_number + 2},{current_number + 3}): ").strip()
                    
                    if not user_input:
                        print("숫자를 입력해주세요!")
                        continue
                    
                    # 입력된 숫자들을 파싱
                    numbers = user_input.replace(',', ' ').split()
                    
                    # 각각이 숫자인지 확인
                    parsed_numbers = []
                    for num in numbers:
                        if not num.isdigit():
                            print("숫자만 입력해주세요!")
                            break
                        parsed_numbers.append(int(num))
                    else:
                        # 연속된 숫자인지 확인
                        expected_numbers = []
                        for i in range(len(parsed_numbers)):
                            expected_numbers.append(current_number + i + 1)
                        
                        if parsed_numbers == expected_numbers:
                            # 1-3개 개수 제한 확인 (31이 포함되지 않은 경우만)
                            if 31 not in parsed_numbers and (len(parsed_numbers) < 1 or len(parsed_numbers) > 3):
                                print("1개부터 3개까지만 말할 수 있어요!")
                                continue
                            
                            current_number += len(parsed_numbers)
                            print(f"👤 {name}: {', '.join(map(str, parsed_numbers))}")
                            
                            # 31이 포함되어 있으면 바로 게임 종료
                            if 31 in parsed_numbers:
                                print(f"\n💥 31! {name}님이 31을 말했습니다!")
                                print(f"🍺 {name}님이 술을 마셔야 해요~ 🍺")
                                return name
                            break
                        else:
                            print(f"연속된 숫자를 말해야 해요! (다음 숫자: {current_number + 1})")
                            continue
                    
                except KeyboardInterrupt:
                    print("\n게임을 종료합니다!")
                    return name
                except:
                    print("올바른 형식으로 입력해주세요! (예: 30,31 또는 30 31)")
            
        else:
            # 봇 턴
            time.sleep(1)  # 봇이 생각하는 시간
            
            # 봇의 랜덤 선택 (1-3개)
            remaining = 31 - current_number
            max_choice = min(3, remaining)
            choice = random.randint(1, max_choice)
            
            # 봇이 선택한 숫자들 출력
            numbers_to_say = []
            for i in range(choice):
                current_number += 1
                numbers_to_say.append(str(current_number))
                if current_number >= 31:
                    break
            
            print(f"🤖 {current_player}: {', '.join(numbers_to_say)}")
            
            # 31을 말했는지 확인
            if current_number >= 31:
                print(f"\n💥 31! {current_player}님이 31을 말했습니다!")
                print(f"🍺 {current_player}님이 술을 마셔야 해요~ 🍺")
                return current_player
        
        # 다음 플레이어로 넘어가기
        turn+=1
        
        # 잠시 대기 (게임 진행 속도 조절)
        time.sleep(0.5)
    
    return name
    