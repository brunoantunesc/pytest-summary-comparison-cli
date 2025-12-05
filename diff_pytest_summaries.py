#!/usr/bin/env python3

import re
import sys
from collections import defaultdict

def parse_summary(summary_text: str):
    categories = defaultdict(set)
    line_regex = re.compile(r"^(FAILED|XFAIL|XPASS|SKIPPED)\s+([^\s]+)")

    for line in summary_text.splitlines():
        m = line_regex.match(line.strip())
        if m:
            category, testname = m.groups()
            categories[category].add(testname)

    return categories


def compare_summaries(base, new):
    base_parsed = parse_summary(base)
    new_parsed = parse_summary(new)

    return {
        "fixed": base_parsed["FAILED"] - new_parsed["FAILED"],
        "regressions": new_parsed["FAILED"] - base_parsed["FAILED"],
        "now_xpass": new_parsed["XPASS"] - base_parsed["XPASS"],
        "now_xfail": new_parsed["XFAIL"] - base_parsed["XFAIL"],
        "skip_removed": base_parsed["SKIPPED"] - new_parsed["SKIPPED"],
        "skip_added": new_parsed["SKIPPED"] - base_parsed["SKIPPED"],
    }


def read_block(prompt):
    print(prompt)
    print("(Paste the whole text summary and then press ENTER twice)")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


def print_section(title, items):
    count = len(items)
    print(f"--- {title} — {count} ---")
    if items:
        for t in sorted(items):
            print("  ", t)
    else:
        print("  (none)")
    print()


def main():
    base = read_block("\n=== Paste the starting Summary ===")
    new  = read_block("\n=== Paste the summary after modifications ===")

    diff = compare_summaries(base, new)

    print("\n======= Summary diffs =======\n")

    print_section("🔧 Corrected (before FAILED → after OK)", diff["fixed"])
    print_section("❌ Regressions (before OK → after FAILED)", diff["regressions"])
    print_section("🟢 Now XPASS", diff["now_xpass"])
    print_section("⚠️ Now XFAIL", diff["now_xfail"])
    print_section("⏭️ Skips removed", diff["skip_removed"])
    print_section("⏩ Skips added", diff["skip_added"])


if __name__ == "__main__":
    main()
