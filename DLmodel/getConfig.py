
from configparser import SafeConfigParser

def get_config(config_file='data/seq2seq.ini'):
    try:
        parser = SafeConfigParser()
        parser.read(config_file, encoding='utf-8')
        # get the ints, floats and strings
        _conf_ints = [ (key, int(value)) for key,value in parser.items('ints') ]
        #_conf_floats = [ (key, float(value)) for key,value in parser.items('floats') ]
        _conf_strings = [ (key, str(value)) for key,value in parser.items('strings') ]
        return dict(_conf_ints  + _conf_strings)
    except:
        gConfig = {
            'enc_vocab_size' : 20000,
            'dec_vocab_size' : 20000,
            'embedding_dim' : 128,
            'layer_size' : 256,
            'batch_size' : 128,
            'max_train_data_size' : 50000,
            'mode' : 'serve',
            'seq_data' : '../data/train_data/seq.data',
            'train_data' : '../data/train_data',
            'resource_data' : '../data/train_data/xiaohuangji50w_nofenci.conv',
            'e' : 'E',
            'm' : 'M',
            'model_data' : '../data/model_data'
        }
        return gConfig