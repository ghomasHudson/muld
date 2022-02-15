"""MuLD: The Multitask Long Document Benchmark"""

import json
import os
import datasets
import bz2

_CITATION = """\
@misc{hudson2022muld,
    title{MuLD: The Multitask Long Document Benchmark},
    author={G Thomas Hudson, Noura Al Moubayed}
    year={2022},
    eprint={TODO},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
Some of these datasets are directly based on existing datasets. Please cite these works.
"""

_DESCRIPTION = """\
MuLD: The Multitask Long Document Benchmark
A set of NLP tasks where each example is over 10,000 tokens long.
"""

_TASK_CONFIGS = {
    "NarrativeQA": {
        "description": """\
The NarrativeQA Reading Comprehension Challenge Dataset consists of user-submitted questions regarding the plot of movies or novels. Annotators were only given access to a human-written plot summary to encourage general questions which require a full understanding of the narrative. When these are given to a question-answering system along with the full text of the narrative (either a movie script or the novel text), this is a test of reading comprehension. As each sentence the annotator readcan summarise the plot of an entire chapter/scene of abook or movie, models evaluated on the full text must model the dependencies between multiple sections of the narrative. For MuLD, we filter any examples shorter than 10,000 words.
""",
        "citation": r"""\
@article{kovcisky2018narrativeqa,
  title={The narrativeqa reading comprehension challenge},
  author={Ko{\v{c}}isk{\'y}, Tom{\'a}{\v{s}} and Schwarz, Jonathan and Blunsom, Phil and Dyer, Chris and Hermann, Karl Moritz and Melis, G{\'a}bor and Grefenstette, Edward},
  journal={Transactions of the Association for Computational Linguistics},
  volume={6},
  pages={317--328},
  year={2018},
  publisher={MIT Press}
}""",
        "urls": {
            datasets.Split.TRAIN: "https://drive.google.com/uc?export=download&id=1sUXIC6lmk9Khp2mnr9VZwQ-StDlHqTw1",
            datasets.Split.VALIDATION: "https://drive.google.com/uc?export=download&id=1xdXEhLHtcqOZh0FbPhY_dnvNMg2bALtm",
            datasets.Split.TEST: "https://drive.google.com/uc?export=download&id=1BPBXyfYWVGtOXVQv_hlqtvbT25rTQzGu",
        }
},

    "HotpotQA": {
        "description": """\
The HotpotQA dataset consists of questions from crowd workers which require information from multiple Wikipedia articles in order to answer, thus testing the ability for models to perform multi-hop question answering. The data is commonly presented as a list of paragraphs containing relevant information plus a setting where the addition of 'distractor paragraphs' fully test the ability of the model to comprehend which information is relevant to the question asked. To transform this into a long document, we expand each paragraph with its full Wikipedia page as well as adding additional distractor articles from similar topics (randomly chosen from links on the existing pages) in order to meet the 10,000 token minimum length requirement for this benchmark. These articles are shuffled and concatenated to form the model input.""",
        "urls": {
            datasets.Split.TRAIN: "https://drive.google.com/uc?export=download&id=1OlGRyCEL9JhwIQIKViaWIXCOB_pwj8xU",
            datasets.Split.VALIDATION: "https://drive.google.com/uc?export=download&id=1_Svtg6PycBpezDYJ78zcJqLa8Ohnk6Gq"
        }
},

    "Character Archetype Classification": {
        "description": """\
The Character Archetype Classification dataset is based on the methodology of Skowron et al. (2016). For this dataset, each example consists of a movie script along with a named character and the task is to classify whether the character is a Hero/Protagonist or Villain/Antagonist based on understanding their role in the narrative.""",
        "urls": {
            datasets.Split.TRAIN: "https://drive.google.com/uc?export=download&id=1Ckabmzbrunj2np2piAN5_ooZgTiK9K5i",
            datasets.Split.VALIDATION: "https://drive.google.com/uc?export=download&id=1I0N8gKD39s0wKLrcAJ0P-4uYdPqzTONS",
            datasets.Split.TEST: "https://drive.google.com/uc?export=download&id=1_AI6whuHfD1p3BF7TvOnr8Fs_lOVdt8j",
        }
},

    "OpenSubtitles": {
        "description": """\
The Open Subtitles corpus (Lison et al., 2018) consists  of  aligned  subtitles from movies and TV shows from the website opensubtitles.org in 60 languages and can be used for machine translation. Importantly rather than individual lines,the data consists of the subtitles for an entire individ-ual movie or tv show, many of these being very long files and we filter to remove any document with less than 10,000 tokens.""",
        "citation": """\
@inproceedings{Lison_2018OpenSubtitles,
  title={OpenSubtitles2018: Statistical Rescoring of Sentence Alignments in Large, Noisy Parallel Corpora},
  author={Pierre Lison and J{\"o}rg Tiedemann and Milen Kouylekov},
  booktitle={LREC},
  year={2018}
}""",
        "urls": {
            datasets.Split.TRAIN: "https://drive.google.com/uc?export=download&id=10QF5kL6nvWC4kHDieKx79K36RLdW1M1r",
            datasets.Split.TEST: "https://drive.google.com/uc?export=download&id=1KWPLYv2_7z_XIBWrWC3khXTNdPKhDF_X"
        }
},

    "AO3 Style Change Detection": {
        "description": """\
Style change detection is the task of identifying the points where the author changes in a document constructed from the work of multiple authors. We use stories contributed to the fanfiction website Archive of Our Own, which contains a large number of works submitted by fans of popular films, tv, game, and book charactersmakicab10mw.
""",
        "urls": {
            datasets.Split.TRAIN: "https://drive.google.com/uc?export=download&id=1R29IQ_bFLw3_6DYLtP7YWFTGe7FQAevT",
            datasets.Split.VALIDATION: "https://drive.google.com/uc?export=download&id=1B_RkTaMMOQXfJ7nDFCpq8GAth7yiW7vF",
            datasets.Split.TEST: "https://drive.google.com/uc?export=download&id=1-1eULJlV9nGrAwpdaEr5Ykchwfxn06kj"
        }
    },

    "VLSP": {
        "description": """\
We follow the  process of the Scientific papers (Cohan  et  al.,2018) summarization  dataset, extracting papers from the open-access preprint server Arxiv.org using both the arxiv short abstract and the one included in the document (where available) as the reference summaries. In contrast to Cohan et al. (2018), rather than removing very long documents, we explicitly include them - removing any document with less than 10,000 tokens.""",
        "urls": {
            datasets.Split.TEST: "https://drive.google.com/uc?export=download&id=1ljTZZV5MpD07my2Vn1SVT3eQPKMVlHU5"
        }
    }
}

