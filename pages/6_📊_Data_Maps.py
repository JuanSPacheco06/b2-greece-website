import streamlit as st
import folium
from streamlit_folium import folium_static
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from utils.data import SITE_DATA, COLORS, UI_TEXT

st.set_page_config(
    page_title="Data & Maps | Greek Escape",
    page_icon="📊",
    layout="wide"
)

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    h1, h2, h3 {{ font-family: 'Playfair Display', serif; }}
    p {{ font-family: 'Inter', sans-serif; line-height: 1.8; }}
    
    .page-header {{
        background: linear-gradient(135deg, {COLORS['olive']} 0%, {COLORS['accent']} 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 3rem;
        color: white;
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
    
    .info-box {{
        background: {COLORS['light_gray']};
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid {COLORS['primary']};
        margin: 1rem 0;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="page-header">
    <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">📊 Data & Maps</h1>
    <p style="font-size: 1.3rem; opacity: 0.9;">Explore Greece through interactive visualizations and insights</p>
</div>
""", unsafe_allow_html=True)

# Tab Navigation
tab1, tab2, tab3 = st.tabs(["🗺️ Interactive Map", "📈 Key Statistics", "🔥 Environmental Timeline"])

# TAB 1: Interactive Map
with tab1:
    st.markdown(f"""
    <div style="text-align: center; margin: 2rem auto;">
        <h2 style="color: {COLORS['primary']}; font-size: 2.5rem; margin-bottom: 1rem;">
            Explore Greece Interactively
        </h2>
        <p style="font-size: 1.1rem; max-width: 800px; margin: 0 auto 2rem auto; line-height: 1.8;">
            Click on markers to discover detailed information about national parks, islands, 
            and key destinations across Greece.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create comprehensive map
    m = folium.Map(
        location=[38.5, 23.5],
        zoom_start=6,
        tiles='OpenStreetMap'
    )
    
    # Add National Parks
    for park in SITE_DATA['nature']['parks']:
        popup_html = f"""
        <div style="font-family: 'Inter', sans-serif; min-width: 250px; max-width: 300px;">
            <h3 style="color: {COLORS['primary']}; margin-bottom: 0.8rem; font-size: 1.3rem;">{park['name']}</h3>
            <p style="margin: 0.5rem 0;"><strong>Type:</strong> National Park</p>
        """
        
        if 'elevation_m' in park:
            popup_html += f"<p style='margin: 0.5rem 0;'><strong>Elevation:</strong> {park['elevation_m']:,}m</p>"
        
        popup_html += f"""
            <p style="margin: 0.5rem 0;"><strong>Best Season:</strong> {park['best_season']}</p>
            <p style="margin: 0.5rem 0;"><strong>Top Activities:</strong></p>
            <ul style="margin: 0.3rem 0; padding-left: 1.2rem;">
                <li>{park['activities'][0]}</li>
                <li>{park['activities'][1]}</li>
            </ul>
        </div>
        """
        
        folium.Marker(
            location=park['coordinates'],
            popup=folium.Popup(popup_html, max_width=350),
            tooltip=park['name'],
            icon=folium.Icon(color='green', icon='mountain', prefix='fa')
        ).add_to(m)
    
    # Add Islands
    for island in SITE_DATA['nature']['islands']:
        popup_html = f"""
        <div style="font-family: 'Inter', sans-serif; min-width: 250px;">
            <h3 style="color: {COLORS['sea']}; margin-bottom: 0.8rem; font-size: 1.3rem;">{island['name']}</h3>
            <p style="margin: 0.5rem 0; font-style: italic;">"{island.get('nickname', island.get('tagline', ''))}"</p>
            <p style="margin: 0.5rem 0;"><strong>Highlights:</strong></p>
            <ul style="margin: 0.3rem 0; padding-left: 1.2rem;">
        """
        
        for highlight in island['highlights'][:3]:
            popup_html += f"<li>{highlight}</li>"
        
        popup_html += "</ul></div>"
        
        folium.Marker(
            location=island['coordinates'],
            popup=folium.Popup(popup_html, max_width=350),
            tooltip=island['name'],
            icon=folium.Icon(color='blue', icon='umbrella-beach', prefix='fa')
        ).add_to(m)
    
    # Add Athens marker
    folium.Marker(
        location=[37.9838, 23.7275],
        popup=folium.Popup("""
            <div style="font-family: 'Inter', sans-serif; min-width: 200px;">
                <h3 style="color: #0066CC; margin-bottom: 0.5rem;">Athens</h3>
                <p style="margin: 0.3rem 0;">Capital of Greece</p>
                <p style="margin: 0.3rem 0;">Over 3,000 years of history</p>
                <p style="margin: 0.3rem 0;"><strong>Must-see:</strong> Acropolis, Ancient Agora, Plaka</p>
            </div>
        """, max_width=250),
        tooltip="Athens - Capital",
        icon=folium.Icon(color='red', icon='landmark', prefix='fa')
    ).add_to(m)
    
    folium_static(m, width=1400, height=600)
    
    # Map Legend
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="info-box" style="border-left-color: red;">
            <strong>🔴 Red Markers:</strong> Major Cities
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="info-box" style="border-left-color: green;">
            <strong>🟢 Green Markers:</strong> National Parks
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="info-box" style="border-left-color: blue;">
            <strong>🔵 Blue Markers:</strong> Islands & Coastal Areas
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="info-box">
            <strong>💡 Tip:</strong> Click markers for details
        </div>
        """, unsafe_allow_html=True)

# TAB 2: Key Statistics
with tab2:
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
        {"value": "6,000+", "label": "Islands & Islets"},
        {"value": "2,917m", "label": "Highest Peak"},
        {"value": "16,000km", "label": "Coastline Length"}
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
    
    # Environmental Statistics
    st.markdown(f"""
    <h3 style="color: {COLORS['accent']}; font-size: 2rem; margin: 2rem 0 1.5rem 0; text-align: center;">
        🌊 Environmental Data
    </h3>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    env_metrics = [
        {"value": "80%", "label": "Water for Agriculture", "color": COLORS['primary']},
        {"value": "50%", "label": "Water Loss Rate", "color": COLORS['accent']},
        {"value": "34%", "label": "Land Desertified", "color": COLORS['accent']},
        {"value": "70%", "label": "Underground Water", "color": COLORS['primary']}
    ]
    
    for col, metric in zip([col1, col2, col3, col4], env_metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card" style="border-top: 4px solid {metric['color']};">
                <div class="metric-value" style="color: {metric['color']};">{metric['value']}</div>
                <div class="metric-label">{metric['label']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Water Usage Distribution Chart
    st.markdown("### 💧 Water Usage Distribution")
    
    fig = go.Figure(data=[go.Pie(
        labels=['Agriculture', 'Residential', 'Industry', 'Tourism'],
        values=[80, 10, 5, 5],
        hole=.4,
        marker_colors=[COLORS['primary'], COLORS['olive'], COLORS['sea'], COLORS['secondary']]
    )])
    
    fig.update_layout(
        title="How Greece Uses Its Freshwater",
        font=dict(family="Inter, sans-serif", size=14),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tourism Statistics
    st.markdown(f"""
    <h3 style="color: {COLORS['primary']}; font-size: 2rem; margin: 2rem 0 1.5rem 0; text-align: center;">
        ✈️ Tourism Impact
    </h3>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    tourism_stats = [
        {"value": "33M+", "label": "Annual Visitors (2019)"},
        {"value": "20%", "label": "of GDP from Tourism"},
        {"value": "900K+", "label": "Tourism Jobs"}
    ]
    
    for col, stat in zip([col1, col2, col3], tourism_stats):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{stat['value']}</div>
                <div class="metric-label">{stat['label']}</div>
            </div>
            """, unsafe_allow_html=True)

# TAB 3: Environmental Timeline
with tab3:
    st.markdown(f"""
    <div style="text-align: center; margin: 2rem auto 3rem auto;">
        <h2 style="color: {COLORS['accent']}; font-size: 2.5rem; margin-bottom: 1rem;">
            🔥 Wildfire Impact Timeline
        </h2>
        <p style="font-size: 1.1rem; max-width: 800px; margin: 0 auto; line-height: 1.8;">
            Major wildfires have significantly impacted Greece's environment and communities. 
            Understanding this history helps us appreciate conservation efforts.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    fires = SITE_DATA['nature']['environmental_issues']['major_fires']
        
    # Detailed Fire Information
    st.markdown("### 📋 Fire Event Details")
    
    for fire in fires:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div class="info-box" style="border-left-color: {COLORS['accent']};">
                <h4 style="color: {COLORS['accent']}; margin-bottom: 0.8rem; font-size: 1.4rem;">
                    {fire['year']} - {fire['event']}
                </h4>
                <p style="font-size: 1rem; line-height: 1.6; margin-bottom: 0.5rem;">
                    {fire['impact']}
                </p>
                <p style="margin: 0.3rem 0;"><strong>Casualties:</strong> {fire['deaths']} deaths</p>
            """, unsafe_allow_html=True)
            
            if fire['area_ha']:
                st.markdown(f"<p style='margin: 0.3rem 0;'><strong>Area Burned:</strong> {fire['area_ha']:,} hectares</p>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card" style="border-top-color: {COLORS['accent']}; height: 100%;">
                <div class="metric-value" style="color: {COLORS['accent']};">{fire['year']}</div>
                <div class="metric-label">{fire['event'].split()[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Solutions Progress
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <h3 style="color: {COLORS['olive']}; font-size: 2rem; margin: 2rem 0 1.5rem 0; text-align: center;">
        🌱 Reforestation Progress
    </h3>
    """, unsafe_allow_html=True)
    
    reforest = SITE_DATA['nature']['environmental_issues']['solutions']['reforestation']
    
    # Progress visualization
    years_passed = 2025 - 2021
    total_years = 2030 - 2021
    progress = (years_passed / total_years) * 100
    trees_planted_estimate = (reforest['target_trees'] * progress) / 100
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=progress,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': f"National Reforestation Plan Progress<br><sub>{reforest['period']}</sub>", 'font': {'size': 20}},
        delta={'reference': 50, 'suffix': "%"},
        gauge={
            'axis': {'range': [None, 100], 'ticksuffix': "%"},
            'bar': {'color': COLORS['olive']},
            'steps': [
                {'range': [0, 50], 'color': COLORS['light_gray']},
                {'range': [50, 100], 'color': "#E8F5E9"}
            ],
            'threshold': {
                'line': {'color': COLORS['accent'], 'width': 4},
                'thickness': 0.75,
                'value': 100
            }
        }
    ))
    
    fig.update_layout(
        height=400,
        font=dict(family="Inter, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="border-top-color: {COLORS['olive']};">
            <div class="metric-value" style="color: {COLORS['olive']};">{int(trees_planted_estimate/1000000)}M+</div>
            <div class="metric-label">Trees Planted (Est.)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="border-top-color: {COLORS['olive']};">
            <div class="metric-value" style="color: {COLORS['olive']};">30M</div>
            <div class="metric-label">Target by 2030</div>
        </div>
        """, unsafe_allow_html=True)

# Final CTA
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="background: linear-gradient(135deg, {COLORS['olive']} 0%, {COLORS['accent']} 100%); padding: 3rem; border-radius: 12px; text-align: center;">
    <h3 style="color: white; font-size: 2rem; margin-bottom: 1rem;">
        Explore More Data
    </h3>
    <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 0;">
        Want deeper insights? Contact us for detailed travel statistics and environmental reports.
    </p>
</div>
""", unsafe_allow_html=True)