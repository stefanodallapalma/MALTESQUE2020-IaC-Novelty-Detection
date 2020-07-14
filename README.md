# MALTESQUE2020-IaC-Novelty-Detection
Replication package for the paper *"Singling the Odd Ones Out: A Novelty Detection Approach to Find Defects in Infrastructure-as-Code"*.

The dataset and the Machine-Learning scripts for Novelty Detection can be found on [Kaggle](https://www.kaggle.com/stefadp/ansiblenoveltydetection).

The original dataset can be found on [Zenodo](https://zenodo.org/record/3906023#.Xw29y3UzaV4).

**Repository structure**

Repository <br>
&emsp;|-data/ <br> 
&emsp;&emsp;|- [isoforest.json](https://www.kaggle.com/stefadp/isolation-forest): output for the IsolationForest model validation.  <br> 
&emsp;&emsp;|- [localoutlier.json](https://www.kaggle.com/stefadp/local-outlier-factor): output for the LocalOutlierFactor model validation. <br> 
&emsp;&emsp;|- [ocsvm.json](https://www.kaggle.com/stefadp/one-class-svm): output for the OneClassSVM model validation. <br> 
&emsp;&emsp;|- [rf.json](https://www.kaggle.com/stefadp/random-forest): output for the RandomForest model validation.

&emsp;|-plots/ <br> 
&emsp;&emsp;|- auc.png: boxplots of the four techniques' AUC-PR.   <br> 
&emsp;&emsp;|- mcc.png: boxplots of the four techniques' MCC.

&emsp;|-plots.py: script to generate plots.
