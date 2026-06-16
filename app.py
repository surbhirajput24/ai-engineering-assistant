import time
import streamlit as st

from src.file_type_detector import detect_file_type
from src.llm_factory import get_llm_response
from src.github_url_parser import parse_github_url
from src.github_client import get_repository_info, get_repository_contents, get_file_content
from src.build_error_classifier import classify_build_error
from src.prompt_builder import build_prompt, build_android_expert_prompt
from src.repository_analyzer import (
    generate_repository_summary,
    get_first_n_files,
    calculate_health_score,
    generate_repository_insights,
    calculate_risk_level,
)


def create_prompt_for_file(
    file_type,
    file_name,
    content,
    user_instruction
):
    if file_type == "BUILD_LOG":
        build_error_type = classify_build_error(content)

        st.write(f"Detected Android Error Type: {build_error_type}")

        return build_android_expert_prompt(
            build_error_type,
            content,
            user_instruction
        )

    else:
        return build_prompt(
            file_type,
            file_name,
            content,
            user_instruction
        )


st.sidebar.title("AI Engineering Assistant")
st.sidebar.write("Analyze code and Android build errors using AI.")
st.sidebar.write("Current Version: 1.0")

selected_model = st.sidebar.selectbox(
    "Select AI Provider",
    ["Gemini", "OpenAI"]
)

max_files_to_analyze = st.sidebar.slider(
    "Files to Analyze from GitHub Repo",
    min_value=1,
    max_value=10,
    value=5,
)

st.title("AI Engineering Assistant")
st.write("Welcome Surbhi 🚀")
st.write("Analyze code, Android build errors and GitHub repositories using AI.")
st.write(f"Selected Provider: {selected_model}")

user_instruction = st.text_area(
    "What do you want AI to focus on?",
    placeholder="If You want to give any specific prompt"
)


st.header("GitHub Repository Analysis")

repo_url = st.text_input("Enter GitHub Repository URL")

if repo_url:
    try:
        owner, repo = parse_github_url(repo_url)

        repo_info = get_repository_info(owner, repo)
        contents = get_repository_contents(owner, repo)

        st.success("Repository Found")

        col1, col2, col3 = st.columns(3)
        col1.metric("Repository", repo_info["name"])
        col2.metric("Language", repo_info["language"])
        col3.metric("Stars", repo_info["stargazers_count"])

        if st.button("Analyze Repository Files"):
            selected_files = get_first_n_files(
                contents,
                max_files=max_files_to_analyze,
            )

            analyzed_files = []
            analyses = []

            for file_item in selected_files:
                try:
                    file_name = file_item["name"]
                    analyzed_files.append(file_name)

                    github_file_content = get_file_content(file_item["url"])
                    file_type = detect_file_type(file_name)

                    prompt = create_prompt_for_file(
                        file_type,
                        file_name,
                        github_file_content,
                        user_instruction
                    )

                    with st.spinner(f"Analyzing {file_name}..."):
                        analysis = get_llm_response(selected_model, prompt)

                    analyses.append(analysis)

                except Exception as error:
                    analyses.append(
                        f"Failed to analyze {file_item.get('name', 'unknown file')}: {str(error)}"
                    )

            health_score = calculate_health_score(contents, analyses)
            risk_level = calculate_risk_level(health_score)
            insights = generate_repository_insights(contents, analyzed_files)

            repository_summary = generate_repository_summary(
                repo_info["name"],
                analyzed_files,
                analyses,
                health_score,
                insights,
                risk_level,
            )

            st.metric("Repository Health Score", f"{health_score}/10")
            st.metric("Repository Risk Level", risk_level)

            st.subheader("Repository Insights")

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Items", insights["total_items"])
            col2.metric("Files Analyzed", insights["files_analyzed"])
            col3.metric("README", insights["readme_present"])

            col4, col5, col6 = st.columns(3)
            col4.metric("LICENSE", insights["license_present"])
            col5.metric("SRC Folder", insights["src_present"])
            col6.metric("Tests", insights["tests_present"])

            st.success("Repository Summary Generated")
            st.markdown(repository_summary)

            st.download_button(
                label="Download Repository Summary",
                data=repository_summary,
                file_name=f"{repo_info['name']}_repository_summary.md",
                mime="text/markdown",
            )

        st.subheader("Repository Files")

        file_names = []

        for item in contents:
            if item["type"] == "file":
                file_names.append(item["name"])

        selected_file = st.selectbox("Select Repository File", file_names)

        st.write(f"Selected File: {selected_file}")

        selected_item = None

        for item in contents:
            if item["name"] == selected_file:
                selected_item = item
                break

        if selected_item:
            if st.button("Fetch GitHub File Content"):
                github_file_content = get_file_content(selected_item["url"])

                st.write("GitHub File Content")
                st.code(github_file_content)

                file_type = detect_file_type(selected_file)

                prompt = create_prompt_for_file(
                    file_type,
                    selected_file,
                    github_file_content,
                    user_instruction
                )

                start_time = time.time()

                with st.spinner("Analyzing GitHub file with AI..."):
                    analysis = get_llm_response(selected_model, prompt)

                end_time = time.time()

                processing_time = round(end_time - start_time, 2)
                report_size = round(len(analysis.encode("utf-8")) / 1024, 2)

                st.success("GitHub File Analysis Complete")

                col1, col2, col3 = st.columns(3)
                col1.metric("File Type", file_type)
                col2.metric("Processing Time", f"{processing_time}s")
                col3.metric("Report Size", f"{report_size} KB")

                st.write("AI Analysis")
                st.markdown(analysis)

                st.download_button(
                    label="Download GitHub File Report",
                    data=analysis,
                    file_name=f"{selected_file}_github_analysis_report.md",
                    mime="text/markdown",
                )

    except Exception as error:
        st.error(f"GitHub Error: {str(error)}")


st.header("Upload File Analysis")

uploaded_file = st.file_uploader(
    "Upload a file",
    type=["py", "java", "txt", "xml", "gradle", "sql"],
)

if uploaded_file:
    st.success(f"File uploaded: {uploaded_file.name}")

    content = uploaded_file.getvalue().decode("utf-8")

    st.write("File Content")
    st.code(content)

    if st.button("Analyze Uploaded File"):
        file_type = detect_file_type(uploaded_file.name)

        prompt = create_prompt_for_file(
            file_type,
            uploaded_file.name,
            content,
            user_instruction
        )

        start_time = time.time()

        with st.spinner("Analyzing with AI..."):
            analysis = get_llm_response(selected_model, prompt)

        end_time = time.time()

        processing_time = round(end_time - start_time, 2)
        report_size = round(len(analysis.encode("utf-8")) / 1024, 2)

        st.success("Analysis Complete")

        col1, col2, col3 = st.columns(3)
        col1.metric("File Type", file_type)
        col2.metric("Processing Time", f"{processing_time}s")
        col3.metric("Report Size", f"{report_size} KB")

        st.write("AI Analysis")
        st.markdown(analysis)

        st.download_button(
            label="Download Report",
            data=analysis,
            file_name=f"{uploaded_file.name}_analysis_report.md",
            mime="text/markdown",
        )