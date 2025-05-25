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

当前的库。requirements：
Package                      Version
---------------------------- ---------------
absl-py                      2.1.0
addict                       2.4.0
affine                       2.4.0
aiofiles                     23.2.1
anyio                        4.4.0
asttokens                    2.4.1
astunparse                   1.6.3
attrs                        24.1.0
backcall                     0.2.0
basicsr                      1.4.2
blinker                      1.8.2
Brotli                       1.0.9
cachetools                   5.3.3
certifi                      2024.2.2
charset-normalizer           2.0.4
ci-info                      0.3.0
click                        8.1.7
click-plugins                1.1.1
cligj                        0.7.2
colorama                     0.4.6
comm                         0.2.2
ConfigArgParse               1.7
configobj                    5.0.8
configparser                 7.0.0
contourpy                    1.1.1
cycler                       0.12.1
dash                         2.18.1
dash-core-components         2.0.0
dash-html-components         2.0.0
dash-table                   5.0.0
decorator                    5.1.1
docx                         0.2.4
et_xmlfile                   2.0.0
etelemetry                   0.3.1
exceptiongroup               1.2.1
executing                    2.1.0
facexlib                     0.3.0
fastjsonschema               2.20.0
filelock                     3.13.1
filterpy                     1.4.5
fiona                        1.9.6
fitz                         0.0.1.dev2
Flask                        3.0.3
flatbuffers                  24.3.25
fonttools                    4.53.0
frontend                     0.0.3
fsspec                       2024.5.0
future                       1.0.0
gast                         0.4.0
geopandas                    0.13.2
gfpgan                       1.3.8
gmpy2                        2.1.2
google-auth                  2.30.0
google-auth-oauthlib         1.0.0
google-pasta                 0.2.0
graphviz                     0.20.3
grpcio                       1.64.1
h11                          0.14.0
h5py                         3.11.0
httplib2                     0.22.0
idna                         3.7
imagecodecs                  2023.3.16
imageio                      2.35.1
importlib_metadata           7.1.0
importlib_resources          6.4.0
ipython                      8.12.3
ipywidgets                   8.1.5
isodate                      0.6.1
itsdangerous                 2.2.0
jedi                         0.19.1
Jinja2                       3.1.3
joblib                       1.4.2
jsonschema                   4.23.0
jsonschema-specifications    2023.12.1
jupyter_core                 5.7.2
jupyterlab_widgets           3.0.13
keras                        2.13.1
kiwisolver                   1.4.5
lazy_loader                  0.4
libclang                     18.1.1
llvmlite                     0.41.1
lmdb                         1.6.2
looseversion                 1.3.0
lxml                         5.2.2
Markdown                     3.6
MarkupSafe                   2.1.3
matplotlib                   3.7.5
matplotlib-inline            0.1.7
mkl-fft                      1.3.8
mkl-random                   1.2.4
mkl-service                  2.4.0
mpmath                       1.3.0
nbformat                     5.10.4
nest-asyncio                 1.6.0
networkx                     3.1
nibabel                      5.2.1
nipype                       1.8.6
numba                        0.58.1
numpy                        1.24.4
oauthlib                     3.2.2
open3d                       0.18.0
opencv-python                4.9.0.80
openpyxl                     3.1.5
opt-einsum                   3.3.0
packaging                    24.0
pandas                       2.0.3
parso                        0.8.4
pathlib                      1.0.1
pickleshare                  0.7.5
pillow                       10.3.0
pip                          24.0
pkgutil_resolve_name         1.3.10
platformdirs                 4.3.6
plotly                       5.24.1
plyfile                      1.0.3
prompt_toolkit               3.0.48
protobuf                     4.25.3
prov                         2.0.0
pure_eval                    0.2.3
pyasn1                       0.6.0
pyasn1_modules               0.4.0
pydot                        2.0.0
Pygments                     2.18.0
pyparsing                    3.1.2
pyproj                       3.5.0
PySocks                      1.7.1
python-dateutil              2.9.0.post0
python-docx                  1.1.2
pytz                         2024.1
PyWavelets                   1.4.1
pywin32                      308
pyxnat                       1.6.2
PyYAML                       6.0.2
rasterio                     1.3.10
rdflib                       7.0.0
realesrgan                   0.3.0
referencing                  0.35.1
requests                     2.31.0
requests-oauthlib            2.0.0
retrying                     1.3.4
rpds-py                      0.20.0
rsa                          4.9
scikit-image                 0.21.0
scikit-learn                 1.3.2
scipy                        1.10.1
seaborn                      0.13.2
setuptools                   69.5.1
shapely                      2.0.4
simplejson                   3.19.2
six                          1.16.0
sniffio                      1.3.1
snuggs                       1.4.7
stack-data                   0.6.3
starlette                    0.37.2
sympy                        1.12
tb-nightly                   2.14.0a20230808
tenacity                     9.0.0
tensorboard                  2.13.0
tensorboard-data-server      0.7.2
tensorboardX                 2.6.2.2
tensorflow                   2.13.0
tensorflow-estimator         2.13.0
tensorflow-intel             2.13.0
tensorflow-io-gcs-filesystem 0.31.0
termcolor                    2.4.0
threadpoolctl                3.5.0
tifffile                     2023.7.10
tomli                        2.2.1
torch                        2.2.1+cu118
torch-fidelity               0.3.0
torchvision                  0.17.1+cu118
tqdm                         4.66.4
traitlets                    5.14.3
traits                       6.3.2
trimesh                      4.6.4
typing_extensions            4.12.2
tzdata                       2024.1
urllib3                      2.2.1
uvicorn                      0.29.0
wcwidth                      0.2.13
Werkzeug                     3.0.3
wheel                        0.43.0
widgetsnbextension           4.0.13
win-inet-pton                1.1.0
wrapt                        1.16.0
yapf                         0.43.0
zipp                         3.19.0
