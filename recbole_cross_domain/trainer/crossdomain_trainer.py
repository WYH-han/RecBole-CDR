# @Time   : 2022/3/12
# @Author : zihan Lin
# @Email  : zhlin@ruc.edu.cn


r"""
recbole_cross_domain.trainer.crossdomain_trainer
################################
"""

from recbole.trainer import Trainer


class CrossDomainTrainer(Trainer):
    r"""

    """

    def __init__(self, config, model):
        super(CrossDomainTrainer, self).__init__(config, model)