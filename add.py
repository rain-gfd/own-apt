#!/usr/bin/env python3
import os
import sys
import random
import datetime
import subprocess
programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
#os.chdir(programPath)
# 获取版本号和架构
def GetDebVersion(deb: str):
    global all
    tempPath = f"/tmp/get-deb-{random.randint(0, 10000)}"
    os.system(f"dpkg -e '{deb}' '{tempPath}'")
    version = "1.0.0"
    arch = "amd64"
    package = "demo"
    v = False
    with open(f"{tempPath}/control", "r") as file:
        all = file.read()
    with open(f"{tempPath}/control", "r") as file:
        while True:
            read = file.readline().replace("\n", "")
            if read == "":
                break
            if "version:" == read[:8].lower() and not v:
                version = read.replace("\n", "").replace("Version:", "").strip().replace(" ", "")
                v = True
            if "Architecture:" in read:
                arch = read.replace("\n", "").replace("Architecture:", "").strip().replace(" ", "")
            if "Package:" in read:
                package = read.replace("\n", "").replace("Package:", "").strip().replace(" ", "")
    os.system(f"rm -rfv '{tempPath}'")
    return [arch, version, package]
debInfo = GetDebVersion(sys.argv[1])
if not os.path.exists(f"{programPath}/{debInfo[2][0].lower()}/{debInfo[2]}"):
    os.makedirs(f"{programPath}/{debInfo[2][0].lower()}/{debInfo[2]}")
os.system(f"cp -v '{sys.argv[1]}' '{programPath}/{debInfo[2][0].lower()}/{debInfo[2]}/{debInfo[2]}_{debInfo[1]}_{debInfo[0]}.deb'")
os.chdir(programPath)

# 更新 pages
try:
    with open(f"{programPath}/list.html", "r") as file:
        html = file.read()
except:
    html = ""
html = f"""<h2>{debInfo[2]}_{debInfo[1]}_{debInfo[0]}.deb</h2>
<p><b>下载链接：<a href='http://apt.gfdgdxi.top/{debInfo[2][0].lower()}/{debInfo[2]}/{debInfo[2]}_{debInfo[1]}_{debInfo[0]}.deb'>http://apt.gfdgdxi.top/{debInfo[2][0].lower()}/{debInfo[2]}/{debInfo[2]}_{debInfo[1]}_{debInfo[0]}.deb</a></b></p>
<pre><code>{all}</code></pre>
{html}"""
with open(f"{programPath}/list.html", "w") as file:
    file.write(html)
indexHtml = f"""<!DOCTYPE html>
<head>
    <title>APT 库列表（By gfdgd xi）</title>
    <meta name="viewport" content="width=device-width" initial-scale="1" />
    <meta charset='UTF-8'>
    <meta http-equiv="content-language" content="zh-cn">
    <meta name="description" content="APT 库列表（By gfdgd xi）" >
    <style  type="text/css">
    pre {{
        overflow: auto;
    }}

    a {{
        word-break:break-all;
        word-wrap:break-word;
    }}

    h2 {{
        overflow: auto;
        word-break:break-all;
        word-wrap:break-word;
    }}
</style>
</head>

<body>
    <h1>APT 库列表（By gfdgd xi）</h1>
    <p>点击下方链接下载</p>
    <h3>推荐直接添加该源，添加方法：</h3>
    <pre><code>
wget http://apt.gfdgdxi.top/sources/github.sh; bash github.sh; rm github.sh
</code></pre>
    <p>作者：<a href='https://gitee.com/gfdgd-xi/'>https://gitee.com/gfdgd-xi/</a></p>
    <p><a href='tree.html'>在这里查看 APT 源目录树</a></p>
    <h3>更新时间：{datetime.datetime.now().year}年{datetime.datetime.now().month}月{datetime.datetime.now().day}日 {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}</h3>
    <hr/>
    {html}
    <hr/>
    <h1 id="copyright">©2020~{datetime.datetime.now().year} gfdgd xi</h1>
</body>
<script>
    window.onload = function(){{
        var d = new Date();
        document.getElementById("copyright").innerHTML = "©2020~" + d.getFullYear() + " gfdgd xi";
    }}
</script>
<script>
var _hmt = _hmt || [];
(function() {{
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?807ee27dfca59506248e7f74c812ca3d";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
}})();
</script>

"""
with open(f"{programPath}/index.html", "w") as file:
    file.write(indexHtml)
with open(f"{programPath}/tree.html", "w") as file:
    file.write(f"""<!DOCTYPE html>
<head>
    <title>APT 库目录树（By gfdgd xi）</title>
    <meta name="viewport" content="width=device-width" initial-scale="1" />
    <meta charset='UTF-8'>
    <meta http-equiv="content-language" content="zh-cn">
    <meta name="description" content="APT 库列表（By gfdgd xi）" >
    <style  type="text/css">
    pre {{
        overflow: auto;
    }}

    a {{
        word-break:break-all;
        word-wrap:break-word;
    }}

    h2 {{
        overflow: auto;
        word-break:break-all;
        word-wrap:break-word;
    }}
</style>
</head>

<body>
    <h1>APT 库目录树（By gfdgd xi）</h1>
    <p>作者：<a href='https://gitee.com/gfdgd-xi/'>https://gitee.com/gfdgd-xi/</a></p>
    <h3>更新时间：{datetime.datetime.now().year}年{datetime.datetime.now().month}月{datetime.datetime.now().day}日 {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}</h3>
    <hr/>
    <pre><code>
{subprocess.getoutput(f"cd '{programPath}' ; tree")}
    </code></pre>
    <hr/>
    <h1 id="copyright">©2020~{datetime.datetime.now().year} gfdgd xi</h1>
</body>
<script>
    window.onload = function(){{
        var d = new Date();
        document.getElementById("copyright").innerHTML = "©2020~" + d.getFullYear() + " gfdgd xi";
    }}
</script>
<script>
var _hmt = _hmt || [];
(function() {{
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?807ee27dfca59506248e7f74c812ca3d";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
}})();
</script>
""")
