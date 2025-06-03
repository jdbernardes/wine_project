import pandas as pd

from kagglehub import load_dataset
from kagglehub import KaggleDatasetAdapter
from wine_project.settings import Settings


class DatasetLoader:
    
    _filepath:str = Settings().FILE
    
    def load_data(self, **kwargs) -> pd.DataFrame:
        return load_dataset(
            KaggleDatasetAdapter.PANDAS,
            Settings().DATASET,
            self._filepath,
            pandas_kwargs= {**kwargs}
        )

if __name__ == '__main__': #pragma: no cover
    df = DatasetLoader()
    kwargs = {
        "sep": ";"
    }
    data: pd.DataFrame = df.load_data(**kwargs)
    print(data.head())