# utils/data.py
"""
Centralized data structure for Greece Travel Agency
All content is structured and ready to use across pages
"""

SITE_DATA = {
    "home": {
        "hero_title": "Greece: Ancient Heritage, Vibrant Culture & Inspiring Nature",
        "hero_subtitle": "Explore Athens, volcanic islands, national parks, and the poetry that shaped the West",
        "tagline": "Discover mythical routes, volcanic beaches, and the literature that inspired civilizations"
    },
    
    "culture": [
        {
            "title": "Athens: The Heart of Ancient Greece",
            "description": "Walk through Plaka and Syntagma Square, full of cafés, shops, and local art. Visit the Acropolis, explore the Ancient Agora, and enjoy breathtaking sunsets from Filopappou Hill.",
            "highlights": ["Acropolis", "Ancient Agora", "Plaka District", "Filopappou Hill"],
            "best_time": "April-October",
            "image_placeholder": "athens_acropolis.jpg"
        },
        {
            "title": "Kalamata Dance Festival",
            "description": "Experience the internationally renowned Kalamata International Dance Festival every July. Dance under the stars and immerse yourself in contemporary performances from around the world.",
            "highlights": ["July Festival", "Contemporary Dance", "Open-air Performances"],
            "best_time": "July",
            "image_placeholder": "kalamata_festival.jpg"
        },
        {
            "title": "Traditional Crafts & Folk Art",
            "description": "Discover authentic Greek handcrafts in Kalamata's local workshops and markets. From traditional textiles to pottery, experience the artisan heritage of Greece.",
            "highlights": ["Handcrafted Textiles", "Traditional Pottery", "Local Markets"],
            "best_time": "Year-round",
            "image_placeholder": "greek_crafts.jpg"
        }
    ],
    
    "literature": [
        {
            "name": "Homer",
            "period": "8th Century BC",
            "summary": "One of the most important writers in world history, known as the author of two great epic poems: The Iliad and The Odyssey.",
            "themes": ["Honor", "Heroism", "Fate", "Loyalty", "Gods & Humans"],
            "legacy": "His works became the foundation of Greek education and a model for later poets and writers throughout history. Homer's epics are the cornerstone of Western literary tradition.",
            "fun_facts": [
                "Stories were told by voice, passed from one person to another",
                "His exact identity is debated - single person or collective name?",
                "Homeric similes are extended comparisons that enhance drama",
                "Athens has used his works for over 3,000 years"
            ],
            "image_placeholder": "homer_bust.jpg"
        },
        {
            "name": "Kiki Dimoula",
            "period": "1931-2020",
            "summary": "A celebrated Greek poet known for her emotional and thoughtful writing about love, loss, time, and the power of memory.",
            "themes": ["Love", "Loss", "Time", "Memory", "Everyday Life"],
            "legacy": "Received the European Prize for Literature in 2009. Her work made her one of the most respected voices in modern Greek literature.",
            "fun_facts": [
                "Used simple words but deep ideas",
                "Showed how people feel in everyday life",
                "Many national and international awards",
                "Contemporary voice of Greek poetry"
            ],
            "image_placeholder": "kiki_dimoula.jpg"
        }
    ],
    
    "nature": {
        "parks": [
            {
                "name": "Mount Olympus National Park",
                "elevation_m": 2917,
                "established": 1938,
                "designation": "UNESCO Biosphere Reserve",
                "best_season": "June-October",
                "highlights": [
                    "Tallest mountain in Greece (2,917m)",
                    "Mythical home of the Greek gods",
                    "1,700+ plant species",
                    "Iconic wildlife sanctuary"
                ],
                "activities": ["Hiking", "Wildlife watching", "Photography", "Climbing"],
                "main_peaks": ["Mytikas", "Skolio", "Stefani"],
                "hiking_routes": ["From Litochoro", "E4 Trail", "Ascent to Mytikas"],
                "quote": "This mythical dream comes true! … to walk upon the sleeping Olympus… it happened, we arrived! — Frederic Boissonnas",
                "coordinates": [40.0854, 22.3586],
                "image_placeholder": "mount_olympus.jpg"
            },
            {
                "name": "Sounion National Park",
                "distance_from_athens_km": 70,
                "location": "Southern tip of Attica Peninsula",
                "best_season": "Year-round",
                "highlights": [
                    "Temple of Poseidon",
                    "Rocky hills & high sea cliffs",
                    "Pine forests & coastal scrub",
                    "Panoramic Aegean Sea views"
                ],
                "activities": ["Sunset watching", "Photography", "Hiking", "Beach exploration"],
                "climate": "Warm, dry Mediterranean with lots of sunshine",
                "quote": "Absolutely stunning place! The views over the Aegean are breathtaking, and the sunset behind the Temple of Poseidon is pure magic.",
                "coordinates": [37.6511, 24.0253],
                "image_placeholder": "sounion_temple.jpg"
            }
        ],
        
        "islands": [
            {
                "name": "Milos",
                "nickname": "Greece's Hidden Paradise",
                "highlights": [
                    "Sarakiniko's moon-white cliffs",
                    "Klima fishing village",
                    "70+ breathtaking beaches",
                    "Ancient catacombs"
                ],
                "local_flavors": ["Pitaraka (cheese pies)", "Ladenia (Greek pizza)", "Pure volcanic island honey"],
                "coordinates": [36.7213, 24.4266],
                "image_placeholder": "milos_sarakiniko.jpg"
            },
            {
                "name": "Corinth",
                "tagline": "The Link Between Two Seas",
                "highlights": [
                    "Corinth Canal boat trips",
                    "Temple of Apollo",
                    "Archaeological Museum",
                    "Ancient Corinth site"
                ],
                "coordinates": [37.9067, 22.8792],
                "image_placeholder": "corinth_canal.jpg"
            }
        ],
        
        "environmental_issues": {
            "water_crisis": {
                "agriculture_usage_percent": 80,
                "groundwater_share_percent": 70,
                "water_loss_percent": 50,
                "desertified_percent": 34,
                "description": "Greece faces serious water challenges, especially in the south and islands. About 80% of freshwater supports agriculture (olives, cotton), while 50% is lost before reaching homes."
            },
            "major_fires": [
                {
                    "year": 2018,
                    "event": "Attica Fire",
                    "deaths": 100,
                    "area_ha": None,
                    "impact": "Devastating loss of life and biodiversity"
                },
                {
                    "year": 2023,
                    "event": "Dadia Forest Fire",
                    "area_ha": 73000,
                    "deaths": 18,
                    "impact": "Massive ecological damage, wildlife loss"
                }
            ],
            "solutions": {
                "reforestation": {
                    "period": "2021-2030",
                    "target_trees": 30000000,
                    "approach": "National Reforestation Plan with native drought-resistant trees"
                },
                "technology": [
                    "Drone technology for monitoring",
                    "Satellite detection systems",
                    "Early warning systems"
                ],
                "co2_reduction": {
                    "2023_drop_percent": 5.93,
                    "coal_phaseout": 2028,
                    "description": "Greece plans to phase out all coal-fired power by 2028, investing billions in green transition"
                }
            }
        }
    },
    
    "gastronomy": [
        {
            "name": "Souvlaki",
            "description": "Grilled meat skewers, a Greek street food classic",
            "region": "All Greece",
            "type": "Main Course",
            "image_placeholder": "souvlaki.jpg"
        },
        {
            "name": "Moussaka",
            "description": "Layered eggplant and meat casserole with béchamel",
            "region": "All Greece",
            "type": "Main Course",
            "image_placeholder": "moussaka.jpg"
        },
        {
            "name": "Tzatziki",
            "description": "Yogurt and cucumber dip with garlic and herbs",
            "region": "All Greece",
            "type": "Appetizer",
            "image_placeholder": "tzatziki.png"
        },
        {
            "name": "Pitarakia",
            "description": "Golden cheese pies from Milos",
            "region": "Milos",
            "type": "Snack",
            "image_placeholder": "pitaraka.jpg"
        },
        {
            "name": "Ladenia",
            "description": "Traditional Greek pizza from Milos",
            "region": "Milos",
            "type": "Main Course",
            "image_placeholder": "ladenia.jpg"
        },
        {
            "name": "Kalamata Olives",
            "description": "World-famous dark purple olives",
            "region": "Kalamata",
            "type": "Appetizer",
            "image_placeholder": "kalamata_olives.jpg"
        },
        {
            "name": "Sfela Cheese",
            "description": "Semi-hard sheep's milk cheese",
            "region": "Peloponnese",
            "type": "Cheese",
            "image_placeholder": "sfela_cheese.jpg"
        },
        {
            "name": "Local Wine",
            "description": "Pair any meal with delicious Greek wine",
            "region": "All Greece",
            "type": "Beverage",
            "image_placeholder": "greek_wine.jpg"
        }
    ],
    
    "gallery_images": [
        {
            "filename": "acropolis_sunset.jpg",
            "caption": "Acropolis at golden hour",
            "region": "Athens",
            "type": "temple"
        },
        {
            "filename": "sarakiniko_beach.jpg",
            "caption": "Sarakiniko's lunar landscape",
            "region": "Milos",
            "type": "beach"
        },
        {
            "filename": "olympus_peak.jpg",
            "caption": "Mount Olympus summit trail",
            "region": "Thessaly",
            "type": "mountain"
        },
        {
            "filename": "klima_village.jpg",
            "caption": "Colorful Klima fishing village",
            "region": "Milos",
            "type": "village"
        },
        {
            "filename": "temple_poseidon.jpg",
            "caption": "Temple of Poseidon at Sounion",
            "region": "Attica",
            "type": "temple"
        },
        {
            "filename": "corinth_canal.jpg",
            "caption": "The impressive Corinth Canal",
            "region": "Peloponnese",
            "type": "landmark"
        }
    ]
}

# Color palette inspired by Greece
COLORS = {
    "primary": "#0066CC",      # Aegean blue
    "secondary": "#FFD700",    # Golden sun
    "accent": "#E63946",       # Mediterranean red
    "white": "#FFFFFF",        # Whitewashed buildings
    "dark": "#1A1A1A",         # Dark text
    "light_gray": "#F5F5F5",   # Light background
    "olive": "#6B8E23",        # Olive green
    "sea": "#4A90E2"           # Sea blue
}

# Micro-copy for UI elements
UI_TEXT = {
    "explore_culture": "Explore Cultural Routes",
    "explore_nature": "Discover Nature",
    "view_parks": "View National Parks",
    "view_gallery": "Beach Gallery",
    "read_more": "Read More",
    "learn_more": "Learn More",
    "empty_state": "No results found — try removing filters or searching another region",
    "contact_cta": "Plan Your Journey",
    "tagline": "Discover mythical routes, volcanic beaches, and the literature that inspired civilizations"
}