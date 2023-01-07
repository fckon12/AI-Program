import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from binance.client import Client

# Replace YOUR_API_KEY and YOUR_API_SECRET with your own API key and secret
client = Client("XvS5nJijuJigeeAe2PpQdDSJUUHNHYFM2QwzjpOfSFO6VrFGacnaNIN7CkTKKuG5", "lyGV7M2btsVtUxiRwZBplWNIQQo2gY9I76bO0OY585cS0uAvXTvec9vGUr9uUJTW", {"verify": False, "timeout": 20})

# Set the API endpoint to the Binance sandbox
client.API_URL = "https://testnet.binance.com"

# You are now logged in to the Binance sandbox and can make API requests
