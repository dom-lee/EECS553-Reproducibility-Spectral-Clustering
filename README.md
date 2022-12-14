# EECS553 (ML) Reproducibility Project
This repository is for reproducibility project from EECS553 (Machine Leaning)
Course. We verified the paper "A Tighter Analysis of Spectral Clustering, and
Beyond", published in ICML 2022.

## Additional Experiments
1. **Less-separated Synthetic Dataset**:
- run `python experiments.py complete`
    - Change `r` value at https://github.com/dom-lee/EECS553-Reproducibility-Spectral-Clustering/blob/06541f4ec59481cefdc981144c0b80f75715a451/pysc/datasets.py#L395
    - Plot Results: run `python plot_results.py` in the folder https://github.com/dom-lee/EECS553-Reproducibility-Spectral-Clustering/tree/reproducibility/results/sbm

2. **Test on BSDS dataset with different parameters**:
- run `python experiments.py bsds`
    - We set break condition to cluster only 25 images
    - Change `variance` at https://github.com/dom-lee/EECS553-Reproducibility-Spectral-Clustering/blob/0ecdd24d48188c51d7a5d71b165d14e00f70e609/pysc/datasets.py#L114 

3. **Test on MNIST dataset with different parameters**:
- run `python experiments.py mnist`
    - Change parameter k to construct different K-NN graph
    https://github.com/dom-lee/EECS553-Reproducibility-Spectral-Clustering/blob/14495ab4c592ec1349e059b60f3e594dd612fda3/experiments.py#L94
    - Test different number of eigenvectors 
    https://github.com/dom-lee/EECS553-Reproducibility-Spectral-Clustering/blob/14495ab4c592ec1349e059b60f3e594dd612fda3/experiments.py#L108

4. **Check the performance of Spectral Clustering with fewer eigenvectors after
   reducing dimensionality through Sketching**
- check `sketch.py` for sketch algorithm
- **MNIST**
    - Uncomment https://github.com/dom-lee/EECS553-Reproducibility-Spectral-Clustering/blob/0ecdd24d48188c51d7a5d71b165d14e00f70e609/pysc/datasets.py#L195 
    - run `python experiments.py mnist`
- **USPS**
    - Uncomment https://github.com/dom-lee/EECS553-Reproducibility-Spectral-Clustering/blob/0ecdd24d48188c51d7a5d71b165d14e00f70e609/pysc/datasets.py#L285
    - run `python experiments.py usps`

5. **Visualize Graph** (Synthetic Dataset, MNIST, USPS)
- run `python plot_graph.py complete`
- run `python plot_graph.py mnist`
- run `python plot_graph.py usps`

<br/>
<br/>

# Original README
# Beyond Spectral Clustering
This directory contains the code to reproduce the results in the paper "A Tighter Analysis of Spectral Clustering, and Beyond", published in 
ICML 2022.

## Preparing your environment
Our code is primarily written in Python 3. There is also a matlab
script for analysing the results of the BSDS experiment.

We recommend running the python code inside a virtual environment.

To install the dependencies of the project, run

```bash
pip install -r requirements.txt
```

If you would like to run the experiments on the BSDS dataset, you should untar the data file
in the `data/bsds` directory. On Linux, this is done with the following commands.

```bash
cd data/bsds
tar -xvf BSR_bsds500.tgz
```

## Running the experiments
To run one of the experiments described in the paper, run

```bash
python experiment.py {experiment_name}
```

where ```{experiment_name}``` is one of `cycle`, `grid`, `mnist`, `usps`, or `bsds`.

The MNIST and USPS experiments will run easily on a laptop or desktop. The `cycle` and `grid` experiments will also run
on a personal computer but could take a few minutes since they must run multiple trials for each number of eigenvectors.

**Please note that the BSDS experiment is quite resource-intensive, and we recommend running on a compute server.**

You can instead choose to run the BSDS experiment on only one of the images from the dataset using the following command.

```bash
python experiment.py bsds {bsds_image_id}
```

For example:

```bash
python experiment bsds 176039
```

## Output
The output from the experiments will be in the `results` directory, under the appropriate experiment name.
The BSDS results can be analysed using the matlab script `analyseBsdsResults.m` which will call the
BSDS benchmarking code to evaluate the image segmentation output.

### Viewing the BSDS segmentations
While the `analyseBsdsResults` script will evaluate the BSDS segmentations, if you would like to view the
segmented images, you can use the provided MATLAB function `compareSegmentations`. This is the method used to generate
Figure 1 in the paper. For example:

```matlab
compareSegmentations("176039")
```

Note that the experiment must have been run for the image ID 176039 before running the MATLAB visualisation script.

## Image Segmentation
If you are primarily interested in the application of spectral clustering to image segmentation, you could take a look at
[this GitHub repository](https://github.com/pmacg/spectral-image-segmentation) which includes only the image segmentation code
from our project and provides a straightforward interface to segment any image file.

## Reference

```bibtex
@InProceedings{pmlr-v162-macgregor22a,
  title = 	 {A Tighter Analysis of Spectral Clustering, and Beyond},
  author =       {Macgregor, Peter and Sun, He},
  booktitle = 	 {Proceedings of the 39th International Conference on Machine Learning},
  pages = 	 {14717--14742},
  year = 	 {2022},
  volume = 	 {162},
  publisher =    {PMLR},
}
```
