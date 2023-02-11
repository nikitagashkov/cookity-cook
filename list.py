import os
import pathlib
import re
import argparse

pattern = re.compile(r"```ingredients(.+?)```", re.DOTALL)


def parse_ingredients(text: str) -> list[str]:
    """Parse all ingredients from a recipe file."""
    ingredients = []

    for match in pattern.findall(text):
        for line in match.strip().splitlines():
            ingredients.append(line.strip())

    return ingredients


def main() -> None:
    parser = argparse.ArgumentParser(description="List ingredients for a recipe.")
    parser.add_argument("paths", type=pathlib.Path, nargs="+", help="Path to recipe file.")

    args = parser.parse_args()

    ingredients = []

    for path in args.paths:
        ingredients.extend(parse_ingredients(path.read_text()))

    print(os.linesep.join(sorted(ingredients)))


if __name__ == "__main__":
    main()
