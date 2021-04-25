For set enrichment analysis.

## Install

### FeatureSetEnrichment.py (this)

```sh
git clone https://github.com/KwatME/FeatureSetEnrichment.py
```

### Julia 1.5.4

### Julia packages

```sh
julia
```

```julia
using Pkg: add, develop, build

for name in (
    "IJulia",
    "DataFrames",
    "Pandas",
)

    add(name)

end

develop(; path="$(homedir())/code/jl/FeatureSetEnrichment.jl/")

build("IJulia")
```

## Use

See [examples](notebook/example.ipynb).

### Check out the [julia interface](https://github.com/KwatME/FeatureSetEnrichment.jl) and the [GSEA application](https://github.com/KwatME/GSEA.js).
