#!/bin/bash
# 寻找py文件
# 最多2级！
# 这个脚本会帮咱们生成一个Readme文件
# Py项目
project_name="changeme"
# Markdown
md="# $project_name"

# 列出根目录文件
project_files=`ls "$project_name"`

pyfiles_md=""
pydirs_md=""

# 遍历判断是否是文件夹
for each in ${project_files[@]}
do
    # echo "$project_name/$each"
    if [ -d "$project_name/$each" ];then
        # 历遍子目录
        subdir_ls=$(ls $project_name/$each | grep ".py$")
        # 结果成功的情况下
        if [ "$?" -eq 0 ];then # && [ "${#subdir_ls[@]}" -ne 0 ]
            # 添加文件夹
            pydirs_md="$pydirs_md
## $each"
            for sub_each in ${subdir_ls[@]}
            do
                pydirs_md="$pydirs_md
### $sub_each"
                # echo "$each 添加 $sub_each"
                sub_each=$(echo $sub_each | sed 's/.py$//g')
                pydirs_md="$pydirs_md 
#### ::: $project_name.$each.$sub_each"
            done
            pydirs_md="$pydirs_md
        "
        fi
    else
        echo "$each" | grep ".py$" > /dev/null
        if [ "$?" -eq 0 ];then
            # echo "添加 $each"
            pyfiles_md="$pyfiles_md 
## $each"
            each=$(echo $each | sed 's/.py$//g')
            pyfiles_md="$pyfiles_md 
### ::: $project_name.$each"
            pyfiles_md="$pyfiles_md 
"
        fi
    fi
done

# echo "$pyfiles_md"
# echo "$pydirs_md"

md="$md
$pydirs_md
$pyfiles_md"

echo "$md" | tee index.md
mv index.md docs

