from collections import defaultdict
import os
import pathlib
import re
import argparse
from typing import NamedTuple

pattern = re.compile(r"```ingredients(.+?)```", re.DOTALL)


class Ingredient(NamedTuple):
    name: str
    quantity: str


def parse_ingredients(text: str) -> list[str]:
    """Parse all ingredients from a recipe file."""
    ingredients = []

    for match in pattern.findall(text):
        for line in match.strip().splitlines():
            name, quantity = line.strip().split(":", maxsplit=1)
            ingredients.append(Ingredient(name=name, quantity=quantity))

    return ingredients


def main() -> None:
    parser = argparse.ArgumentParser(description="List ingredients for a recipe.")
    parser.add_argument("paths", type=pathlib.Path, nargs="+", help="Path to recipe file.")

    args = parser.parse_args()

    ingredients = []

    for path in args.paths:
        ingredients.extend(parse_ingredients(path.read_text()))

    quantities_by_name = defaultdict(list)

    for ingredient in ingredients:
        if quantity := ingredient.quantity.strip():
            quantities_by_name[ingredient.name].append(quantity)

    max_len = max([len(k) for k in quantities_by_name.keys()])

    for name, quantities in sorted(quantities_by_name.items()):
        print(name.ljust(max_len+2), " + ".join(quantities))


if __name__ == "__main__":
    main()
