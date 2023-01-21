import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).parent


def main():
    relative_links = []

    for path in root.glob("recipes/**/*.md"):
        relative_path = path.relative_to(root / "recipes")
        relative_links.append(str(relative_path.with_suffix(".html")))

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
                "--standalone",
                "--output",
                output,
            ],
            stdout=sys.stdout,
            stderr=sys.stderr,
            check=True,
        )

    index_md = ""

    for path in sorted(relative_links):
        index_md += f"* [{path}]({path})\n"

    subprocess.run(
        [
            "pandoc",
            "--from",
            "commonmark",
            "--to",
            "html",
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



if __name__ == "__main__":
    main()
