def get_most_appeared_artist(data):
    lines = data.split("\n")
    items = []
    artists = []
    for element in lines:
        items.append(element)
        current_artist = str(element).split(";")[1]
        artists.append(current_artist)
    from collections import Counter
    occurence_count = Counter(artists)
    return(occurence_count.most_common(1)[0][0])


def get_count_songs(data):
    lines = data.split("\n")
    items = []
    for element in lines:
        items.append(element)
    return(len(items))


def get_most_long_song_by_name(data):
    lines = data.split("\n")
    items = []
    max_len = 0
    max_song = ""
    for element in lines:
        items.append(element)
        
        current_song = str(element).split(";")[0]
        time_values = str(element).split(";")[2].split(":")
        current_len = 60*int(time_values[0]) + int(time_values[1])
        if(current_len>max_len):
            max_len = current_len
            max_song = current_song

    return(max_song)


def my_mp3_playlist(data):
    f = open(r"C:\Python\play_list.txt", "r")
    data = f.read()
    res = ()
    res += (get_most_long_song_by_name(data),)
    res += (get_count_songs(data),)
    res += (get_most_appeared_artist(data),)
    f.close()
    return res


print(my_mp3_playlist(r"c:\Python\play_list.txt"))
#("Tudo Bom", 5, "The black Eyed Peas")
