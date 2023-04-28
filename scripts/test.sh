CONFIG_FILE='configs/resnet/resnet18_8xb32_md.py'
CHECKPOINT_FILE='work_dirs/microD_try/epoch_100.pth'
WORK_DIR='work_dirs/microD_try/results'

python tools/test.py \
$CONFIG_FILE \
$CHECKPOINT_FILE \
--work-dir $WORK_DIR \
--out work_dirs/microD_try/results/out.pkl