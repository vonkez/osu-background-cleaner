import os, shutil


def check_bg(bg):
    a = os.path.splitext(bg)
    if bg is "":
        print("Something is wrong please enter exact location of background"
              " i.e: C:\\Users\\Username\Desktop\\background.jpg")
        return True
    if a[1].lower() == ".jpeg" or a[1].lower() == ".jpg" or a[1].lower() == ".png":
        return False
    else:
        print("Only use '.jpg', '.jpeg' or '.png'")
        return True


def get_bg():
    bg = input("Enter new background location: ")
    while check_bg(bg):
        bg = input("Enter new background location: ")
    return bg


def get_osu():
    o_dir = input("Enter osu directory: ")
    if o_dir is "":
        o_dir = os.getenv("LOCALAPPDATA") + "\osu!\\"
        print("Using default location: " + o_dir)
        return o_dir
    else:
        return o_dir


def clean_one(song_dir, bg):
    c = 0
    files = (os.listdir(song_dir))
    for f in files:
        a = os.path.splitext(song_dir + "\\" + f)[1].lower()
        if a == ".jpg" or a == ".png" or a == ".jpeg":
            shutil.copy2(bg, song_dir + "\\" + f)
            print(song_dir + "\\" + f)
            c += 1
    return c


def clean_all(osu_dir, bg):
    print("Do you want to continue?\nThis will replace all the images in Songs folder PERMANENTLY! (y/n)")
    if input() == "y":
        pass
    else:
        return 0
    counter = 0
    song_list = os.listdir(osu_dir + "\Songs\\")
    for song in song_list:
        print("Cleaning " + song)
        counter += clean_one(osu_dir + "\Songs\\" + song, bg)
    print(counter, "image changed.")


if __name__ == "__main__":
    clean_all(get_osu(), get_bg())
