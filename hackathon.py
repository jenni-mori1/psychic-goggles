<<<<<<< HEAD
from transformers import BertTokenizer, BertForSequenceClassification
import torch_optimizer as optim
from transformers import torch.optim.AdamW
import torch

=======
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import transformers
from transformers import AutoModel, BertTokenizerFast
>>>>>>> 76e254da6f19c0b4b1f92d246d2e2304ccca03d7

device = torch.device("cuda")
df = pd.read_csv("/Users/ionaxia/Downloads/scam_data.csv")

df['label'].value_counts(normalize = True)

train_text, temp_text, train_labels, temp_labels = train_test_split(df['text'], df['label'], 
                                                                    random_state=2018, 
                                                                    test_size=0.3, 
                                                                    stratify=df['label'])


val_text, test_text, val_labels, test_labels = train_test_split(temp_text, temp_labels, 
                                                                random_state=2018, 
                                                                test_size=0.5, 
                                                                stratify=temp_labels)
