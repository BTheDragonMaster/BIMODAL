from trainer import Trainer

for m in ['BIMODAL_random_512']:
    t = Trainer(m)
    t.single_run('../evaluation')
    # t.cross_validation('../evaluation')

