import streamlit as st
from pathlib import Path
import sys
from utils.images import render_image, load_site_image

sys.path.append(str(Path(__file__).parent.parent))
from utils.data import SITE_DATA, COLORS, UI_TEXT

st.set_page_config(
    page_title="Gallery | Greek Escape",
    page_icon="📷",
    layout="wide"
)

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    h1, h2, h3 {{ font-family: 'Playfair Display', serif; }}
    p {{ font-family: 'Inter', sans-serif; line-height: 1.8; }}
    
    .page-header {{
        background: linear-gradient(135deg, {COLORS['dark']} 0%, {COLORS['sea']} 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 3rem;
        color: white;
    }}
    
    .gallery-item {{
        position: relative;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        background: white;
    }}
    
    .gallery-item:hover {{
        transform: scale(1.03);
        box-shadow: 0 12px 30px rgba(0,0,0,0.2);
    }}
    
    .gallery-item:hover .overlay {{
        opacity: 1;
    }}
    
    .image-placeholder {{
        width: 100%;
        height: 350px;
        background: linear-gradient(135deg, {COLORS['light_gray']} 0%, #E0E0E0 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: {COLORS['dark']};
        font-size: 0.85rem;
        text-align: center;
        padding: 1rem;
    }}

      /* Para que las imágenes se ajusten correctamente dentro del contenedor */
    .gallery-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
        display: block;
    }}
    
    .overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
        padding: 2rem 1.5rem 1.5rem 1.5rem;
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    
    .caption {{
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0;
    }}
    
    .meta {{
        color: rgba(255,255,255,0.8);
        font-size: 0.85rem;
        margin-top: 0.3rem;
    }}
    
    .filter-button {{
        padding: 0.6rem 1.5rem;
        margin: 0.3rem;
        background: white;
        border: 2px solid {COLORS['primary']};
        color: {COLORS['primary']};
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: 600;
        font-size: 0.95rem;
    }}
    
    .filter-button:hover {{
        background: {COLORS['primary']};
        color: white;
    }}
    
    .stats-badge {{
        display: inline-block;
        background: {COLORS['secondary']};
        color: {COLORS['dark']};
        padding: 0.5rem 1.2rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.5rem;
        font-size: 1rem;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="page-header">
    <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">📷 Photo Gallery</h1>
    <p style="font-size: 1.3rem; opacity: 0.9;">Visual journey through Greece's most stunning destinations</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown(f"""
<div style="max-width: 800px; margin: 0 auto 3rem auto; text-align: center;">
    <p style="font-size: 1.2rem; line-height: 1.8; color: {COLORS['dark']};">
        From ancient temples kissed by golden sunsets to pristine beaches with crystal waters, 
        explore the visual splendor of Greece through our curated collection.
    </p>
</div>
""", unsafe_allow_html=True)

# Gallery Stats
col1, col2, col3, col4 = st.columns(4)

stats = [
    {"icon": "🏛️", "count": "Ancient Sites"},
    {"icon": "🏖️", "count": "Beaches"},
    {"icon": "⛰️", "count": "Mountains"},
    {"icon": "🏘️", "count": "Villages"}
]

for col, stat in zip([col1, col2, col3, col4], stats):
    with col:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 3rem;">{stat['icon']}</div>
            <div style="font-size: 0.9rem; color: {COLORS['dark']}; margin-top: 0.5rem;">{stat['count']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Filters
st.markdown("### 🔍 Filter Gallery")

col1, col2 = st.columns(2)

with col1:
    regions = list(set([img['region'] for img in SITE_DATA['gallery_images']]))
    selected_region = st.selectbox("Filter by Region", ["All Regions"] + regions, key="region_filter")

with col2:
    types = list(set([img['type'] for img in SITE_DATA['gallery_images']]))
    selected_type = st.selectbox("Filter by Type", ["All Types"] + types, key="type_filter")

st.markdown("<br>", unsafe_allow_html=True)

# Filter images
filtered_images = SITE_DATA['gallery_images']

if selected_region != "All Regions":
    filtered_images = [img for img in filtered_images if img['region'] == selected_region]

if selected_type != "All Types":
    filtered_images = [img for img in filtered_images if img['type'] == selected_type]

# Results count
st.markdown(f"""
<div style="text-align: center; margin-bottom: 2rem;">
    <span class="stats-badge">Showing {len(filtered_images)} of {len(SITE_DATA['gallery_images'])} images</span>
</div>
""", unsafe_allow_html=True)

# Display gallery
if not filtered_images:
    st.markdown(f"""
    <div style="text-align: center; padding: 4rem; background: {COLORS['light_gray']}; border-radius: 12px;">
        <h3 style="color: {COLORS['dark']}; margin-bottom: 1rem;">🔍 No Images Found</h3>
        <p style="color: {COLORS['dark']};">{UI_TEXT['empty_state']}</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Masonry-style grid
    cols_per_row = 3
    rows = [filtered_images[i:i+cols_per_row] for i in range(0, len(filtered_images), cols_per_row)]
    
    for row_idx, row in enumerate(rows):
        cols = st.columns(len(row))
        
        for col_idx, (col, image) in enumerate(zip(cols, row)):
            with col:
                # Alternate heights for masonry effect
                height = 400 if (row_idx + col_idx) % 2 == 0 else 350

                # Cargar la imagen usando Base64
                img_html = render_image(image['filename'], class_name="gallery-image", alt=image['caption'])

                # Generar HTML para cada imagen en la galería
                st.markdown(f"""
                <div class="gallery-item">
                    <div class="image-placeholder" style="height: {height}px;">
                        {img_html} <!-- Imagen cargada dinámicamente -->
                    </div>
                    <div class="overlay">
                        <p class="caption">{image['caption']}</p>
                        <p class="meta">📍 {image['region']} • {image['type'].title()}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

# Featured Collections
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin: 3rem 0 2rem 0;">
    🎨 Featured Collections
</h2>
""", unsafe_allow_html=True)

collections = [
    {
        "title": "Ancient Wonders",
        "description": "Step back in time with temples, ruins, and archaeological marvels",
        "count": "15+ photos",
        "icon": "🏛️"
    },
    {
        "title": "Coastal Paradise",
        "description": "Crystal waters, white cliffs, and pristine beaches await",
        "count": "30+ photos",
        "icon": "🏖️"
    },
    {
        "title": "Mountain Majesty",
        "description": "Epic peaks, hiking trails, and breathtaking alpine vistas",
        "count": "20+ photos",
        "icon": "⛰️"
    }
]

col1, col2, col3 = st.columns(3)

for col, collection in zip([col1, col2, col3], collections):
    with col:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; transition: all 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
            <div style="font-size: 4rem; margin-bottom: 1rem;">{collection['icon']}</div>
            <h3 style="color: {COLORS['primary']}; margin-bottom: 0.8rem; font-size: 1.5rem;">{collection['title']}</h3>
            <p style="color: {COLORS['dark']}; line-height: 1.6; margin-bottom: 1rem;">{collection['description']}</p>
            <span style="background: {COLORS['light_gray']}; padding: 0.4rem 1rem; border-radius: 15px; font-size: 0.85rem; color: {COLORS['dark']}; font-weight: 600;">
                {collection['count']}
            </span>
        </div>
        """, unsafe_allow_html=True)

# Photography Tips
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="background: {COLORS['light_gray']}; padding: 3rem; border-radius: 12px; margin-top: 3rem;">
    <h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin-bottom: 2rem;">
        📸 Photography Tips for Greece
    </h2>
    <br>
""", unsafe_allow_html=True)

tips = [
    {
        "title": "Golden Hour Magic",
        "tip": "Shoot during sunrise or sunset for warm, dramatic lighting on white buildings and temples"
    },
    {
        "title": "Blue Hour at Temples",
        "tip": "Capture ancient sites during twilight when they're illuminated against deep blue skies"
    },
    {
        "title": "Composition with Columns",
        "tip": "Use ancient columns and archways as natural frames for your shots"
    },
    {
        "title": "Local Life",
        "tip": "Visit markets and harbors early morning to capture authentic daily Greek life"
    }
]

col1, col2 = st.columns(2)

for idx, tip in enumerate(tips):
    with col1 if idx % 2 == 0 else col2:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid {COLORS['secondary']};">
            <h4 style="color: {COLORS['primary']}; margin-bottom: 0.5rem;">{tip['title']}</h4>
            <p style="color: {COLORS['dark']}; margin: 0; font-size: 0.95rem; line-height: 1.6;">{tip['tip']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Call to Action
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style=" background: linear-gradient(135deg, {COLORS['dark']} 0%, {COLORS['sea']} 100%); padding: 3rem; border-radius: 12px; text-align: center;">
    <h3 style="color: white; font-size: 2rem; margin-bottom: 1rem;">
        Share Your Greece Photos
    </h3>
    <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 2rem; max-width: 650px; margin-left: auto; margin-right: auto;">
        Captured stunning moments during your Greek adventure? We'd love to feature your photos in our community gallery!
    </p>
    <button style="padding: 1rem 2.5rem; background: {COLORS['secondary']}; color: {COLORS['dark']}; border: none; border-radius: 50px; font-size: 1.1rem; font-weight: 600; cursor: pointer;">
        Submit Your Photos
    </button>
</div>
""", unsafe_allow_html=True)