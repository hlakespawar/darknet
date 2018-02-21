defaultIP="udp://@239.2.99.2:16400"

rm logfile.txt
./darknet detector demo cfg/coco.data cfg/yolo.cfg yolo.weights $defaultIP -i 0
