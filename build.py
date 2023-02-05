import itertools
import pathlib
import shutil
import subprocess
import sys
from typing import NamedTuple

root = pathlib.Path(__file__).parent


class Recipe(NamedTuple):
    relative_path: pathlib.Path
    title: str


def main():
    recipes = []

    for path in root.glob("recipes/**/*.md"):
        with path.open("r") as fd:
            first_line = fd.readline()
            title = first_line.removeprefix("#").strip() or path.stem.replace("-", " ").strip().capitalize()

        relative_path = path.relative_to(root / "recipes")

        recipes.append(
            Recipe(
                relative_path=relative_path.with_suffix(".html"),
                title=title,
            )
        )

        output = root / "_build" / relative_path.with_suffix(".html")
        output.parent.mkdir(exist_ok=True, parents=True)

        subprocess.run(
            [
                "pandoc",
                path.absolute(),
                "--from",
                "commonmark",
                "--to",
                "html",
                "--css",
                "../styles.css",
                "--standalone",
                "--output",
                output,
            ],
            stdout=sys.stdout,
            stderr=sys.stderr,
            check=True,
        )

    categories = []

    for _, recipes in itertools.groupby(recipes, key=lambda r: r.relative_path.parts[0]):
        category = []

        for recipe in recipes:
            category.append(f"* [{recipe.title}]({str(recipe.relative_path)})\n")

        categories.append("".join(sorted(category)))

    index_md = "<hr/>\n".join(categories)

    subprocess.run(
        [
            "pandoc",
            "--from",
            "commonmark",
            "--to",
            "html",
            "--css",
            "styles.css",
            "--standalone",
            "--output",
            root / "_build" / "index.html"
        ],
        input=index_md,
        text=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
        check=True,
    )

    shutil.copy(root / "styles.css", root / "_build" / "styles.css")


if __name__ == "__main__":
    main()
