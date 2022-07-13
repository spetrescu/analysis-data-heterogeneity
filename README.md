# exploratory-analysis-data-heterogeneity
This repository contains an analysis of logs heterogeneity. Specifically, we analyze a variety of datasets, and asses their heterogeneity by considering three metrics, namely __unique number of words__, __unique number of characters__, and __unique number of log lines’ character length__. <br>
<img width="270" alt="data_heterogeneity" src="https://user-images.githubusercontent.com/60047427/178700942-cab47217-15f2-4f5a-ae54-f5a5750b01aa.png">
<img width="270" alt="data_heterogeneity_2" src="https://user-images.githubusercontent.com/60047427/178722374-fa9552de-11e8-4126-8c68-f6f1e916c368.png">
<img width="267" alt="data_heterogeneity_3" src="https://user-images.githubusercontent.com/60047427/178722379-eaa18fcb-298f-4128-a315-4f60a9e6fc60.png">





## Datasets
For the analysis, we used the following datasets:
1. `Apache` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/Apache)
2. `BGL` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/BGL)
3. `HDFS` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/HDFS)
4. `HealthApp` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/HealthApp)
5. `HPC` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/HPC)
6. `Mac` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/Mac)
7. `OpenStack` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/OpenStack)
8. `Spark` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/Spark)
9. `Windows` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/Windows)
10. `Combined` [link](https://github.com/spetrescu/are-log-parsers-ready-for-prime-time/tree/main/data/refactored_logs/Combined_Dataset)
11. `Industry` not publicly available
12. `Entity` [link](https://github.com/spetrescu/entity-dataset)

## Reproduce experiments
Reproduce experiments by running `python measure_statistics.py` <br>
Under `data` the log data can be found.
