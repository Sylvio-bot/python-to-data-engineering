def main():
    song = "RAH RAH AH AH AH ROM MAH RO MAH MAH"
    print(f"This is the first way to get the frequence {generate_word_dict(song)}")
    print(f"Theis is the other method {generate_word_dict_second(song)}")

def generate_word_dict(song:str) -> dict:
    song_words = song.lower()
    words_list = song_words.split()
    word_dict = dict()
    for w in words_list:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1
    return word_dict

def generate_word_dict_second(song:str) -> dict:
    song_words = song.lower()
    words_list = song_words.split()
    word_dict = {}
    for w in words_list:
        word_dict[w] = word_dict.get(w,0) + 1
    return word_dict

if __name__ == "__main__":
    main()
