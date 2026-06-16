# Common report structure used by all file types
COMMON_OUTPUT_FORMAT = """
Return the response in EXACTLY this format:

SUMMARY:
- Short summary of the file

ISSUES:

Issue 1:
Severity: HIGH / MEDIUM / LOW
Category: Bug / Security / Performance / Best Practice
Explanation:
Suggested Fix:

Issue 2:
Severity: HIGH / MEDIUM / LOW
Category: Bug / Security / Performance / Best Practice
Explanation:
Suggested Fix:

FIXED CODE OR FIX STEPS:
- Provide corrected code if applicable
- If code cannot be fixed directly, provide detailed steps

CONFIDENCE:
HIGH / MEDIUM / LOW
"""


def build_prompt(file_type, file_name, content, user_instruction=""):

    if file_type == "JAVA_CODE":

        prompt = f"""
You are a Senior Android Engineer with 10+ years of experience.


User Instruction:
{user_instruction}

Review the Java code for:
1. Bugs
2. Null Pointer Exceptions
3. Memory Leaks
4. Performance Issues
5. Security Issues
6. Android Best Practices
7. Threading Issues
8. Resource Leaks

{COMMON_OUTPUT_FORMAT}

FILE NAME:
{file_name}

JAVA CODE:
{content}
"""

    elif file_type == "PYTHON_CODE":

        prompt = f"""
You are a Senior Python Engineer.

User Instruction:
{user_instruction}


Review the Python code for:
1. Bugs
2. Logic Errors
3. Performance Issues
4. Security Issues
5. Code Smells
6. Python Best Practices

{COMMON_OUTPUT_FORMAT}

FILE NAME:
{file_name}

PYTHON CODE:
{content}
"""

    elif file_type == "BUILD_LOG":

        prompt = f"""
You are a Senior Android Build Engineer.
User Instruction:
{user_instruction}
Analyze this build failure.

Identify:
1. Root Cause
2. Gradle Issues
3. Dependency Issues
4. AGP Compatibility Issues
5. Manifest Issues
6. Suggested Resolution

{COMMON_OUTPUT_FORMAT}

BUILD LOG:
{content}
"""


    elif file_type == "SQL_QUERY":
        prompt = f"""
    You are a Senior Database Engineer and SQL Performance Reviewer.
User Instruction:
{user_instruction}
    Review this SQL query for:
    1. Syntax issues
    2. Performance problems
    3. Missing WHERE conditions
    4. Risky SELECT * usage
    5. Index recommendations
    6. Security risks like SQL injection
    7. Banking/enterprise database best practices

    {COMMON_OUTPUT_FORMAT}

    FILE NAME:
    {file_name}

    SQL QUERY:
    {content}
    """




    elif file_type == "ANDROID_XML":

        prompt = f"""
You are a Senior Android Engineer.
User Instruction:
{user_instruction}
Review this Android XML file.

Check for:
1. Layout Issues
2. Accessibility Issues
3. Performance Problems
4. Best Practices

{COMMON_OUTPUT_FORMAT}

FILE NAME:
{file_name}

XML CONTENT:
{content}
"""

    elif file_type == "GRADLE_FILE":

        prompt = f"""
You are a Senior Android Build Engineer.
User Instruction:
{user_instruction}
Review this Gradle file.

Check for:
1. Dependency Issues
2. Deprecated Configurations
3. AGP Compatibility
4. Build Performance Improvements

{COMMON_OUTPUT_FORMAT}

FILE NAME:
{file_name}

GRADLE CONTENT:
{content}
"""

    else:

        prompt = f"""
You are a Senior Software Engineer.
User Instruction:
{user_instruction}
Review this file.

{COMMON_OUTPUT_FORMAT}

FILE NAME:
{file_name}

CONTENT:
{content}
"""

    return prompt



def build_android_build_error_prompt(build_error_type, content):

    prompt = f"""
You are a Senior Android Build Engineer.

Analyze this Android build error.

Build Error Type:
{build_error_type}

Return the response in this exact format:

SUMMARY:
- Explain the build failure in 2-3 lines

ROOT CAUSE:
- Explain the most likely reason

FIX STEPS:
1.
2.
3.

FILES TO CHECK:
- Mention files like build.gradle, AndroidManifest.xml, settings.gradle, etc.

CONFIDENCE:
HIGH / MEDIUM / LOW

BUILD LOG:
{content}
"""

    return prompt

def build_android_expert_prompt(
    build_error_type,
    content,
    user_instruction=""
):
    prompt = f"""
You are a Senior Android Build Engineer and Android Studio troubleshooting expert.

Analyze the following Android build error.
USER INSTRUCTION:
{user_instruction}
Android Error Type:
{build_error_type}

Return response in this exact format:

SUMMARY:
- Explain the issue in simple terms.

ROOT CAUSE:
- Explain why this error usually happens.

ANDROID FILES TO CHECK:
- build.gradle
- settings.gradle
- AndroidManifest.xml
- app/build.gradle
- gradle.properties

FIX STEPS:
1.
2.
3.
4.

EXAMPLE FIX:
```gradle
// provide Gradle/XML/Java/Kotlin fix if applicable
PREVENTION:

How to avoid this issue in future.

CONFIDENCE:
HIGH / MEDIUM / LOW

ERROR LOG:
{content}
"""
    return prompt