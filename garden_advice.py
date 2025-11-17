"""
Garden Advice CLI module.

Provides gardening advice based on season and plant type.
"""

import argparse
from typing import Dict, Tuple

# --- Constants ---

VALID_SEASONS = ("spring", "summer", "autumn", "fall", "winter")
VALID_PLANT_TYPES = (
    "flower", "vegetable", "herb", "shrub", "tree", "succulent"
)


# --- Private Helper Functions ---

def _normalize_season(season: str) -> str:
    """
    Normalize season input to a standard lowercase value.

    Converts "fall" to "autumn".

    :param season: The raw user input for the season.
    :raises TypeError: If the season is not a string.
    :return: A standardized, lowercase season string.
    """
    if not isinstance(season, str):
        raise TypeError("season must be a string")
    s = season.strip().lower()
    if s == "fall":
        s = "autumn"
    return s


def _normalize_plant(plant_type: str) -> str:
    """
    Normalize plant type input to a lowercase string.

    :param plant_type: The raw user input for the plant type.
    :raises TypeError: If the plant_type is not a string.
    :return: A standardized, lowercase plant type string.
    """
    if not isinstance(plant_type, str):
        raise TypeError("plant_type must be a string")
    return plant_type.strip().lower()


# --- Core Function ---

def get_advice(season: str, plant_type: str) -> str:
    """
    Return garden advice for the given season and plant type.

    :param season: The name of the season.
    :param plant_type: The type of the plant.
    :raises ValueError: For unknown or unsupported inputs.
    :return: A string of combined seasonal and plant-specific advice.
    """
    season_norm = _normalize_season(season)
    plant_norm = _normalize_plant(plant_type)

    if season_norm not in VALID_SEASONS:
        raise ValueError(f"Unknown season: {season!r}")
    if plant_norm not in VALID_PLANT_TYPES:
        raise ValueError(f"Unknown plant type: {plant_type!r}")

    # Advice dictionaries with wrapped lines
    seasonal: Dict[str, str] = {
        "spring": (
            "Prepare soil, prune where needed, and start planting "
            "cool-season crops."
        ),
        "summer": (
            "Water regularly (early morning), mulch to retain moisture, "
            "and provide shade if required."
        ),
        "autumn": (
            "Reduce watering, tidy up spent plants, and plant bulbs "
            "for next year."
        ),
        "winter": (
            "Protect tender plants from frost and reduce watering; "
            "inspect for pests indoors."
        ),
    }

    plant_specific: Dict[str, str] = {
        "flower": (
            "Deadhead spent blooms and feed with a balanced fertiliser "
            "to encourage more flowers."
        ),
        "vegetable": (
            "Rotate crops, keep an eye out for pests, and ensure "
            "consistent moisture for roots."
        ),
        "herb": (
            "Harvest regularly to encourage growth; many herbs prefer "
            "well-drained soil."
        ),
        "shrub": (
            "Prune selectively after flowering and check staking "
            "for newly planted shrubs."
        ),
        "tree": (
            "Check for signs of disease, water deeply during dry "
            "spells, and mulch the root zone."
        ),
        "succulent": (
            "Provide well-draining soil, reduce watering in cool "
            "months, and plenty of light."
        ),
    }

    parts: Tuple[str, str] = (
        seasonal.get(season_norm, ""),
        plant_specific.get(plant_norm, "")
    )
    advice = " ".join(p for p in parts if p)
    return advice


# --- CLI Execution ---

def main() -> None:
    """
    Simple Command-Line Interface for getting garden advice.

    Parses arguments for --season and --plant. If they are not
    provided, it prompts the user for input.
    """
    parser = argparse.ArgumentParser(description="Garden Advice CLI")
    parser.add_argument(
        "--season",
        "-s",
        help="Season (spring, summer, autumn/fall, winter)"
    )
    parser.add_argument(
        "--plant",
        "-p",
        help="Plant type (flower, vegetable, herb, shrub, tree, succulent)"
    )
    args = parser.parse_args()

    season = args.season
    plant = args.plant

    try:
        # Prompt for input if arguments are missing
        if not season:
            season = input("Enter season (e.g. summer): ").strip()
        if not plant:
            plant = input("Enter plant type (e.g. flower): ").strip()

        if not season or not plant:
            print("Error: Both season and plant type are required.")
            return

        advice = get_advice(season, plant)

    except (ValueError, TypeError) as err:
        print(f"Error: {err}")
        return

    print("\nGarden Advice\n-------------")
    print(advice)


if __name__ == "__main__":
    main()