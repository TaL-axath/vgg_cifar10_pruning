## Arguments
`--train-flag`：在 CIFAR 数据集上训练 VGG 模型，训练的时候打上这个flag  
`--save-path`：保存结果的路径，例如 `trained_models/`  
`--load-path`：加载检查点的路径，与 `save-path` 拼接添加 `'checkpoint.pth'`，例如 `trained_models/checkpoint.pth`  
`--resume-flag`：从通过 `load-path` 加载的检查点恢复训练  
`--prune-flag`：对 VGG 模型进行剪枝，剪枝的时候打上这个flag
`--prune-layers`：指定要进行剪枝的卷积层列表，例如 `conv1 conv2`  
`--prune-channels`：指定 `prune-layers` 中每层要剪枝的通道数列表，例如 `4 14`  
`--independent-prune-flag`：使用独立策略对多层进行剪枝  
`--retrain-flag`：对剪枝后的网络进行重新训练，剪枝后网络重新训练的时候打上这个flag
`--retrain-epoch`：剪枝后网络重新训练的轮数  
`--retrain-lr`：剪枝后网络重新训练的学习率  


## 示例

在 cifar10 数据集上训练 vgg11_bn
```bash
python main.py --train-flag --data-set CIFAR10 --vgg vgg11_bn --save-path ./trained_models/vgg11_bn_cifar10/
```

以 greedy strategy 进行剪枝 （以剪掉 conv1 和 conv2 的通道各一个为例）
```bash
python main.py --prune-flag --load-path ./trained_models/vgg11_bn_cifar10/check_point.pth --save-path ./trained_models/pruning_reuslts/ --prune-layers conv1 conv2 --prune-channels 1 1 
```

以 independent strategy 进行剪枝（以剪掉 conv1 和 conv2 的通道各一个为例）
```bash
python main.py --prune-flag --load-path ./trained_models/vgg11_bn_cifar10/check_point.pth --save-path ./trained_models/pruning_reuslts/ --prune-layers conv1 conv2 --prune-channels 1 1 --independent-prune-flag
```

对剪枝后的网络进行重新训练
```bash
python main.py --prune-flag --load-path ./trained_models/vgg11_bn_cifar10/check_point.pth --save-path ./trained_models/pruning_reuslts/ --prune-layers conv1 --prune-channels 1 --retrain-flag --retrain-epoch 20 --retrain-lr 0.001
```