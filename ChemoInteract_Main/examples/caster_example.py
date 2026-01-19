"""Example with CASTER."""

from chemointeract import pipeline
from chemointeract.data import DrugCombDB
from chemointeract.loss import CASTERSupervisedLoss
from chemointeract.models import CASTER


def main():
    """Train and evaluate the CASTER model."""
    dataset = DrugCombDB()
    model = CASTER(drug_channels=dataset.drug_channels)
    results = pipeline(
        dataset=dataset,
        model=model,
        loss_cls=CASTERSupervisedLoss,
        batch_size=5120,
        epochs=1,
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