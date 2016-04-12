import glob
import os
#import pdb
path1 = '/home/zyy/workspace/wangml/caffe-action/data/PersonRunsVideo/CAM3/'
path2 = '/home/zyy/workspace/wangml/caffe-action/data/PersonRuns_Flow_Img/'

videolist = []
videolist = glob.glob(path1 + '/*')
videoname = [fn.split('/',9)[9] for fn in videolist]

for v in videoname:
    v = v.split('.',1)[0]
    path = os.path.join(path2 , v)
    if not os.path.exists(path):
        os.mkdir(path)
    file1 = path1 + v + '.avi'
    file2 = path + '/flow_x'
    file3 = path + '/flow_y'
    file4 = path + '/flow_i'
    device_id = 0
    step = 1
    cmd = './denseFlow_gpu -f {} -x {} -y {} -i {} -b 20 -t {} -d {} -s {}'.format( \
                            file1,file2,file3,file4,1,device_id,step)
    os.system(cmd)
 #   pdb.set_trace()