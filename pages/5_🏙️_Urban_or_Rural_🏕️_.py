import streamlit as st
from pathlib import Path
import sys
from utils.images import render_image, load_site_image

sys.path.append(str(Path(__file__).parent.parent))
from utils.data import SITE_DATA, COLORS, UI_TEXT

st.set_page_config(
    page_title="Urban or Rural? | Greek Escape",
    page_icon="🏙️",
    layout="wide"
)

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    h1, h2, h3 {{ font-family: 'Playfair Display', serif; }}
    p {{ font-family: 'Inter', sans-serif; line-height: 1.8; }}
    
    .page-header {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['olive']} 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 3rem;
        color: white;
    }}
    
    .stat-card {{
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
    }}
    
    .stat-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }}
    
    .stat-icon {{
        font-size: 3rem;
        margin-bottom: 1rem;
    }}
    
    .stat-value {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {COLORS['primary']};
        margin-bottom: 0.5rem;
        font-family: 'Playfair Display', serif;
    }}
    
    .stat-label {{
        font-size: 0.95rem;
        color: {COLORS['dark']};
        line-height: 1.4;
    }}
    
    .comparison-card {{
        background: white;
        border-radius: 12px;
        padding: 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        overflow: hidden;
    }}
    
    .comparison-header {{
        padding: 2rem;
        text-align: center;
        background: linear-gradient(135deg, {COLORS['primary']}15 0%, {COLORS['sea']}15 100%);
    }}
    
    .comparison-image {{
        width: 100%;
        height: 250px;
        object-fit: cover;
        object-position: center;
        transition: all 0.3s ease;
    }}
    
    .advantage-item {{
        background: {COLORS['light_gray']};
        padding: 1.2rem;
        border-radius: 8px;
        margin-bottom: 0.8rem;
        border-left: 4px solid {COLORS['olive']};
        transition: all 0.3s ease;
    }}
    
    .advantage-item:hover {{
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transform: translateX(5px);
    }}
    
    .disadvantage-item {{
        background: {COLORS['light_gray']};
        padding: 1.2rem;
        border-radius: 8px;
        margin-bottom: 0.8rem;
        border-left: 4px solid {COLORS['accent']};
        transition: all 0.3s ease;
    }}
    
    .disadvantage-item:hover {{
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transform: translateX(5px);
    }}
    
    .similarity-badge {{
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }}
    
    .similarity-badge:hover {{
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transform: translateY(-3px);
    }}
    
    .decision-box {{
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }}
    
    .decision-option {{
        background: {COLORS['light_gray']};
        padding: 1rem;
        border-radius: 6px;
        margin: 0.5rem 0;
        border-left: 3px solid {COLORS['primary']};
    }}
    
    .characteristic-pill {{
        display: inline-block;
        background: {COLORS['primary']}15;
        color: {COLORS['primary']};
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0.3rem;
        font-weight: 500;
    }}
</style>
""", unsafe_allow_html=True)

# Load data
data = SITE_DATA['urban_rural']

# Header
st.markdown(f"""
<div class="page-header">
    <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">{data['hero']['title']}</h1>
    <p style="font-size: 1.3rem; opacity: 0.9; margin-bottom: 1rem;">{data['hero']['subtitle']}</p>
    <p style="font-size: 1.1rem; opacity: 0.85;">{data['hero']['description']}</p>
</div>
""", unsafe_allow_html=True)

# Key Statistics
st.markdown(f"""
<h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin: 3rem 0 2rem 0;">
    Greece by the Numbers
</h2>
""", unsafe_allow_html=True)

cols = st.columns(4)
for col, stat in zip(cols, data['key_stats']):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon">{stat['icon']}</div>
            <div class="stat-value">{stat['value']}</div>
            <div class="stat-label">{stat['label']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Main Comparison Section
st.markdown(f"""
<h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin: 3rem 0 2rem 0;">
    Two Lifestyles, One Greece
