import pickle


class ExperimentSnapshot:

    def __init__(
        self,
        experiment_id,
        model_type,
        hyperparameters,
        metrics,
        timestamp
    ):
        self.experiment_id = experiment_id
        self.model_type = model_type
        self.hyperparameters = hyperparameters
        self.metrics = metrics
        self.timestamp = timestamp

    def get_best_metric(self, metric_name):
        return self.metrics[metric_name]


def save_experiment(snapshot, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(snapshot, file)


def load_experiment(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)



if __name__ == "__main__":

    exp = ExperimentSnapshot(
        experiment_id="EXP-2026-001",
        model_type="RandomForest",
        hyperparameters={
            "n_estimators": 100,
            "max_depth": 10
        },
        metrics={
            "accuracy": 0.942,
            "f1_score": 0.938
        },
        timestamp="2026-09-01 10:00:00"
    )

    
    save_experiment(exp, "experiment_01.pkl")

    
    restored_exp = load_experiment("experiment_01.pkl")

    print(restored_exp.experiment_id)
    print(restored_exp.model_type)
    print(restored_exp.hyperparameters)
    print(restored_exp.metrics)
    print(restored_exp.timestamp)

    print(
        restored_exp.get_best_metric("accuracy")
    )