from niftynet.engine.application_driver import ApplicationDriver
from niftynet.io.misc_io import set_logger


class Namespace(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


system_param = {
    'APPLICATION': Namespace(
        action='train',
        num_threads=4,
        num_gpus=4,
        cuda_devices='',
        model_dir='./testing_data'),
    'NETWORK': Namespace(
        batch_size=20,
        name='niftynet.application.toy_application.TinyNet'),
    'TRAINING': Namespace(
        starting_iter=0,
        max_iter=50,
        save_every_n=0,
        tensorboard_every_n=1,
        max_checkpoints=20,
        optimiser='niftynet.engine.application_optimiser.Adagrad',
        lr=0.02),
    'CUSTOM': Namespace(
        vector_size=100,
        name='niftynet.application.toy_application.ToyApplication')
}
set_logger()
app_driver = ApplicationDriver()
app_driver.initialise_application(system_param, {})
app_driver.run_application()