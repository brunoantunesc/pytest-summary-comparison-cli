# 🔍 pytest-summary-diff

A small command-line tool that compares two **pytest short test
summaries** and highlights the differences between them.

Useful for debugging, CI pipelines, or validating the impact of code
changes.

## ✨ Features

-   Paste your pytest summaries directly into the terminal --- **no
    files needed**
-   Clear, categorized output
-   Shows counts for each category (e.g., "Regressions --- 4")
-   Works on Windows (PowerShell), Linux, and macOS
-   Zero dependencies (pure Python)

## 🚀 Installation

Just download or copy the script:

    diff_pytest_summaries.py

and make sure it's accessible to your Python interpreter.

Optionally, give it execute permission (Linux/macOS):

``` bash
chmod +x diff_pytest_summaries.py
```

## ▶️ Usage

Run:

``` bash
python diff_pytest_summaries.py
```

You will be prompted to paste the **BEFORE** summary:

    === Paste BEFORE summary ===
    (Paste the entire summary, then press ENTER on an empty line)

Then the **AFTER** summary:

    === Paste AFTER summary ===
    (Paste the entire summary, then press ENTER on an empty line)

The script will output something like:

    ======= Differences between summaries =======

    --- 🔧 Fixed (before FAILED → after OK) — 2 ---
       tests/unit/test_example.py::test_something
       tests/unit/test_example.py::test_other

    --- ❌ Regressions (before OK → after FAILED) — 5 ---
       tests/func/test_checkout.py::test_load_file
       ...

    --- 🟢 Now XPASS — 0 ---
      (none)

    --- ⚠️ Now XFAIL — 0 ---
      (none)

    --- ⏭️ Skips removed — 1 ---
       tests/func/test_utils.py::test_case

    --- ⏩ Skips added — 0 ---
      (none)

## 🧠 How It Works

The script:

1.  Reads two text blocks from standard input\
2.  Extracts test entries from the categories:
    -   `FAILED`
    -   `XFAIL`
    -   `XPASS`
    -   `SKIPPED`
3.  Compares each category between BEFORE and AFTER
4.  Prints the differences in a structured summary

No need to parse full pytest output --- only the **short test summary
section** is required.

## 📦 Example Input

You can paste normal pytest summary sections like:

    =========================== short test summary info ============================
    FAILED tests/test_a.py::test_example
    SKIPPED tests/test_b.py::test_something
    XPASS tests/test_c.py::test_feature

The script will detect and compare all categories automatically.

## 🛠 Requirements

-   Python **3.7+**
-   No external libraries

## 📄 License

MIT License --- feel free to modify and use it as you wish.
