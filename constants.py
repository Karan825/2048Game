# Game Settings
SCREEN_SIZE = 500  # Increased for better visibility and aesthetics
GRID_LEN = 4
GRID_PADDING = 15  # Slightly increased for better spacing

# Colors
BACKGROUND_COLOR = "#F7E6D9"  # Light, warm cream for the overall background
BACKGROUND_COLOR_CELL_EMPTY = "#D0C0A1"  # Light beige with a hint of warmth for empty cells

# Tile Background Colors (warm gradient)
BACKGROUND_COLOR_DICT = {
    "2": "#FBE3C7",       # Soft peach for the smallest tile
    "4": "#FAD08C",       # Light golden yellow for the next smallest
    "8": "#F6A477",       # Warm apricot-orange
    "16": "#F4895A",      # Warm orange with a bit more intensity
    "32": "#F56D38",      # Deep orange, still warm but more saturated
    "64": "#F64F2F",      # Vibrant orange-red, fiery warmth
    "128": "#F9D36E",     # Soft, golden yellow
    "256": "#F9C21D",     # Rich, deep gold
    "512": "#F8A700",     # Burnished gold
    "1024": "#F7D800",    # Bright golden yellow
    "2048": "#F3A400",    # Radiant, fiery gold
    "4096": "#C96741",    # Elegant, darker brownish orange for larger tiles
    "8192": "#C44D2C",    # Deeper burnt orange for higher tiles
    "16384": "#9C3F1F",   # Darker brownish red for very high values
    "32768": "#8C2F12",   # Rich, dark brick red
    "65536": "#701D0C",   # Deep, dark reddish brown
}

# Tile Text Colors (high contrast for readability)
CELL_COLOR_DICT = {
    "2": "#6C4F3D",       # Soft, dark brown for small values
    "4": "#6C4F3D",       # Consistent dark brown for the next small value
    "8": "#F7F1E1",       # Light cream for contrast and readability
    "16": "#F7F1E1",      # Soft cream for contrast
    "32": "#F7F1E1",      # Soft cream for contrast
    "64": "#F7F1E1",      # Soft cream for contrast
    "128": "#F7F1E1",     # Soft cream for contrast
    "256": "#F7F1E1",     # Soft cream for contrast
    "512": "#F7F1E1",     # Soft cream for contrast
    "1024": "#F7F1E1",    # Soft cream for contrast
    "2048": "#F7F1E1",    # Soft cream for contrast
    "4096": "#F7F1E1",    # Soft cream for contrast
    "8192": "#F7F1E1",    # Soft cream for contrast
    "16384": "#F7F1E1",   # Soft cream for contrast
    "32768": "#F7F1E1",   # Soft cream for contrast
    "65536": "#F7F1E1",   # Soft cream for contrast
}

# Fonts
FONT = ("Verdana", 40, "bold")  # Large, bold font for easy readability
FONT_SMALL = ("Verdana", 20, "bold")  # Additional font size for smaller elements

# Key Bindings
KEY_UP = 'w'
KEY_DOWN = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'
