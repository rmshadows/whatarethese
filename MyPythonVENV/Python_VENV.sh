#!/bin/bash
#### 用于创建Python VENV（仅用于我自己的Python项目）
# 虚拟环境文件夹名称
venv_libs_dir="ENV"
# 创建的激活文件名
act="activate"


## 控制台颜色输出
# 红色：警告、重点
# 黄色：警告、一般打印
# 绿色：执行日志
# 蓝色、白色：常规信息
# 颜色colors
CDEF=" \033[0m"                                     # default color
CCIN=" \033[0;36m"                                  # info color
CGSC=" \033[0;32m"                                  # success color
CRER=" \033[0;31m"                                  # error color
CWAR=" \033[0;33m"                                  # warning color
b_CDEF=" \033[1;37m"                                # bold default color
b_CCIN=" \033[1;36m"                                # bold info color
b_CGSC=" \033[1;32m"                                # bold success color
b_CRER=" \033[1;31m"                                # bold error color
b_CWAR=" \033[1;33m"  
# echo like ...  with  flag type  and display message  colors
# -s 绿
# -e 红
# -w 黄
# -i 蓝
prompt () {
  case ${1} in
    "-s"|"--success")
      echo -e "${b_CGSC}${@/-s/}${CDEF}";;          # print success message
    "-x"|"--exec")
      echo -e "日志：${b_CGSC}${@/-x/}${CDEF}";;          # print exec message
    "-e"|"--error")
      echo -e "${b_CRER}${@/-e/}${CDEF}";;          # print error message
    "-w"|"--warning")
      echo -e "${b_CWAR}${@/-w/}${CDEF}";;          # print warning message
    "-i"|"--info")
      echo -e "${b_CCIN}${@/-i/}${CDEF}";;          # print info message
    "-m"|"--msg")
      echo -e "信息：${b_CCIN}${@/-m/}${CDEF}";;          # print iinfo message
    "-k"|"--kv")  # 三个参数
      echo -e "${b_CCIN} ${2} ${b_CWAR} ${3} ${CDEF}";;          # print success message
    *)
    echo -e "$@"
    ;;
  esac
}

genAct(){
    if ! [ -f "$act" ];then
        prompt -s "正在生成 $act 文件...."
        echo "source ./$venv_libs_dir/bin/activate" > $act
    else
        prompt -e "已经存在名为$act的文件....请自行验证文件正确性(source ./$venv_libs_dir/bin/activate)，退出!"
        exit 1
    fi
}

# 首先检查有没有venv文件夹
if [ -d "$venv_libs_dir" ];then
    if ! [ -f "$venv_libs_dir/bin/activate" ];then
        prompt -e "$venv_libs_dir文件夹已存在，但似乎不是Python虚拟环境！"
        exit 1
    fi
    if ! [ -f "$venv_libs_dir/bin/activate.csh" ];then
        prompt -e "$venv_libs_dir文件夹已存在，但似乎不是Python虚拟环境！"
        exit 1
    fi
    prompt -s "$venv_libs_dir 文件夹已存在，进入Python虚拟环境....请运行 source $act "
    genAct
else
    prompt -w "$venv_libs_dir文件夹不存在，开始创建Python虚拟环境！"
    python3 -m venv "./$venv_libs_dir"
    prompt -s "进入Python虚拟环境....请运行 source $act "
    genAct
fi





