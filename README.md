# pyrate
## About Me
Calculate HONO reaction rates and plot photostationary state

## Installation
```
git clone https://github.com/bhoover59/pyrate
```
```
pip install pyrate
```
```
import pyrate
```

## Usage
Uses the output of the F0AM v4.2.2 code written by Bode Hoover. Reaction rates and names are determined by the MATLAB script.

### plot_rates
1. Inputs
   - Column Name: data frame
   - Column Name: 
2. Outputs:
   - diurnal average
   - diurnal median
```
plot_rates(df = df_name)
```

### plot_stacked_rates
1. Inputs
   - Column Name: data frame
   - Column Name: 
2. Outputs:
   - diurnal average
   - diurnal median
## Calculate unknown
```
calculate_unknown(df = df)
```
