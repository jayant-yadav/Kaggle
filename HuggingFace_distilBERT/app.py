# import gradio as gr
from datasets import load_dataset
import pandas as pd

def greet(name):
    return "Hello " + name + "!!"

# iface = gr.Interface(fn=greet, inputs="text", outputs="text")
# iface.launch()

data_files = {"train": "wikitext-2-raw-v1"}
dataset = load_dataset("wikitext",'wikitext-2-raw-v1', split = "train")

train_df = pd.DataFrame(dataset)
print(train_df.loc[10,'text'])
# data_files = {"train": "train.csv", "test": "test.csv"}
# dataset = load_dataset("namespace/your_dataset_name", data_files=data_files)
