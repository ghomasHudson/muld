# MuLD: The Multitask Long Document Benchmark

MuLD (Multitask Long Document Benchmark) is a set of 6 NLP tasks 
where the inputs consist of at least 10,000 words. The benchmark covers a
 wide variety of task types including translation, summarization, 
question answering, and classification. Additionally there is a range of
 output lengths from a single word classification label all the way up 
to an output longer than the input text.

This repo contains official code for the paper [MuLD: The Multitask Long Document Benchmark](https://arxiv.org/abs/2202.07362).

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
## Manual Download
If you prefer to download the data files yourself:
- NarrativeQA [Train](https://drive.google.com/uc?export=download&confirm=yTib&id=1sUXIC6lmk9Khp2mnr9VZwQ-StDlHqTw1) [Val](https://drive.google.com/uc?&confirm=yTib&export=download&id=1xdXEhLHtcqOZh0FbPhY_dnvNMg2bALtm) [Test](https://drive.google.com/uc?confirm=yTib&export=download&id=1BPBXyfYWVGtOXVQv_hlqtvbT25rTQzGu)
- HotpotQA [Train](https://drive.google.com/uc?export=download&confirm=yTib&id=1OlGRyCEL9JhwIQIKViaWIXCOB_pwj8xU), [Val](https://drive.google.com/uc?export=download&confirm=yTib&id=1_Svtg6PycBpezDYJ78zcJqLa8Ohnk6Gq)
- Character Archetype Classification [Train](https://drive.google.com/uc?export=download&id=1Ckabmzbrunj2np2piAN5_ooZgTiK9K5i) [Val](https://drive.google.com/uc?export=download&id=1I0N8gKD39s0wKLrcAJ0P-4uYdPqzTONS) [Test](https://drive.google.com/uc?export=download&id=1_AI6whuHfD1p3BF7TvOnr8Fs_lOVdt8j)
- OpenSubtitles [Train](https://drive.google.com/uc?export=download&id=10QF5kL6nvWC4kHDieKx79K36RLdW1M1r&confirm=yTib) [Test](https://drive.google.com/uc?export=download&id=1KWPLYv2_7z_XIBWrWC3khXTNdPKhDF_X)
- Style Change [Train](https://drive.google.com/uc?export=download&id=1R29IQ_bFLw3_6DYLtP7YWFTGe7FQAevT&confirm=yTib) [Val](https://drive.google.com/uc?export=download&id=1B_RkTaMMOQXfJ7nDFCpq8GAth7yiW7vF) [Test](https://drive.google.com/uc?export=download&id=1-1eULJlV9nGrAwpdaEr5Ykchwfxn06kj)
- VLSP [Test](https://drive.google.com/uc?export=download&id=1ljTZZV5MpD07my2Vn1SVT3eQPKMVlHU5)

## Citation
If you use our benchmark please cite the paper:
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

Additionally please cite the datasets we used (particularly NarrativeQA, HotpotQA, and Opensubtitles where we directly use their data with limited filtering).

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
