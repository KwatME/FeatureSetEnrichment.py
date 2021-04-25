## Install

### FeatureSetEnrichment.py (this)

```sh
python3 -m pip install git+https://github.com/KwatME/FeatureSetEnrichment.py
```

### Julia 1.5.4 (PyCall and pyjulia are not compatible with 1.6 yet)

### Julia packages

```sh
cd ~/code/jl/ &&

git clone https://github.com/KwatME/FeatureSetEnrichment.jl &&

git clone https://github.com/KwatME/GCTGMT.jl
```

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

    add(; name=name)

end

for path in (
    "$(homedir())/code/jl/FeatureSetEnrichment.jl/",
    "$(homedir())/code/jl/GCTGMT.jl/",
)

    develop(; path=path)

end

build("IJulia")
```

## Use

See [examples](notebook/example.ipynb).

---

Check out the [julia version](https://github.com/KwatME/FeatureSetEnrichment.jl) and the [desktop application](https://github.com/KwatME/GSEA.web).
