import streamlit as st
from pathlib import Path
import sys
from utils.images import render_image, load_site_image

sys.path.append(str(Path(__file__).parent.parent))
from utils.data import SITE_DATA, COLORS, UI_TEXT

st.set_page_config(
    page_title="Gastronomy | Greek Escape",
    page_icon="🍽️",
    layout="wide"
)

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    h1, h2, h3 {{ font-family: 'Playfair Display', serif; }}
    p {{ font-family: 'Inter', sans-serif; line-height: 1.8; }}
    
    .page-header {{
        background: linear-gradient(135deg, {COLORS['accent']} 0%, {COLORS['secondary']} 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 3rem;
        color: white;
    }}
    
    .dish-card {{
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        height: 100%;
    }}
    
    .dish-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.2);
    }}
    
    .dish-content {{
        padding: 1.5rem;
    }}
    
    .region-badge {{
        display: inline-block;
        background: {COLORS['primary']};
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }}
    
    .type-badge {{
        display: inline-block;
        background: {COLORS['olive']};
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        margin-left: 0.3rem;
    }}
    
    .image-placeholder {{
        width: 100%;
        height: 250px;
        background: linear-gradient(135deg, {COLORS['light_gray']} 0%, #E0E0E0 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: {COLORS['dark']};
        font-size: 0.85rem;
        text-align: center;
        padding: 1rem;
        overflow: hidden;  /* Esto es para cortar la imagen si se sale de los bordes */
    }}

    .dish-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;        /* Hace que la imagen llene el contenedor sin deformarse */
        object-position: center;  /* Alinea la imagen al centro */
        display: block;           /* Elimina espacio debajo de la imagen */
    }}
    
    .filter-chip {{
        display: inline-block;
        padding: 0.5rem 1.2rem;
        margin: 0.3rem;
        background: white;
        border: 2px solid {COLORS['primary']};
        color: {COLORS['primary']};
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: 600;
    }}
    
    .filter-chip:hover {{
        background: {COLORS['primary']};
        color: white;
    }}
    
    .filter-chip-active {{
        background: {COLORS['primary']};
        color: white;
    }}
    
    .recommendation-box {{
        background: {COLORS['secondary']}15;
        border-left: 4px solid {COLORS['secondary']};
        padding: 1.5rem;
        border-radius: 8px;
        margin: 2rem 0;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="page-header">
    <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">🍽️ Greek Gastronomy</h1>
    <p style="font-size: 1.3rem; opacity: 0.9;">Taste the Mediterranean flavors that define Greek culture</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown(f"""
<div style="max-width: 900px; margin: 0 auto 4rem auto; text-align: center;">
    <p style="font-size: 1.2rem; line-height: 1.8; color: {COLORS['dark']};">
        Greek cuisine is a celebration of fresh ingredients, time-honored recipes, and the Mediterranean way of life. 
        From the bustling tavernas of Athens to the seaside restaurants of the islands, every meal tells a story 
        of tradition, family, and love for good food.
    </p>
</div>
""", unsafe_allow_html=True)

# Filters
st.markdown("### 🔍 Filter by Region or Type")

col1, col2 = st.columns(2)

with col1:
    regions = list(set([dish['region'] for dish in SITE_DATA['gastronomy']]))
    selected_region = st.selectbox("Select Region", ["All Regions"] + regions)

with col2:
    types = list(set([dish['type'] for dish in SITE_DATA['gastronomy']]))
    selected_type = st.selectbox("Select Type", ["All Types"] + types)

# Filter dishes
filtered_dishes = SITE_DATA['gastronomy']

if selected_region != "All Regions":
    filtered_dishes = [d for d in filtered_dishes if d['region'] == selected_region]

if selected_type != "All Types":
    filtered_dishes = [d for d in filtered_dishes if d['type'] == selected_type]

st.markdown("<br>", unsafe_allow_html=True)

# Display dishes in grid
if not filtered_dishes:
    st.markdown(f"""
    <div style="text-align: center; padding: 4rem; background: {COLORS['light_gray']}; border-radius: 12px;">
        <h3 style="color: {COLORS['dark']};">🔍 {UI_TEXT['empty_state']}</h3>
    </div>
    """, unsafe_allow_html=True)
else:
    # Grid layout
    cols_per_row = 3
    rows = [filtered_dishes[i:i+cols_per_row] for i in range(0, len(filtered_dishes), cols_per_row)]
    
    for row in rows:
        cols = st.columns(len(row))
        
        for col, dish in zip(cols, row):
            with col:
                # Cargar la imagen como Base64
                img_html = render_image(dish['image_placeholder'], class_name="dish-image", alt=dish['name'])
                st.markdown(f"""
                <div class="dish-card">
                    <div class="image-placeholder">
                        {img_html}
                    </div>
                    <div class="dish-content">
                        <span class="region-badge">{dish['region']}</span>
                        <span class="type-badge">{dish['type']}</span>
                        <h3 style="color: {COLORS['primary']}; margin: 0.5rem 0; font-size: 1.5rem;">
                            {dish['name']}
                        </h3>
                        <p style="color: {COLORS['dark']}; font-size: 0.95rem; line-height: 1.6;">
                            {dish['description']}
                        </p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

# Traditional Greek Meal
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="background: {COLORS['light_gray']}; padding: 3rem; border-radius: 12px; margin-top: 3rem;">
    <h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin-bottom: 2rem;">
        🍷 The Greek Dining Experience
    </h2>
    <p style="text-align: center; font-size: 1.1rem; max-width: 800px; margin: 0 auto 3rem auto; line-height: 1.8;">
        A traditional Greek meal is more than food—it's a social celebration that brings people together. 
        Here's how to experience it like a local:
    </p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

meal_tips = [
    {
        "title": "Start with Mezze",
        "icon": "🥗",
        "desc": "Begin with small plates like tzatziki, olives, and cheese to share with everyone at the table"
    },
    {
        "title": "Main Course",
        "icon": "🍖",
        "desc": "Order a variety of main dishes—moussaka, souvlaki, grilled fish—and share family-style"
    },
    {
        "title": "Pair with Wine",
        "icon": "🍷",
        "desc": "Greek wines perfectly complement the cuisine. Try local varieties from different regions"
    }
]

for col, tip in zip([col1, col2, col3], meal_tips):
    with col:
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3.5rem; margin-bottom: 1rem;">{tip['icon']}</div>
            <h4 style="color: {COLORS['primary']}; margin-bottom: 0.8rem; font-size: 1.3rem;">{tip['title']}</h4>
            <p style="color: {COLORS['dark']}; font-size: 0.95rem; line-height: 1.6;">{tip['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Regional Specialties
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<h2 style="text-align: center; color: {COLORS['primary']}; font-size: 2.5rem; margin: 3rem 0 2rem 0;">
    🗺️ Regional Specialties
</h2>
""", unsafe_allow_html=True)

regions_info = [
    {
        "name": "Athens & Mainland",
        "icon": "🏛️",
        "specialties": ["Souvlaki", "Moussaka", "Street food culture"],
        "description": "The heart of traditional Greek cuisine with classic dishes perfected over centuries"
    },
    {
        "name": "Milos Islands",
        "icon": "🏖️",
        "specialties": ["Pitaraka", "Ladenia", "Local honey", "Fresh seafood"],
        "description": "Volcanic island flavors with unique cheese pies and the famous Greek pizza"
    },
    {
        "name": "Kalamata & Peloponnese",
        "icon": "🫒",
        "specialties": ["Kalamata Olives", "Sfela Cheese", "Lalagia pastries"],
        "description": "The olive capital offering world-famous olives and traditional Peloponnesian cuisine"
    }
]

for region in regions_info:
    st.markdown(f"""
    <div class="dish-card" style="margin-bottom: 2rem;">
        <div style="padding: 2rem;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 3rem; margin-right: 1rem;">{region['icon']}</span>
                <h3 style="color: {COLORS['primary']}; font-size: 2rem; margin: 0;">{region['name']}</h3>
            </div>
            <p style="font-size: 1.1rem; line-height: 1.8; color: {COLORS['dark']}; margin-bottom: 1rem;">
                {region['description']}
            </p>
            <div style="background: {COLORS['light_gray']}; padding: 1rem; border-radius: 8px;">
                <strong style="color: {COLORS['primary']};">Must-Try:</strong> 
                {', '.join(region['specialties'])}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Food Pairing Recommendations
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="recommendation-box">
    <h3 style="color: {COLORS['secondary']}; margin-bottom: 1rem;">🍇 Wine Pairing Recommendations</h3>
    <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 1rem;">
        Greek wines are experiencing a renaissance, with ancient varieties producing exceptional modern wines:
    </p>
    <ul style="font-size: 1rem; line-height: 2;">
        <li><strong>Assyrtiko (white):</strong> Pairs perfectly with seafood and salads</li>
        <li><strong>Agiorgitiko (red):</strong> Excellent with grilled meats and moussaka</li>
        <li><strong>Moschofilero (rosé):</strong> Ideal for mezze and cheese plates</li>
        <li><strong>Xinomavro (red):</strong> Bold flavor that complements hearty stews</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="background: linear-gradient(135deg, {COLORS['accent']} 0%, {COLORS['secondary']} 100%); padding: 3rem; border-radius: 12px; text-align: center;">
    <h3 style="color: white; font-size: 2rem; margin-bottom: 1rem;">
        Ready to Taste Greece?
    </h3>
    <p style="color: rgba(255,255,255,0.95); font-size: 1.2rem; margin-bottom: 2rem; max-width: 700px; margin-left: auto; margin-right: auto;">
        From bustling tavernas to seaside restaurants, Greek cuisine offers unforgettable flavors 
        that will make your journey even more memorable.
    </p>
    <button style="padding: 1rem 2.5rem; background: white; color: {COLORS['accent']}; border: none; border-radius: 50px; font-size: 1.1rem; font-weight: 600; cursor: pointer;">
        Find Restaurants
    </button>
</div>
""", unsafe_allow_html=True)