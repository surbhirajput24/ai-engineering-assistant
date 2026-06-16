def classify_build_error(content):

    content_lower = content.lower()

    if "namespace not specified" in content_lower:
        return "NAMESPACE_ERROR"

    elif "manifest merger failed" in content_lower:
        return "MANIFEST_MERGE_ERROR"

    elif "duplicate class" in content_lower:
        return "DUPLICATE_CLASS_ERROR"

    elif "could not resolve" in content_lower:
        return "DEPENDENCY_RESOLUTION_ERROR"

    elif "failed to resolve" in content_lower:
        return "DEPENDENCY_RESOLUTION_ERROR"

    elif "cannot find symbol" in content_lower:
        return "JAVA_COMPILE_ERROR"

    elif "unresolved reference" in content_lower:
        return "KOTLIN_COMPILE_ERROR"

    elif "compile sdk" in content_lower:
        return "COMPILE_SDK_ERROR"

    elif "minsdk" in content_lower:
        return "MIN_SDK_ERROR"

    elif "gradle sync failed" in content_lower:
        return "GRADLE_SYNC_ERROR"

    return "UNKNOWN_BUILD_ERROR"