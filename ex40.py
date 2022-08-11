class Song(object):
    # 初始化对象，将lyrics的值赋值给self.lyrics的实例化对象。
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # 定义函数，传入实例化对象。
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(['happy birthday to you', "I don't want to sued", "so I'll stop right here"])
bulls_on_parade = Song(["they rally around the family", "with pockets full of shells"])

happy_bday.sing_me_a_song()
print('__________________')
bulls_on_parade.sing_me_a_song()
