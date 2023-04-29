CONFIG_FILE='configs/resnet/resnet34_8xb32_md.py'
WORK_DIR='work_dirs/microD_50train_r34_lr0.1'

python tools/train.py \
$CONFIG_FILE \
--work-dir $WORK_DIR \ 