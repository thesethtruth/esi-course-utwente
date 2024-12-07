import cairosvg
from PIL import Image

# First convert SVG to PNG
cairosvg.svg2png(url="wblogo.svg", write_to="WB-logo.png")

# Open both images
ut_logo = Image.open("UT-logo.png")
wb_logo = Image.open("WB-logo.png")

# Get dimensions
ut_width, ut_height = ut_logo.size
wb_width, wb_height = wb_logo.size

# Calculate new height for UT logo to maintain aspect ratio when resizing to WB width
new_ut_height = int((wb_width / ut_width) * ut_height)

# Resize UT logo to match WB width while maintaining aspect ratio
ut_logo_resized = ut_logo.resize((wb_width, new_ut_height), Image.Resampling.LANCZOS)

# Create a new blank image with WB width and combined height
new_height = new_ut_height + wb_height
combined = Image.new("RGBA", (wb_width, new_height), (255, 255, 255, 0))

# Paste resized UT logo at the top
combined.paste(ut_logo_resized, (0, 0))

# Paste WB logo below UT logo
combined.paste(wb_logo, (0, new_ut_height))

# Save the result
combined.save("logo.png")