</h2>
""", unsafe_allow_html=True)

# Urban vs Rural Comparison
col1, col2 = st.columns(2)

with col1:
    urban = data['comparison']['urban']
    img_html = render_image(urban['image'], class_name="comparison-image", alt="Urban Greece")
    
    st.markdown(f"""
    <div class="comparison-card">
        {img_html}
        <div class="comparison-header">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">{urban['emoji']} {urban['title']}</h2>
            <p style="font-size: 1.0rem; font-style: italic; color: {COLORS['primary']}; margin: 0;">
                {urban['tagline']}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Advantages
    st.markdown(f"<h4 style='color: {COLORS['olive']}; margin: 2rem 0 1rem 0;'>✅ Advantages</h4>", unsafe_allow_html=True)
    for adv in urban['advantages']:
        st.markdown(f"""
        <div class="advantage-item">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{adv['icon']}</div>
            <strong style="color: {COLORS['primary']};">{adv['title']}</strong>
            <p style="margin: 0.3rem 0 0 0; font-size: 0.9rem; color: {COLORS['dark']};">
                {adv['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Disadvantages
    st.markdown(f"<h4 style='color: {COLORS['accent']}; margin: 2rem 0 1rem 0;'>⚠️ Disadvantages</h4>", unsafe_allow_html=True)
    for dis in urban['disadvantages']:
        st.markdown(f"""
        <div class="disadvantage-item">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{dis['icon']}</div>
            <strong style="color: {COLORS['primary']};">{dis['title']}</strong>
            <p style="margin: 0.3rem 0 0 0; font-size: 0.9rem; color: {COLORS['dark']};">
                {dis['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    

with col2:
    rural = data['comparison']['rural']
    img_html = render_image(rural['image'], class_name="comparison-image", alt="Rural Greece")
    
    st.markdown(f"""
    <div class="comparison-card">
        {img_html}
        <div class="comparison-header">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">{rural['emoji']} {rural['title']}</h2>
            <p style="font-size: 1.0rem; font-style: italic; color: {COLORS['olive']}; margin: 0;">
                {rural['tagline']}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Advantages
    st.markdown(f"<h4 style='color: {COLORS['olive']}; margin: 2rem 0 1rem 0;'>✅ Advantages</h4>", unsafe_allow_html=True)
    for adv in rural['advantages']:
        st.markdown(f"""
        <div class="advantage-item">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{adv['icon']}</div>
            <strong style="color: {COLORS['primary']};">{adv['title']}</strong>
            <p style="margin: 0.3rem 0 0 0; font-size: 0.9rem; color: {COLORS['dark']};">
                {adv['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Disadvantages
    st.markdown(f"<h4 style='color: {COLORS['accent']}; margin: 2rem 0 1rem 0;'>⚠️ Disadvantages</h4>", unsafe_allow_html=True)
    for dis in rural['disadvantages']:
        st.markdown(f"""
        <div class="disadvantage-item">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{dis['icon']}</div>
            <strong style="color: {COLORS['primary']};">{dis['title']}</strong>
            <p style="margin: 0.3rem 0 0 0; font-size: 0.9rem; color: {COLORS['dark']};">
                {dis['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    

# Similarities Section
sim = data['similarities']
st.markdown(f"""
<div style="background: linear-gradient(135deg, {COLORS['olive']}15 0%, {COLORS['sea']}15 100%); 
            padding: 3rem 2rem; border-radius: 12px; margin: 3rem 0;">
    <h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin-bottom: 1rem;">
        {sim['title']}
    </h2>
    <p style="text-align: center; font-size: 1.1rem; max-width: 700px; margin: 0 auto 2rem auto; color: {COLORS['dark']};">
        {sim['description']}
    </p>
</div>
""", unsafe_allow_html=True)

cols = st.columns(5)
for col, point in zip(cols, sim['points']):
    with col:
        st.markdown(f"""
        <div class="similarity-badge">
            <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">{point['icon']}</div>
            <p style="font-size: 0.9rem; margin: 0; line-height: 1.4; color: {COLORS['dark']};">
                {point['text']}
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)


# Final CTA
st.markdown(f"""
<div style="text-align: center; padding: 3rem 2rem; background: linear-gradient(135deg, {COLORS['accent']} 0%, {COLORS['secondary']} 100%); 
            border-radius: 12px; margin: 3rem 0;">
    <h3 style="color: {COLORS['white']}; font-size: 2rem; margin-bottom: 1rem;">
        Ready to Experience Greece Your Way?
    </h3>
    <p style="font-size: 1.1rem; max-width: 600px; margin: 0 auto 2rem auto; line-height: 1.8;">
        <strong> Whether you choose the energy of Athens or the tranquility of a Greek village, 
        your perfect Greek adventure awaits </strong>.
    </p>
</div>
""", unsafe_allow_html=True)