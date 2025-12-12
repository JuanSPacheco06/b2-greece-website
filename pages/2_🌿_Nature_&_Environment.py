import streamlit as st
import folium
from streamlit_folium import folium_static
import plotly.graph_objects as go
from pathlib import Path
import sys
from utils.images import render_image, load_site_image

sys.path.append(str(Path(__file__).parent.parent))
from utils.data import SITE_DATA, COLORS, UI_TEXT

st.set_page_config(
    page_title="Nature & Environment | Greek Escape",
    page_icon="🌿",
    layout="wide"
)

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    h1, h2, h3 {{ font-family: 'Playfair Display', serif; }}
    p {{ font-family: 'Inter', sans-serif; line-height: 1.8; }}
    
    .page-header {{
        background: linear-gradient(135deg, {COLORS['olive']} 0%, {COLORS['sea']} 100%);
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
        border-top: 4px solid {COLORS['accent']};
    }}
    
    .stat-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }}
    
    .stat-number {{
        font-size: 3rem;
        font-weight: 700;
        color: {COLORS['accent']};
        margin-bottom: 0.5rem;
        font-family: 'Playfair Display', serif;
    }}
    
    .stat-label {{
        font-size: 1.1rem;
        color: {COLORS['dark']};
        font-weight: 600;
    }}
    
    .park-card {{
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }}
    
    .activity-badge {{
        display: i  ;
        background: {COLORS['olive']};
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0.3rem;
        font-weight: 500;
    }}
    
    .alert-box {{
        background: {COLORS['accent']}15;
        border-left: 4px solid {COLORS['accent']};
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }}
    
    .solution-box {{
        background: {COLORS['olive']}15;
        border-left: 4px solid {COLORS['olive']};
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }}
    
    .image-placeholder {{
        width: 100%;
        height: 300px;
        background: linear-gradient(135deg, {COLORS['light_gray']} 0%, #E0E0E0 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        color: {COLORS['dark']};
        text-align: center;
        margin-bottom: 1rem;
    }}

    .park-image-container {{
    width: 100%;
    height: 250px;        /* Altura fija para la imagen del parque */
    overflow: hidden;     /* Recorta lo que se salga */
    border-radius: 12px 12px 0 0;  /* Coincide con el card */
    margin-bottom: 1rem;  /* Separación entre imagen y contenido */
    }}

    .park-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;       /* Llena el contenedor sin deformarse */
        object-position: center; /* Centrado */
        display: block;
        }}
    
    /* Añade estos estilos dentro del st.markdown() del CSS en tu página */

    .flora-fauna-image-container {{
        width: 100%;
        height: 200px;
        overflow: hidden;
        border-radius: 12px 12px 0 0;  /* Solo redondea arriba */
        margin-bottom: 0;  /* Sin margen porque está pegada al card */
    }}

    .flora-fauna-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
        display: block;
        transition: transform 0.3s ease;
    }}

    .park-card:hover .flora-fauna-image {{
        transform: scale(1.05);
    }}

    /* Asegura que el contenido del card esté debajo de la imagen */
    .park-card {{
        padding: 0;  /* Quita el padding general */
        overflow: hidden;  /* Importante para que la imagen no se salga */
    }}

    .park-card > div:not(.flora-fauna-image-container) {{
        padding: 1.5rem;  /* Añade padding solo al contenido de texto */
    }}
        
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="page-header">
    <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">🌿 Nature & Environment</h1>
    <p style="font-size: 1.3rem; opacity: 0.9;">Protecting Greece's natural treasures for future generations</p>
