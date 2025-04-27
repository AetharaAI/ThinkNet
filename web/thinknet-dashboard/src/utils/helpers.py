def safe_get(dictionary: dict, keys: list, default=None):
    """
    Safely navigates nested dictionaries.
    """
    for key in keys:
        dictionary = dictionary.get(key, {})
    return dictionary if dictionary else default
