import os
from dotenv import load_dotenv
from src.pipeline import SalesPipeline
from src.utils.logger import setup_logger


def main():
    """
    Main function: for tp2 (ETL pipeline)
    """

    # Configuration
    load_dotenv()
    logger = setup_logger('Sales_ETL', 'logs/etl.log')

    config = {
        'csv_path': 'data/raw/ventes.csv',
        'api_base_url': 'https://jsonplaceholder.typicode.com',
        'weather_api_key': os.getenv('OPENWEATHER_API_KEY'),
        'output_path': 'data/output/rapport_ventes.xlsx'
    }

    # Exécuter pipeline
    pipeline = SalesPipeline(config, logger)
    pipeline.run()


if __name__ == '__main__':
    main()