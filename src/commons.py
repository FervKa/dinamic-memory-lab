def separator_string(text=None):
    print()
    print(
        f"#-------------------------- {text if text is not None else '- '}"
        f"----------------------------#"
    )
    print()


def cases_string(case=None):
    print()
    print(f"<------ Case: {case} ------>")