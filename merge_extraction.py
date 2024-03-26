import logging
import urllib.request
from datetime import datetime, timedelta

class Extract_Merge:
    def __init__(self):
        self.FONTE = 'MERGE'

    def run(self):
        # {0}Ano  ///  {1}Mês  ///  {2}AnoMêsDia
        link_model = 'http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY/{}/{}/MERGE_CPTEC_{}.grib2'

        data_begin = "20231114" #"<data ano/mes/dia>"
        data_end = "20231231" #"<data ano/mes/dia>"
        data_begin = datetime.strptime(data_begin, '%Y%m%d')
        data_end = datetime.strptime(data_end, '%Y%m%d')

        data_inside_while = data_begin

        while data_inside_while <= data_end:
            year_month_day = data_inside_while.strftime("%Y%m%d")
            year = data_inside_while.strftime("%Y")
            month = data_inside_while.strftime("%m")

            file_name = 'MERGE_CPTEC_{}.grib2'.format(year_month_day)
            file_path = 'raw/' + file_name

            print(f"Extraindo o arquivo da data: {year_month_day}")
            download_link = link_model.format(year, month, year_month_day)

            try:
                urllib.request.urlretrieve(download_link, file_path) 
                # Log success
                logging.info(f"Arquivo: {file_name} extraido com sucesso")
            except Exception as e:
                # Log failure
                logging.error(f"Falha ao extrair o arquivo {file_name}: {str(e)}")

            data_inside_while += timedelta(days=1)


if __name__ == '__main__':
    #root = print(os.getcwd())

    # Configuring the logging module
    logging.basicConfig(filename='logs/merge_extraction.log', level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    extract_merge = Extract_Merge()
    extract_merge.run()

    