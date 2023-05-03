#!/usr/bin/env python3
import os
import sys
programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
for i in sys.argv[1:]:
    os.system(f"python3 '{programPath}/add.py' '{i}'")
os.chdir(programPath)
lists = []
for i in sys.argv[1:]:
    lists.append(os.path.basename(i))
os.system(f"bash '{programPath}/incremental-updating-packages.sh' '{programPath}'")
os.system("apt-ftparchive release . > Release")
os.system("rm Release.gpg")
os.system("rm InRelease")
os.system("rm gpg.asc")
os.system("gpg --armor --detach-sign -o Release.gpg Release")
os.system("gpg --clearsign -o InRelease Release")
os.system("gpg --armor --output gpg.asc --export 3025613752@qq.com")
#os.system(f"cd '{programPath}/../apt-packages-websize-program/' ; git add .")
#os.system(f"cd '{programPath}/../apt-packages-websize-program/' ; git commit -m '新增 {lists} 个安装包'")
#os.system(f"cd '{programPath}/../apt-packages-websize-program/' ; git push")
os.system(f"cd '{programPath}/'; git add . ; git commit -m '新增 {lists} 安装包' ; git push")