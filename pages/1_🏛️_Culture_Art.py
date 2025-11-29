import streamlit as st
from pathlib import Path
from utils.images import render_image, load_site_image
import sys

sys.path.append(str(Path(__file__).parent.parent))
from utils.data import SITE_DATA, COLORS, UI_TEXT

st.set_page_config(
    page_title="Culture & Art | Greek Escape",
    page_icon="🏛️",
    layout="wide"
)

# Apply consistent styling
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    h1, h2, h3 {{ font-family: 'Playfair Display', serif; color: {COLORS['dark']}; }}
    p, li {{ font-family: 'Inter', sans-serif; line-height: 1.8; }}
    
    .page-header {{
        background: linear-gradient(135deg, {COLORS['secondary']} 0%, {COLORS['sea']} 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 3rem;
        color: white !important;
    }}
    
    .destination-card {{
        background: white;
        border-radius: 12px;
        padding: 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        overflow: hidden;
        transition: all 0.3s ease;
        margin-bottom: 2rem;
    }}
    
    .destination-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }}
    
    .card-content {{
        padding: 2rem;
    }}
    
    .highlight-badge {{
        display: inline-block;
        background: {COLORS['secondary']};
        color: {COLORS['dark']};
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem 0.3rem 0.3rem 0;
    }}
    
    .best-time {{
        background: {COLORS['olive']};
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        display: inline-block;
        margin-top: 1rem;
        font-weight: 600;
    }}
    
    .image-placeholder {{
        width: 100%;
        height: 350px;
        background: linear-gradient(135deg, {COLORS['light_gray']} 0%, #E0E0E0 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: {COLORS['dark']};
        font-size: 0.9rem;
        text-align: center;
        padding: 1rem;
    }}
    .destination-image {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    border-radius: 12px 12px 0 0;  /* Para coincidir con card */
    }}
</style>
""", unsafe_allow_html=True)

# Page Header
st.markdown("""
<div class="page-header">
    <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">🏛️ Culture & Art</h1>
    <p style="font-size: 1.3rem; opacity: 0.9;">Experience the living heritage of ancient Greece</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown(f"""
<div style="max-width: 800px; margin: 0 auto 4rem auto; text-align: center;">
    <p style="font-size: 1.2rem; line-height: 1.8; color: {COLORS['dark']};">
        Greece's culture is a tapestry woven through millennia. From the marble columns of the Acropolis 
        to contemporary dance festivals under Mediterranean stars, every corner tells a story of artistic 
        excellence and human achievement.
    </p>
</div>
""", unsafe_allow_html=True)

# Main Content
for idx, destination in enumerate(SITE_DATA['culture']):
    
    # Alternate layout
    if idx % 2 == 0:
        col1, col2 = st.columns([1, 1.2])
        img_col, content_col = col1, col2
    else:
        col2, col1 = st.columns([1.2, 1])
        img_col, content_col = col1, col2
    
    with img_col:
        img_html = render_image(destination['image_placeholder'], class_name="destination-image", alt=destination['title'])
        st.markdown(f"""
        <div class="destination-card">
            <div class="image-placeholder">
                {img_html}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with content_col:
        st.markdown(f"""
        <div style="padding: 1rem;">
            <h2 style="color: {COLORS['primary']}; font-size: 2.2rem; margin-bottom: 1rem;">
                {destination['title']}
            </h2>
            <p style="font-size: 1.1rem; color: {COLORS['dark']}; line-height: 1.8; margin-bottom: 1.5rem;">
                {destination['description']}
            </p>
        """, unsafe_allow_html=True)
        
       # Highlights
        highlights_html = "<div class='highlights-container'>"

        for highlight in destination['highlights']:
            highlights_html += f"<span class='highlight-badge'>✨ {highlight}</span>"

        highlights_html += "</div>"

        st.markdown(highlights_html, unsafe_allow_html=True)
                
        # Best time
        st.markdown(f"""
        <div class="best-time">
            🗓️ Best Time: {destination['best_time']}
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

# Additional Cultural Insights
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="background: {COLORS['light_gray']}; padding: 3rem; border-radius: 12px; margin-top: 3rem;">
    <h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin-bottom: 2rem;">
        Cultural Highlights
    </h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

highlights = [
    {
        "icon": "🏺",
        "title": "Ancient Artifacts",
        "text": "Visit world-class museums housing 5,000+ years of Greek art and archaeology"
    },
    {
        "icon": "🎭",
        "title": "Living Traditions",
        "text": "Experience traditional music, dance, and theater in their authentic settings"
    },
    {
        "icon": "🎨",
        "title": "Local Artisans",
        "text": "Meet craftspeople keeping ancient techniques alive in modern workshops"
    }
]

for col, item in zip([col1, col2, col3], highlights):
    with col:
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{item['icon']}</div>
            <h3 style="color: {COLORS['primary']}; margin-bottom: 0.5rem;">{item['title']}</h3>
            <p style="color: {COLORS['dark']};">{item['text']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Call to Action
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, {COLORS['secondary']} 0%, {COLORS['sea']} 100%); border-radius: 12px; margin-top: 3rem;">
    <h3 style="color: white; font-size: 2rem; margin-bottom: 1rem;">Ready to Explore Greek Culture?</h3>
    <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-bottom: 2rem;">
        From ancient ruins to contemporary festivals, your cultural journey awaits
    </p>
    <button style="padding: 1rem 2.5rem; background: {COLORS['secondary']}; color: {COLORS['dark']}; border: none; border-radius: 50px; font-size: 1.1rem; font-weight: 600; cursor: pointer;">
        Plan Your Cultural Tour
    </button>
</div>
""", unsafe_allow_html=True)