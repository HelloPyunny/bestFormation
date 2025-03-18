# node_pool.py

"""
node_pool.py

consider all positions in a soccer field and consider them a node
we will import this file for other files as (from node_pool import ALL_NODES)

there is a concept called 'line' here that represents literally the line in a soccer field

line 0 = Goalkeeper line | includes: GK
line 1 = Defender line | includes: LWB-D, LB, LCB, CB, RCB, RB, RWB-D
line 2 = Center Defending Midfielder/Attacking Wing Back line | includes: LWB-A, LDM, CDM, RDM, RWB-A
line 3 = Midfielder line | includes: LM LCM CM RCM RM
line 4 = Attacking Midfielder and Wings | includes: LW LAM CAM RAM RW
line 5 = Striker line | includes: LST ST RST

and 'desc' is just a description :)
"""
ALL_NODES = {
    # line 0 = Goalkeeper line | includes: GK
    "GK": {"line": 0, "desc": "Goalkeeper"},
    
    # line 1 = Defender line | includes: LWB-D, LB, LCB, CB, RCB, RB, RWB-D
    "LWB-D": {"line": 1, "desc": "Left Wingback (Attacking)"},
    "LB":    {"line": 1, "desc": "Left Back"},
    "LCB":   {"line": 1, "desc": "Left Center Back"},
    "CB":    {"line": 1, "desc": "Center Back"},
    "RCB":   {"line": 1, "desc": "Right Center Back"},
    "RB":    {"line": 1, "desc": "Right Back"},
    "RWB-D": {"line": 1, "desc": "Right Wingback (Defensive)"},

    # line 2 = Center Defending Midfielder/Attacking Wing Back line | includes: LWB-A, LDM, CDM, RDM, RWB-A
    "LWB-A": {"line": 2, "desc": "Left Wingback (Attacking)"},
    "RWB-A": {"line": 2, "desc": "Right Wingback (Attacking)"},
    "CDM":   {"line": 2, "desc": "Center Defensive Midfielder"},
    "LDM":   {"line": 2, "desc": "Left Defensive Midfielder"},
    "RDM":   {"line": 2, "desc": "Right Defensive Midfielder"},

    # line 3 = Midfielder line | includes: LM LCM CM RCM RM
    "LM":    {"line": 3, "desc": "Left Midfielder"},
    "LCM":   {"line": 3, "desc": "Left Center Midfielder"},
    "CM":    {"line": 3, "desc": "Center Midfielder"},
    "RCM":   {"line": 3, "desc": "Right Center Midfielder"},
    "RM":    {"line": 3, "desc": "Right Midfielder"},

    # line 4 = Attacking Midfielder and Wings | includes: LW LAM CAM RAM RW
    "LW":    {"line": 3, "desc": "Left Winger"},
    "LAM":   {"line": 3, "desc": "Left Attacking Midfielder"},
    "CAM":   {"line": 3, "desc": "Center Attacking Midfielder"},
    "RAM":   {"line": 3, "desc": "Right Attacking Midfielder"},
    "RW":    {"line": 3, "desc": "Right Winger"},

    # line 5 = Striker line | includes: LST ST RST
    "ST":    {"line": 4, "desc": "Striker"},
    "LST":   {"line": 4, "desc": "Left Striker"},
    "RST":   {"line": 4, "desc": "Right Striker"}
}