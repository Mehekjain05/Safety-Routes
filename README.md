Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/womens-safety-crime-map.git
cd womens-safety-crime-map
2. Install Requirements
Ensure you have Python 3.6 or higher. Install project dependencies using:

bash
Copy code
pip install -r requirements.txt
3. Add API Key
Replace YOUR_GOOGLE_MAPS_API_KEY with your actual Google Maps API key in:

The HTML file for the frontend <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&callback=initMap" async defer></script>
Flask app code for the /get_route endpoint.



Start the Flask Server

bash
Copy code
python app.py
Open the HTML Frontend

Navigate to localhost:5000 in your browser.
Enter Start and Destination Locations

Enter your start and end locations, then click Find Route. The map will display the route along with any crime hotspots nearby.