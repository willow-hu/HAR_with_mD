_base_ = [
    '../_base_/models/resnet18.py', '../_base_/datasets/micro_doppler.py', 
    '../_base_/schedules/imagenet_bs256.py', '../_base_/default_runtime.py'
]

# model settings
model = dict(
    head=dict(
        num_classes=4,
    ))

# optimizer
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=1e-3, momentum=0.9, weight_decay=0.0001))

train_cfg = dict(by_epoch=True, max_epochs=100, val_interval=5)