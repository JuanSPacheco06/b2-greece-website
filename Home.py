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

    /* Travel Plans Section */
    .plans-section {{
        background: {COLORS['light_gray']};
        padding: 4rem 2rem;
        border-radius: 12px;
        margin: 4rem 0;
    }}

    .plan-card {{
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        margin-bottom: 2rem;
        border-top: 6px solid;
    }}

    .plan-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.2);
    }}

    .plan-header {{
        padding: 2rem;
        color: white;
        position: relative;
    }}

    .plan-body {{
        padding: 2rem;
    }}

    .plan-badge {{
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem 0.3rem 0.3rem 0;
    }}

    .destination-item {{
        background: {COLORS['light_gray']};
        padding: 1rem;
        border-radius: 8px;
        margin: 0.8rem 0;
        border-left: 4px solid {COLORS['primary']};
    }}

    .safety-box {{
        background: {COLORS['accent']}15;
        border-left: 4px solid {COLORS['accent']};
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }}

    /* Money & Payment Section */
    .money-section {{
        background: white;
        padding: 3rem 2rem;
        border-radius: 12px;
        margin: 4rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }}

    .payment-table {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 2rem 0;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}

    .payment-table thead {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['sea']} 100%);
        color: white;
    }}

    .payment-table thead tr {{
        display: table-row !important;
    }}
    .payment-table thead th {{
        display: table-cell !important;
    }}

    .payment-table th {{
        padding: 1.2rem 1rem;
        text-align: left;
        font-weight: 600;
        font-size: 1.1rem;
        border-bottom: 3px solid {COLORS['secondary']};
    }}

    .payment-table td {{
        padding: 1rem;
        border-bottom: 1px solid {COLORS['light_gray']};
        font-size: 0.95rem;
        vertical-align: top;
    }}

    .payment-table tbody tr {{
        transition: background 0.2s ease;
    }}

    .payment-table tbody tr:hover {{
        background: {COLORS['light_gray']};
    }}

    .payment-table tbody tr:last-child td {{
        border-bottom: none;
    }}

    .category-cell {{
        font-weight: 600;
        color: {COLORS['primary']};
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}

    .note-badge {{
        display: inline-block;
        background: {COLORS['secondary']};
        color: {COLORS['dark']};
        padding: 0.2rem 0.5rem;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 700;
        vertical-align: super;
        margin-left: 0.2rem;
    }}

    .tip-card {{
        background: {COLORS['light_gray']};
        padding: 1rem 1.5rem;
        border-radius: 8px;
        border-left: 4px solid {COLORS['secondary']};
        margin: 0.8rem 0;
        transition: all 0.3s ease;
    }}

    .tip-card:hover {{
        transform: translateX(5px);
        border-left-color: {COLORS['primary']};
    }}

    .currency-box {{
        background: linear-gradient(135deg, {COLORS['secondary']}20 0%, {COLORS['primary']}20 100%);
        padding: 2rem;
        border-radius: 12px;
        border: 2px solid {COLORS['secondary']};
        margin-bottom: 2rem;
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

# Travel Plans Section
def render_travel_plans():
    st.markdown(f"""
    <div class="plans-section">
        <div class="section-header">
            <h2 class="section-title">🗺️ Our Travel Plans</h2>
            <p class="section-subtitle"><strong>Pre-designed itineraries crafted by local experts</strong></p>
            <p style="text-align: center; max-width: 800px; margin: 1rem auto; font-size: 1.1rem; color: {COLORS['dark']};">
                Choose from our curated travel plans or use them as inspiration for your custom journey. 
                Each plan is designed to showcase the best of Greece while ensuring safety and comfort.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display each plan
    for plan in SITE_DATA['travel_plans']:
        # Difficulty badge color
        difficulty_color = {
            "Easy": COLORS['olive'],
            "Moderate": COLORS['secondary'],
            "Challenging": COLORS['accent']
        }.get(plan['difficulty'], COLORS['primary'])
        
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            # Plan image
            img_html = render_image(plan['image_placeholder'], class_name="destination-image", alt=plan['title'])
            st.markdown(f"""
            <div class="image-placeholder" style="min-height: 350px;">
                {img_html}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="plan-card" style="border-top-color: {plan['color']};">
                <div class="plan-header" style="background: linear-gradient(135deg, {plan['color']} 0%, {plan['color']}CC 100%);">
                    <div style="font-size: 3rem; margin-bottom: 0.5rem;">{plan['icon']}</div>
                    <h3 style="font-size: 2rem; margin-bottom: 0.3rem; color: white;">{plan['title']}</h3>
                    <p style="font-size: 1.2rem; opacity: 0.9; margin: 0; color: white;">{plan['subtitle']}</p>
                </div>
                <div class="plan-body">
                    <div style="margin-bottom: 1rem;">
                        <span class="plan-badge" style="background: {difficulty_color}; color: white;">
                            {plan['difficulty']}
                        </span>
                        <span class="plan-badge" style="background: {COLORS['primary']}; color: white;">
                            📅 {plan['duration']}
                        </span>
                        <span class="plan-badge" style="background: {COLORS['secondary']}; color: {COLORS['dark']};">
                            🌤️ {plan['best_season']}
                        </span>
                    </div>
                    <p style="font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
                        {plan['overview']}
                    </p>
            """, unsafe_allow_html=True)
            
        # ---------------------------------------------
        # 🔥 New Itinerary Highlights in TWO COLUMNS
        # ---------------------------------------------
        st.markdown(
            f"<h4 style='color: {plan['color']}; margin-bottom: 1rem;'>📍 Itinerary Highlights</h4>",
            unsafe_allow_html=True
        )

        col_left, col_right = st.columns(2)

        for idx, dest in enumerate(plan['destinations']):
            target_col = col_left if idx % 2 == 0 else col_right
            with target_col:
                st.markdown(f"""
                <div class="destination-item" style="border-left-color: {plan['color']}; margin-bottom: 1.2rem;">
                    <strong style="color: {plan['color']}; font-size: 1.15rem;">
                        {idx + 1}. {dest['name']}
                    </strong>
                    {f"<span style='float: right; color: {COLORS['dark']}; font-size: 0.9rem;'>⏱️ {dest['duration']}</span>" 
                        if 'duration' in dest else ""}
                    <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
                """, unsafe_allow_html=True)

                for activity in dest['activities']:
                    st.markdown(f"<li style='margin: 0.3rem 0;'>{activity}</li>", unsafe_allow_html=True)

                if 'accommodation' in dest:
                    st.markdown(
                        f"<p style='margin-top: 0.5rem; font-size: 0.9rem;'><strong>🏨 Stay:</strong> {dest['accommodation']}</p>",
                        unsafe_allow_html=True
                    )

                st.markdown("</ul></div>", unsafe_allow_html=True)
        # ---------------------------------------------
        # END Two-column itinerary section
        # ---------------------------------------------
        
        # Special notes
        if 'special_note' in plan:
            st.markdown(f"""
            <div class="safety-box">
                <strong>⚠️ Important:</strong> {plan['special_note']}
            </div>
            """, unsafe_allow_html=True)
        
        if 'access' in plan:
            st.markdown(f"""
            <p style="margin-top: 1rem; padding: 0.8rem; background: {COLORS['light_gray']}; border-radius: 8px;">
                <strong>✈️ Access:</strong> {plan['access']}
            </p>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)       
    
    # Safety precautions section
    st.markdown(f"""
    <div style="background: white; padding: 2rem; border-radius: 12px; margin-top: 2rem; border: 2px solid {COLORS['accent']};">
        <h3 style="color: {COLORS['accent']}; text-align: center; margin-bottom: 1.5rem;">
            🛡️ General Safety Precautions
        </h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    safety_items = [
        {"icon": "🏙️", "title": "Urban Safety", "text": SITE_DATA['safety_precautions']['urban']},
        {"icon": "⛰️", "title": "Mountain Safety", "text": SITE_DATA['safety_precautions']['mountain']},
        {"icon": "🌋", "title": "Natural Risks", "text": SITE_DATA['safety_precautions']['natural']},
        {"icon": "🚗", "title": "Road Safety", "text": SITE_DATA['safety_precautions']['road']}
    ]
    
    for idx, item in enumerate(safety_items):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class="safety-box">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{item['icon']}</div>
                <strong style="color: {COLORS['accent']};">{item['title']}:</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.95rem; line-height: 1.6;">{item['text']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

# Money & Payment Information Section
def render_money_info():
    st.markdown(f"""
    <div class="money-section">
        <div class="section-header">
            <h2 class="section-title">💰 Before You Choose...</h2>
            <p class="section-subtitle"><strong>Here's what you need to know so you're never caught off guard!</strong></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Currency info box
    currency = SITE_DATA['money_info']['currency']
    st.markdown(f"""
    <div class="currency-box">
        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
            <div style="font-size: 4rem;">💶</div>
            <div>
                <h3 style="color: {COLORS['primary']}; margin: 0; font-size: 2rem;">{currency['name']}</h3>
                <p style="margin: 0.3rem 0 0 0; font-size: 1.1rem; color: {COLORS['dark']};">
                    Code: <strong>{currency['code']}</strong> | Symbol: <strong>{currency['symbol']}</strong>
                </p>
            </div>
        </div>
        <p style="font-size: 1.05rem; line-height: 1.7; color: {COLORS['dark']}; margin: 0;">
            {currency['intro']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Payment methods table
    st.markdown(f"""
    <h3 style="color: {COLORS['primary']}; text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2rem;">
        💳 Payment Methods Accepted
    </h3>
    """, unsafe_allow_html=True)
    
    # Build the table
    table_html = f"""
    <table class="payment-table">
        <thead>
            <tr>
                <th style="width: 30%;">Payment for...</th>
                <th style="width: 40%;">Card 💳</th>
                <th style="width: 30%;">Cash 💵</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for item in SITE_DATA['money_info']['payment_methods']:
        note_badge = f'<span class="note-badge">{item["card_note"]}</span>' if item['card_note'] else ''
        
        table_html += f"""
        <tr>
            <td>
                <div class="category-cell">
                    <span style="font-size: 1.5rem;">{item['emoji']}</span>
                    <span>{item['category'].replace(item['emoji'] + ' ', '')}</span>
                </div>
            </td>
            <td>{item['card']}{note_badge}</td>
            <td>{item['cash']}</td>
        </tr>
        """
    
    table_html += """
        </tbody>
    </table>
    """
    
    st.html(table_html)
        
    # Quick tips section
    st.markdown(f"""
    <h3 style="color: {COLORS['primary']}; text-align: center; margin: 3rem 0 1.5rem 0; font-size: 1.8rem;">
        💡 Smart Money Tips for Travelers
    </h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    tips = SITE_DATA['money_info']['tips']
    
    for idx, tip in enumerate(tips):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class="tip-card">
                <p style="margin: 0; font-size: 1rem; line-height: 1.6;">{tip}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

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
        <p class="section-subtitle"><strong>From ancient cities to hidden paradises.</strong></p>
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
            Greek Escape © 2025
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
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        ### 🧭 Navigation
        Use the pages in the sidebar to explore:
        - 🏛️ **Arts, Literature & Culture**
        - 🌿 **Nature & Environment**
        - 🍽️ **Gastronomy**
        - ⛰️ **Places to visit**
        - 🏙️**vs**🏕️ 
        - 📊 **Data & Maps**
        """)
        
        st.markdown("---")
        
        st.info("📍 **It's Time to Travel** - Discover the magic of Greece through ancient heritage, vibrant culture, and inspiring nature.")
    
    # Main content
    render_hero()
    render_why_visit()
    render_travel_plans()
    render_money_info() 
    render_stats()
    render_featured_destinations()
    render_footer()

if __name__ == "__main__":
    main()