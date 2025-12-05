# change.py

from pathlib import Path

fps = Path(__file__).parent.glob("**/*tutorial*")
for fp in fps:

    new_fp = fp.parent / (fp.stem.replace("tutorial", "exercises") + ".md")
    # make the new fp

    with open(new_fp, "w") as f:
        f.write(
            f"# {new_fp.stem.replace("0", "").replace('-', ' ').replace("exercises", 'exercises:')}"
        )
