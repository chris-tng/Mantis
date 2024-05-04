# Mantis: Multi-Image Instruction Tuning

![Mantis](./docs/assets/images/radar_chart.png)
<a target="_blank" href="https://arxiv.org/abs/2405.01483">
<img style="height:22pt" src="https://img.shields.io/badge/-Paper-black?style=flat&logo=arxiv"></a>
<a target="_blank" href="https://github.com/TIGER-AI-Lab/Mantis">
<img style="height:22pt" src="https://img.shields.io/badge/-Code-green?style=flat&logo=github"></a>
<a target="_blank" href="https://tiger-ai-lab.github.io/Mantis/">
<img style="height:22pt" src="https://img.shields.io/badge/-🌐%20Website-red?style=flat"> </a>
<a target="_blank" href="https://huggingface.co/datasets/TIGER-Lab/Mantis-Instruct">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Dataset-red?style=flat"></a>
<a target="_blank" href="https://huggingface.co/spaces/TIGER-Lab/Mantis">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Demo-red?style=flat"></a> 
<a target="_blank" href="https://huggingface.co/collections/TIGER-Lab/mantis-6619b0834594c878cdb1d6e4">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Models-red?style=flat"></a>
<a target="_blank" href="https://twitter.com/DongfuJiang/status/1786552974598078677">
<img style="height:22pt" src="https://img.shields.io/badge/-Tweet-blue?style=flat&logo=twitter"></a>
<br>

---

🤔 The recent years have witnessed a great array of large multimodal models (LMMs) to effectively solve single-image vision language tasks. However, their abilities to solve multi-image visual language tasks is yet to be improved.

😦 The existing multi-image LMMs (e.g. OpenFlamingo, Emu, Idefics, etc) mostly gain their multi-image ability through pre-training on hundreds of millions of noisy interleaved image-text data from web, which is neither efficient nor effective.

🔥 Therefore, we present Mantis, an LLaMA-3 based LMM with interleaved text and image as inputs, train on Mantis-Instruct under **academic-level** resources (i.e. 36 hours on 16xA100-40G). 

🚀 Mantis achieves state-of-the-art performance on 5 multi-image benchmarks (NLVR2, Q-Bench, BLINK, MVBench, Mantis-Eval), and maintaining a strong single-image performance on par with CogVLM and Emu2.

## 🔥News
- [2024-05-03] We have release our [training codes](./mantis/train/README.md), [dataset](https://huggingface.co/datasets/TIGER-Lab/Mantis-Instruct), [evaluation codes](./mantis/benchmark/README.md) codes to the community! Check the following sections for more details.
- [2024-05-02] We release the first multi-image abled LMM model Mantis-8B based on LLaMA3! Interact with Mantis-8B-SigLIP on [Hugging Face Spaces](https://huggingface.co/spaces/TIGER-Lab/Mantis) or [Colab Demo](./examples/run_mantis.py)
- [2024-05-02] Mantis's technical report is now available on [arXiv](https://arxiv.org/abs/2405.01483). Kudos to the team!

## Installation
```bash
conda create -n mantis python=3.9
conda activate mantis
pip install -e .
# install flash-attention
```
## Inference

You can run inference with the following command:
```bash
cd examples
python run_mantis.py
```

## Training
Install the requirements with the following command:
```bash
pip install -e[train,eval]
```

We support training of Mantis based on the Fuyu architecture and the LLaVA architecture. You can train the model with the following command:

**Training Mantis based on LLaMA3 with CLIP/SigLIP encoder:**
- Pretrain Mantis-LLaMA3 Multimodal projector on pretrain data (Stage 1):
```bash
cd mantis/train/pretrain_mllava.sh
```

- Fine-tune the pretrained Mantis-LLaMA3 on Mantis-Instruct (Stage 2):
```bash
cd mantis/train/train_mllava.sh
```

**Training Mantis based on Fuyu-8B:**
- Fine-tune Fuyu-8B on Mantis-Instruct to get Mantis-Fuyu:
```bash
cd mantis/train/train_fuyu.sh
```

## Evaluation
To reproduce our evaluation results, please check [mantis/benchmark/README.md](./mantis/benchmark/README.md)

## Data
- [🤗 Mantis-Instruct](https://huggingface.co/datasets/TIGER-Lab/Mantis-Instruct) 721K text-image interleaved datasets for multi-image instruction tuning
- [🤗 Mantis-Eval](https://huggingface.co/datasets/TIGER-Lab/Mantis-Eval) 217 high-quality examples for evaluating LMM's multi-image skills


## Model Zoo
We provide the following models in the 🤗 Hugging Face model hub:
- [TIGER-Lab/Mantis-8B-clip-llama3](https://huggingface.co/TIGER-Lab/Mantis-8B-clip-llama3)
- [TIGER-Lab/Mantis-8B-siglip-llama3](https://huggingface.co/TIGER-Lab/Mantis-8B-siglip-llama3)
- [https://huggingface.co/TIGER-Lab/Mantis-8B-Fuyu](https://huggingface.co/TIGER-Lab/Mantis-8B-Fuyu)

The following intermediate checkpoints after pre-training the multi-modal projectors are also available for experiments reproducibility (**Please note the follwing checkpoints still needs further fine-tuning on Mantis-Eval to be intelligent. They are not working models.**):
- [TIGER-Lab/Mantis-8B-clip-llama3-pretraind](https://huggingface.co/TIGER-Lab/Mantis-8B-clip-llama3-pretraind)
- [TIGER-Lab/Mantis-8B-siglip-llama3-pretraind](https://huggingface.co/TIGER-Lab/Mantis-8B-siglip-llama3-pretraind)



## Acknowledgement
- Thanks LLaVA and LLaVA-hf team for providing the LLaVA codebase, and hugging face compatibility!
- Thanks [Haoning Wu](https://teowu.github.io/) for providing codes of MVBench evaluation!


## Citation
```bibtex
@article{jiang2024mantis,
  title={MANTIS: Interleaved Multi-Image Instruction Tuning},
  author={Jiang, Dongfu and He, Xuan and Zeng, Huaye and Wei, Con and Ku, Max and Liu, Qian and Chen, Wenhu},
  journal={arXiv preprint arXiv:2405.01483},
  year={2024}
}
```
