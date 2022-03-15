#!/bin/bash
#### 同步github

## 询问函数 Yes:1 No:2 ???:5
:<<!询问函数
函数调用请使用：
comfirm "\e[1;33m? [y/N]\e[0m"
choice=$?
if [ $choice == 1 ];then
  yes
elif [ $choice == 2 ];then
  prompt -i "——————————  下一项  ——————————"
else
  prompt -e "ERROR:未知返回值!"
  exit 5
fi
!询问函数
comfirm () {
  flag=true
  ask=$1
  while $flag
  do
    echo -e "$ask"
    read -r input
    if [ -z "${input}" ];then
      # 默认选择Y
      input='y'
    fi
    case $input in [yY][eE][sS]|[yY])
      return 1
      flag=false
    ;;
    [nN][oO]|[nN])
      return 2
      flag=false
    ;;
    *)
      echo "Invalid option..."
    ;;
    esac
  done
}

# 检查
if ! [ -d "./../whatarethese" ];then
    echo "没有whatarethese文件夹"
    exit 1
fi

# Main
comfirm "\e[1;33m是否清空Github目录? [Y/n]\e[0m"
choice=$?
if [ $choice == 1 ];then
  mkdir ./../whatarethese/bak
  mv ./../whatarethese/* ./../whatarethese/bak/
elif [ $choice == 2 ];then
  echo "未清空目录"
else
  echo "未知选项"
  exit 5
fi
# 复制文件
cp -r ./* ./../whatarethese/


