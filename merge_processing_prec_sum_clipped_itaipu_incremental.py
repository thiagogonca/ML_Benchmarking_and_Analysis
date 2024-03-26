import geopandas as gpd
import xarray as xr
import regionmask 
import warnings
from datetime import datetime, timedelta
import logging
import csv

warnings.filterwarnings(action='ignore')
log_filename = "merge_processing_prec_sum_clipped_itaipu_incremental.log"

data_path = "../../data"
raw_merge_path = "merge/raw"
processed_merge_path = "merge/processed"

# Shapefile da Bacia Incremental de Itaipu
shapefilepath = f'{data_path}/basins/Itaipu_incremental/ItaipuInc/ItaipuInc.shp'

csv_file_name = "MERGE_PREC_SUM_ITAIPU_INCREMENTAL_DAILY.csv"
csv_file_path = f"{data_path}/{processed_merge_path}/{csv_file_name}"

data_begin = "20000602" #"<data ano/mes/dia>"
data_end = "20231231" #"<data ano/mes/dia>"

def extract_daily_prec_sum_from_clipped_ds(file_path):

    ds = xr.open_dataset(file_path, engine='cfgrib') 

    ds['longitude'] = ds['longitude'] - 360
    ds = ds.drop_vars('prmsl')
    mask = regionmask.mask_geopandas(gdf,ds.longitude, ds.latitude) 
    ds_masked = ds.where(mask==0)
    
    daily_prec_sum = ds_masked.prec.sum().values.item()

    return daily_prec_sum

if __name__ == '__main__':

    # Configuring the logging module
    logging.basicConfig(filename=f'logs/{log_filename}', level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    data_begin = datetime.strptime(data_begin, '%Y%m%d')
    data_end = datetime.strptime(data_end, '%Y%m%d')

    gdf = gpd.read_file(shapefilepath)

    data = data_begin
    while data <= data_end:
        year_month_day = data.strftime("%Y%m%d")

        file_name = 'MERGE_CPTEC_{}.grib2'.format(year_month_day)
        file_path = f"{data_path}/{raw_merge_path}/{file_name}"

        print(f"Processando o arquivo {file_name} da data: {year_month_day}")

        try:
            daily_prec_sum = extract_daily_prec_sum_from_clipped_ds(file_path)

            with open(csv_file_path, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([data, daily_prec_sum])

            # Log success
            logging.info(f"Arquivo {file_name} processado com êxito")
        except Exception as e:
            # Log failure
            logging.error(f"Falha ao processar o arquivo {file_name}: {str(e)}")

        data += timedelta(days=1)