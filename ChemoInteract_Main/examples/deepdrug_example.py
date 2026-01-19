"""Example with DeepDrug."""

from chemointeract import pipeline
from chemointeract.data import DrugCombDB
from chemointeract.models import DeepDrug


def main():
    """Train and evaluate the DeepDrug model."""
    dataset = DrugCombDB()
    model = DeepDrug()
    results = pipeline(
        dataset=dataset,
        model=model,
        optimizer_kwargs=dict(lr=0.001),
        batch_size=1024,
        epochs=20,
        context_features=False,
        drug_features=True,
        drug_molecules=True,
    )
    results.summarize()


if __name__ == "__main__":
    main()