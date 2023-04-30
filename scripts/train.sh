CONFIG_FILE='configs/resnet/resnet34_8xb32_md.py'
WORK_DIR='work_dirs/microD_subj_r34'

python tools/train.py \
$CONFIG_FILE \
--work-dir $WORK_DIR