import logging
import os
import pandas as pd

# from pipeline.pipeline_base import ETLPipeline        # ETLPipeline générique déjà existante
from pipeline.pipeline_base import ETLPipeline
from extractors.extractors import CSVExtractor
from config.settings import settings
from utils.logger import setup_logger


class CsvPipeline(ETLPipeline):
    """
    Pipeline ETL concret basé sur une API publique (JSONPlaceholder).

    Étapes :
    1) EXTRACT  : appel HTTP GET sur /posts
    2) TRANSFORM:
         - nettoyage (doublons, espaces, colonnes vides)
         - validation des colonnes essentielles
         - enrichissement (longueur du titre)
    3) LOAD     : écriture en Excel dans data/output/posts_api.xlsx
    """

    def _extract(self) -> pd.DataFrame:
        """Extraction des posts depuis le fichier csv data/raw/ventes.csv."""

        csv_path = settings.PATH_CSV_VENTES

        df = pd.read_csv(csv_path)

        return df
    
    def _transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Nettoie, valide et enrichit les données issues de l'API."""

        # 1) Nettoyage générique (doublons, colonnes vides, trim des strings)
        # Nettoyage : doublons, valeurs manquantes
        df_clean = self.transformer.clean(data)

        # 2) Validation de la présence de colonnes clés
        required_cols = ["date", "produit_id", "quantite", "prix_unitaire", "client_id"]
        self.transformer.validate(df_clean, required_cols)

        # 3) Enrichissement : ajout d'une colonne "title_length" ajouter nom produit, catégorie
        produits = {
            1: {'nom': 'Souris', 'categorie': 'Périphérique'},
            2: {'nom': 'Clavier', 'categorie': 'Périphérique'},
            3: {'nom': 'Câble USB', 'categorie': 'Accessoire'},
            4: {'nom': 'Webcam', 'categorie': 'Périphérique'},
            5: {'nom': 'Casque', 'categorie': 'Audio'}
        }


        def add_product_name_and_vategory(df: pd.DataFrame, products: dict) -> pd.DataFrame:
            for product in products:
                df['name'] = products[product]['nom']
                df['category'] = products[product]['categorie']
            return df

        df_enriched = self.transformer.enrich(df_clean, add_product_name_and_vategory(df_clean, produits))
        return df_enriched

    
    def _load(self, data: pd.DataFrame) -> None:
        """Charge les données transformées dans un fichier Excel."""

        # Dossier de sortie depuis la config
        output_dir = settings.PATH_CSV_VENTES_OUTPUT
        os.makedirs(output_dir, exist_ok=True)

        # Nom du fichier de sortie Excel
        output_file = os.path.join(output_dir, "posts_api.xlsx")

        # Utilisation du DataLoader pour écrire en Excel
        self.loader.load_excel(
            df=data,
            filepath=output_file,
            sheet_name="PostsAPI"
        )

        # À la fin, on aura un fichier data/output/posts_api.xlsx

# == Test in this file:
if __name__ == "__main__":
    from src.utils.logger import setup_logger

    print('\n==> in pipeline_csv_ventes.py')

    logger = setup_logger('Sales_ETL', '../logs/etl.log')

    eTLPipeline = ETLPipeline(logger)

    csvPipeline = CsvPipeline(eTLPipeline)

    ##== _extract
    df  = csvPipeline._extract()
    print(df)

    ##== _transform
    df_transformed = csvPipeline._transform(df)
    # print(df_transformed)


