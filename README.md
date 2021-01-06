Module for set enrichment analysis.

## Install

Must install (this) sea, julia, and some julia packages.

### sea

```sh
git clone https://github.com/KwatME/sea

pip install --editable sea/
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

add(url="https://github.com/KwatME/SEA.jl")

add("PyCall")

add("DataFrames")

add("Pandas")
```

## Use

See [examples](notebook/example.ipynb).

#### Check out the [julia interface](https://github.com/KwatME/SEA.jl) and the [GSEA application](https://github.com/KwatME/gsea).
