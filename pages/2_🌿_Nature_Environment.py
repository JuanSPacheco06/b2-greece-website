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
tab1, tab2, tab3 = st.tabs(["🏞️ National Parks", "🌊 Environmental Challenges", "💡 Solutions & Future"])

# TAB 1: National Parks
with tab1:
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

# TAB 2: Environmental Challenges
with tab2:
    st.markdown(f"""
    <div style="text-align: center; max-width: 900px; margin: 2rem auto 3rem auto;">
        <h2 style="color: {COLORS['accent']}; font-size: 2.5rem; margin-bottom: 1rem;">
            Environmental Challenges
        </h2>
        <p style="font-size: 1.1rem; line-height: 1.8;">
            Greece faces serious environmental challenges including water scarcity, wildfires, 
            and climate change impacts. Understanding these issues is crucial for sustainable tourism.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Water Crisis Statistics
    st.markdown("### 💧 Water Crisis in Greece")
    
    col1, col2, col3, col4 = st.columns(4)
    
    water_stats = [
        {"number": "80%", "label": "Water Used in Agriculture"},
        {"number": "50%", "label": "Water Lost Before Homes"},
        {"number": "34%", "label": "Land Facing Desertification"},
        {"number": "70%", "label": "Water from Underground"}
    ]
    
    for col, stat in zip([col1, col2, col3, col4], water_stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{stat['number']}</div>
                <div class="stat-label">{stat['label']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="alert-box">
        <h4 style="color: {COLORS['accent']}; margin-bottom: 0.5rem;">⚠️ Critical Situation</h4>
        <p style="margin: 0;">
            {SITE_DATA['nature']['environmental_issues']['water_crisis']['description']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Wildfire Timeline
    st.markdown("### 🔥 Major Wildfires Timeline")
    

    
    fires = SITE_DATA['nature']['environmental_issues']['major_fires']


    # # Create timeline chart
    # fig = go.Figure()
    
    # years = [fire['year'] for fire in fires]
    # deaths = [fire['deaths'] for fire in fires]
    # events = [fire['event'] for fire in fires]
    
    # fig.add_trace(go.Scatter(
    #     x=years,
    #     y=deaths,
    #     mode='markers+lines+text',
    #     marker=dict(size=20, color=COLORS['accent']),
    #     line=dict(color=COLORS['accent'], width=3),
    #     text=[f"{e}<br>{d} deaths" for e, d in zip(events, deaths)],
    #     textposition="top center",
    #     textfont=dict(size=12),
    #     hovertemplate='<b>%{text}</b><extra></extra>'
    # ))
    
    # fig.update_layout(
    #     title="Impact of Major Wildfires",
    #     xaxis_title="Year",
    #     yaxis_title="Casualties",
    #     height=400,
    #     plot_bgcolor='white',
    #     paper_bgcolor='white',
    #     font=dict(family="Inter, sans-serif", size=14),
    #     showlegend=False
    # )
    
    # st.plotly_chart(fig, use_container_width=True)


    # Fire details
    col1, col2 = st.columns(2)
    
    for col, fire in zip([col1, col2], fires):
        with col:
            st.markdown(f"""
            <div class="alert-box">
                <h4 style="color: {COLORS['accent']};">{fire['year']} - {fire['event']}</h4>
                <p style="margin: 0.5rem 0;"><strong>Deaths:</strong> {fire['deaths']}</p>
            """, unsafe_allow_html=True)
            
            if fire['area_ha']:
                st.markdown(f"<p style='margin: 0.5rem 0;'><strong>Area Burned:</strong> {fire['area_ha']:,} hectares</p>", unsafe_allow_html=True)
            
            st.markdown(f"<p style='margin: 0.5rem 0;'><strong>Impact:</strong> {fire['impact']}</p></div>", unsafe_allow_html=True)

# TAB 3: Solutions
with tab3:
    st.markdown(f"""
    <div style="text-align: center; max-width: 900px; margin: 2rem auto 3rem auto;">
        <h2 style="color: {COLORS['olive']}; font-size: 2.5rem; margin-bottom: 1rem;">
            Solutions & Future
        </h2>
        <p style="font-size: 1.1rem; line-height: 1.8;">
            Greece is taking bold action to protect its environment through reforestation, 
            technology, and sustainable practices.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Reforestation Plan
    reforest = SITE_DATA['nature']['environmental_issues']['solutions']['reforestation']
    
    st.markdown("### 🌳 National Reforestation Plan")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="solution-box">
            <h4 style="color: {COLORS['olive']}; margin-bottom: 1rem;">Ambitious Tree Planting Initiative</h4>
            <p style="font-size: 1.1rem; line-height: 1.8;">
                Greece's National Reforestation Plan ({reforest['period']}) aims to plant 
                <strong>{reforest['target_trees']:,} trees</strong> using native, drought-resistant species 
                that can better withstand climate change impacts.
            </p>
            <p style="margin-top: 1rem; font-size: 1rem;">
                🌱 <strong>Approach:</strong> {reforest['approach']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card" style="border-top-color: {COLORS['olive']};">
            <div class="stat-number" style="color: {COLORS['olive']};">30M</div>
            <div class="stat-label">Trees by 2030</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Technology Solutions
    st.markdown("### 🛰️ Technology & Monitoring")
    
    col1, col2, col3 = st.columns(3)
    
    tech_solutions = SITE_DATA['nature']['environmental_issues']['solutions']['technology']
    
    icons = ["🚁", "🛰️", "🚨"]
    for col, tech, icon in zip([col1, col2, col3], tech_solutions, icons):
        with col:
            st.markdown(f"""
            <div class="park-card" style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
                <h4 style="color: {COLORS['primary']}; margin-bottom: 0.5rem;">Innovation</h4>
                <p style="font-size: 0.95rem;">{tech}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # CO2 Reduction
    co2 = SITE_DATA['nature']['environmental_issues']['solutions']['co2_reduction']
    
    st.markdown("### ♻️ CO₂ Emission Reduction")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown(f"""
        <div class="solution-box">
            <h4 style="color: {COLORS['olive']}; margin-bottom: 1rem;">Historic Climate Action</h4>
            <p style="line-height: 1.8;">
                {co2['description']}
            </p>
            <p style="margin-top: 1rem;">
                <strong>📉 2023 Achievement:</strong> {co2['2023_drop_percent']}% reduction in CO₂ emissions
            </p>
            <p style="margin-top: 0.5rem;">
                <strong>🎯 Target:</strong> Complete coal phase-out by {co2['coal_phaseout']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Progress visualization
        progress = (2025 - 2021) / (2028 - 2021) * 100
        
        st.markdown(f"""
        <div class="park-card" style="text-align: center;">
            <h4 style="color: {COLORS['olive']}; margin-bottom: 1rem;">Coal Phase-Out Progress</h4>
            <div style="font-size: 3rem; color: {COLORS['olive']}; margin: 1rem 0;">
                {int(progress)}%
            </div>
            <p style="font-size: 0.9rem; color: {COLORS['dark']};">
                On track for 2028 target
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to Action
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {COLORS['olive']} 0%, {COLORS['sea']} 100%); padding: 3rem; border-radius: 12px; text-align: center;">
        <h3 style="color: white; font-size: 2rem; margin-bottom: 1rem;">
            Travel Responsibly
        </h3>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; max-width: 700px; margin: 0 auto;">
            Support Greece's environmental efforts by choosing sustainable tourism options, 
            respecting natural areas, and learning about conservation initiatives during your visit.
        </p>
    </div>
    """, unsafe_allow_html=True)