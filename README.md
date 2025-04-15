
# JetPhotos API

A simple Flask API to search and extract aircraft images and metadata from JetPhotos using HTML scraping.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server:

```bash
python app.py
```

3. Query the API:

Example:
```
http://localhost:5000/search?reg=N12345&type=Boeing+737&airline=Delta&serial=123456
```