</div>
""", unsafe_allow_html=True)

# Tab Navigation
tab1, tab2, = st.tabs(["🌊 Natural Paradise", "🏞️ National Parks"])

# TAB 1: National Parks
# TAB 1: Natural Beauty (SELLING GREECE'S NATURE)
with tab1:
    beauty = SITE_DATA['nature']['natural_beauty']
    
    # Hero intro
    st.markdown(f"""
    <div style="text-align: center; max-width: 900px; margin: 2rem auto 3rem auto;">
        <h2 style="color: {COLORS['olive']}; font-size: 2.8rem; margin-bottom: 1rem;">
            {beauty['intro']['title']}
        </h2>
        <p style="color: {COLORS['primary']}; font-size: 1.4rem; font-style: italic; margin-bottom: 1rem;">
            {beauty['intro']['subtitle']}
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8; color: {COLORS['dark']};">
            {beauty['intro']['description']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
# Reemplaza las secciones de Flora y Fauna en tu archivo con este código:

    # Flora Section
    st.markdown(f"""
    <h3 style="color: {COLORS['olive']}; font-size: 2.2rem; margin: 3rem 0 1.5rem 0; text-align: center;">
        {beauty['flora']['title']}
    </h3>
    """, unsafe_allow_html=True)

    # Flora highlights in 2x2 grid
    col1, col2 = st.columns(2)

    for idx, item in enumerate(beauty['flora']['highlights']):
        with col1 if idx % 2 == 0 else col2:
            img_html = render_image(item['image'], class_name="flora-fauna-image", alt=item['name'])
            
            st.markdown(f"""
            <div class="park-card" style="min-height: 380px;">
                <div class="flora-fauna-image-container">
                    {img_html}
                </div>
                <div style="padding: 1.5rem;">
                    <h4 style="color: {COLORS['primary']}; font-size: 1.4rem; margin-bottom: 0.8rem; text-align: center;">
                        {item['name']}
                    </h4>
                    <p style="font-size: 1rem; line-height: 1.7; margin-bottom: 1rem; text-align: center;">
                        {item['description']}
                    </p>
                    <div style="text-align: center;">
                        <span style="background: {COLORS['olive']}15; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.85rem; color: {COLORS['olive']}; font-weight: 600;">
                            📍 {', '.join(item['locations'][:2])}
                        </span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Fauna Section
    st.markdown(f"""
    <h3 style="color: {COLORS['sea']}; font-size: 2.2rem; margin: 3rem 0 1.5rem 0; text-align: center;">
        {beauty['fauna']['title']}
    </h3>
    """, unsafe_allow_html=True)

    # Fauna highlights in 2x2 grid
    col1, col2 = st.columns(2)

    for idx, item in enumerate(beauty['fauna']['highlights']):
        with col1 if idx % 2 == 0 else col2:
            img_html = render_image(item['image'], class_name="flora-fauna-image", alt=item['name'])
            
            st.markdown(f"""
            <div class="park-card" style="min-height: 380px;">
                <div class="flora-fauna-image-container">
                    {img_html}
                </div>
                <div style="padding: 1.5rem;">
                    <h4 style="color: {COLORS['sea']}; font-size: 1.4rem; margin-bottom: 0.8rem; text-align: center;">
                        {item['name']}
                    </h4>
                    <p style="font-size: 1rem; line-height: 1.7; margin-bottom: 1rem; text-align: center;">
                        {item['description']}
                    </p>
                    <div style="text-align: center;">
                        <span style="background: {COLORS['sea']}15; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.85rem; color: {COLORS['sea']}; font-weight: 600;">
                            📍 {', '.join(item['locations'][:2])}
                        </span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    # Iconic Landscapes
    st.markdown(f"""
    <h3 style="color: {COLORS['primary']}; font-size: 2.2rem; margin: 3rem 0 1.5rem 0; text-align: center;">
        {beauty['landscapes']['title']}
    </h3>
    """, unsafe_allow_html=True)

    # Landscapes in single row (4 columns)
    cols = st.columns(4)

    for col, feature in zip(cols, beauty['landscapes']['features']):
        with col:
            st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">{feature['icon']}</div>
                <h4 style="color: {COLORS['primary']}; font-size: 1.1rem; margin-bottom: 0.8rem;">
                    {feature['name']}
                </h4>
                <p style="font-size: 0.9rem; line-height: 1.6; color: {COLORS['dark']};">
                    {feature['description']}
                </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)



# TAB 2: Environmental Challenges
with tab2:
    st.markdown(f"""
    <div style="text-align: center; max-width: 800px; margin: 2rem auto;">
        <h2 style="color: {COLORS['primary']}; font-size: 2.5rem; margin-bottom: 1rem;">
            Must-Visit National Parks
        </h2>
        <p style="font-size: 1.1rem; line-height: 1.8;">
            From the mythical peaks of Mount Olympus to the coastal wonders of Sounion, 
            Greece's national parks offer unforgettable natural experiences.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Map
    st.markdown("### 🗺️ Interactive Park Map")
    
    # Create map centered on Greece
    m = folium.Map(location=[38.5, 23.5], zoom_start=7, tiles='OpenStreetMap')
    
    # Add markers for parks
    for park in SITE_DATA['nature']['parks']:
        folium.Marker(
            location=park['coordinates'],
            popup=folium.Popup(f"""
                <div style="font-family: 'Inter', sans-serif; min-width: 200px;">
                    <h4 style="color: {COLORS['primary']}; margin-bottom: 0.5rem;">{park['name']}</h4>
                    <p style="margin: 0.3rem 0;"><strong>Best Season:</strong> {park['best_season']}</p>
                    <p style="margin: 0.3rem 0;"><strong>Activities:</strong> {', '.join(park['activities'][:2])}</p>
                </div>
            """, max_width=300),
            tooltip=park['name'],
            icon=folium.Icon(color='green', icon='tree', prefix='fa')
        ).add_to(m)
    
    # Add markers for islands
    for island in SITE_DATA['nature']['islands']:
        folium.Marker(
            location=island['coordinates'],
            popup=folium.Popup(f"""
                <div style="font-family: 'Inter', sans-serif; min-width: 200px;">
                    <h4 style="color: {COLORS['sea']}; margin-bottom: 0.5rem;">{island['name']}</h4>
                    <p style="margin: 0;">{island.get('nickname', island.get('tagline', ''))}</p>
                </div>
            """, max_width=300),
            tooltip=island['name'],
            icon=folium.Icon(color='blue', icon='water', prefix='fa')
        ).add_to(m)
    
    folium_static(m, width=1200, height=500)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Park Details
    for park in SITE_DATA['nature']['parks']:
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            img_html = render_image(park['image_placeholder'], class_name="park-image", alt=park['name'])

            st.markdown(f"""
            <div class="park-card">
                <div class="park-image-container">
                    {img_html}
                </div>  
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="park-card">
                <h3 style="color: {COLORS['primary']}; font-size: 2rem; margin-bottom: 1rem;">
                    {park['name']}
                </h3>
            """, unsafe_allow_html=True)
            
            # Key info
            if 'elevation_m' in park:
                st.markdown(f"**🏔️ Elevation:** {park['elevation_m']:,}m | ", unsafe_allow_html=False)
            if 'established' in park:
                st.markdown(f"**📅 Est.** {park['established']} | ", unsafe_allow_html=False)
            if 'designation' in park:
                st.markdown(f"**🏆** {park['designation']}", unsafe_allow_html=False)
            
            st.markdown(f"**🗓️ Best Season:** {park['best_season']}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Highlights
            st.markdown("**✨ Highlights:**")
            for highlight in park['highlights']:
                st.markdown(f"• {highlight}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Activities
            st.markdown("**Activities:**")
            activity_html = '<div class="activities-container">'

            for activity in park['activities']:
                activity_html += f'<span class="activity-badge">{activity}</span>'

            activity_html += '</div>'

            st.markdown(activity_html, unsafe_allow_html=True)
            # Quote
            if 'quote' in park:
                st.markdown(f"""
                <div style="background: {COLORS['light_gray']}; padding: 1rem; border-left: 4px solid {COLORS['secondary']}; border-radius: 4px; margin-top: 1rem; font-style: italic;">
                    "{park['quote']}"
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)

