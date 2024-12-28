"""
Fetch languages in the https://docs.python.org language switcher.

Return a defaultdict mapping language codes to a Boolean indicating
whether it is in the language switcher.
"""
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///
import tomllib
from collections import defaultdict

import requests


def get_languages() -> defaultdict[str, bool]:
    # Languages missing from config.toml are not in production
    in_prod = defaultdict(lambda: False)
    data = requests.get(
        "https://raw.githubusercontent.com/"
        "python/docsbuild-scripts/refs/heads/main/config.toml",
        timeout=10,
    ).text
    languages = tomllib.loads(data)["languages"]
    for code, language in languages.items():
        # Languages in config.toml default to being in production
        in_prod[code] = language.get("in_prod", True)
    return in_prod


def main() -> None:
    languages = get_languages()
    print(languages)
    print("en:", languages["en"])
    print("pl:", languages["pl"])
    print("ar:", languages["ar"])


if __name__ == "__main__":
    main()
