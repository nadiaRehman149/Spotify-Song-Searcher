import requests  # library for making HTTP requests
import spotipy  # library for interacting with Spotify Web API
from spotipy.oauth2 import SpotifyClientCredentials  # uses your client ID and secret to request access token from spotify and refreshes it when it expires for authentication
import pygame  # library for playing audio
import io  # used to handle audio data from spotify in memory instead of on disk


# function for a specific user to access the API
def get_spotify_user():
    client_id = '****************'  # Spotify client ID
    client_secret = '*****************'  # Spotify client secret
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                          client_secret=client_secret)  # handles the authentication process
    user = spotipy.Spotify(
        client_credentials_manager=client_credentials_manager)  # instance that will be used to make requests to the spotify API
    return user


# Function to search for songs, max 5
def search_tracks(user, query, limit=5):
    results = user.search(q=query, limit=limit, type='track')  # performs the search request
    return results['tracks']['items']  # returns the list of songs found


# Function to play the short Spotify preview of the song
def play_preview(url):
    pygame.mixer.init()  # initialises the Pygame mixer
    response = requests.get(url)  # get request that gets the audio from the URL
    audio_file = io.BytesIO(response.content)  # stores the data in memory
    pygame.mixer.music.load(audio_file)  # loads the song data into the Pygame mixer
    pygame.mixer.music.play()  # playing of the song


# Function to stop the preview playing
def stop_song():
    pygame.mixer.music.stop()


# Function to save the found songs to a file
def save_results_to_file(tracks, filename="tracks.txt"):
    with open(filename, "w") as file:
        for track in tracks:
            track_name = (track['name'][:20] + '...') if len(track['name']) > 20 else track['name'] # shortening if name becomes too long
            file.write(f"'{track_name}' by {track['artists'][0]['name']}\n")


def searching_and_displaying_song(user, query):
    print(f"Searching for a song with '{query}' in the title...")
    tracks = search_tracks(user, query)  # searching for the song
    if tracks:  # if songs are found
        print(f"Found {len(tracks)} tracks for '{query}':")
        i = 1
        for track in tracks: # for loop that prints the songs found
            track_name = (track['name'][:20] + '...') if len(track['name']) > 20 else track['name']
            print(f"{i}. '{track_name}' by {track['artists'][0]['name']}")
            i += 1
        save_results_to_file(tracks)  # Save the results to a file
    else:
        print(f"No tracks found for '{query}'.")
    return tracks


# Function to get the user's choice of song to play
def get_user_choice(tracks):
    valid_choices = [str(i) for i in range(1, len(tracks) + 1)] + ['stop', 'new']
    choice = input(
        "\nEnter the number corresponding to the song you want to play. Type 'stop' to stop playing or type 'new' to try a new word: ")
    while choice not in valid_choices:
        print("Invalid input. Please enter a number, 'stop', or 'new'.")
        choice = input(
            "\nEnter the number corresponding to the song you want to play. Type 'stop' to stop playing or type 'new' to try a new word: ")
    return choice


# Function to play the selected song
def play_selected_track(track):
    preview_url = track['preview_url']
    if preview_url:
        # Truncate long track names for readability
        track_name = (track['name'][:20] + '...') if len(track['name']) > 20 else track['name'] # shortening long names
        print(f"Playing preview for '{track_name}' by {track['artists'][0]['name']}...")
        play_preview(preview_url)
    else:
        print(f"Preview not available for '{track['name']}' by {track['artists'][0]['name']}.")


# Function to handle user input and song playback
def main():
    user = get_spotify_user()
    keep_searching = True #boolean to control execution

    while keep_searching:
        query = input("Enter a random word to search for songs: ")
        tracks = searching_and_displaying_song(user, query)

        if tracks:
            continue_playing = True  # controlling the playback
            while continue_playing:
                choice = get_user_choice(tracks)
                if choice == 'stop':
                    stop_song()
                    continue_playing = False  # updating bool to stop loop
                elif choice == 'new':
                    stop_song()
                    continue_playing = False  # updating bool to stop loop
                    keep_searching = True  # continue to search for new songs
                else:
                    choice_index = int(choice) - 1
                    play_selected_track(tracks[choice_index])
        else:
            keep_searching = False  # no tracks were found so exit the loop
main()