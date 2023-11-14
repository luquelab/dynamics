# Folder description
## Main guideline
This folder contains the outputs expected from running the Colab notebook using the default inputs.

If you are a user testing the default values of the Colab, compare your outputs with the files contained here. If they match, you are good to go.

If the outputs do not match and there are no obvious errors, we recommend you [post an issue in the GitHub repository](https://github.com/luquelab/dynamics/issues) to let the developers know.

## Description of the files
+ `dynamics_model.json`: This file contains the simulated model in JSON format.
+ `model_fun.py`: This file contains the simulated model as a Python function.
+ `dynamics_output.png`: This file contains a plot grid with the dynamics of each dependent variable (columns) and the weights of each process (rows) directly impacting the rate of change of the dynamic variable.
