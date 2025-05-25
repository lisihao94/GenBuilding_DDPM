# GenBuilding_DDPM
这是我们的研究的部分原始数据集和测试结果。
This is part of the original data set and test results of our research.

**trainingdata**中的文件是部分示例；您可以根据自己的数据和需求创建更多类似的示例。
The files in **trainingdata** are partial examples; you can create more similar examples based on your own data and requirements. 

本研究所采用的具体数据处理方法，请参见本文。
For the specific data‑processing methods used in this study, please refer to the paper. 

完成数据集的制作之后，请使用flist_generation.py将数据加载到flist文件中，以便模型在训练时读取。
After making the dataset, please use **flist_generation.py** to load the data into the flist file so that the model can be read during training.

请根据自己的数据量和设备进行参数设置。
Please set parameters according to your data volume and equipment.

本研究采用的python库和版本在requirements.txt中。官方的库可能会被更新导致代码报错，请根据官方版本选择合适的库进行安装。
The python library and version used in this study are in **requirements.txt** The official library may be updated, resulting in code errors. Please select the appropriate library to install according to the official version.

完成数据处理、代码调试、环境配置后，运行run.py开始你的训练。
After completing data processing, code debugging and environment configuration, run **run.py** to start your training.
