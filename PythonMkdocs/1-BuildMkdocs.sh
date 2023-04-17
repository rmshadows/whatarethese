#!/bin/bash
# 安装Mkdocs
# md文件： src.xxx(py文件)

DOC_DIR="PyDocs"
# Py项目
project_name="Python项目文档"
# mkdocs配置
mkdocs_conf="site_name: PyDocs
theme: readthedocs
plugins:
  - search
  - mkdocstrings
"

pip install mkdocs
pip install mkdocstrings
pip install mkdocstrings-python
mkdocs -h
if [ "$?" -eq 0 ];then
    echo "Seems everything good."
else
    echo "Something failed. Check manually."
    exit 1
fi
# 新docs建项目
mkdocs new "$DOC_DIR"
# 复制脚本
cp Pydocs2Md.sh "$DOC_DIR"
cd "$DOC_DIR"
echo "$mkdocs_conf" > "mkdocs.yml"
sed -i s/changeme/"$project_name"/g Pydocs2Md.sh

