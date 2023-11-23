import pickle
import pandas as pd
import os

from datasets import load_dataset


def save_result(format='pickle'):
    def decorator(func):
        def wrapper(*args, **kwargs):

            file_path = f"{args[-1]}.pkl"

            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    if format == 'pickle':
                        result = pickle.load(file)
                    elif format == 'csv':
                        result = pd.read_csv(file)
                    else:
                        raise ValueError(f"Niewspierany format: {format}")
                print(f"Wynik wczytany z pliku: {file_path}")
            else:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                result = func(*args, **kwargs)
                with open(file_path, 'wb') as file:
                    if format == 'pickle':
                        pickle.dump(result, file)
                    elif format == 'csv':
                        result.to_csv(file, index=False)
                    else:
                        raise ValueError(f"Niewspierany format: {format}")
                print(f"Wynik zapisany do pliku: {file_path}")
            return result

        return wrapper

    return decorator


@save_result(format='pickle')
def load_and_process_dataset(dataset_path):
    dataset = load_dataset(dataset_path)
    df = pd.DataFrame(dataset['train'])
    return df


if __name__ == '__main__':
    df = load_and_process_dataset("imodels/credit-card")
    df = load_and_process_dataset("imodels/credit-card")
    df = load_and_process_dataset("imodels/compas-recidivism")
    # print(df)
