def main():
    user_input = input("File Name: ").lower().strip()
    return media_type(user_input)


def media_type(file_name):
    media_type = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
        ".bin": "application/octet-stream",
        ".csv": "text/csv",
        ".css": "text/css",
        ".doc": "application/msword",
        ".mp3": "audio/mpeg",
        ".mp4": "video/mp4",
    }

    for key, value in media_type.items():
        if file_name.endswith(key):
            return value


print(main())
