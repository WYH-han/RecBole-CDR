# @Time   : 2022/3/12
# @Author : zihan Lin
# @Email  : zhlin@ruc.edu.cn
# UPDATE
# @Time   : 2022/4/9
# @Author : Gaowei Zhang
# @email  : 1462034631@qq.com

r"""
recbole_cdr.trainer.trainer
################################
"""

import numpy as np
from recbole.trainer import Trainer
from recbole_cdr.utils import CrossDomainDataLoaderState


class CrossDomainTrainer(Trainer):
    r"""

    """

    def __init__(self, config, model):
        super(CrossDomainTrainer, self).__init__(config, model)
        self.train_args = config['train_args']
        self.config_step = config['eval_step']
        self.scheme_list = ['BOTH', 'SOURCE', 'TARGET', 'OVERLAP']
        self.state_list = [CrossDomainDataLoaderState.BOTH, CrossDomainDataLoaderState.SOURCE, CrossDomainDataLoaderState.TARGET, CrossDomainDataLoaderState.OVERLAP]
        self.scheme2state = {}
        for scheme, state in zip(self.scheme_list, self.state_list):
            self.scheme2state[scheme] = state

        self.train_scheme = []
        self.train_epochs = []
        self.split_valid_flag = False
        for train_arg in self.train_args:
            train_scheme, train_epoch = train_arg.split(':')
            self.train_scheme.append(train_scheme)
            self.train_epochs.append(train_epoch)
            if train_scheme == 'SOURCE':
                self.split_valid_flag = True

    def _reinit(self, phase):
        self.start_epoch = 0
        self.cur_step = 0
        self.best_valid_score = -np.inf if self.valid_metric_bigger else np.inf
        self.best_valid_result = None
        self.item_tensor = None
        self.tot_item_num = None
        self.train_loss_dict = dict()
        self.epochs = int(self.train_epochs[phase])
        self.eval_step = min(self.config_step, self.epochs)

    def fit(self, train_data, valid_data=None, verbose=True, saved=True, show_progress=False, callback_fn=None):
        for phase in range(len(self.train_scheme)):
            self._reinit(phase)
            scheme = self.train_scheme[phase]
            state = self.scheme2state[scheme]
            train_data.set_mode(state)
            self.model.set_phase(scheme)
            if self.split_valid_flag and valid_data is not None:
                source_valid_data, target_valid_data = valid_data
                if scheme == 'SOURCE':
                    super().fit(train_data, source_valid_data, verbose, saved, show_progress, callback_fn)
                else:
                    super().fit(train_data, target_valid_data, verbose, saved, show_progress, callback_fn)
            else:
                super().fit(train_data, valid_data, verbose, saved, show_progress, callback_fn)

        return self.best_valid_score, self.best_valid_result