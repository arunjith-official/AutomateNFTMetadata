import json
import random

# Define your artworks
artworks = [
    {"name": "Artwork 1", "description": "Description 1", "image": "image1.jpg"},
    {"name": "Artwork 2", "description": "Description 2", "image": "image2.jpg"},
    # Add more artworks here
]

# Number of editions you want to create for each artwork
editions_per_artwork = 100

# Create a list to hold the shuffled metadata
shuffled_metadata = []

for artwork in artworks:
    for edition in range(1, editions_per_artwork + 1):
        artwork_metadata = artwork.copy()
        artwork_metadata["attributes"] = {
            "edition": f"{edition}",
            "artist": "Artist Name",
            "creation_date": "Creation Date"
        }
        shuffled_metadata.append(artwork_metadata)

# Shuffle the metadata list randomly
random.shuffle(shuffled_metadata)

# Write the shuffled metadata to individual JSON files with just numbers in the filename
for index, metadata in enumerate(shuffled_metadata):
    with open(f"{index + 1}", "w") as metadata_file:
        json.dump(metadata, metadata_file, indent=2)
