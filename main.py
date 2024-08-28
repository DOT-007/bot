import subprocess

def get_spotify_link():
    # Prompt the user for a Spotify link
    return input("Enter the Spotify link (track, album, or playlist): ")

def download_song(spotify_link):
    try:
        # Run spotdl as a subprocess
        subprocess.run(["spotdl", spotify_link], check=True)
        print("Song downloaded successfully!")
    except subprocess.CalledProcessError:
        print("Error downloading the song. Please check the link and try again.")

if __name__ == "__main__":
    spotify_link = get_spotify_link()
    download_song(spotify_link)
