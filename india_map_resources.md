# India Map SVG Resources and Information

## Created SVG Map
**File:** `india_map_states.svg`

### Features:
- All 28 States included
- All 8 Union Territories included (post-2019 reorganization)
- Interactive hover effects (states turn blue, UTs turn orange)
- Clean, professional styling
- Labels for all regions
- Legend included
- Scalable vector graphics (800x1000 viewBox)

### States (28):
1. Andhra Pradesh
2. Arunachal Pradesh
3. Assam
4. Bihar
5. Chhattisgarh
6. Goa
7. Gujarat
8. Haryana
9. Himachal Pradesh
10. Jharkhand
11. Karnataka
12. Kerala
13. Madhya Pradesh
14. Maharashtra
15. Manipur
16. Meghalaya
17. Mizoram
18. Nagaland
19. Odisha
20. Punjab
21. Rajasthan
22. Sikkim
23. Tamil Nadu
24. Telangana
25. Tripura
26. Uttar Pradesh
27. Uttarakhand
28. West Bengal

### Union Territories (8):
1. Andaman and Nicobar Islands
2. Chandigarh
3. Dadra and Nagar Haveli and Daman and Diu
4. Delhi (National Capital Territory)
5. Jammu and Kashmir
6. Ladakh
7. Lakshadweep
8. Puducherry

## Alternative Sources for High-Quality India Maps

### 1. Wikimedia Commons
**URL:** https://commons.wikimedia.org/wiki/Category:SVG_maps_of_India
- Search for: "India states SVG"
- Look for files like "India_states_and_union_territories_map.svg"
- All files are public domain or Creative Commons licensed

### 2. GitHub Repositories
Popular repositories with India map data:

#### a) DataMeet India Maps
**URL:** https://github.com/datameet/maps
- Contains GeoJSON, TopoJSON, and SVG formats
- Highly accurate boundaries
- Regularly updated
- Open data commons license

#### b) India GeoJSON
**URL:** https://github.com/Subhash9325/GeoJson-Data-of-Indian-States
- State-wise GeoJSON files
- Can be converted to SVG using tools

#### c) Indian States and Districts
**URL:** https://github.com/indiapolisdata/india-states-districts-gis
- Comprehensive geographic data
- Multiple formats available

### 3. Government Open Data Portal
**URL:** https://data.gov.in
- Search for: "India boundary map" or "state boundaries"
- Official government data
- May require format conversion

### 4. Natural Earth Data
**URL:** https://www.naturalearthdata.com
- Path: Downloads > Cultural > Admin 1 - States, Provinces
- Free vector and raster map data
- Shapefile format (convertible to SVG)

### 5. OpenStreetMap
**URL:** https://www.openstreetmap.org
- Export India region data
- Use tools like QGIS to extract and convert to SVG
- Most up-to-date boundaries

## Converting GeoJSON/TopoJSON to SVG

### Online Tools:
1. **Mapshaper** (https://mapshaper.org)
   - Upload GeoJSON/TopoJSON
   - Simplify if needed
   - Export as SVG

2. **geojson.io** (http://geojson.io)
   - View and edit GeoJSON
   - Limited SVG export

### Command Line Tools:
```bash
# Using D3.js with Node.js
npm install -g d3-geo-projection topojson

# Convert TopoJSON to SVG
geo2svg -w 960 -h 1200 < india.json > india.svg

# Using GDAL/OGR
ogr2ogr -f "SVG" india.svg india.geojson
```

### Python Script:
```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Read GeoJSON
gdf = gpd.read_file('india_states.geojson')

# Plot and save as SVG
fig, ax = plt.subplots(figsize=(10, 12))
gdf.plot(ax=ax, edgecolor='black', facecolor='lightblue')
plt.savefig('india_map.svg', format='svg')
```

## Customization Tips

### Color Schemes:
- Use different colors for different regions (North, South, East, West, Central, Northeast)
- Color code by population, GDP, or other metrics
- Add gradients for visual appeal

### Interactive Features (with JavaScript):
```javascript
// Add click handlers
document.querySelectorAll('.state, .ut').forEach(element => {
  element.addEventListener('click', function() {
    const id = this.id;
    alert('Clicked: ' + id);
  });
});
```

### Responsive Design:
```css
svg {
  width: 100%;
  height: auto;
  max-width: 800px;
}
```

## Usage in Web Projects

### HTML:
```html
<!-- Inline SVG -->
<div class="map-container">
  <!-- Paste SVG code here -->
</div>

<!-- External SVG -->
<object data="india_map_states.svg" type="image/svg+xml"></object>

<!-- Img tag (loses interactivity) -->
<img src="india_map_states.svg" alt="India Map">
```

### CSS Styling:
```css
.map-container {
  max-width: 800px;
  margin: 0 auto;
}

.state:hover, .ut:hover {
  opacity: 0.7;
}
```

## Important Notes

1. **Post-2019 Reorganization:**
   - Jammu & Kashmir reorganized into J&K (UT) and Ladakh (UT)
   - Dadra and Nagar Haveli merged with Daman and Diu

2. **Border Disputes:**
   - Some international boundaries are disputed
   - Different maps may show varying boundaries
   - Use official government sources for legal/official purposes

3. **Accuracy:**
   - The provided SVG is stylized for web use
   - For highly accurate cartographic work, use GIS data from official sources

4. **License:**
   - The created SVG is provided for your use
   - When using third-party sources, always check licenses
   - Attribute sources when required

## Recommended Next Steps

1. Test the provided SVG in your browser
2. Customize colors and styling to match your project
3. Add tooltips or click handlers for interactivity
4. For production use, consider using DataMeet or government sources for accuracy
5. Validate boundaries against official survey maps if accuracy is critical
