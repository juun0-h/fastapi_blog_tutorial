def truncate_text(text: str, limit: int = 150) -> str:
    if text is not None:
        if len(text) > limit:
            return text[:limit] + "..."
        else:
            return text
    return None


def newline_to_br(newline: str) -> str:
    if newline:
        return newline.replace("\n", "<br>")
    return None