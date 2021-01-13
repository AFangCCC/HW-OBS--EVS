import os
import moxing as mox
from modelarts.session import Session

session = Session()
in_root_dir = "obs://bucket-name/dic-name"
out_root_dir = "/home/ma-user/work/dic-name"

for i, walk_out in enumerate(mox.file.walk(in_root_dir)):

    dirpath, dirnames, filenames = walk_out
    print("----------Epoch: ", i, "----------")

    print("当前根路径：")
    current_in_root = dirpath
    current_out_root = out_root_dir+dirpath.split(in_root_dir)[-1]
    print("输入：", current_in_root)
    print("输出：", current_out_root)

    print("建立子文件夹")
    if len(dirnames) == 0:
        print("None")
        pass
    else:
        for subdir in dirnames:
            if not os.path.exists(os.path.join(current_out_root, subdir)):
                mox.file.mk_dir(os.path.join(current_out_root, subdir))
                print("创建文件夹：", os.path.join(current_out_root, subdir))
            else:
                print("文件夹",os.path.join(current_out_root, subdir),"已经存在")

    print("遍历拷贝文件")
    if len(filenames) == 0:
        print("None")
        pass
    else:
        for f in filenames:
            if not os.path.exists(os.path.join(current_out_root, f)):
                session.obs.download_file(src_obs_file=os.path.join(dirpath, f),
                                          dst_local_dir=current_out_root)
                print(os.path.join(current_out_root, f), "导入成功")
            else:
                print("文件",os.path.join(current_out_root, f),"已经存在")
    
    print("\n")
