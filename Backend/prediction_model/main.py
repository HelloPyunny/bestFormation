# main.py

from predict_position_grouped import predict_position_grouped
from predict_position import predict_position
from predict_ovr import predict_ovr_by_position

def predict_new_player(new_player_stats: dict):
    """
    new_player_stats: 선수 이름을 key로 하고, 해당 선수의 스탯 dict를 value로 갖는 dict.
    
    반환: (선수 이름, 예측된 포지션 그룹, 예측된 세부 포지션, 해당 포지션 기준 OVR)
    """
    # 1. Prediction model for [Position_Grouped]
    name_pg, pos_group = predict_position_grouped(new_player_stats)
    # 2. Prediction model for [Position]
    name_pos, detailed_pos = predict_position(new_player_stats)
    # 3. Prediction model for [OVR]: for the predicted [Position]
    inner_stats = new_player_stats[list(new_player_stats.keys())[0]]
    overall = predict_ovr_by_position(inner_stats, detailed_pos)
    
    return name_pg, pos_group, detailed_pos, overall

if __name__ == '__main__':
    sample_input = {
        "이상엽": {
            "PAC": 60.0, "SHO": 65.0, "PAS": 71.0, "DRI": 76.0, "DEF": 67.0, "PHY": 74.0, 
            "Acceleration": 70.0, "Sprint Speed": 62.0, "Positioning": 72.0, "Finishing": 68.0, 
            "Shot Power": 74.0, "Long Shots": 72.0, "Volleys": 69.0, "Penalties": 75.0, 
            "Vision": 75.0, "Crossing": 70.0, "Free Kick Accuracy": 67.0, "Short Passing": 76.0, 
            "Long Passing": 73.0, "Curve": 71.0, "Dribbling": 72.0, "Agility": 64.0, 
            "Balance": 73.0, "Reactions": 66.0, "Ball Control": 73.0, "Composure": 70.0, 
            "Interceptions": 65.0, "Heading Accuracy": 59.0, "Def Awareness": 62.0, 
            "Standing Tackle": 68.0, "Sliding Tackle": 52.0, "Jumping": 59.0, "Stamina": 55.0, 
            "Strength": 77.0, "Aggression": 64.0, "Skill moves": 5.0, "Weak foot": 1.0, "Height": 185.0,
            "GK Diving": 0.0, "GK Handling": 0.0, "GK Kicking": 0.0, 
            "GK Positioning": 0.0, "GK Reflexes": 0.0
        }
    }
    
    # Basic prediction
    name, pos_group, detailed_pos, overall = predict_new_player(sample_input)
    
    print(f"Player: {name}")
    print(f"Predicted Position_Grouped: {pos_group}")
    print(f"Predicted Position: {detailed_pos}")
    print(f"{detailed_pos} OVR: {overall:.2f}")
    
    # inner_stats is basically the sample_input's inner stat dict
    inner_stats = sample_input[list(sample_input.keys())[0]]
    
    # iterate until quit
    while True:
        user_choice = input("Want to check the OVR of other position? (Y/N): ").strip().lower()
        if user_choice != 'y':
            print("End Program.")
            break
        override_position = input("Type the position code (ex: ST, CB, etc): ").strip()
        new_overall = predict_ovr_by_position(inner_stats, override_position)
        print(f"OVR for: {override_position}")
        print(f"{override_position}OVR: {new_overall:.2f}")

'''
        "Kylian Mbappé": {
            "PAC": 97.0, "SHO": 90.0, "PAS": 80.0, "DRI": 92.0, "DEF": 36.0, "PHY": 78.0, 
            "Acceleration": 97.0, "Sprint Speed": 97.0, "Positioning": 93.0, "Finishing": 94.0, 
            "Shot Power": 90.0, "Long Shots": 83.0, "Volleys": 84.0, "Penalties": 84.0, 
            "Vision": 83.0, "Crossing": 78.0, "Free Kick Accuracy": 69.0, "Short Passing": 86.0, 
            "Long Passing": 71.0, "Curve": 80.0, "Dribbling": 93.0, "Agility": 93.0, 
            "Balance": 82.0, "Reactions": 93.0, "Ball Control": 92.0, "Composure": 88.0, 
            "Interceptions": 38.0, "Heading Accuracy": 73.0, "Def Awareness": 26.0, 
            "Standing Tackle": 34.0, "Sliding Tackle": 32.0, "Jumping": 88.0, "Stamina": 88.0, 
            "Strength": 77.0, "Aggression": 64.0, "Skill moves": 5.0, "Weak foot": 4.0, "Height": 182.0,
            "GK Diving": 0.0, "GK Handling": 0.0, "GK Kicking": 0.0, 
            "GK Positioning": 0.0, "GK Reflexes": 0.0
        }
        }
'''