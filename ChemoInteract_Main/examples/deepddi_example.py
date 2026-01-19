"""Example with DeepDDI."""

from chemointeract import pipeline
from chemointeract.data import DrugbankDDI
from chemointeract.models import DeepDDI


def main():
    """Train and evaluate the DeepSynergy model."""
    dataset = DrugbankDDI()
    model = DeepDDI(drug_channels=dataset.drug_channels, hidden_layers_num=2)
    results = pipeline(
        dataset=dataset,
        model=model,
        batch_size=5120,
        epochs=100,
        context_features=False,
        drug_features=True,
        drug_molecules=False,
        metrics=[
            "roc_auc",
        ],
    )
    results.summarize()


if __name__ == "__main__":
    main()