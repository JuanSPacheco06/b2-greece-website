import base64
import os

ASSETS_DIR = "assets/images"

def load_image_base64(path: str) -> str:
    """
    Converts any image file into a Base64 HTML <img> compatible string.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"[ERROR] Image not found: {path}")

    with open(path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode("utf-8")

    # Detect format automatically
    ext = path.split(".")[-1]
    return f"data:image/{ext};base64,{encoded}"


def load_site_image(filename: str) -> str:
    """
    Loads an image from assets/images/ using only a filename
    (perfect for SITE_DATA image_placeholder).
    """
    full_path = f"{ASSETS_DIR}/{filename}"
    return load_image_base64(full_path)


def render_image(filename: str, class_name: str = "", alt: str = "") -> str:
    """
    Renders an <img> tag dynamically from site data.
    Use this in st.markdown().
    """
    img64 = load_site_image(filename)
    return f'<img src="{img64}" class="{class_name}" alt="{alt}"/>'
