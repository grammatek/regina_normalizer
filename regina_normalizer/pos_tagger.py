
import pos
import torch


class POSTagger:

    tagger = None

    def __init__(self, device='cpu', repo='cadia-lvl/POS', pos_model='tag'):
        """
        Initialize the pos-tagger from LVL (https://github.com/cadia-lvl/POS).
        Any tagger can be used for the normalizer, as long as it uses the same tag-set as the LVL-tagger.

        :param device: cpu or gpu
        :param repo:
        :param pos_model: which model to use. 'tag' is a smaller (and faster) model than 'tag_large'. To follow
        new model developments, see the tagger repository
        """
        device = torch.device(device)
        POSTagger.tagger: pos.Tagger = torch.hub.load(
            repo_or_dir=repo,
            model=pos_model,
            device=device,
            force_reload=False,
            force_download=False,
        )

    @staticmethod
    def get_tagger():
        if POSTagger.tagger is None:
            POSTagger()
        return POSTagger.tagger