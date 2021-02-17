from io import FileIO, TextIOWrapper
from itertools import chain
import json

# Exception classes

class No_Lines_Rendered(Exception):
    def __init__(self, object) -> None:
        super().__init__(f"{object} has no lines rendered.")

''' Main class that contains all methods
and functions to process a text file'''

class TextProcessor:
    def __init__(self, target: FileIO) -> None:
        self.target: str = target

        self.container:  list = []
        self.images:  list = []
        self.links:  list = []
        self.videos:  list = []
        self.outcasts:  list = []

        self.video_types:  list = ['WEBM', 'MPG', 'MP2',
                                   'MPEG', 'MPE', 'MPV',
                                   'OGG', 'MP4', 'M4P',
                                   'M4V', 'AVI', 'WMV',
                                   'MOV', 'QT', 'FLV',
                                   'SWF', 'AVCHD']

        self.image_types:  list = ['JPEG', 'JPG',
                                   'PNG', 'GIF', 'TIFF',
                                   'PSD', 'PDF', 'EPS', 'AI']

    def __repr__(self) -> str:
        return f'< Processing: {len(self.container)} lines: {len(self.images)+len(self.videos)+len(self.links)+len(self.outcast)} scrapped >'

    def __enter__(self) -> type:
        self.file: TextIOWrapper = open(self.target, 'r', encoding="utf-8")
        return self

    def __exit__(self, type, value, traceback) -> bool:
        self.file.close()
        if traceback is not None:
            print(f"{type}, {value}, {traceback}")
        else:
            return True

    '''Raises an error on utilization of a `get` method before loading the file into a generator.'''

    def _affirm(self) -> None:
        if not self.container:
            raise No_Lines_Rendered(self)

    def _empty_db(self) -> bool:
        try:
            if self.videos:
                self.videos = []
            if self.links:
                self.links = []
            if self.images:
                self.images = []
            if self.outcast:
                self.outcast = []
        except:
            return False
        else:
            return True

    def render_lines(self, notation: str = '\n') -> type:
        try:
            self.file
        except AttributeError:
            self.file: TextIOWrapper = open(self.target, 'r', encoding="utf-8")
            print('[Please use a context manager for opening files more efficiently]')
        finally:
            container = (chain.from_iterable(line.split(notation)
                                             for line in self.file))
        self.container: chain = container
        return self

    def get_links(self, hint: str) -> list:
        self._affirm()
        links: list = []
        for line in self.container:
            if line.startswith(hint) and line.endswith('.com') and line not in links:
                links.append(line)
        self.links = links
        return None if not self.links else self.links

    def get_images(self, hint: str) -> list:
        self._affirm()
        links: list = []
        for line in self.container:
            status = True if True in [line.lower().endswith(
                f'.{type.lower()}') for type in self.image_types] else False
            if line.startswith(hint) and status and line not in links:
                links.append(line)
        self.images = links
        return self.images

    def get_videos(self, hint: str) -> list:
        self._affirm()
        links: list = []
        for line in self.container:
            status = True if True in [line.lower().endswith(
                f'.{type.lower()}') for type in self.video_types] else False
            if line.startswith(hint) and status and line not in links:
                links.append(line)
        self.videos = links
        return self.videos

    def get_outcast(self, hint: str) -> list:
        self._affirm()
        links: list = []
        for line in self.container:
            if line.startswith(hint) and not line.endswith('.mp4') and not line.endswith('.jpg') and not line.endswith('.png') and line not in links:
                links.append(line)
        self.outcasts = links
        return self.outcasts

    def fetch_kword_stat(self, kword: str) -> list:
        self._affirm()
        position: int = 0
        if type(kword) == list:
            result: list = [{}, 0]
            for word in kword:
                result[0][word] = []
            for word in self.container:
                for w in kword:
                    if word.lower() == w.lower():
                        result[1] += 1
                        result[0][w].append(position)
                    position += len(word)

        elif type(kword) == str:
            result: list = [[], 0]
            for word in self.container:
                if word.lower() == kword:
                    result[1] += 1
                    result[0].append(position)
                position += len(word)
        return result if result[1] > 0 else None

    def save(self, header: str, destination: FileIO) -> bool:
        new_dict: dict = {}
        new_dict[header] = {}
        composition: list = [self.videos,
                             self.images, self.links, self.outcasts]
        for data in [extracted for extracted in composition if extracted]:
            new_dict[header][data[4:]] = data
        self._empty_db()
        try:
            open(destination, 'r')
        except:
            open(destination, 'w')
        finally:
            with open(destination, 'r+') as f:
                json.dump(new_dict, f, indent=4)
            return True


'''
We can utilize a context manager to work better as
such:

with TextProcessor('top.txt') as f:
    f.render_lines()
    f.get_videos('https://youtube.com/')
    f.save('videos', 'testing.json')


Although it's still very possible to work without one as
such:

f = TextProcessor('top.txt')
f.render_lines()
f.get_videos('https://youtube.com/')
f.save('videos', 'testing.json')
'''