class MuldConfig(datasets.BuilderConfig):
    """BuilderConfig for MuLD."""
    def __init__(self, urls, citation, **kwargs):
        super(MuldConfig, self).__init__(version=datasets.Version("1.0.0"), **kwargs)
        self.features = datasets.Features({
            "input": datasets.Value("string"),
            "output": [datasets.Value("string")],
            "metadata": datasets.Value("string")
        })
        self.urls = urls
        self.citation = citation


class Muld(datasets.GeneratorBasedBuilder):
    """The MuLD benchmark."""
    BUILDER_CONFIGS = []
    for task_name in _TASK_CONFIGS:
        BUILDER_CONFIGS.append(
        MuldConfig(
            name=task_name,
            description=_TASK_CONFIGS[task_name]["description"],
            urls=_TASK_CONFIGS[task_name]["urls"],
            citation=_TASK_CONFIGS[task_name].get("citation", ""),
        ))
    DEFAULT_WRITER_BATCH_SIZE = 1000  # Large Dataset fix

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION + self.config.description,
            features=self.config.features,
            homepage="https://github.com/ghomasHudson/muld",
            citation=self.config.citation + "\n" + _CITATION,
        )

    def _split_generators(self, dl_manager):
        dl_dirs = dl_manager.download_and_extract(self.config.urls)
        splits = []
        for split in dl_dirs:
            splits.append(
                datasets.SplitGenerator(
                    name=split._name,
                    gen_kwargs={
                        "data_file": dl_dirs[split],
                        "split": split,
                    })
            )
        return splits

    def _generate_examples(self, data_file, split):
        with bz2.open(data_file) as f:
            for idx, line in enumerate(f):
                row = json.loads(line)
                if "metadata" not in row:
                    row["metadata"] = ""
                yield idx, row
