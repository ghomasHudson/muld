# MuLD: The Multitask Long Document Benchmark

Official code for the paper [MuLD: The Multitask Long Document Benchmark](https://arxiv.org/abs/2202.07362).

## Quickstart
The easiest method is to use the [Huggingface Datasets](https://github.com/huggingface/datasets) library:
```python
import datasets
ds = datasets.load_dataset("ghomasHudson/muld", "NarrativeQA")
ds = datasets.load_dataset("ghomasHudson/muld", "HotpotQA")
ds = datasets.load_dataset("ghomasHudson/muld", "Character Archetype Classification")
ds = datasets.load_dataset("ghomasHudson/muld", "OpenSubtitles")
ds = datasets.load_dataset("ghomasHudson/muld", "AO3 Style Change Detection")
ds = datasets.load_dataset("ghomasHudson/muld", "VLSP")
```
If you prefer to download the data files yourself, `muld.py` contains all the urls.

## Citation
If you use our code please cite the paper
```
@misc{hudson2022muld,
      title={MuLD: The Multitask Long Document Benchmark}, 
      author={G Thomas Hudson and Noura Al Moubayed},
      year={2022},
      eprint={2202.07362},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Dataset Metadata
The following table is necessary for this dataset to be indexed by search
engines such as <a href="https://g.co/datasetsearch">Google Dataset Search</a>.
<div itemscope itemtype="http://schema.org/Dataset">
<table>
  <tr>
    <th>property</th>
    <th>value</th>
  </tr>
  <tr>
    <td>name</td>
    <td><code itemprop="name">MuLD</code></td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td><code itemprop="alternateName">Multitask Long Document Benchmark</code></td>
  </tr>
  <tr>
    <td>url</td>
    <td><code itemprop="url">https://github.com/ghomasHudson/muld</code></td>
  </tr>
  <tr>
    <td>description</td>
    <td><code itemprop="description">MuLD (Multitask Long Document Benchmark) is a set of 6 NLP tasks 
where the inputs consist of at least 10,000 words. The benchmark covers a
 wide variety of task types including translation, summarization, 
question answering, and classification. Additionally there is a range of
 output lengths from a single word classification label all the way up 
to an output longer than the input text.</code></td>
  </tr>
  <tr>
    <td>citation</td>
    <td><code itemprop="citation">https://arxiv.org/abs/2202.07362</code></td>
  </tr>
    
  <tr>
    <td>creator</td>
    <td>
      <div itemscope itemtype="http://schema.org/Person" itemprop="creator">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td><code itemprop="name">Thomas Hudson</code></td>
          </tr>
          <tr>
            <td>sameAs</td>
            <td><code itemprop="sameAs">https://orcid.org/0000-0003-3562-3593</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
</table>
</div>
