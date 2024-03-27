# Machine Learning Benchmarking of flow rate prediction (regression)

* The goal was to develop a weekly and monthly benchmarking of different ML algorithms to predict Itaipu Hydroelectric Plant flow rate with time series data. Recurrent Neural Networks (RNN) such as Long short-term memory (LSTM) and Gated recurrent unit (GRU), which are known from the literature as neural networks specialized in time series forecasting, achieved the best overall scores in the benchmarking selected metrics. 

* I did develop the end to end solution for this benchmarking. Beginning by collecting the precipitation geospacial data from INPE web API (http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY/) developing a python data pipeline (merge_extraction.py) and then clipping the raw extracted data with Itaipu hydrographic basin shapefile (merge_processing_prec_sum_clipped_itaipu_incremental.py) so we have the daily precipitation data in our coordinates of interest. We finally sum the precipitation data over all the selected coordinates for each time step.

* Then, we collected the daily flow rate from each hydroelectric plant in the ONS brazilian system and filtered by the Itaipu plant, and now we have all the necessary variables to perform a methodology and evaluate it by the benchmarking results.

* In this project, we're working with traditional ML algorithms (basic ones, like Decision Tree, Linear Regression and Random Forest, but also powerful ones, such as XGBoost) and Recurrent Neural Networks (RNN), like mentioned, such as Long short-term memory (LSTM) and Gated recurrent unit (GRU).   

![Alt text](/figures/monthly/history_vazao_vs_precBacia.png)
* Hystorical data from 2001-2021 of Itaipu flow rate x hydrographic basin precipitation sum aggregation


## Plots for Monthly prediction of flow rate in Itaipu Hydroelectric Plant

![Alt text](/figures/monthly/r2_monthly.png)


![Alt text](/figures/monthly/rmse_monthly.png)


![Alt text](/figures/monthly/pred_lstm_n=8_f=1_40_50_60_sigmoid_3hl_.png)


![Alt text](/figures/monthly/disp_lstm_n=8_f=1_40_50_60_sigmoid_3hl_.png)


## Plots for Weekly prediction of flow rate in Itaipu Hydroelectric Plant

![Alt text](/figures/weekly/gru_1.png)


![Alt text](/figures/weekly/gru_3.png)


![Alt text](/figures/weekly/lstm_series_n=5_f=1.png)


![Alt text](/figures/weekly/lstm_disp_n=5_f=1.png)











