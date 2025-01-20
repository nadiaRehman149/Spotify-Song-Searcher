# Spotify Song Previewer

This Python console app uses the Spotify Web API to search for 5 songs with the user's input in the title name. Then it would play a short preview of a selected song and save the search results to a file.

## Libraries to Install
See requirements.txt

## Setting up the Spotify API Credentials
1. Visit [Spotify for Developers](https://developer.spotify.com/).
2. Create a new spotify account or log into your existing account. 
3. In the top right-hand corner, click profile>dashboard>create app 
4. Name the app and add a description as desired, then add a Redirect URI. I added http://localhost:8000/callback although this can be a placeholder as I am not using a web server for authentication flow.
5. Select 'WebAPI', accept the Terms of Service and save.
6. In the top right-hand corner click 'settings' and your `Client ID` should be visible. Underneath, also click on `View Client Secret`. 
7. Using your `Client ID` and `Secret`, insert these characters into the corresponding variables (replacing the *******) and run. 

## Usage

1. Ensure all necessary libraries are installed (see requirements.txt)
2. Run the main script:

    ```sh
    python assignment-2-python.py
    ```

3. Follow the prompts in the terminal to interact. Results will also be saved in the tracks.txt file. Make sure your volume is on to hear the songs!!!

