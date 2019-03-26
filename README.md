# Name

self-position-estimation-intro

# Overview

This repo include contents to check action of self-position-estimation (python ver. / private) .

このレポジトリは， self-position-estimation (python ver. / private) の動作確認に必要なコンテンツが含まれています．

# Requirement

## Linux
- ubuntu 16.04 / 18.04
- anaconda 3

## Mac
- 

## Windows

- 

# Tree

The directory structure of the program is as follows. 

プログラムのディレクトリ構造は下記を参考にしてください．

```
self-position-estimation- conf
├── LICENSE
├── README.md
├── environment_ubuntu.yml  (conda environment file)
├── rectangle.png  (sample image)
└── test_cv2.py (sample OpenCV program)

```

# Install

## install anaconda

ex. ubuntu.


```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
$ chmod 755 ./Anaconda3-5.2.0-Linux-x86_64.sh
$ ./Anaconda3-5.2.0-Linux-x86_64.sh
```

Plese set path during installsion.

If you need more information, plese reade [THIS page](https://docs.anaconda.com/anaconda/install/) . 

インストール中にパスを設定するか聞かれますので，その際には設定するように選択してください．

詳しくは，[公式サイト](https://docs.anaconda.com/anaconda/install/) を参考にしてください．

## conda environment

ex. ubuntu.

`environment_ubuntu.yml` is a conda environment file．

You will create conda environment by using `$ conda env create -f environment_ubuntu.yml` .
If you need more information, please reade https://conda.io/docs/index.html ．

`environment_ubuntu.yml` が環境構築ファイルです．

`$ conda env create -f environment_ubuntu.yml` で作ることができるでしょう．
詳しくは，https://conda.io/docs/index.html を参考にしてください．

If you use Mac: `environment_mac.yml`, or Windows: `environment_windows.yml` .

Macの場合は`environment_mac.yml`， Windowsの場合は `environment_windows.yml` が環境構築ファイルです．


# Version

- 2017/09/03 shishito megane edit
- 2018/07/04 shishito megane edit
- 2019/03/22 shishito megane edit

