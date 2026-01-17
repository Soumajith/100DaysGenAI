# Quick Reference Guide

## 🚀 Essential Commands

### Python & Jupyter
```bash
# Start Jupyter Notebook
jupyter notebook

# Start Jupyter Lab
jupyter lab

# Install package
pip install package-name

# List installed packages
pip list

# Create requirements file
pip freeze > requirements.txt
```

### Git
```bash
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "message"

# Push to GitHub
git push origin branch-name

# Pull latest changes
git pull
```

### Virtual Environments
```bash
# Create venv
python -m venv env

# Activate (Windows)
env\Scripts\activate

# Activate (Mac/Linux)
source env/bin/activate

# Deactivate
deactivate
```

## 📚 Common Python Libraries

### Data Manipulation
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

### Deep Learning
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

# or TensorFlow
import tensorflow as tf
from tensorflow import keras
```

### Transformers & LLMs
```python
from transformers import AutoTokenizer, AutoModel
import openai
from langchain import LLMChain
```

## 🔧 Useful Snippets

### PyTorch Model Template
```python
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = self.layer2(x)
        return x
```

### Training Loop
```python
for epoch in range(num_epochs):
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
```

### Load Pretrained Model
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
```

## 📊 Data Processing

### Load Data
```python
# CSV
df = pd.read_csv('file.csv')

# JSON
df = pd.read_json('file.json')

# Excel
df = pd.read_excel('file.xlsx')
```

### Basic Operations
```python
# Info
df.info()
df.describe()
df.head()

# Filter
df[df['column'] > value]

# Group
df.groupby('column').mean()

# Missing values
df.isnull().sum()
df.fillna(value)
df.dropna()
```

## 🎨 Visualization

### Matplotlib
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()
```

### Seaborn
```python
sns.set_style('whitegrid')
sns.scatterplot(x='col1', y='col2', data=df)
plt.show()
```

## 🤖 ML Model Training

### Scikit-learn
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
```

## 🔍 Debugging Tips

### Print Tensor Shapes
```python
print(f"Shape: {tensor.shape}")
print(f"Type: {tensor.dtype}")
print(f"Device: {tensor.device}")
```

### Check GPU
```python
# PyTorch
print(torch.cuda.is_available())
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# TensorFlow
print(tf.config.list_physical_devices('GPU'))
```

### Memory Management
```python
# PyTorch
torch.cuda.empty_cache()

# Check memory
print(torch.cuda.memory_allocated())
print(torch.cuda.memory_reserved())
```

## 📝 Keyboard Shortcuts

### Jupyter Notebook
- `Shift + Enter`: Run cell
- `Ctrl + Enter`: Run cell (stay in cell)
- `Alt + Enter`: Run cell and insert below
- `A`: Insert cell above
- `B`: Insert cell below
- `DD`: Delete cell
- `M`: Change to Markdown
- `Y`: Change to Code

### VS Code
- `Ctrl + /`: Comment line
- `Ctrl + D`: Select word
- `Ctrl + Shift + K`: Delete line
- `Alt + Up/Down`: Move line
- `Ctrl + Space`: Autocomplete

## 🌐 Useful Links

- [PyTorch Docs](https://pytorch.org/docs/)
- [TensorFlow Docs](https://www.tensorflow.org/api_docs)
- [Hugging Face](https://huggingface.co/)
- [Papers with Code](https://paperswithcode.com/)
- [Google Colab](https://colab.research.google.com/)

## 📱 Community Help

- Stack Overflow
- Reddit r/learnmachinelearning
- PyTorch Forums
- Hugging Face Forums
- Discord AI Communities

---

Keep this guide handy for quick reference! 🚀
