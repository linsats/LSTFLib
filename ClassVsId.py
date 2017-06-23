import sys
sys.path.append('/orions4-zfs/projects/lins2/LSTFLib')
from File_Dir_Op import *

category2synsetid = {'Chair':'03001627',
               'Bookshelf':'02871439',
               'Cabinet':'02933112',
               'Dishwasher':'03207941',
               'Display':'03211117',
               'Lamp':'03636649',
               'Sofa':'04256520',
               'Table':'04379243',
               'Printer':'04004475'}

shapenetcore_top_dir = '/orions4-zfs/projects/lins2/JointEmbedding/data/ShapeNetCore2015Summer/' 
#synsetids = ['03001627', '02871439', '02933112', '03207941', '03211117', '03636649', '04256520', '04379243', '04004475'] 
synsetids = ['03001627', '03337140', '02871439', '02933112', '03636649', '04379243', '04256520']

modelid2synsetid = {}
for cate in synsetids:
    class_dir = os.path.join(shapenetcore_top_dir,cate)
    modelids = dirs_under_top_dir(class_dir)
    for model in modelids:
        modelid2synsetid[model] = cate
  
  

