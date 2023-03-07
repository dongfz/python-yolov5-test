if __name__ == '__main__':
    from yolov5 import train, val, detect, export
    from concurrent.futures import ThreadPoolExecutor

    executor = ThreadPoolExecutor(5)
    train.run(imgsz=640, data='C:/Users/dfz/PycharmProjects/fastApiProject/datas/coco128.yaml')
    # executor.submit(train.run, imgsz=640, data='../datas/coco128.yaml')
