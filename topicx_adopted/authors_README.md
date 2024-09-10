# Is Neural Topic Modelling Better than Clustering? An Empirical Study on Clustering with Contextual Embeddings for Topics
This is the official repository of the NAACL 2022 paper "*Is Neural Topic Modelling Better than Clustering? An Empirical Study on Clustering with Contextual Embeddings for Topics*".

Paper is available at [https://aclanthology.org/2022.naacl-main.285/](https://aclanthology.org/2022.naacl-main.285/). 

## Quick Links
* [Install Dependencies](#install-dependencies)
* [Run CETopic](#run-cetopic)
* [Run Using Shell](#run-using-shell)
    + [Dataset](#dataset)
    + [Topic Model](#topic-model)
    + [Word Selecting Method](#word-selecting-method)
    + [Pretrained Model](#pretrained-model)
    + [Arguments](#arguments)
    + [Examples](#examples)
 * [Add New Models](#add-new-models)
 * [Citation](#citation)
 * [Acknowledgement](#acknowledgement)
 * [License](#license)

## Install Dependencies
```shell
conda create -n cluster_topic_model python=3.7 -y
conda activate cluster_topic_model
pip install -r requirements.txt
```

## Run CETopic

Below is an example of how to run CETopic on the BBC dataset. You can choose a word selecting method from `[tfidf_idfi, tfidf_tfi, tfidfi, tfi]`. If you prefer not to reduce the embedding dimensionalities using UMAP, simply set `dim_size=-1`. You can train the model, get evaluation results and topics:

```python
from baselines.cetopictm import CETopicTM
from utils import prepare_dataset

dataset, sentences = prepare_dataset('bbc')

tm = CETopicTM(dataset=dataset, 
               topic_model='cetopic', 
               num_topics=5, 
               dim_size=5, 
               word_select_method='tfidf_idfi',
               embedding='princeton-nlp/unsup-simcse-bert-base-uncased', 
               seed=42)

tm.train()
td_score, cv_score, npmi_score = tm.evaluate()
print(f'td: {td_score} npmi: {npmi_score} cv: {cv_score}')

topics = tm.get_topics()
print(f'Topics: {topics}')
```

You should expect something similar:
```python
td: 0.96 npmi: 0.11889979828579675 cv: 0.7574707739043192

Topics: {
0: [
    ('tory', 0.010655754552013494), 
    ('labour', 0.010140645139665033), 
    ('election', 0.008794514704281466), 
    ('party', 0.007523648919704865), 
    ('government', 0.006801391630922592), 
    ('plan', 0.00444844822680986), 
    ('minister', 0.003928431285391421), 
    ('leader', 0.0037359746494665725), 
    ('pension', 0.003697165535497612), 
    ('lord', 0.0036023621214819595)
  ], ...
}
```

## Run Using Shell

```shell
bash run_evaluate.sh
```

### Dataset

We use preproessed dataset from [OCTIS](https://github.com/MIND-Lab/OCTIS#datasets-and-preprocessing). You can choose from `[bbc, m10, 20ng]`. 

### Topic Model

You can run our model `cetopic` or you can also choose a baseline model from `[lda, prodlda, zeroshottm, combinedtm, bertopic]`.

### Word Selecting Method

If you use `cetopic`, you can also choose a word selecting method from `[tfidf_idfi, tfidf_tfi, tfidfi, tfi]`.

### Pretrained Model
You can choose a pretrained model such as `princeton-nlp/unsup-simcse-bert-base-uncased` or `bert-base-uncased` from [SimCSE](https://github.com/princeton-nlp/SimCSE) or [HuggingFace](https://huggingface.co/models).

### Arguments
```
usage: main.py [-h] [--topic_model TOPIC_MODEL] [--dataset DATASET] 
[--pretrained_model PRETRAINED_MODEL] [--num_topics NUM_TOPICS] 
[--dim_size DIM_SIZE] [--word_select_method WORD_SELECT_METHOD] [--seed SEED]

Cluster Contextual Embeddings for Topic Models

optional arguments:
  -h, --help            show this help message and exit
  --topic_model TOPIC_MODEL
                        Topic model to run experiments
  --dataset DATASET     Datasets to run experiments
  --pretrained_model PRETRAINED_MODEL
                        Pretrained language model
  --num_topics NUM_TOPICS
                        Topic number
  --dim_size DIM_SIZE   Embedding dimension size to reduce to
  --word_select_method WORD_SELECT_METHOD
                        Word selecting methods to select words from each cluster
  --seed SEED           Random seed
```

### Examples

\>> Run `cetopic` on BBC dataset using `tfidf_idfi` word selecting method and unsupervised SimCSE embeddings, the embedding dimensionality will be reduced to 5 and will ouput 5 topics:
```shell
# run_evaluate.sh

DATASET='bbc'
TOPIC_MODEL='cetopic'
WORD_SELECT_METHOD='tfidf_idfi'
PRETRAINED_MODEL='princeton-nlp/unsup-simcse-bert-base-uncased'

python main.py\
    --topic_model ${TOPIC_MODEL}\
    --dataset ${DATASET}\
    --num_topics 5\
    --dim_size 5\
    --word_select_method ${WORD_SELECT_METHOD}\
    --pretrained_model ${PRETRAINED_MODEL}\
    --seed 30
```

\>> Run `bertopic` on 20NewsGroup dataset using BERT embeddings and expect to ouput 50 topics. *Note that BERTopic may not output the exact specified number of topics*:
```shell
# run_evaluate.sh

DATASET='20ng'
TOPIC_MODEL='bertopic'
PRETRAINED_MODEL='bert-base-uncased'

python main.py\
    --topic_model ${TOPIC_MODEL}\
    --dataset ${DATASET}\
    --num_topics 50\
    --pretrained_model ${PRETRAINED_MODEL}\
```

\>> Run `combinedtm` on M10 dataset using RoBERTa embeddings and expect to ouput 75 topics:
```shell
# run_evaluate.sh

DATASET='m10'
TOPIC_MODEL='combinedtm'
PRETRAINED_MODEL='roberta-base'

python main.py\
    --topic_model ${TOPIC_MODEL}\
    --dataset ${DATASET}\
    --num_topics 75\
    --pretrained_model ${PRETRAINED_MODEL}\
```

## Add New Models

To add new topic models, you can inherit the base class `TopicModel` and implement your own `train()`, `evaluate()`, and `get_topics()` functions:

```python
class TopicModel:
    def __init__(self, dataset, topic_model, num_topics):
        self.dataset = dataset
        self.topic_model = topic_model
        self.num_topics = num_topics
        
    def train(self):
        raise NotImplementedError("Train function has not been defined!")

    def evaluate(self):
        raise NotImplementedError("Evaluate function has not been defined!")

    def get_topics(self):
        raise NotImplementedError("Get topics function has not been defined!")
```

## Citation

If our research helps you, please kindly cite our paper:
```bibtex
@inproceedings{zhang-etal-2022-neural,
    title = "Is Neural Topic Modelling Better than Clustering? An Empirical Study on Clustering with Contextual Embeddings for Topics",
    author = "Zhang, Zihan  and
      Fang, Meng  and
      Chen, Ling  and
      Namazi Rad, Mohammad Reza",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.naacl-main.285",
    doi = "10.18653/v1/2022.naacl-main.285",
    pages = "3886--3893",
    abstract = "Recent work incorporates pre-trained word embeddings such as BERT embeddings into Neural Topic Models (NTMs), generating highly coherent topics. However, with high-quality contextualized document representations, do we really need sophisticated neural models to obtain coherent and interpretable topics? In this paper, we conduct thorough experiments showing that directly clustering high-quality sentence embeddings with an appropriate word selecting method can generate more coherent and diverse topics than NTMs, achieving also higher efficiency and simplicity.",
}
```

## Acknowledgement

The code is implemented using [OCTIS](https://github.com/MIND-Lab/OCTIS) and [BERTopic](https://github.com/MaartenGr/BERTopic).

## License

MIT
