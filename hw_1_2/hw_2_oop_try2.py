class MediaFile:
    def __init__(self, name, size, date, owner):
        self.name = name
        self.size = size
        self.created_at = date
        self.owner = owner

    def save(self):
        # сохранение файла на диск
        pass

    def update(self):
        # обновление файла на диске
        pass

    def delete(self):
        # удаление файла с диска
        pass


# подкласс AudioFile, наследуется от MediaFile
# и содержит специфические для аудиофайлов мета-данные.
class AudioFile(MediaFile):
    def __init__(self, name, size, date, owner, bitrate, channels):
        super().__init__(name, size, date, owner)
        self.bitrate = bitrate
        self.channels = channels


# подкласс VideoFile, наследуется от MediaFile
# и содержит специфические для видеофайлов мета-данные.
class VideoFile(MediaFile):
    def __init__(self, name, size, date, owner, resolution, frame_rate):
        super().__init__(name, size, date, owner)
        self.resolution = resolution
        self.frame_rate = frame_rate


# подкласс PhotoFile, наследуется от MediaFile
# и содержит специфические для фотофайлов мета-данные.
class PhotoFile(MediaFile):
    def __init__(self, name, size, owner, date, resolution, geolocation):
        super().__init__(name, size, owner, date)
        self.resolution = resolution
        self.geolocation = geolocation


# работа с облаком
# предположим, что у нас есть функции upload_file, update_file и delete_file
# которые могут работать с облаком
def upload_file(file, storage_url, access_key, secret_key):
    # код для загрузки файла в облачное хранилище
    pass


def update_file(file, storage_url, access_key, secret_key):
    # код для обновления файла в облачном хранилище
    pass


def delete_file(file, storage_url, access_key, secret_key):
    # код для удаления файла из облачного хранилища
    pass


class CloudStorage:
    def __init__(self, storage_url, access_key, secret_key):
        self.storage_url = storage_url
        self.access_key = access_key
        self.secret_key = secret_key

    def save(self, file):
        # сохранение файла в облачном хранилище
        upload_file(file, self.storage_url, self.access_key, self.secret_key)

    def update(self, file):
        # обновление файла в облачном хранилище
        update_file(file, self.storage_url, self.access_key, self.secret_key)

    def delete(self, file):
        # удаление файла из облачного хранилища
        delete_file(file, self.storage_url, self.access_key, self.secret_key)
