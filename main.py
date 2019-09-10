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
	songs = get_song_names('enter the path of songs')
	write_songs_to_file('enter the output name with txt extension',songs)
	move_output_file_to_folder('same thing above', r'enter google drive folder path')

if __name__ == '__main__':
	main()
