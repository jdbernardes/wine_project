import pandas as pd

from kagglehub import load_dataset
from kagglehub import KaggleDatasetAdapter
from wine_project.settings import Settings


class DatasetLoader:
    
    _filepath:str = Settings().FILE
    
    def load_data(self) -> pd.DataFrame:
        return load_dataset(
            KaggleDatasetAdapter.PANDAS,
            Settings().DATASET,
            self._filepath
        )

if __name__ == '__main__':
    df = DatasetLoader()
    data: pd.DataFrame = df.load_data()
    print(data.head())