"""Example with DeepSynergy."""

from chemointeract import pipeline
from chemointeract.data import DrugCombDB
from chemointeract.models import DeepSynergy


def main():
    """Train and evaluate the DeepSynergy model."""
    dataset = DrugCombDB()
    model = DeepSynergy(
        context_channels=dataset.context_channels,
        drug_channels=dataset.drug_channels
    )
    
    results = pipeline(
        dataset=dataset,
        model=model,
        batch_size=5120,
        epochs=100,
        context_features=True,
        drug_features=True,
        drug_molecules=False,
        metrics=[
            "roc_auc",
        ],
    )
    
    results.summarize()


if __name__ == "__main__":
    main()