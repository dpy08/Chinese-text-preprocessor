# 中文文本预处理器 Chinese-text-preprocessor
> 一个基于 Python + jieba 的中文文本预处理工具，实现文本清洗、分词、停用词过滤、词频统计，结果导出 CSV 文件。

## ✨ 项目功能
1. 文本清洗：去除多余空格、换行、网页符号、非文字字符
2. jieba 中文分词
3. 加载自定义停用词库，过滤无意义虚词
4. 统计单词出现频次
5. 将词频结果导出为 `word_frequency.csv`
   
## 📁 项目目录结构
Chinese-text-preprocessor/
├── src/
│   └── preprocess.py       # 主程序代码
├── data/
│   ├── test.txt            # 待处理原始文本
│   └── STOP_WORDS.txt      # 停用词库
├── result/
│   └── word_frequency.csv  # 输出词频结果
├── .gitignore              # Git忽略配置（忽略虚拟环境、缓存文件）
└── README.md               # 项目说明文档


## 🧰 环境依赖
- Python >=3.8
- jieba

安装依赖：
```bash
pip install jieba


🚀 运行方法
 
1. 在  data/test.txt  放入你需要分析的文本
​
2. 运行主程序
python src/preprocess.py

3. 运行完成后，在  result/word_frequency.csv  查看词频统计结果
 
📌 项目亮点
 
- 模块化代码，易于修改、扩展
​
- 独立停用词文件，方便增删停用词汇
​
- 自动导出CSV，可直接用Excel打开查看词频
​
- 可扩展方向：词性标注、关键词提取、文本摘要
 
📝 开发说明
 
本项目为个人学习项目，用于练习Python、文本处理算法，后续计划持续迭代。
