# formation.py

from node_pool import ALL_NODES

# set line as list by formations
# [ ] is line, and in each line node(position) goes in

FORMATIONS = {
    "442": {
        "lines": [
            ["GK"],
            ["LB", "LCB", "RCB", "RB"],
            ["LM", "LCM", "RCM", "RM"],
            ["LST", "RST"]
        ]
    },
    "433 (정석)": {
        "lines": [
            ["GK"],
            ["LB", "LCB", "RCB", "RB"],
            ["LCM", "CM", "RCM"],
            ["LW", "RW"],
            ["ST"]
        ]
    },
    "433 (원볼란치)": {
        "lines": [
            ["GK"],
            ["LB", "LCB", "RCB", "RB"],
            ["CDM"],
            ["LCM", "RCM"],
            ["LW", "RW"],
            ["ST"]
        ]
    },
    "4231": {
        "lines": [
            ["GK"],
            ["LB", "LCB", "RCB", "RB"],
            ["LDM", "RDM"],
            ["CAM"],
            ["LW", "RW"],
            ["ST"]
        ]
    },
    "352": {
        "lines": [
            ["GK"],
            ["LCB", "CB", "RCB"],
            ["CDM"],
            ["LWB-A", "LCM", "RCM", "RWB-A"],
            ["LST", "RST"]
        ]
    },
    "343": {
        "lines": [
            ["GK"],
            ["LCB", "CB", "RCB", "LWB-A", "LCM", "RCM", "RWB-A"],
            ["LW", "RW"],
            ["ST"]
        ]
    },
    "532": {
        "lines": [
            ["GK"],
            ["LWB-D", "LCB", "CB", "RCB", "RWB-D"],
            ["LCM", "CM", "RCM"],
            ["LST", "RST"]
        ]
    },
    "541": {
        "lines": [
            ["GK"],
            ["LWB-D", "LCB", "CB", "RCB", "RWB-D"],
            ["LM", "LCM", "RCM", "RM"],
            ["ST"]
        ]
    },
    "4141": {
        "lines": [
            ["GK"],
            ["LB", "LCB", "RCB", "RB"],
            ["CDM"],
            ["LM", "LCM", "RCM", "RM"],
            ["ST"]
        ]
    },
    "4222": {
        "lines": [
            ["GK"],
            ["LWB-D", "LCB", "RCB", "RWB-D"],
            ["LDM", "RDM"],
            ["LCM", "RCM"],
            ["LST", "RST"]
        ]
    },
    "4312": {
        "lines": [
            ["GK"],
            ["LB", "LCB", "RCB", "RB"],
            ["CDM"],
            ["LCM", "RCM"],
            ["CAM"],
            ["LST", "RST"]
        ]
    }
}

def get_flat_node_list(formation_name):
    """
    return 1D list by the given formation_name
    ex) "442" -> ['GK', 'LB', 'LCB', 'RCB', 'RB', 'LM', 'LCM', 'RCM', 'RM', 'LST', 'RST']
    """
    formation = FORMATIONS.get(formation_name)
    if formation is None:
        raise ValueError(f"Formation '{formation_name} is not defined.")
    flat_list = []
    for line in formation["lines"]:
        flat_list.extend(line)
    return flat_list

def get_line_info(formation_name):
    """
    return node(position) list by the given formation_name
    """
    formation = FORMATIONS.get(formation_name)
    if formation is None:
        raise ValueError(f"Formation '{formation_name} is not defined.")
    return formation["lines"]

if __name__ == "__main__":
    for name in FORMATIONS:
        print(f"formation: {name}")
        print("  flat node list:", get_flat_node_list(name))
        print("  line composition:")
        for idx, line in enumerate(get_line_info(name), start=1):
            # can also print the descriptions by each line with formation
            line_info0 = [f"{pos} ({ALL_NODES[pos]['desc']})" for pos in line]
            print(f"    line {idx}: {line_info0}")
        print("-" * 50)