import time

from file_scanner import scan_project, read_file_content
from file_type_detector import detect_file_type
from prompt_builder import build_prompt, build_android_build_error_prompt
from ai_client import ask_gemini
from report_writer import save_report
from summary_writer import save_project_summary
from logger import write_log
from build_error_classifier import classify_build_error


def main():
    write_log("Analysis started")

    files = scan_project("samples")

    total_files = len(files)
    success_count = 0
    failed_count = 0
    file_type_count = {}
    total_processing_time = 0

    print(f"Total files found: {total_files}")
    write_log(f"Total files found: {total_files}")

    for file in files:
        print("\n==============================")
        print(f"Analyzing: {file.name}")
        write_log(f"Started analyzing file: {file.name}")

        file_type = detect_file_type(file.name)
        print(f"Detected Type: {file_type}")
        write_log(f"Detected file type for {file.name}: {file_type}")

        file_type_count[file_type] = file_type_count.get(file_type, 0) + 1

        content = read_file_content(file)
        #prompt = build_prompt(file_type, file.name, content)
        if file_type == "BUILD_LOG":
            build_error_type = classify_build_error(content)
            write_log(f"Build error type for {file.name}: {build_error_type}")
            prompt = build_android_build_error_prompt(build_error_type, content)
        else:
            prompt = build_prompt(file_type, file.name, content)

        start_time = time.time()

        try:
            analysis = ask_gemini(prompt)
            success_count += 1
            write_log(f"Successfully analyzed file: {file.name}")

        except Exception as error:
            failed_count += 1
            analysis = f"""
ERROR DURING ANALYSIS

File: {file.name}
Detected Type: {file_type}

Error:
{str(error)}
"""
            write_log(f"Error analyzing file {file.name}: {str(error)}")

        end_time = time.time()
        processing_time = round(end_time - start_time, 2)
        total_processing_time += processing_time

        report_path = save_report(file.name, analysis)

        print(f"Report saved: {report_path}")
        print(f"Processing Time: {processing_time} seconds")

        write_log(f"Report saved for {file.name}: {report_path}")
        write_log(f"Processing time for {file.name}: {processing_time} seconds")

    save_project_summary(
        total_files,
        success_count,
        failed_count,
        file_type_count,
        round(total_processing_time, 2)
    )

    write_log("Project summary saved: reports/project_summary.md")
    write_log("Analysis completed")

    print("\nProject summary saved: reports/project_summary.md")
    print("All files analyzed successfully ✅")


if __name__ == "__main__":
    main()