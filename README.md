# Mantis: Multi-Image Instruction Tuning

![Mantis](./docs/assets/images/overall_barchart.jpeg)
---


**Mantis** is a multimodal conversational AI model that can chat with users about images and text. It's optimized for multi-image reasoning, where inverleaved text and images can be used to generate responses.


- Check out our blog for more details: [Mantis: Interleaved Multi-Image Instruction Tuning](https://tiger-ai-lab.github.io/Blog/mantis)

- 🤗 Hugging face space Demo: [Mantis](https://huggingface.co/spaces/TIGER-Lab/Mantis)

- 🤗 Models: [TIGER-Lab/Mantis](https://huggingface.co/collections/TIGER-Lab/mantis-6619b0834594c878cdb1d6e4)

## Installation
```bash
conda create -n mantis python=3.9
conda activate mantis
pip install -e .
# install flash-attention
pip install flash-attn --no-build-isolation
```
## Inference

You can run inference with the following command:
```bash
cd examples
python run_mantis.py
```

Alternatively, you can run the following command to use the pure hugging face codes, without using the Mantis library:
```bash
python run_mantis_hf.py # with pure hugging face codes
```

## Training
**Training codes coming soon**


## Data
**Data coming soon**


Dongfu Jiang, Xuan He, Huaye Zeng, Cong Wei, Max Ku, Qian Liu, Wenhu Chen

## Citation
```bibtex
@misc{jiang2024mantis,
    title={Mantis: Interleaved Multi-Image Instruction Tuning},
    url={https://tiger-ai-lab.github.io/Blog/mantis},
    author={Jiang, Dongfu and He, Xuan and Zeng, Huaye and Wei, Cong and Max Ku and Liu, Qian and Chen, Wenhu},
    month={April},
    year={2024}
}
```