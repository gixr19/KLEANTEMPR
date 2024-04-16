import os
import shutil
import tempfile


def clear_directory(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                print(f"Removed {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Removed {item_path}")
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")


def clear_temp_files():
    """ Clears the system's temporary files """
    temp_path = tempfile.gettempdir()
    print(f"Clearing temporary files in {temp_path}")
    clear_directory(temp_path)


def clear_browser_cache():
    """ Clear browser cache for common browsers on Windows """
    paths = {
        "chrome": os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache'),
        "firefox": os.path.expanduser('~\\AppData\\Local\\Mozilla\\Firefox\\Profiles'),
        "edge": os.path.expanduser('~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache')
    }

    for browser, path in paths.items():
        print(f"Clearing cache for {browser.capitalize()}")
        if os.path.exists(path):
            clear_directory(path)
        else:
            print(f"No cache directory found for {browser.capitalize()} at {path}")


def clear_windows_prefetch():
    """ Clear the Windows prefetch files """
    prefetch_path = 'C:\\Windows\\Prefetch'
    print(f"Clearing Windows prefetch files in {prefetch_path}")
    clear_directory(prefetch_path)


def main():
    clear_temp_files()
    clear_browser_cache()
    clear_windows_prefetch()


if __name__ == "__main__":
    main()
