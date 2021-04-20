For set enrichment analysis.

## Install

Must install (this) FeatureSetEnrichment.py, julia, and some julia packages.

### sea

```sh
pip install git+https://github.com/KwatME/FeatureSetEnrichment.py
```

### julia

```sh
brew install julia
```

### julia packages

```sh
julia
```

```julia
using Pkg: add

add(url="https://github.com/KwatME/FeatureSetEnrichment.jl")

add("PyCall")

add("DataFrames")

add("Pandas")
```

## Use

See [examples](notebook/example.ipynb).

### Check out the [julia interface](https://github.com/KwatME/FeatureSetEnrichment.jl) and the [GSEA application](https://github.com/KwatME/GSEA.js).
