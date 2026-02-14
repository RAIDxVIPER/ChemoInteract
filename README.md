<p align="center">
  <img src="https://img.shields.io/badge/version-0.1.0-8b5cf6?style=for-the-badge&labelColor=0a0a0f" alt="Version">
  <img src="https://img.shields.io/badge/python-3.8+-3b82f6?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a0f" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-2.0+-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white&labelColor=0a0a0f" alt="PyTorch">
  <img src="https://img.shields.io/badge/license-MIT-10b981?style=for-the-badge&labelColor=0a0a0f" alt="License">
</p>

<h1 align="center">⚗️ ChemoInteract</h1>

<p align="center">
  <strong>A Unified Deep Learning Framework for Drug-Drug Interaction, Polypharmacy Side-Effect, and Drug Synergy Prediction</strong>
</p>

<p align="center">
  <em>11 state-of-the-art models · 5 benchmark datasets · 1 unified pipeline</em>
</p>

---

## 🧬 What is ChemoInteract?

**ChemoInteract** is a deep learning library built on top of **PyTorch** that provides a standardized, modular framework for predicting interactions between drug pairs. It addresses three critical problems in computational pharmacology:

| Problem | Description | Why It Matters |
|---------|-------------|----------------|
| **Drug-Drug Interaction (DDI)** | Predicting whether two drugs will interact when taken together | Prevents adverse reactions in patients taking multiple medications |
| **Polypharmacy Side Effects** | Identifying side effects caused by drug combinations | Improves safety for patients on complex drug regimens |
| **Drug Synergy** | Predicting whether drug combinations produce enhanced therapeutic effects | Accelerates discovery of effective combination therapies (e.g., cancer treatment) |

Instead of reimplementing each model from scratch, ChemoInteract offers a **single unified pipeline** where you can swap models, datasets, loss functions, and metrics with a single parameter change — enabling rapid benchmarking and experimentation.

---

## ✨ Key Features

- 🧠 **11 Deep Learning Models** — From fully connected networks (DeepSynergy, DeepDDI) to graph neural networks (DeepDDS, GCNBMP, MRGNN) and attention mechanisms (MHCADDI, SSI-DDI)
- 📊 **5 Benchmark Datasets** — DrugCombDB, DrugComb, TwoSides, DrugbankDDI, and OncoPolyPharmacology with automatic downloading and preprocessing
- ⚡ **Unified Pipeline** — One standardized `pipeline()` function handles data loading, batching, training, evaluation, and result export
- 🔌 **Modular Architecture** — Plug-and-play design: swap any model, dataset, optimizer, or loss function independently
- 🖥️ **GPU & CPU Support** — Automatic CUDA detection with seamless fallback to CPU
- 📈 **Built-in Metrics** — ROC-AUC, MSE, MAE with extensible metric registration
- 💾 **Result Persistence** — Save trained models, predictions, and evaluation metrics to disk



---

## 🧠 Models

ChemoInteract implements **11 deep learning architectures** spanning three categories:

### Fully Connected (FC) Models

