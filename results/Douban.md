# Experimental setting

**Source domain dataset**: [Douban-Books](https://www.douban.com/)

**Target domain dataset**: [Douban-Music](https://www.douban.com/)

**Evaluation**: all users in target dataset, ratio-based 8:1:1, full sort

**Metrics**: Recall, Precision, NDCG, MRR, Hit

**Topk**: 10, 20, 50

**Properties**:
```yaml
field_separator: "\t"
source_domain:
  dataset: DoubanBook
  data_path: 'datasets/'
  USER_ID_FIELD: user_id
  ITEM_ID_FIELD: item_id
  RATING_FIELD: rating
  TIME_FIELD: timestamp
  NEG_PREFIX: neg_
  LABEL_FIELD: label
  load_col:
    inter: [user_id, item_id, rating]
  user_inter_num_interval: "[5,inf)"
  item_inter_num_interval: "[5,inf)"
  val_interval:
    rating: "[3,inf)"
  drop_filter_field: True

target_domain:
  dataset: DoubanMovie
  data_path: 'datasets/'
  USER_ID_FIELD: user_id
  ITEM_ID_FIELD: item_id
  RATING_FIELD: rating
  TIME_FIELD: timestamp
  NEG_PREFIX: neg_
  LABEL_FIELD: label
  load_col:
    inter: [user_id, item_id, rating]
  user_inter_num_interval: "[5,inf)"
  item_inter_num_interval: "[5,inf)"
  val_interval:
    rating: "[3,inf)"
  drop_filter_field: True

epochs: 500
train_batch_size: 4096
eval_batch_size: 409600
valid_metric: NDCG@10


```
For fairness, we restrict users' and items' embedding dimension as following. Please adjust the name of the corresponding args of different models.
```yaml
embedding_size: 64
```

# Dataset Statistics
| Dataset      | #Users | #items | #Interactions | Sparsity |
|--------------|--------|--------|---------------|----------|
| Douban-Book  | 18085  | 33067  | 809248        | 99.86%   |
| Douban-Movie | 22041  | 25802  | 2552305       | 99.55%   |

Number of Overlapped User: 15434

Number of Overlapped Item: 0

# Evaluation Results

| Method      | Recall@10 | Precesion@10 | NDCG@10 | MRR@10 | Hit@10 |
|-------------|-----------|--------------|---------|--------|--------|
| **CoNet**   | 0.1034    | 0.058        | 0.1011  | 0.1538 | 0.3224 |
| **CLFM**    | 0.0885    | 0.0515       | 0.0861  | 0.1328 | 0.2948 |
| **DTCDR**   | 0.1011    | 0.0609       | 0.102   | 0.1574 | 0.3259 |
| **DeepAPF** | 0.067     | 0.0471       | 0.0737  | 0.1218 | 0.2626 |
| **BiTGCF**  | 0.1124    | 0.063        | 0.109   | 0.1651 | 0.3485 |
| **CMF**     | 0.0976    | 0.0588       | 0.0985  | 0.1531 | 0.3246 |
| **EMCDR**   | 0.1169    | 0.067        | 0.1169  | 0.177  | 0.3568 |
| **NATR**    |           |              |         |        |        |
| **SSCDR**   |           |              |         |        |        |
| **DCDCSR**  |           |              |         |        |        |

| Method      | Recall@20 | Precesion@20 | NDCG@20 | MRR@20 | Hit@20 |
|-------------|-----------|--------------|---------|--------|--------|
| **CoNet**   | 0.1581    | 0.0477       | 0.1108  | 0.1606 | 0.42   |
| **CLFM**    | 0.1393    | 0.0434       | 0.096   | 0.1396 | 0.3937 |
| **DTCDR**   | 0.16      | 0.0502       | 0.1121  | 0.1642 | 0.4248 |
| **DeepAPF** | 0.1063    | 0.0393       | 0.0799  | 0.1277 | 0.3481 |
| **BiTGCF**  | 0.1734    | 0.0522       | 0.1207  | 0.1721 | 0.4503 |
| **CMF**     | 0.1521    | 0.0489       | 0.1086  | 0.1598 | 0.4216 |
| **EMCDR**   | 0.1793    | 0.0545       | 0.1276  | 0.1838 | 0.4564 |
| **NATR**    |           |              |         |        |        |
| **SSCDR**   |           |              |         |        |        |
| **DCDCSR**  |           |              |         |        |        |

| Method      | Recall@50 | Precesion@50 | NDCG@50 | MRR@50 | Hit@50 |
|-------------|-----------|--------------|---------|--------|--------|
| **CoNet**   | 0.2687    | 0.0351       | 0.1332  | 0.1653 | 0.5653 |
| **CLFM**    | 0.2433    | 0.033        | 0.1182  | 0.1442 | 0.5372 |
| **DTCDR**   | 0.2699    | 0.0368       | 0.134   | 0.1687 | 0.5662 |
| **DeepAPF** | 0.1943    | 0.0301       | 0.0977  | 0.1318 | 0.4771 |
| **BiTGCF**  | 0.2891    | 0.0387       | 0.1452  | 0.1766 | 0.5903 |
| **CMF**     | 0.262     | 0.0368       | 0.132   | 0.1643 | 0.561  |
| **EMCDR**   | 0.2936    | 0.0393       | 0.1504  | 0.1883 | 0.5943 |
| **NATR**    |           |              |         |        |        |
| **SSCDR**   |           |              |         |        |        |
| **DCDCSR**  |           |              |         |        |        |

# Hyper-parameters

| Method      | Best hyper-parameters                                                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CoNet**   | learning_rate=0.005<br/>mlp_hidden_size=[64,32,16,8]<br/>reg_weight=0.01                                                                                                  |
| **CLFM**    | learning_rate=0.0005<br/>share_embedding_size=48<br/>alpha=0.1<br/>reg_weight=0.0001                                                                                      |
| **DTCDR**   | learning_rate=0.0001<br/>mlp_hidden_size=[64,64]<br/>dropout_prob=0.2<br/>alpha=0.1<br/>base_model=NeuMF                                                                  |
| **DeepAPF** | learning_rate=0.0005                                                                                                                                                      |
| **BiTGCF**  | learning_rate=0.0005<br/>n_layers=2<br/>concat_way=mean<br/>lambda_source=0.8<br/>lambda_target=0.8<br/>drop_rate=0.1<br/>reg_weight=0.01                                 |
| **CMF**     | learning_rate=0.0005<br/>lambda=0.9<br/>gamma=0.1<br/>alpha=0.1                                                                                                           |
| **EMCDR**   | learning_rate=0.001<br/>mapping_function=non_linear<br/>mlp_hidden_size=[64]<br/>overlap_batch_size=100<br/>reg_weight=0.01<br/>latent_factor_model=BPR<br/>loss_type=BPR |
| **NATR**    |                                                                                                                                                                           |
| **SSCDR**   |                                                                                                                                                                           |
| **DCDCSR**  |   