# Detect what kind of file we are analyzing

def detect_file_type(file_name):

    if file_name.endswith(".java"):
        return "JAVA_CODE"

    elif file_name.endswith(".py"):
        return "PYTHON_CODE"

    elif file_name.endswith(".xml"):
        return "ANDROID_XML"

    elif file_name.endswith(".gradle"):
        return "GRADLE_FILE"

    elif file_name.endswith(".txt"):
        return "BUILD_LOG"

    elif file_name.endswith(".sql"):
        return "SQL_QUERY"

    else:
        return "UNKNOWN"