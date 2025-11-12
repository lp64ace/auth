import os
import subprocess
from pathlib import Path

# ==============================================
# Build all .tex files in all subfolders to PDFs
# ==============================================

# Change this command if you prefer pdflatex, xelatex, etc.
LATEX_CMD = ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error"]

def compile_tex(tex_path: Path):
    """Compile a single .tex file into PDF."""
    print(f"Compiling: {tex_path}\n")
    try:
        subprocess.run(
            LATEX_CMD + [str(tex_path.name)],
            cwd=tex_path.parent,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8"
        )
        print(f"done\n")
    except subprocess.CalledProcessError as e:
        print(f"failed\n{e.stdout}\n")

def main():
    root = Path(".")
    tex_files = list(root.rglob("*.tex"))

    if not tex_files:
        print("No .tex files found.")
        return

    for tex_file in tex_files:
        # Skip common output folders
        if any(part in {"build", "out", "_output"} for part in tex_file.parts):
            continue
        compile_tex(tex_file)

    print("finished.")

if __name__ == "__main__":
    main()
