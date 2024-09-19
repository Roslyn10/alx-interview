#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if the movie ID was provided
if (!movieId) {
    console.error('Please provide a movie ID as the first argument.');
    process.exit(1);
}

// Star Wars API URL for the movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to get the movie details
request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
        console.error('Error fetching movie data:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error('Failed to retrieve movie data. Status code:', response.statusCode);
        return;
    }

    // Extract the characters list from the movie data
    const characterUrls = body.characters;

    // Iterate over the character URLs and print each character's name
    characterUrls.forEach((url) => {
        request(url, { json: true }, (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error fetching character data:', charError);
                return;
            }

            if (charResponse.statusCode === 200) {
                console.log(charBody.name);
            } else {
                console.error('Failed to retrieve character data. Status code:', charResponse.statusCode);
            }
        });
    });
});

