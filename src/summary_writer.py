from pathlib import Path


def save_project_summary(total_files, success_count, failed_count, file_type_count, total_time):
    # Make sure reports folder exists
    Path("reports").mkdir(exist_ok=True)

    # Open project summary file in write mode
    with open("reports/project_summary.md", "w") as summary:

        summary.write("# Project Summary Report\n\n")

        summary.write(f"Total Files Analyzed: {total_files}\n")
        summary.write(f"Successful Analyses: {success_count}\n")
        summary.write(f"Failed Analyses: {failed_count}\n")
        summary.write(f"Total Processing Time: {total_time} seconds\n\n")

        summary.write("## File Types Analyzed\n\n")

        for file_type, count in file_type_count.items():
            summary.write(f"- {file_type}: {count}\n")