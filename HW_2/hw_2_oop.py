# базовый класс MediaFile,
# который будет содержать общие данные о файле: имя, размер, дата создания, владелец и т.д.
class MediaFile:
    def __init__(self, name, size, owner, date):
        self.name = name
        self.size = size
        self.owner = owner
        self.date = date


# подкласс AudioFile, наследуется от MediaFile
# и содержит специфические для аудиофайлов мета-данные.
class AudioFile(MediaFile):
    def __init__(self, name, size, owner, date, bitrate, channels):
        super().__init__(name, size, owner, date)
        self.bitrate = bitrate
        self.channels = channels


# подкласс VideoFile, наследуется от MediaFile
# и содержит специфические для видеофайлов мета-данные.
class VideoFile(MediaFile):
    def __init__(self, name, size, owner, date, resolution, frame_rate):
        super().__init__(name, size, owner, date)
        self.resolution = resolution
        self.frame_rate = frame_rate


# подкласс PhotoFile, наследуется от MediaFile
# и содержит специфические для фотофайлов мета-данные.

class PhotoFile(MediaFile):
    def __init__(self, name, size, owner, date, resolution, format):
        super().__init__(name, size, owner, date)
        self.resolution = resolution
        self.format = format


def create_file(file_type, file_name, file_size, file_owner, file_date):
    if file_type == 'audio':
        file = AudioFile(file_name, file_size, file_owner, file_date)
    elif file_type == 'video':
        file = VideoFile(file_name, file_size, file_owner, file_date)
    elif file_type == 'photo':
        file = PhotoFile(file_name, file_size, file_owner, file_date)
    else:
        raise ValueError('Неверный тип файла')
    return file


# Для обновления файла
def update_file(file, new_file_name, new_file_size, new_file_owner, new_file_date):
    file.name = new_file_name
    file.size = new_file_size
    file.owner = new_file_owner
    file.date = new_file_date


# Для удаления файла
def delete_file(file):
    file.delete()


# Для проведения других действий над файлом, например, конвертации или извлечения фич
def convert_file(file, new_file_type):
    if new_file_type == 'audio':
        file.convert_to_audio()
    elif new_file_type == 'video':
        file.convert_to_video()
    elif new_file_type == 'photo':
        file.convert_to_photo()
    else:
        raise ValueError('Неверный тип файла')


def extract_features(file):
    file.extract_audio_features()
    file.extract_video_features()
    file.extract_photo_features()
