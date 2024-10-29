Here's a more polished version of your README for GitHub:

---

# Women’s Safety Crime Map with Routes

This project provides a route-planning tool that displays a route from a starting location to a destination, highlighting potential crime hotspots along the way to enhance safety. Crime data is visualized in real-time on Google Maps, helping users avoid high-risk areas based on recent incidents.

## Features
- **User-Friendly Interface**: Easily input start and end locations.
- **Real-Time Route Calculation**: Powered by the Google Maps Directions API.
- **Crime Data Markers**: Displays high-risk areas along the route, categorized by risk levels.

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/womens-safety-crime-map.git
cd womens-safety-crime-map
```

### 2. Install Requirements
Ensure you have Python 3.6 or higher. Install the project dependencies using:
```bash
pip install -r requirements.txt
```

### 3. Add Your Google Maps API Key
Replace `YOUR_GOOGLE_MAPS_API_KEY` with your actual Google Maps API key in:
- The HTML file for the frontend:
  ```html
  <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&callback=initMap" async defer></script>
  ```
- The Flask app code for the `/get_route` endpoint.

### 4. Add Crime Data
Place your crime dataset in the `data` directory and name it `file.csv`. Ensure it includes the following columns:
  - `Lat`
  - `Long`
  - `HOUR`
  - `OCCURRED_ON_DATE`
  - `OFFENSE_DESCRIPTION`
  - `Risk_Category`

---

## Usage

1. **Start the Flask Server**
   ```bash
   python app.py
   ```

2. **Open the HTML Frontend**
   - Open your browser and navigate to `http://localhost:5000`.

3. **Enter Start and Destination Locations**
   - Input your start and end locations, then click **Find Route**. The map will display the route, highlighting any nearby crime hotspots with red markers.

---

## Project Structure

- **`app.py`**: Flask server with API endpoints for retrieving data and analyzing routes.
- **`data/file.csv`**: Dataset containing sample crime data.
- **`index.html`**: Frontend interface for map display and route calculations.

## API Endpoints

- **`/get_data`**: Fetches crime data based on risk category.
- **`/get_route`**: Calculates the route between the start and end locations.
- **`/get_crimes_along_route`**: Returns crime data along specified route points.

---

> **Note**: Keep your API key secure and avoid sharing it publicly.

---
