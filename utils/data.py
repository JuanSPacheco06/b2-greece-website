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
                "local_flavors": [
                    "Pitaraka (cheese pies)",
                    "Ladenia (Greek pizza)",
                    "Pure volcanic island honey"
                ],
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

        "natural_beauty": {
            "intro": {
                "title": "Greece's Natural Paradise",
                "subtitle": "A biodiversity hotspot where ancient landscapes meet Mediterranean splendor",
                "description": "Greece is home to over 6,000 plant species—many found nowhere else on Earth. From alpine meadows to coastal wetlands, discover a land where nature thrives in harmony with millennia of human history."
            },
            "flora": {
                "title": "🌸 Flora & Vegetation",
                "highlights": [
                    {
                        "name": "Endemic Species",
                        "image": "endemic_orchids.jpg",
                        "description": "Over 1,700 endemic plant species thrive in Greece's diverse microclimates—from mountain orchids to coastal wildflowers.",
                        "locations": ["Mount Olympus", "Crete", "Peloponnese"]
                    },
                    {
                        "name": "Ancient Olive Groves",
                        "image": "ancient_olive_tree.jpg",
                        "description": "Some olive trees are over 2,000 years old, standing as living witnesses to Greek history and producing world-famous olive oil.",
                        "locations": ["Kalamata", "Crete", "Peloponnese"]
                    },
                    {
                        "name": "Mediterranean Forests",
                        "image": "mediterranean_pine_forest.jpg",
                        "description": "Pine, cypress, and oak forests blanket mountains and coastlines, providing habitat for countless species and natural cooling.",
                        "locations": ["Mount Parnitha", "Samaria Gorge", "Rhodes"]
                    },
                    {
                        "name": "Spring Wildflowers",
                        "image": "greek_wildflowers.jpg",
                        "description": "Each spring, hillsides burst into color with poppies, anemones, and cyclamen—a photographer's dream landscape.",
                        "locations": ["Naxos", "Zagori", "Peloponnese"]
                    }
                ]
            },
            "fauna": {
                "title": "🦅 Wildlife & Fauna",
                "highlights": [
                    {
                        "name": "Loggerhead Sea Turtles",
                        "image": "loggerhead_turtle.jpg",
                        "description": "Greece hosts major nesting sites for the endangered Caretta caretta. Watch these ancient mariners return to the beaches where they were born.",
                        "locations": ["Zakynthos", "Kefalonia", "Peloponnese"]
                    },
                    {
                        "name": "Mediterranean Monk Seal",
                        "image": "monk_seal.jpg",
                        "description": "One of the world's rarest mammals finds refuge in Greece's remote caves and islands—fewer than 700 remain globally.",
                        "locations": ["Alonissos Marine Park", "Cyclades"]
                    },
                    {
                        "name": "Birds of Prey",
                        "image": "golden_eagle.jpg",
                        "description": "Golden eagles, griffon vultures, and peregrine falcons soar above gorges and mountains—a paradise for birdwatchers.",
                        "locations": ["Dadia Forest", "Vikos Gorge", "Crete"]
                    },
                    {
                        "name": "Wild Goats & Mammals",
                        "image": "kri_kri_goat.jpg",
                        "description": "The rare Cretan wild goat (Kri-kri) roams mountain peaks alongside brown bears, wolves, and wild boar in northern forests.",
                        "locations": ["Samaria Gorge (Crete)", "Pindus Mountains", "Rodopi Range"]
                    }
                ]
            },
            "landscapes": {
                "title": "🏞️ Iconic Landscapes",
                "features": [
                    {
                        "name": "Gorges & Canyons",
                        "description": "Samaria Gorge and Vikos Gorge—Europe's deepest—offer dramatic hiking through towering limestone walls.",
                        "icon": "⛰️"
                    },
                    {
                        "name": "Volcanic Islands",
                        "description": "Santorini's caldera and Milos' moon-white cliffs showcase volcanic power and otherworldly beauty.",
                        "icon": "🌋"
                    },
                    {
                        "name": "Crystal Waters",
                        "description": "Over 13,000 km of coastline with turquoise bays, hidden coves, and pristine beaches—some of Europe's cleanest waters.",
                        "icon": "💎"
                    },
                    {
                        "name": "Mountain Peaks",
                        "description": "From snow-capped Olympus to the alpine beauty of Pindus, Greece's mountains offer year-round adventure.",
                        "icon": "🏔️"
                    }
                ]
            },
            "conservation_message": "Greece is committed to protecting its natural heritage through 10 national parks, marine reserves, and the National Reforestation Plan. Your visit supports sustainable tourism and conservation efforts."
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
    ],

    "travel_plans": [
        {
            "id": 1,
            "title": "History, Archaeology & Coast",
            "subtitle": "Peloponnese Cultural Journey",
            "duration": "7-10 days",
            "difficulty": "Easy",
            "overview": "A route designed for travelers who want to explore Greece's cultural foundations while enjoying coastal scenery and charming historical towns.",
            "destinations": [
                {
                    "name": "Athens",
                    "activities": ["Visit the Acropolis & Parthenon", "Archaeological museums", "Stay in Plaka or Monastiraki"],
                    "duration": "2-3 days"
                },
                {
                    "name": "Delphi & Olympia",
                    "activities": ["Road trip from Athens to Delphi", "Ancient sanctuary exploration", "Birthplace of Olympic Games"],
                    "duration": "2 days"
                },
                {
                    "name": "Nafplio & Voidokilia Beach",
                    "activities": ["Explore fortified town of Nafplio", "Relax at semicircle-shaped beach", "Coastal walks"],
                    "duration": "2-3 days"
                }
            ],
            "best_season": "Spring or Fall",
            "season_details": "Warm temperatures, clear skies, and minimal rainfall",
            "icon": "🏛️",
            "color": "#0066CC",
            "image_placeholder": "peloponnese_plan.jpg"
        },
        {
            "id": 2,
            "title": "Mountain Adventure",
            "subtitle": "Mount Olympus Expedition",
            "duration": "4-5 days",
            "difficulty": "Challenging",
            "overview": "An option for active travelers seeking a physical challenge in Greece's most iconic mountain landscape.",
            "destinations": [
                {
                    "name": "Litochoro",
                    "activities": ["Base town for expedition", "Gear preparation", "Local tavernas"],
                    "duration": "1 day"
                },
                {
                    "name": "Mount Olympus Ascent",
                    "activities": ["Classic route from Prionia", "Overnight at Spilios Agapitos Refuge", "Summit Skala & Skolio peaks"],
                    "duration": "2-3 days"
                }
            ],
            "best_season": "June to October",
            "season_details": "High-altitude areas can experience cold, fog, rain, and rapid weather changes",
            "special_note": "Mytikas Peak involves technical scrambling - recommended only for experienced climbers",
            "icon": "⛰️",
            "color": "#6B8E23",
            "image_placeholder": "olympus_expedition.jpg"
        },
        {
            "id": 3,
            "title": "Island Relaxation",
            "subtitle": "Island Hopping Paradise",
            "duration": "7-10 days",
            "difficulty": "Easy",
            "overview": "A peaceful, beach-oriented experience, perfect for ending a trip with relaxation and panoramic island landscapes.",
            "destinations": [
                {
                    "name": "Santorini",
                    "activities": ["Volcanic scenery & caldera views", "Sunsets in Oia", "Red Beach exploration"],
                    "duration": "3-4 days"
                },
                {
                    "name": "Naxos or Paros",
                    "activities": ["Plaka Beach (Naxos)", "Kolymbithres Beach (Paros)", "Quiet, less crowded islands"],
                    "duration": "3-4 days"
                }
            ],
            "best_season": "Spring or Fall",
            "season_details": "Warm and dry conditions ideal for swimming and sunbathing",
            "access": "Flights or ferries from Thessaloniki or Athens",
            "icon": "🏖️",
            "color": "#4A90E2",
            "image_placeholder": "island_hopping.jpg"
        },
        {
            "id": 4,
            "title": "Northern Greece Discovery",
            "subtitle": "Meteora, Ioánnina & Vikos Gorge",
            "duration": "5-7 days",
            "difficulty": "Moderate",
            "overview": "Visit Meteora's cliff-top monasteries, the lakeside city of Ioánnina, and the dramatic viewpoints of Vikos Gorge. A trip that combines nature, culture, and light hiking.",
            "destinations": [
                {
                    "name": "Meteora",
                    "activities": ["Visit 2-4 cliff-top monasteries", "Great Meteoron, Varlaam, Roussanou", "Stunning photography opportunities"],
                    "duration": "2 days",
                    "accommodation": "Kastraki/Kalambaka"
                },
                {
                    "name": "Ioánnina",
                    "activities": ["Walk around Lake Pamvótida", "Boat to Island of the Lake", "Explore Ioánnina Castle", "Try local dishes: Ioannina pie, lake fish"],
                    "duration": "2 days",
                    "accommodation": "Lakeside hotels"
                },
                {
                    "name": "Vikos Gorge",
                    "activities": ["Oxía Viewpoint", "Beloi Viewpoint", "Visit Zagori villages like Monodendri"],
                    "duration": "2 days",
                    "accommodation": "Zagori"
                }
            ],
            "best_season": "Spring (April-May) or Fall (October)",
            "season_details": "Perfect weather for hiking and sightseeing",
            "icon": "🏔️",
            "color": "#E63946",
            "image_placeholder": "northern_greece.jpg"
        }
    ],

    "safety_precautions": {
        "urban": "Beware of pickpocketing in crowded areas of Athens and on public transportation",
        "mountain": "Avoid technical routes without proper experience; never hike alone; check weather conditions and bring warm layers, rain jacket, and plenty of water",
        "natural": "Greece is seismically active and experiences forest fires during the dry season. Follow official guidance during emergencies",
        "road": "Some roads are narrow or in poor condition. Drive defensively and park in well-lit areas"
    },

    "money_info": {
    "currency": {
        "name": "Euro (€)",
        "symbol": "€",
        "code": "EUR",
        "intro": "Greece uses the Euro as its official currency. ATMs are widely available in cities and tourist areas, and credit cards are increasingly accepted. It's always wise to carry some cash for smaller establishments, markets, and remote areas."
    },
    "payment_methods": [
        {
            "category": "🚕 Taxis",
            "emoji": "🚕",
            "card": "Yes (since 1st of April 2024)",
            "card_note": "",
            "cash": "Yes"
        },
        {
            "category": "🏪 Convenience stores",
            "emoji": "🏪",
            "card": "Yes",
            "card_note": "",
            "cash": "Yes"
        },
        {
            "category": "🛒 Open-air markets",
            "emoji": "🛒",
            "card": "Yes (since 1st of April 2024)",
            "card_note": "",
            "cash": "Yes, often preferred"
        },
        {
            "category": "🚇 Public transport",
            "emoji": "🚇",
            "card": "Depends on transport (available in Athens by the end of 2024)",
            "card_note": "",
            "cash": "Yes"
        },
        {
            "category": "🚌 Regional/city buses",
            "emoji": "🚌",
            "card": "Sometimes (at the moment, in 33 cities and islands)",
            "card_note": "",
            "cash": "Yes"
        },
        {
            "category": "🍽️ Tavernas",
            "emoji": "🍽️",
            "card": "Depends on the location",
            "card_note": "",
            "cash": "Yes"
        },
        {
            "category": "🏖️ Beach chairs",
            "emoji": "🏖️",
            "card": "Sometimes",
            "card_note": "",
            "cash": "Yes, often preferred"
        },
        {
            "category": "⛴️ Ferry tickets",
            "emoji": "⛴️",
            "card": "Yes",
            "card_note": "",
            "cash": "Yes"
        }
    ],
    "tips": [
        "💳 Credit cards are widely accepted in hotels, restaurants, and shops in tourist areas",
        "💵 Always carry €20-50 in cash for small purchases, tips, and rural areas",
        "🏧 ATMs charge withdrawal fees; use bank ATMs for better rates",
        "🪙 Small coins are useful for public restrooms and street vendors",
        "💡 Contactless payments are becoming more common in major cities"
    ]
},

    # Añade esta sección a tu SITE_DATA en utils/data.py

    "urban_rural": {
        "hero": {
            "title": "🏠 Urban or Rural 🚜?",
            "subtitle": "",
            "description": "From the buzzing streets of Athens to the peaceful villages of the Peloponnese, Greece offers two distinct lifestyles. Which one suits you best?"
        },
        
        "key_stats": [
            {
                "icon": "🏛️",
                "value": "80%",
                "label": "of Greece's population lives in urban areas",
                "color": "primary"
            },
            {
                "icon": "🚨",
                "value": "1M+",
                "label": "passengers transported daily on Athens public transport",
                "color": "sea"
            },
            {
                "icon": "🍃",
                "value": "5%",
                "label": "annual growth in rural tourism (Crete, Peloponnese)",
                "color": "olive"
            },
            {
                "icon": "🚜",
                "value": "25%",
                "label": "of Greece's workforce in agriculture (rural areas)",
                "color": "accent"
            }
        ],
        
        "comparison": {
            "urban": {
                "title": "Urban Communities",
                "emoji": "🏙️",
                "tagline": "Modern, Connected and Dynamic.",
                "image": "athens_city_life.jpg",
                "advantages": [
                    {
                        "icon": "🏥",
                        "title": "Better Healthcare",
                        "description": "Easy access to hospitals and specialists, especially in Athens and Thessaloniki"
                    },
                    {
                        "icon": "💼",
                        "title": "More Job Opportunities",
                        "description": "Tourism, shipping, technology, and public services concentrated in cities"
                    },
                    {
                        "icon": "🚇",
                        "title": "Excellent Transport",
                        "description": "Metro, buses, and trams make daily travel faster and easier"
                    },
                    {
                        "icon": "🎓",
                        "title": "Education & Culture",
                        "description": "Universities, museums, concerts, and vibrant nightlife"
                    }
                ],
                "disadvantages": [
                    {
                        "icon": "💰",
                        "title": "High Living Costs",
                        "description": "Rent and daily expenses much higher, especially in Athens"
                    },
                    {
                        "icon": "🚗",
                        "title": "Traffic & Pollution",
                        "description": "28 µg/m³ PM10 concentration (above EU's 20 µg/m³ limit)"
                    },
                    {
                        "icon": "👥",
                        "title": "Crowded Environments",
                        "description": "High population density with tourists year-round"
                    },
                    {
                        "icon": "🌳",
                        "title": "Less Nature",
                        "description": "Limited green spaces compared to rural areas"
                    }
                ],
                "characteristics": [
                ]
            },
            "rural": {
                "title": "Rural Communities",
                "emoji": "🏕️",
                "tagline": "Peaceful, Traditional and Authentic.",
                "image": "greek_village_life.jpg",
                "advantages": [
                    {
                        "icon": "🌾",
                        "title": "Calmer Lifestyle",
                        "description": "Less traffic and noise, peaceful daily rhythm"
                    },
                    {
                        "icon": "🏞️",
                        "title": "Cleaner Air & Nature",
                        "description": "Beautiful landscapes with beaches, mountains, and olive fields"
                    },
                    {
                        "icon": "🤝",
                        "title": "Strong Community",
                        "description": "People know each other and help their neighbors"
                    },
                    {
                        "icon": "💵",
                        "title": "Lower Living Costs",
                        "description": "Cheaper housing and daily expenses than urban centers"
                    }
                ],
                "disadvantages": [
                    {
                        "icon": "🏥",
                        "title": "Limited Healthcare",
                        "description": "Many villages have only one doctor or small health centers"
                    },
                    {
                        "icon": "📉",
                        "title": "Fewer Jobs",
                        "description": "Mainly agriculture or seasonal tourism"
                    },
                    {
                        "icon": "🚌",
                        "title": "Weak Transport",
                        "description": "Fewer buses and long distances between services"
                    },
                    {
                        "icon": "👨‍🎓",
                        "title": "Youth Migration",
                        "description": "Young people move to cities for education and work"
                    }
                ],
                "characteristics": [

                ]
            }
        },
        
        "similarities": {
            "title": "What They Have in Common",
            "description": "Despite their differences, urban and rural communities in Greece are deeply interconnected.",
            "points": [
                {
                    "icon": "🤝",
                    "text": "Both contribute to Greece's economy and culture"
                },
                {
                    "icon": "🏫",
                    "text": "Schools and healthcare exist (with different access levels)"
                },
                {
                    "icon": "🇬🇷",
                    "text": "Strong sense of Greek identity and traditions"
                },
                {
                    "icon": "🔄",
                    "text": "They depend on each other for resources and services"
                },
                {
                    "icon": "📱",
                    "text": "Technology present at different levels"
                }
            ]
        },
        
        "decision_guide": {
            "title": "Which Lifestyle Suits You?",
            "subtitle": "Answer these questions to discover your ideal Greek experience",
            "scenarios": [
                {
                    "question": "What's your ideal pace of life?",
                    "urban": "Fast-paced, always something happening",
                    "rural": "Slow and peaceful, time to breathe"
                },
                {
                    "question": "How important is career opportunity?",
                    "urban": "Essential - I need diverse job options",
                    "rural": "Flexible - I can work remotely or seasonally"
                },
                {
                    "question": "What about healthcare access?",
                    "urban": "Must have specialists nearby",
                    "rural": "Basic care is sufficient for me"
                },
                {
                    "question": "Your ideal weekend activity?",
                    "urban": "Museums, concerts, restaurants, nightlife",
                    "rural": "Hiking, beach walks, village festivals"
                },
                {
                    "question": "How do you feel about crowds?",
                    "urban": "I enjoy the energy of city life",
                    "rural": "I prefer knowing my neighbors"
                }
            ]
        }
    }


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