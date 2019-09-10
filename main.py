import os

def write_songs_to_file(path, song_list):
	with open(path, "w") as f:
		for i in song_list:
			f.write('https://osu.ppy.sh/beatmapsets/' + i + '/download' + '\n')

def get_song_names(path):
	song_codes = []
	for song_code in os.listdir(path):
		try:
			int(song_code.split(" ")[0])
			song_codes.append(str(song_code.split(" ")[0]))
		except Exception as e:
			pass

	return song_codes

def move_output_file_to_folder(song_path,destined_path):
	os.rename(song_path,destined_path)

def main():
	songs = get_song_names(r'D:\Progam Files\osu!\Songs')
	write_songs_to_file('songs.txt',songs)
	move_output_file_to_folder('songs.txt', r'C:\Users\Talha\Google Drive\Notes\songs.txt')

if __name__ == '__main__':
	main()