import glob
import os
#import pdb
path_video = '/home/zyy/workspace/wangml/caffe-action/data/PersonRunsVideo/CAM1/'
path_rgb = '/home/zyy/workspace/wangml/caffe-action/data/PersonRuns_rgb_img/'
path_flow = '/home/zyy/workspace/wangml/caffe-action/data/PersonRuns_flow_img/'

videolist = []
videolist = glob.glob(path_video + '/*')
videoname = [fn.split('/',9)[9] for fn in videolist]

for v in videoname:
    v = v.split('.',1)[0]
    path1 = os.path.join(path_rgb , v)
    if not os.path.exists(path1):
        os.mkdir(path1)

    path2 = os.path.join(path_flow , v)
    if not os.path.exists(path2):
        os.mkdir(path2)
    file1 = path_video + v + '.avi'
    file2 = path2 + '/flow_x'
    file3 = path2 + '/flow_y'
    file4 = path1 + '/image'
    device_id = 0
    step = 1
    cmd = './denseFlow_gpu -f {} -x {} -y {} -i {} -b 20 -t {} -d {} -s {}'.format( \
                            file1,file2,file3,file4,1,device_id,step)
    os.system(cmd)
 #   pdb.set_trace()
