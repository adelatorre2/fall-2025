#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SECTIONS_ROOT = SCRIPT_DIR / "sections"

CHAPTER_SPECS = {
    5: {"folder": "ch5_systems_of_linear_equations", "title": "Systems of Linear Equations", "n_sections": 4},
    6: {"folder": "ch6_functions", "title": "Functions", "n_sections": 5},
    7: {"folder": "ch7_real_numbers_&_pythag-thm", "title": "Real Numbers and the Pythagorean Theorem", "n_sections": 5},
    8: {"folder": "ch8_volume_&_similar_solids", "title": "Volume and Similar Solids", "n_sections": 4},
    9: {"folder": "ch9_data_analysis_&_displays", "title": "Data Analysis and Displays", "n_sections": 4},
    10: {"folder": "ch10_exponents_&_sci-notation", "title": "Exponents and Scientific Notation", "n_sections": 7},
}

# Optional: override section titles here. If not provided, placeholders are used.
# Example key: (5, 1) -> "Solving Systems of Linear Equations by Graphing"
SECTION_TITLES: dict[tuple[int, int], str] = {}

# Optional: override review section title per chapter.
REVIEW_TITLES: dict[int, str] = {}

def ensure_file(path: Path, content: str, overwrite: bool = False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or overwrite:
        path.write_text(content, encoding="utf-8")

def insert_into_master(master_path: Path, input_line: str) -> bool:
    """Insert input_line into master_review.tex before the appendix marker if not already present."""
    if not master_path.exists():
        return False

    text = master_path.read_text(encoding="utf-8")
    if input_line in text:
        return True  # already present

    lines = text.splitlines(True)  # keep newlines

    # Preferred insertion point: right before the appendix section
    markers = [
        "% ---------- Appendix ----------",
        "\\input{sections/appendix}",
    ]

    insert_at = None
    for i, ln in enumerate(lines):
        if any(m in ln for m in markers):
            insert_at = i
            break

    if insert_at is None:
        # Fallback: append at end with a preceding newline
        if not text.endswith("\n"):
            lines.append("\n")
        lines.append("\n" + input_line + "\n")
    else:
        # Ensure there is a blank line before insertion for readability
        prefix = "" if (insert_at > 0 and lines[insert_at-1].strip() == "") else "\n"
        lines.insert(insert_at, prefix + input_line + "\n")

    master_path.write_text("".join(lines), encoding="utf-8")
    return True

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate chapter/section LaTeX scaffolding for chapters 5-10."
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing .tex scaffold files (default: only create missing files)",
    )
    parser.add_argument(
        "--update-master",
        action="store_true",
        help="Insert the generated chapter wrapper into master_review.tex if missing",
    )
    parser.add_argument(
        "--master",
        type=Path,
        default=SCRIPT_DIR / "master_review.tex",
        help="Path to master_review.tex (default: ./master_review.tex next to scaffold.py)",
    )

    args = parser.parse_args(argv)

    created = 0
    wrapper_paths = []

    for ch_num in sorted(CHAPTER_SPECS.keys()):
        spec = CHAPTER_SPECS[ch_num]
        folder = spec["folder"]
        title = spec["title"]
        n_sections = spec["n_sections"]

        chap_dir = SECTIONS_ROOT / folder
        sub_dir = chap_dir / "sections"
        sub_dir.mkdir(parents=True, exist_ok=True)

        inputs = []

        # Create subsection files
        for k in range(1, n_sections + 1):
            tex_name = f"ch{ch_num}.{k}.tex"
            tex_path = sub_dir / tex_name
            before = tex_path.exists()

            section_title = SECTION_TITLES.get((ch_num, k), f"Section {ch_num}.{k}")
            content = f"\\section{{{section_title}}}\n\n\\newpage\n"

            ensure_file(tex_path, content, overwrite=args.overwrite)

            after = tex_path.exists()
            if after and not before:
                created += 1

            inputs.append(f"\\input{{sections/{folder}/sections/{tex_name}}}")

        # Create review file
        review_name = f"ch{ch_num}_review.tex"
        review_path = sub_dir / review_name
        before_review = review_path.exists()

        review_title = REVIEW_TITLES.get(ch_num, f"Chapter {ch_num} Review")
        review_content = f"\\section{{{review_title}}}\n\n\\newpage\n"

        ensure_file(review_path, review_content, overwrite=args.overwrite)

        after_review = review_path.exists()
        if after_review and not before_review:
            created += 1

        inputs.append(f"\\input{{sections/{folder}/sections/{review_name}}}")

        # Create chapter wrapper
        wrapper_path = chap_dir / f"{folder}.tex"
        before_wrapper = wrapper_path.exists()

        wrapper_content = (
            f"\\chapter{{{title}}}\n\n"
            + "\n".join(inputs)
            + "\n\n\\newpage\n"
        )

        ensure_file(wrapper_path, wrapper_content, overwrite=args.overwrite)

        if wrapper_path.exists() and not before_wrapper:
            created += 1

        wrapper_paths.append(wrapper_path)

    print(f"✅ New files created: {created} (use --overwrite to rewrite existing scaffolds)")
    for wp in wrapper_paths:
        print(f"✅ Chapter wrapper: {wp}")

    if args.update_master:
        for ch_num in sorted(CHAPTER_SPECS.keys()):
            folder = CHAPTER_SPECS[ch_num]["folder"]
            input_line = f"\\input{{sections/{folder}/{folder}.tex}}"
            ok = insert_into_master(args.master, input_line)
            if ok:
                print(f"✅ Updated master with: {input_line}")
            else:
                print(f"⚠️  Could not update master (file not found?): {args.master}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())