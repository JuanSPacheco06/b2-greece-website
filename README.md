# 🇬🇷 Greek Escape: Four Cities, One Dream

A professional travel agency web application built with Streamlit, showcasing the cultural heritage, natural beauty, and culinary delights of Greece.

## ✨ Features

- **🏛️ Culture & Art**: Explore Athens, festivals, and traditional crafts
- **🌿 Nature & Environment**: Interactive maps of national parks, environmental data, and conservation efforts
- **🍽️ Gastronomy**: Discover authentic Greek dishes with filtering by region and type
- **📚 Writers & Literature**: Learn about Homer, Kiki Dimoula, and Greek literary tradition
- **📷 Gallery**: Visual journey with filterable image collections
- **📊 Data & Maps**: Interactive visualizations and statistics about Greece

## 📦 Installation

### Prerequisites
- Python 3.8+
- `uv` package manager

### Setup Instructions

1. **Clone or create your project structure**:
```bash
mkdir greek-escape
cd greek-escape
```

2. **Install dependencies with uv**:
```bash
uv add streamlit
uv add streamlit-folium
uv add folium
uv add plotly
uv add pandas
```

3. **Create the folder structure**:
```bash
mkdir -p pages utils assets/images
```

4. **Copy all the provided files**:
   - `app.py` → main application
   - `utils/data.py` → centralized data structure
   - `pages/1_🏛️_Culture_Art.py`
   - `pages/2_🌿_Nature_Environment.py`
   - `pages/3_🍽️_Gastronomy.py`
   - `pages/4_📚_Writers_Literature.py`
   - `pages/5_📷_Gallery.py`
   - `pages/6_📊_Data_Maps.py`

5. **Create assets folder for images**:
```bash
mkdir -p assets/images
touch assets/images/.gitkeep
```

## 🚀 Running the Application

Start the application with:

```bash
streamlit run app.py
```

Or with uv:

```bash
uv run streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`

## 📸 Adding Images

Place your images in the `assets/images/` folder. The application has placeholder spaces configured for the following images:

### Home Page
- `hero_acropolis.jpg` (1920x600px) - Hero background
- `athens_panorama.jpg` (800x600px)
- `milos_klima.jpg` (800x600px)
- `olympus_trail.jpg` (800x600px)

### Culture & Art Page
- `athens_acropolis.jpg` (700x500px)
- `kalamata_festival.jpg` (700x500px)
- `greek_crafts.jpg` (700x500px)

### Nature & Environment Page
- `mount_olympus.jpg` (700x500px)
- `sounion_temple.jpg` (700x500px)
- `milos_sarakiniko.jpg` (700x500px)
- `corinth_canal.jpg` (700x500px)

### Gastronomy Page
- `souvlaki.jpg` (700x500px)
- `moussaka.jpg` (700x500px)
- `tzatziki.jpg` (700x500px)
- `pitaraka.jpg` (700x500px)
- `ladenia.jpg` (700x500px)
- `kalamata_olives.jpg` (700x500px)
- `sfela_cheese.jpg` (700x500px)
- `greek_wine.jpg` (700x500px)

### Writers & Literature Page
- `homer_bust.jpg` (600x600px)
- `kiki_dimoula.jpg` (600x600px)

### Gallery Page
- `acropolis_sunset.jpg` (800x600px)
- `sarakiniko_beach.jpg` (800x600px)
- `olympus_peak.jpg` (800x600px)
- `klima_village.jpg` (800x600px)
- `temple_poseidon.jpg` (800x600px)
- `corinth_canal.jpg` (800x600px)

## 🎨 Customization

### Colors
Edit `utils/data.py` to customize the color palette:
```python
COLORS = {
    "primary": "#0066CC",      # Aegean blue
    "secondary": "#FFD700",    # Golden sun
    "accent": "#E63946",       # Mediterranean red
    # ... more colors
}
```

### Content
All content is centralized in `utils/data.py`. Edit the `SITE_DATA` dictionary to update:
- Destinations and descriptions
- Writers and literary content
- Gastronomy items
- Environmental data
- Gallery images metadata

### UI Text
Modify micro-copy and button labels in the `UI_TEXT` dictionary in `utils/data.py`

## 📁 Project Structure

```
greek-escape/
├── app.py                              # Main application
├── pages/
│   ├── 1_🏛️_Culture_Art.py
│   ├── 2_🌿_Nature_Environment.py
│   ├── 3_🍽️_Gastronomy.py
│   ├── 4_📚_Writers_Literature.py
│   ├── 5_📷_Gallery.py
│   └── 6_📊_Data_Maps.py
├── utils/
│   └── data.py                        # Centralized data structure
├── assets/
│   └── images/                        # Image files
└── README.md
```

## 🌟 Features in Detail

### Interactive Maps
- **Folium integration**: Click markers for detailed information
- **Multiple layers**: National parks, islands, cities
- **Responsive design**: Works on mobile and desktop

### Data Visualizations
- **Plotly charts**: Environmental statistics, water usage, wildfire timeline
- **Progress indicators**: Reforestation plan tracking
- **Real-time filtering**: Gallery and gastronomy filters

### Responsive Design
- **Mobile-friendly**: Adapts to all screen sizes
- **Touch-optimized**: Easy navigation on tablets and phones
- **Fast loading**: Optimized performance

## 🛠️ Technical Stack

- **Streamlit** - Web framework
- **Folium** - Interactive maps
- **Plotly** - Data visualizations
- **Pandas** - Data processing
- **Custom CSS** - National Geographic-inspired design

## 📝 Notes

- All content is in **English** as specified
- **Human Rights section excluded** as requested
- Image placeholders show exact filenames and recommended dimensions
- All data sourced from the provided PDF document

## 🎯 Academic Project

This is an academic project simulating a professional travel agency website for Greece. The design is inspired by National Geographic with modern aesthetics, animations, and organized content structure.

## 📧 Contact

For questions or improvements, feel free to reach out!

---

**Greek Escape © 2025** | Four Cities, One Dream