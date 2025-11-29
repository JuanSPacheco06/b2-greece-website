import streamlit as st
from pathlib import Path
import sys
from utils.images import render_image, load_site_image
sys.path.append(str(Path(__file__).parent.parent))
from utils.data import SITE_DATA, COLORS, UI_TEXT

st.set_page_config(
    page_title="Writers & Literature | Greek Escape",
    page_icon="📚",
    layout="wide"
)

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    h1, h2, h3 {{ font-family: 'Playfair Display', serif; }}
    p {{ font-family: 'Inter', sans-serif; line-height: 1.8; }}
    
    .page-header {{
        background: linear-gradient(135deg, {COLORS['sea']} 0%, {COLORS['accent']} 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 3rem;
        color: white;
    }}
    
    .writer-card {{
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 3rem;
        transition: all 0.3s ease;
    }}
    
    .writer-card:hover {{
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    }}

    .writer-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;        /* Hace que la imagen cubra completamente el contenedor */
        object-position: center;  /* Centra la imagen */
        display: block;
    }}
    
    .theme-pill {{
        display: inline-block;
        background: {COLORS['primary']};
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0.3rem 0.3rem 0.3rem 0;
        font-weight: 500;
    }}
    
    .fact-box {{
        background: {COLORS['light_gray']};
        padding: 1rem 1.5rem;
        border-left: 4px solid {COLORS['secondary']};
        border-radius: 4px;
        margin: 0.5rem 0;
    }}
    
    .read-more-btn {{
        padding: 0.7rem 1.5rem;
        background: {COLORS['primary']};
        color: white;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s ease;
        display: inline-block;
        margin-top: 1rem;
    }}
    
    .read-more-btn:hover {{
        background: {COLORS['sea']};
        transform: translateY(-2px);
    }}
    
    .quote-box {{
        background: linear-gradient(135deg, {COLORS['primary']}15 0%, {COLORS['sea']}15 100%);
        padding: 2rem;
        border-left: 5px solid {COLORS['primary']};
        border-radius: 8px;
        font-style: italic;
        font-size: 1.2rem;
        color: {COLORS['dark']};
        margin: 2rem 0;
    }}
    
    .image-placeholder {{
        width: 100%;
        height: 400px;
        background: linear-gradient(135deg, {COLORS['light_gray']} 0%, #E0E0E0 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        color: {COLORS['dark']};
        text-align: center;
        padding: 1rem;
    }}
</style>
""", unsafe_allow_html=True)

# Page Header
st.markdown("""
<div class="page-header">
    <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">📚 Writers & Literature</h1>
    <p style="font-size: 1.3rem; opacity: 0.9;">The voices that shaped Western civilization</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown(f"""
<div style="max-width: 900px; margin: 0 auto 4rem auto; text-align: center;">
    <p style="font-size: 1.2rem; line-height: 1.8; color: {COLORS['dark']};">
        Greek literature spans over two millennia, from Homer's ancient epics to contemporary poetry. 
        These writers captured the human experience—honor, loss, memory, and the eternal questions 
        that still resonate today.
    </p>
</div>
""", unsafe_allow_html=True)

# Writer Profiles
for writer in SITE_DATA['literature']:
    # Create collapsible section for each writer
    with st.expander(f"### {writer['name']} ({writer['period']})", expanded=True):
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            # Cargar la imagen del escritor
            img_html = render_image(writer['image_placeholder'], class_name="writer-image", alt=writer['name'])
            st.markdown(f"""
            <div class="writer-card">
                <div class="image-placeholder">
                    {img_html}  <!-- Ahora la imagen real se muestra aquí -->
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            # Summary
            st.markdown(f"""
            <div class="writer-card">
                <h2 style="color: {COLORS['primary']}; margin-bottom: 1rem; font-size: 2rem;">
                    {writer['name']}
                </h2>
                <p style="font-size: 1.1rem; color: {COLORS['dark']}; margin-bottom: 1.5rem;">
                    {writer['summary']}
                </p>
            """, unsafe_allow_html=True)
            
            # Themes
            st.markdown(
                f"<p style='font-weight: 600; margin-bottom: 0.5rem; color: {COLORS['dark']};'>Key Themes:</p>",
                unsafe_allow_html=True
            )

            themes_html = "<div class='themes-container'>"

            for theme in writer['themes']:
                themes_html += f"<span class='theme-pill'>{theme}</span>"

            themes_html += "</div>"

            st.markdown(themes_html, unsafe_allow_html=True)

            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Legacy section
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="quote-box">
            <strong>Literary Legacy:</strong><br>
            {writer['legacy']}
        </div>
        """, unsafe_allow_html=True)
        
        # Fun Facts
        st.markdown(f"<h4 style='color: {COLORS['primary']}; margin-top: 2rem;'>📖 Did You Know?</h4>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        for idx, fact in enumerate(writer['fun_facts']):
            with col1 if idx % 2 == 0 else col2:
                st.markdown(f"""
                <div class="fact-box">
                    <p style="margin: 0; font-size: 0.95rem;">✨ {fact}</p>
                </div>
                """, unsafe_allow_html=True)

# Literary Timeline
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="background: {COLORS['light_gray']}; padding: 4rem 3rem; border-radius: 12px; margin-top: 3rem;">
    <h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin-bottom: 2rem;">
        The Greek Literary Tradition
    </h2>
    <p style="text-align: center; font-size: 1.1rem; max-width: 800px; margin: 0 auto 3rem auto; line-height: 1.8;">
        Greek literature has evolved over millennia, reflecting the social, political, and philosophical 
        shifts of each era. From oral tradition to written word, from epic poetry to contemporary verse, 
        Greek writers continue to influence global literature.
    </p>
""", unsafe_allow_html=True)

timeline = [
    {"period": "8th Century BC", "event": "Homer's oral epics establish Western literary tradition"},
    {"period": "5th-4th Century BC", "event": "Classical period: Drama, philosophy, and rhetoric flourish"},
    {"period": "Hellenistic Era", "event": "Poetry and scientific writing spread across Mediterranean"},
    {"period": "Byzantine Period", "event": "Religious texts and chronicles preserve Greek language"},
    {"period": "Modern Era", "event": "Contemporary writers like Kiki Dimoula blend ancient and modern themes"}
]

for item in timeline:
    st.markdown(f"""
    <div style="display: flex; margin-bottom: 2.5rem; align-items: flex-start;">
        <div style="min-width: 180px; font-weight: 700; color: {COLORS['primary']}; font-size: 1.1rem;">
            {item['period']}
        </div>
        <div style="width: 4px; height: 100%; background: {COLORS['secondary']}; margin: 0 1.5rem; border-radius: 2px;"></div>
        <div style="flex: 1; font-size: 1rem; color: {COLORS['dark']}; padding-top: 2px;">
            {item['event']}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Reading Recommendations
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="background: linear-gradient(135deg, {COLORS['sea']} 0%, {COLORS['accent']} 100%); padding: 3rem; border-radius: 12px;">
    <h3 style="color: white; font-size: 2rem; margin-bottom: 1rem; text-align: center;">
        Start Your Literary Journey
    </h3>
    <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; text-align: center; margin-bottom: 2rem;">
        Explore the works that have inspired generations of readers and writers
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

recommendations = [
    {"title": "The Iliad & The Odyssey", "author": "Homer", "why": "Experience the epic tales that defined heroism"},
    {"title": "Selected Poems", "author": "Kiki Dimoula", "why": "Discover contemporary Greek emotional depth"}
]

for col, rec in zip([col1, col2], recommendations):
    with col:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 8px; margin: 0.5rem;">
            <h4 style="color: {COLORS['primary']}; margin-bottom: 0.5rem;">{rec['title']}</h4>
            <p style="color: {COLORS['dark']}; font-size: 0.9rem; margin-bottom: 0.5rem;">by {rec['author']}</p>
            <p style="color: {COLORS['dark']}; font-size: 0.95rem; margin: 0;">📚 {rec['why']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)