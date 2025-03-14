# predict_ovr.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer

# load data
df = pd.read_csv('../../data/player_data/data_updated.csv')

# set features
selected_features = ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY', 'Acceleration',
       'Sprint Speed', 'Positioning', 'Finishing', 'Shot Power', 'Long Shots',
       'Volleys', 'Penalties', 'Vision', 'Crossing', 'Free Kick Accuracy',
       'Short Passing', 'Long Passing', 'Curve', 'Dribbling', 'Agility',
       'Balance', 'Reactions', 'Ball Control', 'Composure', 'Interceptions',
       'Heading Accuracy', 'Def Awareness', 'Standing Tackle', 'Sliding Tackle', 
       'Jumping', 'Stamina', 'Strength', 'Aggression', 'Skill moves',
       'Weak foot', 'Height']
target = 'OVR'

# divide data by Position
positions = df['Position'].unique()
position_models = {}

for pos in positions:
    pos_data = df[df['Position'] == pos]
    X = pos_data[selected_features]
    y = pos_data[target]
    
    if len(X) < 30:  # filter if not enough data
        continue
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    position_models[pos] = model
    print(f"Position {pos} model trained. (Sample size: {len(X_train)})")

def predict_ovr_by_position(new_stats: dict, target_position: str):
    """
    new_stats: MUST NEED THE SAME KEYS IN selected_features
    target_position: position for prediction (ex: 'ST', 'CB' etc).
    """
    if target_position not in position_models:
        raise ValueError(f"No trained model for: {target_position}")
    model = position_models[target_position]
    
    # select only the 'selected_features' in new_status
    filtered_stats = {feat: new_stats[feat] for feat in selected_features if feat in new_stats}
    new_data = pd.DataFrame([filtered_stats])
    predicted_ovr = model.predict(new_data)[0]
    return predicted_ovr

'''
# 예시 사용
if __name__ == '__main__':
    sample_stats = {
        "PAC": 97.0, "SHO": 90.0, "PAS": 80.0, "DRI": 92.0, "DEF": 36.0, "PHY": 78.0, 
        "Acceleration": 97.0, "Sprint Speed": 97.0, "Positioning": 93.0, "Finishing": 94.0, 
        "Shot Power": 90.0, "Long Shots": 83.0, "Volleys": 84.0, "Penalties": 84.0, 
        "Vision": 83.0, "Crossing": 78.0, "Free Kick Accuracy": 69.0, "Short Passing": 86.0, 
        "Long Passing": 71.0, "Curve": 80.0, "Dribbling": 93.0, "Agility": 93.0, 
        "Balance": 82.0, "Reactions": 93.0, "Ball Control": 92.0, "Composure": 88.0, 
        "Interceptions": 38.0, "Heading Accuracy": 73.0, "Def Awareness": 26.0, 
        "Standing Tackle": 34.0, "Sliding Tackle": 32.0, "Jumping": 88.0, "Stamina": 88.0, 
        "Strength": 77.0, "Aggression": 64.0, "Skill moves": 5.0, "Weak foot": 4.0, "Height": 182.0
    }
    
    # 예를 들어, 같은 스탯을 가지고 공격수(ST) 모델과 센터백(CB) 모델을 사용하여 예측
    try:
        ovr_st = predict_ovr_by_position(sample_stats, "ST")
        ovr_cb = predict_ovr_by_position(sample_stats, "CB")
        print("ST에서 예측된 OVR:", ovr_st)
        print("CB에서 예측된 OVR:", ovr_cb)
    except ValueError as e:
        print(e)
'''