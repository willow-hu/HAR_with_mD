_base_ = [
    '../_base_/models/resnet50.py', '../_base_/datasets/micro_doppler.py', 
    '../_base_/schedules/imagenet_bs256.py', '../_base_/default_runtime.py'
]

# model settings
model = dict(
    # # Pretrain
    # backbone=dict(
    #     init_cfg=dict(
    #         type='Pretrained',
    #         checkpoint='weights/resnet50_8xb32_in1k_20210831-ea4938fc.pth',
    #         prefix='backbone'
    #     )
    # ),
    head=dict(
        num_classes=4,
        topk=(1),
    ))

# optimizer
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0001))

train_cfg = dict(by_epoch=True, max_epochs=100, val_interval=5)