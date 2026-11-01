import os
import pandas as pd


def cost_agent(state):

    # ----------------------------
    # Load Parts Database
    # ----------------------------
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(BASE_DIR, "rag_db", "parts.csv")

    parts_db = pd.read_csv(csv_path)

    damaged_parts = state["vision_output"]["damaged_parts"]

    replaced_parts = []
    matched_parts = set()

    parts_cost = 0
    labor_cost = 0

    # ----------------------------
    # Gemini Name Mapping
    # ----------------------------
    PART_MAPPING = {
        "front left fender": "Left Fender",
        "left front fender": "Left Fender",

        "front right fender": "Right Fender",
        "right front fender": "Right Fender",

        "front left headlight assembly": "Left Headlight",
        "left headlight assembly": "Left Headlight",

        "front right headlight assembly": "Right Headlight",
        "right headlight assembly": "Right Headlight",

        "front bumper": "Front Bumper",
        "rear bumper": "Rear Bumper",

        "grille": "Front Grille",

        "left fog light": "Left Fog Light",
        "right fog light": "Right Fog Light",

        "radiator support": "Radiator",
        "cooling fan": "Radiator",

        "front left inner structural components": None,
        "engine bay components": None,
        "cooling system components": None,
        "air intake system": None,
        "frame rail": None,
        "inner structure": None
    }

    # ----------------------------
    # Find Cost
    # ----------------------------
    for part in damaged_parts:

        clean_part = part.split("(")[0].strip().lower()

        # Mapping
        if clean_part in PART_MAPPING:

            if PART_MAPPING[clean_part] is None:
                continue

            search_part = PART_MAPPING[clean_part]

        else:
            search_part = part.split("(")[0].strip()

        # Exact Match
        match = parts_db[
            parts_db["Part"].str.lower() == search_part.lower()
        ]

        # Partial Match
        if match.empty:
            match = parts_db[
                parts_db["Part"].str.lower().apply(
                    lambda x: x in search_part.lower() or search_part.lower() in x
                )
            ]

        if not match.empty:

            row = match.iloc[0]

            # Prevent duplicate entries
            if row["Part"] in matched_parts:
                continue

            matched_parts.add(row["Part"])

            part_price = int(row["parts_cost"])
            labour = int(row["labour_cost"])

            replaced_parts.append({
                "part": row["Part"],
                "part_cost": part_price,
                "labour_cost": labour,
                "total": part_price + labour
            })

            parts_cost += part_price
            labor_cost += labour

    # ----------------------------
    # Final Cost
    # ----------------------------
    total_cost = parts_cost + labor_cost

    state["cost_estimation"] = {
        "replaced_parts": replaced_parts,
        "parts_cost": parts_cost,
        "labor_cost": labor_cost,
        "total_cost": total_cost
    }

    return state