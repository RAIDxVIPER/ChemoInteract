"""Example with DeepDDS."""

from chemointeract import pipeline
from chemointeract.data import DrugCombDB
from chemointeract.models import DeepDDS


def main():
    """Train and evaluate the DeepDDS model."""
    dataset = DrugCombDB()
    model = DeepDDS(
        context_channels=dataset.context_channels,
    )
    results = pipeline(
        dataset=dataset,
        model=model,
        batch_size=5120,
        epochs=10,
        context_features=True,
        drug_features=True,
        drug_molecules=True,
    )
    results.summarize()


if __name__ == "__main__":
    main()