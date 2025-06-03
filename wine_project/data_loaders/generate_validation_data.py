import pandas as pd
from wine_project.data_loaders.dataset_loader import DatasetLoader
from wine_project.settings import Settings
from sklearn.model_selection import train_test_split


class ValidationData:

    _SEED = Settings().SEED
    _validation_path = "wine_project/data_loaders"

    def generate_csv(self, df:pd.DataFrame) -> None:
        db_data, valid_data = train_test_split(
            df,
            random_state=self._SEED,
            stratify=df['quality'],
            test_size= Settings().VALID_SIZE
        )
        print(valid_data.head())
        valid_data.to_csv(
            f'{self._validation_path}/validation_data.csv', index=False)
        return db_data


if __name__ == '__main__':
    dl = DatasetLoader()
    vd = ValidationData()
    kwargs = {
    "sep": ";"
    }
    df: pd.DataFrame = dl.load_data(**kwargs)
    vd.generate_csv(df)

