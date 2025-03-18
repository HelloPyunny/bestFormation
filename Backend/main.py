# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

from prediction_model.predict_position_grouped import predict_position_grouped
from prediction_model.predict_position import predict_position
from prediction_model.predict_ovr import predict_ovr_by_position

app  = FastAPI()

# In actual operation, it is recommended to include only the necessary domains in allow_origins.
# For development, ["*"] can be used to allow all origins.
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # OR ["*"]
    allow_credentials=True,
    allow_methods=["*"],         # Allow all HTTP methods
    allow_headers=["*"],         # Allow all Headers
)

# Input data model, key: player_name, value: stat dict
class NewPlayerStats(BaseModel):
    stats: Dict[str, Dict[str, float]]

def predict_new_player(new_player_stats: dict):
    """
    dict that has player's name as key and stat as value
    return: (player name, predicted [Position_Grouped], predicted [Position], OVR of predicted [Position])
    """
    # 1. Prediction model for [Position_Grouped]
    name_pg, pos_group = predict_position_grouped(new_player_stats)
    # 2. Prediction model for [Position]
    name_pos, detailed_pos = predict_position(new_player_stats)
    # 3. Prediction model for [OVR]: for the predicted [Position]
    inner_stats = new_player_stats[list(new_player_stats.keys())[0]]
    overall = predict_ovr_by_position(inner_stats, detailed_pos)
    
    return name_pg, pos_group, detailed_pos, overall

@app.post("/predict")
def predict_endpoint(new_player_stats: NewPlayerStats):
    """
    요청 예시:
    {
      "stats": {
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
    }
    """
    stats = new_player_stats.stats
    name, pos_group, detailed_pos, overall = predict_new_player(stats)
    return {
        "player": name,
        "predicted_position_grouped": pos_group,
        "predicted_position": detailed_pos,
        "OVR": overall
    }






 #######################################################################################################################
'''
if __name__ == '__main__':
    sample_input = {
        "Sanyeop Lee": {
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