"""Tools for the Smart Agriculture Assistant."""

CROP_WATER = {
    "tomato": 1200,
    "rice": 2000,
    "cotton": 1500,
}


def get_crop_water(crop_name):
    """Return water requirement for a crop in litres per acre."""

    crop = crop_name.strip().lower()

    water = CROP_WATER.get(crop)

    if water is not None:
        return water

    return f"Unknown crop: {crop_name}"