from abc import ABCMeta, abstractmethod
from enum import Enum

from yolov5 import train, val, detect, export

"""
EfficientNet
YoloV5
"""


class EModelType(Enum):
    EfficientNet = 'EfficientNetTrainingService'
    YoloV5 = 'YoloV5TrainingService'


class TrainingService(metaclass=ABCMeta):
    @abstractmethod
    def train(self):
        pass


class YoloV5TrainingService(TrainingService):
    def train(self):
        print('YoloV5TrainingService ')
        train.run(imgsz=640, data='coco128.yaml')
        val.run(imgsz=640, data='coco128.yaml', weights='yolov5s.pt')
        detect.run(imgsz=640)
        export.run(imgsz=640, weights='yolov5s.pt')


class EfficientNetTrainingService(TrainingService):
    def train(self):
        print('EfficientNetTrainingService ')


class TrainingFactory:
    @staticmethod
    def new_instance(model_type: EModelType):
        return eval(model_type.value)()


if __name__ == '__main__':
    x = 'EfficientNet'

    model_type = None
    for e in EModelType:
        if e.name.lower().__contains__(x.lower()):
            model_type = e

    if model_type is None:
        raise Exception('service not found.')

    service = TrainingFactory.new_instance(model_type=model_type)
    service.train()
