# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:35:33 2019

@author: Sirius
"""
# 在一个python 文件中调用另外一个python文件
# step1: 将当前文件的 args 传入要运行的python文件中，在将要运行的文件中
# 这样是为了避免将大量的参数全部重写一遍，并且容易出错
import pickle
save_pickle_name = os.path.join(self.savedir, 'current_argparse.pickle')
with open(save_pickle_name, 'wb') as handle:
      pickle.dump(self.args, handle, protocol=pickle.HIGHEST_PROTOCOL)


# 怎样将当前的args全部传到main_cal_activation中去?
subprocess.call("python ./get_intermediate_activation/main_cal_activation.py --evaluate-from {} --savedir {}".format(
current_ckpt_path, self.savedir), shell=True)
