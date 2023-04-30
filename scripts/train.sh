CONFIG_FILE='configs/vision_transformer/vit-base-p16_64xb64_md.py'
WORK_DIR='work_dirs/microD_50train_vit'

python tools/train.py \
$CONFIG_FILE \
--work-dir $WORK_DIR