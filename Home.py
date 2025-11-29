import streamlit as st
from pathlib import Path
import sys

# Add utils to path
sys.path.append(str(Path(__file__).parent))
from utils.data import SITE_DATA, COLORS, UI_TEXT
from utils.images import render_image, load_site_image

# Page configuration
st.set_page_config(
    page_title="Greek Escape | Four Cities, One Dream",
    page_icon="🇬🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for National Geographic-inspired design
st.markdown(f"""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    /* Global Styles */
    .main {{
        background-color: {COLORS['white']};
    }}
    
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Typography */
    h1, h2, h3 {{
        font-family: 'Playfair Display', serif;
        color: {COLORS['dark']};
    }}
    
    p, li, span {{
        font-family: 'Inter', sans-serif;
        color: {COLORS['dark']};
        line-height: 1.6;
    }}
    
    /* Hero Section */
    .hero-container {{
        position: relative;
        width: 100%;
        height: 600px;
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['sea']} 100%);
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 3rem;
    }}

    .hero-content {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 2;
        width: 90%;
    }}
    
    .hero-title {{
        font-size: 4rem;
        font-weight: 700;
        color: white !important;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        font-family: 'Playfair Display', serif;
        line-height: 1.2;
    }}
    
    .hero-subtitle {{
        font-size: 1.5rem;
        color: white !important;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
        font-family: 'Inter', sans-serif;
        font-weight: 300;
    }}

    .hero-image {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
    }}

    .hero-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;       /* 🔥 Llena el contenedor */
        object-position: center; /* Centrado */
    }}
    
    /* CTA Buttons */
    .cta-container {{
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
    }}
    
    .cta-button {{
        padding: 1rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        font-family: 'Inter', sans-serif;
    }}
    
    .cta-primary {{
        background-color: {COLORS['secondary']};
        color: {COLORS['dark']};
    }}
    
    .cta-primary:hover {{
        background-color: #FFC700;
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }}
    
    .cta-secondary {{
        background-color: white;
        color: white;
        border: 2px solid white;
    }}
    
    .cta-secondary:hover {{
        background-color: white;
        color: {COLORS['primary']};
        transform: translateY(-2px);
    }}
    
    /* Feature Cards */
    .feature-card {{
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        height: 100%;
        border-left: 4px solid {COLORS['primary']};
    }}
    
    .feature-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }}
    
    .feature-icon {{
        font-size: 3rem;
        margin-bottom: 1rem;
    }}
    
    .feature-title {{
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: {COLORS['primary']};
    }}
    
    .feature-text {{
        font-size: 1rem;
        color: {COLORS['dark']};
        line-height: 1.6;
    }}
    
    /* Stats Section */
    .stats-container {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['sea']} 100%);
        padding: 3rem;
        border-radius: 12px;
        margin: 3rem 0;
    }}
    
    .stat-box {{
        text-align: center;
        color: black;
    }}
    
    .stat-number {{
        font-size: 3rem;
        font-weight: 700;
        font-family: 'Playfair Display', serif;
        margin-bottom: 0.5rem;
    }}
    
    .stat-label {{
        font-size: 1.1rem;
        font-weight: 300;
        opacity: 0.9;
    }}

     .metric-card {{
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        transition: all 0.3s ease;
    }}
    
    .metric-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }}
    
    .metric-value {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {COLORS['primary']};
        margin-bottom: 0.5rem;
        font-family: 'Playfair Display', serif;
    }}
    
    .metric-label {{
        font-size: 1rem;
        color: {COLORS['dark']};
        font-weight: 600;
    }}
    
    /* Image Placeholder */
    .destination-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;       /* Llena el contenedor sin deformar */
        object-position: center; /* Centrado */
        border-radius: 15px;     /* Opcional: bordes redondeados */
    }}
    .image-placeholder {{
        min-height: 400px;
        position: relative;
        overflow: hidden;
    }}
    
    /* Section Headers */
    .section-header {{
        text-align: center;
        margin: 4rem 0 2rem 0;
    }}
    
    .section-title {{
        font-size: 3rem;
        font-weight: 700;
        color: {COLORS['dark']};
        margin-bottom: 1rem;
    }}
    
    .section-subtitle {{
        font-size: 1.3rem;
        color: {COLORS['primary']};
        font-weight: 300;
    }}
    
    /* Responsive Design */
    @media (max-width: 768px) {{
        .hero-title {{
            font-size: 2.5rem;
        }}
        
        .hero-subtitle {{
            font-size: 1.2rem;
        }}
        
        .section-title {{
            font-size: 2rem;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# Hero Section
def render_hero():
    hero_img = render_image("hero_acropolis.jpg", "hero-image", "Hero Image")

    st.markdown(f"""
    <div class="hero-container">
        <div class="hero-image">
             {hero_img}
        </div>
        <div class="hero-content">
            <h1 class="hero-title">{SITE_DATA['home']['hero_title']}</h1>
            <p class="hero-subtitle"><strong> {SITE_DATA['home']['hero_subtitle']}</strong></p>
            <div class="cta-container">
                <a href="#explore" class="cta-button cta-primary">{UI_TEXT['explore_culture']}</a>
                <a href="#nature" class="cta-button cta-secondary">{UI_TEXT['explore_nature']}</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Why Visit Greece Section
def render_why_visit():
    st.markdown("""
    <div class="section-header" id="explore">
        <h2 class="section-title">Why Visit Greece?</h2>
        <p class="section-subtitle"><strong> Discover the cradle of civilization </strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    features = [
        {
            "icon": "🏛️",
            "title": "Ancient History",
            "text": "Walk through 3,000+ years of history. From the Acropolis to ancient theaters, experience the birthplace of democracy and philosophy."
        },
        {
            "icon": "🏖️",
            "title": "70+ Stunning Beaches",
            "text": "Discover moon-white cliffs at Sarakiniko, volcanic black sands, and crystal-clear Aegean waters across hundreds of islands."
        },
        {
            "icon": "🎭",
            "title": "Living Culture",
            "text": "Dance under the stars at local festivals, explore traditional crafts, and taste authentic Mediterranean cuisine in seaside villages."
        }
    ]
    
    for col, feature in zip([col1, col2, col3], features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature['icon']}</div>
                <h3 class="feature-title">{feature['title']}</h3>
                <p class="feature-text">{feature['text']}</p>
            </div>
            """, unsafe_allow_html=True)

# Quick Stats
def render_stats():
    st.markdown(f"""
        <div style="text-align: center; margin: 2rem auto 3rem auto;">
            <h2 style="color: {COLORS['primary']}; font-size: 2.5rem; margin-bottom: 1rem;">
                Greece by the Numbers
            </h2>
            <p style="font-size: 1.1rem; max-width: 800px; margin: 0 auto; line-height: 1.8;">
                Discover fascinating facts and statistics about Greece's geography, culture, and environment.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    # Key Metrics - Row 1
    col1, col2, col3, col4 = st.columns(4)
    
    metrics_row1 = [
        {"value": "3,000+", "label": "Years of History"},
        {"value": "70+", "label": "Breathtaking Beaches"},
        {"value": "2,917m", "label": "Mount Olympus Peak"},
        {"value": "6,000+", "label": "Islands & Islets"}
    ]
    
    for col, metric in zip([col1, col2, col3, col4], metrics_row1):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metric['value']}</div>
                <div class="metric-label">{metric['label']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

# Featured Destinations
def render_featured_destinations():
    st.markdown("""
    <div class="section-header" id="nature">
        <h2 class="section-title">Featured Destinations</h2>
        <p class="section-subtitle">From ancient cities to hidden paradises</p>
    </div>
    """, unsafe_allow_html=True)
    
    destinations = [
        {
            "name": "Athens",
            "description": "The heart of ancient Greece. Explore the Acropolis, wander through Plaka's charming streets, and watch the sunset from Filopappou Hill.",
            "image": "athens_panorama.jpg"
        },
        {
            "name": "Milos",
            "description": "Greece's hidden paradise with moon-white cliffs at Sarakiniko, 70+ beaches, and colorful fishing villages like Klima.",
            "image": "milos_klima.jpg"
        },
        {
            "name": "Mount Olympus",
            "description": "Home of the Greek gods. Hike through 1,700+ plant species to the 2,917m peak in Greece's first national park.",
            "image": "olympus_trail.jpg"
        }
    ]
    
    for i, dest in enumerate(destinations):
        if i % 2 == 0:
            col1, col2 = st.columns([1, 1])
        else:
            col2, col1 = st.columns([1, 1])
        
        with col1:
            img_html = render_image(dest['image'], class_name="destination-image", alt=dest['name'])
            st.markdown(f"""
            <div class="image-placeholder">
                {img_html}
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div style="padding: 2rem;">
                <h3 style="font-size: 2rem; color: {COLORS['primary']}; margin-bottom: 1rem;">{dest['name']}</h3>
                <p style="font-size: 1.1rem; line-height: 1.8; color: {COLORS['dark']};">{dest['description']}</p>
                <button style="margin-top: 1.5rem; padding: 0.8rem 2rem; background: {COLORS['primary']}; color: white; border: none; border-radius: 25px; cursor: pointer; font-weight: 600;">
                    {UI_TEXT['learn_more']}
                </button>
            </div>
            """, unsafe_allow_html=True)
        
        if i < len(destinations) - 1:
            st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
def render_footer():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: {COLORS['dark']}; padding: 3rem; border-radius: 12px; margin-top: 4rem; text-align: center;">
        <h3 style="color: white; font-size: 2rem; margin-bottom: 1rem;">Ready to Experience Greece?</h3>
        <p style="color: rgba(255,255,255,0.8); font-size: 1.2rem; margin-bottom: 2rem;">
            {UI_TEXT['tagline']}
        </p>
        <button style="padding: 1rem 3rem; background: {COLORS['secondary']}; color: {COLORS['dark']}; border: none; border-radius: 50px; font-size: 1.1rem; font-weight: 600; cursor: pointer;">
            {UI_TEXT['contact_cta']}
        </button>
        <p style="color: rgba(255,255,255,0.5); margin-top: 2rem; font-size: 0.9rem;">
            Greek Escape © 2025 | Four Cities, One Dream
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    # Sidebar
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem 0;">
            <h1 style="color: {COLORS['primary']}; font-size: 1.8rem; margin-bottom: 0.5rem;">🇬🇷 Greek Escape</h1>
            <p style="color: {COLORS['dark']}; font-size: 0.9rem; font-style: italic;">Four Cities, One Dream</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        ### 🧭 Navigation
        Use the pages in the sidebar to explore:
        - 🏛️ **Culture & Art**
        - 🌿 **Nature & Environment**
        - 🍽️ **Gastronomy**
        - 📚 **Writers & Literature**
        - 📷 **Gallery**
        - 📊 **Data & Maps**
        """)
        
        st.markdown("---")
        
        st.info("📍 **It's Time to Travel** - Discover the magic of Greece through ancient heritage, vibrant culture, and inspiring nature.")
    
    # Main content
    render_hero()
    render_why_visit()
    render_stats()
    render_featured_destinations()
    render_footer()

if __name__ == "__main__":
    main()