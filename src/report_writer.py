from pathlib import Path


# Create safe file name for report
def create_report_file_name(file_name):

    # Replace dots with underscores
    safe_name = file_name.replace(".", "_")

    return f"reports/{safe_name}_report.md"


# Save individual report for each file
def save_report(file_name, analysis):

    # Make sure reports folder exists
    Path("reports").mkdir(exist_ok=True)

    # Create report path
    report_path = create_report_file_name(file_name)

    # Write report
    with open(report_path, "w") as report:

        report.write(f"# AI Analysis Report: {file_name}\n\n")

        report.write(analysis)

    return report_path