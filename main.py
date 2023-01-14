import pathlib
import random

root = pathlib.Path(__file__).parent
breakfasts = [l for l in root.glob("recipes/breakfasts/*.md")]
lunches = [l for l in root.glob("recipes/lunches/*.md")]
dinners = [d for d in root.glob("recipes/dinners/*.md")]


def main() -> None:
    print("breakfast:", random.choice(breakfasts).name)
    print("    lunch:", random.choice(lunches).name)
    print("   dinner:", random.choice(dinners).name)


if __name__ == "__main__":
    main()
