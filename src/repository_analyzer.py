def generate_repository_summary(
    repository_name,
    analyzed_files,
    analyses,
    health_score=None,
    insights=None,
    risk_level=None
    
):

    summary = f"""
# Repository Analysis Report

Repository: {repository_name}

Files Analyzed: {len(analyzed_files)}
"""

    if health_score is not None:
        summary += f"\nRepository Health Score: {health_score}/10\n"

    if risk_level is not None:
        summary += f"\nRepository Risk Level: {risk_level}\n"

    if insights:
        summary += f"""
## Repository Insights

- Total Items: {insights["total_items"]}
- Files Analyzed: {insights["files_analyzed"]}
- README Present: {insights["readme_present"]}
- LICENSE Present: {insights["license_present"]}
- SRC Folder Present: {insights["src_present"]}
- Tests Present: {insights["tests_present"]}
"""

    summary += "\n## Files\n"

    for file_name in analyzed_files:
        summary += f"\n- {file_name}"

    summary += "\n\n## AI Analysis Summary\n"

    for index, analysis in enumerate(analyses):
        summary += f"\n### File {index + 1}\n"
        summary += analysis[:800]
        summary += "\n\n"

    return summary

def get_first_n_files(contents, max_files=5):

    selected_files = []

    for item in contents:

        if item["type"] == "file":

            selected_files.append(item)

        if len(selected_files) >= max_files:
            break

    return selected_files


def calculate_health_score(contents, analyses):
    score = 0

    file_names = []

    for item in contents:
        file_names.append(item["name"].lower())

    if "readme.md" in file_names:
        score += 2

    if "license" in file_names:
        score += 2

    if "src" in file_names:
        score += 2

    if "tests" in file_names or "test" in file_names:
        score += 2

    issue_keywords = [
        "critical",
        "security issue",
        "bug",
        "error",
        "vulnerability"
    ]

    issue_count = 0

    for analysis in analyses:
        analysis_lower = analysis.lower()

        for keyword in issue_keywords:
            if keyword in analysis_lower:
                issue_count += 1

    if issue_count == 0:
        score += 2
    elif issue_count <= 2:
        score += 1

    return min(score, 10)

def generate_repository_insights(contents, analyzed_files):
    file_names = []

    for item in contents:
        file_names.append(item["name"].lower())

    total_items = len(contents)
    files_analyzed = len(analyzed_files)

    readme_present = "Yes" if "readme.md" in file_names else "No"
    license_present = "Yes" if "license" in file_names else "No"
    src_present = "Yes" if "src" in file_names else "No"
    tests_present = "Yes" if "tests" in file_names or "test" in file_names else "No"

    return {
        "total_items": total_items,
        "files_analyzed": files_analyzed,
        "readme_present": readme_present,
        "license_present": license_present,
        "src_present": src_present,
        "tests_present": tests_present
    }

def calculate_risk_level(health_score):
    if health_score >= 8:
        return "LOW"
    elif health_score >= 5:
        return "MEDIUM"
    else:
        return "HIGH"