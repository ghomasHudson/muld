# MuLD: The Multitask Long Document Benchmark

Official code for the paper [MuLD: The Multitask Long Document Benchmark](arxiv.org).

## Quickstart
The easiest method is to use the [Huggingface Datasets](https://github.com/huggingface/datasets) library:
```python
import datasets
ds = ds.load_dataset("ghomasHudson/muld", "narrativeqa")
```

## Citation
If you use our code please cite the paper
```
@misc{hudson2022muld,
      title={MuLD: The Multitask Long Document Benchmark}, 
      author={G. Thomas Hudson and Noura Al Moubayed},
      year={2022},
      eprint={},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
