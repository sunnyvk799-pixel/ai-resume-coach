def calculate_score(
    matched: set[str],
    required: set[str]
):
    if not required:
        return 0

    return round(
        len(matched) / len(required) * 100,
        2
    )