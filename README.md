# Machine Learning Benchmarking of flow rate prediction (regression)

* The goal was to develop a weekly and monthly benchmarking of different ML algorithms to predict Itaipu Hydroelectric Plant flow rate with time series data. Recurrent Neural Networks (RNN) such as Long short-term memory (LSTM) and Gated recurrent unit (GRU) achieved the best overall scores in the becnhmarking selected metrics. 

* I did develop the end to end solution for this benchmarking. Beginning by collecting the precipitation geospacial data from INPE web API (http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY/) developing a python data pipeline (merge_extraction.py) and then clipping the raw extracted data with Itaipu hydrographic basin shapefile (merge_processing_prec_sum_clipped_itaipu_incremental.py) so we finally have the daily precipitation data in our region of interest. 

* Then, we collected the daily flow rate from each hydroelectric plant in the ONS brazilian system and filtered by the Itaipu plant. 

* In the end, we have all the necessary variables to perform a methodology and evaluate it by the benchmarking results.

 traditional Machine Learning algorithms (such as Decision Tree, Linear Regression, Random Forest)

![Alt text](/figures/monthly/history_vazao_vs_precBacia.png)
* Flow rate x hydrographic basin precipitation 


## Monthly prediction of flow rate in Itaipu Hydroelectric Plant

![Alt text](/figures/monthly/r2_monthly.png)
* bla bla

![Alt text](/figures/monthly/rmse_monthly.png)
* outro bla bla bla

![Alt text](/figures/monthly/pred_lstm_n=8_f=1_40_50_60_sigmoid_3hl_.png)
* mais um bla bla bla

![Alt text](/figures/monthly/disp_lstm_n=8_f=1_40_50_60_sigmoid_3hl_.png)
* mais outro bla bla bla

## Weekly prediction of flow rate in Itaipu Hydroelectric Plant

![Alt text](/figures/weekly/lstm_series_n=5_f=1.png)
* bla bla 1

![Alt text](/figures/weekly/gru_1.png)
* bla bla 2

![Alt text](/figures/weekly/gru_3.png)
* bla bla 3

![Alt text](/figures/weekly/lstm_disp_n=5_f=1.png)
* bla bla 4










