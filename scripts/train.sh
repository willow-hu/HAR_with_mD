CONFIG_FILE='configs/resnet/resnet18_8xb32_md.py'
GPU_NUM=1
WORK_DIR='work_dirs/microD_try'

bash ./tools/dist_train.sh \
$CONFIG_FILE \
$GPU_NUM \
--work-dir $WORK_DIR \ 