| Model | Paper | Description | Inputs |
|-------|-------|-------------|--------|
| **DeepSynergy** | [Preuer et al., 2018](https://doi.org/10.1093/bioinformatics/btx806) | Multi-layer perceptron for anti-cancer drug synergy prediction using chemical and genomic features | Drug features + Context features |
| **DeepDDI** | — | Deep neural network for drug-drug interaction prediction based on structural similarity profiles | Drug features |
| **MatchMaker** | — | Sub-network architecture with individual and combined drug modeling for synergy prediction | Drug features + Context features |

### Graph Neural Network (GNN) Models

| Model | Paper | Description | Inputs |
|-------|-------|-------------|--------|
| **DeepDDS** | [Wang et al., 2021](http://arxiv.org/abs/2107.02467) | GCN with attention for synergistic drug combination prediction using molecular graphs and cell line features | Drug molecules + Context features |
| **DeepDrug** | — | Graph convolutions on molecular structures for interaction prediction | Drug molecules |
| **CASTER** | [Huang et al., 2020](https://doi.org/10.1609/aaai.v34i01.5412) | Chemical substructure representation with dictionary learning; uses a custom supervised loss function | Drug features (Custom Loss) |
| **GCNBMP** | — | Graph convolutional network with bilinear message passing between molecular graphs | Drug molecules |
| **EPGCNDS** | — | Enhanced pairwise graph convolutional network for drug synergy | Drug molecules + Context features |
| **MRGNN** | — | Multi-resolution graph neural network for molecular interaction prediction | Drug molecules |

### Attention-Based Models

| Model | Paper | Description | Inputs |
|-------|-------|-------------|--------|
| **MHCADDI** | [Deac et al., 2019](http://arxiv.org/abs/1905.00534) | Multi-head co-attention with internal message passing for multi-relational DDI prediction | Drug molecules |
| **SSI-DDI** | — | Substructure-substructure interaction for DDI prediction using learned molecular substructures | Drug molecules |

### Model Capability Matrix

| Model | Type | Drug Features | Drug Molecules | Context Features | Custom Loss |
|:------|:----:|:---:|:---:|:---:|:---:|
| DeepSynergy | FC | ✅ | ❌ | ✅ | ❌ |
| DeepDDI | FC | ✅ | ❌ | ❌ | ❌ |
| MatchMaker | FC | ✅ | ❌ | ✅ | ❌ |
| DeepDDS | GNN | ❌ | ✅ | ✅ | ❌ |
| DeepDrug | GNN | ❌ | ✅ | ❌ | ❌ |
| CASTER | GNN | ✅ | ❌ | ❌ | ✅ |
| GCNBMP | GNN | ❌ | ✅ | ❌ | ❌ |
| EPGCNDS | GNN | ❌ | ✅ | ✅ | ❌ |
| MRGNN | GNN | ❌ | ✅ | ❌ | ❌ |
| MHCADDI | ATTN | ❌ | ✅ | ❌ | ❌ |
| SSI-DDI | ATTN | ❌ | ✅ | ❌ | ❌ |

> **Drug Features** = Pre-computed chemical fingerprints/descriptors  
> **Drug Molecules** = Molecular graph representations (atoms, bonds, structure)  
> **Context Features** = Biological context such as cell line gene expression profiles

---

## 📊 Datasets

ChemoInteract ships with **5 benchmark datasets** that auto-download and cache on first use:

| Dataset | Type | Task | Source | Loader |
|---------|------|------|--------|--------|
| **DrugCombDB** | Remote | Drug Synergy | [drugcombdb.denglab.org](http://drugcombdb.denglab.org) | `DrugCombDB()` |
| **DrugComb** | Remote | Drug Synergy | [drugcomb.fimm.fi](https://drugcomb.fimm.fi/) | `DrugComb()` |
| **TwoSides** | Remote | Side Effects (Polypharmacy) | [tatonettilab.org/offsides](http://tatonettilab.org/offsides/) | `TwoSides()` |
| **DrugbankDDI** | Remote | Drug-Drug Interaction | [DrugBank](https://www.pnas.org/content/115/18/E4304) | `DrugbankDDI()` |
| **OncoPolyPharmacology** | Local/TDC | Oncology Drug Synergy | [O'Neil et al., 2016](https://doi.org/10.1158/1535-7163.MCT-15-0843) | `OncoPolyPharmacology()` |

Each dataset provides:
- **Drug Features** — Chemical fingerprints/descriptors per drug
- **Context Features** — Biological context vectors (e.g., cell line gene expression)
- **Labeled Triples** — `(drug_1, drug_2, context)` → `label` pairs for training and evaluation

---

## 🏗️ Architecture Overview

ChemoInteract follows a clean, modular design with four major stages:

```
┌─────────────────┐     ┌───────────────────┐     ┌────────────────┐     ┌──────────────────┐
│   Data Loading   │────▶│  Batch Generation  │────▶│ Model Training │────▶│ Evaluation &     │
│                 │     │                   │     │                │     │ Results          │
│ • DatasetLoader │     │ • BatchGenerator  │     │ • Model        │     │ • ROC-AUC        │
│ • DrugFeatureSet│     │ • DrugPairBatch   │     │ • Optimizer    │     │ • MSE / MAE      │
│ • ContextSet    │     │ • Train/Test Split│     │ • Loss Function│     │ • Result.save()  │
│ • LabeledTriples│     │                   │     │ • GPU/CPU      │     │ • Result.summary │
└─────────────────┘     └───────────────────┘     └────────────────┘     └──────────────────┘
```

### Core Components

| Component | Module | Purpose |
|-----------|--------|---------|
| `DatasetLoader` | `chemointeract.data` | Abstract base class for all datasets; handles data retrieval and preprocessing |
| `BatchGenerator` | `chemointeract.data` | Creates iterable batches of drug pairs with their features |
| `DrugPairBatch` | `chemointeract.data` | Data container holding drug features, molecular graphs, context features, and labels for a batch |
| `LabeledTriples` | `chemointeract.data` | Stores `(drug_1, drug_2, context, label)` tuples with train/test splitting |
| `Model` | `chemointeract.models` | Abstract base class for all prediction models (`nn.Module` subclass) |
| `pipeline()` | `chemointeract.pipeline` | Orchestrator function combining all components into a complete train/eval workflow |
| `Result` | `chemointeract.pipeline` | Dataclass holding trained models, predictions, losses, timing, and metric results |

---

---

## 📖 Citation

If you use ChemoInteract in your research, please cite:

```bibtex
@software{chemointeract2026,
  title     = {ChemoInteract: A Unified Deep Learning Framework for Drug-Drug Interaction Prediction},
  author    = {Ronit},
  year      = {2026},
  version   = {0.1.0},
  url       = {https://github.com/your-username/ChemoInteract}
}
```

### Referenced Papers

<details>
<summary>Click to expand the complete list of papers implemented in ChemoInteract</summary>

| Model | Citation |
|-------|----------|
| DeepSynergy | Preuer, K., *et al.* (2018). *DeepSynergy: predicting anti-cancer drug synergy with Deep Learning*. Bioinformatics, 34(9), 1538–1546. |
| DeepDDS | Wang, J., *et al.* (2021). *DeepDDS: deep graph neural network with attention mechanism to predict synergistic drug combinations*. arXiv:2107.02467. |
| CASTER | Huang, K., *et al.* (2020). *CASTER: Predicting drug interactions with chemical substructure representation*. AAAI 2020, 702–709. |
| MHCADDI | Deac, A., *et al.* (2019). *Drug-Drug Adverse Effect Prediction with Graph Co-Attention*. arXiv:1905.00534. |
| OncoPolyPharmacology | O'Neil, J., *et al.* (2016). *An Unbiased Oncology Compound Screen to Identify Novel Combination Strategies*. Molecular Cancer Therapeutics, 15(6), 1155–1162. |

</details>

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>Built with ❤️ using PyTorch, TorchDrug, and scikit-learn</strong>
  <br>
  <sub>ChemoInteract v0.1.0</sub>
</p>
