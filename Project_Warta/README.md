# Warta, or not?

## OVERVIEW
This project is about predicting whether a website is about Warta as an insurance company, or something else. It contains scraper for getting website contents, as well as Jupyter notebook scripts for training and making predictions. I use ROBERTA as my main model and XGBoost for reference. In the presentation I look into how transformers, BERT and ROBERTA work and what are some more rudimentary approaches to this kind of problems.

## DATASET
I needed to generate my own dataset, I did it by manually labeling around 90 websites, they are available in file "websitesToScrape". To get the contents I used the scraper module from this repo. In order to generate a file needed for making predictions/training, run `scraper.py <file>` (file needs to be in the format same as websitesToScrape). The result file needs to be uploaded into the working directory of colab/jupyter notebook.

## RUNNING CODE
I used colab for training and making predictions. I used pretrained model from https://github.com/sdadas/polish-roberta. This model needs to be unzipped and then uploaded with scraping results into the colab/notebook (I did this using my drive, you may nedd to modify a few lines with file locations). Then run all the cells to get results and in case of training - saved model.

## REFERENCES
I based my code on article: [Link](https://medium.com/swlh/a-simple-guide-on-using-bert-for-text-classification-bbf041ac8d04) (For English BERT).
References for my presentation are placed at the end.

## Presentation
It is located in the "Presentation" folder.
