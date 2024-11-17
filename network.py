import torch
import torchvision.models as models

class VGG(torch.nn.Module):
    def __init__(self, vgg='vgg11_bn', data_set='CIFAR10', pretrained=False):
        super(VGG, self).__init__()
        self.features = models.__dict__[vgg](pretrained=pretrained).features
        classifier = []
        classifier.append(torch.nn.Linear(512, 512))
        classifier.append(torch.nn.BatchNorm1d(512))
        classifier.append(torch.nn.Linear(512, 10))
        self.classifier = torch.nn.Sequential(*classifier)
        
    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x
