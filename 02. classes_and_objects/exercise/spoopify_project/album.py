from song import Song


class Album:

    def __init__(self, name: str, *args: Song):
        self.name = name
        self.published = False
        self.songs = list(args)

    def add_song(self, song: Song):
        if song in self.songs:
            return f"Song is already in the album."

        if self.published:
            return f"Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        try:
            current_song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(current_song)

        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True

            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        output = [f"Album {self.name}"]
        [output.append(f'== {s.get_info()}') for s in self.songs]

        return '\n'.join(output)
