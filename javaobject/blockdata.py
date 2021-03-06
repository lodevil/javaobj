from .binary import BinReader, BinWriter
import six


class BlockDataReader(BinReader):

    class ReadError(Exception):
        pass

    def __init__(self, raw, objects):
        self.__raw = raw
        self.__objects = objects
        self.__next_obj = 0
        super(BlockDataReader, self).__init__(six.BytesIO(raw))

    def object(self):
        if self.__next_obj >= len(self.__objects):
            raise self.ReadError('EOF')
        i = self.__next_obj
        self.__next_obj += 1
        return self.__objects[i]


class BlockDataWriter(BinWriter):

    def __init__(self):
        self.raw = six.BytesIO()
        self.objects = []
        super(BlockDataWriter, self).__init__(self.raw)

    def object(self, obj):
        self.objects.append(obj)

    def tobytes(self):
        if six.PY3:
            return self.raw.getbuffer().tobytes()
        return self.raw.getvalue()
