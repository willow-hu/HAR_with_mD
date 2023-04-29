EXP_NAME='work_dirs/microD_50train_base_lr0.1/'
CONFIG_FILE='configs/resnet/resnet18_8xb32_md.py'
CHECKPOINT_FILE=$EXP_NAME'epoch_100.pth'
WORK_DIR=$EXP_NAME'results'
OUT_FILE=$EXP_NAME'results/out.pkl'

python tools/test.py \
$CONFIG_FILE \
$CHECKPOINT_FILE \
--work-dir $WORK_DIR \
--out $OUT_FILE