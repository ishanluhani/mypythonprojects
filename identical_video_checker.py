import cv2
import os

path = 'E:/test/input'
videos = os.listdir(path)

for i in videos:
    vid2_data = []
    for j in videos:
        vid1_data = []
        if i != j:
            vid_1 = cv2.VideoCapture(path + '/' + j)
            while True:
                try:
                    ret, frame = vid_1.read()
                    vid1_data.append(frame)
                    cv2.imshow('frame', frame)
                except Exception:
                    break
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            vid_2 = cv2.VideoCapture(path + '/' + i)
            while True:
                try:
                    ret, frame = vid_2.read()
                    vid2_data.append(frame)
                    cv2.imshow('frame', frame)
                except Exception:
                    break
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            print(vid1_data)
            if vid1_data in vid2_data or vid2_data in vid1_data:
                print('ff')
'''
from os import path, walk, makedirs, rename
from shutil import copyfile
from time import clock
from imagehash import average_hash
from PIL import Image
from cv2 import VideoCapture, CAP_PROP_FRAME_COUNT, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS
from json import dump, load
from tkinter import filedialog
from multiprocessing import Pool, cpu_count

input_dir = open('input_dir.txt', 'r')
dir_to_save = 'E:/test/input//'
if input_dir.read() == '':
    dir_to_save = str(filedialog.askdirectory())
    open('input_dir.txt', 'w').write(dir_to_save)
input_vid_dir = dir_to_save + '/'
json_dir = r'E:\test\hidden_json\\'
analyzed_dir = r'E:\test\output_a\\'
duplicate_dir = r'E:\test\output_ua\\'


if not path.exists(json_dir):
    makedirs(json_dir)

if not path.exists(analyzed_dir):
    makedirs(analyzed_dir)

if not path.exists(duplicate_dir):
    makedirs(duplicate_dir)


def write_to_json(filename, data):
    file_full_path = json_dir + filename + ".json"
    with open(file_full_path, 'w') as file_pointer:
        dump(data, file_pointer)
    return


def video_to_json(filename):
    file_full_path = input_vid_dir + filename
    start = clock()
    size = round(path.getsize(file_full_path) / 1024 / 1024, 2)
    video_pointer = VideoCapture(file_full_path)
    frame_count = int(VideoCapture.get(video_pointer, int(CAP_PROP_FRAME_COUNT)))
    width = int(VideoCapture.get(video_pointer, int(CAP_PROP_FRAME_WIDTH)))
    height = int(VideoCapture.get(video_pointer, int(CAP_PROP_FRAME_HEIGHT)))
    fps = int(VideoCapture.get(video_pointer, int(CAP_PROP_FPS)))
    success, image = video_pointer.read()
    video_hash = {}
    while success:
        frame_hash = average_hash(Image.fromarray(image))
        video_hash[str(frame_hash)] = filename
        success, image = video_pointer.read()
    stop = clock()
    time_taken = stop - start
    print("Time taken for ", file_full_path, " is : ", time_taken)
    data_dict = dict()
    data_dict['size'] = size
    data_dict['time_taken'] = time_taken
    data_dict['fps'] = fps
    data_dict['height'] = height
    data_dict['width'] = width
    data_dict['frame_count'] = frame_count
    data_dict['filename'] = filename
    data_dict['video_hash'] = video_hash
    write_to_json(filename, data_dict)
    return


def multiprocess_video_to_json():
    files = next(walk(input_vid_dir))[2]
    processes = cpu_count()
    pool = Pool(processes)
    start = clock()
    pool.starmap_async(video_to_json, zip(files))
    pool.close()
    pool.join()
    stop = clock()
    print("Time Taken : ", stop - start)


def key_with_max_val(d):
    max_value = 0
    required_key = ""
    for k in d:
        if d[k] > max_value:
            max_value = d[k]
            required_key = k
    return required_key


def duplicate_analyzer():
    files = next(walk(json_dir))[2]
    data_dict = {}
    for file in files:
        filename = json_dir + file
        with open(filename) as f:
            data = load(f)
        video_hash = data['video_hash']
        count = 0
        duplicate_file_dict = dict()
        for key in video_hash:
            count += 1
            if key in data_dict:
                if data_dict[key] in duplicate_file_dict:
                    duplicate_file_dict[data_dict[key]] = duplicate_file_dict[data_dict[key]] + 1
                else:
                    duplicate_file_dict[data_dict[key]] = 1
            else:
                data_dict[key] = video_hash[key]
        if duplicate_file_dict:
            duplicate_file = key_with_max_val(duplicate_file_dict)
            duplicate_percentage = ((duplicate_file_dict[duplicate_file] / count) * 100)
            if duplicate_percentage > 50:
                file = file[:-5]
                print(file, " is duplicate of ", duplicate_file)
                src = analyzed_dir + file
                tgt = duplicate_dir + file
                if path.exists(src):
                    rename(src, tgt)



def mv_analyzed_file():
    files = next(walk(json_dir))[2]
    for filename in files:
        filename = filename[:-5]
        src = input_vid_dir + filename
        tgt = analyzed_dir + filename
        if path.exists(src):
            copyfile(src, tgt)


if __name__ == '__main__':
    mv_analyzed_file()
    multiprocess_video_to_json()
    mv_analyzed_file()
    duplicate_analyzer()
'''